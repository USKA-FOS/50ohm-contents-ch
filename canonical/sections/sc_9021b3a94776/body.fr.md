Le transistor bipolaire a déjà été abordé dans les documents de formation pour la classe E. Dans la classe A, nous approfondirons le sujet et examinerons également un autre transistor.Le transistor bipolaire est constitué de trois zones semi-conductrices, alternativement dopées de type N et de type P. Ces zones sont appelées émetteur, base et collecteur. Dans un *transistor NPN*, l’émetteur est dopé de type N, la base de type P et le collecteur de type N. Pour un transistor PNP, il s’agit respectivement d’un émetteur de type P, d’une base de type N et d’un collecteur de type P.L’illustration [ref:a_bipolartransistor_aus] montre un transistor NPN à l’état bloqué. Dès que la tension base-émetteur $U_\mathrm{BE}$ est appliquée (typiquement $\approx \qtyrange{0,6}{0,7}{\volt}$ pour le silicium) en fermant l’interrupteur, la diode base-émetteur devient conductrice. Un faible courant de base $I_\mathrm{B}$ s’établit alors (voir illustration [ref:a_bipolartransistor_ein]).Ce faible courant de base permet d’injecter de nombreux électrons depuis l’émetteur dans la base, zone très mince. La plupart de ces porteurs de charge traversent la base et atteignent le collecteur, où ils sont « aspirés » par la tension collecteur-émetteur $U_\mathrm{CE}$ appliquée. Le courant de collecteur $I_\mathrm{C}$ s’établit alors. Il est plus grand que le courant de base d’un facteur $B$, appelé gain en courant du transistor. Les valeurs typiques de $B$ se situent entre $\num{20}$ et $\num{500}$. <margin>
[picture:1071:a_bipolartransistor_aus:Transistor bipolaire NPN à l’état bloqué]
[picture:1072:a_bipolartransistor_ein:Transistor bipolaire NPN à l’état passant]
</margin>
[question:AC503]
Il est conseillé, par exemple, de retenir le transistor NPN. Pour le PNP, tout est inversé.[question:AC504]
En physique, la tension base-émetteur $U_{BE}$ commande le courant de collecteur $I_C$ de manière exponentielle. Par exemple, pour un transistor NPN, on a :$I_C = I_S \cdot e^{\frac{U_{BE}}{U_T}}$

$I_S$ est le courant de saturation, qui dépend fortement du type de construction du transistor. Il est indiqué dans la fiche technique. $U_T$ est la tension thermique, qui est d'environ $\qty{26}{\milli\volt}$ à température ambiante.

Une différence avec le transistor à effet de champ, examiné plus tard, est que dans le transistor bipolaire, un courant circule toujours à l'entrée (la base), le courant de base $I_B$. Ce courant dépend également de manière exponentielle de $U_{BE}$, mais $I_S$ est plus petit d'un facteur $B$ que dans le cas du courant de collecteur.

$I_B = \frac{I_S}{B} \cdot e^{\frac{U_{BE}}{U_T}}$

Le facteur $B$ est donc le quotient du courant de collecteur et du courant de base :

$B = \frac{I_C}{I_B}$

Bien que le transistor bipolaire soit commandé physiquement par $U_\mathrm{BE}$, on le qualifie de *commandé par courant*, car il ne conduit que lorsqu'un courant de base circule.

[question:AC501]

Un transistor est dit "conducteur" dans le *sens direct* lorsqu'un courant de collecteur significatif circule. Pour cela, la diode base-émetteur doit toujours être polarisée en sens direct, c'est-à-dire que $U_{BE}$ doit être positif pour les transistors npn et négatif pour les transistors pnp. La diode collecteur-base, en revanche, doit être bloquée, car aucun porteur de charge ne doit être injecté du collecteur vers la base.

[question:AC505]

