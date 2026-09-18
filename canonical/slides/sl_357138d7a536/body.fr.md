## Fréquence de coupure

Pour les filtres passe-haut et passe-bas, la fréquence de coupure est définie par :

<left>
Pour les circuits RL
$R = X_\text{L}$
$f_\text{g} = \frac{R}{2 \pi \cdot L}$
</left>
<right>
Pour les circuits RC
$R = X_\text{C}$
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C}$
</right>


---
[question:AD201]
---
#### Méthode de résolution
* donné : $R = \qty{4,7}{\kilo\ohm}$
* donné : $C = \qty{2,2}{\nano\farad}$
* recherché : $f_\text{g}$

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C} = \frac{1}{2 \pi \cdot \qty{4,7}{\kilo\ohm} \cdot \qty{2,2}{\nano\farad}} \approx \qty{15,4}{\kilo\hertz}$
</fragment>
---
[question:AD202]
---
#### Méthode de résolution
* donné : $R = \qty{10}{\kilo\ohm}$
* donné : $C = \qty{47}{\nano\farad}$
* recherché : $f_\text{g}$

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R \cdot C} = \frac{1}{2 \pi \cdot \qty{10}{\kilo\ohm} \cdot \qty{47}{\nano\farad}} \approx \qty{339}{\hertz}$
</fragment>
---
[question:AD203]
---
#### Méthode de résolution
* donné : $R_1 = \qty{4,7}{\kilo\ohm}$
* donné : $C_1 = \qty{6,8}{\nano\farad}$
* recherché : $f_\text{g}$

<fragment>
$C_2$ et toutes les autres données sont sans importance pour le filtre passe-bas.
</fragment>

<fragment>
$f_\text{g} = \frac{1}{2 \pi \cdot R_1 \cdot C_1} = \frac{1}{2 \pi \cdot \qty{4,7}{\kilo\ohm} \cdot \qty{6,8}{\nano\farad}} \approx \qty{5}{\kilo\hertz}$
</fragment>
---
## Fréquence de résonance

* Montage en parallèle ou en série d’une bobine et d’un condensateur → circuit oscillant
* Hautes fréquences → impédance élevée de la bobine
* Basses fréquences → impédance élevée du condensateur
* Il existe une fréquence pour laquelle la bobine et le condensateur présentent la même impédance → *fréquence de résonance*

---
[question:AD206]
--- style="font-size: smaller;"
## Circuit oscillant parallèle

[picture:233:a_schwingkreis_parallelschwingkreis:Circuit oscillant parallèle et représentation de l’impédance en fonction de la fréquence]

* Les composants idéaux se chargent et se déchargent en permanence
* En théorie, l’impédance à la fréquence de résonance est infiniment élevée
* En pratique, c’est le composant présentant la plus faible résistance qui détermine l’impédance totale
* Aux fréquences supérieures ou inférieures à la fréquence de résonance, l’impédance du circuit oscillant parallèle est plus faible

--- style="font-size: smaller;"
## Circuit oscillant série

[picture:230:a_schwingkreis_reihenschwingkreis:Circuit oscillant série et représentation de l’impédance en fonction de la fréquence]

* Ou circuit oscillant en série
* En théorie, l’impédance à la fréquence de résonance est de $\qty{0}{\ohm}$
* En pratique, l’impédance est déterminée par la résistance ohmique
* Aux fréquences supérieures ou inférieures à la fréquence de résonance, l’impédance du circuit oscillant série est plus élevée

---
[question:AD207]
---
[question:AD204]
---
## Cas de résonance

Pour les circuits oscillants parallèle et série :

$X_\text{C} = X_\text{L}$

Les impédances sont de même valeur.

<fragment>
Fréquence de résonance selon la formule du circuit oscillant de Thomson :

$f_0 = \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}$
</fragment>

<note>
William Thomson, plus tard Lord Kelvin, en 1853
</note>
---


[question:AD208]
---
#### Méthode de résolution
* donné : $L = \qty{1,2}{\micro\henry}$
* donné : $C = \qty{6,8}{\pico\farad}$
* donné : $R = \qty{10}{\ohm}$
* recherché : $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{1,2}{\micro\henry} \cdot \qty{6,8}{\pico\farad}}} \approx \qty{55,7}{\mega\hertz} \end{split}$
</fragment>
<fragment>
La résistance $R$ n’est pas nécessaire pour le calcul.
</fragment>
---
[question:AD209]
---
#### Méthode de résolution
* donné : $L = \qty{10}{\micro\henry}$
* donné : $C = \qty{1}{\nano\farad}$
* recherché : $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{10}{\micro\henry} \cdot \qty{1}{\nano\farad}}} \approx \qty{1,592}{\mega\hertz} \end{split}$
</fragment>
---
[question:AD210]
---
#### Méthode de résolution
* donné : $L = \qty{100}{\micro\henry}$
* donné : $C = \qty{0,01}{\micro\farad}$
* recherché : $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{100}{\micro\henry} \cdot \qty{0,01}{\micro\farad}}} \approx \qty{159}{\kilo\hertz} \end{split}$
</fragment>
---
[question:AD211]
---
#### Méthode de résolution
* donné : $L = \qty{2,2}{\micro\henry}$
* donné : $C = \qty{56}{\pico\farad}$
* recherché : $f_0$

