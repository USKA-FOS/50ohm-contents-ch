Dans la section [sec:frequenzvervielfacher_1], nous avons déjà abordé les multiplicateurs de fréquence au niveau des blocs. Maintenant, nous voulons comprendre leur fonctionnement.

Les diodes et les transistors possèdent une caractéristique non linéaire. Lorsqu'ils sont excités par un signal sinusoïdal, celui-ci est ainsi déformé. Comme nous l'avons déjà appris, de telles opérations non linéaires génèrent des harmoniques. Dans un multiplicateur de fréquence, cet effet est délibérément exploité : le signal d'entrée est d'abord déformé de manière non linéaire, produisant ainsi de nombreuses harmoniques. Ensuite, l'harmonique supérieure souhaitée est sélectionnée à l'aide d'un circuit oscillant accordé ou d'un filtre et utilisée comme signal de sortie.

Techniquement, un multiplicateur de fréquence est réalisé de telle sorte que le signal d'entrée soit d'abord appliqué à un étage de distorsion non linéaire. Il peut s'agir, par exemple, d'un amplificateur de classe C, que nous aborderons plus loin dans ce chapitre. Ensuite, à partir du mélange de signaux, l'harmonique supérieure souhaitée du signal est sélectionnée au moyen de filtres et transmise à l'étage suivant. Puisque la multiplication de fréquence est basée sur les harmoniques supérieures/harmoniques, seuls des multiples entiers de la fréquence fondamentale sont possibles. En pratique (à quelques exceptions près), seule la 2e harmonique ou la 3e harmonique de la fréquence fondamentale est utilisée (doublement, triplement).
Pour atteindre des multiplications de fréquence plus élevées, des étages de doublement ou de triplement sont donc connectés en série, de sorte que leurs facteurs se multiplient ensuite.

[question:AF311]

La multiplication de fréquence et, le cas échéant, leur mise en cascade produisent des produits de fréquence qui peuvent souvent entraîner des interférences. Par conséquent, les étages de multiplication de fréquence doivent être très bien blindés afin de réduire au maximum les rayonnements indésirables.

[question:AF313]

Un circuit typique de multiplicateur (voir figure [ref:a_frequenzvervielfacher_schaltung]) contient un étage amplificateur, délibérément exploité sans polarisation de base. Cela crée un amplificateur fonctionnant en classe C, qui déforme fortement le signal d'entrée, et dont le signal de sortie est extrait au moyen de filtres. Pour les filtres, des circuits oscillants correspondants sont utilisés, qui sont en résonance à la fréquence souhaitée et sont généralement accordables.

<margin>
[picture:489:a_frequenzvervielfacher_schaltung:Exemple d'un circuit de multiplicateur de fréquence avec amplificateur classe C sans polarisation de base]
</margin>

[question:AF312]

Lorsque plusieurs étages multiplicateurs sont connectés en série à l'intérieur d'un appareil, des interférences peuvent survenir sur des fréquences qui se forment entre les différents étages multiplicateurs. Pour déterminer ces fréquences, il faut calculer le trajet du signal à travers les différents étages et les fréquences qui y sont présentes par la suite. Par conséquent, l'ordre des étages multiplicateurs correspondants est d'une importance cruciale pour déterminer les fréquences d'interférence, car seules certaines fréquences sont mathématiquement possibles.

[question:AF314]
