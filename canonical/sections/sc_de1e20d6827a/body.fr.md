Cette section montre comment les signaux analogiques sont convertis en valeurs numériques et comment les valeurs numériques sont reconverties en signaux analogiques. Pour cela, on utilise des *convertisseurs A/N* (convertisseurs analogique-numérique) et des *convertisseurs N/A* (convertisseurs numérique-analogique). Le schéma [ref:a_adc_dac] présente les schémas fonctionnels d'un convertisseur A/N et d'un convertisseur N/A.

<margin>
[picture:1130:a_adc_dac:Convertisseurs A/N et N/A]
</margin>

Un convertisseur A/N échantillonne un signal d'entrée analogique à des instants précis et génère à partir de celui-ci des valeurs numériques qui peuvent ensuite être traitées numériquement par d'autres parties d'un circuit.

Comme un convertisseur A/N ne fonctionne qu'avec un nombre limité de valeurs numériques possibles, il ne peut détecter l'amplitude d'un signal d'entrée analogique qu'à certaines étapes. Nous nous souvenons ici de l'exemple utilisé précédemment avec un variateur et un sélecteur de gradation. Si la valeur réelle se situe entre deux étapes possibles, elle doit être attribuée à l'une d'entre elles. Cela entraîne une *erreur de quantification*.

[question:AF607]

---

Le nombre d'étapes possibles d'un convertisseur A/N est appelé sa *résolution*. Elle est souvent indiquée en bits (unité : $\unit{\bit}$). Si un convertisseur peut par exemple distinguer $\num{256}$ valeurs différentes, il possède une résolution de $\qty{8}{\bit}$, car avec $\qty{8}{\bit}$, on peut représenter $\num{256}$ valeurs différentes. Un convertisseur $\qty{16}{\bit}$ peut déjà distinguer $\num{65536}$ valeurs différentes.

Pour les signaux qui peuvent prendre des valeurs positives et négatives, une partie de ces valeurs est typiquement utilisée pour la plage de signal positive et une autre partie pour la plage de signal négative.

Le schéma [ref:a_adc_4bit] montre un signal sinusoïdal qui a été numérisé par un convertisseur A/N avec une résolution de $\qty{4}{\bit}$ puis reconverti en un signal analogique. Le schéma [ref:a_adc_12bit] montre le même signal sinusoïdal, mais numérisé par un convertisseur A/N avec une résolution de $\qty{12}{\bit}$ puis reconverti en un signal analogique. On remarque clairement que les $\qty{8}{\bit}$ supplémentaires permettent une résolution bien plus fine (meilleure d'un facteur 256), de sorte que le signal reconstruit se rapproche déjà beaucoup du signal sinusoïdal d'origine.

<margin>
[picture:300:a_adc_4bit:Signal sinusoïdal numérisé par un convertisseur A/N 4 bits puis reconverti en analogique]
[picture:299:a_adc_12bit:Signal sinusoïdal numérisé par un convertisseur A/N 12 bits puis reconverti en analogique]
</margin>

[question:AF608]

Une autre propriété importante d'un convertisseur A/N est la précision temporelle de l'échantillonnage. Les différents échantillons doivent être prélevés aussi exactement que possible aux intervalles de temps prévus. Pour cela, un générateur d'horloge d'échantillonnage aussi stable que possible est nécessaire.

En pratique, les instants d'échantillonnage réels peuvent légèrement s'écarter des instants idéaux. Ces variations temporelles sont appelées *jitter*. Le jitter peut entraîner des erreurs supplémentaires et donc un bruit supplémentaire dans le signal numérisé. Le même mécanisme se produit du côté du convertisseur N/A. Là, le jitter entraîne un bruit supplémentaire dans le signal analogique.

[question:AF621]

---

Le pendant du convertisseur A/N est le *convertisseur N/A*. Il génère à partir d'un flux de données numériques ou d'échantillons numériques un signal analogique.

Un convertisseur N/A ne peut pas non plus produire des valeurs de sortie arbitrairement nombreuses. Comme pour le convertisseur A/N, il possède une résolution déterminée en bits et donc seulement un nombre fini de valeurs de sortie possibles.

Un convertisseur N/A ne peut en outre produire que des tensions dans une plage de valeurs déterminée, par exemple de $\qty{0}{\volt}$ à $\qty{1}{\volt}$ ou de $\qty{-2}{\volt}$ à $\qty{2}{\volt}$.

Dans le cas d'un convertisseur N/A fonctionnant de manière linéaire, les valeurs de sortie possibles sont réparties uniformément sur cette plage de tension. Si un convertisseur N/A possède par exemple une résolution de $\qty{4}{\bit}$, il dispose de

$\num{2^4}=\num{16}$

étapes possibles.

[question:AF609]

Si ces étapes sont réparties sur une plage de tension de $\qty{0}{\volt}$ à $\qty{1}{\volt}$, il y a $\num{15}$ pas entre les $\num{16}$ étapes. Le pas est donc de

$\frac{\qty{1}{\volt}}{16-1}\approx\qty{67}{\milli\volt}.$

[question:AF611]
[question:AF610]

---

Les convertisseurs A/N et N/A sont utilisés par exemple dans les récepteurs et émetteurs-récepteurs SDR. Les signaux d'entrée analogiques sont d'abord numérisés par un convertisseur A/N puis traités numériquement. Si un signal analogique doit en être issu, les valeurs numériques sont reconverties en valeurs de tension analogiques par un convertisseur N/A.

Il peut arriver qu'un signal d'entrée n'utilise qu'une petite partie de la plage de valeurs disponible d'un convertisseur A/N. Dans ce cas, seule une partie des étapes numériques disponibles est utilisée.

Inversement, un signal d'entrée peut dépasser la plage de valeurs maximale d'un convertisseur A/N. Les valeurs supérieures à la tension d'entrée maximale détectable ne peuvent alors plus être représentées correctement et ne sont affichées qu'avec la valeur maximale possible. Cet effet est appelé *écrêtage*. Dans l'évolution du signal, les zones concernées apparaissent alors coupées.

Un convertisseur N/A ne peut pas non plus produire de tension de sortie en dehors de sa plage de valeurs prévue.

Plus la résolution d'un convertisseur A/N ou N/A est élevée, plus les différentes valeurs d'amplitude peuvent être représentées numériquement ou reconverties en valeurs de tension analogiques de manière fine. Avec une faible résolution, il n'y a en revanche que peu d'étapes possibles, de sorte que les gradations sont plus visibles.

[question:AF613]
[question:AF612]
[question:AF614]