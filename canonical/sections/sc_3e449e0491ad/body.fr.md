Pour établir une liaison radio entre deux lieux via l'onde spatiale, il faut choisir une fréquence qui est réfléchie de manière fiable par l'ionosphère vers la terre. En général, cela ne concerne pas une seule fréquence, mais toute une bande de fréquences. On opte souvent pour la bande radioamateur la plus élevée dans cette plage.

Cette bande de fréquences est limitée vers le haut par la *MUF* (*maximal usable frequency*), c'est-à-dire la fréquence la plus élevée que l'ionosphère peut encore réfléchir pour la distance entre l'émetteur et le récepteur.

[question:EH204]

La MUF dépend de la densité des électrons libres dans la région de réflexion (ici : région F2) ainsi que de l'angle d'incidence de l'onde radio dans l'ionosphère. La figure [ref:e_muf_luf] montre la prévision de la MUF pour un jour d'été en juillet 2025. On voit clairement que la MUF dépend de l'heure de la journée : pendant la journée, l'ionisation plus forte conduit à une MUF plus élevée, la nuit l'ionisation diminue et la MUF baisse en conséquence. Un autre exemple est montré dans la figure [ref:e_muf_luf2]. La MUF est ici d'environ $\qty{7,5}{\mega\hertz}$. Cela signifie que les fréquences $\qty{3,5}{\mega\hertz}$ et $\qty{7}{\mega\hertz}$ sont encore réfléchies vers la terre, tandis que les fréquences au-dessus de $\qty{7,5}{\mega\hertz}$ sont déviées vers l'espace. C'est aussi la raison pour laquelle nous communiquons avec la station spatiale ISS sur la bande des $\qty{2}{\meter}$ : à $\qty{145,800}{\mega\hertz}$, nous sommes nettement au-dessus d'une MUF typique.

<margin>
[picture:991:e_muf_luf:Prévision de la MUF et de la LUF en juillet 2025]
</margin>

<margin>
[picture:997:e_muf_luf2:Simulation des distances de saut pour différentes fréquences et une MUF d'environ $\qty{7,5}{\mega\hertz}$ lors d'une nuit d'août 2024 avec un angle de rayonnement de $\qty{45}{\degree}$]
</margin>

Les relations précises de la MUF, par exemple par rapport à l'angle de rayonnement, ne seront traitées que dans la matière pour HB9. Pour HB3, il est important de savoir :

*Plus l'ionisation de l'ionosphère est forte, plus la MUF est généralement élevée.*

[question:EH207]
[question:EH206]

Nous avons déjà rencontré la couche D dans le chapitre Ionosphère II. Celle-ci détermine une autre fréquence de coupure – la LUF (Lowest Usable Frequency), c'est-à-dire la fréquence utilisable la plus basse en dessous de laquelle l'atténuation est trop forte.

Vers le bas, la LUF représente donc la limitation. Elle est principalement déterminée par l'ionisation dans la *couche D*, mais dépend aussi de l'équipement (puissance d'émission, antennes, sensibilité du récepteur).

[question:EH209]

En particulier lors d'une très faible activité solaire ou pendant de fortes tempêtes magnétiques, le cas particulier peut survenir où pour un certain trajet de signal, la LUF est supérieure à la MUF. Dans ce cas, aucune communication radio via l'onde spatiale n'est possible entre les lieux concernés. La figure [ref:e_muf_luf] montre également une prévision de la LUF pour juillet 2025. On y voit clairement qu'entre 6 et 12 heures, la LUF est au-dessus de la MUF et donc aucune activité en ondes courtes n'est possible.

Pour la propagation des ondes courtes via l'ionosphère, deux fréquences de coupure sont particulièrement importantes : la *LUF (Lowest Usable Frequency)* et la *MUF (Maximum Usable Frequency)*. Entre ces deux valeurs, une liaison radio via l'ionosphère est fondamentalement possible.

La *LUF (Lowest Usable Frequency)* désigne la fréquence la plus basse à laquelle une connexion sur un certain trajet radio est encore possible avec une qualité de signal suffisante. La LUF dépend de la puissance : si la puissance d'émission est augmentée, un signal plus atténué peut quand même atteindre le récepteur avec une intensité de champ suffisante. Ainsi, la LUF baisse, permettant également l'utilisation de fréquences plus basses.

[question:EH220]

La *MUF (Maximum Usable Frequency)* désigne quant à elle la fréquence la plus élevée qui, sur un certain trajet et à un moment donné, est encore réfléchie par l'ionosphère vers la terre. Au-dessus de la MUF, l'onde radio n'est plus suffisamment réfléchie et traverse l'ionosphère vers l'espace. La MUF ne dépend pas de la puissance d'émission.

[question:EH221]

Remarque : Les bases physiques de l'ionosphère et de ses couches (couches D, E, F1 et F2) sont traitées plus en détail dans les sections correspondantes [sec:ionosphaere_3], [sec:tote_zone_2], [sec:sprungdistanz_2] et [sec:muf_luf_2] sur l'ionosphère pour HB9. Ici, il suffit de comprendre que la LUF peut être influencée par l'intensité du signal, tandis que la MUF est déterminée exclusivement par les conditions de propagation de l'ionosphère.

