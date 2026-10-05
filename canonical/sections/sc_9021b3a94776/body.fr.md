Nous avions déjà discuté du transistor bipolaire dans le matériel de formation dans la section [sec:transistor_1]. Dans cette section, nous approfondirons le sujet et examinerons également un autre transistor.

Le transistor bipolaire est constitué de trois zones semi-conductrices, alternativement dopées de type N et de type P. Ces zones sont appelées émetteur, base et collecteur. Dans le *transistor npn*, l'émetteur est dopé de type N, la base de type P et le collecteur de type N. Dans le transistor pnp, c'est respectivement un émetteur de type P, une base de type N et un collecteur de type P.

La figure [ref:a_bipolartransistor_aus] montre un transistor npn à l'état éteint.
Dès que la tension base-émetteur $U_\mathrm{BE}$ est appliquée en fermant l'interrupteur (typiquement $\approx \qtyrange{0,6}{0,7}{\volt}$ pour le silicium), la diode base-émetteur devient conductrice. Il en résulte un faible courant de base $I_\mathrm{B}$ (cf. figure [ref:a_bipolartransistor_ein]).

Ce faible courant de base provoque l'injection de nombreux électrons de l'émetteur dans la base mince. Comme la base est très étroite, la plupart de ces porteurs de charge atteignent le collecteur. Là, ils sont « aspirés » par la tension collecteur-émetteur appliquée $U_\mathrm{CE}$, le courant de collecteur $I_\mathrm{C}$ circule. Il est plus grand que le courant de base d'un facteur $B$, où $B$ est le gain en courant dit du transistor. Les valeurs typiques de $B$ se situent dans la plage de $\num{20}$ à $\num{500}$.

