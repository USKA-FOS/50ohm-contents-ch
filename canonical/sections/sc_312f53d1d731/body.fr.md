Nous avons déjà abordé dans le chapitre [sec:wellenlaenge] la relation entre la fréquence ($f$) et la longueur d’onde ($\lambda$). À l’époque, deux équations de grandeurs spécialement adaptées avaient été fournies à partir du recueil de formules pour l’examen.

$f[\unit{\mega\hertz}] = \dfrac{300}{\lambda[\unit{\meter}]}$

$\lambda[\unit{\meter}] = \dfrac{300}{f[\unit{\mega\hertz}]}$

<indepth>
Les équations où les unités dans lesquelles les valeurs doivent être exprimées sont déjà indiquées sont appelées *équations de grandeurs adaptées*.
</indepth>

En réalité, il ne s’agit que d’une seule et même équation, qui a été réarrangée une fois pour la fréquence et une autre fois pour la longueur d’onde.

Dans les calculs techniques, nous devons constamment réarranger des équations de manière à ce que la grandeur recherchée se trouve seule d’un côté. Pour cela, nous appliquons les opérations mathématiques nécessaires (multiplication, division, addition, soustraction, etc.) *simultanément* aux deux côtés de l’équation. Avec un peu d’entraînement, c’est bien plus simple que de mémoriser toutes les formes nécessaires d’une relation séparément. Dans la classe E et également dans la classe A, cela est même obligatoire, car les équations ne sont plus indiquées dans le recueil de formules que sous leur forme de base.

---

<indepth>
Exprimée en unités de base ($\unit{\second}$, $\unit{\meter}$), la relation entre la longueur d’onde et la fréquence dans l’**espace libre** est :

$\lambda = \dfrac{c_0}{f}$

Ici, $c_0$ représente la vitesse de propagation des ondes électromagnétiques dans le vide ("vitesse de la lumière"), avec $c_0 \approx \qty{300000000}{\meter\per\second}$.
</indepth>

Nous considérons ici la relation entre la fréquence et la longueur d’onde sous une forme plus abstraite :

$\lambda = \dfrac{c_0}{f}$

Nous voulons maintenant déterminer la fréquence correspondant à une longueur d’onde de 2,069 m.

Pour ce faire, nous multiplions d’abord les deux côtés de l’équation par la fréquence.

$\lambda = \dfrac{c_0}{f} \quad\quad\quad | \cdot f$

Cela est illustré par "$|~\cdot f$", où la barre verticale signifie que l’opération suivante est appliquée des deux côtés.

Nous obtenons ainsi une nouvelle équation :

$\lambda\cdot f = \dfrac{c_0 \cdot f}{f}$

où la fréquence s’annule du côté droit (car $f$ divisé par $f$ donne 1) :

$\lambda \cdot f = c_0$

La fréquence se trouve maintenant du côté gauche de l’équation, là où nous la voulons. Ensuite, nous divisons les deux côtés par la longueur d’onde :

$\lambda \cdot f = c_0 \quad\quad\quad |: \lambda$

Nous obtenons ainsi :

$\frac{\lambda\cdot f}{\lambda} = \frac{c_0}{\lambda}$

Du côté gauche, le lambda s’annule à nouveau :

$f = \dfrac{c_0}{\lambda}$

Voici la relation recherchée. Nous insérons les valeurs numériques :

$f = \dfrac{\qty{300000000}{\meter\per\second}}{\qty{2,069}{\meter}} = \dfrac{\num{300000000}}{\qty{2,069}{\second}}  = \qty{144997583}{\hertz} \approx \qty{145}{\mega\hertz} $

Nous avons tenu compte du fait que $\frac{1}{\unit{\second}} = \qty{1}{\hertz}$.

Nous pouvons maintenant réarranger des formules à l’aide de multiplications et de divisions. Plus tard, nous rencontrerons d’autres formules où des additions et soustractions, des puissances et des racines seront nécessaires. Dans les chapitres [sec:dezibel_1] et [sec:dezibel_2], nous aborderons même les logarithmes. Ne vous inquiétez pas, à chaque étape, nous expliquerons précisément comment réarranger ces formules pas à pas.