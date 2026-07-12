La modulation par déplacement de phase (Phase Shift Keying, PSK) est un procédé de modulation numérique utilisé pour la transmission de données dans les télécommunications et en radioamateur. La PSK repose sur la modification de la phase d'un signal porteur pour représenter différents états de données. Comparée à la modulation d'amplitude ou de fréquence, la PSK est moins sensible au bruit d'amplitude et peut atteindre un débit de données plus élevé pour une bande passante donnée.

[picture:705:psk:Modulation par déplacement de phase (Phase-shift Keying)]

Principe de la modulation par déplacement de phase (PSK)

Dans sa forme la plus simple, le **BPSK (Binary Phase Shift Keying)**, il existe deux angles de phase, par exemple $\qty{0}{\degree}$ et $\qty{180}{\degree}$. Chaque angle de phase représente une valeur binaire ($\num{0}$ ou $\num{1}$). Lors d'un changement des valeurs binaires, la phase du porteur change de $\qty{180}{\degree}$.

Pour des débits de données plus élevés, il existe des variantes telles que le **QPSK (Quadrature Phase Shift Keying)** et le **8-PSK**, qui utilisent respectivement quatre et huit positions de phase pour transmettre plusieurs bits par symbole:
- **QPSK**: Utilise quatre phases ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ et $\qty{270}{\degree}$) pour coder respectivement deux bits par symbole.
- **8-PSK**: Utilise huit phases pour coder trois bits par symbole.

Signaux dans la représentation temporelle

Dans la représentation temporelle d'un signal PSK, la modulation par déplacement de phase se manifeste par un changement brutal de l'angle de phase du signal porteur, tandis que l'amplitude reste constante. Il s'agit d'une différence marquée par rapport à la modulation d'amplitude ou de fréquence, car l'amplitude et la fréquence du signal restent constantes, seule la phase change à chaque changement de symbole.

Exemple: BPSK dans la représentation temporelle
- Dans le cas du BPSK, le signal est divisé en deux phases: par exemple, une amplitude positive pour une phase ($\qty{0}{\degree}$) et une amplitude négative pour la phase opposée ($\qty{180}{\degree}$).
- Dans un diagramme temporel, on observe donc un saut du signal à chaque changement de bit, par exemple de positif à négatif ou vice versa.

Exemple: QPSK dans la représentation temporelle
- Ici, on observe quatre angles de phase différents. Les transitions peuvent également être abruptes, mais l'amplitude ne change pas.
- Comme plusieurs angles de phase sont utilisés, les sauts de phase sont plus petits, et la courbe a un aspect légèrement "lissé" par rapport au BPSK.

Comment les signaux sont identifiés

Dans un oscilloscope ou un diagramme de phase, les transitions de phase sont visibles:
- **Dans le domaine temporel**: Un basculement brutal de la phase du signal (positif à négatif ou entre différentes positions de phase).
- **Dans le diagramme de phase** (souvent affiché sous forme de diagramme de constellation): Chaque angle de phase est représenté par un point sur un cercle, qui correspond aux différents états (bits). Pour un signal propre, les points restent stables à des positions fixes.

La PSK est particulièrement utile dans les communications numériques, car elle permet des débits de données élevés tout en assurant une transmission relativement robuste. La modification de la phase tout en maintenant une amplitude constante aide à mieux identifier le signal même en présence de bruit et d'interférences, permettant ainsi une transmission plus stable.

[question:AE401]