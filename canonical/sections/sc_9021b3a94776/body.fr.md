Nous avions déjà discuté du transistor bipolaire dans les documents de formation pour la classe E. Dans la classe A, nous approfondirons le sujet et examinerons également un autre transistor.

Le transistor bipolaire se compose de trois zones de semi-conducteurs qui sont dopées alternativement n et p. Les zones sont désignées comme émetteur, base et collecteur. Pour le *transistor npn*, l'émetteur est n, la base p et le collecteur n. Pour le transistor pnp, il s'agit d'un émetteur p, d'une base n et d'un collecteur p. 

La figure [ref:a_bipolartransistor_aus] montre un transistor npn à l'état éteint.
Dès que la tension base-émetteur $U_\mathrm{BE}$ est appliquée en fermant le commutateur (typiquement $\approx \qtyrange{0,6}{0,7}{\volt}$ pour le silicium), la diode base-émetteur devient conductrice. Un petit courant de base $I_\mathrm{B}$ circule alors (voir figure [ref:a_bipolartransistor_ein]).

Ce petit courant de base fait que de nombreux électrons sont introduits dans la base mince depuis l'émetteur. Comme la base est très étroite, la plupart de ces porteurs de charge parviennent jusqu'au collecteur. Là, ils sont "aspirés" par la tension collecteur-émetteur $U_\mathrm{CE}$ appliquée, le courant de collecteur $I_\mathrm{C}$ circule. Il est plus grand que le courant de base d'un facteur $B$, où $B$ est la soi-disant amplification de courant du transistor. Les valeurs typiques pour $B$ se situent dans la plage de $\num{20}$ à $\num{500}$.

