Viele digitale Modulationsverfahren verwenden mehr als zwei Symbole. Anstelle von nur zwei Amplituden (klein und groß) funktioniert Amplitudenumtastung auch mit vier oder noch mehr unterschiedlichen Amplituden, also beispielsweise $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$, $\qty{100}{\percent}$ des Maximums. So lassen sich zwei oder mehr Bits zu einem Symbol zusammenfassen und gleichzeitig übertragen.

[picture:701:4ask:Quaternäre Amplitudenumtastung (Quaternary Amplitude-shift Keying)]

Dieses Prinzip lässt sich auch wieder auf die Frequenz- und Phasenumtastung übertragen. Eine einfache Phasenumtastung (Binary Phase-Shift Keying, BPSK) verwendet nur zwei verschiedene Phasenlagen und kann daher nur ein Bit gleichzeitig senden. Die Quadraturphasenumtastung (Quadrature Phase-Shift Keying, QPSK) hingegen nutzt schon vier verschiedene Phasenlagen ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ und $\qty{270}{\degree}$). QPSK überträgt somit zwei Bits in jedem Schritt.

[question:AE402]

Da bei Verfahren wie QPSK mehr als ein Bit pro Symbol übertragen wird, müssen wir mit den Einheiten aufpassen. Während wir in Hinblick auf den Datenstrom von einer Datenrate in $\unit{\bit\per\second}$ sprechen, wird die Rate der Abfolge unterschiedlicher Symbole in Symbolen pro Sekunde mit der Einheit Baud notiert.

[question:AA104]

Werden nur zwei Symbole verwendet und somit jedes Bit einzeln gesendet, entspricht die Symbolrate in Baud ($\unit{\baud}$) der Datenrate in Bit pro Sekunde ($\unit{\bit\per\second}$). Werden jedoch mehr Symbole verwendet und somit mehrere Bits gleichzeitig übertragen, ist die Datenrate höher als die Symbolrate. Für den Zusammenhang gilt, dass die Datenrate in $\unit{\bit\per\second}$ gleich der Symbolrate in $\unit{\baud}$ multipliziert mit der Anzahl der pro Symbol übertragenen Bits ist:

$C=R_\mathrm{S}\cdot n$

$C$ Datenübertragungsrate in $\unit{\bit\per\second}$

$R_\mathrm{S}$ Symbolrate in $\unit{\baud}$

$n$ Symbolgröße in $\unit{\bit\per\text{Symbol}}$

[question:AE405]
[question:AE406]
