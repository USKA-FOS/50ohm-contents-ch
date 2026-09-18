Au début de ce chapitre, nous avons abordé le dipôle comme forme de base de toutes les antennes. Le dipôle demi-onde émet des ondes radio perpendiculairement à la direction du fil. D’autres types d’antennes peuvent, selon leur conception, émettre leurs ondes radio de manière préférentielle dans une ou plusieurs directions, et moins dans d’autres :
* Une antenne Groundplane émet de manière quasi uniforme dans toutes les directions horizontales, mais pas vers le haut ou vers le bas.
* Une antenne Yagi-Uda concentre les ondes radio en un faisceau dirigé vers l’avant, comme une lampe torche, et réduit les émissions dans les autres directions.

---

<law>
Les valeurs limites que doit respecter une installation d’émission sont définies dans l’ordonnance sur la protection contre les rayonnements non ionisants [ORNI](https://www.fedlex.admin.ch/eli/cc/2000/38/fr). L’ORNI est un texte très complet qui s’applique également aux services de radiocommunication commerciaux. Voici un résumé des aspects pertinents pour les installations de radioamateur :

*Valeurs limites pour les installations de radioamateur*

Les installations de radioamateur doivent respecter les *valeurs limites d’immission* de l’ORNI. Selon la fréquence, celles-ci se situent entre 28 et 87 [V/m].
Pour calculer les distances à respecter, il existe dans l’espace membre de l’USKA des programmes ou des tableaux Excel adaptés :

[Outils de calcul pour l’ORNI](https://uska.ch/emissions-berechnung/)

En outre, *aucune valeur limite d’installation* ne doit être respectée tant que la durée d’exploitation est *inférieure à 800 heures par an*. Cela est pratiquement toujours le cas pour les applications radioamateur. Si une installation émet exceptionnellement plus longtemps, elle doit respecter une valeur limite d’installation dans les lieux à occupation sensible (LOS). Cette valeur est de 8,5 V/m pour les émetteurs en ondes longues et moyennes, et de 3,0 V/m pour toutes les autres bandes de fréquences.
[Source](https://www.bafu.admin.ch/fr/radioamateurisme-comme-source-de-smog-electromagnetique)

Les « lieux à occupation sensible » (LOS) désignent les endroits où des personnes séjournent régulièrement pendant de longues périodes.
</law>

---

Les valeurs limites prescrites par la procédure de preuve pour la protection des personnes contre les champs électromagnétiques doivent être respectées par une installation d’émission dans toutes les directions. Si, à une certaine distance de l’antenne, les valeurs limites sont respectées dans la direction où l’émission est la plus forte, alors elles le seront également à la même distance dans toutes les autres directions. C’est pourquoi nous nous intéressons particulièrement à la direction de l’émission maximale, appelée *direction principale de rayonnement*.

---

La force avec laquelle une antenne émet dans sa direction principale de rayonnement est exprimée par le *facteur de gain* par rapport au dipôle demi-onde. Celui-ci indique dans quelle mesure une antenne émet mieux qu’un dipôle demi-onde dans sa direction principale de rayonnement. Un facteur de gain de $\num{2}$ par rapport au dipôle demi-onde signifie par exemple qu’une antenne émet deux fois plus fortement dans sa direction principale de rayonnement qu’un dipôle demi-onde dans la sienne.

<indepth>
% TODO : À adapter selon l’édition
Au lieu du facteur de gain des antennes, on indique souvent le « gain en décibels ($\unit{\dB}$) ». Le cours aborde l’unité décibel dans le chapitre [sec:dezibel_1].
</indepth>

---

Pour indiquer la puissance émise par une antenne dans sa direction principale de rayonnement avec une puissance d’émission donnée, on multiplie la puissance d’émission par le facteur de gain par rapport au dipôle demi-onde. On obtient ainsi la *puissance rayonnée effective*, généralement abrégée ERP (de l’anglais *effective radiated power*). Par exemple, si l’on injecte une puissance d’émission de $\qty{5}{\watt}$ dans une antenne avec un facteur de gain de $\num{2}$ par rapport au dipôle demi-onde, on obtient une puissance rayonnée de $\qty{10}{\watt}$ ERP.

<margin>
On peut également se représenter la puissance rayonnée effective (ERP) de la manière suivante : c’est la puissance qu’il faudrait injecter dans un dipôle demi-onde pour qu’il émette aussi fortement dans sa direction principale de rayonnement que l’antenne considérée.
</margin>

Les antennes directives peuvent avoir des facteurs de gain bien plus élevés. Une antenne Yagi-Uda à 9 éléments peut par exemple facilement atteindre un facteur de gain de $\num{10}$ ou plus par rapport au dipôle demi-onde. Si l’on injecte $\qty{100}{\watt}$ dans une telle antenne, la puissance rayonnée atteint déjà $\qty{1000}{\watt}$ ERP ou plus !

[question:NG401]