En modulation de phase, la phase d'une onde porteuse est modifiée en fonction du signal de modulation. Cela signifie que le déphasage de l'onde porteuse varie directement proportionnellement à l'amplitude du signal de modulation. Cette modification de la phase est conservée tout au long du signal et varie par rapport à l'onde porteuse initiale selon un motif déterminé. Le résultat est un signal sinusoïdal dont le « décalage » (phase) s'adapte en continu sans que l'amplitude du signal ne change.

On peut se représenter la modulation de phase comme le déplacement de la courbe sinusoïdale le long de l'axe temporel, chaque modification de la phase étant contrôlée par le signal de modulation. Plus l'amplitude du signal de modulation est forte, plus la phase du signal porteur se décale.

La modulation de phase et la modulation de fréquence appartiennent toutes deux au groupe des techniques de modulation angulaire, car elles influencent toutes deux l'angle de l'onde porteuse. La différence réside dans le fait que, dans la modulation de fréquence, c'est la fréquence qui est directement influencée, tandis que dans la modulation de phase, c'est la phase.

Cela se voit particulièrement bien avec un signal utile en forme d'onde rectangulaire : en modulation de phase, chaque front de l'onde rectangulaire provoque un saut de phase immédiat du signal porteur, tandis qu'en modulation de fréquence, le front du signal ne fait que déclencher un changement de fréquence – la modification de phase qui en résulte n'apparaît qu'indirectement, en s'accumulant de manière continue dans le temps.

<margin>
[picture:907:a_phasenmodulation:Modulation de phase avec inversion de phase]
</margin>

<webonly>
<margin>
[include:applet_pm]
</margin>
</webonly>

<indepth>
Pour les personnes intéressées par les mathématiques : dans la modulation de phase, le signal utile $m(t)$ a une influence directe sur la phase, par exemple :

$\varphi(t) = m(t)$

Le signal porteur est généré sous la forme d'une oscillation sinusoïdale :

$s(t) = A_c \cos(2\pi f_c t + \varphi(t))$

où $A_c$ est l'amplitude, $f_c$ la fréquence porteuse et $\varphi(t)$ la phase modulée.

Les deux types de modulation FM et PM sont étroitement liés : la modulation de phase d'un signal entraîne indirectement une modification de la fréquence, et inversement, la modulation de fréquence produit une modification de la phase. Mathématiquement, le lien entre fréquence et phase peut s'exprimer par la relation suivante :

$f_i(t) = \frac{1}{2\pi} \cdot \frac{d\varphi(t)}{dt}$

Cela signifie que la fréquence est la dérivée temporelle de la phase.

Il est donc possible de réaliser une modulation de fréquence par modulation de phase en intégrant le signal utile $m(t)$ :

$\varphi(t) = 2\pi \int m(t) \, dt$

Le résultat est ensuite utilisé comme $\varphi(t)$ dans la fonction porteuse.
</indepth>

[question:AE313]