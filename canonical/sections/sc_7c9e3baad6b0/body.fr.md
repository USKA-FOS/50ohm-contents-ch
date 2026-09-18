Nous avons déjà abordé le concept de puissance comme produit de l'intensité du courant et de la tension ($P = U \cdot I$). Nous approfondissons ici ce sujet en nous penchant notamment sur la manipulation des formules.

---

Pour cela, examinons le circuit illustré dans la figure [ref:e_leistung_r]. Il montre comment une résistance convertit la puissance électrique en chaleur. Si les grandeurs $P$ et $R$ sont connues, on peut déterminer la tension $U$ à l'aide de la formule de puissance ($P = U \cdot I$) et de la loi d'Ohm ($U = R \cdot I$).

<margin>
[picture:1013:e_leistung_r:La puissance est convertie en chaleur dans la résistance $R$]
</margin>

---

<tip>
Les formules dérivées sont également disponibles de manière claire dans le [recueil de formules de l'OFCOM](https://www.bakom.admin.ch/dam/de/sd-web/ooOLDCmCmEmX/formelsammlung.pdf).
</tip>

Commençons par réarranger l'équation de la loi d'Ohm pour exprimer l'intensité du courant :

$\begin{align*} U &= R \cdot I &\quad\quad\quad &|~: R\\ \frac{U}{R} &= \frac{\cancel{R} \cdot I}{\cancel{R}}\\[1.5ex] I &= \frac{U}{R}.\end{align*}$

En substituant cette expression de $I$ dans la formule de puissance, on obtient :

$\begin{split} P &= U \cdot \frac{U}{R}\\P&=\frac{U^2}{R}.\end{split}$

Résolvons cette équation pour $U^2$ en multipliant les deux côtés par $R$ :

$\begin{align*} P &= \frac{U^2}{R} &\quad\quad\quad &|~\cdot R\\ U^2 &= P \cdot R.\end{align*}$

Pour déterminer la tension $U$, appliquons l'opération inverse de l'élévation au carré, c'est-à-dire l'extraction de la racine carrée. On obtient ainsi :

$\begin{align*} U^2 &= P \cdot R &\quad\quad\quad &|~\sqrt{~~}\\ U &= \sqrt{P \cdot R}.\end{align*}$

Dans certaines questions d'examen, il est important de reconnaître les bonnes relations. À l'aide du recueil de formules, on peut toujours en déduire la solution correcte.

[question:EB504]

On peut également établir la relation entre l'intensité du courant $I$, la résistance $R$ et la puissance $P$ en substituant la loi d'Ohm dans la formule de puissance.

Partons des deux équations $P = U \cdot I$ et $U = R \cdot I$. En substituant la deuxième équation dans la première pour $U$, on obtient :

$\begin{split} P &= R \cdot I \cdot I\\ P &= I^2 \cdot R.\end{split}$

Résolvons pour $I^2$ en divisant les deux côtés par $R$ :

$\begin{align*} P &= I^2 \cdot R &\quad\quad\quad &|~:~R\\ I^2 &= \frac{P}{R}.\end{align*}$

Enfin, extrayons la racine carrée :

$\begin{align*} I^2 &= \frac{P}{R} &\quad\quad\quad &|~\sqrt{~~}\\ I &= \sqrt{\frac{P}{R}}\end{align*}$

[question:EB505]

Si l'on connaît la puissance $P$ et l'intensité du courant $I$ ou la tension $U$, on peut toujours en déduire la résistance $R$.

Nous connaissons déjà :

$P=\frac{U^2}{R}$

Résolvons pour $R$ en multipliant les deux côtés de l'équation par $R$ puis en divisant par $P$ :

$R = \frac{U^2}{P}$

D'autre part, $P = I^2 \cdot R$. En divisant les deux côtés par $I^2$, on obtient l'expression recherchée :

$R = \frac{P}{I^2}$

[question:EB506]

Tous les liens présentés précédemment entre puissance, intensité du courant et tension en courant continu s'appliquent également au courant alternatif. Cependant, il faut utiliser les valeurs efficaces de l'intensité du courant et de la tension. Dans un chapitre précédent [sec:spitze_effektiv_wert], nous avons déjà appris à calculer la valeur efficace à partir de la valeur de crête :

$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}}\text{ respectivement }\hat{U} = U_\text{eff} \cdot \sqrt{2}$

