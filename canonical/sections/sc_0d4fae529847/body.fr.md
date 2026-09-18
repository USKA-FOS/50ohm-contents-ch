**EN COURS DE RÉDACTION**

<attention>
En raison des fréquences utilisées par les satellites, le radioamateurisme par satellite nécessite malheureusement une licence HB9. Comme ce sujet porte principalement sur les réglementations et la technique d’exploitation, il est traité dans le cours HB3.
</attention>

<margin>
[photo:124:n_satellit_oscar1:Maquette du premier satellite radioamateur OSCAR 1, qui a émis depuis son orbite autour de la terre pendant 22 jours un signal de balise dans la bande des $\qty{2}{\meter}$ et a été capté par 570 radioamateurs issus de 28 pays]
</margin>

---

Les satellites gravitent autour de la Terre sur des orbites circulaires ou elliptiques et à différentes altitudes. Plus d’informations à ce sujet dans [sec:satelliten_2]. Depuis 1961, les satellites radioamateurs en font également partie. Ils sont désignés par l’acronyme OSCAR, qui signifie "Orbiting Satellite Carrying Amateur Radio" ("Satellite en orbite transportant un équipement radioamateur"). Le premier satellite radioamateur a été nommé OSCAR 1 ([ref:n_satellit_oscar1]). OSCAR 1 n’était que le début. Au fil des années – jusqu’à aujourd’hui – une série de charges utiles radioamateurs de plus en plus sophistiquées ont été envoyées dans l’espace.

[question:BE415]

Les stations relais embarquées sont appelées « transpondeurs ». La fréquence d'entrée, c'est-à-dire la liaison radio de la terre vers le satellite, est désignée par le terme « uplink » en radio par satellite. La fréquence de sortie, c'est-à-dire la liaison radio du satellite vers la terre, est quant à elle appelée « downlink ». Pour l'uplink et le downlink, on utilise souvent des bandes de fréquences différentes, car cela permet une séparation plus simple entre le signal émis et le signal reçu, et réduit la taille des filtres à bord du satellite.

<indepth>
*Caractérisation des orbites des satellites (orbits)*

Les orbites des satellites peuvent être décrites selon différentes propriétés. Les termes LEO, MEO et GEO se réfèrent principalement à la hauteur de l'orbite. En revanche, des termes comme HEO ou orbite polaire décrivent d'autres caractéristiques de l'orbite, notamment sa forme ou son inclinaison. Ces classifications peuvent donc se chevaucher. Nous présentons ci-dessous les principales hauteurs de vol ou orbites.

*Orbites basses (Low Earth Orbit - LEO)*
Les satellites en orbite basse se trouvent à des hauteurs d'environ 400 à 2 000 kilomètres au-dessus de la surface de la terre. Ce sont des orbites relativement proches de la surface terrestre. Dans cette zone évoluent de nombreux satellites d'observation de la terre et météorologiques, ainsi que de nombreux satellites radioamateurs. La proximité de la terre permet une haute résolution pour l'acquisition de données et d'images. La faible distance par rapport à la terre permet des liaisons radio relativement courtes et donc une atténuation réduite dans l'espace libre. En même temps, les satellites LEO se déplacent rapidement dans le ciel et ne sont visibles depuis une station radio donnée que pendant un survol de durée limitée.

*Orbites moyennes (Medium Earth Orbit - MEO)*
Les orbites moyennes se situent approximativement entre 2 000 et 35 786 kilomètres de hauteur. Dans cette zone se trouvent par exemple de nombreux satellites de navigation, comme ceux utilisés pour le célèbre système GPS. Comme les satellites mettent plus de temps à faire le tour de la terre, ils offrent un équilibre entre couverture et précision pour la navigation et le positionnement. Plus la hauteur de l'orbite augmente, plus la période orbitale s'allonge. Simultanément, la zone accessible par un satellite s'agrandit.

*Orbites hautes (Geostationary Orbit - GEO)*

Une orbite géosynchrone a une période orbitale d'environ un jour sidéral, soit 23 heures, 56 minutes et 4 secondes. Une forme particulière de celle-ci est l'orbite géostationnaire (Geostationary Orbit, GEO) à une hauteur d'environ 35 786 kilomètres au-dessus de l'équateur.

Un satellite géostationnaire se déplace sur une orbite quasi circulaire au-dessus de l'équateur, dans le même sens de rotation et avec la même vitesse angulaire que la terre. De ce fait, il apparaît presque fixe dans le ciel depuis la terre. Cela permet à une station au sol de pointer en permanence son antenne vers la même position. Les satellites géostationnaires sont donc particulièrement adaptés aux applications de communication et permettent une couverture constante d'une zone donnée.

