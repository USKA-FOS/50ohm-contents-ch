Un relais permet d’étendre la portée d’une liaison radio lorsque la connexion directe entre deux stations de radioamateur n’est pas possible. Les relais sont généralement installés à des emplacements dégagés, par exemple au sommet de montagnes, sur des immeubles élevés, des clochers ou d’autres tours. Il existe également des relais embarqués sur des satellites en orbite autour de la Terre. La structure et le fonctionnement d’un relais sont illustrés dans l’image [ref:n_relaisfunkstellen_aufbau]. 
% L’image n’est pas idéale. On distingue à peine qu’il s’agit d’un relais au sommet d’une montagne. Il n’est pas évident qu’il reçoit et "relaye" les signaux. Issue #38 ouverte

[picture:648:n_relaisfunkstellen_aufbau:Représentation schématique d’une station relais avec des utilisateurs]

Par exemple, si une montagne se trouve entre deux stations radio, il est impossible d’établir une liaison à travers celle-ci. Une station relais située au sommet de la montagne permet néanmoins de créer une liaison, car les deux stations peuvent atteindre directement le relais.

---
<law>
Lien direct vers la page de déclaration sur [eGov](https://www.egov.swiss/fr/amateurfunk/spezielle-frequenznutzung-detail)

[Fiche d’information sur le radioamateurisme](https://www.bakom.admin.ch/fr/amateurfunk#Merkblatt-Amateurfunk) 1.7
</law>


En Suisse, seules les associations de radioamateurisme sont autorisées à exploiter des stations non surveillées, y compris les relais.

Les associations de radioamateurisme souhaitant installer une station non surveillée, y compris un relais, doivent déclarer celle-ci à l’OFCOM (enregistrement) avant sa mise en service. 
Pour garantir une utilisation sans interférences des fréquences par l’installation non surveillée, il est recommandé d’effectuer au préalable une coordination des fréquences. Pour cela, vous pouvez contacter l’USKA [Contact :](qrg@uska.ch), qui vous assistera sur une base volontaire. Ensuite, vous pourrez effectuer la déclaration auprès de l’OFCOM via le portail eGov.
% Cette information devrait-elle figurer sur la page d’introduction ?
[question:VN007]



L’indicatif d’appel d’une station relais commence généralement par DB0, DM0 ou DO0, conformément au [plan d’indicatifs](https://50ohm.de/rzp). 
La définition officielle des répéteurs est un peu plus technique : *« station relais » : une station radioamateur télécommandée (y compris les satellites), qui retransmet à distance les émissions radioamateur reçues, des parties de celles-ci ou d’autres signaux introduits ou stockés, afin d’améliorer la portée des stations radioamateur.*
La question suivante peut être résolue par élimination si l’on connaît les points suivants :
* Les stations relais ne sont pas exploitées avec des indicatifs personnels.
* Les stations relais ne sont généralement pas occupées en permanence.
* Les stations relais ne doivent pas obligatoirement être installées à des emplacements géographiquement dégagés.
[question:VD118]
% Existe-t-il une base juridique en Suisse ? Le texte est-il à conserver dans la mesure du possible ?

---
% La notion de « décalage » est-elle correcte ? Existe-t-il une liste pour la Suisse ? Les données du tableau NE-4.9.2 sont-elles conformes ?
Les relais sont également appelés répéteurs ou stations relais. On peut les reconnaître au fait qu’ils émettent régulièrement leur indicatif d’appel.

Un relais reçoit sur sa fréquence d’entrée le signal d’une station radioamateur et le retransmet simultanément sur sa fréquence de sortie. Pour éviter que l’émetteur du relais ne perturbe son propre récepteur, les fréquences d’émission et de réception sont généralement différentes. L’écart entre la fréquence d’émission et la fréquence de réception est appelé décalage de fréquence ou simplement décalage. Les décalages couramment utilisés en Allemagne sont indiqués dans le tableau [ref:n_relaisfunkstellen_ablage].

<margin>
| r : Bande | X : Décalage |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Décalage de fréquence]
</margin>

Par exemple, la fréquence d’un relais en $\qty{70}{\centi\meter}$ est indiquée comme suit :
* Fréquence d’entrée : $\qty{431,275}{\mega\hertz}$
* Décalage : $\qty{+7,600}{\mega\hertz}$
* Fréquence de sortie : $\qty{438,875}{\mega\hertz}$

[question:BE401]
[question:BE402]
[question:BE403]

<indepth>
Certains relais fonctionnent également en mode *crossband*. Cela signifie qu’une station émet et reçoit sur une bande (par exemple $\qty{70}{\centi\meter}$), tandis qu’une autre station utilise la même station relais, mais sur une autre bande (par exemple $\qty{2}{\meter}$). Le contrôle du relais achemine les conversations entre les deux bandes. Il est également possible de convertir le mode de transmission, par exemple de BLU à FM.
</indepth>

Un relais qui transmet des données plutôt que de la voix est appelé digipeater. Un digipeater est capable de recevoir des paquets de données et de les retransmettre. Une particularité est que la retransmission peut se faire par segments ou avec un léger décalage dans le temps. Les paquets de données peuvent également être répétés ou certains champs de données modifiés.

[question:NF118]

---

Avant d’utiliser un relais pour établir une liaison radio, il est essentiel de connaître ses particularités techniques et ses paramètres. Pour certains relais, des réglages supplémentaires sur l’émetteur-récepteur sont nécessaires pour garantir un fonctionnement sans interférences. Outre la FM analogique (modulation de fréquence), des procédés numériques comme le DMR et le D-Star sont également utilisés pour la transmission vocale.

<tip>
Pour obtenir des informations sur les relais ainsi que leurs paramètres et particularités techniques, vous pouvez contacter la section locale de l’USKA, la personne responsable du relais ou consulter Internet.
</tip>
% Où obtenir ces informations en Suisse ? USKA ? https://uska.ch/bandplan/ (Attention : refonte du site de l’USKA en septembre 2026)
[question:NE309]
[question:NE308]

Un réglage important est la bande passante du canal en mode FM. Rappel : la bande passante indique l’espace occupé dans le spectre de fréquences par l’émission. Il existe d’une part le FM large, dont la bande passante est de $\qty{25}{\kilo\hertz}$ et qui est affiché par exemple comme *FM-W* sur l’écran. D’autre part, il y a le FM étroit (Narrow-FM), qui n’occupe qu’une bande passante de $\qty{12,5}{\kilo\hertz}$ et qui est représenté par exemple comme *FM-N* sur l’appareil radio. De nombreux répéteurs n’aiment pas les signaux trop larges, car cela peut entraîner des signaux déformés et perturber les fréquences relais voisines.
% Explication supplémentaire nécessaire pour les 25 kHz. La FRV l’a expressément demandée.
[question:BE407]
[question:BE417]

L’exploitation radio via des stations radioamateur télécommandées est en principe autorisée à tous les radioamateurs disposant d’un indicatif d’appel attribué. Toutefois, pour garantir un fonctionnement sans interférences, l’exploitant peut exclure d’autres radioamateurs de l’utilisation de la station.
% L’Agence fédérale des réseaux (BNetzA) doit en être informée.
[question:VD504]
% Existe-t-il une base juridique en Suisse ? Conserver le texte dans la mesure du possible.

Lors de l’utilisation d’une station relais, les transmissions doivent être aussi courtes que possible afin de faciliter l’accès au relais pour les stations mobiles et portables, en particulier lorsqu’elles ne se trouvent que brièvement dans la zone de réception. Il est conseillé de laisser une pause entre les transmissions pour permettre à d’autres stations de s’annoncer.

[question:BE406]
[question:BE404]

Si deux stations différentes émettent simultanément, la retransmission du relais est perturbée au point de devenir inaudible. Pour éviter ce phénomène appelé *doublon*, il est important de bien gérer les transitions entre les utilisateurs du répéteur. Cela signifie également de ne commencer à émettre qu’une fois que la station précédente a terminé sa transmission.

---
<indepth>
Explication de la gestion des transitions
</indepth>
% À compléter avec une boîte de marge

[question:NE310]
[question:BE405]


Une particularité concerne l’évaluation d’une liaison radio via une station relais. Comme l’intensité du signal que l’on reçoit de son partenaire radio correspond à celle de la station relais et non à celle du partenaire lui-même, on ne tient pas compte de cette intensité. Dans le rapport, seule la lisibilité (R) est évaluée.

---
<indepth>
Explication du rapport sur relais avec exemple
</indepth>
% À compléter avec une boîte de marge

[question:BE408]


Les prescriptions relatives aux puissances d’émission des stations relais figurent également dans l’annexe 1 de l’ordonnance sur le radioamateurisme (AFuV). Au-dessus de 30 MHz, une station fonctionnant automatiquement peut être exploitée avec une puissance maximale de 50 W ERP.
[question:VD503]
% Existe-t-il une base juridique en Suisse ?