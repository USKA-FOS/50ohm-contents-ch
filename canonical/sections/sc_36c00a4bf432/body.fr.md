Contrairement à la modulation, qui a lieu du côté de l'émetteur, la démodulation des signaux dans le récepteur permet de convertir un signal modulé en NF et ainsi de le rendre audible.

Selon le type de modulation utilisé du côté de l'émetteur, une démodulation correspondante doit avoir lieu du côté du récepteur.
Pour cela, il existe différents concepts de circuits qui permettent la démodulation.

La forme la plus simple de démodulation d'un signal haute fréquence est la modulation d'amplitude (AM).
Les signaux AM peuvent être démodulés au moyen d'un détecteur d'enveloppe, comme dans la figure [ref:demodulator_huellkurvendemodulator_am]. À cet effet, le signal haute fréquence est d'abord sélectionné à la fréquence de réception souhaitée, par exemple au moyen d'un circuit oscillant adapté, puis redressé par une diode. Un condensateur monté en aval de la diode est chargé à la valeur de crête instantanée du signal et simultanément déchargé via une résistance montée en parallèle à celui-ci avec une constante de temps appropriée. Cette constante de temps est nettement supérieure à la durée d'une période du signal HF, mais nettement inférieure à la durée d'une période du signal BF.

<margin>
[picture:141:demodulator_huellkurvendemodulator_am:Détecteur d'enveloppe pour la démodulation des signaux AM]
</margin>

[question:AD501]

À la borne X dans la figure [ref:demodulator_huellkurvendemodulator_am_2], la tension de crête redressée du signal HF est représentée, qui diminue légèrement entre les crêtes du signal HF en fonction de la constante de temps de la résistance montée en parallèle au condensateur. L'enveloppe du signal correspond ainsi au BF modulé, qui est superposé à un signal en dents de scie (fréquence porteuse) en raison de la constante de temps du condensateur et correspond au signal dans la figure [ref:demodulator_huellkurvendemodulator_am_abbx]. Dans les étapes de traitement du BF suivantes (non représentées), les restes de cette fréquence porteuse sont ensuite filtrés, de sorte que le BF pur reste en tant que signal de sortie.

<margin>
[picture:607:demodulator_huellkurvendemodulator_am_2:Détecteur d'enveloppe pour la démodulation des signaux AM avec représentation du signal ZF d'entrée qui est appliqué à l'entrée du démodulateur]
[picture:146:demodulator_huellkurvendemodulator_am_abbx:Signal démodulé au point X du détecteur d'enveloppe]
</margin>

[question:AD502]

---
<margin>
[picture:841:demodulator_flankendiskriminator:Circuit oscillant utilisé comme discriminateur de flanc]

[picture:149:demodulator_flankendiskriminator_schaltung:Discriminateur de flanc FM]
</margin>

Un circuit très similaire à celui du détecteur d'enveloppe mentionné précédemment peut être utilisé pour la démodulation des signaux FM.
À partir de la fréquence intermédiaire dans le récepteur FM, comme le montre la figure [ref:demodulator_flankendiskriminator], le signal passe dans un circuit oscillant qui est légèrement accordé avec sa fréquence de résonance $f_\text{res}$ au-dessus ou en dessous de la fréquence ZF $f_\text{ZF}$. De ce fait, le signal FM à démoduler se trouve sur le flanc du circuit oscillant et transforme les variations de fréquence du FM en variations d'amplitude. Au moyen du démodulateur AM monté en aval, le signal FM alors transformé en un signal AM est ensuite démodulé et rendu audible. Ce circuit, montré dans la figure [ref:demodulator_flankendiskriminator_schaltung], est appelé discriminateur de flanc.

[question:AD504]

Les signaux modulés en FM peuvent également être démodulés au moyen d'une PLL (boucle à verrouillage de phase). Dans une PLL, un oscillateur commandé en tension (VCO) est couplé à un signal d'entrée de manière à suivre la fréquence via une boucle d'asservissement de phase. Lorsque la fréquence du signal d'entrée change (modulation FM), la tension de commande du VCO suit la modulation FM. Cette tension de commande correspond alors exactement à la modulation du signal FM et donc au BF modulé et peut être prélevée sur la PLL pour un traitement ultérieur.

[question:AD505]

Pour démoduler les signaux modulés en SSB, on utilise un détecteur de produit. Il s'agit essentiellement d'un mélangeur en anneau qui utilise comme signaux d'entrée la ZF du récepteur ainsi qu'un BFO (oscillateur à fréquence de battement). Par mélange (produit) de ces deux signaux d'entrée, l'un des produits de mélange est le signal BF souhaité (signal SSB), qui peut être prélevé à la sortie pour un traitement ultérieur. Pour la meilleure intelligibilité possible du BF démodulé, le BFO doit être accordé sur la fréquence de la porteuse supprimée du signal SSB.

[question:AD506]