Voici quelques circuits simples à transistor à base de transistor bipolaire.---
[question:AC515]
Le point de fonctionnement souhaité est réglé en injectant un courant de base via $R_1$. Le courant de base est inférieur au courant de collecteur d'un facteur égal au gain en courant, ici $\num{298}$. La tension aux bornes de la résistance est la différence entre la tension de service et le potentiel de la base. Le potentiel de la base est de $\qty{0,6}{\volt}$. Le calcul donne donc :
$R_1 = 298 \cdot \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{0,005}{\ampere}} \approx \qty{680}{\kilo\ohm}$
<indepth>
Ce circuit présente cependant un inconvénient majeur en pratique : le gain en courant d'un transistor bipolaire n'est pas très bien contrôlé. Prenons par exemple le populaire BC547B. Selon les spécifications, son gain en courant peut varier entre $\num{200}$ et $\num{450}$. Le courant de collecteur peut donc s'écarter de plus d'un facteur $2$ de la valeur de conception avec ce circuit.
</indepth>
Pour obtenir une meilleure stabilité du point de fonctionnement, celui-ci est généralement réglé à l'aide d'un diviseur de tension. Le courant transversal, appelé aussi courant de repos, est le courant traversant $R_2$. Il doit être au moins dix fois supérieur au courant de base, afin que ce dernier n'ait pas d'influence significative sur le point de fonctionnement.
---
[question:AC516]
<indepth>
Ce circuit n'est pas non plus très recommandé en pratique. D'une part, le courant de collecteur dépend exponentiellement de la tension base-émetteur. Les résistances ont une tolérance, ce qui peut entraîner un écart du potentiel de base par rapport à la valeur cible, avec un impact important sur le courant de collecteur. D'autre part, la tension de seuil de la diode base-émetteur est fortement dépendante de la température, avec environ $\qty{-2}{\milli\volt\per\kelvin}$. Par conséquent, ce circuit présentera une forte variation du courant de collecteur en fonction de la température. Cela peut parfois être souhaité, mais il faut en être conscient. Nous verrons plus tard un circuit qui intègre une contre-réaction pour stabiliser le point de fonctionnement.
</indepth>
Il y a également un exercice de calcul pour ce circuit :

[question:AC518]

Le diviseur de tension formé par les résistances $R_1$ et $R_2$ fixe le potentiel de la base, qui, l'émetteur étant à la masse, doit être d'environ $\qty{0,6}{\volt}$. Pour un courant de collecteur de $\qty{2}{\milli\ampere}$ et un gain en courant de $\num{200}$, le courant de base est de $\qty{2}{\milli\ampere} / 200 = \qty{10}{\micro\ampere}$. Le courant traversant $R_2$ doit être dix fois le courant de base, et le courant traversant $R_1$ est de $11 \cdot \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$. La résistance $R_1$ est alors :

$R_1 = \frac{\qty{10}{\volt} - \qty{0,6}{\volt}}{\qty{110}{\micro\ampere}} = \qty{85,5}{\kilo\ohm}$

Le circuit suivant montre un réglage typique du point de fonctionnement d'un transistor bipolaire, tel qu'il est également utilisé en pratique.

---

[question:AC517]

<indepth>
Il s'agit d'un bon circuit, souvent utilisé en pratique, car le courant de collecteur est principalement déterminé par la résistance d'émetteur $R_E$, qui constitue une contre-réaction série :

Si le courant de collecteur $I_C$ augmente, le courant d'émetteur $I_E$ augmente également. Par conséquent, une tension plus élevée se développe aux bornes de la résistance d'émetteur $R_E$. L'émetteur devient donc plus positif. Comme la tension de base est presque constante grâce au diviseur de tension formé par $R_1$ et $R_2$, la tension base-émetteur $ U_{BE} = U_B - U_E $ diminue.

Une tension base-émetteur plus faible signifie que le transistor devient moins conducteur. Le courant initialement augmenté est ainsi réduit.

Ce circuit s'oppose donc automatiquement aux variations du courant. C'est pourquoi on parle de contre-réaction. Si le courant augmente, le transistor est légèrement "fermé". S'il diminue, le transistor devient à nouveau plus conducteur. Ainsi, le point de fonctionnement du circuit se stabilise.
</indepth>

Le potentiel de la base est défini par le diviseur de tension constitué de $R_1$ et $R_2$. Comme une tension de $\qty{1}{\volt}$ doit chuter aux bornes de la résistance d'émetteur $R_E$, le potentiel de la base doit être de $\qty{1,6}{\volt}$. Pour un courant de collecteur de $\qty{2}{\milli\ampere}$ et un gain en courant de $\num{200}$, le courant de base est de $\qty{10}{\micro\ampere}$. Comme le courant traversant $R_2$ doit être dix fois supérieur au courant de base, le courant traversant $R_1$ est onze fois supérieur au courant de base, soit $\qty{110}{\micro\ampere}$. Aux bornes de $R_1$, la différence entre la tension de service ($\qty{10}{\volt}$) et le potentiel de la base chute, soit $\qty{8,4}{\volt}$. Nous pouvons maintenant déterminer $R_1$ :

$R_1 = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} = \qty{76,4}{\kilo\ohm}$

[question:AC519]