[QO-100](https://amsat-dl.org/p4-a-nb-transponder-bandplan-und-betriebsrichtlinien/) est à ce jour le premier satellite géostationnaire équipé d'une charge utile radioamateur.

*Orbites fortement elliptiques (Highly Elliptical Orbit - HEO)*

Les orbites fortement elliptiques présentent une forme d'ellipse très excentrique. Pendant une partie de son orbite, le satellite se trouve bien plus éloigné de la terre que pendant le reste de sa révolution. Les orbites HEO peuvent être conçues de manière à ce qu'un satellite reste visible longtemps au-dessus de hautes latitudes géographiques. Elles conviennent donc par exemple pour des applications nécessitant une bonne couverture des régions polaires. HEO n'est pas une simple classe d'altitude comme LEO ou MEO, mais décrit surtout la forme de l'orbite.

*Orbites polaires (Polar Orbit)*
Les satellites évoluant sur des orbites polaires survolent les pôles de la terre. Dans une orbite polaire, l'inclinaison est d'environ 90 degrés. Comme la terre tourne sous l'orbite du satellite, une orbite polaire bien choisie permet de survoler, au fil du temps, presque toutes les régions de la surface de la terre. Une orbite polaire n'est pas non plus une classe d'altitude en soi. Un satellite peut par exemple fonctionner simultanément sur une orbite LEO et sur une orbite polaire.
</indepth>

[question:BE416]
[question:BE411]
[question:BE412]
[question:NF113]

---

Lors de l'utilisation de communications par satellite, l'orientation des antennes est d'une importance capitale. Les termes *azimut* et *élévation* y jouent un rôle clé. Ils décrivent l'orientation horizontale et l'angle vertical sous lesquels un satellite est perçu depuis la surface de la terre :
* L'*azimut* est la direction le long de l'horizon vers laquelle il faut regarder pour voir le satellite. Il est généralement mesuré en degrés et varie de $\qty{0}{\degree}$ (nord) à $\qty{90}{\degree}$ (est), $\qty{180}{\degree}$ (sud) et $\qty{270}{\degree}$ (ouest).
* L'*élévation* est l'angle vertical sous lequel un satellite est visible depuis un point donné au-dessus de l'horizon. Elle est également mesurée en degrés et varie de $\qty{0}{\degree}$ (directement sur l'horizon) à $\qty{90}{\degree}$ (directement au-dessus de soi).

