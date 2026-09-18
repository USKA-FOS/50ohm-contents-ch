À l'aide d'un mélangeur, il est possible de convertir une fréquence déterminée (ou une bande de fréquences avec une bande passante définie) en une fréquence plus élevée ou plus basse. Pour cela, les signaux sont multipliés entre eux.

<indepth>
La multiplication de signaux dans le domaine temporel entraîne une addition (ou une soustraction) dans le domaine fréquentiel. Cette relation peut être illustrée de manière intuitive à l'aide de l'identité trigonométrique suivante (simplifiée, les facteurs $2\pi\cdot t$ ont été omis pour plus de clarté) :

$\sin(f_1)\cdot\sin(f_2) = \frac{1}{2}\left(\cos(f_1-f_2)-\cos(f_1+f_2)\right)$

Lorsqu'on multiplie deux signaux sinusoïdaux – l'un à la fréquence $f_1$ et l'autre à la fréquence $f_2$ – deux nouveaux signaux cosinusoïdaux (qui ne sont rien d'autre que des sinus déphasés) apparaissent dans le domaine fréquentiel. Ces signaux se situent aux fréquences $f_1 - f_2$ et $f_1 + f_2$. On peut imaginer que l'une des composantes de fréquence est décalée vers le bas et l'autre vers le haut. C'est précisément ce principe que le mélangeur exploite.

Dans ce processus, deux composantes fréquentielles sont toujours générées. En pratique, seule l'une d'elles est généralement souhaitée, c'est pourquoi des filtres adaptés sont utilisés après le mélangeur pour sélectionner le produit de mélange désiré. En réalité, des fréquences négatives peuvent également apparaître lors de la formation de la différence, c'est pourquoi on considère en général la valeur absolue $| f_1 \pm f_2 |$.
</indepth>

---

Un mélangeur utilise des composants non linéaires, par exemple des diodes, pour multiplier les signaux entre eux. Cela génère ce qu'on appelle des produits de mélange dont les fréquences correspondent mathématiquement à la somme et à la différence des fréquences des signaux d'entrée.

Grâce à cette propriété, les mélangeurs sont utilisés de manière ciblée pour convertir des signaux dans d'autres bandes de fréquences souhaitées – par exemple pour le mélange vers le haut ou vers le bas dans les émetteurs et récepteurs. Dans les schémas fonctionnels, un mélangeur est représenté, comme dans la figure [ref:e_mischer], par un cercle avec un signe de multiplication, qui indique l'effet multiplicatif de ce module.

<margin>
[picture:903:e_mischer:Mélangeur]
</margin>

---

Les fréquences générées à la sortie d'un mélangeur proviennent principalement des deux produits de mélange des signaux fournis : $f_\text{e}$, le signal d'entrée, et $f_\text{o}$, le signal provenant d'un oscillateur. Deux produits de mélange souhaités en résultent, correspondant à la somme et à la valeur absolue de la différence des signaux fournis :

$f_\text{z}=|f_\text{e}\pm f_\text{o}|$

En raison du $\pm$, une distinction de cas doit être faite : on obtient ainsi $f_\text{z1} = f_\text{e}+f_\text{o}$ ainsi que $f_\text{z2}=|f_\text{e}-f_\text{o}|$.

Les barres de valeur absolue $|x|$ signifient que seule la valeur numérique est prise en compte, sans son signe. Si $x$ est négatif, il devient positif. S'il est déjà positif, il reste inchangé.

Normalement, seul l'un des produits de mélange souhaités est utilisé pour le traitement ultérieur du signal. L'autre produit de mélange (ainsi que d'éventuels autres produits de mélange indésirables – voir approfondissement) doit ensuite être éliminé du mélange de signaux par filtrage.

<indepth>
Un mélangeur réel génère, en plus des produits de mélange souhaités, des produits de mélange d'ordre supérieur, par exemple $2 * f_\text{in1} + f_\text{in2}$, etc. Ces produits de mélange indésirables doivent également être éliminés par des filtres adaptés. De plus, les deux fréquences d'entrée ne sont pas totalement supprimées dans le signal de sortie des mélangeurs réels et doivent être prises en compte dans le traitement ultérieur du signal. L'utilisation d'un mélangeur en anneau équilibré (balance-mixer) permet de fortement supprimer les deux signaux d'entrée dans le signal de sortie, c'est pourquoi ce type de mélangeur est souvent utilisé.
</indepth>

[question:EF201]

Pour cette question, il suffit d'additionner et de soustraire une fois la fréquence de l'oscillateur, en tenant compte de la valeur absolue.

$f_\text{z1} = f_\text{e}+f_\text{o} = \qty{21}{\mega\hertz} + \qty{31,7}{\mega\hertz} = \qty{52,7}{\mega\hertz}$

$f_\text{z2}=|f_\text{e}-f_\text{o}| =|\qty{21}{\mega\hertz} - \qty{31,7}{\mega\hertz}| = |\qty{-10,7}{\mega\hertz}| = \qty{10,7}{\mega\hertz}$

Les questions suivantes fonctionnent selon le même principe.

[question:EF202]
[question:EF203]
[question:EF204]
[question:EF205]

Comme divers signaux de fréquences sont générés dans les mélangeurs par le processus de mélange, *les étages de mélange doivent toujours être très bien blindés* afin qu'aucune émission parasite ne puisse se produire vers d'autres étages ou appareils, et surtout afin de ne pas perturber d'autres services de radiocommunication !

[question:EF206]