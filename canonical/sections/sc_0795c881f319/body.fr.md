% TODO: Lorsque le catalogue de questions 4 arrive, certaines questions disparaîtront ici ! 

Nous avons déjà rencontré la résistance électrique dans le cadre de la loi d'Ohm. Les résistances peuvent être réalisées à partir de différents matériaux. C'est pourquoi on distingue différents matériaux de résistance, par exemple :

- Résistances filaires
- Résistances à couche de carbone
- Résistances à couche métallique
- Résistances à couche d'oxyde métallique
- ...

<margin>
| l: Résistance | X: Propriété |
| Résistances filaires | Résistances haute puissance pour basses fréquences |
| Résistances à couche métallique | Faibles tolérances de fabrication et dépendance à la température, résistances de précision |
| Résistances à couche d'oxyde métallique | Pour des fréquences supérieures à $\qty{30}{\mega\hertz}$ |
[table:e_eigenschaften_widerstaende:Vue d'ensemble des propriétés]
</margin>

Dans ce qui suit, nous nous intéressons plus en détail à ces matériaux - un résumé est donné dans le tableau [ref:e_eigenschaften_widerstaende].

*Les résistances filaires* comptent parmi les plus anciennes formes de résistances électriques. En raison de leurs propriétés avantageuses - telles qu'une surcharge élevée et un faible coefficient de température - elles sont encore utilisées aujourd'hui. Elles sont souvent appelées résistances bobinées, car un fil de résistance isolé par du vernis, par exemple en manganine ou en constantan, est enroulé sur un corps de bobinage en céramique. Une résistance filaire simplement bobinée agit cependant toujours comme une bobine et possède donc une inductance relativement élevée. Nous reviendrons plus en détail sur les bobines dans un chapitre ultérieur ; il convient toutefois de mentionner ici que cela rend l'impédance de la résistance dépendante de la fréquence. En technique radio, ce comportement est généralement indésirable. C'est pourquoi les résistances filaires conviennent principalement comme résistances haute puissance pour le courant continu ou pour des applications à basses fréquences.

EC101 Haute puissance, basses fréquences -> Résistance filaire
[question:EC101]

Dans les résistances à couche de carbone, une fine couche de carbone est déposée sur un support en tant que matériau de résistance. Les résistances à couche de carbone sont peu coûteuses, mais présentent une tolérance de fabrication relativement grande.

Dans les *résistances à couche d'oxyde métallique*, le matériau de résistance est appliqué sous forme d'une fine couche sur un matériau support. Ce type de résistance est largement sans induction et présente une bonne stabilité thermique, ce qui le rend particulièrement adapté à une utilisation à des fréquences plus élevées supérieures à $\qty{30}{\mega\hertz}$.

EC103 sans induction 30 MHz -> Oxyde métallique
[question:EC103]

*Les résistances à couche métallique* peuvent être fabriquées avec une grande précision, c'est-à-dire avec une faible tolérance de fabrication. Elles conviennent comme résistances de précision. Elles sont indépendantes de la température, mais moins sans induction.

EC102 Résistance de précision > Résistance à couche métallique
[question:EC102]


Nous avons déjà rencontré les antennes artificielles, c'est-à-dire les charges fictives, dans la classe N. Pour les hautes fréquences (par exemple, VHF), il est recommandé de construire une charge fictive de préférence à partir de résistances à couche d'oxyde métallique non bobinées. Pour les fréquences plus basses (par exemple, $\qty{50}{\mega\hertz}$ ou $\qty{28}{\mega\hertz}$), des résistances à couche de carbone peuvent également être utilisées. L'essentiel est que la résistance ne présente pas de spires, donc pas d'inductance propre, et ne fonctionne donc pas comme une bobine parasite, car une telle inductance rendrait la valeur de la résistance dépendante de la fréquence - c'est exactement ce qui est indésirable dans une charge fictive. La résistance doit être d'environ $\qty{50}{\ohm}$ indépendamment de la fréquence. C'est pourquoi _aucune_ résistance filaire ne doit être utilisée. De plus, la capacité propre doit être aussi faible que possible pour cette raison. En outre, les résistances utilisées doivent être suffisamment résistantes à la température, car elles convertissent la puissance absorbée en chaleur.

EC107 DL
[question:EC107]
EC104 DL
[question:EC104]

Pour résoudre les questions suivantes, il faut savoir que dix résistances branchées en parallèle, chacune de $\qty{500}{\ohm}$, donnent ensemble une résistance totale de $\qty{50}{\ohm}$. Nous reviendrons plus en détail sur cette relation dans un chapitre ultérieur, lorsque nous parlerons des circuits en série et en parallèle de résistances.

EC106
[question:EC106]
EC105 DL
[question:EC105]