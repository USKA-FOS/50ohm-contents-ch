%TODO ggf. le chapitre doit être déplacé ailleurs 

Dans le sous-chapitre *Décibels* dans le bloc sur "Courant, tension, résistance, puissance, énergie", il a déjà été indiqué que les ajouts $\unit{\dBd}$ et $\unit{\dBi}$, utilisés pour indiquer les gains d'antenne, désignent la référence sous-jacente. Dans ce cas, la valeur en décibels ne se réfère pas à une puissance ou à une tension, mais à un émetteur de référence particulier. Les valeurs habituelles sont $\unit{\dBi}$, par rapport à l'émetteur isotrope sphérique, ainsi que $\unit{\dBd}$, par rapport au dipôle demi-onde.

Le *Émetteur isotrope* (voir figure [ref:e_Kugelstrahler]) est une antenne hypothétique qui rayonne de manière égale dans toutes les directions. Si une antenne réelle présente une directivité, le rayonnement est plus fort dans certaines directions et plus faible dans d'autres que ce qu'il serait pour l'émetteur isotrope hypothétique. 

<margin>
[picture:751:e_Kugelstrahler:Émetteur isotrope au centre d'une sphère, qui produit la même puissance de rayonnement à tous les points de la surface de la sphère]
</margin>

Le gain dans une direction (par exemple, la direction du faisceau principal qui est la direction avec le gain d'antenne maximal) par rapport à un émetteur isotrope peut être indiqué en décibels $\unit{\dB}$. Au lieu de $\unit{\dB}$, on écrit $\unit{\dBi}$ pour clarifier que l'on se réfère à l'émetteur isotrope.

[question:EG220]

Même un simple dipôle demi-onde a un gain, car il rayonne perpendiculairement au conducteur de $\qty{2,15}{\dB}$ plus fortement qu'un émetteur isotrope. Par conséquent, un dipôle demi-onde a un gain de $\qty{2,15}{\dBi}$.

Parfois, le gain qui dépasse celui d'un dipôle demi-onde est intéressant, c'est-à-dire le gain par rapport à un dipôle demi-onde. Celui-ci est indiqué en $\unit{\dBd}$, où le $\text{d}$ signifie dipôle. Un dipôle demi-onde a donc un gain de $\qty{0}{\dBd}$. Les antennes qui ont un gain supérieur à celui d'un dipôle demi-onde ont un gain supérieur à $\qty{0}{\dBd}$ et les antennes avec un gain inférieur à celui d'un dipôle demi-onde ont un gain inférieur à $\qty{0}{\dBd}$.

Comparons encore une fois le gain d'un dipôle demi-onde indiqué en $\unit{\dBi}$ et indiqué en $\unit{\dBd}$ : le dipôle demi-onde a dans la direction du faisceau principal un gain de $\qty{2,15}{\dBi}$, car il rayonne $\qty{2,15}{\dB}$ plus fortement par rapport à l'émetteur isotrope. En $\unit{\dBd}$, il s'agit de $\qty{0}{\dBd}$. L'indication en $\unit{\dBi}$ est toujours $\qty{2,15}{\dB}$ plus élevée que l'indication en $\unit{\dBd}$.

Cela se trouve également dans le recueil de formules : 

$g_i = g_d + \qty{2,15}{\dB}$

[question:EG221]
