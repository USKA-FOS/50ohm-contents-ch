Le circuit en pont est un montage composé de quatre **résistances**, utilisé notamment pour la mesure précise de **résistances**. Un exemple pratique bien connu est le pont de Wheatstone. Le circuit se compose de deux **diviseurs de tension** montés en parallèle. Entre les points milieux des deux **diviseurs de tension** se trouve la branche de pont, où l’on peut mesurer la **tension de pont** $U_\mathrm{AB}$.


<margin>
[picture:343:a_Brückenschaltung:Montage typique d'un circuit en pont avec 4 résistances]
</margin>

Un cas particulièrement intéressant est celui du pont équilibré. Il se produit lorsque les rapports des **diviseurs de tension** sont égaux des deux côtés. Les deux points milieux présentent alors le même potentiel électrique et aucun **courant** ne circule dans la branche de pont ou l’instrument de mesure connecté.


Les **résistances** individuelles n’ont pas besoin d’avoir la même valeur. Il suffit que le rapport des **résistances** soit identique des deux côtés.


Pour l’état équilibré, on a donc :


$ U_\mathrm{AB} = \qty{0}{\volt} $


et par conséquent :


$ \frac{R_1}{R_2} = \frac{R_3}{R_4} $


Le pont de Wheatstone est donc particulièrement adapté pour déterminer des **résistances** inconnues ou de faibles variations de **résistance**. La manière dont cela fonctionne précisément est décrite dans l’approfondissement ci-contre.


<indepth>
Le cas particulier où les rapports des **diviseurs de tension** dans le circuit en pont sont égaux à gauche et à droite est utilisé pour mesurer des **résistances** inconnues. Charles Wheatstone (physicien britannique) a reconnu dès 1833 l’importance du circuit en pont pour la mesure de **résistances** inconnues.


Pour la mesure, on fait varier une **résistance** de précision réglable jusqu’à ce que l’instrument de mesure sensible dans la branche de pont n’indique plus de **courant**. Le pont est alors équilibré, et on peut déterminer la valeur de la **résistance** inconnue à l’aide de l’échelle et du **multiplicateur** de plage de mesure.


Un exemple est visible dans l’image [ref:a_pontavi]. Il y a un **multiplicateur** dont les valeurs peuvent être 0,1/1/10/100. Pour le réglage fin, il y a le grand bouton rotatif.

[photo:286:a_pontavi:Pont de mesure de résistance selon Wheatstone (Pontavi)]


L’image [ref:a_pontavi_schaltung] montre le schéma électrique simplifié de cet appareil de mesure. À l’emplacement $X$, on connecte la **résistance** inconnue. On commence par régler le **multiplicateur** sur l’ordre de grandeur estimé de la **résistance** inconnue. Ensuite, avec le grand bouton rotatif, on fait varier la **résistance** de précision jusqu’à ce que le pont soit équilibré. L’instrument de mesure indique alors qu’aucun **courant** ne circule plus dans la branche de pont.


[picture:1076:a_pontavi_schaltung:Schéma électrique du pont de mesure de résistance (Pontavi)]
</indepth>


[question:AD111]


Dans la tâche suivante, toutes les **résistances** sont de même valeur, donc les rapports des **diviseurs de tension** sont également égaux. Cela correspond au cas particulier décrit.


[question:AD112]


Dans la question suivante, le cas particulier ne s’applique pas, car les rapports des **diviseurs de tension** ne sont pas égaux. Bien que des **résistances** similaires soient présentes, elles sont inversées de haut en bas. La tâche peut être résolue avec les connaissances sur le **diviseur de tension** non chargé.


[question:AD113]


Du côté gauche, nous avons le rapport $\qty{1}{\kilo\ohm}$ à $\qty{10}{\kilo\ohm} = 1/10$.
En supposant que l’instrument de mesure est très haute **impédance** ou déconnecté, avec une **tension de service** de $\qty{11}{\volt}$, nous mesurons du côté gauche sur la **résistance** supérieure ($R_1$) exactement $\qty{1}{\volt}$ et sur la **résistance** inférieure ($R_2$) $\qty{10}{\volt}$. Le potentiel au point de mesure A est donc de $\qty{10}{\volt}$ par rapport à la **masse**.


Du côté droit, nous avons le rapport $\qty{10}{\kilo\ohm}$ à $\qty{1}{\kilo\ohm} = 10/1$ et mesurons donc $\qty{10}{\volt}$ sur la **résistance** supérieure ($R_3$) et $\qty{1}{\volt}$ sur la **résistance** inférieure ($R_4$). Le potentiel au point de mesure B est donc de $\qty{1}{\volt}$ par rapport à la **masse**.


La différence de potentiel entre A et B est donc de $\qty{9}{\volt}$, le point de mesure A étant $\qty{9}{\volt}$ plus positif que le point de mesure B.