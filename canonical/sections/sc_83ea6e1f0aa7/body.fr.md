Les préamplificateurs ou convertisseurs de réception montés sur les antennes nécessitent une alimentation en courant continu. Pour éviter d’ajouter une ligne d’alimentation supplémentaire en courant continu, la tension d’alimentation peut également être transmise via le câble coaxial, en parallèle au signal HF, sans que les deux signaux ne se perturbent mutuellement. Pour injecter la tension continue dans le câble coaxial, on utilise donc un coupleur d’alimentation à distance (ou BIAS-T en anglais). L’illustration [ref:a_qo100_bias_t] montre une station QO-100 équipée d’un coupleur d’alimentation à distance pour l’alimentation électrique du préamplificateur (LNB).

<margin>
[picture:1080:a_qo100_bias_t:Station QO-100 avec coupleur d’alimentation à distance pour l’alimentation du LNB]
</margin>

[question:AD322]

Techniquement, cette structure peut être réalisée, comme illustré dans l’image [ref:a_bias_t], à l’aide d’un circuit très simple. Le coupleur d’alimentation à distance (BIAS-T) se compose, en plus des connexions, uniquement de deux condensateurs et d’une inductance. Nous avons déjà rencontré ce circuit lors de l’étude du MMIC, dont la tension d’alimentation est injectée via sa sortie à l’aide d’un BIAS-T.

<margin>
[picture:399:a_bias_t:Coupleur d’alimentation à distance (BIAS-T)]
</margin>

[question:AD323]

Un BIAS-T se reconnaît au fait que, d’un côté, le signal HF est acheminé vers le récepteur (RX), tandis que de l’autre côté, un préamplificateur ou un convertisseur de réception (LNA) est connecté. En outre, une tension continue d’alimentation est injectée via le connecteur DC. Cette tension continue parvient, via l’inductance, sur le conducteur intérieur du câble coaxial et alimente ainsi le LNA connecté. L’inductance présente une impédance élevée pour la haute fréquence, de sorte que le signal HF ne s’échappe pas vers l’alimentation électrique.

Le condensateur de couplage $C_1$ empêche la tension continue injectée d’atteindre l’entrée du récepteur. Sans le condensateur $C_1$, la tension d’alimentation pourrait être court-circuitée à la masse.

[question:AD324]

---

L’inductance sert à injecter la tension continue d’alimentation dans la ligne, tout en présentant une résistance élevée pour la haute fréquence. Ainsi, la tension continue peut atteindre le LNA sans que le signal HF ne s’échappe vers l’alimentation électrique. Le condensateur $C_2$ évacue les composantes HF résiduelles vers la masse. Cela empêche les signaux HF de s’injecter dans l’alimentation électrique.

<indepth>
[photo:288:a_Bias T Platine:Plaque de circuit imprimé BIAS-T - conçue avec KiCAD]
Voici à quoi pourrait ressembler la mise en œuvre pratique du schéma illustré sous forme de plaque de circuit imprimé. $C_2$ et $C_3$ sont des condensateurs de découplage pour différentes bandes de fréquences, garantissant ainsi le bon fonctionnement sur une large plage de fréquences. $L_1$ sert à l’alimentation en tension continue et doit être dimensionné en conséquence pour le courant de charge. Le condensateur de découplage $C_2$ du côté de la tension continue doit supprimer la tension HF. Il doit être choisi de telle sorte qu’il présente, à la fréquence utile HF, une réactance inférieure à 1 ohm.
</indepth>

La bobine située entre le côté DC (par exemple $\qty{12}{\volt}$) et le côté HF (par exemple $\qty{10}{\giga\hertz}$ signal reçu) ne doit pas laisser passer les composantes HF vers le côté DC. Il s’agit donc d’une self de choc qui doit présenter une impédance élevée à la fréquence utile (par exemple $X_L = \qty{10}{\kilo\ohm}$). Le courant d’alimentation du préamplificateur ou du convertisseur (LNA) circule à travers cette self. Le diamètre du fil de la self doit être suffisamment grand pour que le courant continu d’alimentation ne provoque pas d’échauffement de la self. En d’autres termes, la bobine doit avoir une capacité de charge en courant appropriée.

[question:AD325]