Dans la section [sec:spule_1], nous avons déjà abordé la bobine. En courant continu, la bobine présente, une fois le régime établi, une très faible résistance. Elle se comporte alors comme un simple fil. Cependant, en courant alternatif, la bobine, à l'instar d'un condensateur, présente une impédance $X_{\textrm{L}}$, ce qui signifie que, bien que le fil de la bobine n'ait qu'une très faible résistance ohmique (résistance du conducteur), un courant circule, mais celui-ci diminue avec l'augmentation de la fréquence de la tension alternative :

$|X_{L}| = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$

De cette formule, on peut voir que l'impédance augmente avec la fréquence et diminue avec la baisse de la fréquence. Contrairement au condensateur, l'impédance d'une bobine est positive.

<indepth>
Pourquoi la réactance inductive est-elle positive ? La raison se trouve à nouveau dans le calcul complexe en courant alternatif, qui n'est pas strictement nécessaire pour l'examen de radioamateur.

Pour les lecteurs et lectrices ayant des connaissances en nombres complexes, notons cependant que la représentation correcte de la réactance inductive est en réalité

$X_L = j\omega L$

où $j$ représente à nouveau l'unité imaginaire $\sqrt{-1}$.

On voit ainsi que la réactance inductive n'est pas seulement positive, mais aussi complexe. Le signe positif décrit ici le déphasage entre le courant et la tension aux bornes de la bobine, que nous examinerons de plus près dans ce chapitre.
</indepth>

[question:AC202]

[question:AC203]

---

Avec un analyseur de réseau vectoriel (VNA), on peut représenter la variation de la réactance inductive $X_L$ en fonction de la fréquence (cf. figure [ref:a_XL_Verlauf]).

