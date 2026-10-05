La fonction de base de la diode est déjà connue du chapitre [sec:halbleiter] : elle ne laisse passer le courant que dans une seule direction, à savoir lorsque la tension appliquée à l'anode ($U_a$) est supérieure à la tension à la cathode ($U_k$), cf. figure [ref:e_diode_u_i].

<margin>
[picture:859:e_diode_u_i:Tensions et courant sur une diode avec résistance en série]
</margin>

Mathématiquement, nous pouvons écrire cette condition ainsi :

$U_d = U_a - U_k > 0$

Cependant, si $U_d$ est seulement un tout petit peu supérieur à 0, aucun courant perceptible ne circule encore. Dès que $U_d$ dépasse une tension de seuil, un courant important circule. Cette tension de seuil dépend de la construction de la diode et est aussi appelée tension directe, car lorsqu'elle est dépassée, le courant circule vraiment beaucoup. Cela est dû à la *caractéristique exponentielle* d'une diode.

<margin>
[picture:861:e_diode_kennlinie_iu:Caractéristique d'une diode]
</margin>

<indepth>
Le courant de la diode est donné par une équation exponentielle. Elle est dite "exponentielle" car la variable indépendante $U_d$ se trouve dans l'exposant, c'est-à-dire la "puissance".

$I_d = I_S \left(e^{\frac{U_d}{U_T}}-1\right)$

$e$ est le nombre dit d'Euler ($e\approx 2,718$), $U_T$ une constante qui vaut environ $\qty{26}{\milli\volt}$ à température ambiante.

$I_S$ est ici le *courant de saturation inverse*, c'est le très faible courant qui traverse la diode pour des tensions négatives. La valeur de $I_S$ dépend, outre quelques paramètres de la diode comme la surface de la diode, surtout du matériau semi-conducteur utilisé. Pour des matériaux comme le germanium (Ge) avec une faible *largeur de bande interdite* (nous y reviendrons plus en détail dans la section [sec:diode_2]), $I_S$ est plus grand ; pour des matériaux avec une largeur de bande interdite plus grande, $I_S$ est plus petit.
</indepth>

[question:EC501]

En considérant une caractéristique de diode dans la figure [ref:e_diode_kennlinie_iu], le courant de la diode augmente fortement pour des $U_d$ positifs à partir d'une certaine tension. Cette tension est aussi appelée *tension de seuil* $U_{th}$, mais elle n'est que l'expression des différents $I_S$ : plus $I_S$ est petit, plus la tension de seuil est élevée.

Comme points de repère pour la tension de seuil des diodes, nous pouvons indiquer pour le germanium (Ge) environ $\qtyrange{0,2}{0,3}{\volt}$ et pour le silicium (Si) environ $\qtyrange{0,6}{0,7}{\volt}$.

<attention>
La tension de seuil $U_{th}$ est aussi appelée *tension directe*, car ce n'est qu'à partir de cette tension que le courant commence à circuler de manière marquée.
</attention>

%<margin>
%*Analogie d'un canal d'eau pour une diode :*
%
%Une vanne à clapet à bille avec ressort bloque tant que la force d'écoulement $F_{\text{Strom}}$ est inférieure %à la force du ressort $F_{\text{Feder}}$ (en haut) ; si elle dépasse la force de seuil, la bille se soulève et %le canal devient conducteur (en bas) – analogue au comportement d'une diode au-dessus de sa tension de seuil $U_S$.
%[picture:10102:e_diode_wasserkanal_analogie:Analogie_canal_eau]
%</margin>
% commenté car le texte est déformé.

Les *diodes électroluminescentes* (LEDs) sont des diodes spéciales dont le matériau semi-conducteur est conçu pour émettre de la lumière lorsque la diode est polarisée en sens direct. Cela n'est possible qu'avec certains matériaux - pas avec Si et Ge. La couleur de la lumière est déterminée par la largeur de bande interdite. Plus la largeur de bande interdite est grande, plus la lumière est courte en longueur d'onde, plus le courant de saturation inverse est faible, et donc plus la tension de seuil est élevée. Ainsi, les LEDs rouges ont environ $\qty{1,7}{\volt}$ de tension de seuil et les LEDs vertes $\qty{2,5}{\volt}$. Les différentes caractéristiques sont représentées dans la figure [ref:e_diode_kennlinien].

[question:EC513]
[question:EC510]
[question:EC509]
[question:EC511]
[question:EC512]

---

<margin>
[picture:858:e_diode_kennlinien:Caractéristiques de différentes diodes]
</margin>


[question:EC503]
[question:EC506]
[question:EC507]
[question:EC508]

Puisque les LEDs sont utilisées en sens direct, il est important de placer une résistance $R_V$ entre la source de tension $U$ et la LED. $R_V$ règle le courant souhaité $I$. La tension de seuil $U_{th}$ de la LED doit être prise en compte :

$ I=\frac{U-U_{th}}{R_V}$

[question:EC514]
[question:EC515]
[question:EC516]

---

Dans notre modèle simple, pour des $U_d$ négatifs, seul un faible courant inverse circule. Ce n'est cependant pas vrai pour des tensions très négatives. À un moment donné, le champ électrique à travers la couche de blocage devient trop élevé et la diode "perce", le courant en sens inverse augmente extrêmement fortement, comme le montre la figure [ref:n_diode_kennlinie_uz].

Cette *percée inverse* peut avoir différentes causes physiques que nous ne pouvons pas traiter en détail ici. La tension à laquelle cette percée se produit est communément appelée *tension Zener* $U_z$, même si l'effet Zener (un effet tunnel quantique) n'est qu'un mécanisme de percée possible. Les *diodes Zener* sont utilisées pour la stabilisation de tension. Il est alors important de limiter le courant de percée par une résistance en série.

<margin>
[picture:862:n_diode_kennlinie_uz:Caractéristique d'une diode Z]
</margin>

---

Le symbole électrique d'une diode Zener (figure [ref:e_zener_symbol]) est celui d'une diode régulière, où le trait de la cathode a un prolongement supplémentaire à $\qty{90}{\degree}$. Cela doit rappeler le "cassement" de la caractéristique lors de la percée.

<margin>
[picture:860:e_zener_symbol:Symbole électrique d'une diode Zener]
</margin>



[question:EC517]
[question:EC520]
[question:EC521]
[question:EC522]

Les diodes traitées jusqu'à présent étaient des diodes dont la propriété de diode provient d'une jonction semi-conductrice, qui ne sera abordée qu'en [sec:diode_2]. La *diode Schottky* est une diode dont les propriétés proviennent d'une jonction métal-semi-conducteur. La tension de seuil est environ deux fois plus petite que celle d'une diode à semi-conducteur classique du même matériau, ou plus petite, selon la conception exacte de la jonction métal-semi-conducteur. Les diodes Schottky sont utilisées lorsque la tension de seuil doit être faible, ou comme diodes de commutation très rapides.

[question:EC504]
[question:EC505]

<margin>
Les diodes métal-semi-conducteur sont les plus anciens éléments redresseurs à base de semi-conducteurs. Ferdinand Braun a découvert leur effet redresseur dès 1874, sans pouvoir expliquer son observation.
</margin>

Résumons :

Les diodes ne laissent passer le courant que dans une seule direction. Elles conviennent donc au redressement du courant alternatif.

Cependant, pour des tensions inverses élevées ($U_d < U_z$), le courant en sens inverse augmente fortement. Ce point de fonctionnement peut être très bien utilisé pour la stabilisation de tension (*diode Zener*).

Par ailleurs, en polarisation inverse, elles peuvent aussi être utilisées comme capacités commandées en tension, mais nous ne traiterons cela que dans la section [sec:oszillator_vco].

[question:EC502]
[question:EC518]
[question:EC519]
