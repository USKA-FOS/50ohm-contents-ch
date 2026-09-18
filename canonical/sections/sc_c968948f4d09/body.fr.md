Dans les classes N et E, nous avons appris à connaître le ROS et les formules correspondantes pour la puissance incidente et la puissance réfléchie. Dans de nombreux cas, on peut simplement indiquer le rapport d’ondes stationnaires (ROS) si l’impédance d’alimentation d’une antenne est connue. À condition qu’une antenne (ou une charge fictive) ne présente ni comportement inductif ni comportement capacitif, c’est-à-dire qu’elle représente une résistance active pure ($R_a$), le ROS se calcule à partir du rapport entre la résistance de charge et l’impédance caractéristique de la ligne, le numérateur et le dénominateur étant choisis de manière à obtenir un ROS supérieur ou égal à un.

L’illustration [ref:a_swr] montre la répartition de la tension d’une onde stationnaire sur une ligne. À certains endroits, la tension atteint un maximum $U_\mathrm{max}$, à d’autres un minimum $U_\mathrm{min}$. La distance entre deux maxima de tension voisins ou deux minima de tension voisins est respectivement de $\frac{\lambda}{2}$. Le ROS peut également être déterminé à partir du rapport entre la tension maximale et la tension minimale :

Mathématiquement, cela s’exprime par :

$s = \frac{U_\mathrm{max}}{U_\mathrm{min}} = \begin{cases} \dfrac{R_a}{Z}, & \text{pour } R_a > Z, \[6pt] 1, & \text{pour } R_a = Z, \[6pt] \dfrac{Z}{R_a}, & \text{pour } R_a < Z. \end{cases}$


<margin>
[picture:978:a_swr:Onde stationnaire]
</margin>

Une antenne présentant une impédance d’alimentation de $\qty{100}{\ohm}$ provoque, lorsqu’elle est alimentée par un câble de $\qty{50}{\ohm}$, un ROS de $\num{2}$, car l’impédance d’alimentation est deux fois plus élevée. Une antenne avec une impédance d’alimentation de $\qty{10}{\ohm}$ aurait un ROS de $\num{5}$, car l’impédance caractéristique de la ligne est cinq fois plus élevée.


Pour répondre aux questions suivantes, nous devons également nous rappeler que la résistance d’un dipôle replié est d’environ $\qtyrange{240}{300}{\ohm}$.


[question:AG405]
[question:AI403]


Un effet trompeur est l’impact de l’atténuation de la ligne sur le ROS. Plus une ligne présente de pertes, plus le ROS mesuré sur cette ligne peut être faible (donc « meilleur »). Cela s’explique par le fait qu’une ligne présentant des pertes réduit à la fois la puissance incidente et la puissance réfléchie. Même si, à l’extrémité d’une ligne, aucune antenne n’est connectée (circuit ouvert ou court-circuit) et que $\qty{100}{\percent}$ de l’énergie y est réfléchie, donc que le ROS y est de $\infty$, on peut mesurer à l’autre extrémité un ROS nettement meilleur. Par exemple, si la moitié de la puissance est perdue en direction aller et que la moitié de la puissance restante est perdue en direction retour, l’énergie est réduite à un quart ($
\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$). Ainsi, un ROS-mètre placé à l’extrémité émettrice du câble indique un ROS de $\num{3}$, ce qui correspond à $\qty{25}{\percent}$ de puissance réfléchie, bien que $\qty{100}{\percent}$ soient réfléchis à l’extrémité – seulement $\qty{25}{\percent}$ parviennent au ROS-mètre.


[question:AG402]
[question:AG403]


Avec une atténuation de ligne de $\qty{5}{\dB}$ et une réflexion totale à l’extrémité du câble, par exemple en raison d’une antenne débranchée, nous mesurons un ROS étonnamment bon, bien qu’aucune antenne ne soit connectée ! Cela peut être calculé comme suit :


$s = \frac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}}$


Cela permet de calculer la question suivante, à condition de noter que l’onde réfléchie mesurée ne représente qu’un dixième de l’énergie de l’onde incidente : $\qty{5}{\dB}$ d’atténuation en direction aller et $\qty{5}{\dB}$ en direction retour, soit une atténuation totale de $\qty{10}{\dB}$. $P_\mathrm{r}$ ne représente donc dans ce cas qu’un dixième de $P_\mathrm{v}$.


[question:AG404]