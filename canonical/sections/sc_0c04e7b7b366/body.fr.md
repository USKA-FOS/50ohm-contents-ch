<attention>
*Ce contenu n'est pas pertinent pour l'examen.*
Les satellites et les voyages spatiaux jouent un rôle de plus en plus important. Grâce au service de radioamateurisme, nous, radioamateurs, pouvons également être actifs dans ce domaine passionnant via les satellites. C'est pourquoi nous pensons que cette introduction mérite sa place dans un cours de radioamateurisme, même si le sujet n'est actuellement pas examiné.
</attention>

Quelques bases sont déjà connues du chapitre [sec:satelliten]. Ici, d'autres termes de la communication par satellite sont abordés.

## Orbites et lois de Kepler

Les satellites ne se déplacent pas arbitrairement autour de la terre. Leurs trajectoires sont déterminées par la gravitation et peuvent être décrites par les lois de Kepler. Une orbite circulaire est un cas particulier d'une orbite elliptique ([ref:a_kepler_ellipse]).

### 1ère loi de Kepler - Loi des ellipses

La trajectoire d'un satellite autour de la terre est fondamentalement une ellipse. La terre se trouve alors dans l'un des deux foyers de l'ellipse. Pour une orbite circulaire, les deux foyers coïncident.

---

### 2ème loi de Kepler - Loi des aires

La ligne reliant la terre et le satellite balaie des aires égales en des temps égaux. Il en résulte : un satellite se déplace plus rapidement au point le plus proche de la terre, le périgée, et plus lentement au point le plus éloigné de la terre, l'apogée, sur une orbite elliptique.

Ce comportement est également intéressant pour la pratique radio, car la vitesse relative entre le satellite et la station radio change pendant un passage.

### 3ème loi de Kepler - Loi des périodes

Pour les satellites orbitant autour du même objet central, on a :

$$T^2 \propto a^3$$

Où $T$ est la période orbitale et $a$ le demi-grand axe de l'ellipse orbitale. Plus le demi-grand axe de l'orbite est grand, plus la durée d'une révolution est longue.
Pour la pratique satellitaire, cela signifie : les satellites en orbite basse tournent autour de la terre beaucoup plus rapidement que les satellites en orbite plus haute.

<margin>
[picture:10100:a_kepler_ellipse:Ellipse de Kepler avec satellite en orbite]
</margin>

### Période orbitale d'un satellite

Dans le chapitre [sec:satelliten], nous avons découvert différentes orbites de satellites. La période orbitale d'un satellite autour de la terre dépend du demi-grand axe de son orbite. Pour les orbites circulaires, cela correspond à l'altitude de l'orbite plus le rayon terrestre. Cette relation est illustrée dans l'image [ref:a_umlaufzeiten].

<indepth>
*Période orbitale d'un satellite*
[picture:10101:a_umlaufzeiten:Périodes orbitales en fonction de l'altitude de l'orbite]
</indepth>

Pour la pratique du satellite radio, la période orbitale, la visibilité et la vitesse du satellite sont particulièrement importantes.

## Visibilité d'un satellite

Pour une station radio sur terre, ce qui compte n'est pas de savoir si un satellite orbite fondamentalement autour de la terre, mais s'il se trouve actuellement au-dessus de l'horizon local. Un passage commence avec l'"Acquisition of Signal" (AOS), lorsque le satellite devient visible ou recevable pour la station. Il se termine avec le "Loss of Signal" (LOS), lorsqu'il redescend sous l'horizon.

La position d'un satellite dans le ciel est indiquée par l'azimut, c'est-à-dire la direction le long de l'horizon, et l'élévation, c'est-à-dire l'angle au-dessus de l'horizon. Pendant un passage, ces deux valeurs changent continuellement.

La zone sur la surface de la terre où un satellite ou sa charge utile radio peut être reçu est appelée empreinte. Plus le satellite vole haut, plus cette zone peut être grande.

---

## Effet Doppler en radio par satellite

Comme un satellite se déplace par rapport à la station radio sur terre, l'effet Doppler se produit lors d'une liaison radio avec le satellite. La fréquence reçue change par rapport à la fréquence réellement émise.

Lorsque le satellite se rapproche de la station radio, la fréquence reçue est augmentée par rapport à la fréquence nominale. Lorsque le satellite s'éloigne à nouveau, la fréquence reçue est diminuée.

Pour de petites vitesses par rapport à la vitesse de la lumière, le décalage de fréquence peut être approximé par

$$\Delta f \approx f_0 \frac{v_r}{c}$$

Où $f_0$ est la fréquence d’émission, $v_r$ la vitesse relative dans la direction du lien radio et $c$ la vitesse de la lumière. La vitesse radiale est donc déterminante, et non la vitesse orbitale totale du satellite. On considère $v_r > 0$ lorsque l'émetteur et le récepteur se rapprochent.

Pour les satellites LEO, le décalage Doppler peut être particulièrement notable, surtout aux fréquences plus élevées et avec des modes de fonctionnement à bande étroite. Par conséquent, la fréquence doit éventuellement être ajustée en continu pendant un passage de satellite. Les stations satellitaires modernes peuvent effectuer automatiquement la compensation Doppler.

<indepth>
Cette applet visualise l'effet Doppler. Avec le curseur, la *vitesse relative entre l'émetteur et le récepteur* peut être réglée.

