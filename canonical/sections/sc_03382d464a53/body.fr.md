Un circuit en *série* composé de deux *résistances* est souvent utilisé comme *diviseur de tension*. Nous considérons d’abord le *diviseur de tension non chargé*, comme il apparaît également dans les exercices suivants. Dans un diviseur de tension non chargé, les tensions sont proportionnelles aux résistances. Cela signifie par exemple qu’une tension plus élevée est mesurée aux bornes d’une résistance de forte valeur, tandis qu’une tension plus faible est mesurée aux bornes d’une résistance de faible valeur.


<margin>
[picture:819:E 63. Diviseur de tension:Diviseur de tension]
</margin>

<indepth>
Un diviseur de tension important se trouve par exemple à la *base* d’un transistor dans un circuit amplificateur. On parle alors de diviseur de tension de base. Nous l’examinerons plus en détail dans le chapitre sur les amplificateurs.
</indepth>

Cette relation peut être exprimée par différentes formules, que nous trouvons dans le recueil de formules :


$\frac{U_{1}}{U_{2}} = \frac{R_{1}}{R_{2}}$


ou

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$


% TODO implementiere Attention in CSS!
<danger>
Dans le cas d’un diviseur de tension chargé, ces formules ne s’appliquent pas. Des questions à ce sujet suivront dans le chapitre [sec:spannungsteiler_2].
</danger>

Dans les questions suivantes, le terme diviseur de tension n’est pas mentionné directement, mais la formulation : « Comment la tension se répartit-elle aux bornes de deux résistances montées en série ... » devrait permettre de reconnaître qu’il s’agit d’un diviseur de tension.

[question:ED101]

Aucune valeur concrète de résistance n’est indiquée, c’est pourquoi le résultat doit être présenté sous forme de formule générale. 
D’après l’énoncé, $R_1$ est 5 fois plus grand que $R_2$, donc une tension 5 fois plus élevée doit pouvoir être mesurée à ses bornes, ou $R_1 = 5 \cdot R_2$.


Cette relation peut être exprimée sous forme de formule :


$\frac{U_{1}}{U_{2}} = \frac{5 \cdot R_2}{R_2}$


Les $R_2$ s’annulent et on obtient :


$\frac{U_{1}}{U_{2}} = \frac{5}{1}$


Après quelques transformations, on obtient le résultat :


$U_{1} = U_{2} \cdot \frac{5}{1}$


$U_{1} = 5 \cdot U_{2}$


[question:ED102]

Dans cette question, la relation est inversée par rapport à la question ED 101. D’après l’énoncé, $R_1$ est 6 fois plus petit que $R_2$, donc une tension 6 fois plus faible doit pouvoir être mesurée à ses bornes.


Cette relation exprimée sous forme de formule est la suivante :


$\frac{U_{1}}{U_{2}} = \frac{1}{6}$
  
$U_{1} = U_{2} \cdot {\frac{1}{6}}$
  
$U_1 = \frac{U_2}{6}$


[question:ED103]

Dans cette question, des valeurs concrètes de résistance sont indiquées, qui servent à déterminer le rapport du diviseur de tension. $R_1$ est dans un rapport de $\qty{10}{\kilo\ohm}$ à $\qty{20}{\kilo\ohm}$ avec $R_2$, soit 1 pour 2. $U_2$ doit donc être deux fois plus grande que $U_1$. Cependant, la *tension totale* $U_g$ est indiquée. Cette dernière est appliquée à une *résistance totale* de $\qty{30}{\kilo\ohm}$ et est donc répartie dans un rapport de 30 pour 20 (ou 3 pour 2) par rapport à $R_2$. Une tension de $2/3$ de $U_g$ doit donc pouvoir être mesurée aux bornes de $R_2$.


Bien entendu, ce résultat peut également être calculé à l’aide de la formule du recueil de formules :


$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

et celle-ci ensuite résolue pour $U_2$ :


$U_{2} = \frac{R_{2}}{R_{1} + R_{2}} \cdot U_g$