Si $R_1$ n'est pas traversé par le courant en raison d'une défaillance, aucune tension ne chute aux bornes de $R_2$ : la base est au potentiel de masse. Dans ce cas, la condition $U_{BE} \geq \qty{0,6}{\volt}$ n'est pas remplie et le transistor est bloqué. Comme aucune tension ne chute aux bornes de la résistance de collecteur $R_C$, le potentiel du collecteur monte jusqu'à la tension de service.

[question:AC520]

Dans le cas de la défaillance illustrée ici, $R_2$ n'est traversé par aucun courant. La base est connectée à la tension de service via $R_1$. Un courant de base est injecté par cette voie. Avec la dimensionnement habituel (le courant transversal est dix fois supérieur au courant de base régulier), le courant de base est onze fois supérieur au courant de base régulier : le courant de collecteur augmente fortement, la chute de tension aux bornes de $R_C$ augmente fortement, et la tension collecteur-émetteur diminue jusqu'à la valeur de saturation d'environ $\qty{0,1}{\volt}$. Le courant de collecteur est alors uniquement limité par $R_C$.

---

Dans la tâche suivante, il s'agit d'un relais qui est commuté par le transistor npn représenté en série (cf. figure [ref:a_relais_schaltung]). Supposons que le transistor soit initialement passant, qu'un courant circule à travers la bobine du relais et que le relais soit activé.

<margin>
[picture:426:a_relais_schaltung:Schéma du relais avec transistor npn et diode de roue libre]
</margin>

Le transistor se bloque alors, le courant s'interrompt brutalement. La forte variation du courant induit cependant brièvement dans la bobine du relais une tension négative élevée, qui peut détruire le transistor.Pour éviter cela, on place une diode de roue libre en parallèle. Elle est montée de telle sorte qu'en fonctionnement normal (transistor passant), elle ne conduit aucun courant : elle doit donc être montée en polarisation inverse. La tension négative qui apparaît brièvement lors de l'interruption du courant polarise la diode en direct, et la tension résultante est limitée (pour les diodes au silicium) à environ $\qty{-0,7}{\volt} \ldots \qty{-0,8}{\volt}$.[question:AC524]

---

