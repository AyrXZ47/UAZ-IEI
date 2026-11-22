#!/usr/bin/env python3
"""Convierte cada practicas/practicaN/reporte.md en main.tex + main.pdf.

Cada PDF lleva portada UAZ con los datos del curso y el contenido del reporte
(tablas, formulas, figuras, codigo y cuestionario ya resueltos).

Uso:
    python3 a_pdf.py            # las 8 practicas
    python3 a_pdf.py practica1  # solo una
"""
import re
import subprocess
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent
ASSETS = DIR.parents[2] / "Assets"
DOCENTE = "Dr. Víktor Iván Rodríguez Abdalá"
ALUMNO = "Arnold Yovick Ríos Zaldívar"
MATERIA = "Comunicaciones Inalámbricas"
FECHA = "Octubre de 2026"

UNI = {"\u2013": "--", "\u2014": "---", "\u2248": r"$\approx$", "\u2264": r"$\leq$",
       "\u2265": r"$\geq$", "\u00d7": r"$\times$", "\u00b1": r"$\pm$", "\u00b5": r"$\mu$",
       "\u2192": r"$\rightarrow$", "\u00b0": r"$^\circ$", "\u201c": "``", "\u201d": "''",
       "\u2018": "`", "\u2019": "'", "\u00a0": "~", "\u2212": "$-$",
       "\u03c3": r"$\sigma$", "\u00b2": "$^2$", "\u00b7": r"\textperiodcentered{}",
       "\u00aa": r"\textsuperscript{a}"}
ESC = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_",
       "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}

ESP = re.compile(r"^(#{1,4})\s+(.*)$")
LI = re.compile(r"^([-*]|\d+\.)\s+(.*)$")
IMG = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)$")


def uni(t):
    return "".join(UNI.get(c, c) for c in t)


def esc(t):
    """Escapa LaTeX y traduce los simbolos unicode, sin escapar lo traducido."""
    return "".join(UNI.get(c) or ESC.get(c) or c for c in t)


def inline(s):
    """Markdown en linea -> LaTeX (respeta $matematica$ y `codigo`)."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "$":                                    # matematica: tal cual
            j = s.find("$", i + 1)
            j = len(s) - 1 if j < 0 else j
            out.append(uni(s[i:j + 1]))
            i = j + 1
        elif c == "`":                                  # codigo en linea
            j = s.find("`", i + 1)
            j = len(s) - 1 if j < 0 else j
            out.append(r"\texttt{" + esc(s[i + 1:j]) + "}")
            i = j + 1
        elif s.startswith("**", i):
            j = s.find("**", i + 2)
            j = len(s) if j < 0 else j
            out.append(r"\textbf{" + inline(s[i + 2:j]) + "}")
            i = j + 2
        elif c == "*":
            j = s.find("*", i + 1)
            if j < 0:
                out.append(esc(c))
                i += 1
            else:
                out.append(r"\emph{" + inline(s[i + 1:j]) + "}")
                i = j + 1
        elif c == "[":
            m = re.match(r"\[([^\]]*)\]\(([^)]*)\)", s[i:])
            out.append(inline(m.group(1)) if m else esc(c))
            i += m.end() if m else 1
        else:
            j = i
            while j < len(s) and s[j] not in "$`[*":
                j += 1
            out.append(esc(s[i:j]))
            i = max(j, i + 1)
    return "".join(out)


def celdas(linea):
    """Divide una fila de tabla por | sin partir las barras dentro de $...$."""
    s, out, buf, mat = linea.strip().strip("|"), [], "", False
    for ch in s:
        if ch == "$":
            mat = not mat
        if ch == "|" and not mat:
            out.append(buf)
            buf = ""
        else:
            buf += ch
    out.append(buf)
    return [c.strip() for c in out]


def tabla(filas):
    n = max(len(f) for f in filas)
    filas = [f + [""] * (n - len(f)) for f in filas]
    cols = "@{}" + "*{%d}{>{\\raggedright\\arraybackslash}X}" % n + "@{}"
    cuerpo = " \\\\\n".join(" & ".join(inline(c) for c in f) for f in filas[1:])
    return ("\\begin{tabularx}{\\linewidth}{%s}\n\\toprule\n%s \\\\\n\\midrule\n%s \\\\\n"
            "\\bottomrule\n\\end{tabularx}" % (cols, " & ".join(inline(c) for c in filas[0]),
                                               cuerpo))


def convertir(md):
    lineas, out, titulo = md.splitlines(), [], ""
    i = 0
    while i < len(lineas):
        s = lineas[i].strip()
        if not s or s == "---" or s.startswith("**Materia:**"):
            i += 1
            continue
        m = ESP.match(s)
        if m:
            nivel, txt = len(m.group(1)), m.group(2)
            if nivel == 1:
                titulo = txt
            else:
                cmd = {2: "section", 3: "subsection", 4: "subsubsection"}[nivel]
                txt = re.sub(r"^\d+(\.\d+)*\.?\s+", "", txt)
                out.append("\\%s{%s}" % (cmd, inline(txt)))
            i += 1
            continue
        if s.startswith("$$"):
            mat = [s[2:]]
            i += 1
            while "$$" not in mat[-1] and i < len(lineas):
                mat.append(lineas[i])
                i += 1
            ult = mat[-1]
            mat[-1] = ult[:ult.index("$$")] if "$$" in ult else ult
            out.append("\\[\n" + "\n".join(m.strip() for m in mat if m.strip()) + "\n\\]")
            continue
        if s.startswith("```"):
            i += 1
            bloque = []
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                bloque.append(lineas[i])
                i += 1
            i += 1
            if bloque and all(not b.strip() or b.strip().startswith("|") for b in bloque):
                out.append(tabla([celdas(b) for b in bloque
                                  if b.strip() and not all(c.startswith("---") for c in celdas(b))]))
            else:
                out.append("\\begin{Verbatim}[breaklines=true,breakanywhere=true,"
                           "fontsize=\\small]\n" + "\n".join(bloque) + "\n\\end{Verbatim}")
            continue
        if s.startswith("|"):
            filas = []
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                f = celdas(lineas[i])
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in f if c):
                    filas.append(f)
                i += 1
            if filas:
                out.append(tabla(filas))
            continue
        if s.startswith(">"):
            cita = []
            while i < len(lineas) and lineas[i].strip().startswith(">"):
                cita.append(lineas[i].strip().lstrip(">").strip())
                i += 1
            out.append("\\begin{quote}\n" + inline(" ".join(cita)) + "\n\\end{quote}")
            continue
        mi = IMG.match(s)
        if mi:
            out.append("\\begin{center}\n\\includegraphics[width=0.9\\linewidth]{%s}\\\\[2pt]\n"
                       "{\\small %s}\n\\end{center}" % (mi.group(2), inline(mi.group(1))))
            i += 1
            continue
        m = LI.match(s)
        if m:
            num = m.group(1)[0].isdigit()
            items = []
            while i < len(lineas):
                t = lineas[i]
                mm = LI.match(t.strip())
                if mm and mm.group(1)[0].isdigit() == num:
                    items.append(mm.group(2))
                    i += 1
                elif items and t.strip() and t[0] in " \t":
                    items[-1] += " " + t.strip()
                    i += 1
                else:
                    break
            env = "enumerate" if num else "itemize"
            out.append("\\begin{%s}\n%s\n\\end{%s}" % (
                env, "\n".join("  \\item " + inline(x) for x in items), env))
            continue
        par = []
        while i < len(lineas):
            t = lineas[i].strip()
            if (not t or t == "---" or ESP.match(t) or LI.match(t) or IMG.match(t)
                    or t.startswith(("|", ">", "```", "$$"))
                    or (par and t.startswith("**"))):
                break
            par.append(t)
            i += 1
        out.append(inline(" ".join(par)))
    return titulo, "\n\n".join(out)


PLANTILLA = r"""%% Generado por a_pdf.py desde reporte.md -- no editar a mano
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,mexico]{babel}
\usepackage{graphicx}
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{fvextra}
\usepackage{float}
\usepackage{setspace}
\usepackage{parskip}
\usepackage{fancyhdr}
\usepackage{textcomp}
\usepackage[hidelinks]{hyperref}

