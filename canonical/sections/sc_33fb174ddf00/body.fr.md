Dans la section [sec:kondensator_1], nous avons déjà appris la capacité d'un condensateur ainsi que son comportement qualitatif sous tension alternative : un condensateur se comporte comme une résistance dépendante de la fréquence. Nous avons d'abord noté que la réactance capacitive est inversement proportionnelle à la fréquence. Si on diminue la fréquence, la réactance $X_C$ augmente. En revanche, si on augmente la fréquence, la résistance diminue en conséquence. Le comportement d'un condensateur sous tension alternative peut être décrit par la formule de la réactance capacitive $X_C$ :

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

Ici, nous allons maintenant examiner ce comportement plus en détail et comprendre pourquoi cette résistance est appelée "réactance". Cependant, nous devons d'abord retenir que la réactance d'un condensateur est également négative, afin de pouvoir résoudre la question suivante :

[question:AC102]

<indepth>
Pourquoi la réactance capacitive est-elle négative ? La raison réside dans le calcul complexe des courants alternatifs, qui n'est pas strictement nécessaire pour l'examen de radioamateur.

Pour les lecteurs et lectrices ayant des connaissances en nombres complexes, il est à noter que la représentation correcte de la réactance capacitive est en réalité

$X_C = \frac{1}{j\omega C}$

où $j$ représente l'unité imaginaire $\sqrt{-1}$.

En multipliant cette expression par $j$, on obtient :

$X_C = \frac{1}{j\omega C} = \frac{1 \cdot j}{j\omega C \cdot j} =\frac{-j}{\omega C}$

On voit ainsi que la réactance capacitive n'est pas seulement négative, mais aussi complexe. Le signe négatif décrit le déphasage entre le courant et la tension aux bornes du condensateur, que nous examinerons de plus près dans ce chapitre.
</indepth>

---

Les appareils de mesure modernes et économiques que les radioamateurs utilisent volontiers aujourd'hui sont les analyseurs d'antennes ou les analyseurs de réseau vectoriels (VNA). Ils mesurent la variation de la réactance $X_C$ en fonction de la fréquence et peuvent également afficher graphiquement le résultat de la mesure.
La figure [ref:a_kapazitiver_Blindwiderstand] montre la variation de la réactance capacitive (ligne bleue) d'un condensateur Styroflex de $\qty{1500}{\pico\farad}$ dans la bande de fréquences de $\qtyrange{1}{4,5}{\mega\hertz}$.

