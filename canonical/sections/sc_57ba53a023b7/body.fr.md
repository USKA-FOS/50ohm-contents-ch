Chacun a probablement déjà entendu un amplificateur ou un enregistrement audio surchargé. Si le volume est trop fort lors de l'enregistrement ou de la lecture, des distorsions peuvent se produire.

Par exemple, si un signal audio trop puissant est appliqué à l'entrée d'un émetteur, des harmoniques peuvent être générées et émises. Dans la figure [ref:uebersteuerung_ft8], un signal FT8 ainsi surchargé est représenté dans un diagramme en cascade : à gauche, on peut voir en jaune le signal souhaité et à droite les harmoniques indésirables.

<margin>
[picture:720:uebersteuerung_ft8:Un signal FT8 surchargé, tout à gauche le signal souhaité, à droite les harmoniques indésirables]
[photo:328:uebersteuerung_ft8_wsjtx:Un signal FT8 surchargé dans la cascade du logiciel WSJTX]
</margin>

Des distorsions dues à la surcharge peuvent également se produire dans l'amplificateur d'émission. Pour l'éviter, de nombreux appareils radio disposent d'un contrôle automatique de niveau (en anglais : Automatic Level Control, ALC). Il peut intervenir en réduisant l'amplification.

---

Lors d'émissions utilisant des procédés de transmission numériques tels que FT8, WSPR ou RTTY avec une amplitude constante, le déclenchement de l'ALC est souvent un indice que le signal audio provenant de l'ordinateur est trop fort et qu'il y a surcharge. Cela peut entraîner un *splatter* indésirable sur la bande. C'est pourquoi le signal audio doit toujours être soigneusement contrôlé dans ces procédés de transmission. Une réduction du niveau par l'ALC serait en soi initialement non critique, car dans ces procédés, l'information réside dans la modulation de fréquence. Néanmoins, le déclenchement de l'ALC est un fort indice que le signal BF est déjà surchargé.

<indepth>
Le [manuel](https://wsjt.sourceforge.io/wsjtx-main_en.html#TRANSCEIVER) du logiciel WSJTX donne à ce sujet une bonne recommandation : dans un premier temps, on doit mettre l'émetteur-récepteur en mode émission en appuyant sur la touche TUNE, afin de produire un son uniforme. Ce son peut être vérifié à l'aide de la fonction de surveillance de l'appareil en l'écoutant ou contrôlé visuellement dans la cascade du TRX. Il ne doit pas y avoir de distorsions, de clics ou d'autres perturbations. Ensuite, on réduit lentement le régulateur PWR de son maximum vers le bas jusqu'à ce que la sortie HF de l'émetteur chute légèrement - cela est généralement considéré comme un bon niveau pour la modulation audio. L'affichage de l'ALC ainsi que la puissance de sortie de l'émetteur-récepteur peuvent également aider à trouver le niveau optimal du signal audio.
</indepth>

Dans le cas des procédés de transmission numériques à amplitude variable (par exemple, PSK31, QPSK, 16-QAM), l'ALC peut cependant entraîner de nouveaux problèmes. Le signal pourrait, selon le volume ou la fréquence, déclencher l'ALC à des moments différents et ainsi modifier de manière indésirable l'amplitude au cours du temps. Cela signifie que notre signal utile est en outre modulé en amplitude. Cela entraîne l'apparition de nouvelles composantes fréquentielles qui sont émises comme émissions secondaires. D'une part, d'autres radioamateurs ou services radio sur des fréquences voisines peuvent être perturbés. D'autre part, le décodage est rendu plus difficile au niveau du récepteur.

Le fait que l'ALC pose des problèmes et à quel point ceux-ci sont graves dépend de nombreux facteurs. Outre le procédé de transmission utilisé, la mise en œuvre concrète de l'ALC dans l'émetteur-récepteur, par exemple en ce qui concerne le temps de réaction et de maintien, joue un rôle. L'affichage de l'ALC est également différent selon les appareils. Un coup d'œil dans le manuel peut donner des informations sur le moment où la régulation de niveau intervient et comment cela est affiché. En général, on peut cependant dire : si l'ALC n'intervient pas, elle ne pose pas de problème.

À retenir : Dans le cas des procédés de transmission numériques au moyen d'un signal BF, il est important de maintenir le niveau BF aussi faible que possible afin qu'il n'y ait pas de surcharge et que la régulation automatique de niveau n'intervienne pas.

[question:EJ218]
[question:EJ217]
[question:EJ219]
