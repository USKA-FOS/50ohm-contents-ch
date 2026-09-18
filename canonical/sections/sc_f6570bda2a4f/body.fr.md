Pour calculer la distance de sécurité, il existe une formule approximative. On la trouve dans le [recueil de formules](#) :

$ E = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}}{d} $


On peut facilement réarranger cette formule pour obtenir la distance de sécurité $d$ :


$ d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}}{E} $


Le recueil de formules contient une remarque indiquant que la formule ci-dessus n'est valable que pour les calculs en champ lointain (ou champ proche rayonnant) à partir de $ d > \frac{\lambda}{2\pi} $.


Cela s'explique par le fait que, dans le champ lointain, les champs électrique et magnétique présentent une relation de phase fixe et constante entre eux. En revanche, dans le champ proche réactif, il peut y avoir localement des augmentations importantes des champs électrique et magnétique. Ces effets ne peuvent pas être correctement pris en compte avec les formules approximatives du champ lointain. Pour les calculs en champ proche réactif, c'est-à-dire pour des distances $d \le \frac{\lambda}{2\pi}$, il est généralement nécessaire de recourir à des simulations numériques, par exemple avec [EZNEC](https://www.eznec.com/) ou [Grasp/TICRA Student-Edition](https://www.ticra.com/software/ticra-tools-student-edition/). La manipulation de simulateurs numériques n'est pas requise pour l'examen, mais elle peut être utile en pratique pour évaluer les antennes. Avec certaines restrictions (pas pour les antennes magnétiques, pas pour les antennes très courtes), les résultats sont également utilisables dans le champ proche rayonnant.


<indepth>
Le champ lointain d'une source de rayonnement est la zone où les vecteurs de l'intensité de champ électrique ($E$), de l'intensité de champ magnétique ($H$) sont perpendiculaires entre eux et ne présentent pas de déphasage.


La limite entre le champ lointain et le champ proche dépend principalement de la longueur d’onde. Des informations sur le calcul de l'intensité de champ se trouvent dans la [fiche de formules pour la déclaration d'émission pour les installations radioamateurs](https://uska.ch/wp-content/uploads/2016/06/Formelblatt_d_08-02-21.pdf).


Des informations détaillées sur la création d'une déclaration d'émission concrète sont disponibles auprès de l'USKA sous [**Calcul des émissions**](https://uska.ch/emissions-berechnung/) et la procédure est décrite dans le document [Guide pour la déclaration d'émission pour les installations radioamateurs](https://uska.ch/wp-content/uploads/2016/06/Wegleitung_d_08-03-02_Rev_A-1.pdf).


Le champ proche se divise en *champ proche réactif* et *champ proche rayonnant*. En pratique, il est possible d'utiliser la formule du champ lointain dans le champ proche rayonnant. Cela s'explique par le fait que la formule approximative fournit ici des estimations très conservatrices, c'est-à-dire que les intensités de champ réelles sont inférieures aux valeurs calculées. On se place ainsi du côté de la sécurité.

Avec la formule $ d > \frac{\lambda}{2\pi} $, nous nous assurons donc d'être en dehors du *champ proche réactif*.
</indepth>


%TODO Applet à créer : https://www.leifiphysik.de/elektrizitaetslehre/elektromagnetische-wellen/versuche/dipolstrahlung-animation


<tip>
La déclaration d'émission ne doit pas être soumise ; elle doit cependant pouvoir être présentée si nécessaire, par exemple en cas de perturbations causées.
</tip>

Cette situation est illustrée par la question suivante :


[question:EK105]


Pour $\qty{3,5}{\mega\hertz}$, le champ lointain (champ proche rayonnant) ne commence qu'à $\qty{13,64}{\meter}$.

$\begin{split} d &> \frac{\lambda}{2 \cdot \pi}\\ d &> \frac{\qty{85,7}{\meter}}{2 \cdot \pi}\\ d &> \qty{13,64}{\meter}\end{split}$


La distance de $\qty{3,65}{\meter}$ déterminée se situe clairement dans le champ proche réactif et est donc invalide. Au lieu de la formule approximative du champ lointain, une autre méthode doit être choisie. Les options possibles sont des mesures des composantes de champ E et H, des simulations ou des calculs de champ proche.


Pour pouvoir répondre à la question suivante, il faut calculer à partir de quelle distance commence le champ lointain (champ proche rayonnant) pour la bande $\qty{160}{\meter}$ et $\qty{80}{\meter}$.

[question:EK106]


Pour $\qty{160}{\meter}$, on a : $d > \frac{\qty{160}{\meter}}{2\pi} = \qty{25,5}{\meter}$


Pour $\qty{80}{\meter}$, on a : $d > \frac{\qty{80}{\meter}}{2\pi} = \qty{12,7}{\meter}$


Le calcul est invalide si la distance pour $\qty{160}{\meter}$ est inférieure à $\qty{25,5}{\meter}$ et pour $\qty{80}{\meter}$ inférieure à $\qty{12,7}{\meter}$.


%%%%

Dans la question suivante, il faut maintenant calculer pour la première fois une distance de sécurité réelle.


[question:EK108]


Tout d'abord, nous devons calculer la puissance rayonnée $P_\text{EIRP}$. De plus, nous remarquons que le gain d'antenne est indiqué en $\unit{\dBd}$. Pour cela, nous utilisons à nouveau la formule du recueil de formules :


$P_\text{EIRP} = P_\text{émetteur} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{100}{\watt} \cdot 10^{\frac{\qty{7,5}{\dBd}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{653}{\watt}$


La somme des gains et atténuations de l'ensemble du système d'antenne correspond au gain d'antenne de $\qty{7,5}{\dBd}$, moins l'atténuation du câble de $\qty{1,5}{\dB}$ et plus le gain de $\qty{2,15}{\dBi}$ pour le radiateur isotrope (le gain d'antenne se réfère au dipôle).


Alternativement, comme dans les chapitres précédents, nous pouvons déterminer les facteurs respectifs pour les gains et les atténuations.
$\qty{7,5}{\dB} - \qty{1,5}{\dB} = \qty{6}{\dB}$, ce qui correspond à un facteur de $\num{4}$. Le facteur pour $\qty{2,15}{\dBi}$ est $\num{1,64}$.

$P_\text{EIRP} = \qty{100}{\watt} \cdot 4 \cdot 1,64 = \qty{656}{\watt}$


---

Les résultats des deux méthodes de calcul devraient en principe être identiques. Cependant, ils diffèrent légèrement en raison d'arrondis lors du calcul des facteurs. La puissance calculée de manière arrondie est cependant suffisamment précise pour résoudre correctement la question. Nous insérons donc cette valeur dans la formule de distance :


$ d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}}{E} = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{656}{\watt}}}{\qty{28}{\volt\per\meter}} \approx \qty{5}{\meter} $


La distance de sécurité de $\qty{5}{\meter}$ a été déterminée à l'aide de la formule du champ lointain. Elle n'est donc valable que si elle se situe également dans le champ lointain (ou champ proche rayonnant). Cela peut être vérifié rapidement comme suit :


$\begin{split} d &> \frac{\lambda}{2\pi}\\ d &> \frac{\qty{10}{\meter}}{2\pi}\\ d &> \qty{1,6}{\meter} \end{split}$


La distance de sécurité calculée de $\qty{5}{\meter}$ est supérieure à $\qty{1,6}{\meter}$ et se situe donc clairement dans le champ lointain (ou champ proche rayonnant). Le calcul est donc valable. La bonne réponse est $\qty{5}{\meter}$.


<indepth>
Dans le tableau [sec:dezibel_1], un facteur de $\num{4}$ est indiqué pour $\qty{6}{\dB}$. Il s'agit d'une valeur arrondie et vaut en réalité $\num{3,981071706}$. C'est pourquoi il y a une erreur d'arrondi.
</indepth>