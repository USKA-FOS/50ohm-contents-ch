## Onde fondamentale et harmoniques

* Un signal sinusoïdal idéal ne contient que son onde fondamentale (1ère harmonique)
* Les écarts par rapport à la forme sinusoïdale génèrent des multiples entiers de la fréquence fondamentale
* Ces multiples sont appelés harmoniques

--- style="font-size: smaller;"
### Représentation dans le spectre de fréquences

<left>
[picture:869:zusammenhang_oberwellen_harmonische:Relation entre les harmoniques supérieures et les harmoniques]
</left>
<right>
* 1ère harmonique = fréquence fondamentale
* 2ème harmonique = double de la fréquence fondamentale
* 3ème harmonique = triple de la fréquence fondamentale
* Toutes les harmoniques sont numérotées avec un nombre ordinal (n)
</right>
<note>
Selon la distorsion du signal, plus d'harmoniques paires ou impaires sont générées.
Les signaux rectangulaires (par exemple, par surcharge de l'amplificateur) contiennent principalement des harmoniques impaires.
Les signaux en dents de scie contiennent principalement des harmoniques paires.
</note>

--- style="font-size: smaller;"
### Harmoniques supérieures – Multiples de la fréquence fondamentale

<left>
[picture:595:a_oberwellen:Signal composé d'onde fondamentale et d'harmoniques supérieures]
</left>
<right>
* Un signal non idéalement sinusoïdal contient en outre des harmoniques supérieures
* Les harmoniques supérieures sont des multiples entiers de la fréquence fondamentale
* 1ère harmonique supérieure = 2ème harmonique = double de la fréquence fondamentale
* 2ème harmonique supérieure = 3ème harmonique = triple de la fréquence fondamentale
</right>

---
[question:AB403]

---
[question:AB401]

---
[question:AB402]

---
## Analyse des harmoniques supérieures avec l'analyseur de spectre

* Même un signal apparemment sinusoïdal peut contenir des harmoniques supérieures significatives
* Les composantes des harmoniques supérieures sont mesurées avec un analyseur de spectre
* Représentation dans le domaine des fréquences (Frequency-Domain)
* Les amplitudes des harmoniques supérieures sont affichées de manière logarithmique

---
[question:AI615]

---
[question:AI614]

---
## Calcul des harmoniques et des harmoniques supérieures

* Fréquences harmoniques = fréquence fondamentale × nombre ordinal (n)
* Fréquences des harmoniques supérieures = fréquence fondamentale × (n + 1)

---
[question:AJ201]

---
#### Solution
* donné : $f = \qty{3,730}{\mega\hertz}$
* recherché : $f$ de la 2ème harmonique

<fragment>
$2 \cdot f = 2 \cdot \qty{3,730}{\mega\hertz} = \qty{7,460}{\mega\hertz}$
</fragment>

---
[question:AJ205]

---
#### Solution
* donné : $f = \qty{144,690}{\mega\hertz}$
* recherché : $f$ en tant que 2ème harmonique impaire

<fragment>
2ème harmonique impaire = 3ème harmonique
  
$3 \cdot f = 3 \cdot \qty{144,690}{\mega\hertz} = \qty{434,070}{\mega\hertz}$
</fragment>
---
[question:AJ202]

---
#### Solution
* donné : $f = \qty{7,050}{\mega\hertz}$
* recherché : $f$ en tant que 3ème harmonique

<fragment>
$3 \cdot f = 3 \cdot \qty{7,050}{\mega\hertz} = \qty{21,150}{\mega\hertz}$
</fragment>

---
[question:AJ206]

---
#### Solution
* donné : $f = \qty{144,300}{\mega\hertz}$
* recherché : plusieurs harmoniques

<fragment>
$\begin{split}2 \cdot \qty{144,300}{\mega\hertz} &= \qty{288,600}{\mega\hertz}\\ 3 \cdot \qty{144,300}{\mega\hertz} &= \bold{\qty{432,900}{\mega\hertz}}\\ &\vdots\\ 9 \cdot \qty{144,300}{\mega\hertz} &= \bold{\qty{1298,700}{\mega\hertz}}\end{split}$
</fragment>
