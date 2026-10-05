Ce chapitre traite des bases concernant les liaisons fixes et les règlements associés pour leur exploitation. Un traitement approfondi des aspects techniques est abordé dans le chapitre [sec:paketvermittelte_netzwerke].

Une liaison fixe est une liaison radio établie de manière permanente, servant à interconnecter des stations de radioamateur, par exemple des relais, des digipeaters ou des nœuds HAMNET. Les liaisons fixes peuvent faire partie d'installations de radioamateur non surveillées. L'exploitation de telles installations doit être déclarée à l'OFCOM conformément aux [règlements](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) en vigueur. Pour une installation de radioamateur non surveillée, un indicatif d’appel de radioamateur de la catégorie HB9 est requis. Le responsable technique doit être joignable en permanence pendant l'exploitation. L'image [ref:n_linkstrecken_HB9AK-14] montre un système d'antennes sur le Titlis à 2992 mètres d'altitude. Dans de tels emplacements, comme sur l'image [ref:n_linkstrecken_HB9AK], les conditions météorologiques sont exigeantes. Un alignement précis et stable vers la station correspondante à atteindre est préparé sur l'image [ref:n_linkstrecken_HB9].

<margin>
%[photo:127:n_linkstrecken_db0fc:Travaux de maintenance sur le nœud HAMNET DB0FC, au premier plan l'antenne directionnelle %pour la liaison fixe vers DB0BWL]
%
[photo:1001:n_linkstrecken_HB9AK-14:Emplacement Titlis installation de la SWISS-ARTG, essais avec antennes 10 m ; en haut Peter HB9PAE, en bas Martin HB9AUR]

[photo:1002:n_linkstrecken_HB9AK:Les installations en haute montagne doivent résister à des conditions environnementales rudes]

[photo:1003:n_linkstrecken_HB9:Emplacement Titlis installation de la SWISS-ARTG, Dieter HB9CJD en train de configurer la liaison HAMNET vers HB9BA (Weissenstein), un réflecteur de 85 cm pour 5 GHz]
</margin>

%TODO ARK: faire référence aux images dans le texte !
%TODO ARK: Pour l'image du Titlis, 1001, couper la bordure noire à gauche !
%TODO ARK: Déplacer une des images dans la section 16.11 Réseaux à commutation de paquets !

<law>
- Des "Explications détaillées concernant le service d'amateur" se trouvent dans la [Notice sur le radioamateurisme](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) de l'OFCOM.

- Lien direct pour la déclaration des "Utilisations spéciales de fréquences" à l'OFCOM sur [eGov](https://www.egov.swiss/de/amateurfunk/spezielle-frequenznutzung-detail)

</law>

Les liaisons fixes peuvent transmettre des données numériques ou servir de pont analogique entre des relais. Les liaisons fixes fonctionnent fréquemment dans la gamme des $\unit{\giga\hertz}$ du spectre radioamateur. Plusieurs liaisons fixes interconnectées peuvent par exemple constituer le HAMNET (Highspeed Amateurradio Multimedia NETwork), un réseau IP exploité par des radioamateurs.

[question:NE405]

<indepth>
*Calcul de liaison*

Un [outil de calcul de liaison](http://ham.remote-area.net/linktool/index.php) permet d'évaluer si une liaison hertzienne directionnelle entre deux emplacements est techniquement possible. Il prend en compte, entre autres, la fréquence, la distance, la puissance d'émission, les gains d'antenne, les pertes de câble et le *profil de terrain* entre les emplacements. L'outil calcule, entre autres, l'atténuation en espace libre, la puissance de réception et la marge de liaison, et aide ainsi à la planification des liaisons hertziennes directionnelles et HAMNET.

Pour une liaison hertzienne fiable, une zone de Fresnel aussi dégagée que possible est importante, en plus de la visée directe. La zone de Fresnel désigne une zone spatiale autour de la ligne de visée directe, dans laquelle des obstacles peuvent affecter la transmission radio par diffraction et atténuation supplémentaire.
</indepth>

% Modifications
% Echolink supprimé, il appartient aux relais.
% Descriptions des liens créées ou complétées
% Outil de calcul de liaison décrit, à quoi il sert.