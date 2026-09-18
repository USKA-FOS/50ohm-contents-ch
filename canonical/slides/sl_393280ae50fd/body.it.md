### Circuito risonante parallelo

* Le bobine e i condensatori vengono combinati
* Da considerare anche la *capacità parassita di avvolgimento*
* Questo introduce capacità "invisibili" nel circuito

<note>
Capacità propria di una bobina
</note>
---
[question:AD101]
---
#### Procedimento

* dati: $C_1 = \qty{0,10}{\nano\farad}$
* dati: $C_2 = \qty{47}{\pico\farad}$
* dati: $C_3 = \qty{22}{\pico\farad}$
* richiesto: $C_{\mathrm{ges}}$

<fragment>
$\begin{split} \tfrac{1}{C_{\mathrm{ges}}} &= \tfrac{1}{C_1} + \tfrac{1}{C_2} + \tfrac{1}{C_3} = \tfrac{1}{\qty{0,10}{\nano\farad}} + \tfrac{1}{\qty{47}{\pico\farad}} + \tfrac{1}{\qty{22}{\pico\farad}}\\ &= \qty{7,67e10}{\farad^{-1}}\\ \Rightarrow C_{\mathrm{ges}} &= \frac{1}{\qty{7,67e10}{\farad^{-1}}} \approx \qty{13,0}{\pico\farad} \end{split}$
</fragment>
---
[question:AD103]
---
#### Procedimento

* dati: $C_1 = \qty{0,1}{\nano\farad}$
* dati: $C_2 = \qty{1,5}{\nano\farad}$
* dati: $C_3 = \qty{220}{\pico\farad}$
* dati: $C_L = \qty{1}{\pico\farad}$
* richiesto: $C_{\mathrm{ges}}$

<fragment>
$\begin{split} C_{\mathrm{ges}} &= C_1 + C_2 + C_3 + C_L\\ &= \qty{0,1}{\nano\farad} + \qty{1,5}{\nano\farad} + \qty{220}{\pico\farad} + \qty{1}{\pico\farad}\\ &= \qty{1821}{\pico\farad} \end{split}$
</fragment>
<note>
Attenzione ai prefissi delle unità e ai calcoli con i reciproci
</note>

---
[question:AD105]
---
#### Procedimento

* dati: $R = \qty{100}{\ohm}$
* dati: $L = \qty{100}{\micro\henry}$
* dati: $f = \qty{1}{\mega\hertz}$
* richiesto: $Z$

<fragment>
$\begin{split} X_L &= \omega \cdot L = 2\pi \cdot f \cdot L\\ &= 2\pi \cdot \qty{1}{\mega\hertz} \cdot \qty{100}{\micro\henry} = \qty{628}{\ohm}\end{split}$
</fragment>
<fragment>
$Z = \sqrt{R^2 + X^2} = \sqrt{(\qty{100}{\ohm})^2 + (\qty{628}{\ohm})^2} \approx \qty{636}{\ohm}$
</fragment>

---
[question:AD104]
---
#### Procedimento

* dati: $R = \qty{100}{\ohm}$
* dati: $C = \qty{100}{\nano\farad}$
* dati: $f = \qty{1}{\mega\hertz}$
* richiesto: $Z$

<fragment>
$\begin{split} X_C &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{1}{\mega\hertz} \cdot \qty{100}{\nano\farad}} = \qty{159}{\ohm}\end{split}$
</fragment>
<fragment>
$Z = \sqrt{R^2 + X^2} = \sqrt{(\qty{100}{\ohm})^2 + (\qty{159}{\ohm})^2} \approx \qty{188}{\ohm}$
</fragment>
