Outre les accumulateurs au plomb (Pb) et les accumulateurs nickel-métal-hydrure (NiMH) bien connus, nous utilisons de plus en plus dans la technique radio, par exemple pour les opérations portables, des accumulateurs lithium-fer-phosphate (LiFePO₄). Commençons par examiner un accumulateur et ses inscriptions dans l'illustration [ref:a_akku_lifepo4].


<margin>
[photo:175:a_akku_lifepo4:LiFePO4]
</margin>

<indepth>
* Capacité : $\qty{4200}{\milli\ampere\hour}$
* Tension : 4S1P / $\qty{13,2}{\volt}$
% * Décharge : 30C Constant / 40C Burst
% * Connecteur d'équilibrage : JST-XH
% * Connecteur de décharge : $\qty{5.5}{\milli\meter}$ connecteur à bille

Les caractéristiques les plus importantes pour nous sont la tension nominale de $\qty{13,2}{\volt}$ et le montage 4S1P. Cela signifie que la tension nominale de $\qty{13,2}{\volt}$ résulte de 4 cellules montées en série et 1 fois en parallèle, donc toutes les 4 en série. En général, les LiFePO₄ ont une tension nominale par cellule de $\qty{3,2}{\volt}$ à $\qty{3,3}{\volt}$. Ainsi, on obtient $\qty{3,3}{\volt} \cdot 4 = \qty{13,2}{\volt} \cdot 1 = \qty{13,2}{\volt}$.


Dans un montage 4S2P, il y a au total 8 cellules. 4 en série et 2 fois en parallèle. Cela donnerait alors une tension de $\qty{13,2}{\volt}$, mais une capacité de $\qty{8400}{\milli\ampere\hour}$.

</indepth>


Dans l'exemple d'accumulateur, une capacité nominale de $\qty{4200}{\milli\ampere\hour}$ est indiquée. La capacité nominale $Q$ de l'accumulateur est aussi appelée charge et est exprimée en $\unit{\ampere\hour}$ ou $\unit{\milli\ampere\hour}$.


Pour notre accumulateur exemple, cela correspond à $\qty{4,2}{\ampere\hour}$. Cela signifierait théoriquement que nous pouvons alimenter notre accumulateur pendant $\qty{1}{\hour}$ avec $\qty{4,2}{\ampere}$, ou pendant $\qty{2}{\hour}$ avec $\qty{2,1}{\ampere}$, etc. Cela est décrit par la formule :


$t=\frac{Q}{I}$


$t=\frac{\qty{4,2}{\ampere\hour}}{\qty{4,2}{\ampere}} = \qty{1}{\hour}$


[question:AB210]


Nous voulons maintenant aussi savoir quelle quantité d'énergie électrique est stockée dans l'accumulateur. L'énergie ($\unit{\watt\hour}$) est la charge $Q$ ($\unit{\ampere\hour}$) de l'accumulateur multipliée par la tension totale $U$ en volts.


$\qty{1}{\watt\hour} = \qty{1}{\ampere\hour} \cdot \qty{1}{\volt}$


Pour notre exemple, nous calculons $\qty{4,2}{\ampere\hour} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\hour}$ comme énergie stockée.


[question:AB501]


%La décharge de cet accumulateur peut se faire avec un courant de décharge constant de "30 C". Cela signifie que l'accumulateur peut être déchargé avec 30 fois la capacité $Q$.
%
%Débit de décharge : $I = 30 \cdot \qty{4200}{\milli\ampere} = \qty{126}{\ampere}$
%
%Ceci n'est qu'une valeur théoriquement possible, car notre accumulateur serait ainsi déchargé en $\qty{108}{\second}$. La section du câble doit également être prise en compte.
%

Dans un montage en série (ou en chaîne) d'accumulateurs, comme dans l'illustration [ref:a_akku_4S1P], les tensions s'additionnent et la capacité reste identique. Dans un montage en parallèle, comme dans l'illustration [ref:a_akku_4S2P], la tension reste identique et les capacités s'additionnent.


<margin>
% TODO Image du montage en série disponible chez DG1HXJ sous forme .tex
[photo:176:a_akku_4S1P:Montage en série]
</margin>

<margin>
% TODO Image du montage en parallèle disponible chez DG1HXJ sous forme .tex
[photo:177:a_akku_4S2P:Montage en parallèle]
</margin>

<attention>
Lors de l'utilisation d'un LiFePO₄ monté en 4S1P, notez que des tensions comprises entre $\qty{10}{\volt}$ et $\qty{14,4}{\volt}$ peuvent être présentes. Tous les appareils radio ne peuvent pas fonctionner avec ces tensions. Il est également important de ne connecter que des cellules/accumulateurs ayant les mêmes caractéristiques, car les cellules s'influencent mutuellement et pourraient sinon être endommagées. En particulier avec les accumulateurs lithium actuels, il est judicieux d'installer un dispositif de surveillance (équilibreur, moniteur de batterie). Celui-ci assure, entre autres, l'équilibrage nécessaire des tensions de cellule et une charge optimale.
</attention>

---


% Dans l'illustration [ref:a_akku_lifepo4_anschluss]
% TODO Image de l'encadré "Connexions de l'accumulateur" disponible chez DG1HXJ sous forme .tex
%<margin>
%[photo:178:a_akku_lifepo4_anschluss:Connexions LiFePO4]
%</margin>

Pour résoudre la question suivante, il faut savoir que la tension totale correspond à la somme des tensions des cellules. La charge totale correspond, en revanche, à la charge d'une cellule.


[question:AB209]


Pour la question suivante, il faut d'abord déterminer la quantité de charge extractible de $\qty{90}{\percent}$.
La durée de décharge $t$ est donnée par : $t=\frac{Q}{I}$


[question:AB211]