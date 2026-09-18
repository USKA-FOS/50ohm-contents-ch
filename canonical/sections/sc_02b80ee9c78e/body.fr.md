Dans la classe E, nous avons déjà abordé les [multiplicateurs de fréquence](a_frequenzvervielfacher_schaltung) au niveau des blocs. Dans la classe A, nous voulons comprendre leur fonctionnement.

Les diodes et les transistors possèdent une caractéristique non linéaire. Lorsqu’ils sont pilotés par un signal sinusoïdal, celui-ci est déformé. Comme nous l’avons déjà appris, de tels processus non linéaires génèrent des [harmoniques](a_frequenzvervielfacher_schaltung). Dans un multiplicateur de fréquence, cet effet est exploité de manière ciblée : le signal d’entrée est d’abord déformé de façon non linéaire, ce qui produit de nombreuses [harmoniques](a_frequenzvervielfacher_schaltung). Ensuite, l’harmonique souhaitée est sélectionnée à l’aide d’un [circuit oscillant](a_frequenzvervielfacher_schaltung) ou d’un filtre accordé, puis utilisée comme signal de sortie.

Techniquement, un multiplicateur de fréquence est réalisé en appliquant d’abord le signal d’entrée à un étage de distorsion non linéaire. Cela peut être, par exemple, un [amplificateur](a_frequenzvervielfacher_schaltung) en classe C, que nous aborderons plus en détail dans ce chapitre. Ensuite, à partir du mélange de signaux, le filtre extrait l’harmonique souhaitée du signal et la transmet à l’étage suivant. Comme la multiplication de fréquence repose sur les [harmoniques](a_frequenzvervielfacher_schaltung), seuls des multiples entiers de la fréquence fondamentale sont possibles. En pratique, on utilise presque exclusivement la 2ᵉ ou la 3ᵉ [harmonique](a_frequenzvervielfacher_schaltung) de la fréquence fondamentale (doublement ou triplement de fréquence).

Pour obtenir des multiplications de fréquence plus élevées, on place en cascade des étages de doublement ou de triplement, de sorte que leurs facteurs se multiplient ensuite.

[question:AF311]


La multiplication de fréquence, et éventuellement leur mise en cascade, génère des produits de fréquence qui peuvent souvent causer des perturbations. Par conséquent, les étages de multiplication de fréquence doivent être très bien blindés afin de réduire au maximum les rayonnements indésirables.

[question:AF313]


Un circuit multiplicateur typique (voir figure [ref:a_frequenzvervielfacher_schaltung]) comprend un étage amplificateur fonctionnant délibérément sans polarisation de base. Cela crée un [amplificateur](a_frequenzvervielfacher_schaltung) en classe C qui déforme fortement le signal d’entrée, dont la sortie est prélevée au moyen de filtres. On utilise pour cela des [circuits oscillants](a_frequenzvervielfacher_schaltung) accordés sur la fréquence souhaitée, généralement réglables.

<margin>
[picture:489:a_frequenzvervielfacher_schaltung:Exemple de circuit d’un multiplicateur de fréquence avec amplificateur en classe C sans polarisation de base]
</margin>

[question:AF312]


Lorsqu’un appareil comporte plusieurs étages multiplicateurs en cascade, des perturbations peuvent survenir sur des fréquences générées entre les étages. Pour les identifier, il faut calculer le trajet du signal à travers chaque étage et les fréquences qui en résultent. L’ordre des étages multiplicateurs est donc crucial pour déterminer les fréquences parasites, car seules certaines fréquences sont mathématiquement possibles.

[question:AF314]