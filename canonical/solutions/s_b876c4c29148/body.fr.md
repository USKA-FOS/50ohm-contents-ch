# Solution par exclusion
Il est utile de reconnaître qu'il s'agit du démodulateur d'enveloppe présenté dans le chapitre "Démodulateur".
On peut voir sur le côté gauche du circuit que le signal ZF est appliqué à l'entrée du circuit.
$\rightarrow$ Cela élimine la réponse "La sortie pour le signal ZF.".

La connexion $\text{X}$ se trouve derrière un filtre passe-bas RC, qui est construit avec un condensateur électrolytique (reconnaissable au petit "+"). Les condensateurs électrolytiques ont une capacité relativement élevée. Pour la relation entre la fréquence de coupure ($f_\text{g}$) et la capacité ($C$), nous considérons la formule (filtre, passe-bas RC) du recueil de formules :

$f_\text{g} = \frac{1}{2\cdot\pi\cdot R \cdot C}$

Une grande capacité ($C$) crée un grand dénominateur et donc une petite fréquence de coupure ($f_\text{g}$) pour le filtre passe-bas RC.
$\rightarrow$ Cela élimine les réponses "La sortie pour le signal BF." et "La sortie pour le signal d'oscillateur.".

Une tension basse fréquence est appliquée à la connexion $\text{X}$, qui peut être utilisée pour la régulation.