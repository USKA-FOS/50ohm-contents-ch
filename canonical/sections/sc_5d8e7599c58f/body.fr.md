Comme nous l'avons appris précédemment, les appareils radioamateurs et les lignes de transmission couramment utilisées dans le radioamateur utilisent généralement une impédance de ligne de $\qty{50}{\ohm}$. Nous avons également appris qu'il se produit des réflexions indésirables aux points de connexion des lignes de transmission lorsque l'impédance de la ligne ne correspond pas.

Les antennes ont également une propriété similaire à l'impédance de la ligne, qui dépend de la disposition exacte des éléments de l'antenne. Cette propriété est appelée résistance d'alimentation ou résistance de base. Comme pour la connexion de deux lignes de transmission avec des impédances de ligne différentes, il en va de même ici: si la résistance d'alimentation des antennes ne correspond pas à l'impédance de la ligne d'alimentation, des réflexions indésirables se produisent. Une partie de la puissance d'émission est réfléchie vers l'appareil radio et ne peut pas être rayonnée par l'antenne.

En revanche, si la résistance d'alimentation de l'antenne et l'impédance de la ligne d'alimentation coïncident et garantissent ainsi une transmission optimale de la puissance d'émission dans l'antenne, on parle d'*adaptation*.

<margin>
[photo:144:swr_meter:Un simple SWR-Meter pour déterminer le rapport d’ondes stationnaires]
</margin>

On peut mesurer à quel point l'adaptation de l'antenne est bonne. En termes simplifiés, on détermine ainsi la quantité de puissance d'émission réfléchie par l'antenne. La valeur mesurée indiquée par l'appareil de mesure s'appelle *rapport d’ondes stationnaires*. On utilise généralement l'abréviation SWR, dérivée du terme anglais "standing wave ratio". Pour déterminer le SWR, on utilise un *appareil de mesure des ondes stationnaires*, appelé brièvement *SWR-Meter*.

% TODO: Rendre spécifique à l'édition
<indepth>
Un SWR-Meter mesure simultanément la puissance d'émission avant qui est envoyée par l'émetteur à l'antenne, et la puissance réfléchie qui a été réfléchie. Cela peut être bien vu sur le SWR-Meter dans la figure [ref:swr_meter_kreuzzeiger], qui affiche séparément la puissance avant et réfléchie. Le SWR ne donne cependant pas directement le rapport de ces deux valeurs de mesure, mais est déterminé de manière quelque peu plus compliquée comme $\text{SWR} = \frac {\sqrt{P_\text{V}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{V}}-\sqrt{P_\text{R}}}$, où $P_\text{V}$ est la puissance avant et $P_\text{R}$ la puissance réfléchie. Pour l'examen de la classe N, il n'est pas nécessaire de connaître cette formule.
</indepth>

<margin>
[photo:143:swr_meter_kreuzzeiger:SWR-Meter avec aiguille croisée, l'aiguille de gauche pour la puissance avant et l'aiguille de droite pour la puissance réfléchie; pour lire le SWR, on suit la ligne verte au point d'intersection des deux aiguilles vers le bas]
</margin>

[question:NI201]

---

<margin>
[photo:67:n_swr_display:Affichage d'un émetteur-récepteur]
</margin>

Les émetteurs-récepteurs modernes ont déjà un SWR-Meter intégré. L'affichage se trouve généralement dans l'affichage, voir [ref:n_swr_display].

<attention>
Les SWR-Meter et les S-Meter ont des noms similaires, mais sont différents: le SWR-Meter mesure le rapport d’ondes stationnaires lors de l'émission et le S-Meter mesure l'intensité du signal lors de la réception.
</attention>

% TODO Big Picture: Dans l'image Trx_Display "SWR" marquer
[question:NF101] 

---

Si aucun SWR-Meter n'est intégré dans l'émetteur-récepteur, on peut également utiliser un SWR-Meter externe. Il est branché entre l'appareil radio et l'antenne comme dans la figure [ref:n_trx_kabel_swr_antenne]. On dit aussi: "Le SWR-Meter est inséré entre l'émetteur-récepteur et l'antenne".

[question:NI202]

Si une antenne est parfaitement adaptée à la ligne d'alimentation (par exemple le câble coaxial), le SWR-Meter affiche une valeur de $\num{1}$. C'est la meilleure valeur atteignable. Alors, toute la puissance est absorbée par l'antenne. Aucune puissance n'est réfléchie vers l'émetteur.

<margin>
[picture:670:n_trx_kabel_swr_antenne:Schéma SWR-Meter entre émetteur-récepteur et antenne]
</margin>

[question:NG301]
[question:NI203]

---

Si aucune antenne n'est branchée sur l'émetteur-récepteur ou si la ligne de transmission est soit interrompue soit en court-circuit, la valeur SWR est presque infinie ($\infty$). Un câble ouvert ou en court-circuit réfléchit en effet complètement la puissance d'émission. Cela peut, dans le pire des cas, même détruire l'émetteur dans l'appareil radio.

<indepth>
Outre les deux valeurs *SWR* $\num{1}$ et infini ($\infty$), les valeurs $\num{2}$ et $\num{3}$ à droite sont également marquantes. Pour une valeur SWR de $\num{2}$, $\qty{11}{\percent}$ de la puissance d'émission est réfléchie vers l'émetteur, et pour une valeur SWR de $\num{3}$, $\qty{25}{\percent}$ de la puissance d'émission est réfléchie vers l'émetteur. Dans les émetteurs-récepteurs modernes, une destruction de l'émetteur est évitée en réduisant automatiquement la puissance d'émission dans l'appareil radio.
</indepth>

Un SWR très mauvais, par exemple proche de l'infini, peut également être obtenu si l'adaptation des antennes est très mauvaise ou si la ligne de transmission est endommagée.

[question:NG302]
[question:NG303]

Si une antenne avec une mauvaise adaptation est connectée à un appareil radio avec un SWR-Meter via un long câble coaxial, la valeur SWR affichée peut être nettement meilleure que ce à quoi on pourrait s'attendre en raison de la mauvaise adaptation. La cause en est une forte atténuation du câble, qui réduit non seulement le signal allant vers l'antenne, mais aussi le signal réfléchi.

[question:NG208]
