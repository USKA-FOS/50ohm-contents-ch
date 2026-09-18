Dans la classe E, nous avons déjà abordé le sujet de la bobine. En courant continu, une bobine en régime établi présente une très faible résistance. Elle se comporte alors comme un simple morceau de fil. En courant alternatif, en revanche, la bobine, tout comme un condensateur, présente une impédance $X_{\textrm{L}}$, c'est-à-dire qu'elle oppose une résistance au passage du courant, qui augmente avec la fréquence de la tension alternative :


$|X_{L}| = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$


Cette formule montre que l'impédance augmente avec la fréquence et diminue lorsque celle-ci diminue. Contrairement au condensateur, l'impédance d'une bobine est positive.


<indepth>
Pourquoi la réactance inductive est-elle positive ? Cela s'explique à nouveau par le calcul complexe des courants alternatifs, qui n'est pas obligatoire pour l'examen amateur radio.


Pour les lectrices et lecteurs familiarisés avec les nombres complexes, il est à noter que la représentation correcte de la réactance inductive est en réalité


$X_L = j\omega L$


Ici, $j$ représente l'unité imaginaire $\sqrt{-1}$.


On voit ainsi que la réactance inductive n'est pas seulement positive, mais aussi complexe. Le signe positif décrit la relation de phase entre le courant et la tension aux bornes de la bobine, que nous examinerons plus en détail dans ce chapitre.
</indepth>


[question:AC202]


[question:AC203]


---


Avec un analyseur de réseau vectoriel (VNA), il est possible de représenter la variation de la réactance inductive $X_L$ en fonction de la fréquence (voir figure [ref:a_XL_Verlauf]).


