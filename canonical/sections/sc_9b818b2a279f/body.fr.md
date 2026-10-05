Dans cette section et la suivante, nous nous intéressons à deux circuits fondamentaux importants d'un transistor bipolaire. Nous examinons d'abord dans cette section le *montage à collecteur commun*, puis dans la section suivante le *montage à émetteur commun*. Les deux circuits sont représentés dans la figure [ref:a_emitter_collector]. Ils possèdent des propriétés différentes et sont donc utilisés pour diverses applications.

<margin>
[picture:1118:a_emitter_collector:Montage à émetteur commun et à collecteur commun avec désignations de la base (B), du collecteur (C) et de l’émetteur (E)]
</margin>

La désignation des circuits fondamentaux d'un transistor bipolaire est basée sur la borne qui ne sert ni d'entrée ni de sortie du circuit et constitue ainsi le point de référence commun pour le circuit d'entrée et de sortie. Pour le montage à collecteur commun, c'est le collecteur.

---

[question:AD401]

<tip>
Les circuits amplificateurs des transistors bipolaires sont nommés d'après la borne à laquelle ni l'entrée ni la sortie ne sont directement connectées (cf. figure [ref:a_emitter_collector]).
</tip>

Comme le collecteur est généralement connecté à la tension d'alimentation et se trouve approximativement à un potentiel fixe pour les tensions alternatives, la tension à l'émetteur suit la tension à la base. Le montage à collecteur commun est donc souvent appelé *émetteur suiveur*.

Si la tension d'entrée à la base augmente par exemple pendant une demi-onde positive, le courant d'émetteur augmente. Cela augmente la chute de tension sur la résistance d'émetteur et la tension de sortie augmente également. Le signal d'entrée et de sortie sont donc en phase ; le déphasage est de $\qty{0}{\degree}$.

[question:AD405]

---

La figure [ref:a_collector_circuit] montre un simple montage à collecteur commun avec alimentation électrique, résistance d'émetteur et condensateurs de couplage.

<margin>
[picture:140:a_collector_circuit:Montage à collecteur commun avec alimentation électrique, résistance d'émetteur et condensateurs de couplage]
</margin>

---

Pour fonctionner comme amplificateur de courant linéaire, le transistor dans le montage à collecteur commun nécessite un point de fonctionnement défini (angl. bias, polarisation), qui est normalement fixé par un diviseur de tension à la base.

La figure [ref:a_kennlinie] montre la caractéristique d'un transistor NPN avec le point de fonctionnement réglé par le diviseur de tension. La polarisation de base est choisie pour travailler sur la partie linéaire de la caractéristique d'entrée. Cela implique également qu'un certain courant de repos circule toujours, même en l'absence de signal d'entrée. Nous examinerons cela plus en détail dans le chapitre sur les classes d'amplificateurs.

Lorsqu'un signal d'entrée, par exemple une tension alternative sinusoïdale, est appliqué comme montré dans l'image, ce signal est amplifié par la caractéristique d'entrée. Notez ici l'étiquetage des axes, des microampères deviennent des milliampères. La tension résultante à la sortie peut également être lue sur cette caractéristique.

<margin>
[picture:1119:a_kennlinie:Caractéristique d'un transistor NPN avec point de fonctionnement et superposition de signal]
</margin>

La résistance d'émetteur convertit le courant qui traverse la jonction collecteur-émetteur en une chute de tension, qui est prélevée à l'émetteur. Le courant d'émetteur du transistor circule (avec la part généralement négligeable du courant de base) à travers l'émetteur et la résistance d'émetteur vers la masse. Le courant traversant la résistance d'émetteur provoque, par la chute de tension qui en résulte, une augmentation du potentiel de l'émetteur (tension d'émetteur) et agit ainsi comme une contre-réaction pour la tension de base. Cela stabilise en outre le point de fonctionnement du transistor, car les variations thermiques du courant de collecteur sont ainsi compensées.

Le couplage d'entrée et de sortie des signaux à la base et à l'émetteur se fait via des condensateurs de couplage. Leur rôle est d'empêcher les composantes de tension continue d'atteindre l'étage amplificateur, ce qui modifierait le point de fonctionnement.

Le condensateur de découplage dans la tension de service (+) sert à éliminer les signaux HF et BF indésirables, afin d'éviter les effets de rétroaction sur l'étage et la tension d'alimentation. De plus, le collecteur est connecté du point de vue du signal (pour la tension alternative) à l'entrée et à la sortie via le condensateur de découplage.

Le gain en tension du montage à collecteur commun se situe, avec une conception appropriée, dans la plage de $\num{0,9}$ à $\num{0,98}$ et est toujours légèrement inférieur à $1$.

On pourrait se demander quelle est l'utilité d'un amplificateur avec un gain en tension inférieur à $1$. Cependant, le montage à collecteur commun possède un avantage décisif, que nous examinons ci-dessous.

[question:AD402]

Le montage à collecteur commun possède un gain en courant significatif. Son impédance d'entrée est relativement élevée, car seul un faible courant peut circuler dans la base. En revanche, son impédance de sortie est relativement faible. Si la tension de sortie est modifiée par une charge connectée, cela change la tension base-émetteur et le transistor ajuste son courant d'émetteur pour contrer cette variation. Grâce à cette contre-réaction, le montage à collecteur commun peut piloter une charge de faible impédance sans que sa tension de sortie ne change beaucoup.

[question:AD403]

Pour cette raison, le montage à collecteur commun est souvent utilisé comme *étage tampon entre un oscillateur et d'autres parties du circuit*, qui chargeraient autrement l'oscillateur avec une faible impédance, afin d'obtenir un découplage et une meilleure stabilisation en fréquence de l'oscillateur.

[question:AD404]
