On connaît déjà la fonction de base de la diode à partir du chapitre [sec:halbleiter] : elle ne laisse passer le courant que dans un seul sens, à savoir lorsque la tension appliquée à l'anode ($U_a$) est supérieure à la tension appliquée à la cathode ($U_k$), cf. figure [ref:e_diode_u_i].

<margin>
[picture:859:e_diode_u_i:Tensions et courant aux bornes d'une diode avec résistance en série]
</margin>

Mathématiquement, nous pouvons exprimer cette condition de la manière suivante :

$U_d = U_a - U_k > 0$

Toutefois, si $U_d$ n'est que légèrement supérieure à 0, aucun courant notable ne circule. Cela s'explique par la *caractéristique exponentielle* d'une diode. En effet, le courant traversant la diode est donné par :

$I_d = I_S \left(e^{\frac{U_d}{U_T}}-1\right)$

$e$ est le nombre d'Euler ($e\approx 2,718$), $U_T$ une constante qui, à température ambiante, vaut environ $\qty{26}{\milli\volt}$.

$I_S$ représente ici le *courant de saturation inverse*, c'est-à-dire le très faible courant qui traverse la diode en polarisation inverse. La valeur de $I_S$ dépend, entre autres paramètres de la diode comme la surface de la jonction, principalement du matériau semi-conducteur utilisé. Pour des matériaux comme le germanium (Ge) doté d'une faible *bande interdite* (ce point sera abordé plus en détail dans la formation HB9 au chapitre [sec:diode_2]), $I_S$ est plus élevé, tandis que pour des matériaux à bande interdite plus large, $I_S$ est plus faible.

<margin>
[picture:861:e_diode_kennlinie_iu:Caractéristique courant-tension d'une diode]
</margin>

[question:EC501]

Si l'on examine la caractéristique d'une diode représentée sur la figure [ref:e_diode_kennlinie_iu], on constate que le courant traversant la diode augmente fortement à partir d'une certaine tension positive $U_d$. Cette tension est appelée *tension de seuil* $U_{th}$, mais elle n'est qu'une manifestation des différences de $I_S$ : plus $I_S$ est faible, plus la tension de seuil est élevée.

À titre indicatif, pour les diodes à jonction pn, on peut considérer une tension de seuil d'environ $\qtyrange{0,2}{0,3}{\volt}$ pour le Ge et d'environ $\qtyrange{0,6}{0,7}{\volt}$ pour le Si.

<attention>
La tension de seuil $U_{th}$ est aussi appelée *tension directe*, car c'est seulement à partir de cette tension que le courant commence à circuler de manière significative.
</attention>

Les *diodes électroluminescentes* (LED) sont également des diodes à jonction pn, mais leur matériau semi-conducteur est conçu pour émettre de la lumière lorsqu'elles sont polarisées en direct. Cela n'est possible qu'avec certains matériaux — pas avec le Si ou le Ge. La couleur de la lumière émise dépend de la bande interdite : plus celle-ci est large, plus la lumière est de courte longueur d'onde, plus le courant de saturation inverse est faible, et donc plus la tension de seuil est élevée. Ainsi, les LED rouges ont une tension de seuil d'environ $\qty{1,7}{\volt}$, tandis que les LED vertes en ont une d'environ $\qty{2,5}{\volt}$. Les différentes caractéristiques sont représentées sur la figure [ref:e_diode_kennlinien].

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

Comme les LED fonctionnent en polarisation directe, il est important de placer une résistance $R_V$ entre la source de tension $U$ et la LED. $R_V$ permet de régler le courant souhaité $I$. Il faut alors tenir compte de la tension de seuil $U_{th}$ de la LED :

$ I=\frac{U-U_{th}}{R_V}$

[question:EC514]
[question:EC515]
[question:EC516]

---

Dans notre modèle simple, seul un faible courant inverse circule pour des valeurs négatives de $U_d$. Cependant, cela ne reste vrai que jusqu'à une certaine limite. En effet, si la tension négative devient trop élevée, le champ électrique dans la zone de déplétion entre les régions n et p devient si intense que la diode entre en *claquage*, et le courant en polarisation inverse augmente alors fortement, comme illustré sur la figure [ref:n_diode_kennlinie_uz].

Ce *claquage* peut avoir différentes causes physiques, que nous n'aborderons pas en détail ici. La tension à laquelle ce claquage se produit est généralement appelée *tension Zener* $U_z$, même si l'effet Zener (un effet tunnel quantique) n'est qu'un des mécanismes possibles de claquage. Les *diodes Zener* sont utilisées pour la stabilisation de tension. Il est alors important de limiter le courant de claquage à l'aide d'une résistance en série.

<margin>
[picture:862:n_diode_kennlinie_uz:Caractéristique d'une diode Zener]
</margin>

---

Le symbole électrique d'une diode Zener (figure [ref:e_zener_symbol]) est celui d'une diode classique, mais avec une extension à $\qty{90}{\degree}$ sur le trait de la cathode. Cela rappelle le "coudage" de la caractéristique en régime de claquage.

<margin>
[picture:860:e_zener_symbol:Symbole électrique d'une diode Zener]
</margin>

[question:EC517]
[question:EC520]
[question:EC521]
[question:EC522]

Jusqu'à présent, nous n'avons traité que les *diodes à jonction pn*, dont les propriétés découlent d'une jonction semi-conductrice. La *diode Schottky* est une diode dont les propriétés proviennent d'une jonction métal-semi-conducteur. Sa tension de seuil est environ deux fois plus faible que celle d'une diode à jonction pn du même matériau, voire encore plus faible selon la conception exacte de la jonction métal-semi-conducteur. Les diodes Schottky sont utilisées lorsque l'on souhaite une faible tension de seuil ou lorsque l'on a besoin de diodes de commutation très rapides.

[question:EC504]
[question:EC505]

<margin>
Les diodes à jonction métal-semi-conducteur sont les premiers dispositifs redresseurs à semi-conducteurs. Ferdinand Braun a découvert leur effet redresseur dès 1874, sans pour autant pouvoir l'expliquer.
</margin>

Pour résumer :

Les diodes ne laissent passer le courant que dans un seul sens. Elles sont donc adaptées au redressement du courant alternatif.

Cependant, à des tensions inverses élevées ($U_d < U_z$), le courant en polarisation inverse augmente fortement. Ce point de fonctionnement peut être exploité pour la stabilisation de tension (*diode Zener*).

Par ailleurs, en polarisation inverse, elles peuvent aussi servir de condensateurs commandés par la tension — un sujet que nous aborderons uniquement dans la formation de classe A.