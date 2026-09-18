Lors de la numérisation d'un signal analogique, deux propriétés doivent être prises en compte : à quels moments le signal est mesuré et avec quelle précision les valeurs mesurées peuvent être représentées. Les deux étapes correspondantes sont appelées *échantillonnage* et *quantification*.

Les termes *à temps continu*, *à temps discret*, *à valeurs continues* et *à valeurs discrètes* décrivent deux propriétés indépendantes d'un signal. D'une part, on peut considérer si le signal est défini à tout moment. D'autre part, on peut examiner s'il peut prendre des valeurs arbitraires.

Un signal analogique idéal est à la fois *à temps continu* et *à valeurs continues*. Il est défini à tout moment et peut prendre n'importe quelle valeur intermédiaire dans sa plage de valeurs. Un tel signal est illustré dans la figure [ref:a_wertkont_zeitkont].

---

Les signaux analogiques n'ont pas de résolution temporelle minimale et sont continus dans le temps. Ils sont donc qualifiés de *à temps continu*. Lors de l'échantillonnage, un tel signal n'est mesuré qu'à des moments précis, c'est-à-dire qu'il est prélevé. Les valeurs d'échantillonnage individuelles sont appelées *échantillons*.

Les échantillons ne représentent chacun que l'état instantané du signal au moment de l'échantillonnage. Entre deux instants d'échantillonnage, le signal analogique peut continuer à évoluer. Comme après l'échantillonnage, seuls des valeurs individuelles, séparées dans le temps, sont disponibles, on qualifie le signal échantillonné de *à temps discret*.

La figure [ref:a_wertkont_zeitdisk] montre un tel signal idéalement échantillonné. Il est *à temps discret*, car seules des valeurs sont disponibles à des instants d'échantillonnage précis. Cependant, les échantillons individuels peuvent encore prendre n'importe quelles valeurs et sont donc *à valeurs continues*.

<margin>
[picture:408:a_wertkont_zeitkont:Signal à valeurs et temps continus]
[picture:409:a_wertkont_zeitdisk:Signal à valeurs continues et temps discret]
</margin>

[question:AF601]
[question:AF603]

L'opération par laquelle un signal à temps continu est échantillonné à des moments précis et transformé en un signal à temps discret est appelée *échantillonnage*.

[question:AF606]

La vitesse à laquelle l'échantillonnage d'un signal analogique est effectué est appelée *fréquence d'échantillonnage* ou *Abtastrate*. Elle indique combien d'échantillons sont prélevés par unité de temps, par exemple par seconde.

Les signaux audio analogiques sont par exemple échantillonnés à une fréquence d'échantillonnage de $\num{44100}$ échantillons par seconde (unité $\unit{\sps}$), ou $\qty{44,1}{\kilo\sps}$ pour faire court, sur des supports de données numériques comme les CDs.

[question:AF615]

---

Outre la résolution temporelle, la résolution des valeurs mesurées joue également un rôle dans la numérisation. Les signaux analogiques peuvent prendre n'importe quelles valeurs de tension et varier entre elles sans étapes fixes. C'est pourquoi on les qualifie de *à valeurs continues*.

Lors de la numérisation, en revanche, seul un nombre limité de valeurs numériques possibles est disponible. Une valeur de tension mesurée doit donc être attribuée à l'une de ces étapes fixes. Le signal devient alors *à valeurs discrètes*.

Si une valeur de signal analogique se situe entre deux étapes possibles, il faut décider à quelle étape la valeur mesurée sera attribuée. Cette opération est appelée *quantification*. Le signal précédemment à valeurs continues est ainsi mappé sur un nombre fini de valeurs possibles.

[question:AF605]

La figure [ref:a_wertdisk_zeitkont] montre, à titre d'illustration, un signal *à valeurs discrètes mais à temps continu*. Le signal reste défini à tout moment, mais ne peut prendre que certaines valeurs prédéfinies. Les valeurs possibles sont donc déjà quantifiées, mais le temps n'est pas encore discrétisé.

Lorsque l'échantillonnage et la quantification sont combinés, un signal *à valeurs et temps discrets* est créé, comme illustré dans la figure [ref:a_wertdisk_zeitdisk]. Seuls des échantillons sont disponibles à des moments précis, et leurs valeurs possibles sont également limitées à des étapes fixes. Cela correspond à la représentation numérique d'un signal précédemment analogique.

<tip>
Pour illustrer cela, on peut comparer un variateur analogique à un commutateur à gradins. Avec un variateur analogique, la luminosité d'une lampe peut être réglée de manière arbitrairement fine. Avec un commutateur à gradins, par exemple à $\num{5}$ niveaux, seuls $\num{5}$ valeurs de luminosité différentes sont disponibles. Les valeurs intermédiaires ne sont pas possibles.

Si l'on souhaite reproduire avec le commutateur à gradins une luminosité réglée avec le variateur analogique, il faut choisir le niveau le plus approprié. C'est exactement le principe de la quantification : une valeur continue est attribuée à l'une des plusieurs valeurs prédéfinies.
</tip>

<margin>
[picture:410:a_wertdisk_zeitkont:Signal à valeurs discrètes et temps continu]
[picture:411:a_wertdisk_zeitdisk:Signal à valeurs et temps discrets]
</margin>

[question:AF602]
[question:AF604]

<indepth>
Ici, il est possible d'essayer soi-même. Un signal sinusoïdal à temps continu est numérisé par un convertisseur analogique-numérique (CAN) puis reconverti en un signal analogique à temps continu, mais toujours à valeurs discrètes, par un convertisseur numérique-analogique (CNA). Les curseurs permettent de régler la quantification temporelle et la quantification des valeurs des convertisseurs CAN/CNA.

[include:quantisierung_und_sampling]
</indepth>