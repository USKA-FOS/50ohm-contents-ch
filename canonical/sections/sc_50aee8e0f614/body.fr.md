À l'aide d'un mélangeur, une fréquence déterminée (ou une bande de fréquences avec une bande passante définie) peut être convertie en une fréquence plus élevée ou plus basse. Pour ce faire, les signaux sont multipliés entre eux. 

<indepth>
Une multiplication de signaux dans le domaine temporel conduit à une addition (ou une soustraction) dans le domaine des fréquences. Cette relation peut être expliquée de manière illustrative par l'identité trigonométrique suivante (un peu simplifiée, les facteurs $2\pi\cdot t$ ont été omis pour plus de clarté) :  
  
$\sin(f_1)\cdot\sin(f_2) = \frac{1}{2}\left(\cos(f_1-f_2)-\cos(f_1+f_2)\right)$
  
Lorsque deux signaux sinusoïdaux sont multipliés ensemble – l'un avec la fréquence $f_1$ et l'autre avec la fréquence $f_2$ – deux nouveaux signaux cosinusoïdaux (qui ne sont rien d'autre qu'un sinus déphasé) apparaissent dans le domaine des fréquences. Ceux-ci se situent aux fréquences $f_1 - f_2$ et $f_1 + f_2$. On peut se représenter cela comme une composante de fréquence déplacée vers le bas et une autre vers le haut. C'est exactement ce principe que le mélangeur exploite.

Dans ce cas, deux composantes de fréquence sont toujours générées. En pratique, cependant, une seule d'entre elles est généralement souhaitée, c'est pourquoi des filtres appropriés sont utilisés après le mélangeur pour sélectionner le produit de mélange souhaité. En fait, des fréquences négatives peuvent également apparaître lors de la formation de la différence, c'est pourquoi on considère généralement la valeur absolue $| f_1 \pm f_2 |$.
</indepth>

---

Un mélangeur utilise des composants non linéaires, par exemple des diodes, pour multiplier les signaux entre eux. Des produits de mélange sont ainsi générés, dont les fréquences correspondent mathématiquement à la somme et à la différence des fréquences des signaux d'entrée.

En raison de cette propriété, les mélangeurs sont utilisés de manière ciblée pour convertir les signaux dans d'autres bandes de fréquences souhaitées – par exemple pour la transposition ascendante ou descendante dans les émetteurs et les récepteurs. Dans les schémas blocs, un mélangeur, comme représenté dans la figure [ref:e_mischer], est symbolisé par un cercle avec un signe de multiplication, qui indique l'effet multiplicatif de ce sous-ensemble.

<margin>
[picture:903:e_mischer:Mélangeur]
</margin>

---

Les fréquences générées à une sortie d'un mélangeur consistent principalement en les deux produits de mélange des signaux fournis $f_\text{e}$, le signal d'entrée et $f_\text{o}$ le signal provenant d'un oscillateur. Dans ce cas, deux produits de mélange souhaités résultent de la somme et de la valeur absolue de la différence des signaux fournis:

$f_\text{z}=|f_\text{e}\pm f_\text{o}|$

En raison du $\pm$, une distinction de cas doit être faite : il en résulte ainsi $f_\text{z1} = f_\text{e}+f_\text{o}$ ainsi que $f_\text{z2}=|f_\text{e}-f_\text{o}|$.

Les barres de valeur absolue $|x|$ signifient que seule la valeur numérique sans signe est considérée. Si $x$ est négatif, il est rendu positif. Si $x$ est déjà positif, il reste inchangé.

Normalement, seul l'un des produits de mélange souhaités est utilisé pour le traitement ultérieur du signal. L'autre produit de mélange (ainsi que d'éventuels autres produits de mélange non souhaités - voir l'approfondissement) doivent ensuite être éliminés du mélange de signaux par filtrage.

<indepth>
Un mélangeur réel génère, outre les produits de mélange souhaités, également des produits de mélange d'ordre supérieur comme par exemple $2 * f_\text{in1} + f_\text{in2}$ etc. Ces produits de mélange non souhaités doivent ensuite être éliminés par des filtres appropriés. Les deux fréquences d'entrée ne sont également pas complètement supprimées dans le signal de sortie des mélangeurs réels et doivent être prises en compte lors du traitement ultérieur du signal. En utilisant un mélangeur en anneau équilibré (Balance-Mixer), les deux signaux d'entrée peuvent être très fortement supprimés dans le signal de sortie, c'est pourquoi ce type de mélangeur est souvent utilisé.
</indepth>

[question:EF201]

Pour cette question, nous devons simplement ajouter et soustraire une fois la fréquence de l'oscillateur et prendre en compte la valeur absolue.

$f_\text{z1} = f_\text{e}+f_\text{o} = \qty{21}{\mega\hertz} + \qty{31,7}{\mega\hertz} = \qty{52,7}{\mega\hertz}$

$f_\text{z2}=|f_\text{e}-f_\text{o}| =|\qty{21}{\mega\hertz} - \qty{31,7}{\mega\hertz}| = |\qty{-10,7}{\mega\hertz}| = \qty{10,7}{\mega\hertz}$

Les questions suivantes fonctionnent selon le même principe.

[question:EF202]
[question:EF203]
[question:EF204]
[question:EF205]

Comme différentes fréquences sont générées dans les mélangeurs par le processus de mélange, *les étages mélangeurs doivent toujours être très bien blindés*, afin que ceux-ci ne rayonnent pas dans d'autres étages ou appareils et en particulier ne perturbent pas d'autres services radio!

[question:EF206]