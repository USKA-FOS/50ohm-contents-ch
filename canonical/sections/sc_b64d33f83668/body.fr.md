Un relais permet une portée plus grande que ce qui est souvent possible avec une liaison directe entre deux stations de radioamateurisme. Les relais sont généralement installés sur des sites exposés, par exemple sur des sommets de montagnes, des gratte-ciel, des clochers d'églises et d'autres tours. Il existe également des relais dans des satellites qui tournent autour de la Terre.

La structure et la fonction d'un relais terrestre sont représentées schématiquement dans l'image [ref:n_relaisfunkstellen_aufbau]. L'émission et la réception se font sur des fréquences différentes. L'exemple numérique provient du relais sur l'Üetliberg.

<margin>
[picture:648:n_relaisfunkstellen_aufbau:Représentation schématique d'une station relais avec des utilisateurs]
</margin>

S'il y a par exemple une montagne entre deux stations radio, il est impossible d'émettre à travers la montagne. Un relais au sommet de la montagne permet néanmoins d'établir une liaison, car les deux stations peuvent atteindre directement le relais.

L'image [ref:nea_linkstrecken_antenne_Pilatus] montre le montage d'une antenne de liaison montante sur le campus de Windisch pour le relais Pilatus du [groupe UHF](https://hb9uf.ch) de l'USKA.

</tip>

---

<margin>
[photo:1000:nea_linkstrecken_antenne_Pilatus:Travaux de maintenance sur le campus de Windisch, HB9DWW et HB9ZGF lors du montage de l'antenne de liaison montante "Echolink" pour le relais Pilatus]
</margin>

---

<law>
Lien direct vers la page de déclaration dans [eGov](https://www.egov.swiss/de/amateurfunk/spezielle-frequenznutzung-detail)

[Fiche d'information sur le radioamateurisme](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) 1.7
</law>


En Suisse, seules les associations de radioamateurisme sont autorisées à exploiter des stations non surveillées, y compris les relais.

Les associations de radioamateurisme qui souhaitent installer une station non surveillée sont soumises à l'obligation de déclaration auprès de l'OFCOM (enregistrement). Cette déclaration doit être obtenue auprès de l'OFCOM avant la mise en service.
Pour garantir une utilisation sans interférence des fréquences de l'installation non surveillée, il est recommandé d'effectuer au préalable une coordination des fréquences. Pour cela, vous pouvez contacter l'USKA [Contact :](qrg@uska.ch), qui vous soutiendra sur une base volontaire
%TODO: Corriger le lien USKA

dans cette démarche. Ensuite, vous pouvez effectuer la déclaration auprès de l'OFCOM via le portail eGov.
% Cela devrait-il être sur la "page d'information introductive" ?
[question:VN007]



L'indicatif d’appel d'un relais commence généralement par DB0, DM0 ou DO0 selon le [plan des indicatifs](https://50ohm.de/rzp).

%TODO: Helvétiser le plan des indicatifs

La définition officielle des répéteurs se lit de manière un peu plus aride : *"Station relais" : une station de radioamateurisme télécommandée (également dans des satellites), qui émet à distance des émissions de radioamateurisme reçues, des parties de celles-ci ou d'autres signaux injectés ou stockés, et sert ainsi à augmenter l'accessibilité des stations de radioamateurisme.*
La question suivante sur cette définition peut également être résolue par la méthode d'exclusion, si l'on sait ceci :
* Les relais ne sont pas exploités avec des indicatifs d’appel personnels.
* Les relais ne sont généralement pas occupés en permanence.
* Les relais ne doivent pas nécessairement être exploités à des emplacements géographiquement exposés.
[question:VD118]
% Existe-t-il une base juridique HB pour cela ?

---
% Est-ce correct avec le "décalage". Existe-t-il une telle liste pour la Suisse ? Le tableau NE-4.9.2 est-il correct ?
Les relais sont également appelés répéteurs ou stations relais. On peut les reconnaître au fait qu'ils émettent régulièrement leur indicatif d’appel.

Un relais reçoit sur sa fréquence d'entrée le signal d'une station de radioamateurisme et l'émet simultanément sur sa fréquence de sortie. Pour que l'émetteur du relais n'interfère pas avec son propre récepteur, les fréquences d'émission et de réception sont généralement différentes. L'écart entre la fréquence d'émission et la fréquence de réception est appelé décalage de fréquence ou simplement décalage. Les décalages couramment utilisés en Allemagne se trouvent dans le tableau [ref:n_relaisfunkstellen_ablage].

<margin>
| r: Bande | X: Décalage |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Décalage de fréquence]
</margin>

Par exemple, la fréquence d'un relais $\qty{70}{\centi\meter}$ est indiquée comme suit :
* Fréquence d'entrée : $\qty{431,275}{\mega\hertz}$
* Décalage : $\qty{+7,600}{\mega\hertz}$
* Fréquence de sortie : $\qty{438,875}{\mega\hertz}$

[question:BE401]
[question:BE402]
[question:BE403]

<indepth>
Certains relais fonctionnent également en mode dit *crossband*. Cela signifie : une station émet et reçoit sur une bande (par exemple $\qty{70}{\centi\meter}$), une autre station sur le même relais, mais sur une autre bande (par exemple $\qty{2}{\meter}$). Le contrôleur du relais achemine les conversations sur les deux bandes. Une conversion du mode d'émission peut également avoir lieu, par exemple de SSB vers FM.
</indepth>

Un relais qui transmet des données plutôt que de la parole est appelé digipeater. Un digipeater est capable de recevoir et de réémettre des paquets de données. La particularité ici est que l'émission peut se faire partiellement ou avec un décalage temporel. De même, les paquets de données peuvent être répétés ou des champs de données individuels peuvent être modifiés.

[question:NF118]

---

Avant de pouvoir commencer à utiliser un relais, il faut connaître ses particularités et paramètres techniques. Pour certains relais, en plus de la fréquence, des réglages supplémentaires sur son propre émetteur-récepteur sont nécessaires pour garantir un fonctionnement sans interférence. Outre la FM analogique (modulation de fréquence), des procédés numériques tels que DMR et D-Star sont également utilisés comme méthodes de transmission de la parole.

<tip>
Les informations sur les relais ainsi que les paramètres techniques et particularités sont disponibles auprès de la section locale DARC la plus proche, de la personne responsable du relais ou sur Internet.
</tip>
% Où les obtenir en Suisse ? USKA ? https://uska.ch/bandplan/ (Attention, reconstruction du site web de l'USKA en septembre 26)
[question:NE309]
[question:NE308]

Un réglage important est la largeur de bande du canal en mode FM. Rappelons-nous : la bande passante indique la "place" occupée dans le spectre des fréquences par l'émission. Il y a d'une part le FM large, dont la bande passante est de $\qty{25}{\kilo\hertz}$ et qui est affichée par exemple sous la forme *FM-W*. D'autre part, il y a le FM à bande étroite (Narrow-FM), qui occupe une bande passante de seulement $\qty{12,5}{\kilo\hertz}$ et est affiché par exemple sur l'appareil radio sous la forme *FM-N*. De nombreux répéteurs n'aiment pas du tout que les signaux soient trop larges. Car cela peut entraîner des signaux déformés et interférer avec les fréquences des relais voisins.
% Explication supplémentaire nécessaire pour 25kHz. FRV voulait absolument la question.
[question:BE407]
[question:BE417]

L'exploitation radio via des stations de radioamateurisme télécommandées est en principe autorisée à tous les radioamateurs disposant d'un indicatif d’appel attribué. Pour garantir un fonctionnement sans interférence, l'exploitant peut toutefois exclure d'autres radioamateurs de l'utilisation de la station de radioamateurisme.
%Le BNetzA doit en être informé.
[question:VD504]
% Existe-t-il une base juridique HB ? Laisser le texte dans la mesure où il est pertinent ?

Lors de l'exploitation radio via des stations relais, les transmissions doivent être aussi courtes que possible, afin que les stations mobiles et portables puissent utiliser plus facilement le relais, en particulier si elles ne se trouvent que temporairement dans la zone de réception. Entre les transmissions, il convient de faire une pause pour permettre à d'autres stations de s'annoncer.

[question:BE406]
[question:BE404]

En cas d'entrée vocale simultanée de deux stations différentes, l'émission du relais est perturbée jusqu'à devenir illisible. Pour éviter ce qu'on appelle le *doublage*, une transmission correcte entre les utilisateurs du répéteur doit toujours avoir lieu. Cela signifie également ne commencer à émettre que lorsque la station précédente a terminé son émission.

---
<indepth>
Expliquer la transmission correcte.
</indepth>
%Todo Remplir la marge de manière pertinente

[question:NE310]
[question:BE405]


Il y a une particularité dans l'évaluation d'une liaison radio via une station relais. Comme l'intensité du signal avec laquelle on reçoit le correspondant radio est l'intensité du signal de la station relais et non celle du correspondant radio, on renonce à l'indiquer. Dans le rapport, seule la lisibilité (R) est évaluée.

---
<indepth>
Expliquer le rapport sur relais avec un exemple.
</indepth>
%Todo Remplir la marge de manière pertinente

[question:BE408]


Dans l'annexe 1 de l'AFuV déjà évoquée, on trouve également des prescriptions pour les puissances d'émission des stations relais. Au-dessus de 30 MHz, une station fonctionnant automatiquement peut être exploitée avec une puissance maximale de 50 W PIRE.
[question:VD503]
% Existe-t-il une base juridique HB ?

% Le titre de Relaisfunkstelle a été changé en Relais.
% D'autres occurrences de Relaisfunkstelle ont été changées en Relais.
% TODO pour l'hélvétisation du plan des indicatifs inséré.
