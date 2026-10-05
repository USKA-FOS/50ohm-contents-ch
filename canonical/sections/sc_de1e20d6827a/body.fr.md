Cette section montre comment les signaux analogiques sont convertis en valeurs numériques et les valeurs numériques en signaux analogiques. Pour cela, on utilise des *convertisseurs A/N* (analogique-numérique) et des *convertisseurs N/A* (numérique-analogique). La figure [ref:a_adc_dac] montre les schémas fonctionnels d'un convertisseur A/N et d'un convertisseur N/A.

<margin>
[picture:1130:a_adc_dac:Convertisseurs A/N et N/A]
</margin>

Un convertisseur analogique échantillonne un signal d'entrée analogique à des instants précis et en génère des valeurs numériques, qui peuvent ensuite être traitées numériquement par d'autres parties d'un circuit.

Comme un convertisseur analogique ne fonctionne qu'avec un nombre limité de valeurs numériques possibles, il ne peut capturer l'amplitude d'un signal d'entrée analogique que par paliers spécifiques. Nous nous rappelons ici de l'exemple utilisé précédemment dans la section [sec:sampling_quantisierung] avec le variateur et le commutateur à gradins. Si la valeur réelle se situe entre deux paliers possibles, elle doit être attribuée à l'un d'eux. Cela crée une *erreur de quantification*.

[question:AF607]

---

Le nombre de paliers possibles d'un convertisseur analogique est appelé sa *résolution*. Elle est souvent indiquée en bits (unité : $\unit{\bit}$). Par exemple, si un convertisseur peut distinguer $\num{256}$ valeurs différentes, il a une résolution de $\qty{8}{\bit}$, car avec $\qty{8}{\bit}$, on peut représenter $\num{256}$ valeurs différentes. Un convertisseur $\qty{16}{\bit}$ peut déjà distinguer $\num{65536}$ valeurs différentes.

Pour les signaux pouvant prendre à la fois des valeurs positives et négatives, une partie de ces valeurs est typiquement utilisée pour la plage de signaux positifs et une autre pour la plage de signaux négatifs.

La figure [ref:a_adc_4bit] montre un signal sinusoïdal numérisé par un convertisseur analogique avec une résolution de $\qty{4}{\bit}$ puis reconverti en un signal analogique. La figure [ref:a_adc_12bit] montre le même signal sinusoïdal, mais numérisé par un convertisseur analogique avec une résolution de $\qty{12}{\bit}$ puis reconverti en un signal analogique. On voit clairement que les $\qty{8}{\bit}$ supplémentaires conduisent à une résolution beaucoup plus fine (256 fois meilleure), de sorte que le signal reconstruit se rapproche déjà beaucoup du signal sinusoïdal original.

<margin>
[picture:300:a_adc_4bit:Signal sinusoïdal numérisé par un convertisseur A/N 4 bits et conversion N/A ultérieure]
[picture:299:a_adc_12bit:Signal sinusoïdal numérisé par un convertisseur A/N 12 bits et conversion N/A ultérieure]
</margin>

[question:AF608]

Une autre propriété importante d'un convertisseur analogique est la précision temporelle de l'échantillonnage. Les échantillons individuels doivent être pris aussi exactement que possible aux intervalles de temps prévus. Pour cela, un générateur d'horloge d'échantillonnage aussi stable que possible est nécessaire.

En pratique, les instants d'échantillonnage réels peuvent cependant légèrement s'écarter des instants idéaux. Ces fluctuations temporelles sont appelées *jitter*. Le jitter peut entraîner des erreurs supplémentaires et donc un bruit supplémentaire dans le signal numérisé. Le même mécanisme se produit du côté du convertisseur numérique. Là, le jitter entraîne un bruit supplémentaire dans le signal analogique.

[question:AF621]

---

L'opposé du convertisseur analogique est le *convertisseur numérique*. Il génère à partir d'un flux de données numériques ou d'échantillons numériques un signal analogique.

Un convertisseur numérique ne peut pas non plus générer un nombre arbitraire de valeurs de sortie différentes. Comme pour le convertisseur analogique, il possède une certaine résolution en bits et donc seulement un nombre fini de valeurs de sortie possibles.

Un convertisseur numérique ne peut également générer que des tensions dans une plage de valeurs spécifique, par exemple de $\qty{0}{\volt}$ à $\qty{1}{\volt}$ ou de $\qty{-2}{\volt}$ à $\qty{2}{\volt}$.

Pour un convertisseur numérique fonctionnant linéairement, les valeurs de sortie possibles sont réparties uniformément sur cette plage de tension. Par exemple, si un convertisseur numérique a une résolution de $\qty{4}{\bit}$, il dispose de

$\num{2^4}=\num{16}$

paliers possibles.

[question:AF609]

Si ceux-ci sont répartis sur une plage de tension de $\qty{0}{\volt}$ à $\qty{1}{\volt}$, il y a au total $\num{15}$ pas intermédiaires entre les $\num{16}$ paliers. Le pas est donc de

$\frac{\qty{1}{\volt}}{16-1}\approx\qty{67}{\milli\volt}.$

[question:AF611]
[question:AF610]

---

Les convertisseurs A/N et N/A sont utilisés, par exemple, dans les récepteurs et émetteurs-récepteurs SDR. Les signaux d'entrée analogiques sont d'abord numérisés par un convertisseur analogique puis traités numériquement. Pour en refaire un signal analogique, les valeurs numériques sont reconverties en valeurs de tension analogiques à l'aide d'un convertisseur numérique.

Il peut arriver qu'un signal d'entrée n'utilise qu'une petite partie de la plage de valeurs disponible d'un convertisseur analogique. Dans ce cas, seule une partie des paliers numériques disponibles est utilisée.

Inversement, un signal d'entrée peut dépasser la plage de valeurs maximale d'un convertisseur analogique. Les valeurs supérieures à la tension d'entrée maximale détectable ne peuvent alors plus être représentées correctement et ne sont plus mappées qu'avec la valeur maximale possible. Cet effet est appelé *écrêtage*. Dans l'évolution du signal, les zones concernées apparaissent ainsi tronquées.

Un convertisseur numérique ne peut pas non plus générer une tension de sortie en dehors de sa plage de valeurs prévue.

Plus la résolution d'un convertisseur A/N ou N/A est élevée, plus les différentes valeurs d'amplitude peuvent être représentées numériquement ou reconverties en valeurs de tension analogiques de manière fine. Avec une faible résolution, en revanche, seuls quelques paliers possibles sont disponibles, de sorte que les gradations deviennent plus visibles.

[question:AF613]
[question:AF612]
[question:AF614]
