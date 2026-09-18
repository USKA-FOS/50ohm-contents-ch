Idéalement, les courants circulant dans le conducteur intérieur et le conducteur extérieur d’un câble coaxial sont de même amplitude et de sens opposé. Leur somme est donc nulle, et on parle alors d’un *signal en mode différentiel pur*. Dans ce cas, il n’y a pas de courants de gaine.

Si la somme du signal n’est pas nulle, il y a alors un *signal en mode commun*. La composante en mode commun d’un courant dans le câble coaxial circule toujours sur la face externe du conducteur extérieur et constitue donc un courant de gaine avec une onde de gaine associée autour du câble coaxial.

[question:AG425]

Nous avons déjà appris qu’un câble coaxial enroulé autour d’un noyau en ferrite permet de supprimer les courants de gaine. Il s’agit d’une forme de *self de mode commun*.

Une bobine d’arrêt est une bobine conçue pour bloquer les courants haute fréquence. La self de mode commun est une variante de bobine d’arrêt dans laquelle deux enroulements séparés sont bobinés sur le même noyau magnétique. Cette self de mode commun est câblée de telle sorte que les signaux en mode différentiel, c’est-à-dire les signaux pour lesquels le courant dans un enroulement est exactement opposé à celui de l’autre enroulement et de même amplitude par ailleurs, n’induisent pas de champ magnétique dans le noyau. La self de mode commun laisse donc passer les signaux en mode différentiel sans entrave. En revanche, les composantes en mode commun, par exemple les courants qui ne circulent que sur le conducteur extérieur et donc uniquement dans un enroulement, sont bloquées par l’inductance.

[question:AG426]

<margin>
[picture:633:e_mantelwellen:Ondes de gaine]
</margin>

---

Une alternative à la self de mode commun est un transformateur HF d’isolement. Comme les enroulements primaire et secondaire ne sont pas connectés entre eux, un courant entrant par un pôle dans le transformateur d’isolement (au moins approximativement) doit également ressortir par l’autre pôle avec la même amplitude. Une composante en mode commun est donc exclue.

<indepth>
Comme il existe une capacité entre les spires de la bobine d’un transformateur d’isolement et que la bobine forme également une capacité par rapport à l’autre bobine, un transformateur d’isolement ne supprime pas complètement la composante en mode commun d’un signal.
</indepth>

[question:AJ115]

Si un câble coaxial est exempt de signaux HF en mode commun, le conducteur extérieur ne présente alors aucune tension haute fréquence par rapport à la terre. En effet, dans le cas d’un signal en mode différentiel, c’est-à-dire de courants opposés dans le conducteur intérieur et le conducteur extérieur, un champ électrique ne se forme qu’entre ces deux conducteurs. De l’extérieur, les effets des deux courants s’annulent, car leur somme est nulle. La présence de courants de gaine est donc directement liée à la présence de tensions HF sur le conducteur extérieur.

De telles tensions sur le conducteur extérieur apparaissent par exemple lorsque l’on connecte une antenne symétrique au câble, car à son point d’alimentation, chaque branche du dipôle présente une tension par rapport à la terre. Si l’on connecte chaque branche à un conducteur du câble coaxial, le conducteur extérieur présentera également une tension par rapport à la terre.

En revanche, les antennes bien mises à la terre, par exemple une antenne groundplane avec de nombreux radiaux bien accordés ou enterrés, présentent au point d’alimentation des radiaux une tension quasi nulle par rapport à la terre. Les antennes groundplane mal mises à la terre sont en revanche sensibles aux courants de gaine.

Une autre cause possible de courants de gaine est leur couplage sans contact dans le blindage du câble coaxial. Par exemple, si l’on fait passer un câble d’alimentation parallèlement à une branche de dipôle, il se produit un couplage via le champ proche électromagnétique de l’antenne.

[question:AG427]

Pour les antennes parfaitement symétriques, on peut utiliser un *balun de tension* pour symétriser les courants dans le câble coaxial. Une forme populaire est un autotransformateur, dans lequel le câble coaxial est connecté au milieu et à l’extrémité d’une bobine, et l’antenne est reliée aux deux extrémités de la bobine.

% TODO: Image balun de tension / autotransformateur

Avec cette configuration, en plus de la symétrisation souhaitée, la tension est doublée ($r = 2$) et le courant est divisé en conséquence, ce qui correspond à une adaptation d’impédance de 1:4, c’est-à-dire qu’une antenne avec une impédance d’alimentation de $\qty{200}{\ohm}$ doit être connectée à un câble coaxial de $\qty{50}{\ohm}$.

[question:AG421]
[question:AG422]

Cette configuration ne permet de supprimer les courants de gaine que si l’antenne connectée est effectivement symétrique et n’est pas chargée de manière asymétrique en raison d’influences extérieures.

Tous les composants servant à supprimer les courants de gaine ont en commun le fait qu’un couplage « sans contact » via les champs proches électromagnétiques des antennes peut toujours se produire directement sur le blindage du câble coaxial, c’est-à-dire en aval de la self de mode commun. Dans ce cas, une self de mode commun supplémentaire placée à une certaine distance de l’antenne peut aider.

[question:AG428]
[question:AG429]