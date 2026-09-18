Lors de l'exploitation d'émetteurs – en particulier d'émetteurs de forte puissance – il peut se produire diverses *perturbations* affectant des appareils et installations électroniques. Nous avons déjà abordé ces *perturbations gênantes* et quelques conseils de base pour les éviter dans le chapitre [sec:stoerungen_vermeiden]. L'objectif est d'éviter autant que possible ces perturbations ou d'éliminer leurs causes par des mesures appropriées. Dans cette leçon, nous allons examiner plus en détail les causes et les contre-mesures. En principe, les appareils électroniques peuvent être influencés de deux manières :

- On parle d'*irradiation* lorsque la haute fréquence parvient dans l'électronique d'un appareil via l'antenne de réception (illustration [ref:e_antenne_einstrahlung]) ou directement à travers un boîtier insuffisamment blindé (illustration [ref:e_direkteinstrahlung]), ce qui entraîne des perturbations.
- On parle d'*afflux* lorsque la haute fréquence parvient dans un appareil via des câbles ou lignes, par exemple via l'alimentation secteur, la ligne d'antenne, les câbles de haut-parleur, etc. (illustration [ref:e_einstroemung])

<margin>
[picture:744:e_antenne_einstrahlung:Irradiation via l'antenne de réception]
[picture:746:e_direkteinstrahlung:Irradiation directe dans un appareil]
[picture:747:e_einstroemung:Afflux via les câbles de connexion]
</margin>

<indepth>
On distingue :

1 Perturbations conduites par les lignes – elles sont transmises via des lignes électriques (par exemple, lignes secteur, lignes de signal ou de données).

2 Perturbations rayonnées (ou liées au champ) – elles se propagent sous forme d'ondes électromagnétiques dans l'espace libre.

</indepth>

[question:EJ102]
[question:EJ101]

Même lors d'une exploitation conforme à la loi d'un émetteur, des perturbations peuvent survenir sur des récepteurs situés à proximité immédiate lors de la réception d'autres fréquences. Grâce à des puissances d'émission élevées des stations radioamateur ainsi qu'à l'utilisation d'antennes à haut gain, des intensités de champ très élevées peuvent se produire localement et dans la zone de rayonnement des antennes. Ces dernières peuvent surmoduler les récepteurs et leurs étages de réception, ce qui peut entraîner une réduction de la sensibilité du récepteur, voire un blocage complet de la réception. Cela peut par exemple empêcher le bon fonctionnement des commandes de portes de garage. Les lampes LED, qui sont commandées par des capteurs capacitifs, sont également souvent influencées par les émissions. On parle alors de *surmodulation* ou de *perturbation gênante* des appareils.

[question:EJ106]
[question:EJ107]
[question:EJ103]
[question:EJ112]

Les perturbations gênantes dans le voisinage sont souvent associées à l'exploitation d'une station radioamateur. Pour prouver un éventuel lien avec les émissions de la station radioamateur, il est très utile d'évaluer et, le cas échéant, de tenir un journal des émissions et des contacts effectués. Cela permet également d'exclure que les perturbations supposées dans le voisinage ne soient pas imputables à la station radioamateur.

[question:EJ122]

Le radioamateur devrait, dans le voisinage, apporter son soutien de manière coopérative et orientée vers des solutions et proposer également des mesures correctives. Souvent, les problèmes peuvent être résolus plus facilement par un dialogue direct que par l'intervention d'autorités. Ce n'est qu'en cas d'échec de toutes les tentatives que l'on peut demander à l'antenne locale de l'Agence fédérale des réseaux d'examiner la situation. Cela devrait toutefois être le dernier recours pour résoudre le problème.

[question:EJ124]
[question:VN004]

Parmi ces efforts figurent différentes mesures, comme par exemple :

%- Réduction de la puissance d'émission de l'installation de radioamateur % Cela devrait être le dernier recours !
- Blindage des appareils ou des câbles sensibles
- Installation de filtres et de selfs de mode commun du côté réception du voisin
- Mise en place d'une mise à la terre HF efficace
- Utilisation d'antennes extérieures pour la réception

Nous allons examiner ces mesures plus en détail ci-dessous.

Pour éviter les perturbations gênantes des appareils, un radioamateur devrait toujours n'utiliser que la puissance d'émission nécessaire à une *communication satisfaisante* pour ses émissions.

[question:EJ104]
[question:EJ105]

Si plusieurs signaux de réception puissants parviennent simultanément dans une installation de réception (par exemple, en raison de la réception d'une station de télévision locale et d'une station radioamateur puissante dans le voisinage), des harmoniques indésirables et leurs produits de mélange peuvent se former dans le récepteur en raison de la surmodulation des étages de réception. On parle alors d'*intermodulation*. L'intermodulation génère des *signaux fantômes* qui n'apparaissent qu'en présence des signaux concernés.

[question:EJ120]

Même dans une chaîne stéréo éteinte, des signaux HF puissants peuvent, par redressement dans l'étage final BF sur des composants non linéaires comme des transistors, provoquer des bruits audibles dans les haut-parleurs. De plus, des contacts corrodés entre métaux (oxydes métalliques) ont la propriété de former des effets de redressement en raison de non-linéarités. Cela peut entraîner, lors des émissions de la station radioamateur, des produits de mélange indésirables côté émission ou réception, qui perturbent la réception de la télévision et de la radio.

[question:EJ113]
[question:EJ121]

Toutes les perturbations gênantes ne peuvent pas être résolues par des mesures côté émission. Souvent, l'appareil perturbé lui-même n'est pas adapté à son lieu d'utilisation, ne respecte pas les exigences légales en vigueur ou les câbles d'alimentation et les blindages ne sont pas suffisamment dimensionnés pour résister aux irradiations ou afflux haute fréquence. Dans de tels cas, il est conseillé de proposer aux personnes concernées des mesures permettant de résoudre les problèmes.

Une mesure possible consiste à blinder les modules HF par un boîtier métallique fermé.

[question:EJ108]

Si une antenne d'émission ondes courtes se trouve à proximité et parallèlement à une ligne secteur de $\qty{230}{\volt}$, des courants haute fréquence peuvent être couplés dans le réseau électrique. Pour réduire autant que possible les perturbations dans sa propre maison, il est recommandé d'utiliser une ligne de terre HF séparée pour les antennes d'émission.

[question:EJ109]
[question:EJ111]

Une autre possibilité consiste à *installer des filtres dans les câbles d'alimentation des appareils* ainsi que des *selfs de mode commun (selfs de gaine)* sur les câbles d'alimentation.

En particulier, les filtres peuvent être installés du côté de l'appareil perturbé (téléviseur, récepteur DVB-T2, récepteur DAB, etc.) dans le chemin de réception. Par exemple, l'intensité de champ d'un émetteur radioamateur ondes courtes (par exemple dans la plage de $\qtyrange{3}{30}{\mega\hertz}$) peut perturber la réception de la télévision (par exemple $\qtyrange{470}{690}{\mega\hertz}$). L'installation d'un filtre passe-haut permet de réduire considérablement l'influence du signal d'émission radioamateur : les composantes de fréquence en dehors de la plage de réception de la télévision – dans cet exemple, les ondes courtes – sont supprimées, de sorte que les étages de réception de l'appareil ne peuvent plus être surmodulés.

[question:EJ116]
[question:EJ117]

Souvent, le signal d'émission d'une station radioamateur située à proximité est couplé dans d'autres appareils ou récepteurs perturbés via le blindage des câbles coaxiaux ou des câbles d'alimentation. Si des perturbations se produisent, il est conseillé d'installer une *self de mode commun* sur les câbles d'alimentation de l'appareil perturbé. Une self de mode commun bloque les *courants de gaine* sur la gaine et le conducteur intérieur de l'appareil perturbé. On utilise généralement des noyaux toroïdaux ou des noyaux à pince en ferrite comme selfs de mode commun. Une autre possibilité pour éviter les perturbations sur les lignes de commande d'installations et d'appareils électriques consiste à utiliser des câbles de commande blindés (par exemple pour les interphones, les lignes téléphoniques, etc.).

[question:EJ118]
[question:EJ119]
[question:EJ115]
[question:EJ114]

%De mauvaises conditions de réception du côté de l'appareil perturbé (par exemple antenne de télévision d'intérieur pour la réception) peuvent également faciliter les perturbations de réception. Une contre-mesure possible serait d'utiliser une antenne extérieure, éventuellement avec des préfiltres appropriés.

%[question:EJ123]