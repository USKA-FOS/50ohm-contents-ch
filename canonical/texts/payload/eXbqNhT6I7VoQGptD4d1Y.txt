--- style="font-size: 0.7em;"

[picture:701:4ask:Quaternäre Amplitudenumtastung (Quaternary Amplitude-shift Keying)]

* Viele digitale Modulationsverfahren verwenden mehr als zwei Symbole.
* So funktioniert zum Beispiel die 4-Fach-Amplitudenumtastung (4ASK) mit vier unterschiedlichen Amplituden, $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$, $\qty{100}{\percent}$ des Maximums.
* So lassen sich zwei Bits zu einem Symbol zusammenfassen und gleichzeitig übertragen.

---

* Dieses Prinzip lässt sich auf die Frequenz- und Phasenumtastung übertragen.
* Eine einfache Phasenumtastung (Binary Phase-Shift Keying, BPSK) verwendet nur zwei verschiedene Phasenlagen und kann daher nur ein Bit gleichzeitig senden.
* Die Quadraturphasenumtastung (Quadrature Phase-Shift Keying, QPSK) hingegen nutzt vier verschiedene Phasenlagen ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ und $\qty{270}{\degree}$) und überträgt somit zwei Bits in jedem Schritt.

---
[question:AE402]

---

* Da bei Verfahren wie QPSK mehr als ein Bit pro Symbol übertragen wird, müssen wir mit den Einheiten aufpassen.
* Werden nur zwei Symbole verwendet und somit jedes Bit einzeln gesendet, entspricht die Symbolrate in Baud der Datenrate in $\unit{\bit\per\second}$.
* Werden jedoch mehr Symbole verwendet und somit mehrere Bits gleichzeitig übertragen, ist die Datenrate höher als die Symbolrate.

---

* Die Formel $C = R_{ s } \cdot n$ stellt den Zusammenhang dar:

<fragment>
* $C$ → Datenübertragungsrate in $\unit{\bit\per\second}$
* $R_{ s }$ → Symbolrate in $\unit{\baud}$
* $n$ → Symbolgröße in $\unit{\bit\per\text{Symbol}}$
</fragment>

---
[question:AA104]

---

Beispiele:

<fragment>
*RTTY*: Umschaltung zwischen zwei Symbolfrequenzen, sodass pro Symbol ein Bit ($\num{0}$ oder $\num{1}$) übertragen werden kann.
→ Datenrate = Symbolrate
</fragment>

<fragment>
*FT4*: Umschaltung zwischen vier Symbolfrequenzen, so dass pro Symbol zwei Bit ($\num{00}$, $\num{01}$, $\num{10}$ oder $\num{11}$) übertragen werden können.
→ Datenrate = 2 $\cdot$ Symbolrate
</fragment>

---
[question:AE405]
---
#### Lösungsweg
* gegeben: $R_S = \qty{45,45}{\baud}$
* gegeben: $n=\qty{1}{\bit\per\text{Symbol}}$
* gesucht: $C$

<fragment>
$C = R_S \cdot n = \qty{45,45}{\baud} \cdot \qty{1}{\bit\per\text{Symbol}} = \qty{45,45}{\bit\per\second}$
</fragment>

---
[question:AE406]
---
#### Lösungsweg
* gegeben: $R_S = \qty{23,4}{\baud}$
* gegeben: $n=\qty{2}{\bit\per\text{Symbol}}$
* gesucht: $C$

<fragment>
$C = R_S \cdot n = \qty{23,4}{\baud} \cdot \qty{2}{\bit\per\text{Symbol}} = \qty{46,8}{\bit\per\second}$
</fragment>