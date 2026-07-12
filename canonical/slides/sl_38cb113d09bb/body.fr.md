## Décibels

* Indication logarithmique des rapports, en particulier des puissances
* Rend le travail avec les petites et grandes puissances plus facile
* Les amplifications et les atténuations peuvent être calculées plus facilement

---

## Pourquoi les décibels ?

[picture:877:e_signalkette:Chaîne de signaux avec trois amplificateurs]

[picture:1053:e_signalkette_2:Chaîne de signaux avec deux amplificateurs et un atténuateur]

--- style="font-size: 0.7em;"
## Niveau de puissance

Facteur 10

*Puissance par rapport à $\qty{1}{\milli\watt}$*
$p = 10\cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$
<fragment>
$\rightarrow\qty{0}{\dBm}$ est présent lorsque $P = \qty{1}{\milli\watt}$
</fragment>

<fragment>
*Puissance par rapport à $\qty{1}{\watt}$*
$p = 10\cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}$
</fragment>
<fragment>
$\rightarrow\qty{0}{\dBW}$ est présent lorsque $P = \qty{1}{\watt}$
</fragment>

---
[question:AA110]
<note>
Insérer uniquement
</note>
---
[question:AA105]

--- style="font-size: 0.7em;"

## Niveau de tension

Facteur $20$

$u = 20\cdot \log_{10}\left(\frac{U}{\qty{0,775}{\volt}}\right)\unit{\dBu}$

<fragment>
*Tension par rapport à $\qty{0,775}{\volt}$*
$\rightarrow\qty{0}{\dBu}$ est présent lorsque $U = \qty{0,775}{\volt}$
</fragment>
<fragment>
*Tension par rapport à $\qty{1}{\volt}$*
$\rightarrow\qty{0}{\dBV}$ est présent lorsque $U = \qty{1}{\volt}$
</fragment>
<fragment>
*Tension par rapport à $\qty{1}{\micro\volt}$*
$\rightarrow\qty{0}{\dBuV}$ est présent lorsque $U = \qty{1}{\micro\volt}$
</fragment>

<note>
Les détails du calcul du facteur 20 sont dans le cours en ligne. Version abrégée : Dans le rapport de tension, on calcule avec des carrés, ce qui peut être sorti du logarithme comme facteur.
</note>
---
[question:AA111]
---
[question:AA108]
---
### Solution
* donné : $p = \qty{20}{\dBW}$
* recherché : $P$

<fragment>
$\begin{split} p &= 10\cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}\\ \Rightarrow P &= 10^{\frac{p}{10}} \cdot \qty{1}{\watt} = 10^{\frac{\qty{20}{\dBW}}{10}} \cdot \qty{1}{\watt} = \qty{10^2}{\watt} \end{split}$
</fragment>
---
[question:AA107]
---
[question:AA109]
---
### Solution

$\qty{1}{\watt} = \qty{1000}{\milli\watt}$
$\qty{10}{\dB} = \text{Facteur 10}$
$\qty{1000}{\milli\watt} \cdot 10 = \qty{10000}{\milli\watt} = \qty{40}{\dBm}$
---
[question:AA106]
---
## Solution
* $\qty{16}{\dB} = \qty{10}{\dB} + \qty{6}{\dB} = 10 \cdot 4 = 40$
* $\qty{1}{\watt} \cdot 40 = \qty{40}{\watt}$

<note>
À partir du tableau dans le recueil de formules
</note>

---
[question:AA112]
---
### Solution
* donné : $u = \qty{120}{\dBuV\per\meter}$
* recherché : $U$

<fragment>
$\begin{split} u &= 20\cdot \log_{10}\left(\frac{U}{\qty{1}{\micro\volt}}\right)\unit{\dBuV}\\ \Rightarrow U &= 10^{\frac{u}{20}} \cdot \qty{1}{\micro\volt} = 10^{\frac{\qty{120}{\dBuV\per\meter}}{20}} \cdot \qty{1}{\micro\volt} = \qty{1}{\volt\per\meter} \end{split}$
</fragment>
<fragment>
Dans la littérature, on trouve souvent : $\qty{120}{\dBuV} = \qty{1}{\volt}$
</fragment>
