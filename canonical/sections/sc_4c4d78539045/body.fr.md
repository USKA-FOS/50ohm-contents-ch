
Il est également possible de répartir un flux de données sur plusieurs porteuses, qui se trouvent à des fréquences différentes, mais proches. Les porteuses ne peuvent cependant pas être placées de manière arbitrairement dense les unes à côté des autres, car elles présentent une certaine largeur en raison des bandes latérales inévitables.

Dans le cas de la modulation de fréquence orthogonale (Orthogonal Frequency-Division Multiplexing, OFDM), les porteuses individuelles sont placées à une distance précise où une interférence mutuelle (appelée "diaphonie") est évitée au maximum.

Plus le débit de symboles par porteuse est élevé, plus la distance entre les porteuses doit être grande. C'est pourquoi on choisit souvent un débit de symboles plus faible pour chaque porteuse afin que plus de porteuses puissent être placées. La quantité d'informations transmises reste la même, car bien que moins d'informations puissent être transmises par porteuse, plus de porteuses peuvent être utilisées côte à côte.

Un avantage de cette procédure réside dans le fait que les perturbations à bande étroite ne perturbent qu'une ou quelques porteuses. En combinaison avec des procédés de correction d'erreurs avec transmission de données redondantes, que nous apprendrons plus tard, il est ainsi possible d'obtenir une transmission sans erreur malgré les perturbations à bande étroite.

<margin>
[picture:704:ofdm:Spectre de fréquence d'un signal OFDM simple]
</margin>

[question:AE421]

Un autre avantage découle du faible débit de symboles de chaque porteuse individuelle. En raison du faible débit de symboles, la durée de chaque symbole est plus longue. Dans le cas de décalages temporels dus à la propagation multitrajets, la proportion de superposition entre les signaux (appelée interférence inter-symboles ou diaphonie de symboles) est alors plus faible. Dans le cas de la propagation multitrajets, l'OFDM est donc particulièrement avantageux.

[question:AE422]