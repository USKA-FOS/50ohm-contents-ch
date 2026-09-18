## Fondamentale et harmoniques

* Un signal sinusoïdal idéal ne contient que sa fondamentale (1re harmonique)
* Les écarts par rapport à la forme sinusoïdale génèrent des multiples entiers de la fréquence fondamentale
* Ces multiples sont appelés harmoniques

--- style="font-size: smaller;"
### Représentation dans le spectre de fréquences

<left>
[picture:869:zusammenhang_oberwellen_harmonische:Relation entre harmoniques supérieures et harmoniques]
</left>
<right>
* 1re harmonique = fréquence fondamentale
* 2e harmonique = fréquence double de la fondamentale
* 3e harmonique = fréquence triple de la fondamentale
* Toutes les harmoniques sont numérotées avec un ordre (n)
</right>
<note>
Selon la distorsion du signal, il se forme davantage d'harmoniques paires ou impaires.
Les signaux rectangulaires (par exemple, dus à la saturation d'un amplificateur) contiennent principalement des harmoniques impaires.
Les signaux en dents de scie contiennent principalement des harmoniques paires.
</note>

--- style="font-size: smaller;"
### Harmoniques supérieures – multiples de la fréquence fondamentale

<left>
[picture:595:a_oberwellen:Signal composé de la fondamentale et d'harmoniques supérieures]
</left>
<right>
* Un signal non parfaitement sinusoïdal contient en plus des harmoniques supérieures
* Les harmoniques supérieures sont des multiples entiers de la fréquence fondamentale
* 1re harmonique supérieure = 2e harmonique = fréquence double de la fondamentale
* 2e harmonique supérieure = 3e harmonique = fréquence triple de la fondamentale
</right>

---
[question:AB403]

---
[question:AB401]

---
[question:AB402]

---
## Analyse des harmoniques supérieures avec un analyseur de spectre

* Même un signal apparemment sinusoïdal peut contenir des harmoniques supérieures notables
* Les composantes des harmoniques supérieures sont mesurées avec un analyseur de spectre
* Représentation dans le domaine fréquentiel (domaine des fréquences)
* Les amplitudes des harmoniques supérieures sont affichées de manière logarithmique

---
[question:AI615]

---
[question:AI614]

---
## Calcul des harmoniques et des harmoniques supérieures

* Fréquences des harmoniques = fréquence fondamentale × ordre (n)
* Fréquences des harmoniques supérieures = fréquence fondamentale × (n + 1)

---
[question:AJ201]

---
#### Méthode de résolution
* donné : $f = \qty{3,730}{\mega\hertz}$
* recherché : $f$ de la 2e harmonique

<fragment>
$2 \cdot f = 2 \cdot \qty{3,730}{\mega\hertz} = \qty{7,460}{\mega\hertz}$
</fragment>

---
[question:AJ205]

---
#### Méthode de résolution
* donné : $f = \qty{144,690}{\mega\hertz}$
* recherché : $f$ en tant que 2e harmonique impaire

<fragment>
2e harmonique impaire = 3e harmonique

$3 \cdot f = 3 \cdot \qty{144,690}{\mega\hertz} = \qty{434,070}{\mega\hertz}$
</fragment>
---
[question:AJ202]

---
#### Méthode de résolution
* donné : $f = \qty{7,050}{\mega\hertz}$
* recherché : $f$ en tant que 3e harmonique

<fragment>
$3 \cdot f = 3 \cdot \qty{7,050}{\mega\hertz} = \qty{21,150}{\mega\hertz}$
</fragment>

---
[question:AJ206]

---
#### Méthode de résolution
* donné : $f = \qty{144,300}{\mega\hertz}$
* recherché : plusieurs harmoniques

<fragment>
$\begin{split}2 \cdot \qty{144,300}{\mega\hertz} &= \qty{288,600}{\mega\hertz}\\ 3 \cdot \qty{144,300}{\mega\hertz} &= \bold{\qty{432,900}{\mega\hertz}}\\ &\vdots\\ 9 \cdot \qty{144,300}{\mega\hertz} &= \bold{\qty{1298,700}{\mega\hertz}}\end{split}$
</fragment>