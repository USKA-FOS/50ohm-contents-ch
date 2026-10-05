Lors de l'exploitation d'émetteurs – en particulier d'émetteurs puissants – diverses perturbations des appareils et installations électroniques peuvent survenir. Nous avons déjà abordé ces *perturbations gênantes* et quelques recommandations de base dans le chapitre [sec:stoerungen_vermeiden]. L'objectif est d'éviter autant que possible ces perturbations ou d'éliminer leurs causes par des contre-mesures appropriées. Dans cette leçon, nous allons examiner de plus près les causes et les contre-mesures. Fondamentalement, les appareils électroniques peuvent être perturbés de deux manières :

- Une *irradiation directe* se produit lorsque des hautes fréquences pénètrent directement dans l'électronique d'un appareil via l'antenne de réception (figure [ref:e_antenne_einstrahlung]) ou en raison d'un boîtier insuffisamment blindé (figure [ref:e_direkteinstrahlung]), entraînant des perturbations.
- Des *courants entrants* se produisent lorsque des hautes fréquences pénètrent dans un appareil via des conducteurs ou des câbles, comme par exemple le câble d'alimentation, le câble d'antenne, les câbles de haut-parleurs, etc. (figure [ref:e_einstroemung])

<margin>
[picture:744:e_antenne_einstrahlung:Irradiation via l'antenne de réception]
[picture:746:e_direkteinstrahlung:Irradiation directe dans un appareil]
[picture:747:e_einstroemung:Courants entrants via les câbles de connexion]
</margin>

<indepth>
On distingue :
  
- Les *perturbations conduites* – elles sont transmises via des conducteurs électriques (par ex. câbles d'alimentation, de signal ou de données).
  
- Les *perturbations rayonnées (ou par champ)* – elles se propagent sous forme d'ondes électromagnétiques dans l'espace libre.
  
</indepth>

[question:EJ102]
[question:EJ101]

Même lors d'une exploitation conforme à la loi d'un émetteur, des perturbations peuvent survenir sur les récepteurs situés à proximité immédiate lors de la réception d'autres fréquences. En raison des puissances d'émission élevées des stations de radioamateur et de l'utilisation d'antennes à haut gain, des intensités de champ très élevées peuvent apparaître localement et dans la zone de rayonnement des antennes. Celles-ci peuvent surmoduler les récepteurs et leurs étages de réception, ce qui peut entraîner une réduction de la sensibilité du récepteur jusqu'au blocage complet de la réception. Cela peut par exemple empêcher les commandes de portes de garage de fonctionner normalement. Souvent, les éclairages LED, contrôlés par des capteurs capacitifs, sont également perturbés par les émissions. On parle ici de *surmodulation* ou de *perturbation gênante* des appareils.

[question:EJ106]
[question:EJ107]
[question:EJ103]
[question:EJ112]

Souvent, les perturbations gênantes dans le voisinage sont associées à l'exploitation d'une station de radioamateur. Pour prouver un éventuel lien avec les émissions de la station de radioamateur, l'analyse et, le cas échéant, la tenue d'un journal des émissions et des connexions effectuées sont très utiles. Cela peut également permettre d'exclure que les perturbations suspectées dans le voisinage soient attribuables à la station de radioamateur.

[question:EJ122]

Le radioamateur devrait, dans ce cas, apporter son soutien de manière coopérative et orientée vers des solutions au voisinage, et également formuler des propositions de remèdes. Souvent, les problèmes se résolvent plus facilement par une discussion directe que par l'intervention des autorités. Ce n'est que lorsque tous les efforts ont échoué que l'OFCOM peut être sollicité pour examiner la situation. Cela devrait toutefois être vraiment le dernier recours pour résoudre le problème.

[question:EJ124]
[question:VN004]

Ces efforts comprennent diverses mesures, telles que :

%- Réduction de la puissance d'émission de l'installation de radioamateur % Cela devrait être le dernier recours !
- Blindage des appareils ou câbles sensibles
- Installation de filtres et de selfs de mode commun du côté réception du voisin
- Mise en place d'une mise à la terre HF efficace
- Utilisation d'antennes extérieures pour la réception

Nous allons examiner ces mesures plus en détail ci-après.

Pour éviter les perturbations gênantes des appareils, un radioamateur doit toujours utiliser uniquement la *puissance d'émission nécessaire à une communication satisfaisante* pour ses émissions.

[question:EJ104]
[question:EJ105]

Si plusieurs signaux de réception forts apparaissent simultanément dans une installation de réception (par ex. en raison de la réception d'un émetteur local d'un autre service de radiocommunication et d'une station de radioamateur puissante à proximité), des harmoniques indésirables et leurs produits de mélange peuvent apparaître dans le récepteur en raison de la surmodulation des étages de réception du récepteur. On appelle cela l'*intermodulation*. L'intermodulation génère des *signaux fantômes* qui n'apparaissent qu'en présence des signaux impliqués.

[question:EJ120]

Même dans une chaîne stéréo éteinte, de forts signaux HF peuvent, par redressement dans l'étage final BF sur des composants non linéaires comme les transistors, entraîner des bruits audibles dans les haut-parleurs. Les contacts corrodés entre métaux (oxydes métalliques) ont également la propriété de pouvoir créer des effets de redressement dus à des non-linéarités. Ainsi, lors des émissions de la station de radioamateur, des produits de mélange indésirables peuvent apparaître du côté émission ou réception, ce qui peut entraîner une perturbation gênante de la réception télévisuelle et radiophonique.

[question:EJ113]
[question:EJ121]


Toutes les perturbations gênantes ne peuvent pas être résolues par des mesures du côté émission. Souvent, l'appareil perturbé lui-même n'est pas adapté au lieu d'utilisation concerné, ne respecte pas les prescriptions légales en vigueur, ou les câbles d'alimentation et les blindages ne sont pas dimensionnés de manière suffisante contre les irradiations ou courants entrants haute fréquence. Dans de tels cas, il est judicieux de proposer aux personnes concernées des mesures permettant de résoudre les problèmes.

Une mesure possible consiste à protéger les modules HF autant que possible par un boîtier métallique fermé.

[question:EJ108]

Si une antenne d'émission ondes courtes se trouve à proximité et parallèlement à un câble d'alimentation en courant alternatif de $\qty{230}{\volt}$, des courants haute fréquence peuvent être couplés dans le réseau électrique. Pour minimiser les perturbations dans sa propre maison, il est recommandé d'utiliser une mise à la terre HF séparée pour les antennes d'émission.

[question:EJ109]
[question:EJ111]

Une autre possibilité est l'*installation de filtres dans les câbles d'alimentation des appareils* ainsi que des *selfs de mode commun (bobinages d'étouffement)* sur les câbles d'alimentation.

En particulier, les filtres peuvent être installés du côté de l'appareil perturbé (TV, récepteur DVB-T2, récepteur DAB, etc.) dans le chemin de réception. Par exemple, l'intensité de champ d'un émetteur radioamateur ondes courtes (par ex. dans la plage de $\qtyrange{3}{30}{\mega\hertz}$) peut perturber la réception TV (par ex. $\qtyrange{470}{690}{\mega\hertz}$). En installant un filtre passe-haut, l'influence du signal de l'émetteur radioamateur peut être considérablement réduite : les composantes de fréquence en dehors de la plage de réception TV – dans cet exemple, les ondes courtes – sont supprimées, de sorte que les étages de réception de l'appareil ne peuvent plus être surmodulés.

[question:EJ116]
[question:EJ117]

Souvent, le signal d'émission d'une station de radioamateur située à proximité d'autres appareils est couplé dans les récepteurs ou appareils perturbés via la tresse des câbles coaxiaux ou des câbles d'alimentation. Si des perturbations surviennent à cet endroit, une *self de mode commun* doit être installée sur les câbles d'alimentation de l'appareil perturbé. Une self de mode commun bloque les *courants de mode commun* sur la tresse et le conducteur intérieur de l'appareil perturbé. Les selfs de mode commun utilisent typiquement des noyaux toroïdaux ou des noyaux à fente en ferrite. Une autre possibilité pour éviter les perturbations sur les câbles de commande d'installations et d'appareils électriques est d'utiliser des câbles de commande blindés (par ex. pour les interphones, les lignes téléphoniques, etc.)

[question:EJ118]
[question:EJ119]
[question:EJ115]
[question:EJ114]

%Des conditions de réception médiocres du côté de l'appareil perturbé (par ex. antenne TV intérieure pour la réception) peuvent également faciliter les perturbations lors de la %réception. Une contre-mesure possible serait l'utilisation d'une antenne extérieure, éventuellement avec des préfiltres appropriés.

%[question:EJ123]
