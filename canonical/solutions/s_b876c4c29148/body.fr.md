# Solution par élimination
Il est utile de reconnaître qu’il s’agit ici du *démodulateur à enveloppe* représenté dans le chapitre « Démodulator ».  
Du côté gauche du circuit, on voit que le signal FI est appliqué à l’entrée du circuit.
$\rightarrow$ Cela élimine la réponse « La sortie pour le signal FI ».


La borne $\text{X}$ se trouve après un *filtre passe-bas* RC, constitué d’un condensateur électrolytique (reconnaissable au petit « + »). Les condensateurs électrolytiques ont une capacité relativement élevée. Pour la relation entre la *fréquence de coupure* ($f_\text{g}$) et la capacité ($C$), nous considérons la formule (filtre, *passe-bas* RC) du *recueil de formules* :

$f_\text{g} = \frac{1}{2\cdot\pi\cdot R \cdot C}$


Une grande capacité ($C$) produit un grand dénominateur et donc une *fréquence de coupure* ($f_\text{g}$) faible pour le *filtre passe-bas* RC.
$\rightarrow$ Cela élimine les réponses « La sortie pour le signal BF » et « La sortie pour le signal d’oscillateur ».


À la borne $\text{X}$, une tension basse fréquence est présente, utilisable pour la régulation.