## Décibel

* Représentation logarithmique de rapports, notamment pour les puissances
* Facilite le travail avec des puissances petites et grandes
* Les amplifications et atténuations se calculent plus simplement

---

## Pourquoi le décibel ?

[picture:877:e_signalkette:Chaîne de signal avec trois amplificateurs]

[picture:1053:e_signalkette_2:Chaîne de signal avec deux amplificateurs et un atténuateur]

--- style="font-size: 0.7em;"
## Niveau de puissance

Facteur 10

*Niveau de puissance par rapport à $\qty{1}{\milli\watt}$*
$p = 10\cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$
<fragment>
$\rightarrow\qty{0}{\dBm}$ correspond à $P = \qty{1}{\milli\watt}$
</fragment>

<fragment>
*Niveau de puissance par rapport à $\qty{1}{\watt}$*
$p = 10\cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}$
</fragment>
<fragment>
$\rightarrow\qty{0}{\dBW}$ correspond à $P = \qty{1}{\watt}$
</fragment>

---
[question:AD428]
---
#### Méthode de résolution
* donné : $P_1 = \qty{38}{\watt}$
* donné : $P_2 = \qty{2,5}{\watt}$
* recherché : $g$

<fragment>
$\begin{split} g &= \qty{10\cdot \log_{10}{\left(\frac{P_2}{P_1}\right)}}{\dB}\\ &= \qty{10\cdot \log_{10}{\left(\frac{\qty{38}{\watt}}{\qty{2,5}{\watt}}\right)}}{\dB} = \qty{11,8}{\dB} \end{split}$
</fragment>

---
[question:AA110]
<note>
Seulement à insérer
</note>
---
[question:AA105]

--- style="font-size: 0.7em;"

## Niveau de tension

Facteur $20$

$u = 20\cdot \log_{10}\left(\frac{U}{\qty{0,775}{\volt}}\right)\unit{\dBu}$

<fragment>
*Niveau de tension par rapport à $\qty{0,775}{\volt}$*
$\rightarrow\qty{0}{\dBu}$ correspond à $U = \qty{0,775}{\volt}$
</fragment>
<fragment>
*Niveau de tension par rapport à $\qty{1}{\volt}$*
$\rightarrow\qty{0}{\dBV}$ correspond à $U = \qty{1}{\volt}$
</fragment>
<fragment>
*Niveau de tension par rapport à $\qty{1}{\micro\volt}$*
$\rightarrow\qty{0}{\dBuV}$ correspond à $U = \qty{1}{\micro\volt}$
</fragment>

<note>
Les détails du calcul du facteur 20 sont abordés dans le cours en ligne. Résumé : dans le rapport de tension, on travaille avec des carrés, ce qui peut être extrait comme facteur devant le logarithme.
</note>

---

[question:AD427]

---

#### Méthode de résolution
* donné : $U_1 = \qty{1}{\milli\volt}$
* donné : $U_2 = \qty{4}{\milli\volt}$
* recherché : $g$

<fragment>
$\begin{split} g &= \qty{20\cdot \log_{10}{\left(\frac{U_2}{U_1}\right)}}{\dB}\\ &= \qty{20\cdot \log_{10}{\left(\frac{\qty{4}{\milli\volt}}{\qty{1}{\milli\volt}}\right)}}{\dB} = \qty{12}{\dB} \end{split}$
</fragment>

---

[question:AA111]

---

[question:AA108]

---

### Méthode de résolution
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
### Méthode de résolution

$\qty{1}{\watt} = \qty{1000}{\milli\watt}$
$\qty{10}{\dB} = \text{Facteur 10}$
$\qty{1000}{\milli\watt} \cdot 10 = \qty{10000}{\milli\watt} = \qty{40}{\dBm}$
---
[question:AA106]
---
## Méthode de résolution
* $\qty{16}{\dB} = \qty{10}{\dB} + \qty{6}{\dB} = 10 \cdot 4 = 40$
* $\qty{1}{\watt} \cdot 40 = \qty{40}{\watt}$

<note>
D'après le tableau du recueil de formules
</note>

---
[question:AD426]
---
#### Méthode de résolution
* donné : $g = \qty{16}{\dB}$
* donné : $P_1 = \qty{1}{\watt}$
* recherché : $P_2$

<fragment>
$g = \qty{16}{\dB} = \qty{10}{\dB} + \qty{6}{\dB} = 10 \cdot 4 = 40$
</fragment>
<fragment>
$P_2 = P_1 \cdot g = \qty{1}{\watt} \cdot 40 = \qty{40}{\watt}$
</fragment>

---
[question:AA112]
---
### Méthode de résolution
* donné : $u = \qty{120}{\dBuV\per\meter}$
* recherché : $U$

<fragment>
$\begin{split} u &= 20\cdot \log_{10}\left(\frac{U}{\qty{1}{\micro\volt}}\right)\unit{\dBuV}\\ \Rightarrow U &= 10^{\frac{u}{20}} \cdot \qty{1}{\micro\volt} = 10^{\frac{\qty{120}{\dBuV\per\meter}}{20}} \cdot \qty{1}{\micro\volt} = \qty{1}{\volt\per\meter} \end{split}$
</fragment>
<fragment>
Dans la littérature, on trouve souvent : $\qty{120}{\dBuV} = \qty{1}{\volt}$
</fragment>
