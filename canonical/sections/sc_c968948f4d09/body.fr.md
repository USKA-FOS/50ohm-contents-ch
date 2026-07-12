<margin>
[picture:978:a_swr:Onde stationnaire]
</margin>
Dans de nombreux cas, on peut indiquer simplement le rapport d’ondes stationnaires si l’impédance d’une antenne est connue. Dans la mesure où une antenne (ou charge fictive) ne se comporte ni de manière inductive ni capacitive, c’est-à-dire qu’elle représente une résistance purement active, le rapport d’ondes stationnaires résulte du rapport entre la résistance de charge et l’impédance de la ligne, le numérateur et le dénominateur devant être choisis de manière à obtenir un ROS supérieur ou égal à un.

Une antenne avec une impédance d’alimentation de $\qty{100}{\ohm}$ provoque, lors de l’alimentation avec un câble de $\qty{50}{\ohm}$, un rapport d’ondes stationnaires de $\num{2}$, car l’impédance d’alimentation est deux fois plus grande. Une antenne avec une impédance d’alimentation de $\qty{10}{\ohm}$ aurait un rapport d’ondes stationnaires de $\num{5}$, car l’impédance de la ligne est cinq fois plus grande.

Pour répondre à la question suivante, nous devons également nous rappeler que la résistance d’un dipôle plié est d’environ $\qty{300}{\ohm}$.

[question:AG405]

Un effet trompeur est l’impact de l’atténuation de la ligne sur le rapport d’ondes stationnaires. Plus une ligne présente des pertes, plus le rapport d’ondes stationnaires peut être faible (c’est-à-dire "meilleur") sur cette ligne. Cela est dû au fait qu’une ligne à pertes réduit à la fois la puissance incidente et la puissance réfléchie. Même si aucune antenne n’est connectée à l’extrémité d’une ligne (circuit ouvert ou court-circuit), et que $\qty{100}{\percent}$ de l’énergie est réfléchie, donc que le rapport d’ondes stationnaires *là-bas* est $\infty$, on peut mesurer un rapport d’ondes stationnaires nettement meilleur à l’autre extrémité. Par exemple, si la moitié de la puissance est perdue dans le sens aller et à nouveau la moitié dans le sens retour, l’énergie est réduite à un quart ($\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$). Par conséquent, un mesureur de rapport d’ondes stationnaires à l’extrémité de l’émetteur du câble indique un rapport d’ondes stationnaires de $\num{3}$, ce qui correspond à $\qty{25}{\percent}$ de puissance réfléchie, bien que $\qty{100}{\percent}$ soit réfléchie à l’extrémité – mais seulement $\qty{25}{\percent}$ parvient au mesureur de rapport d’ondes stationnaires.
[question:AG402]
[question:AG403]

En cas d’atténuation de ligne de $\qty{5}{\dB}$ et de réflexion totale à l’extrémité du câble, par exemple en raison d’une antenne déconnectée, nous mesurons même un ROS étonnamment bon, bien qu’aucune antenne ne soit connectée ! Nous pouvons calculer cela comme suit :

$s = \frac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}}$

Cela nous permet de calculer la question suivante, à condition de noter que l’onde réfléchie mesurée ne représente qu’un dixième de l’énergie de l’onde incidente : $\qty{5}{\dB}$ d’atténuation dans le sens aller et $\qty{5}{\dB}$ d’atténuation dans le sens retour, soit $\qty{10}{\dB}$ d’atténuation au total. $P_\mathrm{r}$ n’est donc dans ce cas qu’un dixième de $P_\mathrm{v}$.

[question:AG404]
