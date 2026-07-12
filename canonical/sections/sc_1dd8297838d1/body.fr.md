Les appareils radio doivent parfois être réajustés, par exemple après des réparations ou lorsque des composants se sont modifiés avec le temps. Pour les récepteurs, l'ajustement comprend le contrôle des fréquences de l'oscillateur. Pour cela, on utilise généralement un compteur de fréquence.

[question:EI501]

L'image [ref:e_frequenzzaehler1] montre l'affichage d'un compteur de fréquence. Le trois détaché tout à droite représente, comme dans certains calculatrices de poche, $\num{10^3}$. Ainsi, le compteur mesure la fréquence $\qty{455}\cdot \qty{10^3}{\hertz}$ ou $\qty{455}{\kilo\hertz}$. Les nouveaux appareils de mesure affichent directement le préfixe d'unité.

<margin>
[photo:187:e_frequenzzaehler1:Afficheur d'un compteur de fréquence affichant $\qty{455}\cdot \qty{10^3}{\hertz}$]
</margin>

% J'ai retiré cela pour des raisons de place
%<margin> 
%[photo:189:e_frequenzzaehler2:Multimètre affichant dans la plage de mesure de fréquence $\qty{455}{\kilo\hertz}$. Au-dessus apparaissent un symbole pour une faible tension de batterie, l'humidité de l'air et la température. Ces valeurs n'ont rien à voir avec la mesure de fréquence.]
%</margin>

<indepth>
La fréquence $\qty{455}{\kilo\hertz}$ apparaît fréquemment comme fréquence intermédiaire des récepteurs superhétérodynes et peut être mesurée lorsque le récepteur est accordé sur un signal fort.
</indepth>

---

Dans les instructions d'ajustement, on demande souvent d'ajuster une fréquence avec une certaine précision, par exemple $\pm\qty{10}{\hertz}$. Dans de tels cas, il est utile de se représenter la valeur de chaque chiffre. La puissance de dix indiquée par l'appareil de mesure, donc pour $\qty{455}{\kilo\hertz}$ la valeur $\num{10^3}$ ou $\num{1000}$, s'applique toujours à la position directement avant la virgule. La position à gauche de celle-ci représente alors $\qty{10}{\kilo\hertz}$ ou $\qty{10^4}{\hertz}$ et la position encore plus à gauche, dans l'exemple le quatre, $\qty{100}{\kilo\hertz}$ ou $\qty{10^5}{\hertz}$. Vers la droite, cela va dans l'autre sens.

Dans la figure [ref:e_frequenzzaehler_stellen], nous voyons un exemple avec une fréquence plus élevée.

<margin>
[picture:793:e_frequenzzaehler_stellen:Cet affichage représente une fréquence en $\unit{\mega\hertz}$. Il s'agit en même temps de la valeur de position du chiffre avant la virgule.]
</margin>

<attention>
Les entrées des compteurs de fréquence peuvent avoir une résistance interne élevée. Nous connaissons cela des voltmètres et des oscilloscopes. Mais il existe aussi des connexions avec $\qty{50}{\ohm}$. Elles sont généralement très sensibles et la valeur maximale indiquée dans le manuel de l'appareil pour la tension ou la puissance ne doit en aucun cas être dépassée.
</attention>

[question:EI502]
[question:EI503]

Les compteurs de fréquence sont construits pour une certaine plage de valeurs, par exemple $\qty{100}{\kilo\hertz}$ à $\qty{2}{\giga\hertz}$. En dehors de cette plage, ils mesurent de manière imprécise ou pas du tout. Pour mesurer des fréquences plus élevées, il existe des diviseurs de fréquence. Ils divisent la fréquence d'un signal, que l'on applique à leur entrée, par une valeur fixe et donnent le résultat sous forme d'oscillation électrique à la sortie. On les appelle aussi prédiviseurs, car ils sont branchés entre l'objet à mesurer et le compteur.

%TODO Image diviseur de fréquence

Souvent, les prédiviseurs divisent la fréquence par dix. Si l'on applique $\qty{2,4}{\giga\hertz}$ à l'entrée d'un diviseur 10:1, le compteur de fréquence derrière indique $\qty{240}{\mega\hertz}$.

[question:EI504]