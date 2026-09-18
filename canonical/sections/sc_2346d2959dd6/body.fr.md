La *régulation automatique de niveau (ALC)* contrôle l'excitation de l'étage final de l'émetteur et réduit l'amplitude du signal dans la branche d'émission en cas de surmodulation. Il ne faut pas confondre l'ALC avec l'AGC (*Automatic Gain Control*), qui se trouve dans la branche de réception (voir figure [ref:e_alc]).

<margin>
[picture:914:e_alc:Régulation automatique de niveau dans un émetteur]
</margin>

L'ALC mesure la puissance de sortie de l'étage final de l'émetteur et la compare à une valeur maximale prédéfinie. Si cette limite est dépassée, l'ALC envoie une tension de régulation à l'étage amplificateur HF en amont dans la branche d'émission, réduisant ainsi l'amplitude du signal émis.

Tant que l'affichage de l'ALC ne réagit pas, on peut supposer que la régulation n'intervient pas et que l'émetteur n'est pas surmodulé par un signal BF trop fort. Dès que l'affichage de l'ALC réagit, on peut en déduire que la régulation, au moins partiellement, est active.

Pour les émissions en BLU, un léger déclenchement de l'ALC est souhaitable, car il permet de compenser les variations de volume de la voix et d'utiliser de manière optimale la puissance d'émission disponible. De nombreux émetteurs-récepteurs disposent d'un affichage ALC correspondant, sur lequel on peut généralement voir jusqu'à quel degré l'ALC peut réagir (zone verte) et à partir de quel niveau une surmodulation trop importante se produit, que l'ALC ne peut plus compenser sans distorsion (zone rouge).

<margin>
[picture:915:e_alc_trx:ALC dans l'affichage d'un émetteur-récepteur]
</margin>

<tip>
En pratique, on peut trouver le point optimal où l'ALC ne régule pas encore en augmentant lentement l'excitation BF jusqu'à ce que l'ALC réagisse. Ensuite, on réduit légèrement l'excitation BF pour que l'ALC ne réagisse plus et que l'affichage de la puissance d'émission indique la puissance de sortie souhaitée (éventuellement un peu moins).
</tip>

---

Pour les émissions utilisant des modes de transmission numériques comme FT8 ou WSPR, le déclenchement de l'ALC est souvent un signe que le signal audio provenant du PC est trop fort et surmodulé. Cela peut entraîner un *splatter* indésirable sur la bande. Par conséquent, le signal audio doit toujours être soigneusement contrôlé pour ces modes de transmission.

<indepth>
Le [manuel](https://wsjt.sourceforge.io/wsjtx-main_fr.html#TRANSCEIVER) du logiciel WSJT-X fournit une bonne recommandation à ce sujet : dans un premier temps, il est conseillé d'activer le mode émission de l'émetteur-récepteur en appuyant sur la touche TUNE pour générer un ton uniforme. Ce ton peut être vérifié à l'oreille via la fonction de monitor de l'appareil ou contrôlé visuellement dans le waterfall du TRX. Aucun distorsion, clic ou autre perturbation ne doit apparaître. Ensuite, on réduit progressivement le réglage de puissance (PWR) depuis son maximum jusqu'à ce que la sortie HF de l'émetteur diminue légèrement – cela est généralement considéré comme un bon niveau pour l'excitation audio. L'affichage ALC ainsi que la puissance de sortie de l'émetteur-récepteur peuvent également aider à trouver le niveau optimal du signal BF.
</indepth>

[question:EF305]