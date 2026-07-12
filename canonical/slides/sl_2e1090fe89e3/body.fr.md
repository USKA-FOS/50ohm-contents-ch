## Résistance des fils

<left>
* Un matériau conducteur est constitué d'atomes dans une structure (en réseau)
* Les électrons sont partagés et donc libres de se déplacer
* Selon le matériau, il y a plus ou moins d'électrons libres qui entrent en collision avec les atomes
</left>
<right>
[picture:713:a_leitermodell:Atomes (+) et électrons mobiles (-) dans un conducteur métallique]
</right>

---
### Résistivité $\rho$
<left>
$R = \frac{\rho\cdot l}{A_{\textrm{Dr}}}$

* $l$: Longueur du fil
* $A_{\textrm{Dr}}$: Section transversale du fil
* $\rho$: Résistivité en $\unit{\ohm\cdot\milli\meter\squared\per\meter}$
</left>
<right>
<fragment>
* Cuivre: 0,018
* Aluminium: 0,028
* Or: 0,022
* Argent: 0,016
* Zinc: 0,11
* Fer: 0,1
* Laiton: 0,07
</fragment>
</right>
<note>
Cela permet de calculer la résistance ohmique d'un fil lorsque le matériau, la longueur et la section transversale sont connus
</note>

---
[question:AB101]
--- style="font-size: smaller;"
### Solution
* donné: $l = \qty{1,8}{\meter}$
* donné: $d = \qty{0,2}{\milli\meter}$
* donné: $\rho = \qty{0,018}{\ohm\cdot\milli\meter\squared\per\meter}$
* recherché: $R$

<fragment>
$$A_{\textrm{Dr}} = \frac{d^2\cdot \pi}{4} = \frac{(\qty{0,2}{\milli\meter})^2 \cdot \pi}{4} = \frac{\pi}{100}\unit{\milli\meter\squared} = \qty{0,0314}{\milli\meter\squared}$$
</fragment>
<fragment>
$$R = \frac{\rho\cdot l}{A_{\textrm{Dr}}} = \frac{\qty{0,018}{\ohm\cdot\milli\meter\squared\per\meter} \cdot \qty{1,8}{\meter}}{\qty{0,0314}{\milli\meter\squared}} \approx \qty{1,02}{\ohm}$$
</fragment>
---
[question:AB102]
---
### Solution
* donné: $A_{\textrm{Dr}} = \qty{0,5}{\milli\meter\squared}$
* donné: $R = \qty{1,5}{\ohm}$
* donné: $\rho = \qty{0,018}{\ohm\cdot\milli\meter\squared\per\meter}$
* recherché: $l$

<fragment>
$\begin{split} R &= \frac{\rho\cdot l}{A_{\textrm{Dr}}}\\ \Rightarrow l &= \frac{R\cdot A_{\textrm{Dr}}}{\rho} = \frac{\qty{1,5}{\ohm} \cdot \qty{0,5}{\milli\meter\squared}}{\qty{0,018}{\ohm\cdot\milli\meter\squared\per\meter}} \approx \qty{41,7}{\meter} \end{split}$
</fragment>

---
## Coefficient de température

* La résistance des métaux augmente avec la température
* Les atomes se déplacent davantage à une température plus élevée, ce qui entraîne plus de collisions avec les électrons

---
[question:AB103]