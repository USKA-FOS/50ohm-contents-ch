Dans la classe E, nous avons déjà appris à connaître la capacité d’un condensateur ainsi que son comportement qualitatif en présence d’une tension alternative : un condensateur se comporte comme une résistance dépendant de la fréquence. Nous avons d’abord établi que la réactance capacitive est inversement proportionnelle à la fréquence. Si l’on diminue la fréquence, la réactance $X_C$ augmente. Si l’on augmente la fréquence, la réactance diminue en conséquence. Le comportement d’un condensateur en tension alternative peut être décrit par la formule de la réactance capacitive $X_C$ :

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

Dans la classe A, nous allons examiner ce comportement plus en détail et découvrir pourquoi cette résistance est appelée « réactance ». Avant cela, il est important de retenir que la réactance d’un condensateur est également négative pour pouvoir répondre à la question suivante :

[question:AC102]

<indepth>
Pourquoi la réactance capacitive est-elle négative ? La réponse réside dans le calcul complexe des courants alternatifs, qui n’est pas obligatoire pour l’examen d’opérateur radioamateur.

Pour les lecteurs familiarisés avec les nombres complexes, il convient de noter que la représentation correcte de la réactance capacitive est en réalité

$X_C = \frac{1}{j\omega C}$

où $j$ représente l’unité imaginaire $\sqrt{-1}$.

En multipliant cette expression par $j$, on obtient :

$X_C = \frac{1}{j\omega C} = \frac{1 \cdot j}{j\omega C \cdot j} = \frac{-j}{\omega C}$

Il apparaît ainsi que la réactance capacitive n’est pas seulement négative, mais aussi complexe. Le signe négatif décrit le déphasage entre le courant et la tension aux bornes du condensateur, que nous examinerons plus en détail dans ce chapitre.
</indepth>

---

Les analyseurs d’antenne ou les analyseurs de réseau vectoriels (VNA), instruments modernes et économiques souvent utilisés par les radioamateurs, mesurent la variation de la réactance $X_C$ en fonction de la fréquence et peuvent représenter graphiquement le résultat de la mesure.

La figure [ref:a_kapazitiver_Blindwiderstand] montre la variation de la réactance capacitive (courbe bleue) d’un condensateur Styroflex de $\qty{1500}{\pico\farad}$ dans la bande de fréquences de $\qtyrange{1}{4,5}{\mega\hertz}$.

<margin>
[photo:248:a_kapazitiver_Blindwiderstand:Réactance capacitive $X_C$ (courbe bleue) et déphasage (courbe rouge) d’un condensateur Styroflex de $\qty{1500}{\pico\farad}$ dans la bande de fréquences de $\qtyrange{1}{4,5}{\mega\hertz}$.]
</margin>


Essayez maintenant de répondre aux questions suivantes à l’aide de la formule ci-dessus. Veillez particulièrement aux unités et aux puissances de dix afin d’obtenir les bons résultats.

[question:AC104]
[question:AC105]
[question:AC106]
[question:AC107]

Dans la question suivante, c’est la capacité qui est recherchée. Essayez de réarranger la formule pour calculer la capacité $C$ :

[question:AC108]

---

Si l’on effectue simultanément une mesure de courant et de tension aux bornes d’un condensateur à l’aide d’un oscilloscope à deux voies (cf. [ref:a_strom_eilt_vor]), on observe un résultat surprenant : il existe un déphasage de $\qty{90}{\degree}$ entre le courant et la tension, le courant précédant la tension.

Cela signifie que le courant atteint déjà sa valeur maximale tandis que la tension est encore en train d’augmenter. Ce comportement caractéristique est une propriété fondamentale des condensateurs et joue un rôle important dans la technique des courants alternatifs, notamment dans les filtres et les circuits résonants.
La courbe rouge dans la figure [ref:a_kapazitiver_Blindwiderstand] représente le déphasage de la réactance capacitive, qui est presque constant à $\qty{-90}{\degree}$.

[question:AC101]

<margin>
[photo:268:a_strom_eilt_vor:Déphasage aux bornes d’un condensateur entre tension et courant]
</margin>

