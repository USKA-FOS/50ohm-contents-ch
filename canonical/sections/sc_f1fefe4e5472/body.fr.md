% En cours de rédaction ! De quoi s'agit-il ici ???
% Je me suis tout inventé !

Dans le recueil de formules, on trouve sous le point 6.2, symboles de formule, constantes et tableaux, également la formule pour $Z_{F0}$ l'impédance de la ligne de l'espace libre (vide).
$Z_{F0} = \sqrt{\dfrac{\mu_0}{\varepsilon_0}}$

$\mu_0$ la constante de champ magnétique, $\varepsilon_0$ la permittivité du vide

L'**intensité de champ magnétique** mentionnée dans la question est calculée à l'aide de la constante de champ magnétique, de la densité de flux magnétique et de la magnétisation. La relation entre la permittivité du vide et l'**intensité de champ électrique** est nettement plus complexe.

Dans un milieu (par exemple, l'air), l'impédance de la ligne $Z_{F}$ dépend de $\mu$, la constante de champ magnétique et de $\varepsilon$, la permittivité du vide du milieu.

$Z_{F} = \sqrt{\dfrac{\mu}{\varepsilon}}$

Il existe une dépendance entre l'impédance de la ligne, l'intensité de champ électrique et l'intensité de champ magnétique. Ainsi, l'intensité de champ électrique et l'intensité de champ magnétique dépendent également de l'impédance de la ligne du milieu.


[question:AK102]

% Comment calculez-vous la puissance au point d'alimentation de l'antenne (puissance d'entrée de l'antenne) lorsque la puissance de sortie de l'émetteur est connue ?

La puissance au point d'alimentation de l'antenne résulte de la puissance de sortie de l'émetteur et de l'atténuation de la ligne d'alimentation. Chaque atténuation peut être convertie en un facteur d'atténuation. Par exemple, pour une atténuation de $\qty{10}{\dB}$, le facteur est $\num{0,1}$.
Le calcul est simple : $P_{Ant} = D \cdot P_{Sender}$ (D représente le facteur d'atténuation)

[question:AK104]
% En cours de rédaction !
 Dans le § 8, BEMFV, il est notamment stipulé que la distance de sécurité liée au lieu doit se situer dans la zone contrôlable. Souvent, cette distance est fixée par les conditions locales et ne peut pas être modifiée. Dans ces cas, la puissance d'émission maximale doit être adaptée.
 
La puissance rayonnée inclut, outre la puissance d'émission, le gain d'antenne en $\unit{\dBi}$. Les valeurs indiquées sont $\qty{6}{\dBd}$. Par rapport au rayonnement isotrope, cela donne $\qty{6}{\dBd} + \qty{2,15}{\dB}$. Ce qui donne un facteur de gain de $G_i = 4 \cdot 1,64 = 6,56$.

Maintenant, la puissance d'émission maximale peut être déterminée. Pour cela, la formule de l'intensité de champ dans le champ lointain d'une antenne doit être réarrangée :
 $\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E \cdot d &= \sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}\\ E^2 \cdot d^2 &= \qty{30}{\ohm}\cdot P_A\cdot G_i\\ \dfrac{E^2 \cdot d^2}{\qty{30}{\ohm}\cdot G_i} &= P_A\\ P_A &= \dfrac{E^2 \cdot d^2}{\qty{30}{\ohm}\cdot G_i}\\ P_A &= \qty{\dfrac{28^2 \cdot 5^2}{30 \cdot 6,56}}{\watt}\\ P_A &\approx \qty{99,59}{\watt}\end{split}$
La puissance d'émission doit être limitée à environ $\qty{100}{\watt}$.
  
  Juste pour être sûr, l'équation des unités. Le résultat a l'unité watt.
 $\begin{split} \unit{\watt} &= \dfrac{\left(\unit{\volt\per\meter}\right)^2 \cdot \unit{m\squared}}{\unit{\volt\per\ampere}}\\ \unit{\watt} &= \dfrac{\unit{\volt} \cdot \unit{\volt} \cdot \unit{m\squared} \cdot A}{\unit{\volt} \cdot \unit{m\squared}}\\ \unit{\watt} &= \unit{\volt} \cdot \unit{\ampere}\\ \unit{\watt} &= \unit{\watt}\end{split}$
 
 La formule pour l'intensité de champ ne s'applique qu'au champ lointain. Le fait que cela soit satisfait pour les $\qty{5}{\meter}$ donnés peut être rapidement vérifié.

$\begin{split}d &> \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{2,06}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,33}{\meter}\end{split}$
La distance de sécurité de $d=\qty{5}{\meter}$ est clairement dans le champ lointain.

[question:AK107]

Pour les trois questions suivantes, la procédure est plus ou moins la même.
Pour le calcul de l'intensité de champ électrique, la puissance au point d'alimentation de l'antenne, le facteur de gain et la distance sont nécessaires.

$P_A$, puissance au point d'alimentation : $\qty{250}{\watt}$ (pas de câble, alimentation directe)

$G_i$, facteur de gain : $\qty{12,15}{\dBi}$ ou $\qty{10}{\dBi}$ et $\qty{2,15}{\dBi}$, ce qui correspond aux facteurs $10 \cdot 1,64 = 16,4$

$d$, distance : $\qty{30}{\meter}$

La formule ne s'applique qu'au champ lointain. Cela peut être vérifié avec $d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{250}{\watt}\cdot 16,4}}{\qty{30}{\meter}}\\ E &\approx \qty{11,7}{\volt\per\meter}\end{split}$

[question:AK113]

$P_A$, puissance au point d'alimentation : $\qty{10}{\watt}$ (pas de câble, alimentation directe)

$G_i$, facteur de gain : $\qty{2,15}{\dBi}$, ce qui correspond au facteur $\num{1,64}$ (dipôle comme antenne)

$d$, distance : $\qty{10}{\meter}$

La formule ne s'applique qu'au champ lointain. Cela peut être vérifié avec $ d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{10}{\watt}\cdot 1,64}}{\qty{10}{\meter}}\\ E &\approx \qty{2,2}{\volt\per\meter}\end{split}$

[question:AK114]
% AK115 : Une station de radioamateur émet en FM avec une puissance rayonnée équivalente (ERP) de 100 W. Quelle est l'intensité de champ dans l'espace libre à une distance de 100 m ?

$P_A$, puissance au point d'alimentation : $\qty{100}{\watt}$ (puissance rayonnée en ERP)

$G_i$, facteur de gain : $\qty{2,15}{\dBi}$, ce qui correspond au facteur $\num{1,64}$ (puissance rayonnée en ERP, facteur pour EIRP)

$d$, distance : $\qty{100}{\meter}$

La formule ne s'applique qu'au champ lointain. Cela peut être vérifié avec $ d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{100}{\watt}\cdot 1,64}}{\qty{100}{\meter}}\\ E &\approx \qty{0,7}{\volt\per\meter}\end{split}$

[question:AK115]