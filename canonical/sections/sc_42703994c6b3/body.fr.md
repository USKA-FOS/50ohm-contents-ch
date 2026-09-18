<margin>
[picture:804:mischer_linear_vs_nichtlinear:Résistance linéaire et diode non linéaire]
</margin>


Les composants et modules peuvent se comporter de manière *linéaire* ou *non linéaire*. Dans un composant linéaire, la grandeur de sortie suit la grandeur d’entrée selon une relation fixe. Une résistance idéale possède par exemple une caractéristique linéaire. En revanche, la caractéristique d’une diode est non linéaire (cf. [ref:mischer_linear_vs_nichtlinear]).


Pour un processus de mélange, un comportement purement linéaire ne suffit pas. Si plusieurs signaux sont transmis par un circuit linéaire, ils peuvent être amplifiés, atténués ou additionnés, mais ils ne s’influencent pas mutuellement. Aucune nouvelle composante de fréquence n’est ainsi générée.


Pour qu’un mélange ait lieu, les signaux d’entrée doivent être combinés. Cela peut par exemple se produire grâce à la caractéristique non linéaire d’une diode ou d’un transistor. Une autre méthode couramment utilisée consiste à allumer et éteindre rapidement le signal d’entrée, ou à le commuter, à l’aide du signal de l’oscillateur. Une telle opération de commutation n’est pas non plus un processus linéaire et provoque la combinaison des deux signaux.


C’est précisément cette propriété qui est exploitée de manière ciblée dans un mélangeur. C’est pourquoi les étages de mélange fonctionnent avec des composants non linéaires ou avec des circuits dans lesquels des transistors ou des diodes sont commutés par le signal de l’oscillateur.

En pratique, de nombreux produits de mélange indésirables d’ordre supérieur se forment également. Ceux-ci doivent être supprimés de manière ciblée par des mesures techniques telles que le filtrage.


[question:AF212]


L’objectif d’un mélangeur est qu’à sa sortie n’apparaissent idéalement que les produits de mélange souhaités, tandis que les produits de mélange indésirables ainsi que les signaux d’entrée sont au maximum supprimés.


On atteint au mieux cet objectif à l’aide d’un所谓 mélangeur équilibré. Celui-ci est constitué de 4 diodes ou transistors montés en anneau [ref:mischer_ringmischer]. Grâce à sa structure symétrique, les signaux d’entrée sont supprimés au maximum à la sortie. D’autres types de mélangeurs, comme par exemple les mélangeurs à double diode, les mélangeurs à double transistor ou les mélangeurs à diodes additifs, transmettent toujours l’un des signaux d’entrée à la sortie en raison de leur structure asymétrique.


<indepth>
Fonctionnement d’un mélangeur en anneau :


L’oscillateur local ($U_2$ sur le schéma) commute toujours deux diodes opposées à l’état passant pendant une demi-onde, tandis que les deux autres diodes sont bloquées. Lors de la demi-onde suivante de l’oscillateur local, les conditions s’inversent exactement. Pour cela, l’amplitude de l’oscillateur local ($U_2$) doit être suffisamment élevée pour que les diodes puissent être suffisamment polarisées pendant les demi-ondes positives et négatives.


Ainsi, le montage en anneau de diodes fonctionne comme un inverseur de polarité pour le signal présent à l’entrée ($U_1$).
Pour obtenir un bon résultat de mélange en termes de produits de mélange indésirables et de suppression du signal d’entrée, son amplitude doit être nettement inférieure à celle de l’oscillateur local.
Les valeurs optimales sont atteintes avec les所谓 mélangeurs en anneau à haut niveau, dont le niveau d’entrée de l’oscillateur local peut atteindre jusqu’à $\qty{10}{\milli\watt}$.

<webonly>
[include:applet_ringmodulator]
</webonly>
<latexonly>
[picture:805:mischer_ringmischer:Mélangeur équilibré, mélangeur en anneau ou modulateur en anneau]
</latexonly>
</indepth>

<tip>
Il est important de pouvoir distinguer un mélangeur en anneau d’un circuit redresseur à diodes, qui lui ressemble beaucoup, par le fait que dans un mélangeur en anneau, les diodes sont montées en série en anneau (la cathode de chaque diode étant reliée à l’anode de la diode suivante). Dans un redresseur, en revanche, ce sont toujours deux cathodes et deux anodes qui sont reliées entre elles.
</tip>

Le mélangeur équilibré, également appelé mélangeur en anneau ou modulateur en anneau, est le plus adapté pour supprimer les signaux de sortie indésirables.


[question:AF213]
[question:AF214]
