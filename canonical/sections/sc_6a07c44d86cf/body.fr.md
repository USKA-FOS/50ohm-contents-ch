Nous avons appris que dans la modulation d'amplitude, en plus de la porteuse, deux bandes latérales se forment : une inférieure (LSB) et une supérieure (USB), qui contiennent toutes les informations du signal de modulation, tandis que la porteuse elle-même ne transmet aucune information. Comme les deux bandes latérales contiennent les mêmes informations, il suffit d’en transmettre une seule et de supprimer la porteuse (cf. figure [ref:e_ssb_am_modulation]). Cette méthode s’appelle modulation à bande latérale unique ou Single Sideband (SSB). L’avantage de la SSB réside dans le fait qu’aucune puissance d’émission n’est gaspillée pour la porteuse et la seconde bande latérale, ce qui permet d’utiliser toute la puissance de manière efficace pour la transmission d’informations et réduit considérablement la bande passante nécessaire par rapport à l’AM.


Dans la modulation à bande latérale unique (SSB), le signal émis – selon la bande latérale choisie sur l’émetteur-récepteur – contient soit la fréquence porteuse plus la fréquence de modulation BF (en USB), soit la fréquence porteuse moins la fréquence de modulation BF (en LSB). La figure [ref:e_ssb_einzelsignal] montre deux exemples : si l’on module un émetteur avec une fréquence porteuse de $\qty{7,100}{\mega\hertz}$ à l’aide d’un signal BF de $\qty{1}{\kilo\hertz}$ en USB, l’émetteur émet une fréquence de $\qty{7,100}{\mega\hertz} + \qty{1}{\kilo\hertz} = \qty{7,101}{\mega\hertz}$. Si l’on module l’émetteur en LSB, celui-ci émet une fréquence de $\qty{7,100}{\mega\hertz} - \qty{1}{\kilo\hertz} = \qty{7,099}{\mega\hertz}$.


<margin>
[picture:1056:e_ssb_einzelsignal:Bandes latérales en AM et SSB]
</margin>

Les questions suivantes peuvent être résolues selon ce schéma.


[question:EE203]
[question:EE204]

---

Les signaux AM transmettent les deux bandes latérales et la porteuse, ce qui leur confère une bande passante d’un peu plus du double de celle du signal BF modulant (cf. figure [ref:e_ssb_einzelsignal]). La bande passante d’un signal SSB correspond approximativement à celle du signal BF modulant (après filtrage et limitation de la bande passante du signal BF). En SSB, les composantes du signal en dessous de $\qty{300}{\hertz}$ et la porteuse ($\qty{0}{\hertz}$) ne sont pas transmises ni transmises, ce qui réduit encore davantage la bande passante nécessaire par rapport à l’AM.


<margin>
[picture:743:e_ssb_einzelsignal:Bandes latérales en AM et SSB]
</margin>

[question:EE202]
[question:EE201]

---

Comme nous l’avons déjà appris dans la classe N sur le thème de la télégraphie Morse avec *Continuous Wave* (CW), celle-ci consiste à allumer et éteindre un signal haute fréquence constant selon un rythme déterminé. Les signaux CW nécessitent, comparés aux signaux modulés en parole comme l’AM et la SSB, la bande passante la plus faible. Cela s’explique par le fait que dans le cas du CW, seule une fréquence unique est manipulée, et non plusieurs composantes de fréquence d’un signal BF devant être transmises simultanément, comme c’est le cas pour les signaux vocaux.


<indepth>
La bande passante des signaux CW dépend de la vitesse de transmission (vitesse de manipulation) et atteint environ $\qty{300}{\hertz}$ pour des vitesses de manipulation moyennes de 20 mots par minute (100 caractères par minute).
</indepth>

[question:EE207]


Pour éviter les interférences avec les stations voisines dans la bande de fréquences, la bande passante occupée d’un signal SSB doit être limitée à environ $\qty{2,7}{\kilo\hertz}$. Cette bande passante est largement suffisante pour une bonne intelligibilité de la parole. C’est pourquoi le signal BF du microphone est limité en bande passante dans l’émetteur : les composantes de fréquence en dessous d’environ $\qty{300}{\hertz}$ ainsi qu’au-dessus d’environ $\qty{3}{\kilo\hertz}$ sont supprimées, car elles contribuent peu à l’intelligibilité de la parole.


[question:EJ211]
[question:EJ210]


En pratique, les filtres SSB utilisés pour générer un signal SSB ont souvent une bande passante d’environ $\qty{2,4}{\kilo\hertz}$. Même cette bande passante réduite est suffisante dans de nombreux cas pour une bonne intelligibilité de la parole et permet en même temps une utilisation encore plus efficace du spectre de fréquences disponible.


[question:EF310]


Les interférences avec les stations voisines peuvent également être causées par ce qu’on appelle le *splatter*, qui résulte d’un gain du microphone trop élevé et donc d’une surmodulation des étages BF. Dans le signal émis, cela se traduit par une augmentation de la bande passante de la transmission SSB, ce qui peut perturber d’autres stations.


[question:EJ215]


Un gain du microphone trop faible (amplitude BF) entraîne une modulation insuffisante de l’émetteur SSB, ce qui réduit la puissance de sortie. Il est donc important d’ajuster correctement le gain du microphone pour une bonne communication en SSB (ni trop élevé, ni trop faible). Nous aborderons ce point plus en détail dans le chapitre sur le compresseur de dynamique.