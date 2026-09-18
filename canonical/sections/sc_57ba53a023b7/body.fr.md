Tout le monde a déjà entendu un amplificateur surmodulé ou un enregistrement audio saturé. Si le volume est trop élevé lors de l'enregistrement ou de la lecture, des distorsions peuvent survenir.

Si, par exemple, un signal audio trop fort est appliqué à l'entrée d'un émetteur, des harmoniques peuvent se produire et être émises. Dans l'illustration [ref:uebersteuerung_ft8], un signal FT8 surmodulé est représenté dans le diagramme en cascade : à gauche, en jaune, le signal souhaité est visible, et à droite, les harmoniques indésirables.

<margin>
[picture:720:uebersteuerung_ft8:Un signal FT8 surmodulé, à l'extrême gauche le signal souhaité, à droite les harmoniques indésirables]
[photo:328:uebersteuerung_ft8_wsjtx:Un signal FT8 surmodulé dans le waterfall du logiciel WSJTX]
</margin>

Des distorsions dues à la surmodulation peuvent également se produire dans l'amplificateur d'émission. Pour l'éviter, de nombreux postes radio disposent d'un réglage automatique de niveau (en anglais : Automatic Level Control, ALC). Celui-ci peut intervenir en réduisant le gain.

---

Pour les émissions utilisant des procédés de transmission numériques à amplitude constante, comme par exemple FT8, WSPR ou RTTY, le déclenchement de l'ALC est souvent un indice que le signal BF provenant du PC est trop fort et surmodulé. Cela peut entraîner un *splatter* indésirable sur la bande. C'est pourquoi, pour ces procédés de transmission, le signal BF doit toujours être soigneusement contrôlé. Une réduction du niveau par l'ALC serait en soi peu critique, car dans ces procédés, l'information est transmise par modulation par déplacement de fréquence. Néanmoins, le déclenchement de l'ALC est un fort indicateur que le signal BF est déjà surmodulé.


<indepth>
Le [manuel](https://wsjt.sourceforge.io/wsjtx-main_fr.html#TRANSCEIVER) du logiciel WSJTX donne une bonne recommandation à ce sujet : dans un premier temps, il est conseillé d'activer le mode émission du transceiver en appuyant sur la touche TUNE pour générer un ton uniforme. Ce ton peut être vérifié à l'oreille via la fonction de monitorage de l'appareil ou contrôlé visuellement dans le waterfall du transceiver. Aucune distorsion, clic ou autre perturbation ne doit apparaître. Ensuite, régler le potentiomètre de puissance (PWR) progressivement vers le bas depuis son maximum jusqu'à ce que la sortie HF de l'émetteur commence à diminuer légèrement – cela est généralement considéré comme un bon niveau pour l'excitation audio. L'affichage de l'ALC ainsi que la puissance de sortie du transceiver peuvent également aider à trouver le niveau optimal du signal BF.
</indepth>

Pour les procédés de transmission numériques à amplitude variable (par exemple PSK31, QPSK, 16-QAM), l'ALC peut en revanche entraîner de nouveaux problèmes. Le signal pourrait, selon le volume ou la fréquence, déclencher l'ALC à différents moments avec une intensité variable et ainsi modifier de manière indésirable l'amplitude au fil du temps. Autrement dit, notre signal utile est en plus modulé en amplitude. Cela génère d'autres composantes de fréquence qui sont émises sous forme d'émissions parasites. D'une part, cela peut perturber d'autres radioamateurs ou services de radiocommunication sur des fréquences adjacentes. D'autre part, la démodulation au niveau du récepteur est rendue plus difficile.


Le fait que l'ALC pose problème et dans quelle mesure dépend de nombreux facteurs. Outre le procédé de transmission utilisé, la mise en œuvre concrète de l'ALC dans le transceiver joue un rôle, par exemple en ce qui concerne les temps de réaction et de maintien. L'affichage de l'ALC varie également selon les appareils. Un coup d'œil dans le manuel peut éclairer sur le moment où le réglage de niveau intervient et comment cela est indiqué. On peut cependant dire en général : si l'ALC n'intervient pas, elle ne pose pas de problème.


Règle : pour les procédés de transmission numériques via un signal BF, il faut veiller à maintenir le niveau BF suffisamment bas pour éviter toute surmodulation et tout déclenchement du réglage automatique de niveau.

[question:EJ218]
[question:EJ217]
[question:EJ219]