<margin>
[photo:248:a_kapazitiver_Blindwiderstand:Réactance capacitive $X_C$ (courbe bleue) et déphasage (courbe rouge) d'un condensateur Styroflex de $\qty{1500}{\pico\farad}$ dans la bande de fréquences de $\qtyrange{1}{4,5}{\mega\hertz}$.]
</margin>


Essayez maintenant de répondre aux questions suivantes à l'aide de la formule ci-dessus. Portez une attention particulière aux unités et aux puissances de dix pour obtenir les bons résultats.

[question:AC104]
[question:AC105]
[question:AC106]
[question:AC107]

Pour la question suivante, la capacité est recherchée. Essayez de réarranger la formule pour pouvoir calculer la capacité $C$ :

[question:AC108]

---

Si on effectue une mesure simultanée du courant et de la tension sur un condensateur avec un oscilloscope à deux voies (cf. [ref:a_strom_eilt_vor]), on obtient un résultat initialement surprenant : il existe un déphasage de $\qty{90}{\degree}$ entre le courant et la tension, le courant étant en avance sur la tension.

Cela signifie que le courant atteint déjà sa valeur maximale alors que la tension est encore en train d'augmenter. Ce comportement caractéristique est une propriété fondamentale des condensateurs et joue un rôle important en technique des courants alternatifs, notamment dans les filtres et les circuits oscillants.
La ligne rouge dans la figure [ref:a_kapazitiver_Blindwiderstand] représente le déphasage de la réactance capacitive, qui est presque constant à $\qty{-90}{\degree}$.

[question:AC101]

<margin>
[photo:268:a_strom_eilt_vor:Déphasage sur un condensateur entre tension et courant]
</margin>

<tip>
Aide-mémoire : Dans le condensa*t*eur, le courant est en ava*n*ce !
</tip>

---

Le déphasage entre la tension et le courant est donc de $\qty{90}{\degree}$, le courant (rouge) étant en avance sur la tension (bleue), comme le montre la figure [ref:a_blindleistung_kondensator]. Si on considère la puissance instantanée avec $P = U \cdot I$, on obtient une courbe de puissance (verte) qui oscille symétriquement autour de la ligne zéro, également représentée dans la figure [ref:a_blindleistung_kondensator].

<margin>
[picture:943:a_blindleistung_kondensator:Le produit de $U \cdot I$ donne la courbe de puissance verte]
</margin>

La valeur moyenne de cette puissance est nulle, c'est-à-dire qu'aucune puissance active n'est consommée. Au lieu de cela, de l'énergie est périodiquement stockée dans le champ électrique du condensateur et restituée à la source. On parle donc, pour un condensateur idéal sans pertes, de puissance réactive et d'une réactance.

Seule une résistance ohmique consomme de la puissance active, car la tension et le courant y sont en phase, c'est-à-dire qu'il n'y a pas de déphasage. Cela signifie que la tension et le courant sont simultanément positifs ou négatifs, de sorte que la puissance instantanée $P = U \cdot I$ est toujours positive.

Une réactance idéale, en revanche, ne consomme aucune puissance active et ne chauffe donc pas dans le cas idéal. Au lieu de cela, de l'énergie est périodiquement stockée et restituée à la source.

[question:AC111]

[question:AC103]

---

Si un condensateur chauffe néanmoins dans des applications haute fréquence, cela indique des pertes dans le composant. Un condensateur idéal ne convertirait pas d'énergie en chaleur, mais les condensateurs réels possèdent des propriétés parasites qui entraînent des pertes.

Ces pertes peuvent être identifiées dans le schéma équivalent : la résistance $R_\text{ESR}$ (Equivalent Series Resistance) décrit les pertes ohmiques dans le condensateur, tandis que $R_\text{Isolator}$ modélise les pertes dans le diélectrique / matériau isolant. De plus, l'inductance parasite $L_\text{ESL}$ influence le comportement à haute fréquence.

Pour l'évaluation technique de ces pertes, on utilise le facteur de qualité $Q$ (Quality Factor) ainsi que le facteur de pertes $\tan\delta$. Ces deux grandeurs décrivent à quel point un condensateur réel s'écarte du comportement idéal.

Il existe une relation directe entre les deux grandeurs :

$Q = \frac{1}{\tan\delta}$

À retenir : Des pertes élevées conduisent à un faible facteur de qualité $Q$ et donc à un grand facteur de pertes $\tan\delta$. Plus la fréquence est élevée, plus ces pertes sont importantes, car la réactance $X_C$ diminue avec l'augmentation de la fréquence, tandis que les résistances parasites restent constantes.

<margin>
[picture:1065:a_ersatzchaltbild_kondensator:Schéma équivalent d'un condensateur réel avec pertes parasites.]
</margin>

---

[question:AC109]

[question:AC110]

<indepth>
Grâce au calcul complexe des courants alternatifs, on peut représenter la réactance $X_C$ avec les pertes parasites $R$ sous la forme d'un diagramme vectoriel :
[picture:1066:a_tan_delta:$\tan\delta$ dans le diagramme vectoriel complexe]

La tangente décrit le rapport du côté opposé au côté adjacent, c'est-à-dire dans ce cas les pertes $R$ par rapport à la réactance capacitive sans pertes $X_C$.

$\tan\delta = \frac{R}{|X_C|}$

Plus les pertes sont grandes, plus l'angle $\delta$ est grand, et donc plus le facteur de pertes $\tan\delta$ est grand. Un condensateur idéal aurait un angle de $\delta = 0$ degré, car il n'a pas de pertes.

Grâce à cette addition complexe ou géométrique, on obtient la grandeur $Z$. Elle est appelée *impédance* et décrit la résistance totale complexe d'un composant. La valeur absolue de l'impédance $|Z|$ correspond à la *impédance* apparente.
</indepth>
