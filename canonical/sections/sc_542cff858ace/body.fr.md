Toute installation radioamateur fixe doit être déclarée auprès de la BNetzA, conformément à l'article 9 du BEMFV, lorsqu'elle a une puissance isotrope rayonnée équivalente (EIRP) de $\qty{10}{\watt}$ ou plus. Cela doit être fait avant la mise en service de l'installation. Le radioamateur doit alors prouver qu'il respecte les limites et qu'il a déterminé les distances de sécurité nécessaires, qui doivent se situer dans la zone contrôlée. En langage courant, cela est appelé *déclaration de conformité* par les radioamateurs.

On peut renoncer à une déclaration de conformité uniquement si la puissance isotrope rayonnée équivalente (EIRP) est *inférieure* à $\qty{10}{\watt}$ EIRP - pas $\qty{10}{\watt}$ de puissance d'émission, ni $\qty{10}{\watt}$ ERP!

Même sans calcul précis, il est rapidement évident que la combinaison d'une puissance d'émission de $\qty{6}{\watt}$ et d'un gain d'antenne de $\qty{13}{\dBd}$ (facteur 20) dans la question suivante dépasse clairement la limite de $\qty{10}{\watt}$ EIRP.

<indepth>
Pour s'entraîner, on peut quand même faire le calcul : nous utilisons à nouveau la formule du recueil de formules : 

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{6}{\watt} \cdot 10^{\frac{\qty{13}{dBd}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{197}{\watt}$

Ce calcul peut également être facilement effectué mentalement en décomposant le gain global en parts significatives :
  
$\qty{13}{\dBd} + \qty{2,15}{\dB} = \qty{10}{\dBd} + \qty{3}{\dB} + \qty{2,15}{\dB}$

Ainsi, on obtient :

$P_\text{EIRP} = \qty{6}{\watt} \cdot 10 \cdot 2 \cdot 1,64 \approx \qty{197}{\watt}$
</indepth>

[question:EK104]
  
Dans le [guide pour la réalisation de la déclaration des installations radioamateurs fixes selon l'article 9 du BEMFV](https://50ohm.de/abemfv), il est précisément défini ce que l'on entend par distance de sécurité. La distance de sécurité liée au lieu décrit la distance nécessaire entre l'antenne de référence et la zone dans laquelle les limites applicables doivent être respectées. Il est également nécessaire de prendre en compte les intensités de champ pertinentes des installations radio fixes environnantes.

Il est important de noter que la distance de sécurité ne se réfère pas à un point unique de l'antenne, mais à toute la structure de l'antenne. En d'autres termes, pour chaque point de l'antenne, il doit être garanti que les limites sont respectées en dehors de la distance de sécurité calculée.

[question:EK107]
