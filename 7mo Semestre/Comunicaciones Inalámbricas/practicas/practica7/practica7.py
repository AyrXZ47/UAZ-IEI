#!/usr/bin/env python3
"""Practica 7. Estimacion experimental de la capacidad de canal (Shannon-Hartley).

Una sola ventana en vivo: espectro y cascada del canal, la curva de Shannon con
la posicion de cada escenario medido y las potencias de senal y ruido por
escenario, todo actualizandose en tiempo real.  Por cada escenario (LOS,
interior con obstaculos, distancia maxima) se toma la senal en la frecuencia de
interes y el ruido en un canal cercano vacio, se estima Ps, Pn y la SNR y se
calcula la capacidad C = B*log2(1+SNR).

Procedimiento:
    1. Ubica la antena en el escenario y pulsalo con 1, 2 o 3.
    2. Pulsa ESPACIO para medir: senal en la frecuencia y ruido en el canal vecino.
    3. Repite con los otros escenarios y observa su punto sobre la curva.
    4. Pulsa s para guardar figuras y JSON del reporte.

Uso:
    python3 practica7.py                       # 433.9 MHz, ruido a +1 MHz
    python3 practica7.py --escenarios LOS,NLOS,interior -B 100e3
    python3 practica7.py --sim                 # demo automatica, sin dongle
    python3 practica7.py --selftest            # verifica el estimador sin dongle
Teclas:  1..3 escenario   ESPACIO medir   r reiniciar   s guardar   q salir
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun  # noqa: E402
import vivo  # noqa: E402

DIR = Path(__file__).resolve().parent
FIGS, DATOS = DIR / "figs", DIR / "datos"

SNR_SIM_DB = {"LOS": 20.0, "NLOS": 12.0, "lejano": 5.0}


def potencia_media(x):
    """Ps = mean(abs(data).^2) del manual."""
    return float(np.mean(np.abs(x) ** 2))


def estimar(x, x_ruido, B):
    """Ps, Pn, SNR y capacidad de Shannon a partir de una captura y ruido."""
    Ps, Pn = potencia_media(x), potencia_media(x_ruido)
    snr = Ps / Pn
    C = B * np.log2(1 + snr)
    return {"Ps_dB": 10 * np.log10(Ps), "Pn_dB": 10 * np.log10(Pn),
            "SNR_dB": 10 * np.log10(snr), "C_bps": float(C), "C_kbps": float(C / 1e3)}


def captura_sim(n, snr_db, seed=0):
    """BPSK de potencia unitaria + ruido complejo gaussiano y captura de solo ruido."""
    rng = np.random.default_rng(seed)
    s = (2.0 * rng.integers(0, 2, n) - 1.0).astype(np.complex64)
    escala = np.float32(np.sqrt(10 ** (-snr_db / 10) / 2))
    ruido = lambda: (rng.standard_normal(n) + 1j * rng.standard_normal(n)).astype(np.complex64) * escala
    return (s + ruido()).astype(np.complex64), ruido()


def fig_shannon(resultados, B, ruta):
    import matplotlib.pyplot as plt

    snr_db = np.linspace(-10, 30, 401)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(snr_db, np.log2(1 + 10 ** (snr_db / 10)), lw=2, label="Curva teórica")
    for esc, r in resultados.items():
        c_bhz = r["C_bps"] / B
        ax.plot([r["SNR_dB"]] * 2, [0, c_bhz], "--", lw=1)
        ax.plot(r["SNR_dB"], c_bhz, "o",
                label=f"{esc}: {r['SNR_dB']:.1f} dB, {r['C_kbps']:.1f} kbps")
    ax.set_xlabel("SNR (dB)")
    ax.set_ylabel("Capacidad espectral C/B (bps/Hz)")
    ax.set_title("Capacidad de Shannon por escenario")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    return comun.guardar_fig(fig, ruta, False)


def fig_potencias(resultados, ruta):
    import matplotlib.pyplot as plt

    escs = list(resultados)
    pos = np.arange(len(escs))
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(pos - 0.2, [resultados[e]["Ps_dB"] for e in escs], 0.4, label="Señal (Ps)")
    ax.bar(pos + 0.2, [resultados[e]["Pn_dB"] for e in escs], 0.4, label="Ruido (Pn)")
    ax.set_xticks(pos, escs)
    ax.set_ylabel("Potencia (dB)")
    ax.set_title("Potencia de señal y ruido por escenario")
    ax.grid(alpha=0.3, axis="y")
    ax.legend()
    return comun.guardar_fig(fig, ruta, False)


def reporte(resultados):
    filas = [(esc, f"{r['Ps_dB']:.2f}", f"{r['Pn_dB']:.2f}",
              f"{r['SNR_dB']:.2f}", f"{r['C_kbps']:.2f}")
             for esc, r in resultados.items()]
    print(comun.tabla_markdown(
        ["Escenario", "Potencia señal (dB)", "Potencia ruido (dB)", "SNR (dB)", "Capacidad (kbps)"],
        filas))
    for esc, r in resultados.items():
        print(f"{esc}: C = {r['C_kbps']:.2f} kbps = {r['C_bps'] / 1e6:.4f} Mbps")


class P7(vivo.Practica):
    titulo = "Practica 7 - capacidad de canal (Shannon)"
    filas = 2
    alto = [2.0, 1.3, 2.0, 1.7]

    def __init__(self, args):
        super().__init__(args)
        self.escs = [e.strip() for e in args.escenarios.split(",") if e.strip()]
        if not self.escs:
            raise SystemExit("--escenarios vacio")
        self.sel = 0
        self.res = {}
        self.snr_vivo = None
        self.ax_sh = self.ax_pot = None
        self.l_marca = {}
        self._demo = 0

    # -- paneles ---------------------------------------------------------
    def ejes(self, fig, gs, inicio):
        self.ax_sh = fig.add_subplot(gs[inicio])
        self.ax_sh.set_title("Curva de Shannon y escenarios medidos",
                             fontsize=9, loc="left")
        self.ax_sh.set_xlabel("SNR (dB)")
        self.ax_sh.set_ylabel("C/B (bps/Hz)")
        self.ax_sh.set_xlim(-10, 30)
        self.ax_sh.set_ylim(0, 11)
        self.ax_sh.grid(alpha=0.25)
        snr_db = np.linspace(-10, 30, 401)
        self.ax_sh.plot(snr_db, np.log2(1 + 10 ** (snr_db / 10)), lw=1.6,
                        color="#00e5ff", label="Teórica")
        for esc in self.escs:                    # un marcador por escenario, nunca por frame
            linea, = self.ax_sh.plot([], [], "o", ms=8, label=esc)
            self.l_marca[esc] = linea
        self.ax_sh.legend(fontsize=7, loc="upper left")

        self.ax_pot = fig.add_subplot(gs[inicio + 1])
        self.ax_pot.set_title("Potencia de señal y ruido por escenario",
                              fontsize=9, loc="left")
        self.ax_pot.set_xlabel("Escenario")
        self.ax_pot.set_ylabel("Potencia (dB)")
        self.ax_pot.grid(alpha=0.25)
        self.ax_pot.set_xticks(np.arange(len(self.escs)), self.escs)
        self.ax_pot.set_xlim(-0.5, len(self.escs) - 0.5)
        self.l_ps, = self.ax_pot.plot([], [], "o-", ms=6, lw=1.2, label="Señal (Ps)")
        self.l_pn, = self.ax_pot.plot([], [], "s--", ms=6, lw=1.2, label="Ruido (Pn)")
        self.ax_pot.legend(fontsize=7, loc="upper right")
        return [self.ax_sh, self.ax_pot]

    # -- estado y repintado ----------------------------------------------
    def _estado(self):
        canal = (f"canal {self.snr_vivo:5.1f} dB" if self.snr_vivo is not None
                 else "canal --")
        med = "   ".join(f"{e}: {r['SNR_dB']:.1f} dB, {r['C_kbps']:.1f} kbps"
                         for e, r in self.res.items())
        self.estado = f"| {canal}   {med}".rstrip()

    def _acomodar(self):
        """Vuelca las mediciones en los paneles (solo cuando cambian)."""
        idx = np.arange(len(self.escs))
        faltan = np.nan
        for esc in self.escs:
            r = self.res.get(esc)
            if r:
                self.l_marca[esc].set_data([r["SNR_dB"]], [r["C_bps"] / self.args.banda])
            else:
                self.l_marca[esc].set_data([], [])
        ps = np.array([self.res[e]["Ps_dB"] if e in self.res else faltan for e in self.escs])
        pn = np.array([self.res[e]["Pn_dB"] if e in self.res else faltan for e in self.escs])
        self.l_ps.set_data(idx, ps)
        self.l_pn.set_data(idx, pn)
        if self.res:
            vals = np.concatenate([ps, pn])
            vals = vals[np.isfinite(vals)]
            self.ax_pot.set_ylim(vals.min() - 6, vals.max() + 6)
        self._estado()
        if self.app is not None:
            self.app.reencuadrar()

    # -- mediciones ------------------------------------------------------
    def _registrar(self, x, x_noise):
        self.res[self.escs[self.sel]] = estimar(x, x_noise, self.args.banda)
        self._acomodar()

    def _medir_real(self):
        """Senal en la frecuencia sintonizada y ruido en el canal vecino."""
        fuente = self.app.fuente
        x = fuente.ultimo
        try:
            fuente.sintonizar(self.freq + self.args.fnoise)
            x_noise = self.nuevo_bloque()
        finally:
            fuente.sintonizar(self.freq)          # la ventana sigue mirando la senal
        if x is None or x_noise is None:
            print("sin muestras: no se pudo medir")
            return
        self._registrar(x, x_noise)

    # -- lazo ------------------------------------------------------------
    def actualizar(self, x, fs, t):
        n = min(4096, x.size)
        P = np.abs(np.fft.fftshift(np.fft.fft(x[:n]))) ** 2 / n
        pn = float(np.median(P))                  # piso de ruido por bin = potencia total
        ps = max(float(np.mean(np.abs(x) ** 2)) - pn, 1e-12)
        self.snr_vivo = 10 * np.log10(ps / max(pn, 1e-12))

        if self.args.sim and self.cada(1.5):       # demo: recorre los escenarios
            esc = self.escs[self.sel]
            self._registrar(*captura_sim(1 << 16, SNR_SIM_DB.get(esc, 10.0),
                                         seed=self._demo))
            self._demo += 1
            self.sel = (self.sel + 1) % len(self.escs)
        self._estado()

    def tecla(self, ev):
        k = ev.key or ""
        if k.isdigit() and 1 <= int(k) <= len(self.escs):
            self.sel = int(k) - 1
            self._estado()
        elif k == " ":
            if self.args.sim:
                esc = self.escs[self.sel]
                self._registrar(*captura_sim(1 << 16, SNR_SIM_DB.get(esc, 10.0),
                                             seed=self._demo))
                self._demo += 1
                self.sel = (self.sel + 1) % len(self.escs)
            else:
                self._medir_real()
        elif k in ("r", "R"):
            self.res = {}
            self._acomodar()

    def ayuda(self):
        return f"1..{len(self.escs)} escenario   ESPACIO medir   r reiniciar"

    # -- entregables -----------------------------------------------------
    def guardar(self):
        if not self.res:
            print("faltan mediciones: pulsa ESPACIO en cada escenario")
            return []
        reporte(self.res)
        rutas = [fig_shannon(self.res, self.args.banda, FIGS / "shannon.png"),
                 fig_potencias(self.res, FIGS / "potencias.png")]
        rutas.append(comun.guardar_json(
            DATOS / "resultados.json", frecuencia_Hz=self.freq,
            offset_ruido_Hz=self.args.fnoise, banda_Hz=self.args.banda,
            modo="sim" if self.args.sim else "real", escenarios=self.res))
        return rutas


def selftest():
    x, xr = captura_sim(1 << 18, 15.0, seed=7)
    est = estimar(x, xr, 200e3)
    assert abs(est["SNR_dB"] - 15.0) < 1.5, est["SNR_dB"]
    print("practica7 selftest OK")


def main(argv=None):
    args = vivo.parser(
        __doc__, freq=433.9e6,
        mas=[("--fnoise", dict(type=float, default=1e6,
                               help="offset del canal de ruido (Hz)")),
             ("--escenarios", dict(default="LOS,NLOS,lejano",
                                   help="escenarios separados por coma")),
             (("-B", "--banda"), dict(type=float, default=200e3,
                                      help="ancho de banda del canal (Hz)")),
             ("--selftest", dict(action="store_true"))]).parse_args(argv)
    if args.selftest:
        selftest()
        return 0
    return vivo.correr(P7(args), args)


if __name__ == "__main__":
    sys.exit(main())
