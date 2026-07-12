Dans la classe E, nous avons également étudié la bobine. En courant continu, la bobine a une très faible résistance à l'état stabilisé. La bobine agit alors comme un morceau de fil. Cependant, en courant alternatif, la bobine, comme un condensateur, présente une résistance au courant alternatif $X_{\textrm{L}}$, c'est-à-dire que bien que le fil de la bobine possède une très faible résistance ohmique (résistance du conducteur), un courant circule, mais qui diminue avec l'augmentation de la fréquence de la tension alternative:

$|X_{L}| = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$

La formule montre que la résistance au courant alternatif augmente avec la fréquence et diminue avec la diminution de la fréquence. Contrairement au condensateur, la résistance au courant alternatif d'une bobine est positive. 

<indepth>
Pourquoi la résistance inductive est-elle positive ? L'explication réside à nouveau dans le calcul complexe du courant alternatif, qui n'est pas indispensable pour l'examen de radioamateur.

Pour les lecteurs et lectrices ayant des connaissances en nombres complexes, notons cependant que la représentation correcte de la résistance inductive est en réalité

$X_L = j\omega L$

où $j$ représente à nouveau l'unité imaginaire $\sqrt{-1}$.

Il en résulte que la résistance inductive n'est pas seulement positive, mais aussi complexe. Le signe positif décrit la relation de phase entre le courant et la tension à la bobine que nous examinerons plus en détail dans ce chapitre.
</indepth>

[question:AC202]

[question:AC203]

---

Avec un analyseur de réseau vectoriel (VNA), on peut représenter la variation de la résistance inductive $X_L$ en fonction de la fréquence (voir figure [ref:a_XL_Verlauf]). 

