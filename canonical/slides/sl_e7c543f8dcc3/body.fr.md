<left>
[photo:268:a_I eilt vor:Phasenverschiebung am Kondensator zwischen Spannung und Strom]
</left>
<right>
* Phasenverschiebung de $\qty{90}{\degree}$
* Le courant précède la tension
</right>
<note>
Notez : Condensateuuuur, le courant précède !
</note>
---
[question:AC101]
---
### Puissance active
<left>
[picture:943:a_Blindleistung Kondensator:Das Produkt von $U \cdot I$ ergibt die grüne Leistungskurve]
</left>
<right>
* La courbe de puissance verte est le produit du courant et de la tension
* La puissance oscille symétriquement autour de la ligne de zéro et s'équilibre
* *Puissance réactive* sur une *résistance réactive*
</right>
---
[question:AC111]
<note>
À l'état stable, presque aucun courant ne circule plus, c'est pourquoi la puissance est également presque de 0W.
</note>
---
* La puissance active n'est convertie que dans une résistance ohmique (courant et tension en phase)
* La résistance réactive n'absorbe pas d'énergie active
* Ne chauffe donc pas
* Un condensateur chaud à haute fréquence a une composante ohmique et doit être remplacé

---
[question:AC103]

--- style="font-size: smaller;"
### Résistance réactive capacitive $X_{\textrm{C}}$

Le condensateur est constamment chargé et déchargé lorsqu'il est connecté à une tension alternative $\rightarrow$ résistance au courant alternatif / résistance réactive capacitive

<fragment>
1. Si la fréquence de la tension alternative à un condensateur est augmentée, alors plus de courant circule ; cela signifie que la résistance réactive capacitive est devenue plus petite.
</fragment>
<fragment>
2. Si la capacité du condensateur est augmentée, alors le courant augmente également, c'est-à-dire que la résistance réactive diminue également.
</fragment>

<fragment>
$X_{\textrm{C}} = \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}$
</fragment>

<note>
Un VNA mesure la variation de la résistance réactive $X_C$ en fonction de la fréquence
</note>
---
[question:AC102]
---
[question:AC104]
---
#### Solution
* donné : $C = \qty{10}{\pico\farad}$
* donné : $f = \qty{100}{\mega\hertz}$
* recherché : $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{10}{\pico\farad}}\\ &\approx \qty{159}{\ohm} \end{split}$
</fragment>

---
[question:AC105]
---
#### Solution
* donné : $C = \qty{50}{\pico\farad}$
* donné : $f = \qty{145}{\mega\hertz}$
* recherché : $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{145}{\mega\hertz} \cdot \qty{50}{\pico\farad}}\\ &\approx \qty{22}{\ohm} \end{split}$
</fragment>
---
[question:AC106]
---
#### Solution
* donné : $C = \qty{100}{\pico\farad}$
* donné : $f = \qty{100}{\mega\hertz}$
* recherché : $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{100}{\pico\farad}}\\ &\approx \qty{15,9}{\ohm} \end{split}$
</fragment>

---
[question:AC107]
---
#### Solution
* donné : $C = \qty{100}{\pico\farad}$
* donné : $f = \qty{435}{\mega\hertz}$
* recherché : $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{435}{\mega\hertz} \cdot \qty{100}{\pico\farad}}\\ &\approx \qty{3,7}{\ohm} \end{split}$
</fragment>

---
[question:AC108]
---
#### Solution
<left>
* donné : $U = \qty{16}{\volt}$
* donné : $I = \qty{32}{\milli\ampere}$
</left>
<right>
* donné : $f = \qty{50}{\hertz}$
* recherché : $C$
</right>

<fragment>
$X_{\textrm{C}} = \frac{U}{I} = \frac{\qty{16}{\volt}}{\qty{32}{\milli\ampere}} = \qty{500}{\ohm}$
</fragment>

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} \\ \Rightarrow C &= \frac{1}{\omega \cdot X_{\textrm{C}}} = \frac{1}{2\pi \cdot f \cdot X_{\textrm{C}}}\\ &= \frac{1}{2\pi \cdot \qty{50}{\hertz} \cdot \qty{500}{\ohm}}\\ &\approx \qty{6,37}{\micro\farad}\end{split}$
</fragment>

---
### Pertes de condensateur

<left>
[photo:260:a_Kondensator Ersatzschaltbild:Ersatzschaltbild eines realen Kondensators mit einem seriellen Verlustwiderstand (ESR).]
</left>
<right>
* Facteur de perte<br/>$\tan(\delta) = \frac{R}{X_C}$
* Pertes dans le diélectrique et le câblage
</right>

---
[question:AC109]
---
[question:AC110]
