Comme nous l'avons déjà appris, les batteries fournissent une tension électrique parce que des charges y sont séparées. Cela est réalisé par des processus électrochimiques. Ceux-ci se produisent dès que le circuit est fermé. Les accumulateurs, appelés couramment Akkus, fonctionnent de manière très similaire. Ils ont cependant la particularité d'être rechargeables. Pour cela, une tension est appliquée à la batterie et la réaction électrochimique se produit en sens inverse. Ensuite, la décharge peut recommencer. Les batteries, en revanche, ne peuvent pas être rechargées, mais ne sont utilisables qu'une seule fois.

Dans les appareils radio portatifs, on utilise généralement des Akkus, parfois des batteries. Pour faire fonctionner des stations radio indépendamment du réseau électrique, par exemple lors d'un Fieldday, on utilise souvent des Akkus.

L'inscription sur les batteries (figure [ref:n_Bat_AA]) indique par exemple le pôle positif ou négatif et attire l'attention sur l'utilisation correcte de la polarité. Pour les batteries, l'avertissement "Non rechargeable" doit toujours être pris en compte.

La figure [ref:n_schaltzeichen_batt] montre le symbole de circuit d'une batterie ou d'un Akku. La ligne longue dans le symbole de circuit indique le pôle positif, la ligne courte le pôle négatif. Comme aide-mémoire, on peut retenir qu'un signe plus nécessite deux traits, tandis qu'un signe moins n'en nécessite qu'un seul.

[question:NB201]
[question:NB203]

<margin>
[photo:89:n_Bat_AA:Une batterie avec indication des pôles et avertissements]
</margin>

<margin>
[picture:517:n_schaltzeichen_batt:Symbole de circuit d'une batterie]
</margin>

<webindepth>
Il existe différentes batteries et Akkus avec diverses tensions, capacités et formes de construction:
* Les indications de tension courantes pour les batteries ou les Akkus sont par exemple $\qty{1,5}{\volt}$ ou $\qty{9}{\volt}$. Il en existe cependant aussi avec d'autres tensions. Les voitures télécommandées utilisent par exemple généralement $\qty{7,2}{\volt}$. Dans les outils alimentés par batterie, on trouve souvent des Akkus avec $\qty{18}{\volt}$, $\qty{20}{\volt}$ ou $\qty{40}{\volt}$.
* La capacité d'une batterie ou d'un Akku est indiquée en ampère-heure ($\unit{\ampere\hour}$). Si un Akku a une capacité de $\qty{5}{\ampere\hour}$, il peut laisser passer un courant d'un ampère pendant 5 heures - ou par exemple aussi un courant de 0,5 ampère pendant 10 heures ou un courant de $\qty{5}{\ampere}$ pendant seulement une heure. Pour les batteries, l'indication de la capacité fait souvent défaut. Les batteries courantes ont souvent une capacité de moins de $\qty{5}{\ampere\hour}$. Les grands Akkus peuvent également avoir une capacité de $\qty{100}{\ampere\hour}$ ou plus. Contrairement aux batteries, la capacité est pratiquement toujours indiquée pour les Akkus.
* En ce qui concerne les formes de construction, les piles cylindriques AA et AAA sont très connues, utilisées dans la plupart des appareils ménagers. Mais il existe toutes sortes de formes de construction, surtout pour les Akkus. Souvent même des formes de construction qui ne conviennent que pour un seul appareil.
</webindepth>

<margin>
[photo:209:batterien_und_akkus_sammlung:Différentes batteries et Akkus]
</margin>

<attention>
Les Akkus ne doivent jamais être complètement déchargés. Cette décharge profonde peut endommager l'Akku. En pratique, on peut reconnaître la décharge par le fait que la tension de l'Akku diminue légèrement au fil du temps. Le prélèvement de courant doit être arrêté avant que la tension minimale indiquée par le fabricant ne soit sous-dépassée.
</attention>

De nombreux appareils nécessitent plusieurs batteries. En règle générale, cela sert à augmenter la tension lorsque la tension d'une seule batterie, par exemple de $\qty{1,5}{\volt}$, n'est pas suffisante pour le fonctionnement. Dans le compartiment à batteries de l'appareil, celles-ci sont connectées en série, de sorte que le pôle négatif de la batterie précédente rencontre chaque fois le pôle positif de la suivante. La tension aux extrémités de cette chaîne se calcule comme suit:

$\text{Tension crête à crête} = \text{Nombre de batteries} \cdot \text{Tension de la batterie}$

[question:NB204]

---

En général, il faut éviter un court-circuit avec les batteries et les Akkus. Surtout avec les Akkus modernes et performants, il existe un risque de surchauffe. Ceux-ci peuvent prendre feu ou provoquer un incendie par le courant de court-circuit qui en résulte.

<danger>
Alors que dans les alimentations secteur, un fusible peut arrêter le flux de courant en cas de défaut, ce mécanisme de protection fait généralement défaut dans les batteries ou les Akkus. L'intensité du courant que les batteries et les Akkus peuvent fournir dépasse souvent de plusieurs fois le courant maximal des alimentations secteur. Cela s'applique en particulier aux Akkus très capacitifs comme par exemple les batteries de voiture, qui peuvent fournir un courant de $\qty{1000}{\ampere}$ et plus pendant un court instant. Lors de l'utilisation d'Akkus externes très capacitifs, il faut absolument prévoir une protection supplémentaire, comme celle montrée par exemple dans la figure [ref:n_Bat_Sicherung]!
[photo:90:n_Bat_Sicherung:Boîte de connexion avec fusibles automobiles et sorties protégées contre l'inversion de polarité pour la protection des Akkus puissants]
</danger>

[question:ND110] 

Différentes technologies sont utilisées pour les Akkus, qui sont basées sur diverses réactions électrochimiques: depuis de nombreuses décennies, des batteries au plomb sont utilisées dans les voitures. De petits appareils portables utilisaient autrefois des Akkus avec du nickel et du cadmium (NiCd) et plus tard la technologie nickel-métal hydrure (NiMH). Aujourd'hui, les Akkus à technologie lithium-ion dominent dans les téléphones mobiles, les appareils photo numériques ou les ordinateurs portables. Dans le radioamateur, on utilise de plus en plus des mélanges lithium-fer-phosphate (LiFePO4).

Les différences des réactions électrochimiques doivent être prises en compte lors de la charge de ces différents types d'Akkus. Il faut utiliser des chargeurs respectivement adaptés à la technologie. Des procédures de charge et de décharge inappropriées peuvent entraîner une surchauffe des Akkus. En cas de contact, des brûlures dangereuses peuvent alors survenir. Des explosions des Akkus et des incendies sont également possibles par surchauffe. Des brûlures chimiques ou des intoxications peuvent survenir par les liquides qui se libèrent.

<attention>
Les batteries et les Akkus doivent toujours être éliminés de manière appropriée. Ils ne doivent pas finir dans les ordures ménagères! Cela est indiqué par le symbole de la poubelle barrée (voir figure [ref:n_Bat_AA]).
</attention>

[question:NK306] 

<latexonly>
\newpage
</latexonly>