[question:EB503]

Cela signifie que, grâce aux formules dérivées précédemment, nous pouvons désormais résoudre les problèmes suivants issus du domaine de la haute fréquence, c'est-à-dire du courant alternatif.

%%%%%

[question:EB507]

La valeur efficace est ici de $U_\text{eff} = \qty{100}{\volt}$. La résistance de terminaison est de $\qty{50}{\ohm}$ (résistance active pure). On cherche la puissance dissipée dans la charge.

$P = \frac{U^2}{R} =\frac{(\qty{100}{\volt})^2}{\qty{50}{\ohm}} = \qty{200}{\watt}$

%%%%%

[question:EB508]

Même si l'intensité du courant est connue, on peut calculer la puissance à l'aide de la formule connue $P = I^2 \cdot R$. On remplace :

$P = (\qty{2}{\ampere})^2 \cdot \qty{50}{\ohm} = \qty{200}{\watt}$

%%%%%

[question:EB509]

Pour calculer la puissance dissipée dans une résistance de $\qty{100}{\ohm}$ soumise à une tension de $\qty{10}{\volt}$, on utilise à nouveau :

$P = \frac{U^2}{R} = \frac{(\qty{10}{\volt})^2}{\qty{100}{\ohm}} = \qty{1}{\watt}$

%%%%%

[question:EB510]

Répondre à cette question demande une certaine réflexion. On indique à la fois une tenue en tension maximale ($\qty{700}{\volt}$) et une puissance maximale ($\qty{1}{\watt}$). La question est de savoir quelle limite est atteinte en premier lorsque l'on augmente la tension.

Calculons d'abord la tension qui doit s'appliquer à la résistance ($\qty{10}{\kilo\ohm}$) pour atteindre exactement la puissance admissible. Pour cela, nous calculons (dérivation ci-dessus) :

$U = \sqrt{P \cdot R} = \sqrt{\qty{1}{\watt} \cdot \qty{10000}{\ohm}} = \qty{100}{\volt}$

C'est donc la tension continue maximale recherchée !

%%%%%

[question:EB511]

Le calcul est identique à celui de l'exercice précédent, seuls les valeurs numériques diffèrent :

$U = \sqrt{P \cdot R} = \sqrt{\qty{6}{\watt} \cdot \qty{10^5}{\ohm}} \approx \qty{774,6}{\volt} \approx \qty{775}{\volt}$

%%%%%

[question:EB512]

Si la valeur de la résistance et la capacité de charge maximale sont données et que l'on cherche l'intensité maximale du courant, on utilise la relation :

$I = \sqrt{\frac{P}{R}} =  \sqrt{\frac{\qty{23}{\watt}}{\qty{120}{\ohm}}} \approx \qty{0,4378}{\ampere} \approx \qty{438}{\milli\ampere}$

[question:EB513]

Dans cette question, un oscilloscope est utilisé pour mesurer la tension crête à crête aux bornes de la charge. Cette tension est de $U_\text{SS} = \qty{25}{\volt}$. Cela signifie que la tension de crête est de $\hat{U} = \qty{12,5}{\volt}$. Calculons d'abord la valeur efficace de la tension :

$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}} = \frac{\qty{12,5}{\volt}}{\sqrt{2}} \approx \qty{8,84}{\volt}$

L'intensité efficace du courant (loi d'Ohm) est alors :

$I_\text{eff} = \frac{U_\text{eff}}{R} = \frac{\qty{8,84}{\volt}}{\qty{1000}{\ohm}} \approx \qty{8,8}{\milli\ampere}$

On pourrait également calculer la puissance efficace, mais la question ne va pas jusque-là.

---

[question:EB514]

La réponse à cette question peut être calculée mentalement. Onze résistances identiques sont connectées en parallèle, comme illustré dans la figure [ref:e_dummyload_11]. Cela signifie que l'intensité du courant traversant chaque résistance est $1/11$ de l'intensité totale. Par conséquent, la puissance dissipée dans chaque résistance n'est que $1/11$ de la puissance totale.

La puissance totale admissible est donc de $11 \cdot \qty{5}{\watt} = \qty{55}{\watt}$.

<margin>
[picture:1014:e_dummyload_11:Charge fictive composée de 11 résistances de même valeur]
</margin>