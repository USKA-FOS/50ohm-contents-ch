%TODO: Ce chapitre n'est pas encore définitivement traité et doit encore être révisé !!!

Le facteur d'amplification avant les amplificateurs est généralement exprimé en décibels ($\qty{\frac{1}{10}}{\bel}$). Il faut toujours tenir compte du fait que l'on considère l'amplification de tension ou l'amplification de puissance d'un amplificateur.
*La puissance et la tension sont en relation quadratique* et doivent être calculées différemment !
Un doublement de la tension par un amplificateur correspond à un quadruplement de la puissance (pour une impédance égale à l'entrée et à la sortie de l'amplificateur).

Lors de l'examen de l'amplification de tension d'un amplificateur, nous pouvons l'indiquer en décibels ($\unit{\dB}$). Pour ce faire, nous devons mettre en rapport les deux niveaux de tension au carré (niveau de sortie et niveau d'entrée) et ensuite prendre le logarithme décimal. Nous obtenons alors le résultat en bel. Pour le convertir en décibels, il faut encore le multiplier par le facteur $10$.
Pour pouvoir utiliser directement les niveaux de tension dans le calcul et ne pas avoir à les élever au carré auparavant, on peut extraire le carré comme facteur $2$ du logarithme décimal.
Par conséquent, le résultat doit encore être multiplié par le facteur $2$ dans ce cas. Au total, donc par le facteur $10 \cdot 2 = 20$.

<tip>
Courte excursion dans le calcul des logarithmes

Un carré à l'intérieur du logarithme peut être "extrait" du logarithme. Le carré devient alors le facteur $2$. De manière analogue, il en va de même pour les puissances plus élevées. La puissance devient toujours le multiplicateur devant le logarithme, si on l'"extrait" du logarithme.

Exemple : $\log(x^2) = 2 \cdot \log(x)$
</tip>

%TODO: Tip avec le calcul de Bel et de décibels pour les rapports de tension et de puissance avec explication pourquoi le facteur $2$ se déplace encore devant le logarithme (le carré du logarithme devient le facteur $2$ lors de l'extraction).

Lors de l'examen de l'amplification de puissance d'un amplificateur, nous pouvons également l'indiquer en décibels ($\unit{\dB}$). Pour ce faire, nous devons mettre en rapport les deux niveaux de puissance (niveau de sortie et niveau d'entrée) et ensuite prendre le logarithme décimal. Ensuite, le résultat doit encore être multiplié par le facteur $10$ pour obtenir l'amplification de puissance en $\unit{\dB}$.

Les formules correspondantes pour le calcul de l'amplification de puissance et de tension des amplificateurs se trouvent également dans le recueil de formules.

[question:AD427]
[question:AD428]

Si l'on veut maintenant, à l'inverse, calculer le rapport de la puissance de sortie à la puissance d'entrée à partir de l'amplification de puissance en $\unit{\dB}$, il faut d'abord convertir la valeur en $\unit{\dB}$ en bel en la divisant d'abord par le facteur $10$. Cette valeur doit ensuite être calculée comme exponentielle de base $10$.
Cela donne le facteur d'amplification qui doit être multiplié par la puissance d'entrée pour obtenir la puissance de sortie d'un amplificateur.
Ici, il faut se souvenir de certains rapports en $\unit{\dB}$ (voir le recueil de formules !). Cela permet de simplifier considérablement le calcul.

Exemple :
Pour convertir une amplification de $\qty{13}{\dB}$ en facteur d'amplification, on peut se souvenir que $\qty{3}{\dB}$ correspondent toujours à un doublement de la puissance et $\qty{10}{\dB}$ à un décuplement de la puissance. Dans ce cas, on multiplie les amplifications $2$ et $10$ entre elles et on obtient pour $\qty{13}{\dB}$ le facteur d'amplification $20$.

<tip>
On peut se souvenir, lors du calcul avec des valeurs en $\unit{\dB}$, qu'une addition de valeurs en $\unit{\dB}$ individuelles (connues) correspond toujours à une multiplication des facteurs d'amplification correspondants.

Exemple :
  
$\qty{3}{\dB}$ = Facteur $2$ pour la puissance et facteur $\sqrt{2}$ pour la tension

$\qty{6}{\dB}$ = Facteur $4$ pour la puissance et facteur $\sqrt{4}$ pour la tension

$\qty{10}{\dB}$ = Facteur $10$ pour la puissance et facteur $\sqrt{10}$ pour la tension

$\qty{20}{\dB}$ = Facteur $100$ pour la puissance et facteur $\sqrt{100}$ pour la tension

$\qty{26}{\dB}$ pour la puissance = $\qty{20}{\dB}$ + $\qty{6}{\dB}$ = Facteur $100 \times$ Facteur $4 =$ Facteur $400$

Ainsi, une amplification de puissance de $\qty{26}{\dB}$ correspond à un facteur d'amplification de puissance de $400$.
  
L'amplification de tension correspondante est calculée comme suit :

Facteur $10 \times$ Facteur $2 =$ Facteur $20$

Alternativement : $\sqrt{400}$, si l'on se base sur le facteur d'amplification de puissance.
</tip>

[question:AD426]