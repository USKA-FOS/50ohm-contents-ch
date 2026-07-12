Dans la modulation d'amplitude (AM), un signal de modulation, par exemple un signal vocal, est modulé sur la porteuse en modifiant son amplitude. La fréquence de la porteuse n'est pas affectée par la modulation AM, elle reste inchangée.

Le cas le plus simple et en même temps le plus extrême est celui de la transmission de signaux Morse par onde continue (CW). L'activation et la désactivation de la porteuse au rythme de l'action sur la touche Morse peuvent également être décrites comme une alternance entre une amplitude minimale et maximale.

Pour moduler un signal vocal par AM, on utilise également la plage entre l'amplitude minimale et maximale. Dans le diagramme en cascade de la figure [ref:n_Wasserfall0], nous voyons un signal vocal modulé en amplitude. On peut distinguer au centre la porteuse sous forme de ligne étroite avec une fréquence constante. À gauche et à droite de la porteuse, on observe également quelque chose, bien que la fréquence de la porteuse ne soit pas affectée !

<margin>
[picture:716:n_Wasserfall0:Signal d'un émetteur radio AM (parole / musique)]
</margin>

Cet effet inattendu est dû au fait que la modification de l'amplitude change la forme de la porteuse, qui n'est plus une oscillation sinusoïdale pure. Les fréquences supplémentaires sont appelées *bandes latérales*. C'est dans ces bandes que se trouve l'information transmise, par exemple la parole. Dans la figure [ref:n_seitenband], nous voyons une représentation symbolique habituelle de l'AM avec la porteuse au centre et les deux bandes latérales de chaque côté.

<margin>
[picture:476:n_seitenband:Représentation symbolique d'un signal modulé en amplitude avec porteuse et bandes latérales]
</margin>

<webindepth>
*Pourquoi des fréquences supplémentaires apparaissent-elles à côté de la porteuse en AM ?* Cela peut s'expliquer en comprenant ce qui est représenté dans un spectre d'amplitude ou un diagramme en cascade : il indique pour chaque fréquence l'amplitude correspondante. Plus précisément, il montre pour toutes les oscillations sinusoïdales possibles avec différentes fréquences, l'intensité de leur amplitude. Si, par exemple, l'indication affiche une valeur à $\qty{144,3}{\mega\hertz}$, alors une oscillation sinusoïdale pure avec une fréquence de $\qty{144,3}{\mega\hertz}$ est mesurée. Si, en revanche, l'indication affiche simultanément des valeurs à $\qty{144,300}{\mega\hertz}$ et à $\qty{144,301}{\mega\hertz}$, alors deux oscillations sinusoïdales ont été mesurées.

Avec cette connaissance, examinons à nouveau l'émission AM dans le diagramme en cascade. Nous pouvons maintenant constater que de nombreuses fréquences différentes entre $\qty{144,250}{\mega\hertz}$ et $\qty{144,350}{\mega\hertz}$ apparaissent avec des amplitudes différentes. Il s'ensuit que plusieurs oscillations sinusoïdales sont mesurables simultanément.

[picture:738:n_seitenband_frequenzen_einzeln:Plusieurs oscillations sinusoïdales de fréquences différentes]

La question qui se pose est de savoir pourquoi une seule oscillation sinusoïdale, déformée par modulation, devient soudainement plusieurs oscillations sinusoïdales. Pour répondre à cette question, nous allons examiner le processus en sens inverse. Si l'on a plusieurs oscillations sinusoïdales de fréquences différentes et que l'on les additionne, on obtient une oscillation "déformée" !

[picture:739:n_seitenband_frequenzen_addiert:Somme de plusieurs oscillations sinusoïdales de fréquences différentes]

Il s'agit simplement de deux points de vue différents. On peut le considérer soit comme une oscillation déformée, soit comme la somme de plusieurs oscillations sinusoïdales. Et c'est la raison pour laquelle la modification de l'amplitude d'une porteuse entraîne l'apparition de fréquences supplémentaires à côté de la porteuse dans le diagramme en cascade.
</webindepth>

[question:NE202]
[question:NE206]

Par ailleurs, la bande passante occupée par l'AM est deux fois plus élevée que la fréquence la plus élevée du signal de modulation. Dans notre exemple du paragraphe précédent, la fréquence la plus élevée était de $\qty{2700}{\hertz}$. En conséquence, ce signal, s'il était émis en AM, occuperait une bande passante de $\qty{5400}{\hertz}$.