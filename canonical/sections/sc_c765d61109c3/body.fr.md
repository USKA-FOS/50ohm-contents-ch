Dans un récepteur dont l'entrée reçoit deux signaux HF forts, des perturbations peuvent être causées par de l'intermodulation ou de la modulation croisée.
En cas d'intermodulation, cet effet se manifeste par la génération de fréquences supplémentaires indésirables, similaires à celles produites dans un mélangeur, en raison du comportement non linéaire de l'étage du récepteur (fonctionnement en limite non linéaire). Ces fréquences peuvent se superposer aux signaux utiles reçus et les perturber.
En cas de modulation croisée, cet effet se manifeste par l'influence du signal AM fort et proche en fréquence sur le signal utile souhaité. La modulation du signal adjacent devient alors audible dans le signal reçu et le perturbe.

[question:AF217]
[question:AF219]
[question:AF222]
[question:AF218]

Pour supprimer un signal indésirable fort avant l'entrée du récepteur, on peut par exemple placer un circuit bouchon accordé sur la fréquence exacte du signal perturbateur devant l'entrée du récepteur.

[question:AF223]

La robustesse aux signaux forts d'un récepteur peut être décrite par le point d'interception d'ordre 3 (IP3). Il s'agit d'une mesure du point où les produits de mélange indésirables d'ordre 3 atteignent l'amplitude du signal d'entrée. Plus l'IP3 d'un récepteur est élevé, plus celui-ci peut traiter de grands signaux sans perturbation.

<indepth>
Dans cette section approfondie, nous considérons l'IP3 comme un paramètre de la robustesse aux signaux forts d'un récepteur. En général, les produits de mélange proviennent de non-linéarités dans les amplificateurs, mélangeurs ou autres étages du récepteur. Pour deux signaux d'entrée $f_1$ et $f_2$, des produits d'intermodulation de la forme

$f_{\text{mélange}} = \left| m \cdot f_1 \pm n \cdot f_2 \right|$

peuvent apparaître, où $m,n \in \mathbb{N}_0$ et les deux coefficients ne peuvent pas être nuls simultanément. L'ordre d'un tel produit de mélange est donné par la somme des coefficients :

$\text{Ordre} = m+n$

Les produits d'intermodulation d'ordre 3 sont particulièrement critiques, car ils se situent souvent à proximité des signaux d'entrée initiaux. Ils peuvent ainsi tomber dans la bande de réception souhaitée et être difficiles, voire impossibles, à éliminer par les filtres suivants.

Dans l'illustration suivante [ref:a_intermodulation], l'intermodulation de deux signaux $f_1$ et $f_2$ est représentée. Les produits d'intermodulation d'ordre 3 sont particulièrement mis en évidence :

[picture:1095:a_intermodulation:Intermodulation de deux signaux $f_1$ et $f_2$]

Il est important de noter que ces produits d'intermodulation ne sont pas reçus de l'extérieur, mais se forment dans le récepteur en raison d'un comportement non linéaire. Un test à deux tons permet d'étudier la linéarité d'un récepteur. Pour cela, deux signaux d'entrée définis sont injectés. Si des produits d'intermodulation d'ordre 3 apparaissent en plus de ces deux signaux de base dans le spectre, par exemple dans un diagramme en cascade, cela indique un comportement non linéaire.

L'illustration [ref:a_zweitontest] montre un test à deux tons avec un balayage de puissance, où les produits d'intermodulation d'ordre 3 deviennent clairement visibles.

[picture:1096:a_zweitontest:Test à deux tons avec balayage de puissance]

Si l'on trace la puissance de sortie en fonction de la puissance d'entrée, les signaux de base augmentent dans la zone linéaire avec une pente de $1{:}1$. Les produits d'intermodulation d'ordre 3 augmentent quant à eux avec une pente de $3{:}1$. En prolongeant les zones linéaires de ces deux courbes, on obtient un point d'intersection théorique. Ce point est appelé IP3, c'est-à-dire point d'interception d'ordre 3.

L'IP3 décrit ainsi le point extrapolé où les produits d'intermodulation d'ordre 3 atteindraient théoriquement la même puissance de sortie que les signaux de base. En pratique, ce point n'est généralement pas atteint, car le récepteur entre en compression ou en saturation avant.

Plus l'IP3 d'un récepteur est élevé, meilleure est sa robustesse aux signaux forts. Un IP3 élevé signifie que même des signaux adjacents puissants peuvent être traités sans que des produits d'intermodulation indésirables n'apparaissent dans la bande de réception souhaitée.
</indepth>

[question:AF221]

Pour réduire l'apparition de produits de mélange indésirables à l'entrée du récepteur en raison de signaux puissants, on peut placer un atténuateur commutable devant l'entrée du récepteur. Cela réduit les produits d'intermodulation ainsi que la modulation croisée dans le récepteur. Le signal utile n'est atténué que du facteur de l'atténuateur, tandis que les produits de mélange indésirables sont atténués d'un facteur de $\num{3}$ (ordre 3) en dB en raison des propriétés mathématiques du processus de mélange. Par exemple, un atténuateur de $\qty{10}{\dB}$ réduit le signal utile de seulement $\qty{10}{\dB}$, tandis que les produits de mélange indésirables sont déjà atténués de $\qty{30}{\dB}$.

[question:AF220]