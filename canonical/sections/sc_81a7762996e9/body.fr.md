Les oscillateurs, en raison de la dépendance à la température des composants qu'ils utilisent, ont toujours une dépendance de la fréquence générée à la température ambiante. Les transistors et les diodes ont une dépendance relativement forte de leur caractéristique et de leur caractéristique à la température ambiante (facteur d'amplification, tension de seuil, capacités). De même, les paramètres électriques des composants passifs tels que les condensateurs, les résistances et en particulier les quartz oscillants dépendent de leur température ambiante.
Pour maintenir les oscillateurs dans une fréquence aussi stable que possible, il existe différentes possibilités techniques et physiques :
1. Tous les oscillateurs doivent toujours être aussi bien isolés thermiquement que possible des autres sources de chaleur dans les appareils.
2. Au lieu d'un oscillateur RC, LC ou VCO, il est préférable d'utiliser un oscillateur à quartz, car celui-ci est beaucoup plus stable en fréquence en raison de la haute qualité (Q) du quartz. Ce type d'oscillateur est appelé *XO* - Crystal oscillator. 
3. Utilisation d'un oscillateur à quartz et compensation des influences thermiques par l'utilisation de composants dans le circuit oscillateur, de sorte que les influences de la température s'annulent mutuellement dans la plage des températures de fonctionnement habituelles. Ce type d'oscillateur est appelé *TCXO* - Temperature compensated crystal oscillator
4. Stabilisation artificielle de la température ambiante d'un oscillateur à quartz par un réglage de la température au moyen d'un circuit thermostat et installation dans un boîtier thermiquement isolé ainsi qu'isolation par rapport aux sources de chaleur et de froid externes. Ce type d'oscillateur est appelé *OCXO* - Oven controlled crystal oscillator. L'OCXO a la plus haute stabilité de fréquence par rapport aux autres types d'oscillateurs.

En général, les oscillateurs stables en fréquence doivent toujours être aussi bien isolés thermiquement que possible des sources de chaleur et de froid internes et externes de l'appareil. Cela peut être réalisé, par exemple, par une distance aussi grande que possible par rapport aux sources de chaleur et de froid internes et externes ainsi que par les flux d'air.

[question:AF215]
[question:AD602]
[question:AD603]
[question:AD605]

En particulier lors du fonctionnement à des fréquences élevées, la stabilité de fréquence de l'oscillateur de référence des émetteurs-récepteurs, des transverters et des convertisseurs est très importante lors de l'utilisation de modes de fonctionnement sensibles aux écarts de fréquence. Pour atteindre les fréquences de sortie ou de réception élevées, une multiplication de fréquence de l'oscillateur de référence a lieu à l'intérieur de l'appareil. Les écarts de fréquence de l'oscillateur de référence agissent ainsi de manière multiplicative sur les fréquences d'émission ou de réception, ce qui peut entraîner des écarts de fréquence élevés et des instabilités de fréquence (par exemple, la dérive du signal émis ou reçu).
C'est pourquoi il faut toujours utiliser le meilleur type d'oscillateur disponible (par exemple, TCXO ou OCXO).

[question:AD604]