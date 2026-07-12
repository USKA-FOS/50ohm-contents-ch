Le *Automatic-Level-Control (ALC)* régule l'excursion de l'étage final de l'émetteur de l'appareil radio et réduit, en cas de surcharge, l'amplitude du signal dans la branche d'émission. Il ne faut pas confondre l'ALC avec l'AGC (Automatic-Gain-Control), qui se trouve dans la branche du récepteur (voir figure [ref:e_alc]).

<margin>
[picture:914:e_alc:Automatic-Level-Control dans un émetteur]
</margin>

L'ALC détecte la puissance de sortie de l'étage final de l'émetteur et la compare à une valeur maximale prédéfinie. En cas de dépassement de cette valeur limite, l'ALC fournit une tension de régulation correspondante à l'étage amplificateur HF précédent dans la branche d'émission et réduit ainsi l'amplitude du signal d'émission.

Tant que l'indicateur ALC ne réagit pas, on peut supposer que la régulation n'intervient pas et que l'émetteur n'est pas surchargé par un signal audio trop fort. Dès que l'indicateur ALC réagit, on peut supposer que la régulation devient, au moins partiellement, active.

Dans le cas des émissions SSB, une légère réaction de l'ALC est même souhaitable, car cela permet de compenser les fluctuations de volume de la voix et d'utiliser de manière optimale la puissance d'émission disponible. De nombreux émetteurs-récepteurs disposent d'un indicateur ALC correspondant, sur lequel il est généralement possible de voir jusqu'à quel point l'ALC peut réagir (zone verte) et à partir de quelle zone une excursion trop forte se produit, que l'ALC ne peut plus compenser sans distorsion (zone rouge).

<margin>
[picture:915:e_alc_trx:ALC dans l'affichage d'un appareil radio]
</margin>

<tip>
En pratique, on peut trouver le point optimal, auquel l'ALC n'excursionne pas encore, en augmentant lentement l'excursion audio jusqu'au point où l'ALC réagit. Ensuite, on réduit à nouveau légèrement l'excursion audio, de sorte que l'ALC ne réagit plus et que l'indicateur de puissance d'émission affiche encore la puissance de sortie souhaitée (éventuellement un peu moins).
</tip>

---

Dans le cas d'émissions avec des procédés de transmission numériques tels que FT8 ou WSPR, la réaction de l'ALC est souvent un indice que le signal audio de l'ordinateur est trop fort et qu'il est surchargé. Cela peut entraîner un *Splatter* indésirable sur la bande. C'est pourquoi le signal audio doit toujours être contrôlé avec soin dans le cas de ces procédés de transmission.

<indepth>
Le [manuel](https://wsjt.sourceforge.io/wsjtx-main_en.html#TRANSCEIVER) du logiciel WSJTX donne à ce sujet une bonne recommandation : dans un premier temps, on doit mettre l'émetteur-récepteur en mode émission en appuyant sur la touche TUNE pour produire un son uniforme. Ce son peut être vérifié en l'écoutant via la fonction de surveillance de l'appareil ou contrôlé visuellement dans le spectre de l'émetteur-récepteur. Il ne doit pas y avoir de distorsions, de clics ou d'autres perturbations. Ensuite, on réduit le régulateur PWR de son maximum lentement vers le bas jusqu'à ce que la sortie HF de l'émetteur chute légèrement - cela est généralement considéré comme un bon niveau pour l'excursion audio. L'indicateur ALC ainsi que la puissance de sortie de l'émetteur-récepteur peuvent également aider à trouver le niveau de signal audio optimal.
</indepth>

[question:EF305]
