Jusqu'à présent, nous avons examiné les champs électriques et magnétiques dans le cas où ces champs ne varient pas dans le temps. Cependant, dans la technique radio, ces champs sont en réalité sans intérêt, car nous nous occupons de tensions et de courants qui varient dans le temps. De même, les champs électriques et magnétiques générés sont variables dans le temps.

<margin>
[picture:885:e_vertikalantenne_em:Champ électrique et champ magnétique sur une antenne]
</margin>

Des effets supplémentaires apparaissent alors. Dès 1831, Michael Faraday a découvert qu'un champ magnétique variable dans le temps induit une tension électrique dans un conducteur voisin. Cet effet, appelé *induction*, est par exemple utilisé dans le transformateur : un courant variable dans le temps (par exemple sinusoïdal) dans l'enroulement primaire génère un champ magnétique variable dans le temps, qui induit à son tour une tension dans l'enroulement secondaire.

Pour comprendre que, inversement, la variation d'un champ électrique entraîne l'apparition d'un champ magnétique, imaginons un condensateur à plaques dont les armatures forment un circuit électrique avec une source de tension externe. Si nous modifions le champ électrique à l'intérieur du condensateur, des charges doivent être déplacées dans le circuit extérieur. Le déplacement de porteurs de charge implique un courant électrique. Ce courant électrique génère alors à son tour un champ magnétique autour du conducteur.

Bien que les modèles utilisant des conducteurs électriques soient intuitifs pour nous, il est essentiel de comprendre que ces conducteurs ne sont pas nécessaires. Les champs magnétiques et électriques existent également en dehors des conducteurs, même dans le vide. Ici aussi, un champ magnétique variable dans le temps génère un champ électrique variable dans le temps. Ce champ électrique variable entraîne à son tour l'apparition d'un champ magnétique variable. *Les champs magnétiques et électriques variables dans le temps sont donc toujours couplés.* C'est pourquoi nous parlons de *champ électromagnétique*. En résumé : une onde électromagnétique, qui peut se propager librement dans l'espace, repose sur l'interaction entre des champs magnétiques et électriques variables dans le temps.

[question:EB302]

Comme décrit précédemment, des tensions et courants constants dans le temps ne peuvent pas générer de champ électromagnétique. Pour cela, nous avons besoin d'un courant variable dans le temps dans un conducteur.

[question:EB301]

<indepth>
Le champ magnétique et le champ électrique sont en réalité décrits par des *vecteurs*, c'est-à-dire des grandeurs qui ont une direction dans l'espace. Mathématiquement, on peut montrer que dans le *champ lointain*, c'est-à-dire suffisamment loin de l'antenne, les vecteurs des deux champs doivent être perpendiculaires l'un à l'autre. La direction de propagation de l'onde électromagnétique (c'est-à-dire notre signal radio ...) est quant à elle perpendiculaire à la fois au champ électrique et au champ magnétique.

[picture:886:e_emfeld_ausbreitung:Propagation de l'onde électromagnétique]

Les relations décrites sont mathématiquement exprimées par les *équations de Maxwell*, du nom de James Clerk Maxwell, qui les a élaborées entre 1861 et 1864 à partir d'observations d'autres physiciens. Il en a conclu que les champs magnétiques et électriques devaient être couplés :

1. $\vec{\nabla} \cdot \vec{E} =\frac{\rho}{\varepsilon_{0}}$
2. $\vec{\nabla} \cdot \vec{B} = 0$
3. $\vec{\nabla} \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$
4. $\vec{\nabla } \times \vec{B} =\mu_0 (\vec{j} +\varepsilon_0 \frac{\partial\vec{E}}{\partial t})$

L'équation (3) montre qu'un champ magnétique variable dans le temps génère un champ électrique. Ce champ électrique variable contribue, selon l'équation (4), via le courant de déplacement, à la génération d'un champ magnétique. Ces relations vont bien au-delà de ce qu'il faut savoir en radioamateurisme.

L'existence du champ électromagnétique n'a été démontrée expérimentalement que plus de vingt ans plus tard (1886) par Heinrich Hertz.
</indepth>

<indepth>
Comme les équations de Maxwell sont présentées ci-dessus, voici une explication de la symbolique spéciale utilisée :

L'*opérateur nabla* ∇ est un outil mathématique qui décrit comment un champ (par exemple un champ électrique ou magnétique) varie d'un point à l'autre. Selon la manière dont il est utilisé, il indique où les lignes de champ apparaissent ou disparaissent, ou si elles tournent autour d'un point.

Le point ⋅ signifie *divergence*. Il décrit si des lignes de champ apparaissent ou disparaissent en un point.

La croix × signifie *rotation*. Elle décrit à quel point un champ « tourbillonne ».

Il est à noter que la compréhension et l'application des équations de Maxwell vont bien au-delà des connaissances exigées à l'examen. Cependant, il s'agit d'un fondement si essentiel de l'électrotechnique qu'il est bon d'en avoir au moins entendu parler une fois.
</indepth>

Comme le montrent les figures et [ref:e_emfeld_ausbreitung], dans le champ lointain (loin de l'antenne), la composante du champ magnétique est toujours perpendiculaire à la composante du champ électrique.

[question:EB303]

Les composantes du champ magnétique et du champ électrique, perpendiculaires l'une à l'autre dans le champ lointain, déterminent également la direction de propagation $S$, comme le montre la figure [ref:e_vertikalantenne_em] : elle est à son tour perpendiculaire aux deux. On peut s'imaginer que le champ magnétique et le champ électrique définissent un plan sur lequel la direction de propagation est perpendiculaire.

[question:EB304]