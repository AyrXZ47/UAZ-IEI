#!/usr/bin/env python3
"""RTL-SDR en vivo: espectro + cascada + audio FM en tiempo real (sin guardar archivos).

Antes de usarlo hay que liberar el driver DVB del kernel (una vez):
    sudo modprobe -r dvb_usb_rtl28xxu

Uso:
    python3 rtl_sdr_live.py -f 106.5e6                 # escucha/ve FM comercial
    python3 rtl_sdr_live.py -f 106.5e6 --no-plot      # solo audio (lo mas estable)
    python3 rtl_sdr_live.py -f 106.5e6 --no-audio     # solo espectro y cascada
    python3 rtl_sdr_live.py --selftest                # verifica la matematica sin antena
"""
import argparse
import subprocess
import sys
import threading
import time

import numpy as np

AUDIO_RATE = 48000
WBFM_MAX_DEV = 75e3
DEEMPH_TAU = 75e-6


def fm_demod(x):
    return np.angle(x[1:] * np.conj(x[:-1]))


def decimate(d, dec):
    k = (d.size // dec) * dec
    return d[:k].reshape(-1, dec).mean(axis=1)


def make_audio(dec, gain, deemph):
    from scipy.signal import lfilter

    state = np.zeros(1)
    b = 1.0 - deemph

    def proc(demod):
        nonlocal state
        a = decimate(demod, dec) * gain
        # ponytail: de-enfasis de un polo (75us, America), mono sin estereo.
        # Suficiente para escuchar; para calidad FM completa falta piloto 19k + L-R.
        a, state = lfilter([b], [1.0, -deemph], a, zi=state)
        return (np.clip(a, -1.0, 1.0) * 32767).astype(np.int16)

    return proc


def selftest():
    fs, f, n = AUDIO_RATE, 1000.0, AUDIO_RATE
    x = np.exp(2j * np.pi * f * np.arange(n) / fs)
    got = np.mean(fm_demod(x)) * fs / (2 * np.pi)
    assert abs(got - f) < 1.0, (got, f)
    assert decimate(np.arange(8.0), 4).tolist() == [1.5, 5.5]
    a = make_audio(1, 1.0, 0.5)(np.full(1000, 0.5))
    assert a.dtype == np.int16 and a.size == 1000, (a.dtype, a.size)
    print("selftest OK")


def parse_gain(v):
    return "auto" if v == "auto" else float(v)


def run(args):
    from rtlsdr import RtlSdr
    try:
        sdr = RtlSdr()
    except Exception as e:
        print("No se pudo abrir el SDR:", e, file=sys.stderr)
        print("Reconecta el dongle y libera el driver:  sudo modprobe -r dvb_usb_rtl28xxu",
              file=sys.stderr)
        return 1
    sdr.sample_rate = args.rate
    sdr.center_freq = args.freq
    if args.ppm:
        sdr.freq_correction = int(args.ppm)
    sdr.gain = args.gain

    dec = max(1, int(round(args.rate / AUDIO_RATE)))
    arate = args.rate / dec
    deemph = np.exp(-1.0 / (arate * DEEMPH_TAU))
    gain = 0.7 * args.rate / (2 * np.pi * WBFM_MAX_DEV)

    player = None
    audio = None
    if not args.no_audio:
        player = subprocess.Popen(
            ["pw-cat", "-p", "-a", "--format", "s16",
             "--rate", str(int(round(arate))), "--channels", "1", "-"],
            stdin=subprocess.PIPE)
        audio = make_audio(dec, gain, deemph)

    latest = {"x": None}
    lock = threading.Lock()
    stop = threading.Event()

    def capture():
        while not stop.is_set():
            x = sdr.read_samples(args.block)
            with lock:
                latest["x"] = x
            if audio is not None:
                try:
                    player.stdin.write(audio(fm_demod(x)).tobytes())
                except (BrokenPipeError, ValueError):
                    return

    th = threading.Thread(target=capture, daemon=True)
    th.start()

    try:
        if args.no_plot:
            print("Audio en vivo (sin grafica). Ctrl+C para salir.")
            while th.is_alive():
                time.sleep(0.5)
        else:
            import matplotlib.pyplot as plt
            from scipy import signal as sig

            fq, _ = sig.welch(np.zeros(args.block, np.complex64), fs=args.rate,
                              nperseg=args.bins, return_onesided=False)
            fq = np.fft.fftshift(fq) / 1e6

            plt.ion()
            fig, (ax_s, ax_w) = plt.subplots(2, 1, num="RTL-SDR en vivo", figsize=(9, 6))
            line, = ax_s.plot(fq, np.full(fq.size, np.nan), lw=0.8)
            ax_s.set_title(f"Espectro @ {args.freq/1e6:.3f} MHz  (span {args.rate/1e6:.2f} MHz)")
            ax_s.set_ylabel("dB")
            ax_s.set_ylim(-80, 5)
            ax_s.grid(alpha=0.3)

            wf = np.full((args.history, fq.size), np.nan)
            img = ax_w.imshow(wf, aspect="auto", origin="lower", cmap="viridis",
                              extent=[fq[0], fq[-1], 0, args.history], vmin=-60, vmax=0)
            ax_w.set_xlabel("Frecuencia (MHz)")
            ax_w.set_ylabel("Cascada (tiempo)")
            fig.tight_layout()

            while plt.fignum_exists(fig.number):
                with lock:
                    x = latest["x"]
                if x is None:
                    plt.pause(0.02)
                    continue
                _, P = sig.welch(x, fs=args.rate, nperseg=args.bins, return_onesided=False)
                pdb = 10 * np.log10(np.fft.fftshift(P) + 1e-12)
                line.set_ydata(pdb)
                wf[:-1] = wf[1:]
                wf[-1] = pdb
                img.set_data(wf)
                plt.pause(0.001)
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        th.join(timeout=2)
        sdr.close()
        if player is not None:
            player.stdin.close()
            player.terminate()


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=106.5e6, help="frecuencia central (Hz)")
    p.add_argument("-r", "--rate", type=float, default=2.4e6, help="sample rate / ancho de banda (Hz)")
    p.add_argument("-g", "--gain", type=parse_gain, default="auto", help="ganancia dB o 'auto'")
    p.add_argument("--ppm", type=float, default=0.0, help="correccion de frecuencia en ppm")
    p.add_argument("--block", type=int, default=16384, help="muestras por bloque")
    p.add_argument("--bins", type=int, default=1024, help="bins del FFT")
    p.add_argument("--history", type=int, default=200, help="filas de la cascada")
    p.add_argument("--no-audio", action="store_true")
    p.add_argument("--no-plot", action="store_true")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()
    if args.selftest:
        selftest()
        return 0
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
