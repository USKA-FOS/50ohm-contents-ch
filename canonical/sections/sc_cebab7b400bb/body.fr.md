Dans les leçons des classes N et E, nous avons déjà abordé les perturbations typiques des appareils et installations électroniques – par exemple, par rayonnement direct dans le boîtier ou par couplage dans les câbles d’alimentation – ainsi que les contre-mesures et les bonnes pratiques adaptées. Dans la classe A, ces aspects sont approfondis davantage.

[question:AJ105]

Lorsqu’un récepteur construit par soi-même présente des perturbations de réception, une cause possible peut être un blindage insuffisant du récepteur. Il est alors conseillé d’intégrer la carte de circuit imprimé du récepteur dans un boîtier métallique mis à la masse. Cela est particulièrement important pour les récepteurs SDR ou les solutions maison utilisant la technologie SDR, où un bon blindage est indispensable pour éviter les rayonnements parasites. Inversement, cela réduit également les émissions indésirables de ces appareils.

[question:AJ103]

---

Dans la classe E, nous avons déjà traité des couplages dans les lignes secteur. Cependant, il existe une autre contre-mesure que nous allons examiner plus en détail ci-dessous. Si des perturbations pénètrent par les câbles d’alimentation secteur, l’installation d’un filtre secteur sous forme de filtre passe-bas (voir figure [ref:a_netzfilter] et schéma [ref:a_netzfilter_draw]) est recommandée. Ces filtres sont disponibles sous forme d’appareils finis, conformément aux normes VDE.

[question:AJ116]
[question:AJ117]
[question:AJ118]

<margin>
[photo:244:a_netzfilter:Filtre secteur]
[picture:367:a_netzfilter_draw:Schéma d’un filtre secteur]
</margin>

Les différentes méthodes de transmission, en raison de leurs caractéristiques de modulation, ont des effets variables sur les perturbations des appareils et des lignes. En particulier, les modes CW ainsi que SSB (pour lesquels l’amplitude varie rapidement) entraînent souvent des perturbations dans les câbles des haut-parleurs et une détection HF consécutive sur les jonctions base-émetteur dans la partie BF des amplificateurs. La jonction base-émetteur se comporte alors comme une diode et redresse la HF. Cela rend la BF ainsi démodulée audible dans les haut-parleurs.

[question:AJ107]
[question:AJ106]

Pour protéger les récepteurs DVB-T des signaux puissants d’un émetteur amateur VHF/UHF situé à proximité, il est recommandé d’installer un filtre passe-haut sur la ligne d’antenne du récepteur DVB-T. Cela n’est efficace qu’avec des antennes de réception passives. En particulier, les préamplificateurs d’antenne TV non sélectifs sont rapidement surmodulés par des signaux d’émission voisins, car ils amplifient une large bande de fréquences.
Pour les antennes actives, un filtre passe-haut doit être installé avant le préamplificateur d’antenne.
Lors de l’installation de filtres, il faut également tenir compte de l’affaiblissement d’insertion des filtres dans la bande passante. Celui-ci doit être aussi faible que possible et ne pas dépasser $\qtyrange{2}{3}{\dB}$ afin de laisser passer le signal reçu souhaité sans entrave.

[question:AJ113]
[question:AJ114]
[question:AJ108]

En règle générale, il est judicieux d’installer derrière un émetteur ondes courtes puissant un filtre passe-bas avec une fréquence de coupure de $\qtyrange{30}{40}{\mega\hertz}$. L’utilisation d’un syntoniseur d’antenne en configuration passe-bas (filtre en π ou LC) permet également d’obtenir un effet passe-bas qui supprime efficacement les émissions d’harmoniques.

[question:AJ112]
[question:AJ104]

Les signaux puissants d’une station de radio amateur peuvent provoquer des perturbations de réception, des bruits parasites ou des coupures/artefacts/mutations (notamment sur les récepteurs numériques comme DAB/DVB-T) chez les récepteurs DAB, TV et FM. Ces perturbations sont souvent causées par la surmodulation de l’entrée du récepteur par des signaux de forte intensité sur le lieu de réception, ce qui réduit la sensibilité du récepteur ou surmodule l’étage d’entrée.

[question:AJ110]
[question:AJ111]
[question:AJ109]

Pour éviter ces problèmes, l’opérateur radio doit toujours utiliser la puissance d’émission minimale nécessaire pour une communication satisfaisante.

[question:AJ101]

Pour découpler les perturbations HF dans les circuits et appareils, on utilise souvent des condensateurs de découplage. Ceux-ci doivent permettre de dériver efficacement la HF vers la masse. Les condensateurs céramiques sont particulièrement adaptés à cet usage. Les condensateurs électrolytiques et les condensateurs à film plastique sont inadaptés en raison de leur construction enroulée, qui leur confère une inductance propre élevée. Pour les condensateurs au tantale, un condensateur céramique est souvent monté en parallèle en raison de leurs meilleures propriétés de dérivation HF, car ces derniers ne conviennent que pour des fréquences HF moyennes jusqu’à environ $\qty{30}{\mega\hertz}$, tandis que les condensateurs céramiques peuvent bloquer des fréquences bien plus élevées.
Pour une dérivation efficace des perturbations HF, une mise à la masse efficace avec une impédance faible est indispensable.

[question:AJ119]
[question:AJ102]

Dans les lignes d’alimentation électrique des étages HF, on utilise souvent des selfs HF. Celles-ci présentent une impédance longitudinale pour la haute fréquence et bloquent efficacement les courants entrants HF dans les étages ainsi que les courants HF de retour dans l’alimentation des étages.
En raison de leur construction enroulée, ces selfs présentent également des capacités parasites, de sorte qu’en association avec leur inductance, elles forment des points de résonance indésirables (circuits oscillants). Cela peut entraîner dans les étages HF des *résonances parasites*, causées par les *résonances propres* des selfs HF, qui altèrent négativement les caractéristiques des étages HF. Cela peut provoquer des effets de réaction indésirables, notamment dans les amplificateurs, ainsi que des chutes dans les caractéristiques de puissance des étages HF.

[question:AJ214]