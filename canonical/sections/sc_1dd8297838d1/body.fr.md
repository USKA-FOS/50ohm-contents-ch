Les émetteurs-récepteurs doivent parfois être réaccordés, par exemple après des réparations ou lorsque des composants ont changé en raison du vieillissement. Pour les récepteurs, le réaccordement inclut le contrôle des fréquences de l'oscillateur. Pour cela, on utilise généralement un fréquencemètre.

[question:EI501]

L'illustration [ref:e_frequenzzaehler1] montre l'affichage d'un fréquencemètre. Le chiffre trois isolé à droite, comme sur certaines calculatrices, représente $\num{10^3}$. Ainsi, le compteur mesure la fréquence $\qty{455}\cdot \qty{10^3}{\hertz}$ ou $\qty{455}{\kilo\hertz}$. Les appareils de mesure plus récents affichent directement le préfixe d'unité au lieu de la puissance de dix.

<margin>
[photo:187:e_frequenzzaehler1:Affichage d'un fréquencemètre indiquant $\qty{455}\cdot \qty{10^3}{\hertz}$]
</margin>

<indepth>
La fréquence $\qty{455}{\kilo\hertz}$ est souvent utilisée comme fréquence intermédiaire dans les récepteurs à superhétérodyne et peut être mesurée lorsque le récepteur est accordé sur un signal fort.
</indepth>

---

Dans les instructions de réaccordement, il est souvent demandé de régler une fréquence avec une tolérance précise, par exemple $\pm\qty{10}{\hertz}$. Dans ces cas, il est utile de connaître la valeur de position des différents chiffres. La puissance de dix affichée par l'appareil de mesure, c'est-à-dire pour $\qty{455}{\kilo\hertz}$ la valeur $\num{10^3}$ ou $\num{1000}$, s'applique toujours au chiffre situé directement avant la virgule. Le chiffre à gauche correspond à $\qty{10}{\kilo\hertz}$ ou $\qty{10^4}{\hertz}$, et celui encore plus à gauche, dans l'exemple le chiffre quatre, correspond à $\qty{100}{\kilo\hertz}$ ou $\qty{10^5}{\hertz}$. Vers la droite, cela fonctionne dans l'autre sens.

Dans l'illustration [ref:e_frequenzzaehler_stellen], nous voyons un exemple avec une fréquence plus élevée.

<margin>
[picture:793:e_frequenzzaehler_stellen:Cet affichage représente une fréquence en $\unit{\mega\hertz}$. C'est également la valeur de position du chiffre avant la virgule.]
</margin>

<attention>
Les entrées des fréquencemètres peuvent présenter une résistance interne élevée. Cela est comparable aux voltmètres et aux oscilloscopes. Cependant, il existe aussi des connexions avec $\qty{50}{\ohm}$. Elles sont généralement très sensibles et la tension ou la puissance maximale indiquée dans le manuel de l'appareil ne doit en aucun cas être dépassée.
</attention>

[question:EI502]
[question:EI503]

Les fréquencemètres sont conçus pour une plage de valeurs spécifique, par exemple de $\qty{100}{\kilo\hertz}$ à $\qty{2}{\giga\hertz}$. En dehors de cette plage, ils mesurent de manière imprécise ou ne mesurent pas du tout. Pour mesurer des fréquences plus élevées, il existe des diviseurs de fréquence. Ils divisent la fréquence d'un signal appliqué à leur entrée par une valeur fixe et fournissent le résultat sous forme d'oscillation électrique à la sortie. On les appelle aussi prédiviseurs, car ils sont placés entre l'objet de mesure et le compteur.

%TODO Image diviseur de fréquence

Les prédiviseurs divisent souvent la fréquence par dix. Si l'on applique $\qty{2,4}{\giga\hertz}$ à l'entrée d'un tel diviseur 10:1, le fréquencemètre en aval affichera $\qty{240}{\mega\hertz}$.

[question:EI504]