<margin>
[photo:265:a_XL_Verlauf:Variation de la résistance inductive $X_L$ d'une bobine de $\qty{500}{\kilo\hertz}$ à $\qty{10}{\mega\hertz}$]
</margin>

Essaie maintenant de répondre à la question suivante en utilisant la formule ci-dessus. Fais particulièrement attention aux unités ou aux puissances de dix, afin d'obtenir les bons résultats.

[question:AC204]

---

Comme pour le condensateur, une bobine présente également un déphasage entre la tension et le courant. Celui-ci est de $\qty{+90}{\degree}$, le courant étant en retard par rapport à la tension, comme le montre la figure [ref:a_Blindleistung_Spule]. La ligne rouge dans la figure [ref:a_XL_Verlauf] montre la relation de phase de la résistance inductive $X_L$ à environ $\qty{+90}{\degree}$.

<tip>
Astuce : Avec l'inductance, le courant arrive en retard !
</tip>

[question:AC201]

Cela donne une courbe de puissance qui oscille symétriquement autour de la ligne nulle. La valeur moyenne de cette puissance est nulle, c'est-à-dire qu'aucune puissance active n'est absorbée, tout comme pour le condensateur. Au lieu de cela, l'énergie est stockée périodiquement dans le champ magnétique de la bobine et restituée à la source.

On parle donc, pour une bobine idéalement sans perte, de puissance réactive et de résistance réactive.

<margin>
[picture:944:a_Blindleistung_Spule:Le produit de $U \cdot I$ donne la courbe de puissance verte]
</margin>

Si une bobine s'échauffe lors d'applications à haute fréquence, elle présente des pertes qui provoquent cet échauffement. Les pertes sont dues à la résistance ohmique du fil et, en outre, l'effet de peau réduit apparemment la section transversale du fil. Comme pour le condensateur, la qualité $Q$ ou le facteur de perte $\tan\delta$ est utilisé pour décrire les pertes.

[question:AC209]

---

Nous avons maintenant fait connaissance avec la résistance capacitive $X_C$ du condensateur et la résistance inductive $X_L$ de la bobine. Ces deux grandeurs dépendent de la fréquence et, avec la résistance ohmique $R$, forment ce qu'on appelle l'*impédance* $Z$ d'un composant.

Les résistances réactives $X_L$ et $X_C$ agissent en sens opposé et peuvent s'annuler partiellement ou totalement. Cependant, pour le calcul des résistances réactives avec la résistance ohmique, une simple addition algébrique n'est pas possible, mais une addition géométrique est nécessaire. Celle-ci est réalisée à l'aide du théorème de Pythagore (voir figure [ref:a_impedanzdreieck]).

Le résultat est l'impédance $Z$, qui décrit la résistance totale complexe d'un composant. La valeur de l'impédance $|Z|$ correspond à la soi-disant résistance apparente:

$Z = \sqrt{R^2 + (X_L - X_C)^2}$ 

ou simplifiée (voir recueil de formules – mot-clé : résistance apparente):

$Z = \sqrt{R^2 + X^2}$ 

Dans la technique des hautes fréquences, l'impédance joue un rôle central, car elle détermine le comportement des composants dans les circuits et est particulièrement décisive pour l'adaptation des lignes, des antennes et des amplificateurs. Elle est indiquée en ohms ($\unit{\ohm}$) et décrit la résistance totale d'un composant en régime de courant alternatif. Dans un circuit série de résistance réactive et de résistance active, il en résulte une résistance apparente $Z$, qui n'apparaît qu'en fonctionnement sous tension alternative et ne peut pas être mesurée avec un ohmmètre. 

<margin>
[picture:1067:a_impedanzdreieck:Impédance $Z$ comme addition géométrique de $R$ et $X$]
</margin>

<indepth>
L'impédance $Z$ est une grandeur complexe qui prend en compte à la fois la résistance ohmique $R$ et les résistances réactives $X_L$ et $X_C$ ($Z = R + j\cdot X$).
</indepth>

[question:AA101]

<tip>
Résistance active $\qty{100}{\ohm}$ et résistance réactive $\qty{100}{\ohm}$ en série donnent une résistance apparente (impédance) de $\qty{141}{\ohm}$.
Le résultat est obtenu par addition géométrique des deux résistances sur un triangle rectangle selon le théorème de Pythagore $a^2 + b^2 = c^2$.
Pour les résistances, cela signifie : $R^2 + X_L^2 = Z^2$
$Z = \sqrt{(\qty{100}{\ohm})^2 + (\qty{100}{\ohm})^2} = \qty{141}{\ohm}$
</tip>


---

Nous avons également fait connaissance avec l'inductance d'une bobine dans la classe E. En général, l'inductance augmente lorsque le nombre de spires est augmenté, que la longueur de la bobine est réduite, que la section transversale de la bobine est agrandie et qu'un matériau plus magnétiquement conducteur est utilisé comme noyau de bobine. Pour augmenter l'inductance sans augmenter drastiquement le nombre de spires, l'enroulement est bobiné sur un noyau en anneau de ferrite. Les bobines d'arrêt à haute inductance sont utilisées pour réduire les courants à haute fréquence.

<indepth>
[photo:270:a_Pulvereisenringkern:Exemple d'un noyau en anneau de fer poudreux]
[photo:271:a_Ferritringkern:Exemple d'un noyau en ferrite]
</indepth>

[question:AC211]

Pour les bobines à noyau toroïdal, une valeur appelée $A_\text{L}$ du matériau du noyau est indiquée pour faciliter le calcul de l'inductance.
Le calcul de l'inductance est alors:
$L = N^2 \cdot A_\text{L}$ (voir recueil de formules - mot-clé : inductance d'une bobine à noyau toroïdal). Essaie maintenant de répondre aux questions suivantes.

<attention>
La désignation de la valeur $A_\text{L}$ est donnée en nanohenry par spire au carré.
</attention>


[question:AC205]
[question:AC206]
[question:AC207]
[question:AC208]

<indepth>
Si un matériau magnétiquement conducteur se trouve à l'intérieur de la bobine (par exemple, fer, ferrite), alors le champ magnétique est amplifié. La densité de flux magnétique $B$ alors effective peut être calculée avec la formule (voir recueil de formules - mot-clé : densité de flux magnétique)
$B = \mu_0 \cdot \mu_r \cdot H$
où $\mu_0$ correspond à la constante de champ magnétique $\qty{1,2566e-6}{\volt\second\per\ampere\meter}$ et $\mu_r$ représente la perméabilité relative du matériau du noyau dans la bobine. Pour l'air, le facteur $1$ est utilisé (voir recueil de formules - mot-clé : constante de champ magnétique ; perméabilité relative).
</indepth>

Pour protéger un champ magnétique, il faut un matériau magnétiquement bon conducteur, par exemple de la tôle blanche. La figure [ref:a_abschirmbecher] montre un exemple de bobines avec un boîtier de blindage. Les boîtiers de blindage métalliques contiennent des bobines avec un noyau de ferrite réglable, qui est vissé ou dévissé par le haut avec un tournevis à travers l'ouverture. Cela modifie l'inductance de la bobine.

[question:AC210]

<margin>
[photo:333:a_abschirmbecher:Exemple de bobines avec boîtier de blindage pour le blindage des champs magnétiques]
</margin>