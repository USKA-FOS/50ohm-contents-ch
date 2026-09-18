Comme nous l'avons déjà appris, les batteries fournissent une tension électrique parce que des charges y sont séparées. Cela est rendu possible par des processus électrochimiques. Ceux-ci se produisent dès que le circuit électrique est fermé. Les accumulateurs, appelés plus simplement accus, fonctionnent de manière similaire. Ils ont cependant la particularité d'être rechargeables. Pour ce faire, une tension est appliquée à la batterie et la réaction électrochimique se déroule en sens inverse. Ensuite, la décharge peut recommencer. Les batteries, en revanche, ne peuvent pas être rechargées et ne sont utilisables qu'une seule fois.


Dans les talkies-walkies, on utilise généralement des accus, parfois aussi des batteries. Pour faire fonctionner des stations radio indépendamment du réseau électrique, par exemple lors d'un Fieldday, on utilise souvent des accus.


L'inscription sur les batteries (illustration [ref:n_Bat_AA]) indique par exemple le pôle positif et le pôle négatif et signale l'importance de respecter la polarité. Pour les batteries, l'avertissement "Non rechargeable" doit toujours être respecté.


L'illustration [ref:n_schaltzeichen_batt] montre le symbole de circuit d'une batterie ou d'un accus. Le trait long dans le symbole de circuit indique le pôle positif, le trait court le pôle négatif. Pour s'en souvenir, on peut retenir : un signe plus nécessite deux traits, un signe moins n'en nécessite qu'un seul.


[question:NB201]
[question:NB203]

<margin>
[photo:89:n_Bat_AA:Une batterie avec indication des pôles et des avertissements]
</margin>

<margin>
[picture:517:n_schaltzeichen_batt:Symbole de circuit d'une batterie]
</margin>

<webindepth>
Il existe toutes sortes de batteries et d'accus avec différentes tensions, capacités et formes de construction :
* Les tensions courantes pour les batteries ou les accus sont par exemple $\qty{1,5}{\volt}$ ou $\qty{9}{\volt}$. Il en existe aussi avec d'autres tensions. Les voitures radiocommandées utilisent par exemple généralement des accus de $\qty{7,2}{\volt}$. Dans les outils à batterie, on trouve souvent des accus de $\qty{18}{\volt}$, $\qty{20}{\volt}$ ou $\qty{40}{\volt}$.
* La capacité d'une batterie ou d'un accus est indiquée en ampère-heures ($\unit{\ampere\hour}$). Si un accus a une capacité de $\qty{5}{\ampere\hour}$, il peut fournir un courant d'un ampère pendant 5 heures — ou par exemple un courant de $\qty{0,5}{\ampere}$ pendant 10 heures, ou encore un courant de $\qty{5}{\ampere}$ pendant seulement une heure. Pour les batteries, la capacité n'est souvent pas indiquée. Les batteries domestiques courantes ont souvent une capacité inférieure à $\qty{5}{\ampere\hour}$. Les grands accus peuvent avoir une capacité de $\qty{100}{\ampere\hour}$ ou plus. Contrairement aux batteries, les accus indiquent presque toujours leur capacité.
* En ce qui concerne les formes de construction, les piles cylindriques AA et AAA sont très connues et utilisées dans la plupart des appareils domestiques. Il existe cependant toutes sortes de formes pour les accus, souvent même des formes spécifiques à un seul appareil.
</webindepth>

<margin>
[photo:209:batterien_und_akkus_sammlung:Différentes batteries et accus]
</margin>

<attention>
Les accus ne doivent jamais être complètement déchargés. Cette décharge profonde, appelée "tiefentladung", peut endommager l'accumulateur. En pratique, on peut reconnaître la décharge au fait que la tension de l'accumulateur diminue progressivement. L'extraction du courant doit être arrêtée avant que la tension minimale indiquée par le fabricant ne soit atteinte.
</attention>

Beaucoup d'appareils nécessitent plusieurs batteries. En général, cela sert à augmenter la tension lorsque la tension d'une seule batterie, par exemple $\qty{1,5}{\volt}$, ne suffit pas pour le fonctionnement. Dans le compartiment à piles de l'appareil, celles-ci sont montées en série, de sorte que le pôle négatif de la batterie précédente soit relié au pôle positif de la batterie suivante. La tension aux bornes de cette chaîne se calcule comme suit :


$\text{tension totale} = \text{nombre de batteries} \cdot \text{tension de la batterie}$


[question:NB204]


---


En général, il faut éviter les courts-circuits avec les batteries et les accus. Avec les accus modernes et performants, il existe un risque de surchauffe. Ils peuvent prendre feu ou provoquer un incendie à cause du courant de court-circuit généré.


<danger>
Alors que pour les alimentations secteur, un fusible peut couper le courant en cas de défaut, ce mécanisme de protection est généralement absent pour les batteries ou les accus. L'intensité du courant que les batteries et les accus peuvent fournir dépasse souvent de plusieurs fois le courant maximal des alimentations secteur. Cela vaut particulièrement pour les accus à haute capacité comme par exemple les batteries de voiture, qui peuvent fournir temporairement $\qty{1000}{\ampere}$ ou plus. Lors de l'utilisation d'accus externes à haute capacité, il est impératif de prévoir un fusible supplémentaire, comme celui montré dans l'illustration [ref:n_Bat_Sicherung] !
[photo:90:n_Bat_Sicherung:Boîtier de connexion avec fusibles automobiles et sorties protégées contre l'inversion de polarité pour la protection des accus puissants]
</danger>

[question:ND110]


Différentes technologies sont utilisées pour les accus, basées sur diverses réactions électrochimiques : depuis des décennies, les batteries au plomb sont utilisées dans les voitures. Les petits appareils portables utilisaient autrefois des accus au nickel et cadmium (NiCd) puis plus tard la technologie nickel-hydrure métallique (NiMH). Aujourd'hui, les téléphones mobiles, appareils photo numériques ou ordinateurs portables utilisent principalement des accus à technologie lithium-ion. Dans le radioamateurisme, on utilise de plus en plus des mélanges lithium-fer-phosphate (LiFePO4).


Les différences entre les réactions électrochimiques doivent être prises en compte lors de la charge de ces différents types d'accus. Il faut utiliser des chargeurs adaptés spécifiquement à chaque technologie. Des procédés de charge et de décharge inappropriés peuvent entraîner une surchauffe des accus. Au contact, cela peut provoquer des brûlures dangereuses. Des explosions ou des incendies des accus sont également possibles en cas de surchauffe. Les liquides libérés peuvent causer des brûlures chimiques ou des intoxications.


<attention>
Les batteries et les accus doivent toujours être éliminés de manière appropriée. Ils ne doivent pas être jetés avec les ordures ménagères ! Cela est signalé par le symbole de la poubelle barrée (voir illustration [ref:n_Bat_AA]).
</attention>

[question:NK306]


<latexonly>
\newpage
</latexonly>