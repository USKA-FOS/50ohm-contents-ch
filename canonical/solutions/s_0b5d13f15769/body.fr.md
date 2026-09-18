## Première partie de la démarche de résolution
D'après le *recueil de formules* dans les outils auxiliaires de l'Agence fédérale des réseaux, on peut lire dans le chapitre « niveau » qu'une atténuation de $\qty{-6}{\dB}$ correspond à un facteur de 0,25 dans le rapport de puissance.

Exprimé sous forme de formule :

$P_{\qty{40}{^\circ}} = 0{,}25 \cdot P_\mathrm{EIRP}$

## Deuxième partie de la démarche de résolution
D'après le *recueil de formules* dans les outils auxiliaires de l'Agence fédérale des réseaux, on peut trouver dans le chapitre « puissance rayonnée et gain » des antennes la formule suivante :

$E = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{d}$

Comme on souhaite déterminer une distance de sécurité, il faut réarranger la formule pour isoler $d$ :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$

## Substitution

$d_{\qty{40}{^\circ}} = \frac{\sqrt{\qty{30}{\ohm} \cdot P_{\qty{40}{^\circ}}}}{E} = \frac{\sqrt{\qty{30}{\ohm} \cdot 0,25 \cdot P_\mathrm{EIRP}}}{E} = \frac{\sqrt{0,25} \cdot \sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E} = \sqrt{0,25} \cdot \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E} = 0,5 \cdot \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E} = 0,5 \cdot d$

## Interprétation de la formule

La distance de sécurité à $\qty{40}{^\circ}$ est divisée par deux par rapport à la distance de sécurité dans la direction du rayonnement principal. Elle passe ainsi de la valeur prédéfinie de $\qty{20}{\meter}$ à la valeur recherchée de $\qty{10}{\meter}$.