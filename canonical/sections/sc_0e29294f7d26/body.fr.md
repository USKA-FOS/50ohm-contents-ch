% Le titre de l’édition 14 a été modifié (le titre original était « Antennenformen II », mais il n’existe pas de chapitre « Antennenformen I »)

Nous avons déjà appris à connaître plusieurs formes d’antennes. Nous allons maintenant examiner plus en détail les propriétés des différentes antennes. Les dipôles alimentés au centre sont des *antennes symétriques*. Une antenne symétrique est, dans l’idéal, une antenne dont les deux pôles (par exemple les points d’alimentation de chaque branche d’un dipôle) présentent, à un signe près, la même tension par rapport à la terre en fonctionnement. C’est le cas des dipôles, y compris les dipôles repliés et les antennes Yagi-Uda qui en sont dérivées. Une antenne Groundplane, en revanche, présente au point de connexion des radiales un potentiel de terre idéal (c’est-à-dire une tension nulle par rapport à la terre) et ne fait donc pas partie des antennes symétriques.


<indepth>
Pour les câbles servant au transport du signal, par exemple la *ligne d’alimentation* d’une antenne, on distingue également les câbles *symétriques* et *asymétriques*. Ici aussi, la symétrie concerne les tensions électriques idéales par rapport à la terre. Dans un câble coaxial, les courants doivent être symétriques, mais seul le conducteur intérieur présente une tension par rapport à la terre. Les câbles coaxiaux font donc partie des lignes d’alimentation asymétriques. Comme nous l’apprendrons plus tard, ces lignes d’alimentation asymétriques ne doivent être connectées à une antenne symétrique qu’au moyen d’un élément de symétrisation appelé *balun*.
</indepth>


[question:EG213]


---


Une forme d’antenne très populaire est un fil d’environ une longueur d’onde, disposé en cercle, en carré, en triangle ou sous une forme similaire. On parle alors d’*antennes en boucle à onde entière*. Très appréciée pour sa construction simple, l’antenne Delta-Loop, qui, comme le grand delta (Δ) de l’alphabet grec, a la forme d’un triangle.


<margin>
[picture:311:e_delta_loop:Exemple d’une antenne Delta-Loop]
</margin>

[question:EG101]


<indepth>
Dans le cas des antennes en boucle à onde entière, la *forme* exacte n’a pas d’importance tant que la longueur du fil correspond à environ une longueur d’onde. Selon la forme, la résistance d’alimentation ou le gain de l’antenne peuvent légèrement varier, pour le meilleur ou pour le pire.
</indepth>

---


À distinguer des antennes en boucle à onde entière, les *antennes à boucle magnétique* (Magnetic-Loops) ont des dimensions beaucoup plus petites par rapport à la longueur d’onde et génèrent un champ proche magnétique (cf. illustration [ref:e_mag_loop]).


<margin>
[picture:977:e_mag_loop:Exemple d’une antenne Magnetic-Loop]
</margin>

[question:EG105]


<indepth>
Bien que ces antennes à boucle magnétique soient fondamentalement adaptées à l’*émission*, il est difficile d’obtenir un *rendement* élevé. Des rendements compris entre $\qty{1}{\percent}$ et $\qty{10}{\percent}$ sont courants pour les Magnetic-Loops en émission. Malgré cela, ces antennes offrent des avantages par rapport à d’autres : outre leur construction compacte, elles sont souvent moins perturbées par des objets conducteurs ou atténuants situés dans leur champ proche, par exemple des murs ou des tuiles en cas de montage à l’intérieur ou sous un toit.
</indepth>

---


Les *antennes alimentées en bout* sont alimentées depuis une extrémité. Leur longueur est généralement d’une demi-onde. On parle alors d’un dipôle demi-onde alimenté en bout (en anglais : *end fed half wave*, EFHW). Une telle antenne nécessite une tension bien plus élevée que le courant, tension qui peut être générée par un élément d’adaptation approprié, par exemple un *circuit de Fuchs*. Les dipôles demi-onde alimentés en bout et adaptés avec un circuit de Fuchs sont appelés antennes Fuchs en conséquence.