<margin>
[photo:265:a_XL_Verlauf:Variation de la réactance inductive $X_L$ d'une bobine de $\qty{500}{\kilo\hertz}$ à $\qty{10}{\mega\hertz}$]
</margin>


Essayez maintenant de répondre à la question suivante à l'aide de la formule ci-dessus. Veillez particulièrement à respecter les unités et les puissances de dix afin d'obtenir les bons résultats.


[question:AC204]


---


Tout comme le condensateur, la bobine provoque un déphasage entre la tension et le courant. Celui-ci s'élève à $\qty{+90}{\degree}$, le courant étant en retard sur la tension, comme illustré dans la figure [ref:a_Blindleistung_Spule]. La ligne rouge dans la figure [ref:a_XL_Verlauf] montre la phase de la réactance inductive $X_L$ à environ $\qty{+90}{\degree}$.


<tip>
Astuce : Avec l'inducti*vité*, le courant arrive en retard !
</tip>


[question:AC201]


Il en résulte une courbe de puissance qui oscille symétriquement autour de la ligne zéro. La valeur moyenne de cette puissance est nulle, c'est-à-dire qu'aucune puissance active n'est absorbée, tout comme pour le condensateur. À la place, l'énergie est stockée périodiquement dans le champ magnétique de la bobine puis restituée à la source.


On parle donc, pour une bobine idéale sans pertes, de puissance réactive et de réactance.


<margin>
[picture:944:a_Blindleistung_Spule:Le produit de $U \cdot I$ donne la courbe de puissance en vert]
</margin>

Si une bobine chauffe en haute fréquence, cela indique qu'elle présente des pertes responsables de cet échauffement. Ces pertes sont causées par la résistance ohmique du fil et, en plus, par l'effet de peau qui réduit apparemment la section du fil. Comme pour le condensateur, on utilise le facteur de qualité $Q$ ou le facteur de dissipation $\tan\delta$ pour décrire ces pertes.


[question:AC209]


---


Nous avons maintenant découvert la réactance capacitive $X_C$ du condensateur et la réactance inductive $X_L$ de la bobine. Ces deux grandeurs dépendent de la fréquence et, associées à la résistance active $R$, forment ce qu'on appelle l'*impédance* $Z$ d'un composant.


Les réactances $X_L$ et $X_C$ agissent en sens opposé et peuvent se compenser partiellement ou totalement. Cependant, leur combinaison avec la résistance active ne peut pas être calculée par une simple addition algébrique, mais nécessite une addition géométrique. Celle-ci s'effectue à l'aide du théorème de Pythagore (voir figure [ref:a_impedanzdreieck]).


Le résultat est l'impédance $Z$, qui décrit la résistance totale complexe d'un composant. La valeur absolue de l'impédance $|Z|$ correspond à ce qu'on appelle la résistance apparente :


$Z = \sqrt{R^2 + (X_L - X_C)^2}$ 


ou, de manière simplifiée (voir recueil de formules – mot-clé : résistance apparente) :


$Z = \sqrt{R^2 + X^2}$ 


En haute fréquence, l'impédance joue un rôle central, car elle détermine le comportement des composants dans les circuits et est essentielle notamment pour l'adaptation des lignes, des antennes et des amplificateurs. Elle s'exprime en ohms ($\unit{\ohm}$) et décrit la résistance totale d'un composant en courant alternatif. Dans un circuit en série associant réactance et résistance active, il en résulte une résistance apparente $Z$ qui n'apparaît qu'en fonctionnement sous tension alternative et ne peut pas être mesurée avec un ohmmètre.


<margin>
[picture:1067:a_impedanzdreieck:Impédance $Z$ comme addition géométrique de $R$ et $X$]
</margin>

<indepth>
L'impédance $Z$ est une grandeur complexe qui prend en compte à la fois la résistance active $R$ et les réactances $X_L$ et $X_C$ ($Z = R + j\cdot X$).
</indepth>


[question:AA101]


<tip>
Une résistance active de $\qty{100}{\ohm}$ et une réactance de $\qty{100}{\ohm}$ en série donnent une résistance apparente (impédance) de $\qty{141}{\ohm}$.
Le résultat s'obtient par addition géométrique des deux résistances au moyen d'un triangle rectangle selon le théorème de Pythagore $a^2 + b^2 = c^2$.
Pour les résistances, cela signifie : $R^2 + X_L^2 = Z^2$
$Z = \sqrt{(\qty{100}{\ohm})^2 + (\qty{100}{\ohm})^2} = \qty{141}{\ohm}$
</tip>


---


Nous avons déjà abordé l'inductance d'une bobine dans la classe E. Fondamentalement, l'inductance augmente lorsque le nombre de spires est augmenté, que la longueur de la bobine est réduite, que la surface de la section transversale de la bobine est agrandie et qu'un matériau à plus grande perméabilité magnétique est utilisé comme noyau. Pour augmenter l'inductance sans augmenter de manière drastique le nombre de spires, l'enroulement est réalisé sur un noyau toroïdal en ferrite. Les bobines de choc à haute inductance sont utilisées pour réduire les courants haute fréquence.


<indepth>
[photo:270:a_Pulvereisenringkern:Exemple de noyau toroïdal en poudre de fer]
[photo:271:a_Ferritringkern:Exemple de noyau toroïdal en ferrite]
</indepth>

[question:AC211]


Pour les bobines toroïdales, on indique une valeur $A_\text{L}$ du matériau du noyau pour faciliter le calcul de l'inductance. Le calcul de l'inductance est alors :
$L = N^2 \cdot A_\text{L}$ (voir recueil de formules – mot-clé : Inductance d'une bobine toroïdale). Essayez maintenant de répondre aux questions suivantes avec cette formule.


<attention>
La désignation de la valeur $A_\text{L}$ est indiquée en nanohenry par spire au carré.
</attention>


[question:AC205]

[question:AC206]
[question:AC207]
[question:AC208]


<indepth>
Si un matériau à haute perméabilité magnétique se trouve à l'intérieur de la bobine (par exemple du fer, de la ferrite), le champ magnétique est amplifié. La densité de flux magnétique $B$ alors effective peut être calculée à l'aide de la formule (voir recueil de formules – mot-clé : Densité de flux magnétique)
$B = \mu_0 \cdot \mu_r \cdot H$
où $\mu_0$ correspond à la perméabilité du vide $\qty{1,2566e-6}{\volt\second\per\ampere\meter}$ et $\mu_r$ représente la perméabilité relative du matériau du noyau dans la bobine. Pour l'air, on utilise le facteur $1$ (voir recueil de formules – mot-clé : Perméabilité du vide ; Perméabilité relative).
</indepth>

Pour le blindage d'un champ magnétique, il faut un matériau à bonne conductivité magnétique, par exemple de la tôle blanche. La figure [ref:a_abschirmbecher] montre un exemple de bobines avec un godet de blindage. Les godets de blindage métalliques contiennent des bobines avec un noyau de ferrite réglable, qui peut être vissé ou dévissé par l'ouverture supérieure à l'aide d'un tournevis. Cela modifie l'inductance de la bobine.


[question:AC210]


<margin>
[photo:333:a_abschirmbecher:Exemple de bobines avec godet de blindage pour le blindage de champs magnétiques]
</margin>