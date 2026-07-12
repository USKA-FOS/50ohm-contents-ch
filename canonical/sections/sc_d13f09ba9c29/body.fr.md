%Dans le champ proche d’une antenne, l’intensité du champ électrique et l’intensité du champ magnétique n’ont pas de relation de phase constante entre elles. Cela ne change que dans le champ lointain d’une antenne. La transition entre les deux domaines est progressive et est également appelée champ de transition.

%En général, la transition entre le champ proche et le champ lointain dépend de la longueur d’onde considérée. Elle est indiquée comme

%$d > \dfrac {\lambda} {2 \cdot \pi}$

%Pour une longueur d’onde de par exemple $\qty{20}{\meter}$, la transition est donc à une distance d’environ $d = \frac {\qty{20}{\meter}} {2 \cdot \pi} \approx \qty{3,18}{\meter}$.

%Pour les antennes qui sont géométriquement petites par rapport à leur longueur d’onde, le champ lointain peut cependant ne se former que plus tard.

%Pour le calcul des distances de protection des personnes, une formule approchée est possible dans le champ lointain. Cela évite éventuellement des mesures ou des simulations coûteuses.

% ************

Le champ lointain d’une source de rayonnement est la zone dans laquelle les vecteurs de l’intensité du champ électrique (E), de l’intensité du champ magnétique (H) ainsi que la direction de propagation sont perpendiculaires entre eux et ne présentent pas de différences de phase. De plus, l’impédance de la ligne de champ doit correspondre à celle de l’espace libre.

La limite entre le champ lointain et le champ proche dépend en premier lieu de la longueur d’onde. Cependant, le type d’antenne utilisée et son environnement jouent également un rôle important. Pour les antennes filaires principalement utilisées en radioamateur (par exemple les dipôles), le champ lointain se forme à une distance d’environ $4\cdot\lambda$.

Le champ proche se divise en le champ proche réactif et le champ proche rayonnant. En pratique, la formule pour le champ lointain peut également être utilisée dans le champ proche rayonnant. Cela est dû au fait que la formule approchée fournit ici des estimations très conservatrices, c’est-à-dire que les intensités de champ réelles sont inférieures aux intensités calculées. On est du bon côté. Cela ne s’applique cependant pas aux antennes magnétiques et aux antennes qui sont très courtes par rapport à la longueur d’onde. Dans ces cas, il faut recourir à d’autres procédés, par exemple des programmes de calcul de champ proche.

La transition entre le champ proche réactif et le champ proche rayonnant dépend de la longueur d’onde.

$d > \dfrac {\lambda} {2 \cdot \pi}$

Le calcul avec la formule approchée évite éventuellement des mesures ou des simulations coûteuses.

La formule $d = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_{\textrm{EIRP}}}}{E}$ s’applique à la plupart des formes d’antennes, si la distance de sécurité calculée se situe dans le champ proche rayonnant ou dans le champ lointain.

<indepth>
Dans les [explications des procédures d’évaluation selon BEMFV](https://50ohm.de/bemfv), la BNetzA a expliqué les termes et les procédures pour déterminer les distances de sécurité.
% Image de DL4HR
[photo:80:n_Bewertungsverfahren:Dans ce document, les procédures d’évaluation sont décrites.]
</indepth>