<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{2,2}{\micro\henry} \cdot \qty{56}{\pico\farad}}} \approx \qty{14,34}{\mega\hertz} \end{split}$
</fragment>
---
[question:AD212]
--- style="font-size: 0.7em;"
#### Méthode de résolution
* donné : $C_1 = \qty{0,1}{\nano\farad}$
* donné : $C_2 = \qty{1,5}{\nano\farad}$
* donné : $C_3 = \qty{220}{\pico\farad}$
* donné : $L = \qty{1,2}{\milli\henry}$
* recherché : $f_0$

<fragment>
$C = C_1 + C_2 + C_3 = \qty{0,1}{\nano\farad} + \qty{1,5}{\nano\farad} + \qty{220}{\pico\farad} = \qty{1,82}{\nano\farad}$
</fragment>
<fragment>
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{1,2}{\milli\henry} \cdot \qty{1,82}{\nano\farad}}} \approx \qty{107,7}{\kilo\hertz} \end{split}$
</fragment>
---
### Modification de la fréquence de résonance

* Bobine ou condensateur plus grand → fréquence de résonance plus basse
* Bobine ou condensateur plus petit → fréquence de résonance plus élevée

<fragment>
Augmenter l’inductance
* Augmenter le nombre de spires
* Resserrer les spires
* Introduire un noyau en ferrite

</fragment>

---
[question:AD213]
---
[question:AD214]
---
[question:AD215]
---
[question:AD216]
---
[question:AD217]
---
### Circuit oscillant commandé par tension

[picture:752:a_schwingkreis_potentiometer:Modification de la capacité par une varicap]

* La varicap est modifiée par une tension de commande appliquée au diviseur de tension résistif
* Tension plus faible aux bornes de la varicap → jonction plus fine dans la varicap → capacité plus grande
* Condensateurs montés en série → capacité plus faible → fréquence de résonance plus élevée

---
[question:AD218]
--- style="font-size: smaller;"
## Filtre passe-bande

[picture:785:a_schwingkreis_bandpass:Filtre passe-bande composé de plusieurs circuits oscillants]

* Combinaison de circuits oscillants parallèle et série
* Laisse passer une bande de fréquences spécifique
* Les circuits oscillants parallèles se comportent comme des résistances de forte valeur
* Le circuit oscillant série se comporte comme une résistance de faible valeur

---
[question:AD205]
---
## Bande passante

* Forte dépendance à la résistance ohmique
* Exprimée en dB par rapport à une valeur de référence du filtre
* Ex. : *bande passante* à la valeur de $\qty{-3}{\dB}$
* Une puissance de signal réduite de moitié peut encore traverser le filtre
* Ou une tension de signal égale à 0,7 fois la tension initiale

---
[question:AD219]
---
[question:AD220]
---
### Bandes passantes courantes

* Bande étroite de $\qty{500}{\hertz}$ pour la télégraphie (CW)
* Bande large de $\qty{2,7}{\kilo\hertz}$ pour la modulation vocale (SSB)

---
[question:AD221]
---
[question:AD222]
---
## Facteur de qualité d’un circuit oscillant

* Ou facteur Q
* Caractérise les pertes d’énergie
* Rapport des réactances à la résistance ohmique en cas de résonance ($X_\text{L} = X_\text{C}$)

<fragment>
<left>
Circuit oscillant série
$Q = \frac{f_0}{BP} = \frac{X_\text{L}}{R_\text{S}}$
</left>
<right>
Circuit oscillant parallèle
$Q = \frac{f_0}{BP} = \frac{R_\text{P}}{X_\text{L}}$
</right>
</fragment>
  
---
[question:AD225]
--- style="font-size: 0.7em;"
#### Méthode de résolution
<left>
* donné : $L = \qty{100}{\micro\henry}$
* donné : $C = \qty{0,01}{\micro\farad}$
</left>
<right>
* donné : $R_\text{S} = \qty{10}{\ohm}$
* recherché : $Q$
</right>