<margin>
[picture:876:n_azimut_elevation:Azimut et élévation dans l'espace]
</margin>

<wordorigin>
Le terme *azimut* provient de l'arabe *as-sumūt* ("les chemins"). *Élévation* dérive du latin *elevare* ("élever").
</wordorigin>

[question:BE413]
[question:BE414]

Dans le service d'amateur par satellite, une exception est faite à l'obligation d'utiliser uniquement un langage ouvert. Il est permis de crypter les signaux de commande échangés entre les stations terrestres et les satellites de radioamateur à des fins de dissimulation. Cela signifie que des procédés de chiffrement empêchant la lecture du contenu des signaux de commande par des tiers peuvent être utilisés à cette fin. Cela sert à protéger les satellites contre des commandes de contrôle émanant de personnes non autorisées.

[question:VA303]
[question:VN026]


En droit allemand – mais pas au niveau international – cette réglementation s’applique également aux signaux de commande des stations automatiques, télécommandées ou distantes. La question correspondante VD104 a été supprimée.

---

**XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX**
**CE PASSAGE DOIT ÊTRE PLACÉ DANS UN CHAPITRE SUPPLÉMENTAIRE POUR LA PARTIE HB9**

---

<attention>
*Ce contenu n’est pas pertinent pour l’examen.*
Les satellites et l’exploration spatiale jouent un rôle de plus en plus important. Grâce au service d’amateur par satellite, nous pouvons également œuvrer dans ce domaine passionnant. C’est pourquoi nous estimons que cette introduction mérite sa place dans un cours de radioamateur, même si le sujet n’est actuellement pas évalué à l’examen.
</attention>

## Orbites et lois de Kepler

Les satellites ne se déplacent pas de manière arbitraire autour de la terre. Leurs orbites sont déterminées par la gravitation et peuvent être décrites à l’aide des lois de Kepler. Une orbite circulaire constitue un cas particulier d’orbite elliptique ([ref:a_kepler_ellipse]).

### 1. Première loi de Kepler – loi des orbites

L’orbite d’un satellite autour de la terre est fondamentalement une ellipse. La terre se situe alors dans l’un des deux foyers de l’ellipse. Dans le cas d’une orbite circulaire, les deux foyers coïncident.

---

### 2. Deuxième loi de Kepler - Loi des aires

La ligne reliant la terre au satellite balaye des aires égales en des temps égaux. Il en découle que le satellite se déplace plus rapidement au point le plus proche de la terre, le périgée, et plus lentement au point le plus éloigné, l'apogée, sur une orbite elliptique.

Ce comportement est également intéressant pour la pratique radioamateur, car la vitesse relative entre le satellite et la station radio varie pendant un passage.

### 3. Troisième loi de Kepler - Loi des périodes

Pour les satellites qui orbitent autour du même objet central, on a :

$$T^2 \propto a^3$$

où $T$ est la période orbitale et $a$ le demi-grand axe de l'ellipse orbitale. Plus le demi-grand axe, et donc la distance orbitale moyenne, est grand, plus la durée d'une orbite est longue.

Pour la pratique des satellites, cela signifie que les satellites en orbite basse tournent autour de la terre beaucoup plus rapidement que ceux en orbite haute.

<margin>
[picture:10100:a_kepler_ellipse:Ellipse de Kepler avec satellite en orbite] 
</margin>

## Visibilité d'un satellite

Pour une station radio au sol, ce qui compte n’est pas de savoir si un satellite tourne bien autour de la terre, mais s’il se trouve actuellement au-dessus de l’horizon local. Un passage commence avec l’**Acquisition of Signal** (AOS), lorsque le satellite devient visible ou accessible pour la station. Il se termine avec le **Loss of Signal** (LOS), lorsque le satellite disparaît à nouveau sous l’horizon.

La position d’un satellite dans le ciel est définie par son **azimut**, c’est-à-dire la direction le long de l’horizon, et son **élévation**, c’est-à-dire l’angle au-dessus de l’horizon. Ces deux valeurs changent en permanence pendant un passage.

La zone à la surface de la terre d’où un satellite peut être vu au-dessus de l’horizon est appelée **footprint**. Plus le satellite vole haut, plus cette zone peut être étendue.

---

## Effet Doppler en radiocommunication par satellite

Comme un satellite se déplace par rapport à une station radio au sol, une **liaison radio** avec ce satellite est soumise à l’effet Doppler. La fréquence reçue diffère alors de la fréquence réellement émise.

Lorsque le satellite se rapproche de la station radio, la fréquence reçue est plus élevée que la fréquence nominale. Lorsqu’il s’éloigne à nouveau, la fréquence reçue est plus basse.

Pour des vitesses faibles par rapport à la **vitesse de la lumière**, le décalage de fréquence peut être approximé par

$$\Delta f \approx f_0 \frac{v_r}{c}$$

où $f_0$ est la **fréquence d’émission**, $v_r$ la vitesse radiale dans la direction de la **liaison radio** et $c$ la **vitesse de la lumière**. Ce qui compte donc, c’est la vitesse radiale et non la vitesse orbitale totale du satellite.

Pour les satellites LEO, le décalage Doppler peut être particulièrement perceptible aux fréquences élevées et avec des modes de fonctionnement à bande étroite. C'est pourquoi il peut être nécessaire de corriger en continu la fréquence pendant le passage du satellite. Les stations satellites modernes peuvent effectuer automatiquement la compensation Doppler.

<indepth>
Cet applet visualise l'effet Doppler. Le curseur permet de régler la *vitesse relative entre l'émetteur et le récepteur*.
  
- Si la *source se rapproche*, davantage de fronts d'onde atteignent le récepteur par unité de temps, ce qui correspond à une *augmentation de la fréquence reçue*, bien que l'émetteur émette toujours à la même fréquence.
  
- Si la *source s'éloigne*, moins de fronts d'onde atteignent le récepteur par unité de temps, ce qui correspond à une *diminution de la fréquence reçue*, bien que l'émetteur émette toujours à la même fréquence.

[include:doppler_visualisierung]

</indepth>

## Affaiblissement en espace libre et liaison radio

Le signal radio d'un satellite doit parcourir une grande distance entre la station au sol et le satellite. Cela entraîne ce qu'on appelle l'affaiblissement en espace libre. Celui-ci augmente avec la distance et avec la fréquence.

Pour une liaison en espace libre idéale, la formule de Friis s'applique. Elle constitue la base de tout bilan de liaison :

$$L_{FS}=20\log_{10}\left(\frac{4\pi d}{\lambda}\right)$$

Dans ce cas, $d$ représente la distance entre l’émetteur et le récepteur et $\lambda$ la longueur d’onde.Pour qu’une liaison par satellite fonctionne, il faut donc considérer conjointement la puissance d’émission, le gain d’antenne, les pertes de câble, l’affaiblissement en espace libre et la sensibilité du récepteur. Cette analyse est appelée bilan de liaison (Linkbudget).<indepth>
*Bilan simplifié d’une liaison descendante (Downlink) d’un CubeSat en orbite basse (LEO) à 145 MHz*

Un exemple fortement simplifié d’une liaison descendante (Downlink) d’un CubeSat en orbite basse (LEO) vers une station au sol pourrait ressembler à ceci :| Grandeur | Valeur exemple |
| Fréquence | 145 MHz |
| Puissance d’émission | 1 W = 0 dBW |
| Câble et connecteur TX | −1 dB |
| Antenne d’émission | +3 dBi |
| EIRP | +2 dBW |
| Distance | 1 000 km |
| Affaiblissement en espace libre | −135,7 dB |
| Antenne de réception | +15 dBi |
| Câble et connecteur RX | −2 dB |
| Puissance reçue | −120,7 dBW = −90,7 dBm |

Dans un bilan de liaison réel, d’autres facteurs s’ajoutent, par exemple le type de modulation, le débit de données, le bruit du récepteur et la marge de liaison.
</indepth>

## Antennes et polarisationComme le satellite se déplace pendant un passage, sa direction par rapport à la station au sol change également. C’est pourquoi, pour de nombreuses liaisons par satellite, on utilise des antennes dotées d’un gain adapté et d’une directivité suffisante. Avec des antennes plus directives, un suivi (pointage) de l’antenne peut être nécessaire.La polarisation du signal doit également être prise en compte. En raison du mouvement et de l’orientation du satellite, l’alignement de la polarisation par rapport à la station au sol peut varier. En radiocommunication par satellite, on utilise donc, selon l’application, des polarisations linéaires ou circulaires.## Transpondeurs et digipeatersLes satellites radioamateurs peuvent être équipés de différents types de charges utiles radio.Un transpondeur linéaire reçoit une bande de fréquences et la convertit en une autre bande de fréquences. Plusieurs signaux peuvent être transmis simultanément dans la largeur de bande disponible du transpondeur. Les modes de fonctionnement typiques sont par exemple la BLU et la CW.Un transpondeur FM fonctionne quant à lui avec des signaux FM et est généralement conçu pour transmettre simultanément une seule conversation ou quelques signaux planifiés en conséquence.Un digipeateur reçoit des données numériques et les retransmet selon une procédure définie. Il se distingue ainsi fondamentalement d'un transpondeur linéaire, qui convertit le spectre de fréquences reçu sans traiter les différents signaux utiles en tant que paquets de données.## Balises de satelliteDe nombreux satellites radioamateurs sont équipés d'une balise. [sec:baken] émettent automatiquement à intervalles réguliers ou en continu des signaux définis. Ils peuvent servir à observer la réception du satellite, les conditions de propagation et l'état de la charge utile radio.Lors de la réception d'une balise, une station radio peut par exemple déterminer si le satellite est déjà au-dessus de l'horizon, comment la fréquence de réception évolue en raison de l'effet Doppler et la qualité de la liaison radio.## Suivi des satellitesPour la pratique de la radio par satellite, la trajectoire actuelle et la position du satellite sont nécessaires. On utilise pour cela des éléments orbitaux, par exemple des TLE (Two-Line Elements). Les programmes de suivi calculent à partir de ces données la position prévue du satellite et indiquent notamment l'azimut, l'élévation, le lever (AOS) et le coucher (LOS) du satellite ainsi que l'effet Doppler attendu.Cela permet de planifier les passages et de suivre automatiquement les antennes et les émetteurs-récepteurs.---

Les satellites radioamateurs disposent d’une balise. Une balise émet automatiquement, à intervalles réguliers ou en continu, des signaux définis. Elle peut servir à observer la réception du satellite, les conditions de propagation et l’état de la charge utile radio.

Lors de la réception d’une balise, une station radio peut par exemple déterminer si le satellite est déjà au-dessus de l’horizon, comment la fréquence de réception évolue en raison de l’effet Doppler et à quel point la liaison radio fonctionne bien.

Dans le chapitre [sec:satelliten], nous avons appris à connaître différentes orbites de satellites. La période orbitale d’un satellite autour de la terre dépend de la hauteur de son orbite. Cette relation est illustrée dans l’image [ref: a_umlaufzeiten].

<indepth>
*Période orbitale d’un satellite*
[picture:10101:a_umlaufzeiten:Périodes orbitales en fonction de la hauteur de l’orbite]
</indepth>

<tip>
Le radioamateurisme par satellite est étudié dans le monde entier par les organisations AMSAT. En Suisse, cela relève de [AMSAT-HB](https://amsat-hb.org/)
</tip>

