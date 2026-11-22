#!/usr/bin/env python3
"""RTL-SDR en vivo: espectro + cascada + audio FM en tiempo real (sin guardar archivos).

Antes de usarlo hay que liberar el driver DVB del kernel (una vez):
    sudo modprobe -r dvb_usb_rtl28xxu

Uso:
    python3 rtl_sdr_live.py -f 106.5e6                  # escucha/ve FM comercial
    python3 rtl_sdr_live.py -f 106.5e6 --no-plot       # solo audio (lo mas estable)
    python3 rtl_sdr_live.py -f 106.5e6 --no-audio      # solo espectro y cascada
    python3 rtl_sdr_live.py --selftest                # verifica la matematica sin antena

Notas:
    - La ganancia por defecto NO es "auto": el AGC del R820T de este dongle
      satura el ADC (RMS ~0.9) y el audio sale como ruido.  Con "auto" el script
      elige la ganancia fija mas alta que no recorta el ADC.
    - El filtro IF del tuner se estrecha a 0.6 MHz por defecto (-b): a 2.4 MHz
      de span el R820T deja pasar demasiado ruido y el audio pierde ~6 dB.
      Usa -b 2.4e6 si quieres ver todo el ancho en el espectro.
    - El audio se decodifica en mono, con de-enfasis de 75 us (America).
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
CHANNEL_RATE = 240e3
CHANNEL_BW = 100e3


def fm_demod(x):
    return np.angle(x[1:] * np.conj(x[:-1]))


def bytes_to_iq(raw):
    a = np.frombuffer(raw, dtype=np.uint8).astype(np.float32)
    iq = a.view(np.complex64)
    iq *= np.float32(1.0 / 127.5)
    iq -= np.complex64(1.0 + 1.0j)
    return iq


def make_channelizer(fs, dec):
    """Filtro de canal +-100 kHz y diezmado a ~240 kHz (con estado entre bloques)."""
    from scipy.signal import firwin, lfilter

    taps = firwin(121, CHANNEL_BW, fs=fs, window=("kaiser", 6.0))
    zi = np.zeros(taps.size - 1, np.complex64)

    def proc(x):
        nonlocal zi
        y, zi = lfilter(taps, 1.0, x, zi=zi)
        return y[::dec]

    return proc


def make_audio(fs, dec):
    """Diezma el discriminador a 48 kHz con filtro anti-alias + de-enfasis."""
    from scipy.signal import firwin, lfilter

    out_rate = fs / dec
    taps = firwin(129, 15e3, fs=fs)
    zi = np.zeros(taps.size - 1)
    deemph = np.exp(-1.0 / (out_rate * DEEMPH_TAU))
    b = 1.0 - deemph
    gain = 0.7 * fs / (2 * np.pi * WBFM_MAX_DEV)
    state = np.zeros(1)

    def proc(demod):
        nonlocal zi, state
        a, zi = lfilter(taps, 1.0, demod, zi=zi)
        a = a[::dec] * gain
        a, state = lfilter([b], [1.0, -deemph], a, zi=state)
        return (np.clip(a, -1.0, 1.0) * 32767).astype(np.int16)

    return proc, out_rate


def selftest():
    fs, fm, dev = 2.4e6, 1000.0, 75e3
    t = np.arange(int(fs)) / fs
    x = np.exp(2j * np.pi * (100e3 * t + dev / fm * np.sin(2 * np.pi * fm * t)))
    x = x.astype(np.complex64)
    ch = make_channelizer(fs, 10)(x)
    proc, out_rate = make_audio(240e3, 5)
    a = proc(fm_demod(ch)).astype(np.float32) / 32767
    F = np.abs(np.fft.rfft(a * np.hanning(a.size)))
    fr = np.fft.rfftfreq(a.size, 1 / out_rate)
    peak = fr[np.argmax(F)]
    assert abs(peak - fm) < 20, (peak, fm)
    assert 0.05 < np.sqrt(np.mean(a ** 2)) < 1.0, np.sqrt(np.mean(a ** 2))
    y = np.exp(2j * np.pi * 1000 * np.arange(48000) / 48000)
    got = np.mean(fm_demod(y)) * 48000 / (2 * np.pi)
    assert abs(got - 1000) < 1, got
    assert bytes_to_iq(np.array([255, 255, 0, 0], np.uint8)).tolist() == [1.0 + 1.0j, -1.0 - 1.0j]
    print("selftest OK")


def parse_gain(v):
    return "auto" if v == "auto" else float(v)


def pick_gain(sdr, gain):
    """Ganancia fija.  Con 'auto' baja desde la mas alta hasta que el ADC no recorte."""
    if gain != "auto":
        sdr.gain = gain
        return
    gains = sorted((g for g in sdr.valid_gains_db if g > 0), reverse=True)
    for g in gains:
        sdr.gain = g
        x = sdr.read_samples(65536)
        clip = np.mean((np.abs(x.real) > 0.98) | (np.abs(x.imag) > 0.98))
        if clip < 0.001:
            break
    print(f"ganancia fija elegida: {sdr.get_gain()} dB", file=sys.stderr)


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
    if args.bw:
        try:
            sdr.set_bandwidth(args.bw)
        except Exception as e:
            print("aviso: no se pudo fijar el filtro IF del tuner:", e, file=sys.stderr)
    pick_gain(sdr, args.gain)

    fs = sdr.get_sample_rate()
    cdec = max(1, int(round(fs / CHANNEL_RATE)))
    channelize = make_channelizer(fs, cdec)
    audio = out_rate = None
    if not args.no_audio:
        adec = max(1, int(round(fs / cdec / AUDIO_RATE)))
        audio, out_rate = make_audio(fs / cdec, adec)

    player = None
    if audio is not None:
        player = subprocess.Popen(
            ["pw-cat", "-p", "-a", "--format", "s16",
             "--rate", str(int(round(out_rate))), "--channels", "1",
             "--latency", "200ms", "-"],
            stdin=subprocess.PIPE)

    latest = {"x": None}
    lock = threading.Lock()
    stop = threading.Event()

    def on_block(raw, ctx):
        x = bytes_to_iq(raw)
        if audio is not None:
            try:
                player.stdin.write(audio(fm_demod(channelize(x))).tobytes())
            except (BrokenPipeError, ValueError):
                pass
        with lock:
            latest["x"] = x

    def capture():
        try:
            sdr.read_bytes_async(on_block, 2 * args.block)
        except Exception:
            if not stop.is_set():
                raise

    th = threading.Thread(target=capture, daemon=True)
    th.start()

    try:
        if args.no_plot:
            print("Audio en vivo (sin grafica). Ctrl+C para salir.", file=sys.stderr)
            while th.is_alive():
                time.sleep(0.5)
        else:
            import matplotlib.pyplot as plt
            from scipy import signal as sig

            fq, _ = sig.welch(np.zeros(args.block, np.complex64), fs=fs,
                              nperseg=args.bins, return_onesided=False)
            fq = np.fft.fftshift(fq) / 1e6

            plt.ion()
            fig, (ax_s, ax_w) = plt.subplots(2, 1, num="RTL-SDR en vivo", figsize=(9, 6))
            line, = ax_s.plot(fq, np.full(fq.size, np.nan), lw=0.8)
            ax_s.set_title(f"Espectro @ {args.freq/1e6:.3f} MHz  (span {fs/1e6:.2f} MHz)")
            ax_s.set_ylabel("dB")
            ax_s.set_ylim(-80, 5)
            ax_s.grid(alpha=0.3)

            wf = np.full((args.history, fq.size), np.nan)
            img = ax_w.imshow(wf, aspect="auto", origin="lower", cmap="viridis",
                              extent=[fq[0], fq[-1], 0, args.history], vmin=-60, vmax=0)
            ax_w.set_xlabel("Frecuencia (MHz)")
            ax_w.set_ylabel("Cascada (tiempo)")
            fig.tight_layout()
            fig.canvas.draw()
            bg = fig.canvas.copy_from_bbox(fig.bbox)
            size = fig.canvas.get_width_height()
            last = 0.0

            while plt.fignum_exists(fig.number):
                now = time.monotonic()
                if now - last < 0.1:
                    fig.canvas.flush_events()
                    time.sleep(0.01)
                    continue
                with lock:
                    x = latest["x"]
                if x is None:
                    time.sleep(0.01)
                    continue
                _, P = sig.welch(x, fs=fs, nperseg=args.bins, return_onesided=False)
                pdb = 10 * np.log10(np.fft.fftshift(P) + 1e-12)
                line.set_ydata(pdb)
                wf[:-1] = wf[1:]
                wf[-1] = pdb
                img.set_data(wf)
                if fig.canvas.get_width_height() != size:
                    fig.canvas.draw()
                    bg = fig.canvas.copy_from_bbox(fig.bbox)
                    size = fig.canvas.get_width_height()
                fig.canvas.restore_region(bg)
                ax_s.draw_artist(line)
                ax_w.draw_artist(img)
                fig.canvas.blit(fig.bbox)
                fig.canvas.flush_events()
                last = time.monotonic()
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        sdr.cancel_read_async()
        th.join(timeout=2)
        sdr.close()
        if player is not None:
            try:
                player.stdin.close()
            except (BrokenPipeError, ValueError):
                pass
            player.terminate()


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-f", "--freq", type=float, default=106.5e6, help="frecuencia central (Hz)")
    p.add_argument("-r", "--rate", type=float, default=2.4e6, help="sample rate / ancho de banda (Hz)")
    p.add_argument("-g", "--gain", type=parse_gain, default="auto", help="ganancia dB o 'auto'")
    p.add_argument("-b", "--bw", type=float, default=0.6e6,
                   help="ancho del filtro IF del tuner (Hz, 0 = no tocar; 0.6e6 mejora el audio)")
    p.add_argument("--ppm", type=float, default=0.0, help="correccion de frecuencia en ppm")
    p.add_argument("--block", type=int, default=131072, help="muestras por bloque de lectura")
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