<fragment>
Calculer d’abord $f_0$
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{100}{\micro\henry} \cdot \qty{0,01}{\micro\farad}}} \approx \qty{159,2}{\kilo\hertz} \end{split}$
</fragment>
<fragment>
Calculer ensuite $BP$ ou $X_\text{L}$
$\begin{split} X_\text{L} &= \omega \cdot L = 2 \pi \cdot f_0 \cdot L\\ &= 2 \pi \cdot \qty{159,2}{\kilo\hertz} \cdot \qty{100}{\micro\henry} \approx \qty{100,03}{\ohm} \end{split}$
</fragment>
<fragment>
$Q = \frac{X_\text{L}}{R_\text{S}} = \frac{\qty{100,03}{\ohm}}{\qty{10}{\ohm}} \approx 10$
</fragment>
---
[question:AD226]
--- style="font-size: 0.7em;"
#### Méthode de résolution
<left>
* donné : $L = \qty{2,2}{\micro\henry}$
* donné : $C = \qty{56}{\pico\farad}$
</left>
<right>
* donné : $R_\text{P} = \qty{1}{\kilo\ohm}$
* recherché : $Q$
</right>

<fragment>
Calculer d’abord $f_0$
$\begin{split} f_0 &= \frac{1}{2 \pi \cdot \sqrt{L \cdot C}}\\ &= \frac{1}{2 \pi \cdot \sqrt{\qty{2,2}{\micro\henry} \cdot \qty{56}{\pico\farad}}} \approx \qty{14,34}{\mega\hertz} \end{split}$
</fragment>
<fragment>
Calculer ensuite $BP$ ou $X_\text{L}$
$\begin{split} X_\text{L} &= \omega \cdot L = 2 \pi \cdot f_0 \cdot L\\ &= 2 \pi \cdot \qty{14,34}{\mega\hertz} \cdot \qty{2,2}{\micro\henry} \approx \qty{198,2}{\ohm} \end{split}$
</fragment>
<fragment>
$Q = \frac{R_\text{P}}{X_\text{L}} = \frac{\qty{1}{\kilo\ohm}}{\qty{198,2}{\ohm}} \approx 5$
</fragment>
---
### Calcul de la bande passante

À partir de la fréquence de résonance et du facteur de qualité

$Q = \frac{f_0}{BP} \Rightarrow BP = \frac{f_0}{Q}$

<fragment>
Ou en utilisant la formule du circuit oscillant de Thomson

<left>
Circuit oscillant série
$BP = \frac{R_\text{S}}{2 \pi \cdot L}$
</left>
<right>
Circuit oscillant parallèle
$BP = \frac{1}{2 \pi \cdot R_\text{P} \cdot C}$
</right>
</fragment>
<note>
Démonstration non présentée
</note>

---
[question:AD224]
---
#### Méthode de résolution
* donné : $L = \qty{2,2}{\micro\henry}$
* donné : $C = \qty{56}{\pico\farad}$
* donné : $R_\text{P} = \qty{1}{\kilo\ohm}$
* recherché : $BP$

<fragment>
$\begin{split} BP &= \frac{1}{2 \pi \cdot R_\text{P} \cdot C}\\ &= \frac{1}{2 \pi \cdot \qty{1}{\kilo\ohm} \cdot \qty{56}{\pico\farad}} \approx \qty{2,84}{\mega\hertz} \end{split}$
</fragment>

---
[question:AD223]
---
#### Méthode de résolution
* donné : $L = \qty{100}{\micro\henry}$
* donné : $C = \qty{0,01}{\micro\farad}$
* donné : $R_\text{S} = \qty{10}{\ohm}$
* recherché : $BP$

<fragment>
$BP = \frac{R_\text{S}}{2 \pi \cdot L} = \frac{\qty{10}{\ohm}}{2 \pi \cdot \qty{100}{\micro\henry}} \approx \qty{15,9}{\kilo\hertz}$
</fragment>
--- style="font-size: 0.7em;" data-transition="none"
## Couplage

[picture:184:a_schwingkreis_kopplung:Couplage inductif de deux circuits oscillants et diagramme de tension en fonction de la fréquence]

* Les circuits oscillants couplés sont souvent utilisés entre les étages de circuits ou dans les filtres
* Deux circuits oscillants couplés par induction ou par capacité
* Le degré de couplage détermine l’influence mutuelle, la bande passante et la courbe d’atténuation

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Couplage inductif de deux circuits oscillants et diagramme de tension en fonction de la fréquence]

* d : *couplage lâche* → influence mutuelle quasi nulle, forte atténuation d’insertion et bande passante très étroite
* c : *couplage sous-critique* → influence mutuelle quasi nulle, atténuation d’insertion élevée et bande passante étroite

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Couplage inductif de deux circuits oscillants et diagramme de tension en fonction de la fréquence]

* b : *couplage critique* → influence mutuelle modérée, courbe d’atténuation plate avec faible atténuation et plateau dans la bande passante ainsi qu’une bonne bande passante

--- style="font-size: 0.7em;" data-transition="none"
[picture:184:a_schwingkreis_kopplung:Couplage inductif de deux circuits oscillants et diagramme de tension en fonction de la fréquence]
* a : *couplage surcritique* → influence mutuelle forte, modification des fréquences de résonance, grande bande passante et distorsion de la courbe d’atténuation dans la bande passante avec des "creux"

---
[question:AD227]
---
[question:AD228]
---
[question:AD229]