<tip>
Astuce : Pour un condensat*eur*, le courant est en av*ance* !
</tip>

---

Le déphasage entre la tension et le courant est donc de $\qty{90}{\degree}$, le courant (rouge) précédant la tension (bleue), comme le montre la figure [ref:a_blindleistung_kondensator]. Si l’on considère la puissance instantanée avec $P = U \cdot I$, on obtient une courbe de puissance (verte) qui oscille symétriquement autour de la ligne zéro, également représentée dans la figure [ref:a_blindleistung_kondensator].

<margin>
[picture:943:a_blindleistung_kondensator:Le produit $U \cdot I$ donne la courbe de puissance verte]
</margin>

La valeur moyenne de cette puissance est nulle, ce qui signifie qu’aucune puissance active n’est dissipée. À la place, l’énergie est stockée périodiquement dans le champ électrique du condensateur puis restituée à la source. On parle donc, pour un condensateur idéal sans pertes, de puissance réactive et de réactance.

Seule une résistance ohmique dissipe de la puissance active, car la tension et le courant y sont en phase, c’est-à-dire qu’il n’y a pas de déphasage. Cela signifie que la tension et le courant sont simultanément positifs ou négatifs, de sorte que la puissance instantanée $P = U \cdot I$ est toujours positive.

Une réactance idéale, en revanche, ne dissipe aucune puissance active et ne chauffe donc pas en théorie. À la place, l’énergie est stockée périodiquement puis restituée à la source.

[question:AC111]

[question:AC103]

---

Si un condensateur chauffe dans des applications à haute fréquence, cela indique la présence de pertes dans le composant. Un condensateur idéal ne convertirait pas d’énergie en chaleur, mais les condensateurs réels possèdent des propriétés parasites qui entraînent des pertes.

Ces pertes peuvent être représentées dans le schéma équivalent : la résistance $R_\text{ESR}$ (Equivalent Series Resistance) décrit les pertes ohmiques dans le condensateur, tandis que $R_\text{Isolator}$ modélise les pertes dans le diélectrique / matériau isolant. De plus, l’inductance parasite $L_\text{ESL}$ influence le comportement aux fréquences élevées.

Pour évaluer techniquement ces pertes, on utilise le facteur de qualité $Q$ ainsi que le facteur de dissipation $\tan\delta$. Ces deux grandeurs décrivent dans quelle mesure un condensateur réel s’écarte du comportement idéal.

Il existe un lien direct entre ces deux grandeurs :

$Q = \frac{1}{\tan\delta}$

À retenir : des pertes élevées entraînent un faible facteur de qualité $Q$ et donc un facteur de dissipation $\tan\delta$ élevé. Plus la fréquence est élevée, plus ces pertes se manifestent, car la réactance $X_C$ diminue avec l’augmentation de la fréquence, tandis que les résistances parasites restent constantes.

<margin>
[picture:1065:a_ersatzchaltbild_kondensator:Schéma équivalent d’un condensateur réel avec pertes parasites.]
</margin>

---

[question:AC109]

[question:AC110]

<indepth>
Grâce au calcul complexe des courants alternatifs, on peut représenter la réactance $X_C$ avec les pertes parasites $R$ sous la forme d’un diagramme de Fresnel :
[picture:1066:a_tan_delta:$\tan\delta$ dans le diagramme de Fresnel complexe]

La tangente décrit en effet le rapport entre le côté opposé et le côté adjacent, c’est-à-dire dans ce cas les pertes $R$ par rapport à la réactance capacitive sans pertes $|X_C|$.

$\tan\delta = \frac{R}{|X_C|}$

Plus les pertes sont importantes, plus l’angle $\delta$ est grand et donc plus le facteur de dissipation $\tan\delta$ est élevé. Un condensateur idéal aurait un angle $\delta = 0$ degré, car il ne présente aucune perte.

Grâce à cette addition complexe ou géométrique, on obtient la grandeur $Z$. Elle est appelée *impédance* et décrit la résistance totale complexe d’un composant. La valeur absolue de l’impédance $|Z|$ correspond à ce qu’on appelle la *résistance apparente*.
</indepth>