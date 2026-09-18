Comme nous l’avons appris précédemment, les appareils radioamateurs et les lignes de transmission couramment utilisées en radioamateurisme ont généralement une impédance caractéristique de $\qty{50}{\ohm}$. Nous avons également appris que des réflexions indésirables se produisent aux points de connexion des lignes de transmission si l’impédance caractéristique n’est pas adaptée.

Les antennes possèdent également une propriété similaire à l’impédance caractéristique, qui dépend de la disposition exacte des éléments de l’antenne. Cette propriété est appelée impédance d’alimentation ou impédance au point d’alimentation. Comme pour la connexion de deux lignes de transmission d’impédances caractéristiques différentes, si l’impédance d’alimentation de l’antenne ne correspond pas à l’impédance caractéristique de la ligne d’alimentation, des réflexions indésirables se produisent. Une partie de la puissance d’émission est réfléchie vers l’émetteur et ne peut pas être rayonnée par l’antenne.

En revanche, si l’impédance d’alimentation de l’antenne et l’impédance caractéristique de la ligne d’alimentation sont adaptées, garantissant ainsi une transmission optimale de la puissance d’émission vers l’antenne, on parle alors d’*adaptation*.

<margin>
[photo:144:swr_meter:Un ROS-mètre simple pour déterminer le rapport d’ondes stationnaires]
</margin>

On peut mesurer la qualité de l’adaptation de l’antenne. En termes simplifiés, on détermine la quantité de puissance d’émission réfléchie par l’antenne. La valeur mesurée affichée par l’appareil s’appelle le *rapport d’ondes stationnaires*. On utilise généralement l’abréviation SWR, dérivée de l’anglais *standing wave ratio*. Pour déterminer le SWR, on utilise un *ROS-mètre*, appelé aussi *SWR-Meter*.

% TODO: À adapter selon l’édition
<indepth>
Un ROS-mètre mesure simultanément la puissance d’émission incidente envoyée par l’émetteur vers l’antenne et la puissance réfléchie renvoyée. Cela peut être clairement observé sur le ROS-mètre de la figure [ref:swr_meter_kreuzzeiger], qui affiche séparément la puissance incidente et la puissance réfléchie. Le SWR n’indique cependant pas directement le rapport de ces deux valeurs mesurées, mais est calculé de manière un peu plus complexe selon la formule $\text{SWR} = \frac {\sqrt{P_\text{inc}}+\sqrt{P_\text{réfl}}} { \sqrt{P_\text{inc}}-\sqrt{P_\text{réfl}}}$, où $P_\text{inc}$ est la puissance incidente et $P_\text{réfl}$ la puissance réfléchie.
</indepth>

<margin>
[photo:143:swr_meter_kreuzzeiger:ROS-mètre à aiguilles croisées, l’aiguille de gauche pour la puissance incidente et celle de droite pour la puissance réfléchie ; pour lire le SWR, on suit la ligne verte au point d’intersection des deux aiguilles vers le bas]
</margin>

[question:NI201]

---

<margin>
[photo:67:n_swr_display:Écran d’un émetteur-récepteur]
</margin>

Les émetteurs-récepteurs modernes intègrent déjà un ROS-mètre. L’affichage se trouve généralement dans l’écran, voir [ref:n_swr_display].

<attention>
ROS-mètre et S-mètre se ressemblent, mais ils sont différents : le ROS-mètre mesure le rapport d’ondes stationnaires lors de l’émission, tandis que le S-mètre mesure l’intensité du signal lors de la réception.
</attention>

% TODO Big Picture : Dans l’image Trx_Display, indiquer "SWR"
[question:NF101]

---

Si l’émetteur-récepteur ne dispose pas d’un ROS-mètre intégré, on peut utiliser un ROS-mètre externe. Celui-ci est alors connecté entre l’appareil radio et l’antenne, comme illustré dans la figure [ref:n_trx_kabel_swr_antenne]. On dit aussi : « Le ROS-mètre est inséré entre l’émetteur-récepteur et l’antenne ».

[question:NI202]

Si une antenne est parfaitement adaptée à la ligne d’alimentation (par exemple, le câble coaxial), le ROS-mètre affiche une valeur de $\num{1}$. Il s’agit de la meilleure valeur possible. Dans ce cas, toute la puissance est absorbée par l’antenne. Aucune puissance n’est réfléchie vers l’émetteur.

<margin>
[picture:670:n_trx_kabel_swr_antenne:Schéma de principe d’un ROS-mètre inséré entre l’émetteur-récepteur et l’antenne]
</margin>

[question:NG301]
[question:NI203]

---

Si aucune antenne n’est connectée à l’émetteur-récepteur, ou si la ligne de transmission est soit coupée, soit en court-circuit, la valeur du SWR est quasi infinie ($\infty$). En effet, un câble ouvert ou en court-circuit réfléchit intégralement la puissance d’émission. Dans le pire des cas, cela peut même endommager l’émetteur de l’appareil radio.

<indepth>
En plus des deux valeurs de SWR $\num{1}$ et infinie ($\infty$), les valeurs $\num{2}$ et $\num{3}$ sont également marquantes. Pour un SWR de $\num{2}$, $\qty{11}{\percent}$ de la puissance d’émission sont réfléchis vers l’émetteur, et pour un SWR de $\num{3}$, $\qty{25}{\percent}$ le sont. Dans les émetteurs-récepteurs modernes, une puissance d’émission trop élevée est évitée en réduisant automatiquement la puissance de l’émetteur.
</indepth>

Un SWR très élevé, par exemple proche de l’infini, peut également indiquer une adaptation très médiocre de l’antenne ou un endommagement de la ligne de transmission.

[question:NG302]
[question:NG303]

Si une antenne mal adaptée est connectée à un appareil radio équipé d’un ROS-mètre via un long câble coaxial, la valeur de SWR affichée peut être nettement meilleure que ce à quoi on pourrait s’attendre en raison de la mauvaise adaptation. La cause en est l’atténuation élevée du câble, qui réduit non seulement le signal allant vers l’antenne, mais aussi le signal réfléchi.

[question:NG208]
