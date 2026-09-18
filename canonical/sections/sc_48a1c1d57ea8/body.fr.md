Dans la classe E, nous avons déjà rencontré une formule approchée permettant de calculer la distance de sécurité par rapport à une antenne :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{E}$


Cette formule peut être appliquée à de nombreuses formes d’antennes, à condition que la condition

$d > \frac{\lambda}{2\pi}$

soit remplie, c’est-à-dire que nous nous trouvions en dehors du champ proche réactif. Dans ce qui suit, nous examinerons d’où provient cette restriction et la valeur de $\qty{30}{\ohm}$ apparaissant dans la formule.


La formule approchée générale s’écrit :

$d = \frac{\sqrt{\frac{Z_0}{4\pi} \cdot P_{\textrm{EIRP}}}}{E}$


Ici, $Z_0$ désigne l’**impédance d’onde** de l’espace libre. Comme nous l’avons vu dans le chapitre précédent, celle-ci s’approche, à mesure que l’on s’éloigne de l’antenne, de la valeur du champ lointain

$Z_0 \approx \qty{120\pi}{\ohm} \approx \qty{377}{\ohm}$

(cf. figure [ref:a_feldwellenwiderstand]). En substituant cette valeur dans l’expression $\frac{Z_0}{4\pi}$, on obtient :

$\frac{Z_0}{4\pi} \approx \frac{\qty{120\pi}{\ohm}}{4\pi} = \qty{30}{\ohm}$


Cela donne la formule approchée connue de la classe E. Il devient également clair pourquoi elle ne doit pas être utilisée dans le champ proche réactif : dans cette zone, l’**impédance d’onde** n’est pas constante, mais dépend fortement de la distance, de la forme de l’antenne et de la **direction** considérée. Pour les calculs dans le champ proche réactif, c’est-à-dire pour des distances $d \le \frac{\lambda}{2\pi}$, des calculs plus détaillés, des simulations numériques ou des mesures sont généralement nécessaires.


<margin>
[image:1116:a_feldwellenwiderstand:Évolution de l’impédance d’onde dans les zones de champ proche et de champ lointain (échelle logarithmique).]
</margin>

Si la formule approchée du champ lointain est appliquée à une antenne dipôle déjà dans le champ proche rayonnant, la distance de sécurité calculée est généralement plus grande que nécessaire. Dans cette zone, l’**impédance d’onde** est inférieure à $\qty{377}{\ohm}$, alors que la formule approchée utilise la valeur plus élevée du champ lointain. Le résultat est donc conservateur et du côté de la sécurité. Cette méthode est acceptée par l’Agence fédérale des réseaux (Bundesnetzagentur).


Cela ne s’applique cependant pas aux antennes magnétiques et aux antennes très courtes électriquement. La figure [ref:a_feldwellenwiderstand] montre par exemple que l’**impédance d’onde** d’une antenne boucle magnétique peut être nettement supérieure à $\qty{377}{\ohm}$ dans le champ proche rayonnant. La formule approchée du champ lointain donnerait alors une distance de sécurité trop faible. C’est pourquoi il faut utiliser d’autres méthodes pour ces antennes, par exemple des programmes spécifiques de calcul du champ proche (simulations) ou des mesures.


[question:AK103]


Pour le calcul des distances de protection des personnes, la formule approchée connue peut être utilisée dans le champ lointain. Cela permet souvent d’éviter des mesures ou simulations complexes. Elle permet notamment, en fonctionnement portable, une estimation rapide de la distance de sécurité requise.