Dans la classe E, nous avons déjà fait connaissance avec la [ligne d’alimentation bifilaire](#), également appelée *ligne bifilaire* (voir figure [ref:a_huenerleiter]). Elle est composée de deux conducteurs parallèles. Les lignes bifilaires, lorsqu’elles sont alimentées et chargées de manière symétrique, se comportent également de façon symétrique en ce qui concerne la répartition du courant et de la tension. Cela signifie que le courant et la tension en un point donné sur les deux conducteurs ont la même valeur absolue, mais des signes opposés, comme illustré à la figure [ref:a_zweidrahtleitung].

<margin>
[photo:324:a_huenerleiter:Ligne bifilaire, également appelée ligne bifilaire]
</margin>

Les courants circulant sur les deux conducteurs sont donc toujours de sens opposés à tout moment. On parle alors de *courants en mode différentiel*. Les champs électromagnétiques générés par les deux conducteurs s’annulent donc en grande partie à distance, car ils agissent en opposition. Une ligne bifilaire exploitée de manière symétrique rayonne donc très peu.

<margin>
[picture:1107:a_zweidrahtleitung:Répartition du courant et de la tension sur une ligne bifilaire]
</margin>

Si la ligne d’alimentation n’est pas parfaitement symétrique, des *courants en mode commun* peuvent apparaître en plus. Dans ce cas, une partie du courant circule dans le même sens sur les deux conducteurs. Les champs générés par ces courants ne s’annulent pas mutuellement. La ligne d’alimentation peut alors agir comme une antenne et rayonner de l’énergie haute fréquence. De telles composantes en mode commun peuvent par exemple survenir si un dipôle n’est pas construit de manière parfaitement symétrique, si une antenne ou une charge asymétrique est connectée, ou si la transition entre une antenne symétrique et une ligne d’alimentation asymétrique n’est pas découplée par un balun ou une self de mode commun approprié.

[question:AG312]

Dans le champ proche d’autres lignes ou appareils électriques, une forte couplage électromagnétique peut également se produire. C’est pourquoi les lignes d’alimentation à l’intérieur des bâtiments sont généralement blindées, par exemple sous forme de câble coaxial. Dans un câble coaxial, les champs électromagnétiques du mode différentiel se trouvent principalement entre le conducteur intérieur et le blindage. Cela réduit à la fois le rayonnement de la ligne d’alimentation et l’injection de perturbations extérieures.

[question:AG301]

Le câble coaxial, qui est également une ligne blindée, est une solution pratique. Il existe en différentes versions. Dans la question suivante, nous examinerons les *propriétés haute fréquence* des câbles coaxiaux, c’est-à-dire leurs caractéristiques électriques à haute fréquence. Il s’agit principalement de :

* l’impédance caractéristique,
* l’affaiblissement du câble et le
* facteur de vélocité,

que nous allons examiner de plus près. Le rayon de courbure, en revanche, est une propriété mécanique indiquant à quel point le câble peut être plié serré. La perte de retour indique le nombre de réflexions présentes, ce qui dépend de la charge connectée à la ligne et n’est donc pas une propriété du câble.

[question:AG303]

Le facteur de vélocité est déterminé par le diélectrique situé entre le conducteur intérieur et le conducteur extérieur. C’est dans ce matériau que se propage principalement l’onde électromagnétique transmise par le câble. Le choix du diélectrique détermine la vitesse à laquelle une onde se propage dans le câble. La vitesse de propagation dans le câble coaxial est inférieure à la vitesse de la lumière dans l’espace libre. Les matériaux diélectriques courants sont le polyéthylène (PE) et le téflon (PTFE). Une mousse permet de créer un mélange avec de l’air, réduisant ainsi l’affaiblissement du câble.

[question:AG314]
[question:AG302]

La vitesse de propagation réduite par le diélectrique se reflète dans le facteur de vélocité, qui indique de combien un câble doit être raccourci mécaniquement pour avoir une longueur électrique donnée (par exemple, un quart de longueur d’onde). Dans le recueil de formules, nous trouvons la relation suivante pour le facteur de vélocité :

$k_\mathrm{v} = \frac{L_\mathrm{G}}{L_\mathrm{E}} = \frac{1}{\sqrt{\epsilon_\mathrm{r}}}$

Ici, $k_\mathrm{v}$ est le facteur de vélocité, $L_\mathrm{G}$ la longueur géométrique ("mécanique"), et $L_\mathrm{E}$ la longueur électrique. La permittivité relative $\epsilon_\mathrm{r}$ dépend du diélectrique utilisé. Pour le polyéthylène non expansé (PE), on peut trouver dans le recueil de formules une permittivité relative de $\num{2,29}$.

[question:AG317]