<margin>
[picture:1071:a_bipolartransistor_aus:Transistor bipolaire NPN à l'état éteint]
[picture:1072:a_bipolartransistor_ein:Transistor bipolaire NPN à l'état allumé]
</margin>

[question:AC503]

Il est recommandé, par exemple, de mémoriser le transistor NPN. Pour le PNP, tout est inversé.

[question:AC504]

Physiquement, la tension base-émetteur $U_{BE}$ contrôle le courant de collecteur $I_C$, et ce de manière exponentielle. Pour un transistor npn, par exemple, on a :

$I_C = I_S \cdot e^{\frac{U_{BE}}{U_T}}$

$I_S$ est le courant de saturation, qui dépend fortement de la conception du transistor. Il est à consulter dans la fiche technique. $U_T$ est la tension dite thermique, qui à température ambiante est d'environ $\qty{26}{\milli\volt}$.

Une différence avec le transistor à effet de champ examiné plus tard est que, dans le transistor bipolaire, un courant circule toujours dans l'entrée (la base), le courant de base $I_B$. Il dépend également de manière exponentielle de $U_{BE}$, où $I_S$ est inférieur d'un facteur $B$ par rapport au courant du collecteur.

$I_B = \frac{I_S}{B} \cdot e^{\frac{U_{BE}}{U_T}}$

Le facteur $B$ est donc le quotient entre le courant du collecteur et le courant de base :

$B = \frac{I_C}{I_B}$

Même si le transistor bipolaire est physiquement commandé par $U_\mathrm{BE}$, on le qualifie de *commandé en courant*, car il ne conduit que lorsqu'un courant de base circule.

[question:AC501]

Un transistor est dit "conducteur" en "sens direct" lorsqu'un courant de collecteur significatif circule. Pour cela, la diode base-émetteur doit toujours être polarisée en direct, c'est-à-dire $U_{BE}$ positif pour les transistors npn et négatif pour les transistors pnp. En revanche, la diode collecteur-base doit être bloquée, car aucun porteur de charge ne doit être injecté du collecteur vers la base.

[question:AC505]

Dans ce qui suit, nous examinons encore quelques circuits simples à transistor basés sur le transistor bipolaire.

---

[question:AC515]

Le point de fonctionnement souhaité est réglé en imposant un courant de base via $R_1$. Le courant de base est inférieur au courant de collecteur par le facteur de gain en courant donné de $\num{298}$. La différence entre la tension de service et le potentiel de base chute aux bornes de la résistance. Le potentiel de base est donné à $\qty{0,6}{\volt}$. Nous calculons donc :

$R_1 = 298 \cdot \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{0,005}{\ampere}} \approx \qty{680}{\kilo\ohm}$

<indepth>
Le circuit présente cependant un énorme inconvénient en pratique : le gain en courant d'un transistor bipolaire n'est pas particulièrement bien contrôlé. Prenons comme exemple le populaire BC547B. Son gain en courant peut, selon les spécifications, varier entre $\num{200}$ et $\num{450}$. Le courant de collecteur peut donc, avec ce circuit, s'écarter de la conception de plus d'un facteur $2$.
</indepth>

Pour obtenir une meilleure stabilité du point de fonctionnement, le point de fonctionnement du transistor bipolaire est généralement réglé via un diviseur de tension. Le courant dit transversal est le courant qui circule ici à travers $R_2$. Il devrait être au moins dix fois plus élevé que le courant de base, afin que le courant de base n'ait pas une grande influence sur le point de fonctionnement.

---

[question:AC516]

<indepth>
Ce circuit n'est pas non plus très recommandable d'un point de vue pratique. D'une part, le courant de collecteur dépend exponentiellement de la tension base-émetteur. Les résistances ont une tolérance, ce qui peut faire dévier le potentiel de base de la valeur nominale - avec un impact important sur le courant de collecteur. De plus, la tension de seuil de la diode base-émetteur, d'environ $\qty{-2}{\milli\volt\per\kelvin}$, est assez fortement dépendante de la température. Par conséquent, ce circuit aura une forte variation du courant de collecteur avec la température. Cela peut parfois être souhaitable, mais il faut en être conscient. Nous allons encore découvrir un circuit qui contient une contre-réaction stabilisant le point de fonctionnement.
</indepth>

Il existe également un problème de calcul pour ce circuit :

[question:AC518]

Le diviseur de tension $R_1$ et $R_2$ règle le potentiel de base qui, parce que l'émetteur est à la masse, doit être d'environ $\qty{0,6}{\volt}$. Avec un courant de collecteur de $\qty{2}{\milli\ampere}$ et un gain en courant de $\num{200}$, le courant de base est $\qty{2}{\milli\ampere} / 200 = \qty{10}{\micro\ampere}$. Le courant traversant $R_2$ doit être dix fois le courant de base, le courant traversant $R_1$ est $11 \cdot \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$. La résistance $R_1$ est alors :

$R_1 = \frac{\qty{10}{\volt} - \qty{0,6}{\volt}}{\qty{110}{\micro\ampere}} = \qty{85,5}{\kilo\ohm}$

Le circuit suivant montre un réglage typique du point de fonctionnement pour un transistor bipolaire, tel qu'il est également utilisé en pratique.

---

[question:AC517]

<indepth>
Il s'agit d'un bon circuit, fréquemment utilisé en pratique, car le courant de collecteur est principalement déterminé par la résistance d'émetteur $R_E$, qui représente une contre-réaction en série :

Si le courant de collecteur $I_C$ augmente, le courant d'émetteur $I_E$ augmente également. Il en résulte une chute de tension plus importante aux bornes de la résistance d'émetteur $R_E$. L'émetteur devient donc plus positif. Comme la tension de base reste quasiment constante grâce au diviseur de tension formé par $R_1$ et $R_2$, la tension base-émetteur $ U_{BE} = U_B - U_E $ diminue.

Une tension base-émetteur plus faible signifie que le transistor devient moins conducteur. Le courant initialement augmenté est ainsi réduit à nouveau.

Le circuit agit donc automatiquement contre les variations du courant. C'est pourquoi on parle de contre-réaction. Si le courant augmente, le transistor est légèrement « fermé ». Si le courant diminue, le transistor devient à nouveau plus conducteur. Ainsi, le point de fonctionnement du circuit se stabilise.
</indepth>

Le potentiel de base est fixé par le diviseur de tension $R_1$ et $R_2$. Puisqu'une tension de $\qty{1}{\volt}$ doit diminuer aux bornes de la résistance d'émetteur $R_E$, le potentiel de base doit être de $\qty{1,6}{\volt}$. Avec un courant de collecteur de $\qty{2}{\milli\ampere}$ et un gain en courant de $\num{200}$, le courant de base est de $\qty{10}{\micro\ampere}$. Étant donné que le courant traversant $R_2$ doit être dix fois le courant de base, le courant traversant $R_1$ est onze fois le courant de base, soit $\qty{110}{\micro\ampere}$. Aux bornes de $R_1$, la différence de la tension de service ($\qty{10}{\volt}$) et du potentiel de base diminue, donc $\qty{8,4}{\volt}$. Nous pouvons maintenant déterminer $R_1$ :

$R_1 = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} = \qty{76,4}{\kilo\ohm}$

[question:AC519]

Si $R_1$ n'est pas traversé par le courant en raison de la panne, alors aucune tension ne diminue aux bornes de $R_2$ - la base est au potentiel de masse. Alors $U_{BE} \geq \qty{0,6}{\volt}$ n'est pas satisfaite, et le transistor est sans courant. Puisqu'aucune tension ne diminue aux bornes de la résistance de collecteur $R_C$, le potentiel de collecteur monte à la tension de service.

