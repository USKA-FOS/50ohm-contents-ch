Déjà dans le chapitre [sec:wellenlaenge], nous avons appris la relation entre la fréquence ($f$) et la longueur d’onde ($\lambda$). Deux équations aux grandeurs spécifiquement ajustées y étaient données.
% Insérer cette subordonnée dans la phrase précédente si les formules sont dans le recueil. "... du recueil de formules pour l'examen..."

$f[\unit{\mega\hertz}] = \dfrac{300}{\lambda[\unit{\meter}]}$

$\lambda[\unit{\meter}] = \dfrac{300}{f[\unit{\mega\hertz}]}$

<indepth>
Les équations qui indiquent déjà dans quelle unité les valeurs doivent être exprimées sont appelées *équations aux grandeurs ajustées*.
</indepth>

En réalité, ce n'est qu'une seule équation, qui a été, dans le premier cas, résolue pour la fréquence et dans le second cas pour la longueur d’onde.

Dans les calculs techniques, nous devons constamment réarranger des équations de manière à ce que la grandeur recherchée se trouve seule d'un côté. Pour cela, nous appliquons les opérations mathématiques nécessaires (multiplication, division, addition, soustraction, ...) aux deux côtés de l'équation *simultanément*. Avec un peu de pratique, c'est beaucoup plus simple que de mémoriser séparément toutes les formes nécessaires d'une relation. Dans le recueil de formules, les équations simples ne sont données que sous leur forme de base. Le réarrangement de formules simples fait partie de la matière d'examen.

---

<indepth>
En unités de base ($\unit{\second}$, $\unit{\meter}$), la relation entre la longueur d’onde et la fréquence dans l'espace libre est :

$\lambda = \dfrac{c_0}{f}$

Ici, $c_0$ est la vitesse de propagation des ondes électromagnétiques dans le vide ("vitesse de la lumière"), $c_o \approx \qty{300000000}{\meter\per\second}$
</indepth>

Nous considérons ici la relation entre la fréquence et la longueur d’onde sous sa forme plus abstraite :

$\lambda = \dfrac{c_0}{f}$

Nous voulons maintenant déterminer la fréquence qui correspond à une longueur d’onde de 2,069 m.

Pour y parvenir, nous multiplions d'abord les deux côtés de l'équation par la fréquence.

$\lambda = \dfrac{c_0}{f} \quad\quad\quad | \cdot f$

Ceci est illustré par "$|~\cdot f$", où la barre verticale signifie que l'opération suivante est effectuée des deux côtés.

Il en résulte une nouvelle équation :

$\lambda\cdot f = \dfrac{c_0 \cdot f}{f}$

où la fréquence se simplifie à droite (car $f$ divisé par $f$ donne 1) :

$\lambda \cdot f = c_0$

Maintenant, la fréquence est déjà du côté gauche de l'équation, où nous la voulons. Ensuite, nous divisons les deux côtés par la longueur d’onde :

$\lambda \cdot f = c_0 \quad\quad\quad |: \lambda$

Ainsi, nous obtenons :

$\frac{\lambda\cdot f}{\lambda} = \frac{c_0}{\lambda}$

À gauche, le lambda se simplifie à nouveau :

$f = \dfrac{c_0}{\lambda}$

C'est la relation recherchée. Nous substituons les valeurs numériques :

$f = \dfrac{\qty{300000000}{\meter\per\second}}{\qty{2,069}{\meter}} = \dfrac{\num{300000000}}{\qty{2,069}{\second}}  = \qty{144997583}{\hertz} \approx \qty{145}{\mega\hertz} $

Nous avons tenu compte du fait que $\frac{1}{\unit{\second}} = \qty{1}{\hertz}$.

Nous pouvons maintenant réarranger des formules à l'aide de la multiplication et de la division. Plus tard, nous rencontrerons d'autres formules nécessitant également l'addition et la soustraction, les puissances et les racines. Dans les chapitres [sec:dezibel_1] et [sec:dezibel_2], des logarithmes s'ajouteront même. Pas de panique, à chaque endroit, nous expliquerons précisément comment ces formules sont réarrangées étape par étape.