<margin>
[picture:1071:a_bipolartransistor_aus:Transistor bipolaire NPN à l'état éteint]
[picture:1072:a_bipolartransistor_ein:Transistor bipolaire NPN à l'état allumé]
</margin>

[question:AC503]

Il est conseillé de mémoriser par exemple le transistor NPN. Pour le PNP, tout est alors inversé.

[question:AC504]

Physiquement, la tension base-émetteur $U_{BE}$ commande le courant de collecteur $I_C$ et de manière exponentielle. Pour le transistor npn, par exemple, on a :

$I_C = I_S \cdot e^{\frac{U_{BE}}{U_T}}$

$I_S$ est le courant de saturation, qui dépend fortement du type de transistor. Il est indiqué dans la feuille de données. $U_T$ est la soi-disant tension de température, qui est d'environ $\qty{26}{\milli\volt}$ à température ambiante.

Une différence avec le transistor à effet de champ que nous examinerons plus tard est que dans le transistor bipolaire, un courant circule toujours à l'entrée (la base), le courant de base $I_B$. Il dépend également de manière exponentielle de $U_{BE}$, où $I_S$ est plus petit d'un facteur $B$ que pour le courant de collecteur.

$I_B = \frac{I_S}{B} \cdot e^{\frac{U_{BE}}{U_T}}$

Le facteur $B$ est donc le quotient du courant de collecteur et du courant de base:

$B = \frac{I_C}{I_B}$

Même si le transistor bipolaire est physiquement commandé par $U_\mathrm{BE}$, on le désigne comme *commandé par le courant*, car il ne conduit que lorsqu'un courant de base circule.

[question:AC501]

Un transistor est désigné comme "conducteur" dans le sens de la "direction de passage" lorsqu'un courant de collecteur significatif circule. Pour cela, la diode base-émetteur doit toujours être connectée dans le sens passant, donc $U_{BE}$ positif pour les transistors npn et négatif pour les transistors pnp. La diode collecteur-base, en revanche, doit être bloquée, car aucun porteur de charge ne doit être injecté du collecteur dans la base.

[question:AC505]

Ensuite, nous examinons encore quelques circuits de transistor simples basés sur le transistor bipolaire.

---

[question:AC515]

Le point de fonctionnement souhaité est réglé en injectant un courant de base via $R_1$. Le courant de base est plus petit que le courant de collecteur de la amplification donnée de $\num{298}$. La différence entre la tension de service et le potentiel de base chute sur la résistance. Le potentiel de base est donné à $\qty{0,6}{\volt}$. Nous calculons donc:

$R_1 = 298 \cdot \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{0,005}{\ampere}} \approx \qty{680}{\kilo\ohm}$

<indepth>
Le circuit a cependant un énorme inconvénient en pratique : l'amplification d'un transistor bipolaire n'est pas particulièrement bien contrôlée. Prenons comme exemple le populaire BC547B. Son amplification peut, selon la spécification, être comprise entre $\num{200}$ et $\num{450}$. Le courant de collecteur peut donc s'écarter considérablement du projet avec cette circuit, de plus d'un facteur $2$.
</indepth>

Pour obtenir une meilleure stabilité du point de fonctionnement, le point de fonctionnement du transistor bipolaire est généralement réglé via un diviseur de tension. Le soi-disant courant transversal est le courant qui circule ici à travers $R_2$. Il doit être au moins dix fois plus élevé que le courant de base, afin que le courant de base n'ait pas grande influence sur le point de fonctionnement. 

---

[question:AC516]

<indepth>
Ce circuit n'est pas très recommandé en pratique. D'une part, le courant de collecteur dépend de manière exponentielle de la tension base-émetteur. Les résistances ont une tolérance, ce qui peut faire que le potentiel de base peut s'écarter quelque peu de la valeur de consigne - avec un grand effet sur le courant de collecteur. De plus, la tension de seuil de la diode base-émetteur est assez fortement dépendante de la température avec environ $\qty{-2}{\milli\volt\per\kelvin}$. Par conséquent, ce circuit aura une forte dépendance à la température du courant de collecteur. Cela peut parfois être souhaité, mais il faut en tenir compte. Nous apprendrons encore un circuit qui contient une contre-réaction qui stabilise le point de fonctionnement.
</indepth>

Il y a aussi un exercice de calcul pour ce circuit:

[question:AC518]

Le diviseur de tension $R_1$ et $R_2$ règle le potentiel de base, qui, puisque l'émetteur est à la masse, doit être d'environ $\qty{0,6}{\volt}$. Pour un courant de collecteur de $\qty{2}{\milli\ampere}$ et une amplification de $\num{200}$, le courant de base est $\qty{2}{\milli\ampere} / 200 = \qty{10}{\micro\ampere}$. Le courant à travers $R_2$ doit être le dixième du courant de base, à travers $R_1$ circule $11 \cdot \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$. La résistance $R_1$ est alors:

$R_1 = \frac{\qty{10}{\volt} - \qty{0,6}{\volt}}{\qty{110}{\micro\ampere}} = \qty{85,5}{\kilo\ohm}$

Le circuit suivant montre un réglage typique du point de fonctionnement pour le transistor bipolaire, tel qu'il est également utilisé en pratique.

---

[question:AC517]

<indepth>
C'est un bon circuit, qui est également fréquemment utilisé en pratique, car le courant de collecteur est principalement déterminé par la résistance d'émetteur $R_E$, qui représente une contre-réaction en série:

Si le courant de collecteur $I_C$ augmente, le courant d'émetteur $I_E$ augmente également. Une tension plus grande chute alors sur la résistance d'émetteur $R_E$. L'émetteur devient donc plus positif. Comme la tension de base reste presque constante grâce au diviseur de tension constitué de $R_1$ et $R_2$, la tension base-émetteur $ U_{BE} = U_B - U_E $ devient plus petite.

Une tension base-émetteur plus faible signifie que le transistor devient moins conducteur. Le courant initialement augmenté est ainsi réduit.

Le circuit agit donc automatiquement contre les changements de courant. C'est pourquoi on parle de contre-réaction. Si le courant augmente, le transistor est un peu "fermé". Si le courant diminue, le transistor devient à nouveau plus conducteur. Ainsi, le point de fonctionnement du circuit se stabilise.
</indepth>

Le potentiel de base est fixé par le diviseur de tension $R_1$ et $R_2$. Comme une tension de $\qty{1}{\volt}$ doit tomber sur la résistance d'émetteur $R_E$, le potentiel de base doit être de $\qty{1,6}{\volt}$. Pour un courant de collecteur de $\qty{2}{\milli\ampere}$ et une amplification de $\num{200}$, le courant de base est de $\qty{10}{\micro\ampere}$. Comme le courant à travers $R_2$ doit être le dixième du courant de base, le courant à travers $R_1$ est le onze fois le courant de base, donc $\qty{110}{\micro\ampere}$. La tension à travers $R_1$ est la différence entre la tension de service ($\qty{10}{\volt}$) et le potentiel de base, donc $\qty{8,4}{\volt}$. Nous pouvons maintenant déterminer $R_1$:

$R_1 = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} = \qty{76,4}{\kilo\ohm}$

[question:AC519]

Si $R_1$ n'est pas traversé par le courant en raison de l'erreur, aucune tension ne chute sur $R_2$ - la base est au potentiel de masse. Alors $U_{BE} \geq \qty{0,6}{\volt}$ n'est pas rempli, et le transistor est sans courant. Comme aucune tension ne chute sur la résistance de collecteur $R_C$, le potentiel de collecteur monte à la tension de service.

