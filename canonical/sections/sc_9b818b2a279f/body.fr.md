Dans les deux prochains chapitres, nous allons nous pencher sur deux montages fondamentaux importants d’un transistor bipolaire. Dans ce chapitre, nous examinons d’abord le *montage à collecteur commun*, puis, dans le chapitre suivant, le *montage à émetteur commun*. Les deux circuits sont illustrés dans la figure [ref:a_emitter_collector]. Ils présentent des propriétés différentes et sont donc utilisés pour des applications distinctes.

<margin>
[picture:1118:a_emitter_collector:Montages à émetteur commun et à collecteur commun avec désignations de la base (B), du collecteur (C) et de l’émetteur (E)]
</margin>

Le nom des montages fondamentaux d’un transistor bipolaire est déterminé par la borne qui n’est ni l’entrée ni la sortie du circuit et qui sert donc de point de référence commun pour le circuit d’entrée et le circuit de sortie. Dans le montage à collecteur commun, il s’agit du collecteur.

---

[question:AD401]


<tip>
Les circuits amplificateurs à transistors bipolaires sont nommés d’après la borne à laquelle ni l’entrée ni la sortie ne sont directement connectées (cf. figure [ref:a_emitter_collector]).
</tip>

Puisque le collecteur est généralement relié à l’alimentation électrique et se trouve approximativement à un potentiel fixe pour les tensions alternatives, la tension à l’émetteur suit celle de la base. C’est pourquoi le montage à collecteur commun est souvent appelé *émetteur suiveur*.


Si la tension d’entrée à la base augmente, par exemple pendant une demi-onde positive, le courant d’émetteur augmente. La chute de tension aux bornes de la résistance d’émetteur s’accroît alors, et la tension de sortie augmente également. Les signaux d’entrée et de sortie sont donc en phase ; le déphasage est de $\qty{0}{\degree}$.


[question:AD405]


---

La figure [ref:a_collector_circuit] montre un montage à collecteur commun simple avec alimentation électrique, résistance d’émetteur et condensateurs de couplage.


<margin>
[picture:140:a_collector_circuit:Montage à collecteur commun avec alimentation électrique, résistance d’émetteur et condensateurs de couplage]
</margin>

---

Pour fonctionner en amplificateur linéaire de courant, le transistor dans le montage à collecteur commun nécessite un point de fonctionnement défini (polarisation en anglais), généralement établi par un diviseur de tension à la base.


La figure [ref:a_kennlinie] montre la caractéristique d’un transistor NPN avec le point de fonctionnement réglé par le diviseur de tension. La tension de polarisation de la base est choisie de manière à travailler sur la partie linéaire de la courbe d’entrée. Cela implique également qu’un certain courant de repos circule même en l’absence de signal d’entrée. Nous examinerons ce point plus en détail dans le chapitre consacré aux classes d’amplification.


Si un signal d’entrée, par exemple une tension alternative sinusoïdale, est appliqué comme indiqué sur l’image, ce signal est amplifié par la courbe d’entrée. On remarquera la graduation des axes : les microampères deviennent des milliampères. La tension de sortie résultante peut également être lue sur cette courbe.


<margin>
[picture:1119:a_kennlinie:Caractéristique d’un transistor NPN avec point de fonctionnement et superposition du signal]
</margin>

La résistance d’émetteur convertit le courant circulant dans la jonction collecteur-émetteur en une chute de tension mesurée à l’émetteur. Le courant d’émetteur du transistor (en négligeant généralement la faible partie du courant de base) traverse la résistance d’émetteur vers la masse. Le courant traversant la résistance d’émetteur provoque, par la chute de tension qui en résulte, une augmentation du potentiel de l’émetteur (tension d’émetteur) et agit ainsi comme une contre-réaction sur la tension de base. Cela contribue à stabiliser davantage le point de fonctionnement du transistor, car les variations thermiques du courant de collecteur sont ainsi compensées.


L’injection et l’extraction des signaux à la base et à l’émetteur s’effectuent via des condensateurs de couplage. Leur rôle est d’empêcher les composantes continues de la tension d’atteindre l’étage amplificateur et de modifier ainsi le point de fonctionnement.


Le condensateur de découplage sur l’alimentation (+) sert à évacuer les signaux HF et BF indésirables afin d’éviter les effets de réaction sur l’étage et l’alimentation. De plus, le collecteur est mis au même potentiel que l’entrée et la sortie pour les signaux alternatifs grâce au condensateur de découplage.


Le gain en tension du montage à collecteur commun, pour une conception appropriée, se situe entre $\num{0,9}$ et $\num{0,98}$ et reste toujours inférieur à $1$.


On pourrait se demander quel est l’intérêt d’un amplificateur dont le gain en tension est inférieur à $1$. Cependant, le montage à collecteur commun présente un avantage décisif, que nous allons examiner maintenant.


[question:AD402]


Le montage à collecteur commun offre un gain en courant marqué. Son impédance d’entrée est relativement élevée, car seul un faible courant peut circuler dans la base. En revanche, son impédance de sortie est relativement faible. Si la tension de sortie est modifiée par une charge connectée, la tension base-émetteur varie et le transistor ajuste son courant d’émetteur pour contrer cette variation. Grâce à cette contre-réaction, le montage à collecteur commun peut piloter une charge de faible impédance sans que sa tension de sortie ne varie fortement.


[question:AD403]


C’est pourquoi le montage à collecteur commun est souvent utilisé comme *étage tampon entre un oscillateur et d’autres parties du circuit* qui, autrement, chargeraient l’oscillateur de manière basse impédance, assurant ainsi un découplage et une meilleure stabilité en fréquence de l’oscillateur.


[question:AD404]