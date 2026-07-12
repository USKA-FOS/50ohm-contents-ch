Idéalement, les courants à travers le conducteur intérieur et extérieur d'un câble coaxial sont exactement de même grandeur et de direction opposée. Leur somme est donc nulle et on parle alors d'un signal *en opposition de phase* pur. C'est exactement dans ce cas que des ondes de surface n'apparaissent pas.

Si la somme du signal est par contre différente de zéro, alors un signal dit *en phase* est présent. La composante en phase d'un courant dans le câble coaxial circule toujours sur la face extérieure du conducteur extérieur et est donc un courant de surface avec une onde de surface associée autour du câble coaxial.

[question:AG425]

Nous avons déjà appris qu'un câble coaxial enroulé autour d'un noyau de ferrite est adapté pour la suppression des ondes de surface. Il s'agit d'une forme de la soi-disant *bobine à compensation de courant*.

Une bobine est une inductance qui doit bloquer les courants à haute fréquence. La bobine à compensation de courant est une forme de construction de la bobine d'inductance, dans laquelle deux enroulements séparés sont enroulés sur le même noyau magnétique. Dans ce cas, la bobine à compensation de courant est connectée de telle sorte que les signaux en opposition de phase, c'est-à-dire les signaux pour lesquels le courant dans un enroulement est exactement opposé à celui de l'autre enroulement et sinon de même grandeur, n'induisent pas de champ magnétique dans le noyau. La bobine à compensation de courant laisse donc passer les signaux en opposition de phase sans entrave. Les composantes en phase, c'est-à-dire par exemple les courants qui ne circulent que sur le conducteur extérieur et donc dans un seul enroulement, sont bloquées par l'inductance.

[question:AG426]

---

Une alternative à la bobine à compensation de courant est un transformateur de séparation HF. Comme les enroulements primaire et secondaire ne sont pas connectés entre eux, un courant qui entre dans le transformateur de séparation à une borne (au moins approximativement) doit également ressortir de l'autre borne avec la même grandeur. Une composante en phase est donc exclue.

<indepth>
Comme une capacité se forme entre les spires de la bobine d'un transformateur de séparation et que la bobine forme également une capacité par rapport à l'autre bobine, un transformateur de séparation ne supprime pas non plus complètement la composante en phase d'un signal.
</indepth>

[question:AJ115]

Si un câble coaxial est exempt de signaux HF en phase, alors le conducteur extérieur ne présente aucune tension haute fréquence par rapport à la terre. Cela est dû au fait que pour un signal en opposition de phase, c'est-à-dire des courants opposés dans le conducteur intérieur et extérieur, un champ électrique se forme exclusivement entre le conducteur intérieur et extérieur. De l'extérieur, les effets des deux courants s'annulent, car ils donnent zéro en somme. La présence d'ondes de surface est donc directement liée à la présence de tensions HF sur le conducteur extérieur.

C'est précisément de telles tensions sur le conducteur extérieur qui se produisent, par exemple, lorsque nous connectons une antenne symétrique au câble, car au point d'alimentation, chaque branche du dipôle présente une tension par rapport à la terre. Si nous connectons les branches respectivement à un conducteur du câble coaxial, le conducteur extérieur présentera également une tension par rapport à la terre.

Les antennes bien mises à la terre, par exemple une antenne Groundplane avec de nombreux radiaux bien accordés ou enterrés, présentent au point d'alimentation des radiaux une tension presque nulle par rapport à la terre. Les antennes Groundplane mal mises à la terre, en revanche, peuvent être sensibles aux ondes de surface.

Une autre possibilité pour laquelle des ondes de surface peuvent se produire est par couplage sans contact dans le blindage coaxial. Par exemple, si l'on guide un câble d'alimentation parallèlement à une branche de dipôle, un couplage se produit par le champ proche électromagnétique de l'antenne.

[question:AG427]

Dans le cas d'antennes complètement symétriques, un soi-disant balun de tension peut être utilisé pour symétriser les courants dans le câble coaxial. Une forme de construction populaire est un transformateur d'autotransformateur, dans lequel le câble coaxial est connecté au milieu et à l'extrémité d'une bobine, et l'antenne est connectée aux deux extrémités de la bobine.

% TODO: Image du balun de tension / transformateur d'autotransformateur

Dans cette forme de construction, en plus de la symétrisation souhaitée, il y a également un doublement de la tension ($ü = 2$) ainsi qu'une division correspondante du courant, ce qui correspond à une transformation d'impédance de 1:4, c'est-à-dire qu'une antenne avec une résistance d'alimentation de $\qty{200}{\ohm}$ doit être connectée à un câble coaxial de $\qty{50}{\ohm}$.

[question:AG421]
[question:AG422]

Cette forme de construction n'est cependant adaptée pour supprimer les ondes de surface que si l'antenne connectée se comporte effectivement de manière symétrique et n'est pas chargée de manière asymétrique en raison d'influences environnementales.

Tous les composants qui servent à la suppression des ondes de surface ont en commun qu'un couplage "sans contact" peut encore se produire via les champs proches électromagnétiques des antennes directement sur le blindage coaxial, c'est-à-dire derrière le blocage des ondes de surface. Ici, par exemple, une autre barrière supplémentaire aux ondes de surface avec un certain éloignement de l'antenne peut aider.

[question:AG428]
[question:AG429]