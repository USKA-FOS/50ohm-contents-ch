En modulation de fréquence (FM), un signal modulant est superposé au porteur en modifiant sa fréquence. L’amplitude de la porteuse, en revanche, reste inchangée et est idéalement constante.


<margin>
[picture:711:n_fm_wasserfall:Signal d’une émission radioamateur en FM (voix)]
</margin>

<margin>
[picture:357:n_fm_frequenzmodulation:Modulation de fréquence]
</margin>

[question:NE301]
[question:NE302]
[question:NE303]

Plus le volume de la voix captée par le microphone est élevé — donc plus l’amplitude du signal modulant est grande — plus l’écart de la fréquence porteuse par rapport à sa valeur centrale augmente, tant vers le haut que vers le bas. Par conséquent, la bande passante occupée par l’émission s’élargit.


---


La valeur maximale de cet écart de la fréquence porteuse est appelée *excursion de fréquence porteuse* ou simplement *excursion*. Sur certains émetteurs-récepteurs, cette valeur peut être réglée, tandis que sur d’autres, elle est fixe. Souvent, il est possible de basculer entre deux valeurs prédéfinies : le FM « classique » et le FM à bande étroite (en anglais Narrow-FM, abrégé en NFM), qui occupe environ la moitié de la bande passante.


<indepth>
L’*excursion de fréquence porteuse* s’exprime, comme la bande passante, en hertz, mais il ne faut pas la confondre avec celle-ci. L’excursion désigne l’écart maximal de la fréquence porteuse. La bande passante est approximativement égale au double de la somme de l’excursion et de la bande passante du signal BF. Exemple : un signal BF occupant une bande passante de $\qty{3}{\kilo\hertz}$ est modulé avec une excursion de $\qty{3}{\kilo\hertz}$. Cela donne une bande passante totale de :
$2 \cdot (\qty{3}{\kilo\hertz} + \qty{3}{\kilo\hertz}) = \qty{12}{\kilo\hertz}$
</indepth>


Dans ce contexte, il convient également de tenir compte du plan de bandes de l’IARU, qui fournit des indications sur la bande passante maximale recommandée pour une émission selon les différentes bandes de fréquences. Par exemple, dans la bande des $\qty{2}{\meter}$ réservée à la téléphonie FM, la bande passante maximale recommandée est de $\qty{12}{\kilo\hertz}$, ce qui correspond au FM à bande étroite. La question suivante peut être résolue à l’aide de ces connaissances et du plan de bandes de l’IARU, qui est disponible comme outil d’aide lors de l’examen.


[question:BC216]


Si l’excursion ne peut pas être réglée ou ne l’est pas suffisamment, cela peut entraîner en pratique une émission occupant une bande passante supérieure à celle autorisée pour la bande de fréquences utilisée. De nombreux émetteurs-récepteurs portables et mobiles plus anciens disposent d’une excursion fixe, ce qui peut conduire à une bande passante occupée allant jusqu’à $\qty{25}{\kilo\hertz}$.


Dans de telles situations, il est possible de parler plus doucement dans le microphone. Cela réduit l’amplitude du signal modulant et, par conséquent, l’écart de la fréquence porteuse, ce qui diminue la bande passante occupée par l’émission.


[question:NE306]


Comme l’amplitude de la porteuse ne varie pas, la puissance d'émission reste également inchangée par la modulation. Tant que la touche PTT est enfoncée, la puissance d'émission est maximale, que l’on parle doucement, fort ou pas du tout dans le microphone. Cela présente l’avantage que les interférences n’entraînent pas de variations du volume du signal vocal.


[question:NE304]
