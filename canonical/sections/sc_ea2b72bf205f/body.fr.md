En modifiant la capacité du condensateur déterminant la fréquence, à l'intérieur d'un oscillateur, on peut générer une modulation de fréquence. Dans le cas d'un oscillateur à quartz, par exemple, une diode de capacité en série avec le quartz peut être utilisée pour générer une modulation de fréquence. L'amplitude du signal modulant (par exemple, un microphone) appliqué à la diode de capacité détermine directement la variation de fréquence de l'oscillateur.
[question:AE303]

La fréquence de modulation influence ici la fréquence à laquelle la fréquence de l'oscillateur change.
[question:AE301]

Dans le cas de la modulation de fréquence, l'information du signal modulant ne se trouve pas dans l'amplitude, mais uniquement dans la variation de fréquence du signal porteur. Par conséquent, seuls les passages par zéro du signal porteur doivent être évalués dans le récepteur. Les fluctuations d'amplitude sont ici masquées par un amplificateur limiteur. Par conséquent, la modulation de fréquence est, par nature, insensible aux perturbations impulsives de l'amplitude, qui peuvent être causées, par exemple, par des étincelles d'allumage, des moteurs électriques, etc. La FM convient donc bien pour le fonctionnement dans les véhicules automobiles.
[question:AE302]

La déviation de fréquence d'un signal FM détermine la quantité dont la fréquence de l'oscillateur dans l'émetteur change, en fonction de l'amplitude du signal modulant. Une plus grande déviation de la fréquence correspond, après démodulation dans le récepteur FM, à une plus grande amplitude du signal démodulé. Par conséquent, une plus grande déviation d'un émetteur à modulation de fréquence a une influence directe sur le volume du signal démodulé dans un récepteur FM.
[question:AE305]

La bande passante occupée d'une émission FM est déterminée par la déviation et la fréquence de modulation maximale. En première approximation, pour une faible déviation et une faible fréquence de modulation, la formule de Carson peut être appliquée. Elle indique dans quelle bande passante se trouvent $\qty{99}{\percent}$ de la puissance d'émission.

**Formule de Carson**

$B\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$

La bande passante occupée se calcule ici selon la formule mentionnée ci-dessus. Il en résulte qu'une fréquence de modulation plus élevée ou une déviation plus grande (par exemple, provoquée par une excitation plus élevée du modulateur FM) entraîne une bande passante plus large du signal. Cela peut provoquer des interférences dans les canaux adjacents, car la bande passante du signal augmente dans les deux cas.
[question:AE306]
[question:AE307]
[question:AE304]

Grâce à la formule de Carson, on peut calculer la bande passante occupée d'une émission FM lorsque les valeurs de la déviation et de la fréquence de modulation sont connues. En manipulant la formule de manière appropriée, on peut également calculer les autres grandeurs.
[question:AE309]
[question:AE308]
[question:AE311]
[question:AE312]
[question:AE310]