[question:EG104]
[question:EG103]


<margin>
[picture:310:e_fuchsantenne:Exemple d’une antenne Fuchs]
</margin>

<person>
Le circuit de Fuchs, respectivement l’antenne Fuchs, porte le nom du *Dr. Josef Fuchs* (indicatif d’appel de radioamateur OE1JF, UO1JF et EAAA), qui l’a également breveté en 1927.
</person>

<indepth>
Une antenne alimentée en bout nécessite également un *contrepoids*, par exemple sous la forme d’un fil de $\lambda / 4$ ou d’une autre forme de mise à la terre HF. Cependant, les courants apparaissant aux points d’alimentation des EFHW sont nettement plus faibles, raison pour laquelle une mise à la terre moins bonne peut suffire, par exemple un court fil d’un dixième ou même d’un vingtième de la longueur d’onde. Parfois, même le blindage de la ligne d’alimentation ou d’autres éléments métalliques (destinés à d’autres usages) servent de mise à la terre.

Il ne faut pas confondre les dipôles demi-onde alimentés en bout avec les *antennes filaires longues* dont la longueur dépasse nettement une longueur d’onde. La confusion vient du fait que les dipôles demi-onde alimentés en bout sont souvent utilisés sur des fréquences plus élevées, ce qui, pour ces fréquences, en fait de facto une antenne filaire longue.
</indepth>

---


La *directivité* d’une antenne peut être représentée dans un diagramme de rayonnement. Pour un plan donné, on y représente dans chaque direction le gain, l’*intensité de champ* ou la *puissance rayonnée* dans le champ lointain. Plus la courbe s’éloigne du centre, plus le gain, l’intensité de champ ou la puissance rayonnée sont élevés. Si aucune échelle angulaire n’est utilisée, on représente souvent également la disposition mécanique de l’antenne dans le même diagramme pour clarifier quelle direction du diagramme correspond à quelle direction par rapport à la disposition de l’antenne.

Un dipôle ne rayonne pas, contrairement à ce que l’on pourrait croire à tort, dans la direction du fil, mais perpendiculairement à celui-ci. Dans un plan donné et représenté sous forme de diagramme de rayonnement, cela donne des lobes (par exemple à gauche et à droite) à côté du dipôle (cf. illustration [ref:e_dipol_strahlungsdiagramm]). Un dipôle suspendu verticalement rayonne donc, par exemple, vers la gauche et la droite ainsi que vers l’avant et l’arrière. Comme le diagramme de rayonnement ne considère qu’un seul plan, on ne voit par exemple qu’un lobe pour le rayonnement vers la gauche et un lobe pour le rayonnement vers la droite. Selon l’échelle, ces lobes peuvent apparaître circulaires.

<margin>
[picture:1045:e_dipol_strahlungsdiagramm:Exemple du rayonnement d’un dipôle]
</margin>

<indepth>
Un lobe de section *circulaire* résulte d’une échelle linéaire par rapport à l’intensité de champ lorsque l’on considère un dipôle fortement raccourci (dipôle de Hertz). Un dipôle demi-onde a en réalité un gain légèrement plus élevé correspondant à un lobe légèrement plus étroit. Pourtant, dans les questions d’examen, on trouve une représentation circulaire qui n’est qu’approximative. Si l’échelle était linéaire par rapport à la *puissance rayonnée* dans chaque direction, le lobe devrait même être encore plus étroit.
% TODO : éventuellement corriger l’image de la question
</indepth>

[question:EG215]
[question:EG214]


---


Grâce à sa caractéristique de rayonnement perpendiculaire au dipôle, un dipôle demi-onde monté verticalement permet un rayonnement plat, souhaitable par exemple en trafic DX ou lors de contacts via onde de sol ou onde directe.


[question:EG219]


