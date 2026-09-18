## Distance de sécurité : calcul du champ lointain (sans atténuation des câbles)

* Pour les installations de radioamateur fixes, la distance de sécurité est déterminée à l'aide de la formule du champ lointain

<fragment>
$d=\dfrac{\sqrt{30\,\Omega\cdot P_A\cdot G_i}}{E}$
</fragment>

--- style="font-size: 0.7em;"
#### Informations complémentaires sur les procédés de modulation dans le calcul de la distance de sécurité

* Lors de l'affichage d'une installation de radioamateur fixe (selon § 9, BEMFV), le facteur de conversion $\textrm{Facteur}_\textrm{FmodPers}$ doit être indiqué
* Ce facteur convertit la puissance de crête indiquée (PEP) en puissance moyenne, qui est utilisée dans la formule du champ lointain pour calculer la distance de sécurité
* La plupart des procédés de modulation ont ici un facteur de $\num{1}$
* ATV : facteur $\num{0,38}$

<note>
DIN EN 50413, pertinent pour le radioamateurisme uniquement ATV avec $\num{0,38}$ et SATV avec $\num{0,54}$
</note>

---

[question:AK106]

--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $E = \qty{28}{\volt\per\meter}$
* donné : $P_S = P_A = \qty{100}{\watt}$
</left>
<right>
* donné : $G_i = 1,64$
* recherché : $d$
</right>

<fragment>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{100}{\watt} \cdot 1,64}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{2,5}{\meter}\end{split}$
</fragment>

---
## Distance de sécurité : prise en compte de l'atténuation des câbles
* La puissance isotrope rayonnée équivalente (EIRP) est d'abord calculée

<fragment>
$P_\text{EIRP} = P_S\cdot10^{\frac{g_d - a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}$
</fragment>

---

[question:AK108]

--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $E = \qty{28}{\volt\per\meter}$
* donné : $P_S = \qty{300}{\watt}$
* donné : $a = \qty{0,5}{\dB}$
</left>
<right>
* donné : $g_d = \qty{0}{\dBd}$
* recherché : $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{300}{\watt} \cdot 10^{\frac{\qty{0}{\dBd} - \qty{0,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{438,7}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{438,7}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{4,10}{\meter}\end{split}$
</right>
</fragment>

---

[question:AK109]

--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $E = \qty{28}{\volt\per\meter}$
* donné : $P_S = \qty{700}{\watt}$
* donné : $a = \qty{0,5}{\dB}$
</left>
<right>
* donné : $g_d = \qty{0}{\dBd}$
* recherché : $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{700}{\watt} \cdot 10^{\frac{\qty{0}{\dBd} - \qty{0,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1023,5}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1023,5}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{6,26}{\meter}\end{split}$
</right>
</fragment>

---

[question:AK110]

--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $E = \qty{28}{\volt\per\meter}$
* donné : $P_S = \qty{75}{\watt}$
* donné : $a = \qty{1,5}{\dB}$
</left>
<right>
* donné : $g_d = \qty{11,5}{\dBd}$
* recherché : $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{75}{\watt} \cdot 10^{\frac{\qty{11,5}{\dBd} - \qty{1,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1230,4}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1230,4}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{6,86}{\meter}\end{split}$
</right>
</fragment>

---

[question:AK111]

--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $E = \qty{28}{\volt\per\meter}$
* donné : $P_S = \qty{100}{\watt}$
* donné : $a = \qty{1,5}{\dB}$
</left>
<right>
* donné : $g_d = \qty{10,5}{\dBd}$
* recherché : $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{100}{\watt} \cdot 10^{\frac{\qty{10,5}{\dBd} - \qty{1,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{1303,2}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1303,2}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{7,1}{\meter}\end{split}$
</right>
</fragment>

---

[question:AK112]

--- style="font-size: smaller;"
#### Méthode de résolution
<left>
* donné : $E = \qty{61}{\volt\per\meter}$
* donné : $P_S = \qty{40}{\watt}$
* donné : $a = \qty{2}{\dB}$
</left>
<right>
* donné : $g_d = \qty{18}{\dBd}$
* recherché : $d$
</right>

<fragment>
<left>
$\begin{split}P_{EIRP} &= P_S \cdot 10^{\frac{g_d -a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{40}{\watt} \cdot 10^{\frac{\qty{18}{\dBd} - \qty{2}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{2612,5}{\watt}\end{split}$
</left>
</fragment>
<fragment>
<right>
$\begin{split}E &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{d}\\ \Rightarrow d &= \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}\\ &= \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{2612,5}{\watt}}}{\qty{61}{\volt\per\meter}}\\ &\approx \qty{4,6}{\meter}\end{split}$
</right>
</fragment>