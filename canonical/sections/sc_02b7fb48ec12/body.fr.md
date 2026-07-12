Outre les accumulateurs au plomb (Pb) et les accumulateurs nickel-métal hydrure (NiMH) connus, nous utilisons de plus en plus dans la technique radio, par exemple lors du fonctionnement portable, des accumulateurs lithium fer phosphate (LiFePO4). Examinons d'abord un accumulateur et ses inscriptions dans la figure [ref:a_akku_lifepo4].

<margin>
[photo:175:a_akku_lifepo4:LiFePO4]
</margin>

<indepth>
* Capacité : $\qty{4200}{\milli\ampere\hour}$
* Tension : 4S1P / $\qty{13,2}{\volt}$
% * Décharge : 30C Constant / 40C Burst
% * Connecteur d'équilibrage : JST-XH
% * Connecteur de décharge : $\qty{5.5}{\milli\meter}$ Connecteur à bille

Les données les plus importantes pour nous sont la tension nominale de $\qty{13,2}{\volt}$ et le circuit 4S1P. Cela signifie que la tension nominale de $\qty{13,2}{\volt}$ est composée de 4 en série et 1 fois en parallèle, donc toutes les 4 sont connectées en série. Habituellement, les LiFePO4 ont une tension nominale de cellule de $\qty{3,2}{\volt}$ à $\qty{3,3}{\volt}$. Et ainsi, on obtient $\qty{3,3}{\volt} \cdot 4 = \qty{13,2}{\volt} \cdot 1 = \qty{13,2}{\volt}$.

Dans le cas d'un 4S2P, 8 cellules sont installées au total. 4 en série et 2 fois en parallèle. Cela donnerait une tension de $\qty{13,2}{\volt}$ mais une capacité de $\qty{8400}{\milli\ampere\hour}$.

</indepth>

Dans le cas de l'accumulateur exemple, $\qty{4200}{\milli\ampere\hour}$ sont indiqués comme capacité nominale. La capacité nominale de l'accumulateur $Q$ est également appelée charge et est indiquée en $\unit{\ampere\hour}$ ou $\unit{\milli\ampere\hour}$.

Pour notre accumulateur exemple, cela correspond à $\qty{4,2}{\ampere\hour}$. Cela signifierait théoriquement que nous pouvons charger notre accumulateur pendant $\qty{1}{\hour}$ avec $\qty{4,2}{\ampere}$ ou $\qty{2}{\hour}$ avec $\qty{2,1}{\ampere}$ etc. Cela est décrit par la formule :

$t=\frac{Q}{I}$

$t=\frac{\qty{4,2}{\ampere\hour}}{\qty{4,2}{\ampere}} = \qty{1}{\hour}$

[question:AB210]

Nous voulons maintenant également savoir quelle est la quantité d'énergie électrique stockée dans l'accumulateur. L'énergie ($\unit{\watt\hour}$) est la charge $Q$ ($\unit{\ampere\hour}$) de l'accumulateur multipliée par la tension totale $U$ en volts.

$\qty{1}{\watt\hour} = \qty{1}{\ampere\hour} \cdot \qty{1}{\volt}$

Pour notre exemple, nous calculons $\qty{4,2}{\ampere\hour} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\hour}$ comme énergie stockée.

[question:AB501]

%Décharge de cet accumulateur peut se faire avec un courant de décharge constant de "30 C". Cela signifie que l'accumulateur peut être déchargé avec 30 $\cdot$ capacité $Q$.
%
%Courant de décharge final : $I = 30 \cdot \qty{4200}{\milli\ampere} = \qty{126}{\ampere}$
%
%Il s'agit toutefois d'une valeur théoriquement possible, car notre accumulateur serait ainsi déchargé en $\qty{108}{\second}$. La section transversale des câbles doit également être prise en compte.
%

Dans le cas d'un circuit en série ou en série d'accumulateurs, comme dans la figure [ref:a_akku_4S1P], les tensions s'additionnent et la capacité reste la même. 
Dans le cas d'un circuit en parallèle comme dans la figure [ref:a_akku_4S2P], la tension reste la même et les capacités s'additionnent. 

<margin>
% TODO Bild Reihenschaltung liegt bei DG1HXJ als .tex
[photo:176:a_akku_4S1P:Circuit en série]
</margin>

<margin>
% TODO Bild Parallelschaltung liegt bei DG1HXJ als .tex
[photo:177:a_akku_4S2P:Circuit en parallèle]
</margin>

<attention>
Remarquez que lors de l'utilisation d'un LiFePO4 en circuit 4S1P, des tensions comprises entre $\qty{10}{\volt}$ et $\qty{14,4}{\volt}$ peuvent être présentes. Tous les appareils radio ne peuvent pas fonctionner avec ces tensions. Il est également important de ne connecter que des cellules/accumulateurs avec les mêmes données, car les cellules s'influencent mutuellement et peuvent sinon être endommagées. En particulier avec les accumulateurs lithium actuels, il est judicieux d'installer un dispositif de surveillance (équilibreur, moniteur de batterie). Celui-ci assure, entre autres, l'équilibrage nécessaire des tensions des cellules et une charge optimale.
</attention>

---


% In der Abb. [ref:a_akku_lifepo4_anschluss]
% TODO Bild Infobox Anschluss Akku liegt bei DG1HXJ als .tex
%<margin>
%[photo:178:a_akku_lifepo4_anschluss:LiFePO4 Anschlüsse]
%</margin>

Pour résoudre la question suivante, il faut savoir que la tension totale correspond à la somme des tensions des cellules. La charge totale correspond quant à elle à la charge d'une cellule.

[question:AB209]

Pour la question suivante, il faut d'abord déterminer la quantité de charge prélevable de $\qty{90}{\percent}$.
Le temps de décharge $t$ résulte de : $t=\frac{Q}{I}$

[question:AB211]
