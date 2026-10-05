Un avantage essentiel du traitement numérique des signaux réside dans le fait que les informations disponibles sous forme numérique peuvent être traitées presque arbitrairement. Une séquence d'échantillons d'entrée est convertie en une séquence d'échantillons de sortie à l'aide de fonctions mathématiques. Des filtres numériques simples, comme les filtres passe-bas, passe-bande ou passe-haut, peuvent être exécutés de deux manières différentes : en tant que filtres FIR et filtres IIR. FIR signifie *Finite Impulse Response* (réponse impulsionnelle finie) et IIR signifie *Infinite Impulse Response* (réponse impulsionnelle infinie).

La caractéristique principale des filtres FIR est, comme l'indique déjà la désignation "finite" (en allemand : fini), que seul un nombre limité d'échantillons d'entrée est utilisé pour le calcul d'un échantillon de sortie. Les filtres IIR utilisent en revanche également des échantillons de sortie déjà calculés, qui sont réinjectés à l'entrée du calcul. Grâce à cette rétroaction, un seul échantillon d'entrée peut théoriquement avoir une influence pendant une durée illimitée sur les échantillons de sortie suivants.

Les filtres numériques peuvent être implémentés à la fois en logiciel sur un DSP et en matériel programmable sur un FPGA. En outre, il existe des frontends dits à signaux mixtes, qui réalisent diverses fonctions de traitement du signal, comme par exemple des filtres de décimation, avec des convertisseurs AD/DA dans une seule puce, afin de les exécuter de manière aussi économe en énergie que possible et de soulager les étapes de traitement du signal suivantes.

[question:AF631]

<indepth>
[picture:1133:a_fir:Filtre FIR]

La figure [ref:a_fir] montre schématiquement la structure d'un filtre FIR. Un échantillon d'entrée est écrit dans une mémoire d'entrée. À chaque cycle, les valeurs stockées sont décalées d'un emplacement de mémoire comme dans un registre à décalage. Les prélèvements des différents emplacements de mémoire sont multipliés par les coefficients de filtre correspondants puis sommés. Le résultat est délivré en tant qu'échantillon de sortie.

Supposons que les quatre coefficients de filtre aient chacun la valeur $\frac{1}{4}$, alors les quatre derniers échantillons d'entrée sont chacun multipliés par $\frac{1}{4}$ puis sommés. L'échantillon de sortie est donc la moyenne des quatre derniers échantillons d'entrée. Un tel filtre est également appelé *moyenne mobile*.

Une séquence d'entrée $0,0,0,4,0,0,0,0$ conduit ainsi à la séquence de sortie $0,0,0,1,1,1,1,0$.

Le filtre lisse ainsi les changements rapides, c'est-à-dire les composantes haute fréquence du signal d'entrée. Les changements lents ou les basses fréquences sont largement transmis, tandis que les changements rapides ou les composantes haute fréquence sont atténués. Une moyenne mobile agit donc comme un filtre passe-bas numérique très simple.

Le filtre effectue une opération dite de convolution, qui est d'ailleurs aussi la base de nombreux réseaux neuronaux qui alimentent l'intelligence artificielle.
</indepth>

<indepth>
*FPGA*
désigne un circuit intégré du nom de **F**ield **P**rogrammable **G**ate **A**rray. Il s'agit d'un composant matériel programmable.
</indepth>
%TODO: FPGA est déjà apparu plus tôt -> déplacer là-bas

