---

[picture:701:4ask:Modulazione a spostamento di ampiezza quaternaria (Quaternary Amplitude-shift Keying)]

* Molti metodi di modulazione digitale utilizzano più di due simboli.
* Ad esempio, la modulazione a spostamento di ampiezza a 4 vie (4ASK) funziona con quattro ampiezze diverse, $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$, $\qty{100}{\percent}$ del massimo.
* In questo modo, due bit possono essere combinati in un simbolo e trasmessi contemporaneamente.

---

* Questo principio può essere applicato alla modulazione a spostamento di frequenza e di fase.
* Una semplice modulazione a spostamento di fase (Binary Phase-Shift Keying, BPSK) utilizza solo due diverse posizioni di fase e quindi può inviare solo un bit alla volta.
* La modulazione a spostamento di fase in quadratura (Quadrature Phase-Shift Keying, QPSK), invece, utilizza quattro diverse posizioni di fase ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ e $\qty{270}{\degree}$) e quindi trasmette due bit in ogni passo.

---
[question:AE402]

---

* Poiché metodi come QPSK trasmettono più di un bit per simbolo, dobbiamo prestare attenzione alle unità.
* Se vengono utilizzati solo due simboli e quindi ogni bit viene inviato singolarmente, la velocità di simbolo in Baud corrisponde alla velocità di trasmissione dati in $\unit{\bit\per\second}$.
* Tuttavia, se vengono utilizzati più simboli e quindi vengono trasmessi più bit contemporaneamente, la velocità di trasmissione dati è superiore alla velocità di simbolo.

---

* La formula $C = R_{ s } \cdot n$ rappresenta la relazione:

<fragment>
* $C$ → Velocità di trasmissione dati in $\unit{\bit\per\second}$
* $R_{ s }$ → Velocità di simbolo in $\unit{\baud}$
* $n$ → Dimensione del simbolo in $\unit{\bit\per\text{Symbol}}$
</fragment>

---
[question:AA104]

---

Esempi:

<fragment>
*RTTY*: Commutazione tra due frequenze di simbolo, in modo che un bit ($\num{0}$ o $\num{1}$) possa essere trasmesso per simbolo.
→ Velocità di trasmissione dati = Velocità di simbolo
</fragment>

<fragment>
*FT4*: Commutazione tra quattro frequenze di simbolo, in modo che due bit ($\num{00}$, $\num{01}$, $\num{10}$ o $\num{11}$) possano essere trasmessi per simbolo.
→ Velocità di trasmissione dati = 2 $\cdot$ Velocità di simbolo
</fragment>

---
[question:AE405]
---
#### Percorso di soluzione
* dato: $R_S = \qty{45,45}{\baud}$
* dato: $n=\qty{1}{\bit\per\text{Symbol}}$
* cercato: $C$

<fragment>
$C = R_S \cdot n = \qty{45,45}{\baud} \cdot \qty{1}{\bit\per\text{Symbol}} = \qty{45,45}{\bit\per\second}$
</fragment>

---
[question:AE406]
---
#### Percorso di soluzione
* dato: $R_S = \qty{23,4}{\baud}$
* dato: $n=\qty{2}{\bit\per\text{Symbol}}$
* cercato: $C$

<fragment>
$C = R_S \cdot n = \qty{23,4}{\baud} \cdot \qty{2}{\bit\per\text{Symbol}} = \qty{46,8}{\bit\per\second}$
</fragment>