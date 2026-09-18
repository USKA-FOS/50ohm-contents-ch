## Fréquence maximale utilisable (MUF)

<left>
* Classe E : Fréquence maximale à laquelle une liaison peut être établie par onde spatiale
</left>
<right>
[picture:997:e_muf_luf2:Simulation des distances de saut pour différentes fréquences et une MUF d'environ $\qty{7,5}{\mega\hertz}$ lors d'une nuit d'août 2024 avec un angle de rayonnement de $\qty{45}{\degree}$]
</right>

---

## Fréquence maximale utilisable (MUF)

<left>
* Classe A : Dépend de l'angle de rayonnement $\alpha$
</left>
<right>
[picture:870:e_muf_winkel:Les angles pour le calcul de la MUF]
</right>

---

## Fréquence maximale utilisable (MUF)

<left>
* Si l'on émet avec un angle raide (par ex. $\qty{60}{\degree}$), la MUF diminue et l'onde radio n'est plus réfractée.
* Si l'on émet avec un angle plat (par ex. $\qty{30}{\degree}$), la MUF augmente.
</left>
<right>
[picture:998:e_muf_winkel2:Distance de saut à 7 MHz en été 2024]
</right>

---

[question:AH206]

---

[question:AH207]

---

## Fréquence critique

<left>
* Avec un angle de rayonnement de $\qty{90}{\degree}$, le signal doit effectuer un virage de $\qty{180}{\degree}$ dans l'ionosphère
* Fréquence critique $f_c$ à laquelle le signal est réfléchi
* La MUF est supérieure à $f_c$, car en général, l'émission n'est pas verticale
</left>
<right>
[picture:870:e_muf_winkel:Les angles pour le calcul de la MUF]
<fragment>
$\mathrm{MUF} \approx \frac{f_c}{\sin(\alpha)}$
</fragment>
</right>

<note>
La fréquence critique est aussi indiquée par $f_k$ ou $f_\mathrm{krit}$
</note>

---

## Exemple : Ionosonde Juliusruh


[picture:999:e_muf_fof2:MUF 3000 (Émission plate) et $f_\text{c}$ le 08.09.2025]


---

[question:AH208]


---

*style="font-size: smaller;"*
## Fréquence optimale


* La planification des fréquences commerciales utilise une *Frequency of optimal transmition*, fréquence d'émission optimale
* Fréquence qui permet statistiquement une liaison radio sur un trajet donné 90% des jours
* Se situe 15% en dessous de la moyenne mensuelle de la MUF
* $f_{\mathrm{opt}} = \mathrm{MUF}\cdot 0,85$
* Joue un rôle mineur en radioamateurisme, car aucune liaison permanente n'est établie
* En radioamateurisme, on travaille jusqu'à proximité de la MUF

---
[question:AH209]
---
### Méthode de résolution
<left>
* donné : $\alpha = \qty{45}{\degree}$
* donné : $f_c = 3\text{MHz}$
</left>
<right>
* recherché : $\mathrm{MUF}$
* recherché : $f_{\mathrm{opt}}$
</right>

<left>
<fragment>
$\begin{split} \text{MUF} & \approx \frac{f_c}{\sin(\alpha)}\\n&\approx \frac{\qty{3}{\mega\hertz}}{\num{0,71}}\\n&\approx \qty{4,2}{\mega\hertz}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split} f_{\mathrm{opt}} &= \mathrm{MUF}\cdot 0,85\\ &= \qty{4,2}{\mega\hertz} \cdot 0,85\\ &= \qty{3,6}{\mega\hertz} \end{split}$
</fragment>
</right>

---

## Fréquence minimale utilisable (LUF)

Fréquence minimale à laquelle une liaison peut être établie par onde spatiale

---
[question:AH210]
---
[question:AH211]
---

## Fréquence critique

<left>
[picture:870:e_muf_winkel:Les angles pour le calcul de la MUF]
Rappel
</left>
<right>
* Avec un angle de rayonnement de $\qty{90}{\degree}$, le signal doit effectuer un virage de $\qty{180}{\degree}$ dans l'ionosphère
* Fréquence critique $f_c$ à laquelle le signal est réfléchi
* La MUF est supérieure à $f_c$, car en général, l'émission n'est pas verticale
</right>

<note>
La fréquence critique est aussi indiquée par $f_k$ ou $f_\mathrm{krit}$
</note>
---

* La fréquence critique varie selon la région ionosphérique, la position et le temps
* Des indications séparées sont possibles pour chaque région ionosphérique
* Symbole : fo
* Complétée par la couche, par ex. foF2

<note>
fo avec un petit "o" pour l'onde ordinaire
</note>
---
[question:AH204]
---
[question:AH205]