<margin>
[photo:265:a_XL_Verlauf:Variation de la réactance inductive $X_L$ d'une bobine de $\qty{500}{\kilo\hertz}$ à $\qty{10}{\mega\hertz}$]
</margin>

Essayez maintenant de répondre à la question suivante à l'aide de la formule ci-dessus. Portez une attention particulière aux unités et aux puissances de dix pour obtenir les bons résultats.

[question:AC204]

---

Comme pour le condensateur, un déphasage apparaît également entre la tension et le courant dans une bobine. Celui-ci est de $\qty{+90}{\degree}$, le courant étant en retard sur la tension, comme illustré dans la figure [ref:a_Blindleistung_Spule]. La ligne rouge dans la figure [ref:a_XL_Verlauf] montre la phase de la réactance inductive $X_L$ à environ $\qty{+90}{\degree}$.

<tip>
Moyen mnémotechnique : Avec l'inductivité, le courant arrive en ret*aaa*rd !
</tip>

[question:AC201]

Il en résulte une courbe de puissance qui oscille symétriquement autour de la ligne zéro. La valeur moyenne de cette puissance est nulle, ce qui signifie qu'aucune puissance active n'est consommée – exactement comme pour un condensateur. Au lieu de cela, l'énergie est périodiquement stockée dans le champ magnétique de la bobine et restituée à la source.

On parle donc, pour une bobine idéale sans pertes, de puissance réactive et de réactance.

<margin>
[picture:944:a_Blindleistung_Spule:Le produit de $U \cdot I$ donne la courbe de puissance verte]
</margin>

Si une bobine chauffe dans des applications haute fréquence, c'est qu'elle présente des pertes qui provoquent cet échauffement. Les pertes proviennent de la résistance ohmique du fil et, de plus, l'effet de peau agit également, réduisant apparemment la section du fil. Ici aussi, comme pour le condensateur, le facteur de qualité $Q$ ou le facteur de pertes $\tan\delta$ est utilisé pour décrire les pertes.

[question:AC209]

---

Nous avons maintenant appris la réactance capacitive $X_C$ du condensateur et la réactance inductive $X_L$ de la bobine. Ces deux grandeurs dépendent de la fréquence et, avec la résistance ohmique $R$, forment l'*impédance* $Z$ d'un composant.

Les réactances $X_L$ et $X_C$ agissent de manière opposée et peuvent partiellement ou totalement se compenser mutuellement. Cependant, pour combiner les réactances avec la résistance ohmique, une simple addition algébrique n'est pas possible ; une addition géométrique est nécessaire. Celle-ci s'effectue à l'aide du théorème de Pythagore (cf. figure [ref:a_impedanzdreieck]).

Le résultat est l'impédance $Z$, qui décrit la résistance totale complexe d'un composant. La valeur absolue de l'impédance $|Z|$ correspond à la résistance apparente :

$Z = \sqrt{R^2 + (X_L - X_C)^2}$

ou simplifié (cf. recueil de formules – mot-clé : résistance apparente) :

$Z = \sqrt{R^2 + X^2}$

En technique haute fréquence, l'impédance joue un rôle central, car elle détermine le comportement des composants dans les circuits et est particulièrement cruciale pour l'adaptation des lignes, des antennes et des amplificateurs. Elle est exprimée en ohms ($\unit{\ohm}$) et décrit la résistance totale d'un composant en régime alternatif. Pour un montage en série d'une réactance et d'une résistance active, on obtient une résistance apparente $Z$, qui n'apparaît qu'en fonctionnement sous tension alternative et ne peut pas être mesurée avec un ohmmètre.

<margin>
[picture:1067:a_impedanzdreieck:Impédance $Z$ comme addition géométrique de $R$ et $X$]
</margin>

<indepth>
L'impédance $Z$ est une grandeur complexe qui prend en compte à la fois la résistance ohmique $R$ et les réactances $X_L$ et $X_C$ ($Z = R + j\cdot X$).
</indepth>

[question:AA101]

<tip>
Une résistance active de $\qty{100}{\ohm}$ et une réactance de $\qty{100}{\ohm}$ en série donnent une résistance apparente (impédance) de $\qty{141}{\ohm}$.
Le résultat est obtenu par addition géométrique des deux résistances via un triangle rectangle selon le théorème de Pythagore $a^2 + b^2 = c^2$.
Pour les résistances, cela signifie : $R^2 + X_L^2 = Z^2$
$Z = \sqrt{(\qty{100}{\ohm})^2 + (\qty{100}{\ohm})^2} = \qty{141}{\ohm}$
</tip>

---

Nous avons également déjà abordé l'inductance d'une bobine dans la classe E. Fondamentalement, l'inductance augmente lorsque le nombre de spires est augmenté, la longueur de la bobine est réduite, la section transversale de la bobine est agrandie et un matériau à plus grande perméabilité magnétique est utilisé comme noyau. Pour augmenter l'inductance sans augmenter drastiquement le nombre de spires, l'enroulement est réalisé sur un noyau toroïdal en ferrite. Les bobines d'arrêt à haute inductance sont utilisées pour réduire les courants haute fréquence.

<indepth>
[photo:270:a_Pulvereisenringkern:Exemple d'un noyau toroïdal en poudre de fer]
[photo:271:a_Ferritringkern:Exemple d'un noyau en ferrite]
</indepth>

[question:AC211]

Pour les bobines à noyau toroïdal, une valeur dite $A_\text{L}$ du matériau du noyau est indiquée pour faciliter le calcul de l'inductance.
Le calcul de l'inductance est alors :
$L = N^2 \cdot A_\text{L}$ (voir recueil de formules - mot-clé : inductance d'une bobine toroïdale). Essayez maintenant de répondre aux questions suivantes avec cela.

<attention>
La désignation de la valeur $A_\text{L}$ est donnée en nanohenry par tour au carré.
</attention>

[question:AC205]
[question:AC206]
[question:AC207]
[question:AC208]

<indepth>
Si un matériau à perméabilité magnétique se trouve à l'intérieur de la bobine (par exemple du fer, de la ferrite), alors le champ magnétique est amplifié. La densité de flux magnétique effective $B$ peut alors être calculée avec la formule (voir recueil de formules - mot-clé : densité de flux magnétique)
$B = \mu_0 \cdot \mu_r \cdot H$
Ici, $\mu_0$ correspond à la perméabilité du vide $\qty{1,2566e-6}{\volt\second\per\ampere\meter}$ et $\mu_r$ représente la perméabilité relative du matériau du noyau dans la bobine. Pour l'air, le facteur $1$ est utilisé (voir recueil de formules - mot-clé : perméabilité du vide ; perméabilité relative).
</indepth>

Pour protéger un champ magnétique, on a besoin d'un matériau à bonne conductivité magnétique, par exemple de la tôle étamée. La figure [ref:a_abschirmbecher] montre un exemple de bobines avec écran de protection. Les écrans métalliques contiennent des bobines avec un noyau en ferrite réglable, qui peut être vissé ou dévissé par l'ouverture du dessus à l'aide d'un tournevis. Cela modifie l'inductance de la bobine.

[question:AC210]

<margin>
[photo:333:a_abschirmbecher:Exemple de bobines avec écran de protection pour la protection contre les champs magnétiques]
</margin>