\onehalfspacing
\setlength{\parskip}{6pt}
\sloppy
\setlength{\emergencystretch}{3em}
\setlength{\headheight}{40pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\includegraphics[width=1cm]{%(uie)s}}
\fancyhead[R]{\small %(materia)s}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

\begin{document}

%% ---------------------------- PORTADA -----------------------
\begin{titlepage}
  \thispagestyle{empty}
  \begin{center}
    \vspace*{1cm}
    \includegraphics[width=4.5cm]{%(uaz)s}
    \vspace{0.8cm}

    {\large Universidad Autónoma de Zacatecas}\\[4pt]
    {\large Unidad Académica de Ingeniería Eléctrica}\\[4pt]
    {\normalsize Ingeniería Electrónica Industrial con especialidad en Telecomunicaciones}

    \vspace{1.8cm}
    {\LARGE\bfseries %(numero)s}\\[10pt]
    {\Large\bfseries %(titulo)s}
  \end{center}

  \vspace{2.2cm}
  \begin{center}
    \begin{tabular}{rl}
      \textbf{Materia:} & %(materia)s\\
      \textbf{Docente:} & %(docente)s\\
      \textbf{Alumno:}  & %(alumno)s\\
      \textbf{Fecha:}   & %(fecha)s\\
    \end{tabular}
  \end{center}
  \vfill
\end{titlepage}

%(cuerpo)s

\end{document}
"""


def generar(carpeta):
    md = (carpeta / "reporte.md").read_text(encoding="utf-8")
    titulo, cuerpo = convertir(md)
    numero, resto = "Práctica", titulo
    if "." in titulo:
        numero, resto = (p.strip() for p in titulo.split(".", 1))
    tex = PLANTILLA % {
        "uie": (ASSETS / "UIE.png"),
        "uaz": (ASSETS / "uaz.png"),
        "numero": esc(numero),
        "titulo": inline(resto),
        "materia": MATERIA,
        "docente": DOCENTE,
        "alumno": ALUMNO,
        "fecha": FECHA,
        "cuerpo": cuerpo,
    }
    (carpeta / "main.tex").write_text(tex, encoding="utf-8")
    return carpeta / "main.tex"


def compilar(carpeta):
    r = subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                        "main.tex"], cwd=carpeta, capture_output=True, text=True,
                        errors="replace")
    if r.returncode != 0:
        print(r.stdout[-3000:], file=sys.stderr)
    return r.returncode


def main(argv):
    carpetas = sorted(p for p in DIR.glob("practica*") if (p / "reporte.md").exists())
    if argv:
        carpetas = [c for c in carpetas if c.name in argv]
    fallos = 0
    for c in carpetas:
        tex = generar(c)
        rc = compilar(c)
        pdf = c / "main.pdf"
        print(f"{c.name}: {'OK' if rc == 0 else 'FALLO'}  {pdf} "
              f"({pdf.stat().st_size // 1024} kB)" if pdf.exists() else f"{c.name}: FALLO")
        fallos += rc != 0
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
