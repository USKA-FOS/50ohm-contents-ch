--- style="font-size: 0.7em;"

[picture:701:4ask:Modulation d'amplitude à quatre niveaux (Quaternary Amplitude-shift Keying)]

* De nombreux procédés de modulation numérique utilisent plus de deux symboles.
* Par exemple, la modulation d'amplitude à quatre niveaux (4ASK) utilise quatre amplitudes différentes, $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$, $\qty{100}{\percent}$ du maximum.
* Ainsi, deux bits peuvent être combinés en un symbole et transmis simultanément.

---

* Ce principe peut être appliqué à la modulation de fréquence et de phase.
* Une modulation de phase simple (Binary Phase-Shift Keying, BPSK) utilise seulement deux positions de phase différentes et ne peut donc envoyer qu'un bit à la fois.
* La modulation de phase en quadrature (Quadrature Phase-Shift Keying, QPSK) utilise quant à elle quatre positions de phase différentes ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ et $\qty{270}{\degree}$) et transmet ainsi deux bits à chaque étape.

---
[question:AE402]

---

* Comme dans les procédés comme la QPSK, plus d'un bit par symbole est transmis, nous devons faire attention aux unités.
* Si seulement deux symboles sont utilisés et donc chaque bit est envoyé individuellement, le débit de symboles en Baud correspond au débit de données en $\unit{\bit\per\second}$.
* Si plus de symboles sont utilisés et donc plusieurs bits sont transmis simultanément, le débit de données est supérieur au débit de symboles.

---

* La formule $C = R_{ s } \cdot n$ représente cette relation:

<fragment>
* $C$ → Débit de transmission de données en $\unit{\bit\per\second}$
* $R_{ s }$ → Débit de symboles en $\unit{\baud}$
* $n$ → Taille du symbole en $\unit{\bit\per\text{Symbol}}$
</fragment>

---
[question:AA104]

---
Exemples:

<fragment>
*RTTY*: Commutation entre deux fréquences de symboles, permettant de transmettre un bit ($\num{0}$ ou $\num{1}$) par symbole.
→ Débit de données = Débit de symboles
</fragment>

<fragment>
*FT4*: Commutation entre quatre fréquences de symboles, permettant de transmettre deux bits ($\num{00}$, $\num{01}$, $\num{10}$ ou $\num{11}$) par symbole.
→ Débit de données = 2 $\cdot$ Débit de symboles
</fragment>

---
[question:AE405]
---
#### Solution
* donné: $R_S = \qty{45,45}{\baud}$
* donné: $n=\qty{1}{\bit\per\text{Symbol}}$
* recherché: $C$

<fragment>
$C = R_S \cdot n = \qty{45,45}{\baud} \cdot \qty{1}{\bit\per\text{Symbol}} = \qty{45,45}{\bit\per\second}$
</fragment>

---
[question:AE406]
---
#### Solution
* donné: $R_S = \qty{23,4}{\baud}$
* donné: $n=\qty{2}{\bit\per\text{Symbol}}$
* recherché: $C$

<fragment>
$C = R_S \cdot n = \qty{23,4}{\baud} \cdot \qty{2}{\bit\per\text{Symbol}} = \qty{46,8}{\bit\per\second}$
</fragment>