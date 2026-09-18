La fréquence d'un oscillateur dépend toujours de la température ambiante, car les caractéristiques des composants utilisés varient avec la température. Pour les transistors et les diodes, cela concerne par exemple le facteur d'amplification, la tension de seuil et les capacités. Même les composants passifs comme les condensateurs, les résistances et en particulier les oscillateurs à quartz présentent des propriétés électriques dépendant de la température.

Pour maintenir la fréquence d'un oscillateur aussi stable que possible, il doit être bien isolé thermiquement des autres sources de chaleur ou de froid dans l'appareil. Cela peut être réalisé, par exemple, en le plaçant à une distance suffisante des sources internes et externes de chaleur ou de froid ainsi que des courants d'air. De plus, un oscillateur à quartz est à privilégier par rapport à un oscillateur RC, LC ou VCO, car il offre une stabilité de fréquence bien supérieure grâce à la haute qualité du quartz.

[question:AF215]

Il existe différents types d'oscillateurs à quartz, qui diffèrent par leur stabilité en fréquence :

* L'oscillateur à quartz le plus simple (voir figure [ref:a_xo]) est appelé *XO*, abréviation de *Crystal Oscillator*.
* Un *TCXO* (*Temperature Compensated Crystal Oscillator*) compense les effets de la température à l'aide de composants supplémentaires dans le circuit de l'oscillateur, de sorte que leurs effets dépendant de la température s'annulent largement dans la plage de température de fonctionnement habituelle.
* Un *OCXO* (*Oven-Controlled Crystal Oscillator*) stabilise la température de l'oscillateur à quartz à l'aide d'un chauffage régulé. Pour cela, l'oscillateur est placé dans un boîtier thermiquement isolé, qui le protège largement des influences thermiques externes. Parmi les types d'oscillateurs mentionnés, l'OCXO offre la plus grande stabilité de fréquence.

<margin>
[photo:333:a_xo:Oscillateur à quartz XO à $\qty{433,75}{\mega\hertz}$]
[photo:337:a_ocxo:Oscillateur à quartz OCXO à $\qty{10}{\mega\hertz}$]
</margin>

[question:AD602]
[question:AD603]
[question:AD605]

En particulier lors de l'utilisation de procédés de transmission sensibles aux écarts de fréquence, la stabilité en fréquence de l'oscillateur de référence des émetteurs-récepteurs, des transverters et des convertisseurs est très importante, surtout pour les fréquences élevées. Pour atteindre les fréquences de sortie ou de réception élevées, une multiplication de fréquence de l'oscillateur de référence est effectuée en interne dans l'appareil. Ainsi, les écarts de fréquence de l'oscillateur de référence se répercutent de manière multiplicative sur les fréquences d'émission ou de réception, ce qui peut entraîner des écarts et des instabilités de fréquence élevés (par exemple, dérive du signal d'émission ou de réception). C'est pourquoi, sur la bande des $\qty{3}{\centi\mètre}$ (soit $\qty{10}{\giga\hertz}$), il est recommandé d'utiliser au moins un TCXO.

[question:AD604]