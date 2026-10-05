from __future__ import annotations

import argparse
from pathlib import Path


DRAWINGS = {
    "648": "dr_ec2725d9655a",
    "10102": "dr_a7a7722dfbc9",
}


def replace_once(text: str, source: str, target: str, label: str) -> str:
    count = text.count(source)
    if count != 1:
        raise ValueError(f"{label}: expected one occurrence, found {count}: {source!r}")
    return text.replace(source, target, 1)


def prepare_648(text: str, language: str) -> str:
    labels = {
        "fr": {
            "title": r"Relais Uetliberg\\HB9UF\\[1pt]Décalage : $-7{,}6\,$MHz",
            "input": r"$f_1$ = 438,650 MHz\\(entrée) TSQ 71,9\,Hz",
            "output": r"$f_2$ = 431,050 MHz\\(sortie)",
            "explanation": "Entrée = le relais reçoit (l’utilisateur émet) "
            r"$\cdot$ "
            "sortie = le relais émet (l’utilisateur reçoit)",
            "portable": "Émetteur-récepteur portatif : semi-duplex -- émet "
            r"\textbf{ou} "
            "reçoit, commandé par la touche Push-to-Talk (PTT)",
        },
        "it": {
            "title": r"Ripetitore Uetliberg\\HB9UF\\[1pt]Offset: $-7{,}6\,$MHz",
            "input": r"$f_1$ = 438,650 MHz\\(ingresso) TSQ 71,9\,Hz",
            "output": r"$f_2$ = 431,050 MHz\\(uscita)",
            "explanation": "Ingresso = il ripetitore riceve (l’utente trasmette) "
            r"$\cdot$ "
            "uscita = il ripetitore trasmette (l’utente riceve)",
            "portable": "Ricetrasmettitore portatile: semiduplex -- trasmette "
            r"\textbf{o} "
            "riceve, comandato dal tasto Push-to-Talk (PTT)",
        },
    }[language]
    replacements = [
        (
            r"Relais Uetliberg\\HB9UF\\[1pt]Shift: $-7{,}6\,$MHz",
            labels["title"],
        ),
        (r"$f_1$ = 438,650 MHz\\(Eingabe) TSQ 71,9\,Hz", labels["input"]),
        (r"$f_2$ = 431,050 MHz\\(Ausgabe)", labels["output"]),
        (
            r'Eingabe = Relais empf\"angt (Nutzer sendet) $\cdot$ Ausgabe = Relais sendet (Nutzer empf\"angt)',
            labels["explanation"],
        ),
        (
            r'Handfunkger\"at: Halbduplex -- sendet \textbf{oder} empf\"angt, gesteuert per Push-to-Talk (PTT)-Taste',
            labels["portable"],
        ),
    ]
    for source, target in replacements:
        text = replace_once(text, source, target, f"648.{language}")
    return text


def prepare_10102(text: str, language: str) -> str:
    terms = {
        "fr": {
            "flow": "écoulement",
            "spring": "ressort",
            "no_flow": "aucun écoulement (bloquant)",
            "flowing": "écoulement (passant)",
            "closed": "Fermé",
            "open": "Ouvert",
            "below": "force sous le seuil -- analogie :",
            "above": "force au-dessus du seuil -- analogie :",
        },
        "it": {
            "flow": "flusso",
            "spring": "molla",
            "no_flow": "nessun flusso (bloccato)",
            "flowing": "flusso (in conduzione)",
            "closed": "Chiuso",
            "open": "Aperto",
            "below": "forza sotto la soglia -- analogia:",
            "above": "forza sopra la soglia -- analogia:",
        },
    }[language]
    counts = {
        r"\text{Strom}": 2,
        r"\text{Feder}": 2,
        "kein Durchfluss (sperrend)": 1,
        "Durchfluss (leitend)": 1,
        r"\small Geschlossen \\ \small (Kraft unterhalb Schwellwert -- Analogie:": 1,
        r"\small Offen \\ \small (Kraft oberhalb Schwellwert -- Analogie:": 1,
    }
    for source, expected in counts.items():
        count = text.count(source)
        if count != expected:
            raise ValueError(f"10102.{language}: expected {expected}, found {count}: {source!r}")
    text = text.replace(r"\text{Strom}", rf"\text{{{terms['flow']}}}")
    text = text.replace(r"\text{Feder}", rf"\text{{{terms['spring']}}}")
    text = text.replace("kein Durchfluss (sperrend)", terms["no_flow"])
    text = text.replace("Durchfluss (leitend)", terms["flowing"])
    text = replace_once(
        text,
        r"\small Geschlossen \\ \small (Kraft unterhalb Schwellwert -- Analogie:",
        rf"\small {terms['closed']} \\ \small ({terms['below']}",
        f"10102.{language}",
    )
    text = replace_once(
        text,
        r"\small Offen \\ \small (Kraft oberhalb Schwellwert -- Analogie:",
        rf"\small {terms['open']} \\ \small ({terms['above']}",
        f"10102.{language}",
    )
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    for figure, object_id in DRAWINGS.items():
        source = args.source_root / "canonical" / "drawings" / object_id / f"{figure}.de.tex"
        original = source.read_text(encoding="utf-8")
        for language in ("fr", "it"):
            localized = (
                prepare_648(original, language)
                if figure == "648"
                else prepare_10102(original, language)
            )
            if figure == "10102":
                localized = localized.replace(
                    "% Mechanisches Analogon einer Diode, das der Veranschaulichung dienen kann. \n",
                    "% Mechanisches Analogon einer Diode, das der Veranschaulichung dienen kann.\n",
                )
            target = args.output_root / "canonical" / "drawings" / object_id / f"{figure}.{language}.tex"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(localized, encoding="utf-8")
            print(target)


if __name__ == "__main__":
    main()
