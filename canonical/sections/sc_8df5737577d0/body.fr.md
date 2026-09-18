Dans le chapitre [sec:unerwuenschte_aussendungen_1], nous avons déjà abordé les émissions indésirables. Ces émissions doivent absolument être évitées, ce qui peut être réalisé grâce à différentes mesures techniques – nous allons examiner celles-ci de plus près dans cette leçon. Les émissions indésirables proviennent souvent, dans les émetteurs radio, d’*harmoniques*, c’est-à-dire des multiples entiers de la fréquence fondamentale, ainsi que d’émissions dites *secondaires*, comme illustré dans la figure [ref:e_unerwuenschte_aussendungen_uebersicht]. Nous nous concentrons d’abord sur les harmoniques, car elles peuvent perturber ou interférer avec d’autres services de radiocommunication. On parle d’*interférence* lorsqu’une station de radioamateur émet des composantes de fréquence indésirables avec une intensité telle que les valeurs limites autorisées sont dépassées. Un exemple typique est l’émission d’une harmonique supérieure d’un transceiver dans la bande de radiodiffusion FM, comme illustré dans la figure [ref:e_unerwuenschte_aussendungen_oberwelle]. Ici, la fréquence quadruple (\qty{145,9}{\mega\hertz} \cdot 4 = \qty{583,6}{\mega\hertz}) de la fréquence fondamentale entraîne une perturbation. Les émissions secondaires seront abordées à la fin de cette leçon.


<margin>
[picture:1008:e_unerwuenschte_aussendungen_uebersicht:Émissions indésirables causées par des harmoniques (OW) et des émissions secondaires (NA)]
</margin>

<margin>
[picture:745:e_unerwuenschte_aussendungen_oberwelle:Perturbation de la réception DVB-T2 d’un téléviseur par l’harmonique d’une émission de radioamateur]
</margin>

---


La mesure des émissions indésirables d’un émetteur se fait – contrairement à la mesure de la PEP – toujours à la sortie de l’émetteur, en incluant éventuellement le ROS-mètre utilisé, les dispositifs d’adaptation supplémentaires et les filtres passe-bas éventuellement employés (cf. figure [ref:e_unerwuenschte_aussendungen_trx]).
Cela permet de s’assurer que seules les émissions indésirables pouvant atteindre l’antenne sont mesurées. L’instrument le plus adapté pour cette mesure est un analyseur de spectre. La manière exacte de réaliser cette vérification, l’aspect du spectre de fréquence des harmoniques et les prescriptions légales applicables seront abordés plus en détail dans la classe A.

<margin>
[picture:917:e_unerwuenschte_aussendungen_trx:Mesure des émissions indésirables]
</margin>

[question:EJ209]


Un signal d’émission idéal, qui n’émet que sur une fréquence souhaitée, devrait être un sinus parfait. Ce dernier ne contient, en dehors de la fréquence fondamentale, aucune autre composante de fréquence.

[question:EJ201]


<indepth>
Les formes d’onde qui ne sont pas sinusoïdales et qui présentent notamment des "angles vifs" sont composées de nombreuses sinusoïdes de fréquences différentes et contiennent donc de nombreuses composantes harmoniques. En particulier lorsque les émetteurs sont surmodulés, des signaux auparavant sinusoïdaux sont souvent déformés ou leur amplitude est tronquée. Cela génère également des composantes harmoniques importantes. Toute déviation par rapport à une forme sinusoïdale idéale doit donc être évitée pour des signaux d’émission idéaux. Ce sujet sera examiné plus en détail dans la classe A. Cependant, cette problématique peut déjà être testée avec cette applet.
[include:fourier]

</indepth>

---


Pour supprimer les harmoniques, on utilise généralement des *filtres d’harmoniques* en bande HF. Leur caractéristique est conçue de telle sorte que les fréquences inférieures à une certaine *fréquence de coupure* passent presque sans atténuation, tandis que les fréquences supérieures à cette limite ne sont pas ou très peu transmises. Un *filtre d’harmoniques* est donc un *filtre passe-bas*, comme nous l’avons déjà vu dans le chapitre sur les circuits oscillants. La *réponse en fréquence* d’un tel filtre passe-bas est illustrée dans la figure [ref:e_ua_tiefpass]. La figure [ref:e_ua_tiefpass_selbstbau] montre un filtre passe-bas fabriqué maison, composé de condensateurs et de bobines enroulées sur des noyaux toroïdaux. Lorsqu’on change de bande sur un émetteur multibande, on sélectionne généralement un filtre d’harmoniques adapté. Souvent, un clic de relais est audible, indiquant cette commutation.


L’importance de ce sujet se reflète dans le grand nombre de questions d’examen qui y sont consacrées. Grâce aux connaissances sur les harmoniques et les filtres passe-bas, ces questions peuvent cependant être facilement résolues.

<margin>
[picture:591:e_ua_tiefpass:Réponse en fréquence d’un filtre passe-bas]
</margin>

<margin>
[photo:320:e_ua_tiefpass_selbstbau:Filtre passe-bas fabriqué maison]
</margin>

---


[question:EJ202]
[question:EJ204]
[question:EJ205]
[question:EJ206]
[question:EJ207]
[question:EJ208]
[question:EJ203]


<indepth>
[picture:593:bandpass:Réponse en fréquence d’un filtre passe-bande]


Une autre possibilité de supprimer les harmoniques consiste à utiliser un *filtre passe-bande*. Les filtres passe-bande sont fréquemment employés dans les émetteurs monobande ainsi que dans les émetteurs pour les bandes VHF/UHF/SHF. Dans ces cas, il faut souvent aussi supprimer les composantes de signal qui apparaissent lors de la préparation du signal d’émission et qui peuvent se situer en dessous de la fréquence d’émission.
</indepth>


Comme mentionné précédemment, les signaux sinusoïdaux sont essentiels pour éviter les composantes harmoniques. Cela est notamment réalisé en veillant à ce que les étages d’émission, en particulier les *étages finaux* d’un émetteur, fonctionnent sans distorsion. Après un nouveau réglage du point de fonctionnement d’un étage final d’émetteur, il est impératif de vérifier sa linéarité et la qualité de l’émission en termes de faible teneur en harmoniques.

[question:EF404]


Les émissions indésirables peuvent également apparaître à proximité immédiate du signal d’émission proprement dit (cf. figure [ref:e_unerwuenschte_aussendungen_uebersicht]) et concernent ainsi souvent d’autres radioamateurs sur la même bande. Ces interférences sont difficiles, voire impossibles à supprimer avec des filtres et doivent donc être évitées dès la préparation du signal par des mesures appropriées. Ces *émissions secondaires* – aussi appelées *produits secondaires* et désignées familièrement par le terme "splatter" – sont souvent causées par un réglage trop élevé de l’amplificateur microphonique de l’émetteur, ce qui élargit involontairement le signal d’émission.

[question:EJ213]
[question:EJ214]


Il en va de même pour les procédés de transmission numériques, comme par exemple le Packet Radio. Pour éviter les émissions secondaires et les dépassements de la bande passante autorisée, on peut notamment, dans le cas des émetteurs FM modulés AFSK, limiter l’excursion ou réduire la modulation BF.

[question:EJ212]


La stabilité de l’oscillateur utilisé dans l’émetteur peut également entraîner des émissions en dehors des limites de bande ou perturber des stations voisines. Cela est particulièrement possible avec les anciens appareils de construction amateur sans oscillateurs stabilisés par quartz. Les émetteurs-transcepteurs modernes en bande HF, mais aussi les appareils et kits de construction récents, disposent généralement d’oscillateurs de référence très stables.

[question:EJ216]