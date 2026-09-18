Un avantage majeur du traitement numérique des signaux réside dans le fait que les informations disponibles sous forme numérique peuvent être traitées de manière quasi illimitée. Une séquence d'échantillons d'entrée est convertie en une séquence d'échantillons de sortie à l'aide de fonctions mathématiques. Les filtres numériques simples, tels que les filtres passe-bas, passe-bande ou passe-haut, peuvent être implémentés de deux manières différentes : sous forme de filtres RIF (Réponse Impulsionnelle Finie) ou de filtres RII (Réponse Impulsionnelle Infinie). RIF signifie *Finite Impulse Response* et RII signifie *Infinite Impulse Response*.

La principale caractéristique des filtres RIF, comme l'indique déjà le terme *« finite »* (fini en allemand), est qu'un nombre limité d'échantillons d'entrée est utilisé pour calculer un échantillon de sortie. Les filtres RII, en revanche, utilisent également des échantillons de sortie déjà calculés, qui sont réinjectés dans le calcul d'entrée. Grâce à cette rétroaction, un seul échantillon d'entrée peut théoriquement influencer indéfiniment les échantillons de sortie suivants.

Les filtres numériques peuvent être implémentés soit en logiciel sur un DSP, soit en matériel programmable sur un FPGA. Par ailleurs, il existe des interfaces mixtes (Mixed Signal Frontends) qui intègrent diverses fonctions de traitement du signal, comme des filtres de décimation, ainsi que des convertisseurs N/A et A/N dans une seule puce, afin d'optimiser leur efficacité énergétique et de soulager les étages de traitement du signal en aval.

[question:AF631]

<indepth>
[picture:1133:a_fir:Filtre RIF]

La figure [ref:a_fir] montre schématiquement la structure d'un filtre RIF. Un échantillon d'entrée est écrit dans une mémoire d'entrée. À chaque cycle d'horloge, les valeurs stockées sont décalées d'une position mémoire, comme dans un registre à décalage. Les prises sur les différentes positions mémoire sont multipliées par les coefficients de filtrage correspondants, puis additionnées. Le résultat est ensuite transmis en tant qu'échantillon de sortie.

Si les quatre coefficients de filtrage valent chacun $\frac{1}{4}$, les quatre derniers échantillons d'entrée sont multipliés par $\frac{1}{4}$ puis additionnés. L'échantillon de sortie correspond ainsi à la moyenne des quatre derniers échantillons d'entrée. Un tel filtre est également appelé *moyenne mobile*.

Une séquence d'entrée $0,0,0,4,0,0,0,0$ produit ainsi la séquence de sortie $0,0,0,1,1,1,1,0$.

Le filtre lisse donc les variations rapides, c'est-à-dire les composantes haute fréquence du signal d'entrée. Les variations lentes ou les basses fréquences sont largement transmises, tandis que les variations rapides ou les composantes haute fréquence sont atténuées. Une moyenne mobile agit donc comme un simple filtre passe-bas numérique.

Ce filtre effectue une opération de convolution, qui constitue par ailleurs la base de nombreux réseaux de neurones utilisés en intelligence artificielle.