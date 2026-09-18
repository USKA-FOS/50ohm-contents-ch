Dans la modulation d'amplitude (AM), un signal de modulation, par exemple un signal vocal, est superposé au porteur en modifiant l'amplitude. La fréquence du porteur n'est pas affectée par l'AM et reste inchangée.

Le cas le plus simple et en même temps le plus extrême est celui de la transmission de signaux Morse au moyen d'une onde entretenue (CW). L'allumage et l'extinction du porteur au rythme de l'appui sur la clé Morse peuvent également être décrits comme un changement entre une amplitude minimale et une amplitude maximale.

Pour moduler un signal vocal en AM, on utilise également la plage entre l'amplitude minimale et maximale. Dans le diagramme en cascade de l'illustration [ref:n_Wasserfall0], nous voyons un signal vocal modulé en amplitude. On peut clairement distinguer au centre le porteur sous la forme d'une ligne étroite à fréquence constante. À gauche et à droite du porteur, on observe également quelque chose, bien que la fréquence du porteur ne soit pas modifiée !

<margin>
[picture:716:n_Wasserfall0:Signal d'un émetteur radio AM (voix / musique)]
</margin>

Cet effet inattendu est dû au fait que le changement d'amplitude modifie la forme du porteur, qui ne correspond plus à une oscillation sinusoïdale pure. Les fréquences supplémentaires sont appelées *bandes latérales*. C'est dans ces bandes que se trouve l'information transmise, par exemple la voix. Dans l'illustration [ref:n_seitenband], nous voyons une représentation symbolique classique d'un signal AM avec le porteur au centre et les deux bandes latérales à gauche et à droite.

<margin>
[picture:476:n_seitenband:Représentation symbolique d'un signal modulé en amplitude avec porteur et bandes latérales]
</margin>

<webindepth>
*Pourquoi l'AM génère-t-elle des fréquences supplémentaires en plus du porteur ?* Cela s'explique si l'on comprend ce qui est représenté dans un spectre d'amplitude ou un diagramme en cascade : il indique, pour chaque fréquence, l'amplitude correspondante. Plus précisément, il montre, pour toutes les oscillations sinusoïdales possibles de différentes fréquences, l'amplitude de chacune. Ainsi, si l'affichage indique par exemple $\qty{144,3}{\mega\hertz}$, cela signifie qu'une oscillation sinusoïdale pure de $\qty{144,3}{\mega\hertz}$ a été mesurée. Si l'affichage indique simultanément $\qty{144,300}{\mega\hertz}$ et $\qty{144,301}{\mega\hertz}$, cela signifie que deux oscillations sinusoïdales ont été mesurées.

Avec ces connaissances, examinons à nouveau l'émission AM dans le diagramme en cascade. Nous pouvons maintenant voir que de nombreuses fréquences différentes entre $\qty{144,250}{\mega\hertz}$ et $\qty{144,350}{\mega\hertz}$ apparaissent avec des amplitudes variables. Il s'agit donc de plusieurs oscillations sinusoïdales mesurables simultanément.

[picture:738:n_seitenband_frequenzen_einzeln:Plusieurs oscillations sinusoïdales de fréquences différentes]

Reste la question de savoir pourquoi une seule oscillation sinusoïdale, déformée par la modulation, devient soudainement plusieurs oscillations sinusoïdales. Pour y répondre, examinons la situation dans l'autre sens. Si l'on additionne plusieurs oscillations sinusoïdales de fréquences différentes, on obtient une oscillation "déformée" !

[picture:739:n_seitenband_frequenzen_addiert:Somme de plusieurs oscillations sinusoïdales de fréquences différentes]

Il s'agit simplement de deux points de vue différents. On peut considérer qu'il s'agit d'une oscillation déformée ou, au contraire, de la somme de plusieurs oscillations sinusoïdales. C'est la raison pour laquelle la modification de l'amplitude d'un porteur entraîne l'apparition de fréquences supplémentaires à côté du porteur dans le diagramme en cascade.
</webindepth>

[question:NE202]
[question:NE206]

Par ailleurs, la bande passante occupée par l'AM est deux fois plus grande que la fréquence la plus élevée du signal de modulation. Dans notre exemple de la section précédente, la fréquence la plus élevée était de $\qty{2700}{\hertz}$. Par conséquent, ce signal occuperait une bande passante de $\qty{5400}{\hertz}$ en AM.