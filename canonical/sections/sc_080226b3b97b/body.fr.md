Dans la classe E, nous avons déjà appris à connaître le ROS-mètre et son utilisation. Dans la classe A, nous voulons comprendre le fonctionnement interne d’un ROS-mètre. Un ROS-mètre se compose généralement de deux coupleurs directionnels. Commençons par nous familiariser avec leur principe de fonctionnement.

Un *coupleur directionnel* sert à prélever une petite partie d’un signal HF sur une ligne d’alimentation. Sa particularité réside dans le fait qu’il peut distinguer la direction dans laquelle l’onde se propage sur la ligne. Pour cela, le signal est capté de deux manières différentes. Une tension $U_C$ est obtenue par couplage capacitif, qui dépend de la tension sur la ligne d’alimentation. Simultanément, le couplage inductif génère une tension $U_I$, qui dépend du courant sur la ligne d’alimentation. Le coupleur directionnel est dimensionné de telle sorte que les composantes du signal obtenues par couplage capacitif et inductif soient de même amplitude à ses sorties. Cependant, ces composantes sont combinées avec des signes différents aux deux sorties.

Pour une onde se propageant dans une direction donnée sur la ligne, par exemple de gauche à droite comme illustré dans la figure [ref:a_richtkoppler_rechts_links], les tensions obtenues par couplage capacitif et inductif s’additionnent à une sortie. À l’autre sortie, elles sont de signes opposés et s’annulent mutuellement dans l’idéal. Le signal apparaît donc principalement sur une seule des deux sorties.

<margin>
[picture:1109:a_richtkoppler_rechts_links:Coupleur directionnel, l’onde se propage de gauche à droite]
</margin>

---

Si la direction de propagation de l’onde s’inverse, par exemple de droite à gauche comme illustré dans la figure [ref:a_richtkoppler_rechts_links], le sens du courant par rapport à la tension s’inverse également. Ainsi, la tension $U_I$ couplée par induction change de signe, tandis que la tension $U_C$ couplée par capacité dépend de la tension sur la ligne.

<margin>
[picture:1110:a_richtkoppler_rechts_links:Coupleur directionnel, l’onde se propage de droite à gauche]
</margin>

Les deux sorties du coupleur directionnel s’inversent donc également : la sortie où les deux composantes s’additionnaient précédemment est maintenant largement annulée, tandis qu’elles s’additionnent à l’autre sortie.

Ainsi, un coupleur directionnel peut distinguer une *onde en avance de phase* en direction de l’antenne d’une *onde réfléchie* en direction de l’émetteur.

---

Cette propriété des coupleurs directionnels est exploitée dans un *ROS-mètre* : pour cela, on mesure les tensions de sortie de deux coupleurs directionnels insérés dans la ligne et fonctionnant en directions opposées. Les tensions HF aux sorties des coupleurs directionnels sont redressées par des diodes et lissées. Cela génère des tensions continues qui peuvent être affichées par un instrument de mesure.

[question:AI401]

La figure [ref:a_rswr_meter] montre la structure de principe d’un ROS-mètre avec deux coupleurs directionnels. Nous supposons ici que l’émetteur se trouve à gauche et l’antenne à droite.

[question:AI402]

Le conducteur supérieur fait partie de la ligne d’alimentation entre l’émetteur et l’antenne. Deux grandeurs y sont mesurées : par couplage capacitif, une petite partie de la tension HF est prélevée. Par couplage inductif, une partie dépendant du courant sur la ligne d’alimentation est simultanément obtenue.

Le côté non utilisé de la ligne de couplage est terminé par une *résistance de terminaison*. Cette résistance correspond approximativement à l’impédance caractéristique $Z_0$ de la ligne de couplage. Ainsi, la puissance HF arrivant est absorbée et n’est pas réinjectée dans la ligne de couplage. De telles réflexions dégraderaient la séparation entre l’onde directe et l’onde réfléchie.

Ces deux composantes du signal sont combinées dans le coupleur directionnel. Pour une onde allant de l’émetteur vers l’antenne, elles s’additionnent dans l’un des deux coupleurs, tandis qu’elles s’annulent presque mutuellement dans l’autre. Pour une onde dans la direction opposée, c’est exactement l’inverse.

Les deux parties du circuit, construites de manière presque symétrique, peuvent ainsi détecter des directions de propagation différentes :

* L’un des coupleurs directionnels fournit un signal proportionnel à l’*onde en avance de phase* de l’émetteur vers l’antenne.
* L’autre coupleur directionnel fournit un signal proportionnel à l’*onde réfléchie* de l’antenne vers l’émetteur.

Les signaux prélevés sont initialement des tensions alternatives HF. Les diodes redressent ces tensions, et les condensateurs les lissent. Cela génère des tensions continues qui peuvent être affichées par les deux aiguilles d’un instrument à aiguilles croisées, ou mesurées par un microcontrôleur avec un convertisseur numérique. Les résistances réglables servent à l’ajustement ou à l’étalonnage de l’affichage. Elles ne doivent pas être confondues avec les résistances de terminaison des lignes de couplage, qui assurent une terminaison sans réflexion avec $Z_0$.

<margin>
[picture:499:a_rswr_meter:ROS-mètre avec deux coupleurs directionnels]
</margin>