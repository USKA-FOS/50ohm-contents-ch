<left>
[picture:978:a_swr:Onde stationnaire]
</left>
<right>
* Le **rapport d’ondes stationnaires** (ROS) peut souvent être indiqué directement à partir de l’impédance d’alimentation d’une antenne
* Dans le cas d’une **résistance active** pure (sans composantes inductives ou capacitives), le ROS se calcule à partir du **rapport** entre la **résistance de charge** et l’impédance caractéristique du câble (de sorte que ROS ≥ 1)
</right>

---

* Exemple : une antenne de **résistance** 100 Ω sur un câble de 50 Ω donne un ROS de 2, tandis qu’une antenne de 10 Ω donne un ROS de 5
* Pour rappel : la **résistance** d’un dipôle replié est d’environ 300 Ω

---
[question:AG405]
---
#### Méthode de résolution
* données : $Z = \qty{75}{\ohm}$
* données : $R_2 \approx \qty{300}{\ohm}$ (résistance du dipôle replié)
* recherché : $s$

<fragment>
$s = \frac{R_2}{Z} = \frac{\qty{300}{\ohm}}{\qty{75}{\ohm}} = 4$
</fragment>
---

### Influence de l’**atténuation** de la ligne sur le ROS

* L’**atténuation** de la ligne réduit à la fois la **puissance incidente** et la **puissance réfléchie**
* Même si 100 % de l’énergie est réfléchie à l’extrémité du câble, un ROS plus faible (meilleur) peut être mesuré à l’émetteur
* Exemple : si la moitié de la **puissance** est perdue dans les deux sens (aller et retour), il ne reste qu’un quart de la **puissance** initiale – cela correspond à un ROS mesuré de 3 (25 % de **puissance réfléchie**)

---
[question:AG402]
[question:AG403]
---

### Effet de l’**atténuation** de la ligne sur le ROS mesuré

* Avec une **atténuation** de 5 dB dans les deux sens (soit 10 dB au total), la **puissance réfléchie** ne représente qu’un dixième de la **puissance incidente**
* Le ROS mesuré peut être calculé avec la formule :

<fragment>
$s = \frac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}}$
</fragment>

---
[question:AG404]
---
#### Méthode de résolution
* données : $P_V = \qty{10}{\watt}$
* données : $a = \qty{5}{\dB}$
* recherché : $s$

<fragment>
**Atténuation** sur l’ensemble du câble (aller-retour) : $\qty{10}{\dB}$
$P_R = \qty{-10}{\dB} \cdot P_V = \dfrac{\qty{10}{\watt}}{10} = \qty{1}{\watt}$
</fragment>
<fragment>
$s = \dfrac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}}} = \dfrac{\sqrt{\qty{10}{\watt}}+\sqrt{\qty{1}{\watt}}}{\sqrt{\qty{10}{\watt}}-\sqrt{\qty{1}{\watt}}}} = 1,92$
</fragment>
