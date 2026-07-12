Nous avons appris que lors de la modulation d'amplitude, outre la porteuse, deux bandes latérales sont générées, une inférieure (LSB) et une supérieure (USB), contenant toutes deux l'information complète du signal de modulation, tandis que la porteuse elle-même ne transmet aucune information. Comme les deux bandes latérales contiennent la même information, il suffit d'en envoyer une seule et de supprimer la porteuse (voir figure [ref:e_ssb_am_modulation]). Cette méthode est appelée modulation à bande latérale unique ou Single Sideband (SSB). L'avantage de la SSB réside dans le fait qu'aucune puissance d'émission n'est gaspillée pour la porteuse et la deuxième bande latérale, ce qui permet d'utiliser toute la puissance de manière efficace pour la transmission d'informations et, simultanément, de réduire considérablement la bande passante nécessaire par rapport à l'AM.


Dans la modulation à bande latérale unique (SSB), le signal émis – en fonction de la bande latérale choisie sur l'émetteur-récepteur – contient soit la fréquence porteuse plus la fréquence de modulation NF (dans le cas de USB) soit la fréquence porteuse moins la fréquence de modulation NF (dans le cas de LSB). La figure [ref:e_ssb_einzelsignal] montre deux exemples : si un émetteur avec une fréquence porteuse de $\qty{7,100}{\mega\hertz}$ est modulé avec un signal NF de $\qty{1}{\kilo\hertz}$ en USB, l'émetteur émet une fréquence de $\qty{7,100}{\mega\hertz} + \qty{1}{\kilo\hertz} = \qty{7,101}{\mega\hertz}$. Si l'émetteur est modulé en LSB, l'émetteur émet une fréquence de $\qty{7,100}{\mega\hertz} -\qty{1}{\kilo\hertz} = \qty{7,099}{\mega\hertz}$.

<margin>
[picture:1056:e_ssb_einzelsignal:Bandes latérales en AM et SSB]
</margin>

Les questions suivantes peuvent être résolues selon ce schéma.

[question:EE203]
[question:EE204]

---

Les signaux AM transmettent les deux bandes latérales et la porteuse et ont donc une bande passante de plus du double de celle du signal NF modulant (voir figure [ref:e_ssb_einzelsignal]). La bande passante d'un signal SSB correspond approximativement à la bande passante du signal NF modulant (après filtrage et limitation de la bande passante du signal NF). Dans le cas de la SSB, les composantes du signal en dessous de $\qty{300}{\hertz}$ et la porteuse ($\qty{0}{\hertz}$) ne sont pas transmises et sont supprimées. Par conséquent, la SSB a une bande passante légèrement inférieure à la moitié de celle de l'AM.

<margin>
[picture:743:e_ssb_einzelsignal:Bandes latérales en AM et SSB]
</margin>

[question:EE202]
[question:EE201]

---

Comme nous l'avons déjà appris dans la classe N sur le thème de la télégraphie Morse avec l'onde continue (CW), un porteuse haute fréquence constante est allumée et éteinte à un rythme déterminé. Les signaux CW nécessitent, par rapport aux signaux modulés par la voix comme l'AM et la SSB, la bande passante la plus faible. Cela est dû au fait que dans le cas de la CW, une seule fréquence est modulée et non, comme dans le cas des signaux vocaux, plusieurs composantes de fréquence d'un signal NF doivent être transmises simultanément.

<indepth>
La bande passante des signaux CW dépend de la vitesse de transmission (vitesse de modulation) et est d'environ $\qty{300}{\hertz}$ pour des vitesses moyennes de 20 mots par minute (100 caractères par minute).
</indepth>

[question:EE207]

Pour éviter les perturbations des stations voisines dans la bande de fréquences, la bande passante occupée d'un signal SSB doit être limitée à environ $\qty{2,7}{\kilo\hertz}$ au maximum. Cette bande passante est tout à fait suffisante pour une bonne intelligibilité de la parole. C'est pourquoi le signal NF du microphone dans l'émetteur est limité en bande passante : les composantes de fréquence en dessous d'environ $\qty{300}{\hertz}$ ainsi que celles au-dessus d'environ $\qty{3}{\kilo\hertz}$ sont supprimées, car elles contribuent peu à l'intelligibilité de la parole.

[question:EJ211]
[question:EJ210]

En pratique, les filtres SSB pour la génération d'un signal SSB ont souvent une bande passante d'environ $\qty{2,4}{\kilo\hertz}$. Cette bande passante plus faible suffit dans de nombreux cas pour une bonne intelligibilité de la parole et permet en même temps une utilisation plus efficace du spectre de fréquences disponible.

[question:EF310]

Les perturbations des stations voisines peuvent également être causées par ce que l'on appelle le *Splatter*, qui se produit lorsque l'amplification du microphone est trop élevée et que les étages NF sont surchargés. Cela se traduit dans le signal émis par une augmentation de la bande passante de la transmission SSB, ce qui peut perturber d'autres stations.

[question:EJ215]

Une amplification du microphone trop faible (amplitude NF) entraîne une modulation plus faible de l'émetteur SSB, ce qui réduit la puissance de sortie. Il est donc important que l'amplification du microphone soit optimisée pour une bonne communication en SSB (ni trop grande ni trop petite). Nous reviendrons sur ce point plus en détail dans le chapitre sur le compresseur dynamique.

[question:EE206]
[question:EE205]
