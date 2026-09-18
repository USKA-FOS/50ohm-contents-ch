Il est également possible de répartir un flux de données sur plusieurs porteuses situées à des fréquences différentes, mais proches les unes des autres. Cependant, les porteuses ne peuvent pas être placées arbitrairement près les unes des autres, car elles présentent nécessairement une certaine largeur en raison des bandes latérales qui en résultent.

Dans le procédé de multiplexage en fréquence orthogonal (Orthogonal Frequency-Division Multiplexing, OFDM), les porteuses individuelles sont placées exactement à l'espacement où les interférences mutuelles (appelées " diaphonie ") sont évitées autant que possible.

Plus le débit de symboles par porteuse est élevé, plus l'espacement des porteuses doit être grand. C'est pourquoi on choisit souvent un débit de symboles plus faible pour chaque porteuse individuelle, afin de pouvoir utiliser davantage de porteuses côte à côte. La quantité d'informations transmise reste la même, car bien que moins d'informations puissent être transmises par porteuse, davantage de porteuses peuvent être utilisées côte à côte. Un espacement plus grand des porteuses est par exemple utile pour rendre le signal plus tolérant aux erreurs de fréquence, qu'il s'agisse de déviations de fréquence entre l'émetteur et le récepteur ou de décalages Doppler en cas d'émetteurs ou de récepteurs mobiles.

Un avantage de cette approche réside dans le fait que les perturbations à bande étroite n'affectent qu'une ou quelques porteuses. Associé à des procédés de correction d'erreurs avec transmission de données redondantes, que nous avons appris à connaître quelques chapitres plus tôt, il est ainsi possible d'obtenir une transmission sans erreur malgré des perturbations à bande étroite.

<margin>
[picture:704:ofdm:Spectre de fréquence d'un signal OFDM simple]
</margin>

[question:AE421]

Un autre avantage résulte du débit de symboles plus faible de chaque porteuse individuelle. Grâce à ce débit plus faible, la durée de chaque symbole est plus longue. En cas de décalages temporels dus à une propagation par trajets multiples, la partie de superposition entre les signaux (appelée interférence entre symboles ou diaphonie entre symboles) est alors correspondingly plus faible. Il peut également arriver que certaines fréquences soient annulées ou du moins fortement atténuées par la propagation par trajets multiples (on parle alors d'évanouissement sélectif en fréquence). Cela peut être compensé par les mêmes mécanismes que ceux mentionnés précédemment pour les perturbations à bande étroite. Dans le cas d'une propagation par trajets multiples, l'OFDM est donc particulièrement avantageux.

[question:AE422]