<margin>
[photo:316:e_vertikaldipol:Dipôle vertical $\frac{\lambda}{2}$]
</margin>

---


Un cas particulier d’antenne verticale est l’antenne $\frac{5}{8}\lambda$ excitée par rapport à la terre (ou à la carrosserie d’un véhicule) (cf. illustration [ref:e_fuenf_achtel]). Sa longueur de $\qty{0.625}{\lambda}$ a été choisie pour une raison précise. Le radiateur est ainsi mécaniquement environ 2,5 fois plus long qu’une Groundplane normale ($\qty{0.25}{\lambda}$). Cette longueur accrue modifie avantageusement le diagramme de rayonnement vertical, comme illustré dans l’image [ref:a_5_8_lambda_strahlung] : une plus grande partie de la puissance rayonnée est concentrée vers l’horizon, moins est rayonnée vers le haut ou vers le bas. Cela permet généralement d’obtenir une portée plus grande pour les liaisons terrestres à puissance égale. Une longueur de radiateur d’environ $\frac{5}{8} \lambda$ est optimale pour cet effet : si le radiateur est rallongé, une plus grande partie de la puissance est à nouveau perdue vers le haut et vers le bas.


[question:EG108]


<margin>
[picture:1134:a_5_8_lambda_strahlung:Diagramme de rayonnement et répartition du courant d’antennes verticales avec sol idéal]
[picture:650:e_fuenf_achtel:Antenne $\frac{5}{8}\lambda$]
</margin>

---


Une antenne Groundplane rayonne également perpendiculairement au radiateur (pas aux radiales). Comme le diagramme de rayonnement de l’antenne Groundplane est souvent vu d’en haut, cela donne presque un *antenne omnidirectionnelle* dont le gain est presque identique dans toutes les directions (cf. illustration [ref:e_ground_plane_abstrahlung]). Les radiales n’ont qu’une faible influence et peuvent légèrement « déformer » le diagramme de rayonnement, ce qui correspond à un gain légèrement différent dans certaines directions.


<margin>
[picture:1046:e_ground_plane_abstrahlung:Rayonnement d’une antenne Groundplane]
</margin>

[question:EG216]


<indepth>
Bien que le diagramme de rayonnement d’une antenne Groundplane avec radiales soit légèrement « déformé », cet écart est en théorie bien plus faible que ce qui est souvent représenté. Une antenne Groundplane est donc en réalité un *antenne omnidirectionnelle* presque idéale dans le plan.
</indepth>

---


Les *antennes directionnelles* (par exemple l’antenne Yagi-Uda) se distinguent par un gain nettement plus élevé dans une direction que dans les autres, comme illustré dans l’image [ref:e_richtantenne_abstrahlung].


[question:EG217]


<margin>
[picture:1047:e_richtantenne_abstrahlung:Rayonnement d’une antenne directionnelle]
</margin>

---


Aux fréquences plus élevées, par exemple dans la bande UHF ou au-delà, on utilise également des *antennes cornet* ou des antennes paraboliques (cf. [ref:e_parabolantenne]). On trouve aussi des antennes patch sur les cartes de circuits imprimés de petits appareils. Toutes ces formes d’antennes sont inhabituelles en ondes courtes, car elles atteindraient des tailles peu maniables. C’est pourquoi, pour les questions suivantes, il ne reste plus que les antennes suivantes : antenne filaire longue, antenne Yagi-Uda, antenne dipôle, antenne Windom et antenne Delta-Loop.


[question:EG106]


<margin>
[picture:850:e_parabolantenne:Antenne parabolique]
</margin>

L’*antenne à manchon* est composée d’un pot de $\lambda / 4$ qui agit comme élément de symétrisation, respectivement comme *self de mode commun*. Avec cette information, on peut répondre à la question suivante, car aussi bien un manchon que le croisement d’une antenne Yagi-Uda ou un réflecteur parabolique seraient aussi encombrants dans la bande des $\qty{80}{\meter}$.

[question:EG107]