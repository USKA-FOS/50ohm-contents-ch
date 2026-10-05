Les préamplificateurs ou convertisseurs de réception montés sur l'antenne et déportés nécessitent une alimentation en courant continu. Pour éviter une ligne d'alimentation en courant continu supplémentaire, la tension d'alimentation peut également être transmise via le câble coaxial, parallèlement au signal haute fréquence, sans que les deux signaux ne s'interfèrent mutuellement. Pour injecter la tension continue dans le câble coaxial, un coupleur d’alimentation à distance ou BIAS-T en anglais est donc utilisé. La figure [ref:a_qo100_bias_t] montre une station QO-100 avec un coupleur d’alimentation à distance pour l'alimentation électrique du préamplificateur (LNB).

<margin>
[picture:1080:a_qo100_bias_t:Station QO-100 avec coupleur d’alimentation à distance pour l'alimentation du LNB]
</margin>

[question:AD322]

<wordorigin>
*Terminologie*

- BIAS-T : circuit en forme de T, avec lequel une tension continue (BIAS) et un signal haute fréquence peuvent être acheminés ensemble sur une ligne ou séparés l'un de l'autre.

- BIAS = tension de polarisation ou tension continue superposée à un signal. En électronique, le terme bias désigne généralement une tension continue ou un courant continu pour le réglage du point de fonctionnement.

</wordorigin>

Techniquement, cette structure, comme illustré dans la figure [ref:a_bias_t], peut être réalisée avec un circuit très simple. Le coupleur d’alimentation à distance (BIAS-T) ne consiste, outre les connexions, qu'en deux condensateurs et une inductance. Nous avons déjà rencontré ce circuit avec le MMIC dans la section [sec:integrierte_schaltkreise], dont la tension d'alimentation est injectée via la sortie avec un BIAS-T.

<margin>
[picture:399:a_bias_t:Coupleur d’alimentation à distance (BIAS-T)]
</margin>

<wordorigin>
*autres termes*

- LNA = *L*ow *N*oise *A*mplifier, un préamplificateur à faible bruit

- LNB = *L*ow *N*oise *B*lock, un préamplificateur et convertisseur descendant à faible bruit
  Le LNB est traité en détail dans la section [sec:low_noise_block].

</wordorigin>

[question:AD323]

Un BIAS-T se reconnaît au fait que d'un côté, le signal haute fréquence est acheminé vers le récepteur (RX), tandis que de l'autre côté, un préamplificateur ou un convertisseur de réception (LNA) est connecté. De plus, une tension continue d'alimentation est injectée via la connexion DC. Cette tension continue atteint l'âme du câble coaxial via l'inductance et alimente ainsi le LNA connecté. L'inductance présente une haute impédance pour les hautes fréquences, de sorte que le signal haute fréquence ne s'écoule pas vers l'alimentation électrique.

Le condensateur de couplage $C_1$ empêche la tension continue injectée d'atteindre l'entrée du récepteur. Sans le condensateur $C_1$, la tension d'alimentation pourrait donc être court-circuitée à la masse.

[question:AD324]

---

L'inductance sert à injecter la tension continue d'alimentation dans la ligne, tout en présentant une haute résistance pour les hautes fréquences. Ainsi, la tension continue peut atteindre le LNA sans que le signal haute fréquence ne s'écoule vers l'alimentation électrique. Le condensateur $C_2$ dérive les composantes haute fréquence résiduelles vers la masse. Cela empêche les signaux haute fréquence de se coupler dans l'alimentation électrique.

<indepth>
[photo:288:a_Bias T Platine:Platine BIAS-T - créée avec KiCAD]
Voici à quoi pourrait ressembler la mise en pratique pratique du schéma de circuit illustré sur une carte de circuit imprimé. $C_2$ et $C_3$ sont des condensateurs de découplage pour différentes bandes de fréquences, afin que la fonction soit assurée sur une large bande de fréquences. $L_1$ sert à acheminer la tension continue et doit être dimensionnée spécifiquement pour le courant de charge. Le condensateur de découplage $C_2$ côté tension continue doit supprimer la tension haute fréquence. Il doit être choisi de manière à présenter une réactance inférieure à 1 ohm à la fréquence porteuse haute fréquence.
</indepth>

La bobine entre le côté DC (côté tension continue, par exemple $\qty{12}{\volt}$) et le côté haute fréquence (par exemple, signal reçu à $\qty{10}{\giga\hertz}$) ne doit pas laisser passer les composantes haute fréquence vers le côté DC. Il s'agit donc d'une bobine d'arrêt, qui doit présenter une haute impédance à la fréquence porteuse (par exemple, $X_L = \qty{10}{\kilo\ohm}$). Le courant d'alimentation pour le préamplificateur ou le convertisseur (LNA) circule à travers cette bobine d'arrêt. Le diamètre du fil de la bobine d'arrêt doit être suffisamment grand pour que le courant continu d'alimentation ne provoque pas d'échauffement de la bobine d'arrêt. Autrement dit : la bobine doit avoir une capacité de charge en courant correspondante.

[question:AD325]
