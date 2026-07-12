La synthèse numérique directe (Direct Digital Synthesis ou DDS en abrégé) sert à générer des signaux périodiques à bande limitée avec une haute résolution de fréquence.
En plus de la synthèse de signaux au moyen de boucles de régulation PLL, cette méthode de génération de signaux est aujourd'hui largement répandue dans les techniques de communication et de mesure et représente l'état actuel de la technique. Les signaux sont ici très finement réglables en fréquence par rapport à une PLL classique.

Principe de fonctionnement de base d'une DDS :

Au moyen d'un générateur de rythme à fréquence fixe, un compteur d'adresses est compté en continu. En cas de débordement du compteur d'adresses, celui-ci redémarre. Cela permet de générer une séquence de valeurs binaires croissantes à sa sortie. Au moyen de ces valeurs, un tableau de sinus est parcouru en continu. Cela permet de générer à la sortie du tableau de sinus des valeurs d'amplitude numériques pour une oscillation sinusoïdale, qui sont ensuite transmises à un registre. Les valeurs d'amplitude numériques sont ensuite transmises à un convertisseur numérique/analogique en aval, au moyen de l'horloge du registre, qui les convertit ensuite en un signal analogique (oscillation sinusoïdale) et les émet.

<indepth>
Une DDS peut également parcourir différentes tables de valeurs, de sorte que des formes de signaux cycliques quelconques peuvent également être générées. En commandant le compteur d'adresses (au moyen d'un mot de réglage), qui influence en continu le pas du compteur, la fréquence à laquelle la table de valeurs est parcourue peut être commandée dans de larges limites.
Pour le registre d'adresses, on utilise souvent des registres avec $\qty{32}{\bit}$ ou plus, dont seuls un plus petit nombre de bits de poids fort (par exemple, les $\qty{14}{\bit}$ supérieurs) sont utilisés pour parcourir la table de valeurs. Cela permet de sortir également des fractions de la fréquence d'horloge, et la résolution de fréquence de la DDS est ainsi augmentée.
L'avantage d'une DDS par rapport à une PLL réside dans le fait qu'une résolution de fréquence presque quelconque peut être obtenue en commandant les paramètres mentionnés ci-dessus. De plus, il est possible de passer rapidement d'une fréquence à une autre (par commande au moyen du mot de réglage) sans processus de mise en oscillation.

La qualité du signal de sortie d'une DDS dépend essentiellement de la qualité du générateur de rythme utilisé (stabilité, jitter). De plus, la résolution d'amplitude (quantification) du convertisseur numérique/analogique et sa linéarité sont décisives pour la qualité du signal de sortie.
</indepth>

[question:AD620]