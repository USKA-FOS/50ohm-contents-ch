[image:810:doppelsuper_blockschaltbild:Schéma bloc d'un double superhétérodyne]

1. Partie HF avec présélection
2. Premier mélangeur avec oscillateur local
3. Premier amplificateur FI avec filtre *Roofing*
4. Deuxième mélangeur avec oscillateur de conversion

--- data-transition="none"
[image:810:doppelsuper_blockschaltbild:Schéma bloc d'un double superhétérodyne]

5. Deuxième amplificateur FI avec filtre
6. Troisième mélangeur en tant que détecteur de produit ou démodulateur, éventuellement avec oscillateur de battement
7. Amplificateur BF

--- data-transition="none"
[image:810:doppelsuper_blockschaltbild:Schéma bloc d'un double superhétérodyne]

* Utilisation de deux fréquences intermédiaires
* 1ère FI élevée → bonne suppression de la fréquence image
* 2ème FI basse → haute sélectivité

---
* Après la 1ère FI, un filtre d'entrée est placé avant le 2ème mélangeur
* La fréquence image peut être bien supprimée grâce à un grand écart
* Après la 2ème FI, un filtre à haut facteur de qualité
* Facile à réaliser pour des fréquences basses
* Éloigner la FI et la fréquence de réception souhaitée → éviter la réception directe de la FI
* La 1ère FI devrait être le double de la fréquence de réception maximale

---
[question:AF112]
---
[question:AF113]
---
[question:AF114]
---
### Filtre *Roofing*

* Filtre étroit (*Roofing Filter*) après le 1er mélangeur
* Accordé sur la 1ère FI
* Bande passante au moins aussi grande que la plus grande largeur de bande de réception nécessaire

---
[question:AF116]
---
[question:AF209]
---
[question:AF117]
---
### Fréquences des oscillateurs
* Les fréquences des oscillateurs sont respectivement au-dessus ou en dessous de la fréquence d'entrée souhaitée
* Il existe deux solutions possibles pour chaque mélangeur

<fragment>
1. $f_\text{OSC} = f_\text{FI}\,+\,f_\text{E}$
2. $f_\text{OSC} = f_\text{FI}\,-\,f_\text{E}$
</fragment>

---
[question:AF210]
--- style="font-size: smaller;"
#### Méthode de résolution
* donné : $f_\text{E} = 3\dots\qty{30}{\mega\hertz}$
* donné : $f_\text{FI1} = \qty{50}{\mega\hertz}$
* recherché : $f_\text{OSC}$

<fragment>
$f_\text{FI} = |f_\text{E} − f_\text{OSC}| \Rightarrow f_\text{OSC} = f_\text{FI} \pm f_\text{E}$
</fragment>
<fragment>
<left>
1. Solution :
$\begin{split}f_\text{OSC} &= f_\text{FI} \, + \, f_\text{E}\\ &= \qty{50}{\mega\hertz} \, + \, 3\dots\qty{30}{\mega\hertz}\\ &= 53\dots\qty{80}{\mega\hertz}\end{split}$
</left>
</fragment>
<fragment>
<right>
2. Solution :
$\begin{split}f_\text{OSC} &= f_\text{FI} \, - \, f_\text{E}\\ &= \qty{50}{\mega\hertz} \, - \, 3\dots\qty{30}{\mega\hertz}\\ &= 47\dots\qty{20}{\mega\hertz}\end{split}$
</right>
</fragment>
---
[question:AF120]
--- style="font-size: smaller;"
### Méthode de résolution
<left>
* donné : $f_\text{E} = \qty{3,65}{\mega\hertz}$
* donné : $f_\text{FI1} = \qty{50}{\mega\hertz}$
</left>
<right>
* donné : $f_\text{FI2} = \qty{9}{\mega\hertz}$
* donné : $f_\text{BF} = \qty{455}{\kilo\hertz}$
</right>
* recherché : $f_\text{OSC}$ pour $f_\text{VFO}$, $f_\text{CO1}$, $f_\text{CO2}$

<fragment>
$f_\text{FI1} = \begin{cases}f_\text{E}\,+\,f_\text{OSC}\\ f_\text{OSC}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSC}\end{cases} \Rightarrow f_\text{OSC} = \begin{cases}f_\text{FI}\,-\,f_\text{E}\\ f_\text{E}\,+\,f_\text{FI}\\ f_\text{E}\,-\,f_\text{FI}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = \begin{cases}f_\text{FI1}\,-\,f_\text{E} = \qty{50}{\mega\hertz}\,-\,\qty{3,65}{\mega\hertz} = \qty{46,35}{\mega\hertz}\\ f_\text{E}\,+\,f_\text{FI1} = \qty{3,65}{\mega\hertz}\,+\,\qty{50}{\mega\hertz} = \qty{53,65}{\mega\hertz}\\ f_\text{E}\,-\,f_\text{FI1} = \qty{3,65}{\mega\hertz}\,-\,\qty{50}{\mega\hertz} = \cancel{\qty{-46,35}{\mega\hertz}}\end{cases}$
</fragment>
--- style="font-size: smaller;"
<fragment>
$f_\text{CO1} = \begin{cases}f_\text{FI2}\,-\,f_\text{FI1} = \qty{9}{\mega\hertz}\,-\,\qty{50}{\mega\hertz} = \cancel{\qty{-41}{\mega\hertz}}\\ f_\text{FI1}\,+\,f_\text{FI2} = \qty{50}{\mega\hertz}\,+\,\qty{9}{\mega\hertz} = \qty{59}{\mega\hertz}\\ f_\text{FI1}\,-\,f_\text{FI2} = \qty{50}{\mega\hertz}\,-\,\qty{9}{\mega\hertz} = \qty{41}{\mega\hertz}\end{cases}$
</fragment>
<fragment>
$f_\text{CO2} = \begin{cases}f_\text{BF}\,-\,f_\text{FI2} = \qty{455}{\kilo\hertz}\,-\,\qty{9}{\mega\hertz} = \cancel{\qty{-8,545}{\mega\hertz}}\\ f_\text{FI2}\,+\,f_\text{BF} = \qty{9}{\mega\hertz}\,+\,\qty{455}{\kilo\hertz} = \qty{9,455}{\mega\hertz}\\ f_\text{FI2}\,-\,f_\text{BF} = \qty{9}{\mega\hertz}\,-\,\qty{455}{\kilo\hertz} = \qty{8,545}{\mega\hertz}\end{cases}$
</fragment>
<fragment>
VFO : $\bold{\qty{46,35}{\mega\hertz}} \And \qty{53,65}{\mega\hertz}$, CO1 : $\bold{\qty{41}{\mega\hertz}} \And \qty{59}{\mega\hertz}$, CO2 : $\qty{8,545}{\mega\hertz} \And \bold{\qty{9,455}{\mega\hertz}}$
</fragment>
---
[question:AF118]
--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $f_\text{E} = \qty{21,1}{\mega\hertz}$
* donné : $f_\text{FI1} = \qty{9}{\mega\hertz}$
</left>
<right>
* donné : $f_\text{FI2} = \qty{460}{\kilo\hertz}$
</right>
* recherché : $f_\text{VFO} > f_\text{E}$, $f_\text{CO} < f_\text{FI1}$

<fragment>
$f_\text{FI} = \begin{cases}f_\text{OSC}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSC}\end{cases} \Rightarrow f_\text{OSC} = \begin{cases}f_\text{E}\,+\,f_\text{FI}\\ f_\text{E}\,-\,f_\text{FI}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = f_\text{E}\,+\,f_\text{FI1} = \qty{21,1}{\mega\hertz}\,+\,\qty{9}{\mega\hertz} = \qty{30,1}{\mega\hertz}$
</fragment>
<fragment>
$f_\text{CO} = f_\text{FI1}\,-\,f_\text{FI2} = \qty{9}{\mega\hertz}\,-\,\qty{460}{\kilo\hertz} = \qty{8,54}{\mega\hertz}$
</fragment>

---
[question:AF119]
--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $f_\text{E} = \qty{28}{\mega\hertz}$
* donné : $f_\text{FI1} = \qty{10,7}{\mega\hertz}$
</left>
<right>
* donné : $f_\text{FI2} = \qty{460}{\kilo\hertz}$
</right>
* recherché : $f_\text{VFO} > f_\text{E}$, $f_\text{CO} > f_\text{FI1}$

<fragment>
$f_\text{FI} = \begin{cases}f_\text{OSC}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSC}\end{cases} \Rightarrow f_\text{OSC} = \begin{cases}f_\text{E}\,+\,f_\text{FI}\\ f_\text{E}\,-\,f_\text{FI}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = f_\text{E}\,+\,f_\text{FI1} = \qty{28}{\mega\hertz}\,+\,\qty{10,7}{\mega\hertz} = \qty{38,70}{\mega\hertz}$
</fragment>
<fragment>
$f_\text{CO} = f_\text{FI1}\,+\,f_\text{FI2} = \qty{10,7}{\mega\hertz}\,+\,\qty{460}{\kilo\hertz} = \qty{11,16}{\mega\hertz}$
</fragment>