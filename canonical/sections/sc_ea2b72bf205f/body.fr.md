Comme nous l'avons déjà appris dans la section [sec:fm_2], dans la modulation de fréquence, l'information du signal modulant ne se trouve pas dans l'amplitude, mais uniquement dans le changement de fréquence du signal porteur. Par conséquent, seuls les passages par zéro du signal porteur doivent être évalués dans le récepteur.

Les fluctuations d'amplitude sont éliminées ici par un amplificateur limiteur. C'est pourquoi la modulation de fréquence est intrinsèquement insensible aux perturbations impulsionnelles de l'amplitude, causées par exemple par des étincelles d'allumage, des moteurs électriques ou similaires. La FM convient donc bien pour une utilisation dans les véhicules à moteur.

[question:AE302]

Nous allons maintenant examiner comment la modulation de fréquence peut être générée dans un émetteur et comment la bande passante d'un signal FM peut être calculée.

---

La modulation de fréquence peut être générée en modifiant la capacité du condensateur déterminant la fréquence dans un oscillateur (voir [ref:fm_modulation_schaltung]). Par exemple, une modulation de fréquence peut être produite à l'aide d'une diode à capacité variable, placée en série avec un circuit oscillant ou un quartz. L'amplitude de la basse fréquence (BF), générée par exemple par un microphone connecté à la diode à capacité variable, détermine directement le changement de fréquence de l'oscillateur.

[question:AE303]

<margin>
[picture:155:fm_modulation_schaltung:Circuit simple pour la modulation de fréquence d'un oscillateur avec diode à capacité variable]
</margin>

La fréquence de modulation influence ici la fréquence à laquelle la fréquence de l'oscillateur change.

[question:AE301]

Dans la section [sec:fm_2], nous avons déjà rencontré l'*excursion de fréquence porteuse*. Elle indique de quelle valeur la fréquence instantanée du signal FM est déviée par rapport à la fréquence porteuse sous l'effet du signal modulant. Plus l'amplitude du signal modulant est grande, plus cette déviation de fréquence est importante.

Lors de la démodulation dans le récepteur FM, cette déviation de fréquence est reconvertie en une amplitude correspondante du signal démodulé. Une excursion de fréquence plus grande conduit donc, toutes choses égales par ailleurs, à une amplitude plus grande du signal BF démodulé.

Une excursion de fréquence plus grande augmente la bande passante requise du signal FM. Si les valeurs prévues sont dépassées, le signal émis peut s'étendre dans les canaux adjacents et ainsi provoquer des interférences sur les canaux voisins.

[question:AE305]
[question:AE306]
[question:AE307]
[question:AE304]

---

Précisément, la bande passante occupée d'une émission FM n'est pas seulement déterminée par l'excursion, mais aussi par la fréquence de modulation maximale (voir figure [ref:fm_modulation]). En première approximation, pour une petite excursion et une faible fréquence de modulation, la formule de Carson peut être appliquée. Elle indique dans quelle bande passante se trouve $\qty{99}{\percent}$ de la puissance d'émission.

$B\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$

<margin>
[picture:910:fm_modulation:Bande passante de la modulation de fréquence]
</margin>

À l'aide de la formule de Carson, la bande passante occupée d'une émission FM peut être calculée pour des valeurs connues d'excursion et de fréquence de modulation. En réarrangeant convenablement la formule, les autres grandeurs peuvent également être calculées.

[question:AE309]
[question:AE308]
[question:AE311]
[question:AE312]
[question:AE310]
[question:AE314]
