Au début de ce chapitre, nous nous sommes occupés du dipôle comme forme de base de toutes les antennes. Le dipôle demi-onde émet des ondes radio perpendiculairement à la direction du fil. D'autres formes d'antennes peuvent émettre leurs ondes radio, selon leur construction, de préférence dans une ou plusieurs directions et moins dans d'autres directions :
* Une antenne Groundplane émet de manière presque uniforme dans toutes les directions du ciel, mais pas vers le haut ou le bas.
* Dans le cas d'une antenne Yagi-Uda, les ondes radio sont concentrées en un faisceau vers l'avant, comme une lampe de poche, et réduites dans toutes les autres directions.

Les valeurs limites prescrites par la procédure de preuve pour la protection des personnes dans les champs électromagnétiques doivent être respectées par une installation d'émission dans chaque direction. Si, à une certaine distance de l'antenne, les valeurs limites sont respectées dans la direction dans laquelle elle émet le plus fortement, alors elle respectera également les valeurs limites à la même distance dans toutes les autres directions. C'est pourquoi nous nous intéressons particulièrement à la direction de l'émission la plus forte. Celle-ci est appelée *direction du faisceau principal*.

---

La puissance avec laquelle une antenne émet dans sa direction de faisceau principal est exprimée par le *facteur de gain* par rapport au dipôle demi-onde. Celui-ci indique dans quelle mesure une antenne émet mieux dans la direction de faisceau principal respective par rapport à un dipôle demi-onde. Un facteur de gain de $\num{2}$ par rapport au dipôle demi-onde signifie, par exemple, qu'une antenne émet dans la direction de faisceau principal deux fois plus fortement qu'un dipôle demi-onde dans sa direction de faisceau principal.

<indepth>
% TODO: Rendre spécifique à l'édition
Au lieu du facteur de gain des antennes, on indique souvent le "gain en décibels ($\unit{\dB}$)". L'unité décibel fait l'objet du cours pour la classe E.
</indepth>

---

Pour indiquer maintenant combien une antenne concrète émet dans la direction de faisceau principal lorsque l'on entre une puissance d'émission déterminée, on multiplie la puissance d'émission par le facteur de gain par rapport au dipôle demi-onde. On obtient alors la *puissance rayonnée efficace*, qui est généralement abrégée en ERP (de l'anglais "effective radiated power"). Si l'on entre par exemple une puissance d'émission de $\qty{5}{\watt}$ dans une antenne avec un facteur de gain de $\num{2}$ par rapport au dipôle demi-onde, on obtient une puissance rayonnée de $\qty{10}{\watt}$ ERP.

<margin>
On peut se représenter la puissance rayonnée efficace (ERP) comme suit : il s'agit de la puissance qu'il faudrait injecter dans un dipôle demi-onde pour qu'il émette aussi fortement dans sa direction de faisceau principal que l'antenne considérée.
</margin>

Les antennes directionnelles peuvent avoir des facteurs de gain beaucoup plus élevés. Une antenne Yagi-Uda à 9 éléments peut par exemple atteindre facilement un facteur de gain de $\num{10}$ ou plus par rapport au dipôle demi-onde. Si l'on entre par exemple $\qty{100}{\watt}$ dans une telle antenne, la puissance rayonnée est déjà de $\qty{1000}{\watt}$ ERP ou plus !

[question:NG401]
