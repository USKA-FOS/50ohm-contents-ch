Pour calculer la distance de sécurité, il existe une formule approchée. Nous la trouvons dans le recueil de formules :

$ E = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{d} $

Celle-ci peut être rapidement réarrangée pour obtenir la distance de sécurité $d$ :

$ d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{E} $

Le recueil de formules contient également une note indiquant que la formule ci-dessus ne s'applique qu'aux calculs dans le champ lointain (ou champ proche rayonnant) pour $ d > \frac{\lambda}{2\pi} $

Cela est dû au fait que seule dans le champ lointain, les vecteurs de l'intensité de champ électrique ($E$) et de l'intensité de champ magnétique ($H$) présentent une relation de phase fixe et constante l'un par rapport à l'autre. Dans le champ proche réactif, en revanche, il peut y avoir localement des surélévations importantes tant du champ électrique que du champ magnétique. Ces effets ne peuvent pas être capturés de manière fiable avec les formules approchées pour le champ lointain. Pour les calculs dans le champ proche réactif, c'est-à-dire pour des distances $d \le \frac{\lambda}{2\pi}$, des simulations numériques sont donc généralement nécessaires. Sous certaines réserves (pas pour les antennes magnétiques, pas pour les antennes très courtes), les résultats sont également utilisables dans le champ proche rayonnant.

<indepth>
Le champ lointain d'une source de rayonnement est la zone dans laquelle les vecteurs de l'intensité de champ électrique ($E$) et de l'intensité de champ magnétique ($H$) sont perpendiculaires entre eux et ne présentent pas de différences de phase. 

La limite entre le champ lointain et le champ proche dépend principalement de la longueur d’onde. Selon les [explications sur la BEMFV](https://50ohm.de/ebemfv), le champ lointain se forme à une distance d'environ $4\cdot\lambda$. 

Le champ proche se divise en champ proche *réactif* et champ proche *rayonnant*. En pratique, dans le champ proche rayonnant, la formule pour le champ lointain peut également être utilisée. Cela est dû au fait que la formule approchée fournit ici des estimations très conservatrices, c'est-à-dire que les intensités de champ réelles sont inférieures à celles calculées. On est du bon côté. 
  
Avec la formule $ d > \frac{\lambda}{2\pi} $, nous nous assurons donc que nous sommes en dehors du *champ proche réactif*.
</indepth>

%TODO Applet basteln: https://www.leifiphysik.de/elektrizitaetslehre/elektromagnetische-wellen/versuche/dipolstrahlung-animation

Le fait suivant est visé par la question suivante :

[question:EK105]

Pour $\qty{3,5}{\mega\hertz}$, le champ lointain (champ proche rayonnant) ne commence qu'à $\qty{13,64}{\meter}$.

 $\begin{split} d &> \frac{\lambda}{2 \cdot \pi}\\ d &> \frac{\qty{85,7}{\meter}}{2 \cdot \pi}\\ d &> \qty{13,64}{\meter}\end{split}$
 
La distance de $\qty{3,65}{\meter}$ déterminée est clairement dans le champ proche réactif et est donc invalide. Au lieu de la formule approchée pour le champ lointain, une autre méthode doit être choisie. Les mesures des composantes des champs E et H, les simulations ou les calculs du champ proche sont envisageables.

Pour que la question suivante puisse être répondue, il faut calculer où commence le champ lointain (champ proche rayonnant) pour la bande de $\qty{160}{\meter}$ et de $\qty{80}{\meter}$.

[question:EK106]

Pour $\qty{160}{\meter}$ s'applique : $d > \frac{\qty{160}{\meter}}{2\pi} = \qty{25,5}{\meter}$
 
Pour $\qty{80}{\meter}$ s'applique : $d > \frac{\qty{80}{\meter}}{2\pi} = \qty{12,7}{\meter}$

Le calcul est invalide si la distance pour $\qty{160}{\meter}$ est inférieure à $\qty{25,5}{\meter}$ et pour $\qty{80}{\meter}$ inférieure à $\qty{12,7}{\meter}$.

%%%%

Dans la question suivante, une distance de sécurité correcte doit être calculée pour la première fois. 

[question:EK108]

Tout d'abord, nous devons calculer la puissance de rayonnement en $P_\textrm{EIRP}$. De plus, nous remarquons que le gain d'antenne est indiqué en $\unit{\dBd}$. À cet effet, nous utilisons à nouveau la formule du recueil de formules :

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{100}{W} \cdot 10^{\frac{\qty{7,5}{\dBd}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{653}{\watt}$

La somme des gains et des atténuations de l'ensemble du système d'antenne est le gain d'antenne de $\qty{7,5}{\dBd}$, moins l'atténuation du câble de $\qty{1,5}{\dB}$ et plus le gain de $\qty{2,15}{\dBi}$ pour le rayonnement isotrope (le gain d'antenne se réfère au dipôle).

En variante, comme dans les chapitres précédents, nous pouvons déterminer les facteurs respectifs pour les gains et l'atténuation.
$\qty{7,5}{\dB} - \qty{1,5}{dB} = \qty{6}{\dB}$, ce qui correspond à un facteur de $\num{4}$. Le facteur pour $\qty{2,15}{\dBi}$ est $\num{1,64}$.

$P_\textrm{EIRP} = \qty{100}{\watt} \cdot 4 \cdot 1,64 = \qty{656}{\watt}$

---

Les résultats des deux méthodes de calcul devraient être identiques. Cependant, ils diffèrent légèrement l'un de l'autre. C'est le résultat des arrondis des deux facteurs. Cependant, la puissance calculée de manière arrondie est suffisamment précise pour résoudre la question correctement. Nous utilisons donc cette valeur dans la formule de distance :

$ d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{E} = \frac{\sqrt{\qty{30}{\ohm}\cdot \qty{656}{\watt}}}{\qty{28}{\volt\per\meter}} \approx \qty{5}{\meter}  $

La distance de sécurité de $\qty{5}{\meter}$ a été déterminée avec la formule pour le champ lointain. Elle n'est donc valable que si elle se situe également dans le champ lointain (ou champ proche rayonnant). Cela peut être rapidement vérifié comme ci-dessus.

$\begin{split} d &> \frac{\lambda}{2\pi}\\ d &> \frac{\qty{10}{\meter}}{2\pi}\\ d &> \qty{1,6}{\meter} \end{split}$

La distance de sécurité calculée de $\qty{5}{\meter}$ est supérieure à $\qty{1,6}{\meter}$ et se situe clairement dans le champ lointain (ou champ proche rayonnant). Le calcul est donc valable. La bonne réponse est $\qty{5}{\meter}$.

<indepth>
Dans le tableau, un facteur de $\num{4}$ est indiqué pour $\qty{6}{\dB}$. Il s'agit d'une valeur arrondie et qui est en réalité de $\num{3,981071706}$. C'est pourquoi il y a une erreur d'arrondi.
</indepth>
