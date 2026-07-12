### Circuito oscillante parallelo

* bobine e condensatori vengono combinati
* Da considerare anche la *capacità di avvolgimento*
* Ciò introduce capacità "invisibili" nel circuito

<note>
Auto-capacità di una bobina
</note>
---
[question:AD101]
---
#### Percorso di soluzione

* dato: $C_1 = \qty{0,10}{\nanofarad}$
* dato: $C_2 = \qty{47}{\picofarad}$
* dato: $C_3 = \qty{22}{\picofarad}$
* cercato: $C_{\mathrm{totale}}$

<fragment>
$\begin{split} \tfrac{1}{C_{\mathrm{totale}}} &= \tfrac{1}{C_1} + \tfrac{1}{C_2} + \tfrac{1}{C_3} = \tfrac{1}{\qty{0,10}{\nanofarad}} + \tfrac{1}{\qty{47}{\picofarad}} + \tfrac{1}{\qty{22}{\picofarad}}\\ &= \qty{7,67e10}{\farad^{-1}}\\ \Rightarrow C_{\mathrm{totale}} &= \frac{1}{\qty{7,67e10}{\farad^{-1}}} \approx \qty{13,0}{\picofarad} \end{split}$
</fragment>
---
[question:AD103]
---
#### Percorso di soluzione

* dato: $C_1 = \qty{0,1}{\nanofarad}$
* dato: $C_2 = \qty{1,5}{\nanofarad}$
* dato: $C_3 = \qty{220}{\picofarad}$
* dato: $C_L = \qty{1}{\picofarad}$
* cercato: $C_{\mathrm{totale}}$

<fragment>
$\begin{split} C_{\mathrm{totale}} &= C_1 + C_2 + C_3 + C_L\\ &= \qty{0,1}{\nanofarad} + \qty{1,5}{\nanofarad} + \qty{220}{\picofarad} + \qty{1}{\picofarad}\\ &= \qty{1821}{\picofarad} \end{split}$
</fragment>
<note>
Prestare attenzione ai prefissi delle unità e calcolare con i reciproci
</note>

---
[question:AD105]
---
#### Percorso di soluzione

* dato: $R = \qty{100}{\ohm}$
* dato: $L = \qty{100}{\micro\henry}$
* dato: $f = \qty{1}{\megahertz}$
* cercato: $Z$

<fragment>
$\begin{split} X_L &= \omega \cdot L = 2\pi \cdot f \cdot L\\ &= 2\pi \cdot \qty{1}{\megahertz} \cdot \qty{100}{\micro\henry} = \qty{628}{\ohm}\end{split}$
</fragment>
<fragment>
$Z = \sqrt{R^2 + X^2} = \sqrt{(\qty{100}{\ohm})^2 + (\qty{628}{\ohm})^2} \approx \qty{636}{\ohm}$
</fragment>

---
[question:AD104]
---
#### Percorso di soluzione

* dato: $R = \qty{100}{\ohm}$
* dato: $C = \qty{100}{\nanofarad}$
* dato: $f = \qty{1}{\megahertz}$
* cercato: $Z$

<fragment>
$\begin{split} X_C &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{1}{\megahertz} \cdot \qty{100}{\nanofarad}} = \qty{159}{\ohm}\end{split}$
</fragment>
<fragment>
$Z = \sqrt{R^2 + X^2} = \sqrt{(\qty{100}{\ohm})^2 + (\qty{159}{\ohm})^2} \approx \qty{188}{\ohm}$
</fragment>
