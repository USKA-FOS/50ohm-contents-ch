Le circuit en pont est un arrangement de quatre résistances utilisé, entre autres, pour la mesure précise des résistances. Un exemple pratique connu est le pont de Wheatstone. Le circuit est composé de deux diviseurs de tension connectés en parallèle. Entre les points centraux des deux diviseurs de tension se trouve la branche de pont, où la tension de pont $U_\mathrm{AB}$ peut être mesurée.

<margin>
[picture:343:a_Brückenschaltung:Circuit en pont typique avec 4 résistances]
</margin>

Le cas particulier du pont équilibré est particulièrement intéressant. Celui-ci se produit lorsque les rapports des diviseurs de tension des deux côtés sont égaux. Dans ce cas, les deux points centraux possèdent le même potentiel électrique et aucun courant ne circule à travers la branche de pont ou l'instrument de mesure connecté.

Les résistances individuelles n'ont pas besoin d'avoir la même valeur. L'important est simplement que le rapport des résistances des deux côtés soit identique.

Pour l'état équilibré, on a donc:

$ U_\mathrm{AB} = \qty{0}{\volt} $

et donc:

$ \frac{R_1}{R_2} = \frac{R_3}{R_4} $

Le pont de Wheatstone convient donc particulièrement bien pour la détermination de résistances inconnues ou de petites variations de résistance. Comment cela fonctionne exactement est décrit dans l'approfondissement ci-contre.

<indepth>
Le cas particulier où les rapports des diviseurs de tension dans le circuit en pont sont égaux des deux côtés est utilisé pour mesurer des résistances inconnues. Charles Wheatstone (physicien britannique) a reconnu dès 1833 l'importance du circuit en pont pour la mesure de résistances inconnues. 

Lors de la mesure, une résistance de précision réglable est modifiée jusqu'à ce que l'instrument de mesure sensible dans la branche de pont n'indique plus de courant. Le pont est alors équilibré, et on peut déterminer la valeur de la résistance inconnue à l'aide de la graduation et du multiplicateur de plage de mesure.

Un exemple est montré dans la figure [ref:a_pontavi]. Ici, il existe un multiplicateur qui peut prendre les valeurs de 0,1/1/10/100. Pour le réglage fin, il y a le grand bouton rotatif. 
[photo:286:a_pontavi:Pont de mesure de résistance selon Wheatstone (Pontavi)]

La figure [ref:a_pontavi_schaltung] montre le schéma simplifié de cet appareil de mesure. À l'endroit $X$, la résistance inconnue est connectée. Tout d'abord, on règle avec le multiplicateur l'ordre de grandeur estimé de la résistance inconnue. Ensuite, on modifie la résistance de précision avec le grand bouton rotatif jusqu'à ce que le pont soit équilibré. L'instrument de mesure indique alors qu'aucun courant ne circule plus à travers la branche de pont.

[picture:1076:a_pontavi_schaltung:Schéma du pont de mesure de résistance (Pontavi)]
</indepth>

[question:AD111]

Comme tous les résistances sont égales dans l'exercice suivant, les rapports des diviseurs de tension doivent également être égaux. Cela correspond au cas particulier décrit.

[question:AD112]

Dans la question suivante, le cas particulier ne s'applique pas, car les rapports des diviseurs de tension sont inégaux. Bien qu'il y ait des résistances similaires, elles sont cependant échangées de haut en bas. L'exercice peut être résolu avec les connaissances sur le diviseur de tension non chargé.

[question:AD113]

Du côté gauche, nous trouvons le rapport $\qty{1}{\kilo\ohm}$ à $\qty{10}{\kilo\ohm} = 1/10$.
À condition que l'instrument de mesure soit très haute impédance ou déconnecté, nous mesurons, pour une tension de service de $\qty{11}{\volt}$, du côté gauche, exactement $\qty{1}{\volt}$ sur la résistance supérieure ($R_1$) et $\qty{10}{\volt}$ sur la résistance inférieure ($R_2$). Le potentiel au point de mesure A est donc de $\qty{10}{\volt}$ mesuré par rapport à la masse.

Du côté droit, nous trouvons le rapport $\qty{10}{\kilo\ohm}$ à $\qty{1}{\kilo\ohm} = 10/1$ et mesurons donc $\qty{10}{\volt}$ sur la résistance supérieure ($R_3$) et $\qty{1}{\volt}$ sur la résistance inférieure ($R_4$). Le potentiel au point de mesure B est donc de $\qty{1}{\volt}$ mesuré par rapport à la masse.

La différence de potentiel entre A et B est donc de $\qty{9}{\volt}$, le point de mesure A étant $\qty{9}{\volt}$ plus positif que le point de mesure B.
