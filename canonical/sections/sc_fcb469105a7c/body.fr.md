Dans la section précédente, nous avons découvert le [sec:kollektorschaltung] d'un transistor bipolaire. Dans cette section, nous examinons le *montage à émetteur commun*.

<margin>
[picture:1118:a_emitter_collector:Montage à émetteur commun et à collecteur commun avec désignations base (B), collecteur (C) et émetteur (E)]

Résumons brièvement les propriétés des montages à collecteur commun et à émetteur commun dans le tableau suivant :

| l: Propriété | X: Montage à émetteur commun | X: Montage à collecteur commun |
| Déphasage | $\qty{180}{\degree}$ | $\qty{0}{\degree}$ |
| Gain en tension | $\num{100}\dots\num{300}$ | $\num{0,9}\dots\num{0,98}$ |
| Impédance d'entrée | élevée | élevée |
| Impédance de sortie | élevée | faible |
</margin>

Comme nous l'avons appris dans la section précédente, la désignation des circuits de base d'un transistor bipolaire dépend de la borne qui ne sert ni d'entrée ni de sortie du circuit et constitue ainsi le point de référence commun pour le circuit d'entrée et de sortie. Dans le montage à émetteur commun, c'est l'émetteur.

---

[question:AD409]

<tip>
Les circuits amplificateurs des transistors bipolaires sont nommés d'après la borne à laquelle ni l'entrée ni la sortie ne sont directement connectées (cf. figure [ref:a_emitter_collector]).
</tip>

---

La figure [ref:a_emitterschaltung] montre un simple montage à émetteur commun avec alimentation électrique, résistance de collecteur et condensateurs de couplage.

Pour fonctionner comme un amplificateur de tension linéaire, le transistor en montage à émetteur commun nécessite un point de fonctionnement défini (anglais : bias, polarisation), qui est normalement fixé par un diviseur de tension à la base.

<margin>
[picture:136:a_emitterschaltung:Montage à émetteur commun]
</margin>

[question:AD411]

La résistance de collecteur convertit le courant qui traverse la jonction collecteur-émetteur en une chute de tension, qui est prélevée au collecteur. Le courant de collecteur du transistor circule (avec la part généralement négligeable du courant de base) via l'émetteur à travers la résistance d'émetteur vers la masse. Le courant traversant la résistance d'émetteur provoque, par la chute de tension qui en résulte à ses bornes, une augmentation du potentiel de l'émetteur (tension d'émetteur) et agit ainsi comme une contre-réaction pour la tension de base. Ceci stabilise en outre le point de fonctionnement du transistor, car les variations thermiques du courant de collecteur sont ainsi compensées.

Le couplage d'entrée et de sortie des signaux à la base et au collecteur s'effectue via des condensateurs de couplage. Leur tâche est d'empêcher les composantes de tension continue d'atteindre l'étage amplificateur, ce qui modifierait le point de fonctionnement.

[question:AD412]

Le condensateur de découplage dans la tension de service (+) sert à évacuer les signaux HF et BF indésirables, afin d'éviter les effets de rétroaction sur l'étage et la tension d'alimentation.

Le déphasage entre le signal d'entrée et le signal de sortie est de $\qty{180}{\degree}$ dans le montage à émetteur commun, car lors d'une demi-onde positive dans la tension d'entrée à la base, le courant de collecteur augmente et donc la chute de tension aux bornes de la résistance de collecteur augmente. Ceci fait baisser la tension aux bornes du condensateur de sortie. Il en résulte une demi-onde négative à la sortie de l'étage amplificateur.

[question:AD407]
[question:AD408]

Le gain en tension du montage à émetteur commun, avec une conception appropriée, se situe dans la plage de $100\dots 300$ et est donc très élevé par rapport au montage à collecteur commun.

[question:AD410]

Le condensateur à l'émetteur court-circuite la résistance d'émetteur pour les tensions alternatives, ce qui réduit la contre-réaction et augmente le gain en tension alternative, tandis que le point de fonctionnement en courant continu reste inchangé.

[question:AD413]

Cependant, si le condensateur d'émetteur est retiré, le facteur d'amplification du circuit diminue considérablement (par exemple, de $\num{100}$ à $\num{10}$). Il est finalement défini uniquement par le rapport entre la résistance de collecteur et la résistance d'émetteur.

[question:AD414]
[question:AD415]

Si un montage à émetteur commun est exploité sans préréglage du point de fonctionnement par un diviseur de tension, comme dans la question suivante, la commande du transistor s'effectue uniquement par le signal d'entrée appliqué. Ce n'est que lorsque ce signal dépasse environ $\qty{0,6}{\volt}$ que la jonction base-émetteur du transistor devient conductrice. Ainsi, un courant de collecteur ne circule que pendant les pics de tension, provoquant une chute de tension à la sortie. Comme signal de sortie, la tension d'alimentation apparaît, qui chute aux moments où le transistor entre dans la région conductrice. C'est ainsi que s'explique le signal de sortie correspondant.

[question:AD406]
