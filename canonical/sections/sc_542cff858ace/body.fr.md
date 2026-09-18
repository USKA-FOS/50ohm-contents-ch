Toute installation de radioamateur fixe doit être déclarée à l’OFCOM, conformément à l’article 9 de l’ordonnance sur la protection contre les rayonnements non ionisants (ORNI), lorsque sa puissance isotrope rayonnée équivalente (EIRP) atteint ou dépasse $\qty{10}{\watt}$. Cette déclaration doit être effectuée avant le début des émissions. Le radioamateur doit fournir la preuve que les valeurs limites sont respectées, que les distances de sécurité nécessaires ont été déterminées et que celles-ci se situent dans la zone contrôlée. Dans le langage courant, les radioamateurs parlent de « déclaration sur l’honneur » pour désigner cette procédure.

Il est possible de renoncer à cette déclaration uniquement si la puissance isotrope rayonnée équivalente (EIRP) est *inférieure* à $\qty{10}{\watt}$ EIRP – et non $\qty{10}{\watt}$ de puissance d’émission, ni $\qty{10}{\watt}$ de puissance rayonnée effective (ERP) !

Même sans calcul précis, il est rapidement évident que la combinaison d’une puissance d’émission de $\qty{6}{\watt}$ et d’un gain d’antenne de $\qty{13}{\dBd}$ (facteur $\num{20}$) dépasse largement la valeur limite de $\qty{10}{\watt}$ EIRP.

<indepth>
Pour s’entraîner, on peut tout de même effectuer le calcul : nous utilisons à nouveau la formule du recueil de formules :

$P_\mathrm{EIRP} = P_\mathrm{émetteur} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{6}{\watt} \cdot 10^{\frac{\qty{13}{\dBd}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{197}{\watt}$

Ce calcul peut également être effectué mentalement en décomposant le gain total en parties significatives :

$\qty{13}{\dBd} + \qty{2,15}{\dB} = \qty{10}{\dBd} + \qty{3}{\dB} + \qty{2,15}{\dB}$

On obtient ainsi :

$P_\mathrm{EIRP} = \qty{6}{\watt} \cdot 10 \cdot 2 \cdot 1,64 \approx \qty{197}{\watt}$
</indepth>

[question:EK104]

Dans le [guide pour la déclaration des installations de radioamateur fixes selon l’article 9 de l’ORNI](https://50ohm.de/abemfv), il est précisé ce qu’il faut entendre par distance de sécurité. La distance de sécurité liée au site décrit l’écartement nécessaire entre l’antenne de référence et la zone où les valeurs limites doivent être respectées. Il faut également prendre en compte les intensités de champ pertinentes des installations radio fixes environnantes.

Il est important de noter que la distance de sécurité ne se réfère pas à un point unique de l’antenne, mais à l’ensemble de la structure de l’antenne. En d’autres termes, pour chaque point de l’antenne, il doit être garanti que les valeurs limites sont respectées en dehors de la distance de sécurité calculée.

[question:EK107]