<margin>
[picture:804:mischer_linear_vs_nichtlinear:Résistance linéaire et diode non linéaire]
</margin>

Les courbes caractéristiques de composants ou d'éléments peuvent avoir un caractère linéaire, non linéaire ou partiellement mixte. Par exemple, une résistance a une courbe caractéristique linéaire, tandis que la courbe caractéristique d'une diode est non linéaire [ref:mischer_linear_vs_nichtlinear].

Dans la plage linéaire des courbes caractéristiques, il n'y a pas de distorsion des signaux d'entrée car chaque modification d'un signal d'entrée entraîne une modification proportionnellement égale du signal de sortie. Mathématiquement, cela correspond à un comportement linéaire (addition). Un exemple de courbe caractéristique de commande linéaire est une résistance. Sur les courbes caractéristiques de commande linéaires ou dans la plage linéaire des courbes caractéristiques de commande, **aucun** processus de mélange n'a lieu.

Dans la plage non linéaire des courbes caractéristiques, il y a distorsion des signaux d'entrée car une modification d'un signal d'entrée n'entraîne pas une modification proportionnellement égale d'un signal de sortie. Mathématiquement, cela correspond à un comportement non linéaire dans lequel une multiplication des grandeurs d'entrée a lieu et donc des produits de mélange supplémentaires (dépendant de la forme de la courbe caractéristique) sont générés. Par conséquent, un processus de mélange a toujours lieu dans la plage non linéaire des courbes caractéristiques. Les produits de mélange génèrent toujours des fréquences supplémentaires dans le signal de sortie qui se présentent principalement sous forme de sommes et de différences des fréquences d'entrée dans le signal de sortie.

En pratique, de nombreux produits de mélange indésirables d'ordre supérieur se forment, qui doivent être supprimés de manière ciblée par des mesures techniques telles que le filtrage.

%TODO ÉVENTUELLEMENT RÉFÉRENCE À D'AUTRES LITTÉRATURES OU ARRIÈRE-PLAN MATHÉMATIQUE

[question:AF212]

---
<margin>
[picture:805:mischer_ringmischer:Mélangeur équilibré, mélangeur en anneau ou également modulateur en anneau]
</margin>

L'objectif d'un mélangeur est que seuls les produits de mélange souhaités apparaissent à sa sortie et que les produits de mélange indésirables ainsi que les signaux d'entrée soient supprimés au maximum.

On atteint cet objectif au mieux à l'aide d'un mélangeur équilibré. Celui-ci est construit avec 4 diodes ou transistors en circuit en anneau [ref:mischer_ringmischer]. Grâce à sa structure symétrique, les signaux d'entrée sont supprimés au maximum à la sortie. D'autres formes de mélangeurs, comme par exemple les mélangeurs à double diode, les mélangeurs à double transistor ainsi que les mélangeurs à diodes additives, conduisent toujours l'un des signaux d'entrée à la sortie en raison de leur structure non symétrique.

<indepth>
Fonctionnement d'un mélangeur en anneau:

L'oscillateur local ($U_2$ dans le schéma) rend toujours deux diodes opposées conductrices pendant une demi-onde, tandis que les deux autres diodes sont bloquées. Dans la demi-onde suivante de l'oscillateur local, les rapports s'inversent exactement. Pour cela, l'amplitude de l'oscillateur local ($U_2$) doit être suffisamment élevée pour que les diodes puissent être suffisamment commandées pendant les demi-ondes positives et négatives.

C'est ainsi que l'anneau de diodes fonctionne comme un inverseur de polarité pour le signal appliqué à l'entrée ($U_1$).
Pour obtenir un bon résultat de mélange en ce qui concerne les produits de mélange indésirables et la suppression du signal d'entrée, son amplitude doit être nettement inférieure à l'amplitude de l'oscillateur local.
Des valeurs optimales sont obtenues par des mélangeurs en anneau à haut niveau, dont le niveau d'entrée de l'oscillateur local peut se situer dans la plage allant jusqu'à $\qty{10}{\milli\watt}$.
</indepth>

<tip>
Il est important de pouvoir distinguer le mélangeur en anneau du circuit d'un redresseur à diodes, qui a une apparence très similaire, par le fait que les diodes du mélangeur en anneau sont connectées en série en anneau (cathode respectivement connectée à l'anode suivante de la diode suivante). Dans le cas du redresseur, en revanche, 2 cathodes et 2 anodes sont toujours connectées.
</tip>
  
Le mélangeur équilibré, également appelé mélangeur en anneau ou modulateur en anneau, est le mieux adapté pour supprimer les signaux de sortie indésirables.

% FEEDBACK: Comment cela fonctionne-t-il? Cela n'est pas clair! De plus: indication de la confusion avec le redresseur en pont!
% RÉPONSE AU FEEDBACK: Nous avons complété l'article par un conseil et une approfondissement concernant les points abordés.

[question:AF213]
[question:AF214]