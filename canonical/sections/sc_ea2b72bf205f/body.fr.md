Comme nous l'avons déjà appris dans les classes N et E, dans la modulation de fréquence, l'information du signal modulant ne se trouve pas dans l'amplitude, mais uniquement dans la variation de fréquence du signal porteur. Par conséquent, seuls les passages par zéro du signal porteur doivent être évalués dans le récepteur.

Les fluctuations d'amplitude sont éliminées par un amplificateur limiteur. La modulation de fréquence est donc, par nature, insensible aux perturbations impulsionnelles de l'amplitude, qui peuvent être causées par exemple par des étincelles d'allumage, des moteurs électriques, etc. La FM est donc bien adaptée pour une utilisation dans les véhicules automobiles.

[question:AE302]

Dans la classe A, nous allons maintenant examiner comment la modulation de fréquence peut être générée dans un émetteur et comment calculer la bande passante d'un signal FM.

---

En modifiant la capacité du condensateur déterminant la fréquence dans un oscillateur, on peut générer une modulation de fréquence (cf. [ref:fm_modulation_schaltung]). Par exemple, une diode à capacité variable, placée en série avec un circuit oscillant ou un quartz, permet de générer une modulation de fréquence. L'amplitude de la basse fréquence (BF), par exemple produite par un microphone connecté à la diode à capacité variable, détermine directement la variation de fréquence de l'oscillateur.

[question:AE303]

<margin>
[picture:155:fm_modulation_schaltung:Schéma simple de modulation de fréquence d'un oscillateur avec diode à capacité variable]
</margin>

La fréquence de modulation influence ici la fréquence à laquelle la fréquence de l'oscillateur change.

[question:AE301]

Dans la classe E, nous avons déjà appris ce qu'est l'*excursion de fréquence porteuse*. Elle indique de combien la fréquence instantanée du signal FM est déviée par rapport à la fréquence porteuse sous l'effet du signal modulant. Plus l'amplitude du signal modulant est grande, plus cette déviation de fréquence est importante.

Lors de la démodulation dans le récepteur FM, cette déviation de fréquence est reconvertie en une amplitude correspondante du signal démodulé. Une excursion de fréquence porteuse plus grande conduit donc, dans des conditions par ailleurs identiques, à une amplitude plus grande du signal BF démodulé.

Une excursion de fréquence porteuse plus grande augmente la bande passante nécessaire du signal FM. Si les valeurs prévues sont dépassées, le signal émis peut empiéter sur des canaux adjacents et ainsi provoquer des interférences de canal adjacent.

[question:AE305]
[question:AE306]
[question:AE307]
[question:AE304]

---

En réalité, la bande passante occupée d'une émission FM n'est pas déterminée uniquement par l'excursion, mais aussi par la fréquence de modulation maximale (cf. figure [ref:fm_modulation]). En première approximation, pour une excursion faible et une fréquence de modulation basse, on peut appliquer la formule de Carson. Elle indique dans quelle bande passante se trouve $\qty{99}{\percent}$ de la puissance d'émission.

$BP\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$

<margin>
[picture:910:fm_modulation:Bande passante de la modulation de fréquence]
</margin>

Grâce à la formule de Carson, il est possible de calculer la bande passante occupée d'une émission FM à partir des valeurs connues de l'excursion et de la fréquence de modulation. En réarrangeant la formule de manière appropriée, on peut également calculer les autres grandeurs.

[question:AE309]
[question:AE308]
[question:AE311]
[question:AE312]
[question:AE310]
[question:AE314]
