<left>
[photo:268:a_I eilt vor:Déphasage entre tension et courant dans un condensateur]
</left>
<right>
* Déphasage de $\qty{90}{\degree}$
* Le courant précède la tension
</right>
<note>
À retenir : Condensateeeeur, le courant précède !
</note>
---
[question:AC101]
---
### Puissance active
<left>
[picture:943:a_Blindleistung Kondensator:Le produit de $U \cdot I$ donne la courbe de puissance en vert]
</left>
<right>
* La courbe de puissance en vert est le produit du courant et de la tension
* La puissance oscille symétriquement autour de la ligne zéro et s'annule
* *Puissance réactive* aux bornes d'une *réactance*
</right>
---
[question:AC111]
<note>
En régime établi, le courant est presque nul, ce qui explique que la puissance est également quasi nulle (0 W).
</note>
---
* La puissance active n'est dissipée que dans une résistance ohmique (courant et tension en phase)
* Une réactance ne consomme pas d'énergie active
* Elle ne chauffe donc pas
* Un condensateur chaud en haute fréquence présente une composante résistive et doit être remplacé

---
[question:AC103]

--- style="font-size: smaller;"
### Réactance capacitive $X_{\textrm{C}}$

Un condensateur connecté à une tension alternative est constamment chargé et déchargé $\rightarrow$ impédance / réactance capacitive

<fragment>
1. Si la fréquence de la tension alternative aux bornes d'un condensateur augmente, le courant augmente ; cela signifie que la réactance capacitive diminue.
</fragment>
<fragment>
2. Si la capacité du condensateur augmente, le courant augmente également, c'est-à-dire que la réactance diminue aussi.
</fragment>

<fragment>
$X_{\textrm{C}} = \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}$
</fragment>

<note>
Un analyseur de réseau mesure la variation de la réactance $X_C$ en fonction de la fréquence
</note>
---
[question:AC102]
---
[question:AC104]
---
#### Méthode de résolution
* donné : $C = \qty{10}{\pico\farad}$
* donné : $f = \qty{100}{\mega\hertz}$
* recherché : $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{10}{\pico\farad}}\\ &\approx \qty{159}{\ohm} \end{split}$
</fragment>

---
[question:AC105]
---
#### Méthode de résolution
* donné : $C = \qty{50}{\pico\farad}$
* donné : $f = \qty{145}{\mega\hertz}$
* recherché : $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{145}{\mega\hertz} \cdot \qty{50}{\pico\farad}}\\ &\approx \qty{22}{\ohm} \end{split}$
</fragment>
---
[question:AC106]
---
#### Méthode de résolution
* donné : $C = \qty{100}{\pico\farad}$
* donné : $f = \qty{100}{\mega\hertz}$
* recherché : $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{100}{\pico\farad}}\\ &\approx \qty{15,9}{\ohm} \end{split}$
</fragment>

---
[question:AC107]
---
#### Méthode de résolution
* donné : $C = \qty{100}{\pico\farad}$
* donné : $f = \qty{435}{\mega\hertz}$
* recherché : $X_{\textrm{C}}$

<fragment>
$\begin{split} X_{\textrm{C}} &= \frac{1}{\omega \cdot C} = \frac{1}{2\pi \cdot f \cdot C}\\ &= \frac{1}{2\pi \cdot \qty{435}{\mega\hertz} \cdot \qty{100}{\pico\farad}}\\ &\approx \qty{3,7}{\ohm} \end{split}$
</fragment>

---
[question:AC108]
---
#### Méthode de résolution
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
### Pertes dans un condensateur

<left>
[photo:260:a_Kondensator Ersatzschaltbild:Schéma équivalent d'un condensateur réel avec une résistance de perte série (ESR).]
</left>
<right>
* Facteur de perte
$\tan(\delta) = \frac{R}{X_C}$
* Pertes dans le diélectrique et les connexions
</right>

---
[question:AC109]
---
[question:AC110]
