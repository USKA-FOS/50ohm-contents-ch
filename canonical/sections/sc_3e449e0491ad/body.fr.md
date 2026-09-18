Pour établir une liaison radio entre deux lieux via l'onde spatiale, il faut choisir une fréquence qui est suffisamment réfractée par l'ionosphère vers la terre. En règle générale, cela ne concerne pas une fréquence unique, mais toute une bande de fréquences. Souvent, on opte pour la bande radioamateur la plus élevée dans cette plage.

Cette bande de fréquences est limitée vers le haut par la *MUF* (*Maximum Usable Frequency*), c'est-à-dire la fréquence maximale que l'ionosphère peut encore réfracter pour la distance entre l'émetteur et le récepteur.

[question:EH204]

La MUF dépend de la densité des électrons libres dans la région de réfraction (ici : région F2) ainsi que de l'angle d'incidence de l'onde radio dans l'ionosphère. La figure [ref:e_muf_luf] montre la prévision de la MUF pour un jour d'été en juillet 2025. Il apparaît clairement que la MUF dépend de l'heure de la journée : en journée, l'ionisation plus forte entraîne une MUF plus élevée, tandis qu'elle diminue la nuit avec la baisse de l'ionisation. Un autre exemple est illustré par la figure [ref:e_muf_luf2]. Ici, la MUF est d'environ $\qty{7,5}{\mega\hertz}$. Cela signifie que les fréquences de $\qty{3,5}{\mega\hertz}$ et $\qty{7}{\mega\hertz}$ sont encore réfractées vers la terre, tandis que les fréquences supérieures à $\qty{7,5}{\mega\hertz}$ sont déviées vers l'espace. C'est aussi la raison pour laquelle nous communiquons avec la Station spatiale internationale (ISS) sur la bande $\qty{2}{\meter}$ : avec $\qty{145,800}{\mega\hertz}$, nous sommes bien au-dessus d'une MUF typique.

<margin>
[picture:991:e_muf_luf:Prévision de la MUF et de la LUF en juillet 2025]
</margin>

<margin>
[picture:997:e_muf_luf2:Simulation des distances de saut pour différentes fréquences et une MUF d'environ $\qty{7,5}{\mega\hertz}$ lors d'une nuit d'août 2024 avec un angle de rayonnement de $\qty{45}{\degree}$]
</margin>

Les relations exactes de la MUF, par exemple en fonction de l'angle de rayonnement, ne seront abordées que dans le cours pour HB9. Pour HB3, il est important de savoir que :

*Plus l'ionisation de l'ionosphère est forte, plus la MUF est généralement élevée.*

[question:EH207]
[question:EH206]

Nous avons déjà rencontré la couche D dans le chapitre sur l'ionosphère II. Une autre fréquence de coupure est déterminée par cette couche – la *LUF* (*Lowest Usable Frequency*), c'est-à-dire la fréquence minimale utilisable en dessous de laquelle l'atténuation devient trop importante.
Vers le bas, la LUF représente donc la limitation. Elle est principalement déterminée par l'ionisation dans la *couche D*, mais dépend aussi de l'équipement (puissance d'émission, antennes, sensibilité du récepteur).

[question:EH209]

En particulier en cas d'activité solaire très faible ou lors de fortes tempêtes magnétiques, un cas particulier peut se produire : pour une liaison donnée, la LUF peut dépasser la MUF. Dans ce cas, aucune communication radio via l'onde spatiale n'est possible entre les lieux concernés. La figure [ref:e_muf_luf] montre également une prévision de la LUF pour juillet 2025. On y voit clairement que, entre 6 et 12 heures, la LUF se situe au-dessus de la MUF, rendant toute exploitation en ondes courtes impossible.

Pour la propagation des ondes courtes via l'ionosphère, deux fréquences de coupure sont particulièrement importantes : la *LUF (Lowest Usable Frequency)* et la *MUF (Maximum Usable Frequency)*. Entre ces deux valeurs, une liaison radio via l'ionosphère est fondamentalement possible.

La *LUF (Lowest Usable Frequency)* désigne la fréquence minimale à laquelle une liaison sur un trajet radio donné est encore possible avec une qualité de signal suffisante. La LUF dépend de la puissance : si la puissance d'émission est augmentée, un signal plus atténué peut atteindre le récepteur avec une intensité de champ suffisante. La LUF diminue alors, permettant l'utilisation de fréquences plus basses.

[question:EH220]

La *MUF (Maximum Usable Frequency)* désigne en revanche la fréquence maximale qui, sur un trajet donné et à un moment précis, est encore réfractée par l'ionosphère vers la terre. Au-dessus de la MUF, l'onde radio n'est plus suffisamment réfractée et traverse l'ionosphère pour se perdre dans l'espace. La MUF ne dépend pas de la puissance d'émission.

[question:EH221]

Remarque : Les bases physiques de l'ionosphère et de ses couches (couches D, E, F1 et F2) sont traitées plus en détail dans les chapitres correspondants [sec:ionosphaere_3], [sec:tote_zone_2], [sec:sprungdistanz_2] et [sec:muf_luf_2] sur l'ionosphère pour HB9. Ici, il suffit de comprendre que la LUF peut être influencée par l'intensité du signal, tandis que la MUF est déterminée exclusivement par les conditions de propagation dans l'ionosphère.

<!-- Review abgeschlossen, passt so für mich. Vy 73 de Marc -->