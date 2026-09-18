Le phénomène physique qui rend les signaux radio possibles est le champ électromagnétique. Le fait que ce champ puisse se propager dans le vide, sans support matériel, fut l'une des découvertes les plus importantes du XIXe siècle.

<margin>
Longtemps, la physique a cru à l'existence d'un « éther », présent partout et dans lequel les ondes électromagnétiques se propageraient comme le son dans l'air. Cette idée était erronée, mais le terme est resté dans le langage courant, par exemple lorsque nous disons que nous sommes assis devant le récepteur et que nous *écoutons l'éther*.
</margin>

---

Comme son nom l'indique, le champ électromagnétique est composé de deux éléments : le champ électrique et le champ magnétique. Lorsque le champ électrique et le champ magnétique varient dans le temps, les deux composantes du champ apparaissent toujours ensemble.

Commençons par le champ électrique invariable dans le temps, aussi appelé champ statique. Le champ électrique est généralement désigné par la lettre $E$.

<margin>
[picture:881:e_plattenkondensator: Condensateur à plaques sous tension avec champ électrique homogène]
</margin>

---

La figure [ref:e_plattenkondensator] montre schématiquement un *condensateur à plaques* aux bornes duquel une tension $U$ est appliquée. Les plaques sont isolées l'une de l'autre, aucun courant ne circule. La tension entraîne l'accumulation de porteurs de charge positifs sur la plaque de gauche et négatifs sur celle de droite. Un champ électrique statique $E$ s'établit entre les deux plaques. Si l'on suppose que l'étendue des plaques en longueur et en largeur est bien plus grande que leur distance, l'intensité du champ est indépendante de la position — on parle alors de champ *homogène*. L'intensité du champ électrique peut alors être calculée simplement par :

$E = \frac{U}{d}$

où $d$ est la distance entre les plaques.

<unit>
D'après l'équation $E = \frac{U}{d}$, l'unité de l'intensité du champ électrique est : $\unit{\volt\per\meter}$
</unit>

[question:EB101]
[question:EA103]

---

Pour calculer l'intensité du champ électrique dans un condensateur à plaques, il faut connaître la tension appliquée et la distance entre les plaques. Les condensateurs à plaques sont souvent utilisés dans les boîtiers d'adaptation d'antenne.

<danger>
Dans ces questions, il est impératif de respecter la bonne unité !
</danger>

[question:EB102]

Ici, on peut à nouveau calculer simplement avec la formule ci-dessus :

$E = \frac{\qty{9}{\volt}}{\qty{0,6}{\centi\meter}} = \frac{\qty{9}{\volt}}{\qty{0,006}{\meter}} = \qty{1500}{\volt\per\meter}$

Un *condensateur enroulé* peut être imaginé comme un condensateur à plaques dont les plaques, très larges, ont été enroulées. Entre les plaques se trouve cependant une couche isolante, le *diélectrique*. Celui-ci augmente la *capacité* du condensateur — sa capacité à stocker des charges. Il n'a cependant aucune influence sur le calcul de l'intensité du champ à l'intérieur.

[question:EB103]

Pour cette question, utilisons à nouveau notre formule :

$E = \frac{\qty{300}{\volt}}{\qty{0,15}{\milli\meter}} = \frac{\qty{300}{\volt}}{\qty{0,00015}{\meter}} = \qty{2000000}{\volt\per\meter} = \qty{2000}{\kilo\volt\per\meter}$

Les diélectriques ne peuvent supporter qu'une intensité de champ électrique limitée avant de perdre leur capacité d'isolation. La valeur limite de l'intensité de champ à laquelle cela se produit est appelée *intensité de claquage*. Si l'on connaît l'intensité de claquage et l'épaisseur du diélectrique, on peut calculer la tension maximale que le condensateur peut supporter.

Si l'intensité de claquage est $E_d$ et l'épaisseur du diélectrique $d$, alors la tension de claquage est :

$U_d =E_d \cdot d$

[question:EB104]

Ici, nous calculons avec la formule ci-dessus (attention aux unités !) :

$\begin{split} U_d &= \qty{400}{\kilo\volt\per\centi\meter} \cdot \qty{0,15}{\milli\meter} \\ &= \qty{40000000}{\volt\per\meter} \cdot \qty{0,00015}{m} \\ &= \qty{6000}{\volt} \\ &= \qty{6}{\kilo\volt} \end{split}$

---

Une autre compétence importante consiste à distinguer, dans des croquis, les lignes de champ électrique des lignes de champ magnétique, qui seront traitées plus tard.

Une règle simple permet de le faire facilement : les lignes de champ électrique ont un début et une fin, ce qui n'est pas le cas des lignes de champ magnétique ! La direction du champ électrique va toujours du potentiel le plus positif vers le potentiel le plus négatif.

[question:EB105]

<margin>
[picture:884:e_feldlinien_vertikalantenne: Lignes de champ sur une antenne verticale]
</margin>