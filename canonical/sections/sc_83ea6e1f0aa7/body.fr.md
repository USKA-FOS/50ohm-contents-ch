Les préamplificateurs ou convertisseurs de réception montés sur les antennes nécessitent une alimentation en tension continue. Pour éviter d'avoir à installer une ligne d'alimentation supplémentaire, la tension d'alimentation peut également être transmise via le câble coaxial, en parallèle avec le signal HF, sans que les deux signaux ne s'interfèrent mutuellement. Pour injecter la tension continue dans le câble coaxial, on utilise donc un filtre d'alimentation à distance ou un BIAS-T en anglais. La figure [ref:a_qo100_bias_t] montre une station QO-100 avec un filtre d'alimentation à distance pour l'alimentation électrique du préamplificateur (LNB).

<margin>
[picture:1080:a_qo100_bias_t:Station QO-100 avec filtre d'alimentation à distance pour l'alimentation électrique du LNB]
</margin>

[question:AD322]

Techniquement, cette structure, comme le montre la figure [ref:a_bias_t], peut être réalisée avec un circuit très simple. Le filtre d'alimentation à distance (BIAS-T) ne se compose, outre les connexions, que de deux condensateurs et d'une inductance. Nous avons déjà rencontré ce circuit lors de l'étude du MMIC, dont la tension d'alimentation est injectée via la sortie avec un BIAS-T.

<margin>
[picture:399:a_bias_t:Filtre d'alimentation à distance (BIAS-T)]
</margin>

[question:AD323]

On reconnaît un BIAS-T au fait que le signal HF est dirigé vers le récepteur (RX) d'un côté, tandis qu'un préamplificateur ou un convertisseur de réception (LNA) est connecté de l'autre côté. En outre, une tension continue d'alimentation est injectée via la connexion DC. Cette tension continue parvient, via l'inductance, au conducteur intérieur du câble coaxial et alimente ainsi le LNA connecté. L'inductance présente une impédance élevée pour les hautes fréquences, de sorte que le signal HF ne s'écoule pas dans l'alimentation électrique.

Le condensateur de couplage $C_1$ empêche que la tension continue injectée n'atteigne l'entrée du récepteur. Sans le condensateur $C_1$, la tension d'alimentation pourrait donc être court-circuitée vers la masse.

[question:AD324]

---

L'inductance sert à injecter la tension continue d'alimentation dans la ligne, tandis qu'elle présente une résistance élevée pour les hautes fréquences. De ce fait, la tension continue peut atteindre le LNA sans que le signal HF ne s'écoule dans l'alimentation électrique. Le condensateur $C_2$ dérive les composantes haute fréquence restantes vers la masse. Cela empêche que les signaux HF ne se couplent dans l'alimentation électrique.

<indepth>
[photo:288:a_Bias T Platine:Plaque BIAS-T - créée avec KiCAD]
C'est à quoi pourrait ressembler la mise en œuvre pratique du schéma de circuit illustré sur une carte de circuit imprimé. $C_2$ et $C_3$ sont des condensateurs de blocage pour différentes bandes de fréquences, afin de garantir le fonctionnement sur une large bande de fréquences. $L_1$ sert à l'alimentation en tension continue et doit être dimensionnée de manière ciblée pour le courant de charge. Le condensateur de blocage $C_2$ du côté de la tension continue doit supprimer la tension HF. Il doit être choisi de manière à présenter une impédance inférieure à 1 Ohm à la fréquence utile HF.
</indepth>

La bobine entre le côté DC (côté tension continue, par exemple $\qty{12}{\volt}$) et le côté HF (par exemple $\qty{10}{\giga\hertz}$ signal reçu) ne doit pas laisser passer les composantes haute fréquence vers le côté DC. Il s'agit donc d'une bobine d'arrêt qui doit présenter une impédance élevée à la fréquence utile (par exemple $X_L = \qty{10}{\kilo\ohm}$). Le courant d'alimentation pour le préamplificateur ou le convertisseur (LNA) circule à travers cette bobine d'arrêt. Le diamètre du fil de la bobine d'arrêt doit être suffisamment grand pour que le courant continu d'alimentation ne provoque pas de chauffage de la bobine d'arrêt. En d'autres termes : la bobine doit présenter une capacité de charge appropriée.

[question:AD325]