[question:AC520]

Dans le cas de défaut présenté ici, $R_2$ est sans courant. La base est connectée à la tension de service via $R_1$. Un courant de base est injecté par cette voie. Avec le dimensionnement usuel (le courant de shunt est dix fois le courant de base régulier), le courant de base est 11 fois plus élevé que le courant de base régulier - le courant du collecteur augmentera très fortement, la chute de tension aux bornes de $R_C$ augmente fortement, la tension collecteur-émetteur descend à la valeur de saturation d'environ $\qty{0,1}{\volt}$. Le courant du collecteur est uniquement limité par $R_C$.

---

Dans la tâche suivante, il s'agit d'un relais qui est commuté via le transistor npn représenté en série (cf. figure [ref:a_relais_schaltung]). Supposons que le transistor est initialement saturé, un courant circule dans la bobine du relais, le relais est activé.

<margin>
[picture:426:a_relais_schaltung:Circuit de relais avec transistor npn et diode de roue libre]
</margin>

Le transistor se coupe alors, l'écoulement du courant s'effondre. Cependant, la forte variation du courant induit brièvement dans la bobine du relais une haute tension négative, qui peut conduire à la destruction du transistor.

Pour éviter cela, nous connectons une diode de roue libre *en parallèle*. Elle est connectée de manière à ne pas conduire de courant en fonctionnement normal (transistor saturé) - elle doit donc être installée en polarisation inverse. La tension négative qui apparaît brièvement lors de l'effondrement du courant met la diode en conduction directe, la tension résultante est limitée (pour les diodes au silicium) à $\qty{-0,7}{\volt} \ldots \qty{-0,8}{\volt}$.

[question:AC524]

---

Les transistors à effet de champ ont un principe de commande totalement différent de celui des transistors bipolaires. Alors que pour les transistors bipolaires, il faut considérer à la fois les électrons et les trous d'électrons ("trous") (d'où "bipolaire"), dans le transistor à effet de champ, une seule sorte de porteurs de charge est impliquée ("unipolaire"). Il peut s'agir soit d'électrons (*transistor à effet de champ à canal n*) soit de trous (*transistor à effet de champ à canal p*).

Les électrodes du FET, représentées dans la figure [ref:a_fet_schnitt_aus], sont désignées comme suit :

* *Source* : c'est la "source" (angl. source) des porteurs de charge dans le canal. Ne vous laissez pas tromper : le sens conventionnel du courant est défini à l'opposé de la direction du flux des porteurs de charge !
* *Drain* : c'est le drain (angl. drain) pour les porteurs de charge dans le canal.
* *Gate* : La grille (angl. gate) contrôle le flux des porteurs de charge dans le canal.

[question:AC512]

Tous les transistors à effet de champ (ou *FETs*) ont en commun qu'en fonctionnement normal, aucun courant ne circule dans l'entrée, l'électrode de grille. Le contrôle de la charge dans le canal (la zone entre la *Source* et le *Drain*) dépend exclusivement de la tension grille-source.

<margin>
[picture:1073:a_fet_schnitt_aus:FET en coupe transversale, non conducteur]
[picture:1074:a_fet_schnitt_ein:FET en coupe transversale, conducteur]
</margin>

Les figures [ref:a_fet_schnitt_aus] et [ref:a_fet_schnitt_ein] montrent la coupe transversale d'un MOSFET à canal N à l'état bloqué et à l'état conducteur. Dans l'image du haut, aucune tension grille-source $U_{GS}$ suffisante n'est appliquée. Entre les zones dopées de type N de la source et du drain se trouve le substrat dopé de type P, de sorte qu'aucun canal conducteur n'est présent. Le transistor est bloqué, et aucun courant ne peut circuler entre la source et le drain.

Si une tension positive est appliquée à la grille par rapport à la source (voir figure [ref:a_fet_schnitt_ein]), un champ électrique se crée à travers la couche isolante de SiO$_2$. Ce champ attire les électrons vers la surface du substrat dopé de type P juste en dessous de la grille. Il en résulte la formation d'un canal conducteur de type N qui relie la source et le drain. Le MOSFET devient conducteur, et un courant peut circuler entre le drain et la source.

Il est important de noter que la grille est électriquement isolée par la couche d'oxyde. Dans l'idéal, aucun courant de grille ne circule ; le MOSFET n'est pas commandé par un courant de commande, mais par le champ électrique à la grille. C'est pourquoi il est également appelé composant *commandé en tension*.

