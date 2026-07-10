# Zeichnen von Vektorgrafiken

Die Zeichnungen werden durch LaTeX und TikZ umgesetzt. In der Regel ist immer die neueste LaTeX-Version erforderlich. Außerdem kommt insbesondere die Bibliothek [CircuiTikZ](https://ctan.org/pkg/circuitikz?lang=de) zum Einsatz. Ein direktes Modifizieren der SVG-Dateien ist für die Inhalte nicht vorgesehen! Außerdem ist es notwendig, dass das Programm *pdftocairo* installiert ist, um aus dem von LaTeX erzeugten PDF ein SVG zu generieren.

Das Python-Skript `src/build_drawings.py` wird verwendet, um ein neues Bild zu erstellen. Beim Aufrufen des Skripts muss eine Bildnummer eingegeben werden. Die Bildnummern müssen aufsteigend vergeben werden: Bitte hierzu vorher ein Issue öffnen. Weiterhin ist die Breite des Bildes optional anzugeben. Der Standardwert liegt bei 9 cm. Bei manchen Grafiken kann es sinnvoll sein, eine kleinere Breite zu wählen. 

Bitte vor dem Zeichnen eines neuen Bildes einen Issue öffnen um Missverständnisse zu vermeiden. 