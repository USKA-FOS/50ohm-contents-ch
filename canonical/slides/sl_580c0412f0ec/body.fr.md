<left>
[picture:978:a_swr:Onde stationnaire]
</left>
<right>
* Le rapport d’ondes stationnaires (ROS) peut souvent être indiqué directement à partir de l'impédance d'une antenne
* En cas de résistance pure (sans composantes inductives ou capacitives), le ROS est calculé à partir du rapport de la résistance de charge à l'impédance de la ligne (de sorte que ROS ≥ $\num{1}$)
</right>

---

* Exemple : Une antenne de $\qty{100}{\ohm}$ sur un câble de $\qty{50}{\ohm}$ donne un ROS de $\num{2}$, tandis qu'une antenne de $\qty{10}{\ohm}$ donne un ROS de $\num{5}$
* Rappel : La résistance d'un dipôle replié est d'environ $\qty{300}{\ohm}$

---
[question:AG405]
---
#### Solution
* donné : $Z = \qty{75}{\ohm}$
* donné : $R_2 \approx \qty{300}{\ohm}$ résistance dipôle replié
* recherché : $s$

<fragment>
$s = \frac{R_2}{Z} = \frac{\qty{300}{\ohm}}{\qty{75}{\ohm}} = 4$
</fragment>
---

### Influence de l'atténuation de la ligne sur le rapport d’ondes stationnaires

* L'atténuation de la ligne réduit à la fois la puissance incidente et la puissance réfléchie
* Même si $\qty{100}{\percent}$ de l'énergie est réfléchie à l'extrémité du câble, un ROS plus faible (meilleur) peut être mesuré au niveau de l'émetteur
* Exemple : Si la moitié de la puissance est perdue dans les deux sens, il ne reste qu'un quart de la puissance d'origine – ce qui correspond à un ROS mesuré de $\num{3}$ ($\qty{25}{\percent}$ de puissance réfléchie)

---
[question:AG402]
---
[question:AG403]
---

### Effet de l'atténuation de la ligne sur le ROS mesuré

* Avec une atténuation de ligne de $\qty{5}{\dB}$ dans les deux sens (au total $\qty{10}{\dB}$), la puissance réfléchie n'est qu'un dixième de la puissance incidente
* Le ROS mesuré peut être calculé avec la formule :
  
<fragment>
$s = \frac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}}$
</fragment>

---
[question:AG404]
---

#### Solution
* donné : $P_V = \qty{10}{\watt}$
* donné : $a = \qty{5}{\dB}$
* recherché : $s$

<fragment>
Atténuation sur l'ensemble du câble pour l'aller et le retour : $\qty{10}{\dB}$
$P_R = \qty{-10}{\dB} \cdot P_V = \dfrac{\qty{10}{\watt}}{10} = \qty{1}{\watt}$
</fragment>
<fragment>
$s = \dfrac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}} = \dfrac{\sqrt{\qty{10}{\watt}}+\sqrt{\qty{1}{\watt}}}{\sqrt{\qty{10}{\watt}}-\sqrt{\qty{1}{\watt}}} = 1,92$
</fragment>
