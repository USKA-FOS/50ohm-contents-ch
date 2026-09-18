<left>
[photo:267:a_U_eilt_vor:Déphasage entre tension et courant dans une bobine]
</left>
<right>
* Déphasage de $\qty{90}{\degree}$
* La tension est en avance sur le courant
</right>
<note>
À retenir : Avec les inductances, les courants sont en retard – ou bien : inductance, courant trop tard !
</note>

---
[question:AC201]

---
### Puissance active

<left>
[picture:944:a_Blindleistung Spule:Le produit de $U \cdot I$ donne la courbe de puissance en vert]
</left>
<right>
* La courbe de puissance en vert est le produit de la tension et du courant
* La puissance oscille symétriquement autour de la ligne zéro et s’annule
* *Puissance réactive* aux bornes d’une *réactance*
</right>

---

* Une réactance ne consomme pas d’énergie active
* Une bobine idéale ne chauffe pas
* Cependant, une bobine est composée de fil et présente donc des pertes ohmiques
* De plus, l’*effet de peau* intervient

---
[question:AC202]

--- style="font-size: smaller;"
### Réactance inductive $X_{\textrm{L}}$

Une bobine connectée à une tension alternative fait varier en permanence le champ magnétique $\rightarrow$ impédance / réactance inductive

1. Si la fréquence de la tension alternative aux bornes d’une bobine augmente, le courant diminue ; cela signifie que la réactance inductive devient plus grande.
2. Si l’inductance de la bobine augmente, le courant diminue également, c’est-à-dire que la réactance devient aussi plus grande.

<fragment>
$|X_{\textrm{L}}| = \omega \cdot L = 2\pi \cdot f \cdot L$
</fragment>

---
[question:AC203]
---
[question:AC204]
---
#### Méthode de résolution
* donné : $L = \qty{3}{\micro\henry}$
* donné : $f = \qty{100}{\mega\hertz}$
* recherché : $X_{\textrm{L}}$

<fragment>
$\begin{split} |X_{\textrm{L}}| &= \omega \cdot L = 2\pi \cdot f \cdot L\\ &= 2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{3}{\micro\henry}\\ &\approx \qty{1885}{\ohm} \end{split}$
</fragment>

---
### Augmentation de l’inductance
<left>
Bobine cylindrique
<fragment>
$L = \dfrac{\mu_0 \cdot \mu_r \cdot N^2 \cdot A_S}{l}$
</fragment>

* Augmenter le nombre de spires $N$
* Réduire la longueur de la bobine $l$
* Agrandir la surface de la section transversale $A_S$ de la bobine

</left>
<right>
Bobine à noyau toroïdal
<fragment>
$L = N^2 \cdot A_{\textrm{L}}$
</fragment>

* Augmenter le nombre de spires $N$
* Utiliser un *matériau* plus conducteur magnétiquement (avec une constante d’inductance $A_{\textrm{L}}$ plus élevée) comme noyau

</right>

<note>
C’est pourquoi on utilise des noyaux (toroïdaux)
</note>
---
[question:AC211]

---
[question:AC205]
---
#### Méthode de résolution
* donné : $N = 14$
* donné : $A_{\textrm{L}} = \qty{1,5}{\nano\henry}$
* recherché : $L$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ &= 14^2 \cdot \qty{1,5}{\nano\henry}\\ &= \qty{0,294}{\micro\henry} \end{split}$
</fragment>

---
[question:AC206]
---
#### Méthode de résolution
* donné : $N = 300$
* donné : $A_{\textrm{L}} = \qty{1250}{\nano\henry}$
* recherché : $L$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ &= 300^2 \cdot \qty{1250}{\nano\henry}\\ &= \qty{112,5}{\milli\henry} \end{split}$
</fragment>

---
[question:AC207]
---
#### Méthode de résolution
* donné : $L = \qty{2}{\milli\henry}$
* donné : $A_{\textrm{L}} = \qty{250}{\nano\henry}$
* recherché : $N$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ N &= \sqrt{\frac{L}{A_{\textrm{L}}}} = \sqrt{\frac{\qty{2}{\milli\henry}}{\qty{250}{\nano\henry}}} \\ &= 89\,\text{spires} \end{split}$
</fragment>

---
[question:AC208]
---
#### Méthode de résolution
* donné : $L = \qty{12}{\micro\henry}$
* donné : $A_{\textrm{L}} = \qty{30}{\nano\henry}$
* recherché : $N$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ N &= \sqrt{\frac{L}{A_{\textrm{L}}}} = \sqrt{\frac{\qty{12}{\micro\henry}}{\qty{30}{\nano\henry}}} \\ &= 20\,\text{spires} \end{split}$
</fragment>

---
### Pertes des bobines

* Facteur de perte $\tan(\delta) = \frac{R}{X_L}$
* Pertes dans le conducteur

---
[question:AC209]

---
### Impédance

* Montage en *série* d’une réactance et d’une résistance active $\rightarrow$ impédance $Z$
* N’apparaît qu’en courant alternatif
* Ne peut pas être mesurée avec un ohmmètre
* Bobine en radioélectricité $\rightarrow$ *impédance*
* Impédance d’antenne, impédance d’entrée et de sortie, adaptateurs d’impédance, etc.
* Impédance $Z$ en $\unit{\ohm}$

---
<left>
[picture:1067:a_impedanzdreieck:Impédance $Z$ comme addition géométrique de $R$ et $X$]
  
$Z = \sqrt{R^2 + X^2}$
</left>
<right>
* Résistance active $R$
* Réactance $X_{\textrm{L}}$
* L’impédance se calcule par le théorème de Pythagore
</right>

---
[question:AA101]

---
### Blindage des champs magnétiques

<left>
* Pour le blindage : un boîtier en *matériau* très conducteur.
* Exemple : godet de blindage en acier ou en fer.
* Noyau ferrite réglable pour modifier l’inductance.
</left>
<right>
[photo:333:a_abschirmbecher:Exemple de bobines avec godet de blindage pour le blindage des champs magnétiques]
</right>


---
[question:AC210]