[question:AC520]

Dans le cas du schéma d'erreur donné ici, $R_2$ est sans courant. La base est connectée à la tension de service via $R_1$. Un courant de base est injecté via ce chemin. Avec le dimensionnement habituel (le courant transversal est le onze fois le courant de base régulier), le courant de base est 11 fois plus élevé que le courant de base régulier - le courant de collecteur augmentera fortement, la chute de tension sur $R_C$ augmentera fortement, la tension collecteur-émetteur diminuera à la valeur de saturation d'environ $\qty{0,1}{\volt}$. Le courant de collecteur n'est limité que par $R_C$.

---

Dans la tâche suivante, il s'agit d'un relais qui est commuté via le transistor npn représenté en série (cf. figure [ref:a_relais_schaltung]). Supposons que le transistor soit d'abord passant, un courant circule à travers la bobine du relais, le relais a attiré.<margin>
[picture:426:a_relais_schaltung:Circuit de relais avec transistor npn et diode de roue libre]
</margin>

Maintenant, le transistor se coupe, le flux de courant s'interrompt. Cependant, le changement important du courant induit brièvement dans la bobine du relais une tension négative élevée, qui peut entraîner la destruction du transistor.Pour éviter cela, nous branchons une diode de roue libre *en parallèle*. Elle est branchée de telle sorte qu'elle ne conduit pas de courant en fonctionnement normal (transistor passant) - elle doit donc être montée en sens inverse. La tension négative qui apparaît brièvement lors de l'interruption du courant commute la diode en sens direct, la tension générée est limitée (pour les diodes au silicium) à $\qty{-0,7}{\volt} \ldots \qty{-0,8}{\volt}$.[question:AC524]

---

Les transistors à effet de champ ont un principe de commande tout à fait différent de celui des transistors bipolaires. Alors que dans les transistors bipolaires, il faut prendre en compte à la fois les électrons et les électrons manquants ("trous"), dans le transistor à effet de champ, seule une sorte de porteurs de charge est impliquée ("unipolaire"). Il peut s'agir soit d'électrons (*transistor à effet de champ à canal n*) soit de trous (*transistor à effet de champ à canal p*).Les électrodes du FET, qui sont représentées dans la figure [ref:a_fet_schnitt_aus], sont désignées comme suit:* *Source*: c'est la "source" (en anglais source) pour les porteurs de charge dans le canal. Ne pas se laisser tromper: la soi-disant direction technique du courant est définie à l'inverse de la direction du flux de porteurs de charge!
* *Drain*: c'est l'écoulement (en anglais drain) pour les porteurs de charge dans le canal.
* *Gate*: La grille (en anglais gate) commande le flux des porteurs de charge dans le canal.

[question:AC512]

Tous les transistors à effet de champ (ou *FETs*) ont en commun qu'en fonctionnement normal, aucun courant ne circule dans l'entrée, l'électrode de grille. La commande de la charge dans le canal (la zone entre *Source* et *Drain*) dépend exclusivement de la tension Gate-Source.<margin>
[picture:1073:a_fet_schnitt_aus:FET en coupe transversale, non conducteur]
[picture:1074:a_fet_schnitt_ein:FET en coupe transversale, conducteur]
</margin>

Les figures [ref:a_fet_schnitt_aus] et [ref:a_fet_schnitt_ein] montrent la section transversale d'un MOSFET à canal n dans l'état bloqué et dans l'état conducteur. Dans l'image supérieure, aucune tension Gate-Source $U_{GS}$ suffisante n'est appliquée. Entre les zones dopées n de Source et Drain se trouve le substrat dopé p, de sorte qu'aucun canal conducteur n'est présent. Le transistor bloque, et aucun courant ne peut circuler entre Source et Drain.Si une tension positive est appliquée sur la grille par rapport à la source (cf. figure [ref:a_fet_schnitt_ein]), un champ électrique est créé à travers la couche isolante de SiO$_2$. Ce champ attire les électrons à la surface du substrat dopé p directement sous la grille. Cela forme un canal conducteur n qui relie la source et le drain. Le MOSFET devient conducteur, et un courant peut circuler entre le drain et la source.Il est important que la grille soit isolée électriquement par la couche d'oxyde. Idéalement, aucun courant de grille ne circule donc; le MOSFET n'est pas commandé par un courant de commande, mais par le champ électrique sur la grille. C'est pourquoi il est également désigné comme un composant *commandé par tension*.[question:AC502]