Les transistors à effet de champ (FET) fonctionnent selon un principe de commande très différent de celui des transistors bipolaires. Alors que pour les transistors bipolaires, il faut considérer à la fois les électrons et les trous (d'où le terme « bipolaire »), dans le cas du transistor à effet de champ, une seule sorte de porteurs de charge est impliquée (« unipolaire »). Il peut s'agir soit d'électrons (transistor à effet de champ à canal *n*), soit de trous (transistor à effet de champ à canal *p*).Les électrodes du FET, représentées dans l'illustration [ref:a_fet_schnitt_aus], sont désignées comme suit :* *Source* : il s'agit de la « source » (en anglais *source*) des porteurs de charge dans le canal. Attention à ne pas confondre : le sens conventionnel du courant est défini à l'inverse de la direction du flux des porteurs de charge !
* *Drain* : il s'agit de l'évacuation (en anglais *drain*) des porteurs de charge dans le canal.
* *Gate* : la grille (en anglais *gate*) contrôle le flux des porteurs de charge dans le canal.[question:AC512]

Tous les transistors à effet de champ (ou *FET*) ont en commun qu'en fonctionnement normal, aucun courant ne circule dans l'entrée, c'est-à-dire l'électrode de grille. La commande des porteurs de charge dans le canal (la zone entre *Source* et *Drain*) dépend exclusivement de la tension grille-source.<margin>
[picture:1073:a_fet_schnitt_aus:FET en coupe, non conducteur]
[picture:1074:a_fet_schnitt_ein:FET en coupe, conducteur]
</margin>

Les figures [ref:a_fet_schnitt_aus] et [ref:a_fet_schnitt_ein] montrent une coupe transversale d'un MOSFET à canal N en état bloqué et en état passant. Dans l'image du haut, aucune tension grille-source $U_{GS}$ suffisante n'est appliquée. Entre les zones dopées de type N de la source et du drain se trouve le substrat dopé de type P, de sorte qu'aucun canal conducteur n'existe. Le transistor est bloqué, et aucun courant ne peut circuler entre la source et le drain.

Lorsqu'une tension positive est appliquée sur la grille par rapport à la source (cf. figure [ref:a_fet_schnitt_ein]), un champ électrique se crée à travers la couche isolante de SiO$_2$. Ce champ attire des électrons vers la surface du substrat dopé de type P directement sous la grille. Il se forme ainsi un canal conducteur de type N qui relie la source et le drain. Le MOSFET devient passant, et un courant peut circuler entre le drain et la source.

Il est important de noter que la grille est isolée électriquement par la couche d'oxyde. Dans l'idéal, aucun courant ne circule dans la grille ; le MOSFET n'est pas commandé par un courant de commande, mais par le champ électrique sur la grille. C'est pourquoi il est aussi appelé composant *commandé par tension*.

[question:AC502]

[question:AC513]

[question:AC514]

Comme nous l'avons déjà établi, le FET est un composant *commandé par tension* dans lequel aucun courant ne circule dans la grille. La réponse attendue est que la tension grille-source commande la *résistance du canal*. Cependant, le comportement du canal ne peut être décrit comme une résistance que pour des tensions drain-source très faibles ; cette formulation est donc un peu malheureuse. Une meilleure formulation serait : la tension grille-source commande le courant dans le canal.

---

La ligne verticale symbolise le canal, qui est connecté en haut (drain) et en bas (source). À gauche se trouve la grille – la flèche, combinée à la ligne verticale, rappelle une diode. Il s'agit donc d'un FET, plus précisément d'un JFET. La figure [ref:a_fet_overview] présente une vue d'ensemble des différents types de FET avec leurs symboles de schéma.

<margin>
[picture:1075:a_fet_overview:Vue d'ensemble des FET avec symboles]
</margin>

[question:AC506]

Les questions suivantes visent à associer certains types de FET à leur symbole électrique. Voici quelques règles de base :

* Le courant dans le canal peut être transporté soit par des électrons, soit par des trous. Dans le premier cas, on parle d’un *FET à canal n*, dans le second cas d’un *FET à canal p*.
* On peut aussi classer les FET selon qu’un courant circule dans le canal lorsque la tension grille-source vaut $U_{GS}=0$ ou non. Ils sont alors dits *à appauvrissement* ou *à enrichissement*.
* Enfin, on peut distinguer les FET selon que l’électrode de grille est une diode ou une structure capacitive. Si la grille est une diode, on parle de FET à jonction (JFET, pour *junction field effect transistor*, ou MESFET, pour *metal semiconductor field effect transistor*). Dans le cas du MESFET, la diode de grille est une diode Schottky. Pour un *FET à grille isolée*, l’électrode de grille est séparée du canal par un isolant (un matériau diélectrique). La tension appliquée contrôle la densité de porteurs de charge dans le canal. Si l’isolant est un oxyde, par exemple du dioxyde de silicium, on parle aussi de MOSFET (*metal oxide semiconductor FET*). En raison de leur utilisation dans les circuits numériques, les MOSFET sont de loin les transistors les plus répandus.

La flèche indique s’il s’agit d’un FET à canal n ou à canal p. Comme pour la diode, la flèche pointe vers la cathode, c’est-à-dire la zone dopée n. Si la flèche pointe vers le canal, il s’agit d’un FET à canal n. Dans le cas du FET à jonction, la grille entoure le canal, tandis que dans le cas du FET à grille isolée, la flèche est située entre le canal et la couche dite de *bulk*, qui se trouve sous le canal et est généralement reliée en interne à l’électrode de source.

Dans un FET à grille isolée, la grille et le canal forment également, graphiquement, un condensateur.

Pour un FET à appauvrissement, la ligne entre source et drain est continue, tandis que pour un FET à enrichissement, elle est interrompue.

[question:AC507]
[question:AC508]
[question:AC509]
[question:AC510]
[question:AC511]

Nous allons maintenant examiner quelques circuits à MOSFET, qui s’appuient sur les questions précédentes.

[question:AC521]

Aucun courant continu ne circule dans la grille d’un MOSFET. Il s’agit donc d’un *diviseur de tension non chargé* et l’on a :

$U_{GS} = \frac{R_2}{R_1 + R_2} \cdot U_B = \frac{\qty{1}{\kilo\ohm}}{\qty{11}{\kilo\ohm}} \cdot \qty{44}{\volt} = \qty{4}{\volt}$

[question:AC522]

Il s'agit ici également d'un diviseur de tension non chargé. Comme les tensions sont données, nous utilisons la méthode la plus simple :

$\frac{R_2}{R_1} = \frac{\qty{2,8}{\volt}}{\qty{44}{\volt} - \qty{2,8}{\volt}} \rightarrow R_2 = 0,068 \cdot \qty{10}{\kilo\ohm} = \qty{680}{\ohm}$

[question:AC523]

Le MOSFET de puissance est ici complètement passant, le canal peut être représenté comme une résistance ohmique de (selon l'énoncé) $R_{\mathrm{DSon}} = \qty{4}{\milli\ohm}$. Un courant de $\qty{25}{\ampere}$ circule. Nous calculons la puissance dissipée à l'aide de la formule de puissance connue :

$P_V = I^2 \cdot R_{\mathrm{DSon}} = \qty{2,5}{\watt}$