Die Phasenumtastung (Phase Shift Keying, PSK) ist ein digitales Modulationsverfahren, das zur Übertragung von Daten in der Telekommunikation und im Amateurfunk genutzt wird. PSK basiert auf der Veränderung der Phase eines Trägersignals, um verschiedene Datenzustände zu repräsentieren. Im Vergleich zu Amplituden- oder Frequenzmodulation ist PSK weniger anfällig für Amplitudenrauschen und kann bei gleicher Bandbreite eine höhere Datenrate erreichen.

[picture:705:psk:Phasenumtastung (Phase-shift Keying)]

Prinzip der Phasenumtastung (PSK)

In der einfachsten Form, dem **BPSK (Binary Phase Shift Keying)**, gibt es zwei Phasenwinkel, z. B. $\qty{0}{\degree}$ und $\qty{180}{\degree}$. Jeder Phasenwinkel repräsentiert einen Bitwert ($\num{0}$ oder $\num{1}$). Bei einem Wechsel der Bitwerte verändert sich die Phase des Trägers um $\qty{180}{\degree}$.

Für höhere Datenraten gibt es Varianten wie **QPSK (Quadrature Phase Shift Keying)** und **8-PSK**, bei denen vier bzw. acht Phasenlagen verwendet werden, um mehrere Bits pro Symbol zu übertragen:
- **QPSK**: Verwendet vier Phasen ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ und $\qty{270}{\degree}$), um jeweils zwei Bits pro Symbol zu kodieren.
- **8-PSK**: Verwendet acht Phasen, um drei Bits pro Symbol zu kodieren.

Signale in der Zeitdarstellung

In der Zeitdarstellung eines PSK-Signals zeigt sich die Phasenumtastung als abrupter Wechsel im Phasenwinkel des Trägersignals, während die Amplitude konstant bleibt. Dies ist ein deutlicher Unterschied zur Amplituden- oder Frequenzmodulation, da die Höhe und Frequenz des Signals gleichbleiben, nur die Phase ändert sich bei jedem Symbolwechsel.

Beispiel: BPSK in der Zeitdarstellung
- Bei BPSK ist das Signal in zwei Phasen gespalten: z. B. positive Amplitude für eine Phase ($\qty{0}{\degree}$) und negative Amplitude für die entgegengesetzte Phase ($\qty{180}{\degree}$).
- In einem Zeit-Diagramm sieht man daher bei jedem Bitwechsel einen Sprung des Signals, z. B. von positiv nach negativ oder umgekehrt.

Beispiel: QPSK in der Zeitdarstellung
- Hier sieht man vier verschiedene Phasenwinkel. Die Übergänge können ebenfalls abrupt sein, aber die Amplitude ändert sich nicht.
- Da hier mehrere Phasenwinkel verwendet werden, sind die Phasensprünge kleiner, und die Kurve hat einen etwas „geglätteten“ Verlauf im Vergleich zu BPSK.

Wie die Signale zu erkennen sind

In einem Oszilloskop- oder Phasen-Diagramm sind die Phasenübergänge sichtbar:
- **Im Zeitbereich**: Ein abruptes Umkippen der Signalphase (positiv zu negativ oder zwischen verschiedenen Phasenlagen).
- **Im Phasendiagramm** (oft als Constellation Diagram angezeigt): Jeder Phasenwinkel ist als Punkt auf einem Kreis dargestellt, der für die verschiedenen Zustände (Bits) steht. Bei einem sauberen Signal bleiben die Punkte stabil auf festen Positionen.

PSK ist besonders nützlich in der digitalen Kommunikation, da es hohe Datenraten bei vergleichsweise robuster Übertragung erlaubt. Die Veränderung der Phase bei gleichbleibender Amplitude hilft, das Signal auch bei Rauschen und Interferenzen besser zu erkennen und damit eine stabilere Übertragung zu ermöglichen.

[question:AE401]