- Lorsque la *source se déplace vers le récepteur*, plus de fronts d'onde arrivent par unité de temps, ce qui correspond à une *augmentation de la fréquence reçue*. Bien que l'émetteur émette toujours à la même fréquence.

- Lorsque la *source s'éloigne du récepteur*, moins de fronts d'onde arrivent par unité de temps, ce qui correspond à une *diminution de la fréquence reçue*. Bien que l'émetteur émette toujours à la même fréquence.

[include:doppler_visualisierung]

</indepth>

## Affaiblissement en espace libre et liaison radio

Le signal radio d'un satellite doit parcourir une grande distance entre la station au sol et le satellite. Cela crée ce qu'on appelle l'affaiblissement en espace libre. Il augmente avec la distance croissante et avec la fréquence croissante.

Pour une liaison en espace libre idéale, la formule de Friis pour l'espace libre s'applique, qui constitue la base de tout budget de liaison :

$$L_{FS}=20\log_{10}\left(\frac{4\pi d}{\lambda}\right)$$

Où $d$ est la distance entre l'émetteur et le récepteur et $\lambda$ la longueur d’onde.

Pour une liaison satellitaire fonctionnelle, la puissance d'émission, le gain d'antenne, les pertes de câble, l'affaiblissement en espace libre et la sensibilité du récepteur doivent donc être considérés ensemble. Cette analyse est appelée budget de liaison.

<indepth>
*Budget de liaison descendant simplifié d'un CubeSat LEO dans la bande des 2 mètres*
Le terme dB (décibel) ne sera traité en détail que dans le chapitre [sec:dezibel_1]. Ici, il suffit de savoir que dB représente un rapport et dBm un niveau de puissance absolu.
Un exemple très simplifié pour une liaison descendante d'un CubeSat LEO vers une station au sol pourrait ressembler à ceci :

| Grandeur | Valeur exemple |
| Fréquence | 145.9 MHz |
| Puissance d'émission 1 W | 30 dB<sub>m</sub>  |
| Pertes câble TX et connecteurs | −1 dB |
| Gain antenne d'émission | +3 dB<sub>i</sub> |
| PIRE | +32 dB<sub>m</sub> |
| Distance | 2000 km |
| Affaiblissement espace libre | −141.7 dB |
| Gain antenne de réception | +8 dB<sub>i</sub> |
| Préamplificateur | +15 dB |
| Pertes câble RX et connecteurs | −2 dB |
| Puissance à l'entrée du Rx | −88.7 dB<sub>m</sub> |
| sensibilité supposée du récepteur | -104 dB<sub>m</sub>  |
|  |   |
| Marge de liaison  |  +15.3 dB |

Dans un vrai budget de liaison, d'autres facteurs s'ajoutent, par exemple le type de modulation, le débit de données, le bruit du récepteur et le plancher de bruit.
</indepth>

## Antennes et polarisation

Comme le satellite se déplace pendant un passage, sa direction relative à la station au sol change également. Pour de nombreuses liaisons par satellite, des antennes avec un gain approprié et une directivité suffisante sont donc utilisées. Pour les antennes plus directives, un suivi de l'antenne peut être nécessaire.

La polarisation du signal doit également être prise en compte. En raison du mouvement et de l'orientation du satellite, l'orientation de la polarisation par rapport à la station au sol peut changer. En radio par satellite, des polarisations linéaires ou circulaires sont donc utilisées selon l'application.

## Transpondeurs et digipeaters

Les satellites de radioamateurisme peuvent avoir différents types de charges utiles radio.

Un transpondeur linéaire reçoit une bande de fréquences et la convertit en une autre bande de fréquences. Plusieurs signaux peuvent être transmis simultanément dans la largeur de bande du transpondeur disponible. Les modes de fonctionnement typiques sont par exemple SSB et CW.

Un transpondeur FM fonctionne quant à lui avec des signaux FM pour la transmission simultanée d'une seule conversation.

Un digipeater reçoit des données numériques et les retransmet selon une procédure définie. Il diffère donc fondamentalement d'un transpondeur linéaire, qui convertit le spectre de fréquences reçu sans traiter les signaux individuels comme des paquets de données.

## Balises de satellites

De nombreux satellites de radioamateurisme sont équipés d'une balise. [sec:baken] émettent automatiquement à intervalles réguliers ou en continu des signaux définis. Elles peuvent servir à observer la réceptabilité du satellite, les conditions de propagation et l'état de la charge utile radio.

Lors de la réception d'une balise, une station radio peut par exemple déterminer si le satellite est déjà au-dessus de l'horizon, comment la fréquence de réception change en raison de l'effet Doppler et comment fonctionne la liaison radio.

## Suivi de satellites

Pour la pratique du satellite radio, l'orbite actuelle et la position du satellite sont nécessaires. Pour cela, des éléments orbitaux, par exemple les TLE (Two-Line Elements), sont utilisés. Les programmes de suivi calculent à partir de ceux-ci la position prévue du satellite et affichent, entre autres, l'azimut, l'élévation, l'AOS et le LOS ainsi que l'effet Doppler attendu.

Cela permet de planifier les passages et de suivre automatiquement les équipements radio et les antennes.

---

<tip>
Les organisations AMSAT dans le monde entier s'occupent de la radio par satellite en radioamateurisme, en Suisse c'est [AMSAT-HB](https://amsat-hb.org/).
</tip>
