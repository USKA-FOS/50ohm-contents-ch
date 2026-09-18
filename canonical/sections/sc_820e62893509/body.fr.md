%TODO éventuellement déplacer ce chapitre ailleurs

Dans le sous-chapitre *Décibel* du bloc traitant de la « Courant, tension, résistance, puissance, énergie », il a déjà été évoqué que les suffixes $\unit{\dBd}$ et $\unit{\dBi}$, utilisés pour indiquer les gains d'antenne, désignent la référence sous-jacente. Dans ce cas, la valeur en décibels ne se rapporte pas à une puissance ou une tension, mais à un radiateur de référence spécifique. Les références courantes sont $\unit{\dBi}$, basé sur le radiateur isotrope sphérique, et $\unit{\dBd}$, basé sur le dipôle demi-onde.

Le *radiateur isotrope* (cf. illustration [ref:e_Kugelstrahler]) est une antenne hypothétique idéale qui rayonne avec la même intensité dans toutes les directions. Si une antenne réelle présente une directivité, le rayonnement est plus intense dans certaines directions et moins intense dans d'autres que ce que produirait le radiateur isotrope hypothétique.

<margin>
[picture:751:e_Kugelstrahler:Radiateur isotrope au centre d'une sphère, produisant une puissance rayonnée identique en tous points de la surface de la sphère]
</margin>

Le gain dans une direction donnée (par exemple, la direction principale de rayonnement, qui est celle où le gain de l'antenne est maximal) par rapport à un radiateur isotrope peut être exprimé en décibels $\unit{\dB}$. On utilise la notation $\unit{\dBi}$ pour préciser qu'il s'agit d'une référence au radiateur isotrope.

[question:EG220]

Un simple dipôle demi-onde possède également un gain, car il rayonne perpendiculairement au conducteur avec une intensité supérieure de $\qty{2,15}{\dB}$ à celle d'un radiateur isotrope. Ainsi, un dipôle demi-onde a un gain de $\qty{2,15}{\dBi}$.

Parfois, on s'intéresse au gain supplémentaire par rapport à celui d'un dipôle demi-onde, c'est-à-dire au gain par rapport à un dipôle demi-onde. Ce gain est exprimé en $\unit{\dBd}$, où le « d » signifie dipôle. Un dipôle demi-onde a donc un gain de $\qty{0}{\dBd}$. Les antennes offrant un gain supérieur à celui d'un dipôle demi-onde ont un gain supérieur à $\qty{0}{\dBd}$, tandis que celles dont le gain est inférieur ont un gain inférieur à $\qty{0}{\dBd}$.

Comparons une dernière fois le gain d'un dipôle demi-onde exprimé en $\unit{\dBi}$ et en $\unit{\dBd}$ : le dipôle demi-onde a un gain de $\qty{2,15}{\dBi}$ dans la direction principale de rayonnement, car il rayonne $\qty{2,15}{\dB}$ plus intensément que le radiateur isotrope. Exprimé en $\unit{\dBd}$, il atteint $\qty{0}{\dBd}$. La valeur en $\unit{\dBi}$ est toujours supérieure de $\qty{2,15}{\dB}$ à celle en $\unit{\dBd}$.

Cela est également indiqué dans le recueil de formules :

$g_i = g_d + \qty{2,15}{\dB}$

[question:EG221]