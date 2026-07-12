Le phénomène physique qui rend les signaux radio possibles est le champ électromagnétique. Le fait que ce champ puisse se propager dans le vide, sans support, a été l'une des découvertes les plus importantes du 19e siècle.

<margin>
Pendant longtemps, la physique a cru à l'existence d'un "éther", présent partout et dans lequel les ondes électromagnétiques se propagent comme le son dans l'air. Cette idée était fausse, mais le terme s'est maintenu dans le langage courant, par exemple, nous sommes assis devant le récepteur et *écoutons l'éther*.
</margin>

---

Comme le suggère le nom, le champ électromagnétique est composé de deux composantes, le champ électrique et le champ magnétique. Lorsque le champ électrique et le champ magnétique changent dans le temps, les deux composantes de champ apparaissent toujours ensemble.

Commençons cependant par le champ électrique temporellement invariable, également appelé champ statique. Le champ électrique est généralement désigné par la lettre $E$.

<margin>
[picture:881:e_plattenkondensator: Un condensateur à plaques avec une tension appliquée et un champ électrique homogène]
</margin>
  
---

La figure [ref:e_plattenkondensator] montre schématiquement un *condensateur à plaques*, dans lequel une tension $U$ est appliquée aux plaques. Les plaques sont isolées l'une de l'autre, aucun courant ne circule. La tension entraîne l'accumulation de porteurs de charge positifs sur la plaque de gauche et de porteurs de charge négatifs sur la plaque de droite. Entre les deux plaques, un champ électrique statique $E$ se forme. Supposons que l'étendue des plaques en longueur et en largeur soit beaucoup plus grande que la distance, alors l'intensité du champ est indépendante de l'emplacement -- nous parlons d'un champ *homogène*. L'intensité du champ électrique peut alors être calculée très simplement:

$E = \frac{U}{d}$

où $d$ est la distance entre les plaques. 

<unit>
De l'équation $E = \frac{U}{d}$ découle également l'unité de l'intensité du champ électrique : $\unit{\volt\per\meter}$
</unit>

[question:EB101]
[question:EA103]

---

Pour calculer l'intensité du champ électrique dans un condensateur à plaques, nous devons connaître la tension appliquée et la distance entre les plaques. Les condensateurs à plaques sont souvent utilisés dans les appareils d'adaptation d'antennes. 

<danger>
Pour ces questions, il est impératif de respecter l'unité correcte!
</danger>

[question:EB102]

Ici, nous pouvons à nouveau calculer simplement avec la formule ci-dessus : 

$E = \frac{\qty{9}{\volt}}{\qty{0,6}{\centi\meter}} = \frac{\qty{9}{\volt}}{\qty{0,006}{\meter}} = \qty{1500}{\volt\per\meter}$

Un *condensateur bobiné* peut être imaginé comme un condensateur à plaques avec des plaques très larges qui ont été enroulées. Entre les plaques se trouve cependant une couche isolante, le *diélectrique*. Il augmente la *capacité* du condensateur -- la capacité à stocker des charges. Cependant, le diélectrique n'a aucune influence sur le calcul de l'intensité du champ à l'intérieur.

[question:EB103]

Pour cette question également, nous utilisons à nouveau notre formule : 

$E = \frac{\qty{300}{\volt}}{\qty{0,15}{\milli\meter}} = \frac{\qty{300}{\volt}}{\qty{0,00015}{\meter}} = \qty{2000000}{\volt\per\meter} = \qty{2000}{\kilo\volt\per\meter}$

Les diélectriques ne peuvent supporter qu'une intensité de champ électrique limitée avant de perdre leur capacité d'isolation. L'intensité de champ limite à laquelle cela se produit est également appelée *intensité de champ de claquage*. Si nous connaissons l'intensité de champ de claquage et l'épaisseur du diélectrique, nous pouvons calculer la tension que le condensateur peut supporter au maximum.

Si l'intensité de champ de claquage est $E_d$ et l'épaisseur du diélectrique *d*, alors la tension de claquage est:

$U_d =E_d \cdot d$

[question:EB104]

Ici, nous calculons avec la formule ci-dessus (attention aux unités!) :

$\begin{split} U_d &= \qty{400}{\kilo\volt\per\centi\meter} \cdot \qty{0,15}{\milli\meter} \\ &= \qty{40000000}{\volt\per\meter} \cdot \qty{0,00015}{m} \\ &= \qty{6000}{\volt} \\ &= \qty{6}{\kilo\volt} \end{split}$

---

Une autre capacité importante est de distinguer dans les schémas les lignes de champ électrique des lignes de champ magnétique traitées plus tard. 

Avec une règle simple, cela est assez facile : les lignes de champ électrique ont un début et une fin, pas les lignes de champ magnétique ! La direction du champ électrique va toujours du potentiel plus positif au potentiel moins positif. 

[question:EB105]

<margin>
[picture:884:e_feldlinien_vertikalantenne:Lignes de champ d'une antenne verticale]
</margin>




