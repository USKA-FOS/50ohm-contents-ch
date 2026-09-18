% TODO : Lorsque le catalogue de questions 4 sera disponible, certaines questions disparaîtront !

Nous avons déjà abordé la résistance électrique dans le contexte de la loi d'Ohm. Les résistances peuvent être réalisées à partir de différents matériaux. C'est pourquoi on distingue plusieurs types de matériaux résistifs, par exemple :

- Résistances bobinées
- Résistances à couche de carbone
- Résistances à couche métallique
- Résistances à couche d'oxyde métallique
- ...

<margin>
| l : Résistance | X : Propriété |
| Résistances bobinées | Résistances de puissance pour basses fréquences |
| Résistances à couche métallique | Faibles tolérances de fabrication et faible dépendance en température, résistances de précision |
| Résistances à couche d'oxyde métallique | Pour les fréquences supérieures à $\qty{30}{\mega\hertz}$ |
[table:e_eigenschaften_widerstaende:Vue d'ensemble des propriétés]
</margin>

Nous allons maintenant examiner ces matériaux plus en détail – un résumé est disponible dans le tableau [ref:e_eigenschaften_widerstaende].

Les *résistances bobinées* comptent parmi les plus anciennes formes de résistances électriques. Grâce à leurs propriétés avantageuses – comme une grande capacité de surcharge et un faible coefficient de température – elles sont encore utilisées aujourd'hui. Elles sont souvent appelées résistances à enroulement, car un fil de résistance isolé (par exemple en manganin ou constantan) est enroulé sur un support en céramique. Cependant, une résistance bobinée simple agit toujours comme une bobine et possède donc une inductance relativement élevée. Nous aborderons les bobines plus en détail dans un chapitre ultérieur ; pour l'instant, retenons que cela rend l'impédance de la résistance dépendante de la fréquence. En radiofréquence, ce comportement est généralement indésirable. C'est pourquoi les résistances bobinées conviennent surtout comme résistances de puissance pour le courant continu ou pour des applications à basses fréquences.

%EC101 Résistance de puissance, basses fréquences → Résistance bobinée
[question:EC101]

Dans les *résistances à couche de carbone*, une fine couche de carbone est vaporisée sur un support. Les résistances à couche de carbone sont économiques, mais présentent une tolérance de fabrication relativement importante.

Les *résistances à couche d'oxyde métallique* utilisent un matériau résistif sous forme de fine couche déposée sur un support. Ce type de résistance est largement exempt d'inductance parasite et présente une bonne stabilité thermique, ce qui le rend particulièrement adapté aux applications à fréquences élevées, au-dessus de $\qty{30}{\mega\hertz}$.

%EC103 Exempt d'inductance parasite, 30 MHz → Résistance à couche d'oxyde métallique
[question:EC103]

Les *résistances à couche métallique* peuvent être fabriquées avec une grande précision, c'est-à-dire avec une faible tolérance de fabrication. Elles conviennent comme résistances de précision. Elles sont indépendantes de la température, mais moins exemptes d'inductance parasite.

%EC102 Résistance de précision → Résistance à couche métallique
[question:EC102]

Les antennes artificielles, ou charges fictives (dummy loads), ont déjà été abordées dans la classe N. Pour les hautes fréquences (par exemple VHF), il est recommandé de construire une charge fictive de préférence avec des résistances à couche d'oxyde métallique non bobinées. Pour les fréquences plus basses (par exemple $\qty{50}{\mega\hertz}$ ou $\qty{28}{\mega\hertz}$), des résistances à couche de carbone peuvent également être utilisées. L'essentiel est que la résistance ne possède pas de spires, donc pas d'inductance propre, et ne se comporte donc pas comme une bobine parasite, car une telle inductance rendrait la valeur de la résistance dépendante de la fréquence – ce qui est précisément indésirable pour une charge fictive. La résistance doit toujours être d'environ $\qty{50}{\ohm}$ indépendamment de la fréquence. C'est pourquoi il ne faut *pas* utiliser de résistances bobinées. De plus, la capacité parasite doit être aussi faible que possible pour cette raison. Enfin, les résistances utilisées doivent être suffisamment résistantes à la température, car elles transforment la puissance absorbée en chaleur.

%EC107 Charge fictive
[question:EC107]
%EC104 Charge fictive
[question:EC104]

Pour résoudre les questions suivantes, il faut savoir que dix résistances de $\qty{500}{\ohm}$ montées en parallèle donnent une résistance totale de $\qty{50}{\ohm}$. Nous aborderons ce principe plus en détail dans un chapitre ultérieur, lorsque nous parlerons des montages en série et en parallèle de résistances.

%EC106
[question:EC106]
%EC105 Charge fictive
[question:EC105]