[question:AC502]

[question:AC513]

[question:AC514]

Comme nous l'avons déjà établi, le FET est un composant *commandé par tension*, dans lequel aucun courant de grille ne circule. La réponse souhaitée est que la tension grille-source contrôle la *résistance du canal*. Cependant, le comportement du canal ne peut être décrit comme une résistance que pour des tensions drain-source très faibles, donc la réponse est quelque peu maladroitement formulée. Il serait préférable de dire : la tension grille-source contrôle le courant du canal.

---

La ligne verticale symbolise le canal, qui est contacté en haut (Drain) et en bas (Source). À gauche, on voit la grille - la flèche, avec le trait vertical, rappelle une diode. Il s'agit donc d'un FET, plus précisément d'un JFET. La figure [ref:a_fet_overview] montre un aperçu des différents types de FET avec leurs symboles de circuit.

<margin>
[picture:1075:a_fet_overview:FET-Übersicht mit Symbolen]
</margin>

[question:AC506]

Les questions suivantes concernent l'association de types spécifiques de FET à leur symbole électrique. Voici quelques règles de base :

* Le courant dans le canal peut être transporté soit par des électrons, soit par des trous. Dans le premier cas, nous parlons d'un *FET à canal n*, dans le second d'un *FET à canal p*.
* Nous pouvons également distinguer les FET selon qu'un courant circule dans le canal pour une tension grille-source $U_{GS}=0$ ou non. Ils sont alors appelés soit *à déplétion* (ou auto-conducteurs), soit *à enrichissement* (ou auto-bloquants).
* Enfin, nous pouvons distinguer les FET selon que l'électrode de grille est une diode ou une structure de condensateur. Si la grille est une diode, nous parlons d'un JFET. Des exemples sont le JFET (transistor à effet de champ à jonction) et le MESFET (transistor à effet de champ métal-semiconducteur). Dans le MESFET, la diode de grille est une diode Schottky. Dans un *transistor FET à grille isolée*, l'électrode de grille est séparée du canal par un isolant (un diélectrique / matériau isolant). La tension appliquée contrôle la densité des porteurs de charge dans le canal. Si l'isolant est un oxyde, par exemple le dioxyde de silicium, nous parlons également d'un MOSFET (FET métal-oxyde-semiconducteur). En raison de leur utilisation dans les circuits numériques, les MOSFETs sont de très loin les types de transistors les plus courants.

La flèche indique s'il s'agit d'un FET à canal n ou p. Comme pour la diode, la flèche pointe vers la cathode, c'est-à-dire la région dopée n. Ainsi, si la flèche pointe vers le canal, il s'agit d'un FET à canal n. Dans le JFET, la grille porte le canal, tandis que dans le transistor FET à grille isolée, la flèche est visible entre le canal et la couche dite bulk, qui se trouve sous le canal et est généralement connectée en interne à l'électrode source.

Dans le transistor FET à grille isolée, la grille et le canal forment également graphiquement un condensateur.

Pour le FET à canal conducteur, la ligne entre la source et le drain est continue, tandis que pour le FET à canal bloqué, elle est interrompue.

[question:AC507]
[question:AC508]
[question:AC509]
[question:AC510]
[question:AC511]

Dans la suite, nous allons également examiner quelques circuits MOSFET qui s'appuient sur les questions précédentes.

[question:AC521]

Aucun courant continu ne circule dans la borne de grille d'un MOSFET. Il s'agit donc d'un *diviseur de tension non chargé* et on a :

$U_{GS} = \frac{R_2}{R_1 + R_2} \cdot U_B = \frac{\qty{1}{\kilo\ohm}}{\qty{11}{\kilo\ohm}} \cdot \qty{44}{\volt} = \qty{4}{\volt}$

[question:AC522]

Ici aussi, il s'agit d'un diviseur de tension non chargé. Comme les tensions sont données, nous partons le plus simplement de :

$\frac{R_2}{R_1} = \frac{\qty{2,8}{\volt}}{\qty{44}{\volt} - \qty{2,8}{\volt}} \rightarrow R_2 = 0,068 \cdot \qty{10}{\kilo\ohm} = \qty{680}{\ohm}$

[question:AC523]

Le MOSFET de puissance est ici complètement saturé, le canal peut être représenté comme une résistance ohmique de (selon l'énoncé du problème) $R_\mathrm{DSon} = \qty{4}{\milli\ohm}$. Un courant de $\qty{25}{\ampere}$ circule. Nous calculons simplement la puissance dissipée à l'aide de la formule de puissance connue :

$P_V = I^2 \cdot R_{\mathrm{DSon}} = \qty{2,5}{\watt}$
