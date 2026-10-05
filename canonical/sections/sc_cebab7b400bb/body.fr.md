Dans la section [sec:stoerungen_elektronischer_geraete_1], nous avons déjà appris à connaître les perturbations typiques des appareils et installations électroniques – par exemple par rayonnement direct dans le boîtier ou par couplage dans les câbles d'alimentation – ainsi que les mesures et comportements appropriés pour y remédier. Dans cette section, nous allons approfondir un peu plus ces aspects.

[question:AJ105]

Si des interférences de réception se produisent sur des récepteurs numériques construits par soi-même, une cause possible peut en être un blindage insuffisant du récepteur. Il est alors judicieux de monter la carte de circuit imprimé du récepteur dans un boîtier métallique mis à la masse. Un bon blindage est absolument nécessaire, en particulier pour les récepteurs SDR ou les solutions de construction personnelle en technologie SDR, afin d'éviter les rayonnements indésirables. Inversement, cela réduit également les rayonnements indésirables émis par ces appareils.

[question:AJ103]

---

Dans la section [sec:stoerungen_vermeiden], nous nous sommes déjà intéressés aux couplages dans les câbles d'alimentation secteur. Il existe cependant une autre mesure corrective que nous allons examiner de plus près ci-après. Si des perturbations pénètrent via le câble d'alimentation secteur, l'installation d'un filtre secteur sous la forme d'un filtre passe-bas (cf. figure [ref:a_netzfilter] et figure [ref:a_netzfilter_draw]) est recommandée. Ces filtres sont disponibles en tant qu'appareils finis, en respectant les prescriptions VDE.

[question:AJ116]
[question:AJ117]
[question:AJ118]

<margin>
[photo:244:a_netzfilter:Filtre secteur]
[picture:367:a_netzfilter_draw:Circuit d'un filtre secteur]
</margin>

Différentes méthodes de transmission ont, en raison de leurs caractéristiques de modulation, des effets différents concernant les perturbations des appareils et des câbles. En particulier, les modes de modulation CW et SSB (dont l'amplitude change rapidement) provoquent souvent des perturbations dans les câbles des haut-parleurs et une rectification ultérieure de la haute fréquence au niveau des jonctions base-émetteur dans la partie BF des amplificateurs. La jonction base-émetteur se comporte ici comme une diode et redresse la haute fréquence. Le signal BF ainsi démodulé devient alors audible dans les haut-parleurs.

[question:AJ107]
[question:AJ106]

Pour protéger les récepteurs DVB-T contre les signaux puissants d'un émetteur radioamateur VHF/UHF à proximité immédiate, un filtre passe-haut doit être installé dans le câble d'antenne du récepteur DVB-T. Ceci n'est cependant efficace qu'avec des antennes de réception passives. En particulier, les préamplificateurs d'antenne TV non sélectifs sont rapidement surmodulés par les signaux d'émission voisins, car ils amplifient une large bande de fréquences.
Pour les antennes de réception actives, un filtre passe-haut doit être installé avant le préamplificateur d'antenne.
Lors de l'installation de filtres, il faut également tenir compte de l'affaiblissement d'insertion des filtres dans la bande passante. Celui-ci doit être aussi faible que possible et ne pas dépasser $\qtyrange{2}{3}{\dB}$ pour laisser passer le signal reçu souhaité aussi librement que possible.

[question:AJ113]
[question:AJ114]
[question:AJ108]

En principe, il est judicieux d'installer derrière un émetteur ondes courtes puissant un filtre passe-bas avec une fréquence de coupure de $\qtyrange{30}{40}{\mega\hertz}$. L'utilisation d'un accordeur d'antenne en configuration passe-bas (filtre Pi ou LC) peut également produire un effet passe-bas qui supprime efficacement les émissions d'harmoniques.

[question:AJ112]
[question:AJ104]

Les signaux d'émission puissants d'une station radioamateur peuvent provoquer chez les récepteurs DAB, TV et FM des interférences de réception, des bruits parasites ou des coupures/artefacts/silence (en particulier pour les récepteurs numériques comme DAB/DVB-T). Ces perturbations sont souvent causées par la surmodulation de l'entrée du récepteur due à des niveaux de signal élevés sur le lieu de réception et entraînent une réduction de la sensibilité du récepteur ou une surmodulation de l'étage d'entrée du récepteur.

[question:AJ110]
[question:AJ111]
[question:AJ109]

Pour éviter les problèmes mentionnés ci-dessus, le radioamateur doit donc toujours travailler avec la puissance d'émission minimale nécessaire pour une communication satisfaisante.

[question:AJ101]

Pour découpler les perturbations haute fréquence dans les circuits et appareils, on utilise souvent des condensateurs de découplage. Ceux-ci doivent avoir la propriété de dériver la haute fréquence vers la masse aussi efficacement que possible. Les condensateurs céramiques conviennent particulièrement bien à cet effet. Les condensateurs électrolytiques et à film plastique ne sont pas adaptés, car leur structure enroulée leur confère une inductance propre élevée. Pour les condensateurs au tantale, un condensateur céramique est souvent connecté en parallèle en raison de ses meilleures propriétés de dérivation haute fréquence, car ils ne sont seuls adaptés qu'aux fréquences HF moyennes jusqu'à environ $\qty{30}{\mega\hertz}$ et les condensateurs céramiques peuvent découpler des fréquences bien plus élevées.
Pour dériver efficacement les perturbations haute fréquence, une mise à la masse efficace avec une faible impédance doit être présente.

[question:AJ119]
[question:AJ102]

Dans les câbles d'alimentation électrique des étages haute fréquence, on utilise souvent des selfs haute fréquence. Celles-ci représentent une impédance longitudinale pour la haute fréquence et bloquent efficacement les courants entrants haute fréquence dans les étages ainsi que les retours haute fréquence vers l'alimentation électrique des étages.
En raison de leur structure enroulée, ces selfs ont également des capacités propres, de sorte qu'avec leur inductance, elles forment des points de résonance indésirables (circuits oscillants). Cela peut entraîner dans les étages haute fréquence des *résonances parasites*, provoquées par les *résonances propres* des selfs haute fréquence. Les résonances parasites peuvent influencer négativement les caractéristiques des étages haute fréquence. Cela peut entraîner des effets de rétroaction indésirables, en particulier dans les amplificateurs, ainsi que des creux dans les caractéristiques de puissance des étages haute fréquence.

[question:AJ214]
