La plage de la résistance d'entrée du circuit est recherchée. La résistance de gauche avec $\qty{200}{\ohm}$ est toujours en série avec le reste du circuit.

Après cette résistance, le circuit se divise en deux branches parallèles :

* une branche avec $\qty{100}{\ohm}$
* une branche avec $\qty{200}{\ohm} + R$

Nous considérons d'abord la valeur la plus petite. Pour cela, nous posons :

$ R = \qty{0}{\ohm} $

Alors, $\qty{100}{\ohm}$ est en parallèle avec $\qty{200}{\ohm}$ :

$ R_\mathrm{par} = \frac{\qty{100}{\ohm} \cdot \qty{200}{\ohm}}{\qty{100}{\ohm} + \qty{200}{\ohm}} \approx \qty{67}{\ohm} $

Avec la résistance en amont, nous obtenons :

$ R_\mathrm{min} = \qty{200}{\ohm} + \qty{67}{\ohm} = \qty{267}{\ohm} $

Nous considérons maintenant la valeur la plus grande. Pour cela, nous posons :

$ R = \qty{1}{\kilo\ohm} $

Alors, $\qty{100}{\ohm}$ est en parallèle avec $\qty{200}{\ohm} + \qty{1}{\kilo\ohm}$, donc en parallèle avec $\qty{1200}{\ohm}$ :

$ R_\mathrm{par} = \frac{\qty{100}{\ohm} \cdot \qty{1200}{\ohm}}{\qty{100}{\ohm} + \qty{1200}{\ohm}} \approx \qty{92}{\ohm} $

Avec la résistance en amont, nous obtenons :

$ R_\mathrm{max} = \qty{200}{\ohm} + \qty{92}{\ohm} = \qty{292}{\ohm} $

La résistance d'entrée se situe donc dans la plage d'environ $\qtyrange{267}{292}{\ohm}$.