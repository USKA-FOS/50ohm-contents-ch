## Explication

### Source pour le calcul de la distance de sécurité

Le document « Explication des procédures d’évaluation selon le règlement BEMFV » de l’Agence fédérale des réseaux, daté d’août 2013, apporte des éclaircissements.

La section 1.2.2 (Exécution du calcul du champ lointain) contient la formule (5) pour calculer la distance de sécurité – désignée ici par $r$ :

$r = \sqrt(\frac{Z_0}{4 \cdot \pi}) \cdot \frac{\sqrt{P \cdot G_i}}{E_g} \cdot C$

Avec $Z_0 = \qty{120\pi}{\Ohm}$, le premier facteur se simplifie en $\sqrt{\qty{30}{\Ohm}}$. En négligeant le facteur de perte $C$, on obtient la formule indiquée dans l’énoncé et les outils de l’Agence fédérale des réseaux pour calculer la distance de sécurité :

$d = \frac{\sqrt{\qty{30}{\Ohm} \cdot P_\mathrm{EIRP}}}{E}$

La section 1.2.1 précise que la formule ci-dessus pour le calcul de la distance de sécurité n’est valable que dans le champ lointain d’une source de rayonnement.

Elle y distingue en outre le *champ proche réactif* et le *champ proche rayonnant*.

### Champ proche réactif

On se trouve dans le champ proche réactif d’une antenne lorsque la distance par rapport à l'antenne est

$d < \frac{\lambda}{2\pi}$

Dans ce cas :

« À l’intérieur du champ proche réactif, il peut y avoir localement de fortes augmentations du champ électrique et magnétique, qui ne peuvent pas être déterminées par le calcul du champ lointain. Par conséquent, un calcul du champ lointain n’est pas autorisé dans cette zone. »

### Champ proche rayonnant

On se trouve dans le champ proche rayonnant d’une antenne lorsque

* l’on se situe en dehors du champ proche réactif et
* la distance par rapport à l'antenne est inférieure à $4 \lambda$.

Dans ce cas :

« Si la formule du champ lointain est appliquée dans la zone du champ proche rayonnant, on obtient pour la plupart des formes d’antennes des estimations conservatrices, c’est-à-dire que les intensités de champ réelles sont inférieures à celles calculées. Cela ne s’applique cependant pas à tous les types d’antennes : par exemple, une antenne magnétique produit dans le champ proche des intensités de champ plus élevées que celles prédites par la formule du champ lointain. En particulier, les antennes dont les dimensions géométriques sont petites par rapport à la longueur d’onde présentent un tel comportement. »

### Calculs de champ proche

La section 1.3 aborde la possibilité de calculer le champ proche par simulation :

« L’utilisation de méthodes numériques, comme celles appliquées dans les programmes de calcul de champ proche, permet de calculer avec précision les champs électriques et magnétiques en amplitude et en phase pour n’importe quel point de l’espace autour d’une antenne. »

### Interprétation

Les explications concernant le champ proche réactif et rayonnant ainsi que les calculs de champ proche permettent de justifier la réponse donnée ci-dessus.