Le champ électromagnétique d’une antenne peut être divisé, comme illustré dans la figure [ref:a_nahfernfeld], en le *champ proche* dans l’environnement immédiat de l’antenne et le *champ lointain*, plus éloigné. Le champ proche est lui-même subdivisé en *champ proche réactif* et *champ proche rayonné*.

<tip>
Dans les [explications des procédures d’évaluation selon le BEMFV](https://50ohm.de/bemfv), l’Agence fédérale des réseaux (BNetzA) a clarifié les concepts et les procédures pour la détermination des distances de sécurité.
[photo:80:n_Bewertungsverfahren:Ce document décrit les procédures d’évaluation.]
</tip>

[picture:1113:a_nahfernfeld:Définitions des distances pour le champ proche et le champ lointain selon l’Agence fédérale des réseaux (BNetzA).]

---

Selon la définition utilisée dans la figure par l’Agence fédérale des réseaux (BNetzA), le champ proche réactif s’étend jusqu’à une distance

$d \le \dfrac{\lambda}{2 \cdot \pi}$

de l’antenne, où $\lambda$ désigne la longueur d’onde. Au-delà de cette distance commence le champ proche rayonné. La distance de cette limite dépend donc de la longueur d’onde. Pour une longueur d’onde de, par exemple, $\qty{20}{\meter}$, on obtient :

$d = \frac{\qty{20}{\meter}}{2 \cdot \pi} \approx \qty{3,18}{\meter}$

Dans cet exemple, le champ proche réactif s’étend donc jusqu’à environ $\qty{3,18}{\meter}$ de l’antenne.

Dans le champ proche réactif d’une antenne, l’**intensité du champ électrique** et l’**intensité du champ magnétique** ne présentent pas de relation de phase constante entre elles. Ce que cela signifie exactement est expliqué plus en détail dans l’approfondissement ci-contre.

[question:AK101]

Si l’on examine l’évolution du champ électrique et du champ magnétique pour une antenne dipôle sur ces différentes zones dans la figure [ref:a_dipol_feld_e_h], on constate que les deux grandeurs de champ n’ont pas les mêmes amplitudes. Le champ électrique est bien plus fort que le champ magnétique. Pour une antenne boucle magnétique dans la figure [ref:a_loop_feld_e_h], c’est exactement l’inverse : le champ magnétique est bien plus fort que le champ électrique.

<margin>
[picture:1114:a_dipol_feld_e_h:Évolution de l’intensité du champ électrique et du champ magnétique d’une antenne dipôle sur les zones du champ proche et du champ lointain (échelle logarithmique).]
[picture:1115:a_loop_feld_e_h:Évolution de l’intensité du champ électrique et du champ magnétique d’une antenne boucle sur les zones du champ proche et du champ lointain (échelle logarithmique).]
</margin>

<indepth>
Pour les personnes intéressées par les mathématiques et déjà familiarisées avec les nombres complexes, voici une explication simplifiée du fait que l’**intensité du champ électrique** et l’**intensité du champ magnétique** ne présentent pas de relation de phase indépendante de la position dans le champ proche réactif.

Pour un dipôle court, les champs peuvent être simplifiés comme suit :

$ \underline{E}(r)~=~\left( \underbrace{\frac{A}{r^3}}_{\text{quasi-statique}} + \underbrace{j\,\frac{B}{r^2}}_{\text{inductif}} + \underbrace{\frac{C}{r}}_{\text{rayonnement}} \right) e^{-jkr}$

$ \underline{H}(r)~=~\left( \underbrace{j\,\frac{D}{r^2}}_{\text{inductif}} + \underbrace{\frac{F}{r}}_{\text{rayonnement}} \right) e^{-jkr}. $

Les grandeurs soulignées sont complexes et décrivent, en plus de l’amplitude, la phase des différentes composantes du champ. Des facteurs comme $j$ ou $-j$ dans les équations complètes des champs correspondent à des déphasages de $\qty{90}{\degree}$ ou $\qty{-90}{\degree}$.

Comme les différentes composantes diminuent à des vitesses différentes en fonction de la distance $r$, leur rapport change. Par conséquent, la **différence de phase** entre l’**intensité du champ électrique** et l’**intensité du champ magnétique** dans le champ proche dépend de la distance, de la direction et de la forme de l’antenne.

Pour une compréhension complète, il faut considérer les composantes vectorielles individuelles des équations des champs. Ces relations dépassent largement le cadre des contenus d’apprentissage de la classe A et ne sont pas pertinentes pour l’examen.
</indepth>

En particulier dans le champ proche réactif, des **intensités de champ** locales élevées peuvent survenir en raison des composantes électriques ou magnétiques fortes qui diminuent rapidement avec la distance. Cette zone est qualifiée de *réactive* car une grande partie de l’énergie du champ n’est pas rayonnée, mais oscille entre l’antenne et le champ. Tout comme pour un condensateur (champ électrique) ou une bobine (champ magnétique), l’énergie stockée dans le champ proche réactif n’est pas consommée, mais restituée à l’antenne avec un déphasage – cette oscillation entre le champ et l’antenne correspond à la composante réactive de l’impédance de l’antenne, tandis que seule la composante active (résistance de rayonnement) décrit la puissance effectivement rayonnée.

Dans le *champ proche rayonné*, dans la zone

$\frac{\lambda}{2\pi} < d < 4\cdot\lambda$

les composantes de champ rayonnées prennent progressivement le dessus. Le rapport entre l’**intensité du champ électrique** et l’**intensité du champ magnétique** se rapproche alors de plus en plus des rapports observés dans le champ lointain. Cependant, l’antenne rayonne déjà dans cette zone, mais les composantes réactives du champ perdent de leur importance avec l’augmentation de la distance. Pour de nombreuses considérations simplifiées, le champ proche rayonné peut déjà être traité de manière similaire au champ lointain. Nous y reviendrons plus en détail ultérieurement.

Le *champ lointain* commence, selon la définition utilisée ici, à une distance

$d \ge 4\cdot\lambda$

de l’antenne. Dans cette zone, l’**intensité du champ électrique** et l’**intensité du champ magnétique** diminuent chacune proportionnellement à $\frac{1}{d}$. De plus, les deux composantes du champ sont dans un rapport fixe l’une par rapport à l’autre et présentent une relation de phase constante.

---

Le rapport des amplitudes de l’**intensité du champ électrique** et de l’**intensité du champ magnétique** est appelé *impédance d’onde* :

$Z_\mathrm{F}(d)=\left|\frac{E(d)}{H(d)}\right|$

La figure [ref:a_feldwellenwiderstand] montre comment l’**impédance d’onde** évolue avec l’augmentation de la distance par rapport à l’antenne. Dans le champ proche réactif, elle dépend fortement de la forme de l’antenne, de la direction considérée et de la distance. Elle peut y être nettement supérieure ou inférieure à l’**impédance d’onde** de l’espace libre.

Dans le champ proche rayonné, le rapport entre l’**intensité du champ électrique** et l’**intensité du champ magnétique** se rapproche progressivement de la valeur de l’espace libre. Dans le champ lointain, elle est enfin constante et s’élève approximativement à :

$Z_0 = \sqrt{\dfrac{\mu_0}{\varepsilon_0}} \approx \qty{120\pi}{\ohm} \approx \qty{377}{\ohm}$

L’**impédance d’onde** de l’espace libre relie les grandeurs du champ électrique et du champ magnétique. Elle mesure la force relative de l’**intensité du champ électrique** par rapport à l’**intensité du champ magnétique**.

[question:AK102]

Il est important de retenir cette valeur, car nous en aurons besoin pour la dérivation de la formule d’approximation.

Faisons un résumé :

* Le champ lointain d’une source de rayonnement est la zone dans laquelle les vecteurs de l’**intensité du champ électrique** (E), de l’**intensité du champ magnétique** (H) et la direction de propagation sont perpendiculaires les uns aux autres et ne présentent pas de **différence de phase**. De plus, l’**impédance d’onde** doit correspondre à celle de l’espace libre.
* La limite entre le champ lointain et le champ proche dépend principalement de la longueur d’onde. Cependant, le type d’antenne utilisée et son environnement jouent également un rôle. Pour les antennes filaires (par exemple, dipôles) principalement utilisées en radioamateurisme, le champ lointain se forme à une distance d’environ $4\cdot\lambda$.

<margin>
[picture:1116:a_feldwellenwiderstand:Évolution de l’impédance d’onde sur les zones du champ proche et du champ lointain (échelle logarithmique).]
</margin>