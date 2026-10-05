<attention>
La radio par satellite est déjà abordée dans le cours HB3 parmi les règlements fondamentaux et la technique d’exploitation. Les aspects techniques avancés sont approfondis dans le cours HB9 au chapitre [sec:satelliten_2].
</attention>

<margin>
[photo:124:n_satellit_oscar1:Modèle du premier satellite radioamateur OSCAR 1, qui en 1961 a émis depuis l'orbite de la terre une balise dans la bande des $\qty{2}{\meter}$ pendant 22 jours et a été entendu par 570 radioamateurs de 28 pays]
</margin>

---

Les satellites orbitent autour de la terre sur des trajectoires circulaires ou elliptiques et à différentes hauteurs.
Depuis 1961, cela inclut également les satellites radioamateurs. Ceux-ci sont désignés sous le nom d'OSCAR. C'est l'abréviation de "Orbiting Satellite Carrying Amateur Radio" ("Satellite en orbite transportant la radio amateur"). Le premier satellite radioamateur a été nommé OSCAR 1 ([ref:n_satellit_oscar1]). OSCAR 1 n'était que le début. Au cours des années suivantes - jusqu'à aujourd'hui - toute une série de charges utiles radioamateurs de plus en plus équipées ont été envoyées dans l'espace. Ceux qui s'intéressent à l'histoire des satellites radioamateurs trouveront plus d'informations dans la [History of AMSAT](https://www.amsat.org/amsat-history/).
% Avec la dernière phrase, l'exigence d'une référence de source est également remplie.
[question:BE415]

Dans ce chapitre, nous apprenons "Qu'est-ce qu'un satellite radioamateur ?" et "Comment se déplace-t-il ?". Dans le chapitre [sec:satelliten_2], nous découvrons ensuite "Comment réaliser réellement une liaison radio par satellite ?".

Les relais radio embarqués sont appelés "transpondeurs". La fréquence d'entrée, c'est-à-dire le lien radio de la terre vers le satellite, est appelée "uplink" en radio par satellite. La fréquence de sortie, c'est-à-dire le lien radio du satellite vers la terre, est quant à elle appelée "downlink". Pour l'uplink et le downlink, des bandes de fréquences différentes sont souvent utilisées, car cela permet un découplage plus simple entre le signal émis et le signal reçu.

<indepth>
Différentes altitudes de vol et orbites de satellites permettent une large gamme d'applications satellitaires, allant de la communication à la navigation en passant par la recherche scientifique et l'observation de la terre. Dans ce qui suit, nous présentons les principales altitudes de vol ou orbites.
  
*Caractérisation des orbites de satellites (orbits)*

Les orbites de satellites peuvent être décrites selon différentes propriétés. Les termes LEO, MEO et GEO se réfèrent principalement à l'altitude de l'orbite. En revanche, des termes comme HEO ou Polar Orbit décrivent d'autres propriétés de l'orbite, notamment sa forme ou son inclinaison. Ces classifications peuvent donc se chevaucher. Dans ce qui suit, nous présentons les principales altitudes ou orbites.

*Orbites basses (Low Earth Orbit - LEO)*
Les satellites en orbite basse sont généralement positionnés à des hauteurs d'environ 160 à 2'000 kilomètres au-dessus de la terre. Il s'agit d'orbites relativement proches de la surface de la terre. Dans cette région, se déplacent de nombreux satellites d'observation de la terre, comme par exemple les satellites météorologiques ou les satellites de surveillance environnementale. La proximité avec la terre permet une haute résolution dans la collecte de données et d'images. La faible distance à la terre permet des liaisons radio relativement courtes et donc une faible atténuation en espace libre. En même temps, les satellites LEO se déplacent rapidement dans le ciel et ne sont visibles depuis une station radio donnée que pendant un survol limité dans le temps.

*Orbites moyennes (Medium Earth Orbit - MEO)*
Les orbites moyennes s'étendent à des hauteurs d'environ 2'000 à 35'786 kilomètres au-dessus de la terre. Cette région abrite souvent des satellites de navigation, comme ceux utilisés pour le système mondialement connu GPS. Comme les satellites mettent ici plus de temps à orbiter autour de la terre, ils offrent un équilibre entre couverture et précision pour la navigation et le positionnement. Avec l'augmentation de l'altitude de l'orbite, la période orbitale s'allonge. En même temps, la zone accessible par un satellite s'agrandit.

*Orbite géostationnaire (Geostationary Orbit – GEO)*
À des hauteurs d'environ 35'786 kilomètres au-dessus de la surface de la terre se trouvent les orbites géostationnaires. Un satellite géostationnaire se déplace sur une orbite presque circulaire au-dessus de l'équateur dans la même direction de rotation et avec la même vitesse angulaire que la terre. Ainsi, il apparaît presque fixe dans le ciel vu de la terre. Cela permet à une station au sol d'orienter son antenne en permanence vers la même position. Les satellites géostationnaires sont donc particulièrement adaptés aux applications de communication et permettent une couverture constante d'une zone spécifique.
Une orbite géosynchrone a une période orbitale d'environ un jour sidéral, soit 23 heures, 56 minutes et 4 secondes. Une forme particulière de celle-ci est l'orbite géostationnaire (Geostationary Orbit, GEO) à une hauteur d'environ 35'786 kilomètres au-dessus de l'équateur. [QO-100](https://amsat-dl.org/p4-a-nb-transponder-bandplan-und-betriebsrichtlinien/) est la charge utile radioamateur sur le satellite géostationnaire Es’hail-2 et était la première charge utile radioamateur en orbite géostationnaire.

*Orbites hautement elliptiques (Highly Elliptical Orbit - HEO)*
Les orbites hautement elliptiques possèdent une forme d'ellipse fortement excentrique. Le satellite est alors pendant une partie de l'orbite nettement plus éloigné de la terre que pendant le reste de la révolution. Les orbites HEO peuvent être conçues de manière à ce qu'un satellite reste longtemps visible au-dessus des hautes latitudes géographiques. Elles conviennent donc par exemple pour des applications nécessitant une bonne couverture des régions polaires. HEO n'est pas une classe de hauteur pure comme LEO ou MEO, mais décrit surtout la forme de l'orbite.

*Orbites polaires (Polar Orbit)*
Les satellites opérant en orbites polaires survolent les pôles de la terre. Dans une orbite polaire, l'inclinaison de l'orbite est d'environ 90 degrés. Comme la terre tourne sous l'orbite du satellite, presque toutes les régions de la surface de la terre peuvent être survolées au fil du temps avec une orbite appropriée. Comme ces orbites offrent une couverture complète de la surface de la terre au fil du temps, elles sont souvent utilisées pour des études scientifiques, la surveillance environnementale et l'observation de la terre.

Une orbite polaire n'est pas non plus une classe de hauteur propre. Un satellite peut par exemple être opéré simultanément en orbite basse (LEO) et en orbite polaire.
</indepth>

[question:BE416]
[question:BE411]
[question:BE412]
[question:NF113]

---

Lors de l'utilisation de la communication par satellite, l'orientation des antennes est d'une importance centrale. Les termes *Azimut* et *Élévation* y jouent un rôle clé. Ils décrivent l'orientation horizontale et l'angle vertical sous lesquels un satellite est perçu depuis la surface de la terre.
* L'*Azimut* est la direction le long de l'horizon vers laquelle on regarde pour voir le satellite. Il est généralement mesuré en degrés et va de $\qty{0}{\degree}$ (nord) à $\qty{90}{\degree}$ (est), $\qty{180}{\degree}$ (sud) jusqu'à $\qty{270}{\degree}$ (ouest).
* L'*Élévation* est l'angle vertical sous lequel un satellite se trouve au-dessus de l'horizon. Elle est également mesurée en degrés et varie de $\qty{0}{\degree}$ (directement à l'horizon) à $\qty{90}{\degree}$ (directement au-dessus).

<margin>
[picture:876:n_azimut_elevation:Azimut et élévation dans l'espace]
</margin>

<wordorigin>
Le terme *Azimut* vient de l'arabe *as-sumūt*, ("les chemins"). *Élévation* dérive du latin elevare ("élever").
</wordorigin>

[question:BE413]
[question:BE414]

Dans le service d'amateur par satellite, une exception s'applique à l'obligation d'utiliser uniquement un langage clair. Il est exceptionnellement permis aux stations de commande de chiffrer les signaux de commande vers les satellites radioamateurs dans le but de les dissimuler. Cela signifie que des procédures de chiffrement peuvent exceptionnellement être utilisées pour empêcher que le contenu des signaux de commande ne soit lu par des tiers. Cela sert à la sécurité des satellites contre les commandes de contrôle par des personnes non autorisées.

[question:VA303]
[question:VN026]


%Dans le droit allemand - mais pas internationalement - cette règle s'applique également aux signaux de commande vers les stations automatiques, télécommandées et distantes. Question correspondante VD104 supprimée.
