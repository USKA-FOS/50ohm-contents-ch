<left>
[photo:267:a_U_eilt_vor:Phasenverschiebung an einer Spule zwischen Spannung und Strom]
</left>
<right>
* Phasenverschiebung de $\qty{90}{\degree}$
* La tension précède le courant
</right>
<note>
Note : Dans les inductances, les courants sont en retard -ou- Inductance, courant en retard !
</note>

---
[question:AC201]

---
### Puissance active

<left>
[picture:944:a_Blindleistung Spule:Das Produkt von $U \cdot I$ ergibt die grüne Leistungskurve]
</left>
<right>
* La courbe de puissance verte est le produit du courant et de la tension
* La puissance oscille symétriquement autour de la ligne nulle et se compense
* *Puissance réactive* sur une *réactance inductive*
</right>

---

* La réactance inductive n'absorbe pas d'énergie active
* Une bobine idéale ne chauffe pas
* Cependant, une bobine est constituée de fil et présente donc des pertes ohmiques
* De plus, l'effet de peau agit

---
[question:AC202]

--- style="font-size: smaller;"
### Réactance inductive $X_{\textrm{L}}$

La bobine connectée à une tension alternative crée constamment un champ magnétique $\rightarrow$ résistance au courant alternatif / réactance inductive

1. Si la fréquence de la tension alternative appliquée à une bobine est augmentée, alors le courant diminue ; cela signifie que la réactance inductive a augmenté.
2. Si l'inductance de la bobine est augmentée, le courant diminue également, c'est-à-dire que la réactance inductive augmente également.

<fragment>
$|X_{\textrm{L}}| = \omega \cdot L = 2\pi \cdot f \cdot L$
</fragment>

---
[question:AC203]
---
[question:AC204]
---
#### Solution
* donné : $L = \qty{3}{\micro\henry}$
* donné : $f = \qty{100}{\mega\hertz}$
* recherché : $X_{\textrm{L}}$

<fragment>
$\begin{split} |X_{\textrm{L}}| &= \omega \cdot L = 2\pi \cdot f \cdot L\\ &= 2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{3}{\micro\henry}\\ &\approx \qty{1885}{\ohm} \end{split}$
</fragment>

---
### Augmentation de l'inductance
<left>
Bobine cylindrique
<fragment>
$L = \dfrac{\mu_0 \cdot \mu_r \cdot N^2 \cdot A_S}{l}$
</fragment>

* Augmenter le nombre de spires $N$
* Réduire la longueur de la bobine $l$
* Augmenter la surface de section transversale $A_S$ de la bobine

</left>
<right>
Bobine à noyau toroïdal
<fragment>
$L = N^2 \cdot A_{\textrm{L}}$
</fragment>
  
* Augmenter le nombre de spires $N$
* Utiliser un matériau plus magnétiquement conducteur (avec une constante d'inductance $A_{\textrm{L}}$ plus grande) comme noyau

</right>

<note>
C'est pourquoi des noyaux (annulaires) sont utilisés
</note>
---
[question:AC211]

---
[question:AC205]
---
#### Solution
* donné : $N = 14$
* donné : $A_{\textrm{L}} = \qty{1,5}{\nano\henry}$
* recherché : $L$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ &= 14^2 \cdot \qty{1,5}{\nano\henry}\\ &= \qty{0,294}{\micro\henry} \end{split}$
</fragment>

---
[question:AC206]
---
#### Solution
* donné : $N = 300$
* donné : $A_{\textrm{L}} = \qty{1250}{\nano\henry}$
* recherché : $L$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ &= 300^2 \cdot \qty{1250}{\nano\henry}\\ &= \qty{112,5}{\milli\henry} \end{split}$
</fragment>

---
[question:AC207]
---
#### Solution
* donné : $L = \qty{2}{\milli\henry}$
* donné : $A_{\textrm{L}} = \qty{250}{\nano\henry}$
* recherché : $N$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ N &= \sqrt{\frac{L}{A_{\textrm{L}}}} = \sqrt{\frac{\qty{2}{\milli\henry}}{\qty{250}{\nano\henry}}} \\ &= 89\,\text{spires} \end{split}$
</fragment>

---
[question:AC208]
---
#### Solution
* donné : $L = \qty{12}{\micro\henry}$
* donné : $A_{\textrm{L}} = \qty{30}{\nano\henry}$
* recherché : $N$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ N &= \sqrt{\frac{L}{A_{\textrm{L}}}} = \sqrt{\frac{\qty{12}{\micro\henry}}{\qty{30}{\nano\henry}}} \\ &= 20\,\text{spires} \end{split}$
</fragment>

---
### Pertes dans les bobines

* Facteur de perte $\tan(\delta) = \frac{R}{X_L}$
* Pertes dans le conducteur

---
[question:AC209]

---
### Impédance

* Circuit série d'une réactance et d'une résistance $\rightarrow$ impédance $Z$
* Se produit uniquement avec une tension alternative
* Ne peut pas être mesurée avec un ohmmètre
* Bobine en radio technique $\rightarrow$ *Impédance*
* Impédance d'antenne, impédance d'entrée et de sortie, transformateur d'impédance, …
* Impédance $Z$ en $\unit{\ohm}$

---
<left>
[picture:1067:a_impedanzdreieck:Impedanz $Z$ als geometrische Addition von $R$ und $X$]
  
$Z = \sqrt{R^2 + X^2}$
</left>
<right>
* Résistance $R$
* Réactance $X_{\textrm{L}}$
* L'impédance est à calculer par Pythagore
</right>

---
[question:AA101]

---
### Blindage des champs magnétiques

<left>
* Pour le blindage : Un boîtier en matériau bon conducteur.
* Exemple : Béchers de blindage en acier ou en fer.
* Noyau de ferrite réglable pour modifier l'inductance.
</left>
<right>
[photo:333:a_abschirmbecher:Exemple de bobines avec un bécher de blindage pour le blindage des champs magnétiques]
</right>


---
[question:AC210]
