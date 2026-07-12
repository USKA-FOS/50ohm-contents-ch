Un relais radio permet une portée plus grande que celle possible entre deux stations radioamateurs en liaison directe. Les relais radio sont généralement installés à des endroits exposés, par exemple sur des sommets de montagnes, des gratte-ciels, des clochers et autres tours. Il existe également des relais radio dans des satellites en orbite autour de la Terre. La structure et la fonction d'une telle station radio sont représentées dans l'image [ref:n_relaisfunkstellen_aufbau].

[picture:648:n_relaisfunkstellen_aufbau:Représentation schématique d'un relais radio avec des utilisateurs]

Par exemple, si une montagne se trouve entre deux stations radio, il est impossible d'émettre à travers la montagne. Un relais radio sur le sommet de la montagne permet néanmoins d'établir une liaison, car les deux stations peuvent atteindre le relais directement.

Les relais radio sont également appelés brièvement relais ou répéteurs. On peut les reconnaître au fait qu'ils émettent régulièrement leur indicatif. L'indicatif d'un relais radio commence généralement par DB0, DM0 ou DO0 selon le [plan d'indicatifs](https://50ohm.de/rzp).

La définition officielle des répéteurs est un peu plus sèche : *"Relais radio" : une station radioamateur télécommandée (également dans des satellites), qui émet des émissions radioamateurs reçues, des parties de celles-ci ou d'autres signaux injectés ou mémorisés, déclenchés à distance, et sert à augmenter la portée des stations radioamateurs*

La question suivante sur cette définition peut également être résolue par exclusion, si l'on sait ce qui suit :
* Les relais radio ne sont pas exploités avec des indicatifs personnels.
* Les relais radio ne sont généralement pas occupés en permanence.
* Les relais radio n'ont pas besoin d'être exploités à des endroits géographiquement exposés.

[question:VN007]

[question:VD118]

---

Un relais radio reçoit sur sa fréquence d'entrée le signal d'une station radioamateur et l'émet simultanément sur sa fréquence de sortie. Afin que l'émetteur du relais radio ne perturbe pas son propre récepteur, les fréquences d'émission et de réception sont généralement différentes. L'écart entre les fréquences d'émission et de réception est appelé décalage de fréquence ou simplement décalage. Les décalages généralement utilisés en Allemagne se trouvent dans le tableau [ref:n_relaisfunkstellen_ablage].

<margin>
| r: Bande | X: Décalage |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Décalage de fréquence]
</margin>

Par exemple, la fréquence d'un relais de $\qty{70}{\centi\meter}$ est indiquée comme suit :
* Fréquence d'entrée : $\qty{431,275}{\mega\hertz}$
* Décalage : $\qty{+7,600}{\mega\hertz}$
* Fréquence de sortie : $\qty{438,875}{\mega\hertz}$

[question:BE401]
[question:BE402]
[question:BE403]

<indepth>
Certaines stations relais fonctionnent également en mode dit *Crossband*. Cela signifie qu'une station émet et reçoit sur une bande (par exemple $\qty{70}{\centi\meter}$), une autre station sur le même relais, mais sur une autre bande (par exemple $\qty{2}{\meter}$). Le contrôle du relais transmet les conversations sur les deux bandes. Une conversion du mode d'émission peut également être effectuée, par exemple de SSB à FM.
</indepth>

Une station relais qui transmet non pas de la voix mais des données est appelée Digipeater. Un Digipeater est capable de recevoir et de retransmettre des paquets de données. La particularité ici est que l'émission ne peut se faire qu'en partie ou de manière décalée dans le temps. De même, les paquets de données peuvent être répétés ou certains champs de données modifiés.

[question:NF118]

---

Avant de pouvoir commencer à émettre via un relais radio, il faut connaître ses particularités techniques et ses paramètres. Pour certains relais, en plus de la fréquence, d'autres réglages sur votre émetteur-récepteur sont nécessaires pour garantir un fonctionnement sans perturbation. En plus de la FM analogique (Modulation de fréquence), des procédés numériques, comme par exemple DMR et D-Star, sont utilisés comme procédés de transmission vocale.

<tip>
Des informations sur les relais radio ainsi que sur les paramètres et particularités techniques peuvent être obtenues auprès de l'association locale DARC la plus proche, de la personne responsable du relais ou sur Internet.
</tip>

[question:NE309]
[question:NE308]

Un réglage important est la largeur de bande du canal en mode FM. Nous nous en souvenons : la largeur de bande indique combien de "place" on occupe dans le spectre de fréquences avec l'émission. Il existe d'une part le Wide-FM, dont la largeur de bande est de $\qty{25}{\kilo\hertz}$ et qui est affiché à l'écran par exemple sous la forme *FM-W*. D'autre part, il existe le FM à bande étroite (Narrow-FM), qui occupe une largeur de bande de seulement $\qty{12,5}{\kilo\hertz}$ et est affiché par exemple sur l'appareil radio sous la forme *FM-N*. De nombreux répéteurs n'aiment pas que les signaux soient trop larges. En effet, cela peut entraîner des signaux déformés et perturber les fréquences de relais voisines.

[question:BE407]
[question:BE417]

Le fonctionnement radio via des stations radioamateurs télécommandées est en principe autorisé pour tous les radioamateurs ayant un indicatif attribué. Pour garantir un fonctionnement sans perturbation, l'exploitant peut toutefois exclure d'autres radioamateurs de l'utilisation de la station radioamateur. La BNetzA doit en être informée.

[question:VD504]

Lors du fonctionnement radio via des stations relais, les passages doivent être aussi courts que possible afin que les stations mobiles et portables puissent utiliser le relais plus facilement, en particulier si elles ne se trouvent que temporairement dans la zone de réception. Entre les passages, il faut faire une pause pour permettre à d'autres stations de s'annoncer.

[question:BE406]
[question:BE404]

En cas de double entrée vocale de deux stations différentes, l'émission du relais est perturbée jusqu'à devenir illisible. Pour éviter ce double passage, il faut toujours procéder à un transfert correct entre les utilisateurs du répéteur. Cela signifie également de ne commencer l'émission que lorsque la station précédente a terminé son émission.

[question:NE310]
[question:BE405]

Dans l'installation déjà discutée 1 de l'AFuV, on trouve également des prescriptions pour les puissances d'émission des stations relais. Au-dessus de 30 MHz, une station fonctionnant automatiquement peut être exploitée avec une puissance maximale de 50 W ERP.

[question:VD503]

Il existe une particularité dans l'évaluation d'une liaison radio via une station relais radio. Comme l'intensité du signal avec laquelle on reçoit le partenaire radio est l'intensité du signal de la station relais et non l'intensité du signal du partenaire radio, on renonce à son indication. Dans le rapport, seule la lisibilité (R) est évaluée.

[question:BE408]