[question:AC513]

[question:AC514]

Comme nous l'avons déjà constaté, le FET est un composant *commandé par tension*, dans lequel aucun courant de grille ne circule. La réponse souhaitée est que la tension Gate-Source commande la *résistance du canal*. Cependant, le comportement du canal ne peut être décrit comme une résistance que pour de très petites tensions Drain-Source, dans cette mesure la réponse est quelque peu malheureuse. Mieux serait : la tension Gate-Source commande le courant du canal.---

La ligne verticale symbolise le canal, qui est contacté en haut (Drain) et en bas (Source). À gauche, on voit la grille - la flèche rappelle, avec la ligne verticale, une diode. Il s'agit donc d'un FET, plus précisément d'un FET à jonction. La figure [ref:a_fet_overview] montre une vue d'ensemble des différents types de FET avec leurs symboles de circuit.<margin>
[picture:1075:a_fet_overview:Aperçu des FET avec symboles]
</margin>

[question:AC506]

Dans les questions suivantes, il s'agit d'associer certains types de FET à leur symbole de circuit. Voici quelques règles de base :* Le courant dans le canal peut être transporté soit par des électrons, soit par des trous. Dans le premier cas, nous parlons d'un FET à canal n, dans le second cas d'un FET à canal p.
* Nous pouvons également distinguer les FETs selon qu'un courant circule dans le canal pour une tension Gate-Source $U_{GS}=0$ ou non. Ils sont alors soit *auto-conducteurs* soit *auto-bloquants*. 
* Enfin, nous pouvons distinguer les FETs selon que l'électrode de grille est une diode, ou une structure de condensateur. Si la grille est une diode, nous parlons d'un FET à jonction. Exemples : le JFET (transistor à effet de champ à jonction) et le MESFET (transistor à effet de champ métal-semi-conducteur). Dans le MESFET, la diode de grille est une diode Schottky. Dans un FET à couche isolante, l'électrode de grille est séparée du canal par un isolant (un diélectrique). La tension appliquée commande la densité de porteurs de charge dans le canal. Si l'isolant est un oxyde, par exemple le dioxyde de silicium, nous parlons également d'un MOSFET (transistor à effet de champ métal-oxyde-semi-conducteur). En raison de leur utilisation dans les circuits numériques, les MOSFETs sont de très loin les types de transistors les plus courants.La flèche indique s'il s'agit d'un FET à canal n ou p. Comme pour la diode, la flèche pointe vers la cathode, donc la zone dopée n. Si donc la flèche pointe vers le canal, il s'agit d'un FET à canal n. Dans le FET à jonction, la grille porte le canal, dans le FET à couche isolante, la flèche est visible entre le canal et la soi-disant couche de masse, qui se trouve sous le canal et est généralement connectée en interne à l'électrode de source.Dans le FET à couche isolante, la grille et le canal forment également graphiquement un condensateur.Dans le FET auto-conducteur, la ligne entre la source et le drain est continue, tandis que dans le FET auto-bloquant, elle est interrompue.[question:AC507]
[question:AC508]
[question:AC509]
[question:AC510]
[question:AC511]

Ensuite, nous voulons également examiner quelques circuits MOSFET qui s'appuient sur les questions précédentes.[question:AC521]

Aucun courant continu ne circule dans la connexion de grille d'un MOSFET. Il s'agit donc d'un diviseur de tension *non chargé* et il s'applique :$U_{GS} = \frac{R_2}{R_1 + R_2} \cdot U_B = \frac{\qty{1}{\kilo\ohm}}{\qty{11}{\kilo\ohm}} \cdot \qty{44}{\volt} = \qty{4}{\volt}$

[question:AC522]

Il s'agit également d'un diviseur de tension non chargé. Comme les tensions sont données, nous commençons simplement par :

$\frac{R_2}{R_1} = \frac{\qty{2,8}{\volt}}{\qty{44}{\volt} - \qty{2,8}{\volt}} \rightarrow R_2 = 0,068 \cdot \qty{10}{\kilo\ohm} = \qty{680}{\ohm}$

[question:AC523]

Le MOSFET de puissance est ici complètement saturé, le canal peut être représenté comme une résistance ohmique de (selon l'énoncé) $R_\mathrm{DSon} = \qty{4}{\milli\ohm}$. Un courant de $\qty{25}{\ampere}$ circule. Nous calculons la puissance dissipée simplement selon la formule de puissance connue :

$P_V = I^2 \cdot R_{\mathrm{DSon}} = \qty{2,5}{\watt}$