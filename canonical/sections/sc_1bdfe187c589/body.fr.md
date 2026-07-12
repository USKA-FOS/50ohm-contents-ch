Dans le cas des dipôles alimentés au centre dans l'espace libre, l'impédance d'alimentation est de $\qty{73,1}{\ohm}$, donc de l'ordre de $\qty{50}{\ohm}$ - mais pas exactement ! Cela s'applique également à une hauteur de montage d'une longueur d'onde ou plus.

<margin>
[picture:788:e_fusspunktimpedanz_dipol:Impédance de pied d'un dipôle en fonction de la hauteur de montage (Simulé avec NECPP)]
</margin>

[question:EG207]

En cas d'interaction avec le sol en raison d'une hauteur de montage plus faible, l'impédance d'alimentation d'un dipôle alimenté au centre se situe dans la plage de $\qty{40}{\ohm}$ à $\qty{90}{\ohm}$ comme le montre la figure [ref:e_fusspunktimpedanz_dipol]. 

[question:EG208]
[question:EG209]

Si l'on réalise un dipôle sous forme de dipôle plié, la tension appliquée est doublée en raison des sections d'antenne partiellement guidées en parallèle mais connectées en série, et le courant nécessaire est divisé par deux. Cela correspond à un quadruplement de l'impédance d'alimentation. C'est pourquoi un dipôle plié a une impédance de pied de $\qtyrange{240}{300}{\ohm}$.

[question:EG211]

---

Dans le cas d'une antenne Groundplane, en revanche, l'un des bras du dipôle est omis et remplacé par une terre avec une résistance aussi faible que possible. On obtient donc une résistance d'alimentation de $\frac{\qty{73,1}{\ohm}}{2} \approx \qty{37}{\ohm}$, ce qui correspond à la moitié de la résistance d'alimentation d'un dipôle dans l'espace libre. Dans le cas des antennes Groundplane avec des radiaux coudés à $\qty{45}{\degree}$ vers le bas, une résistance d'alimentation de exactement $\qty{50}{\ohm}$ résulte du rayonnement supplémentaire par le radial, de sorte qu'aucune adaptation supplémentaire aux câbles coaxiaux usuels n'est nécessaire. C'est pourquoi l'impédance de pied d'une Groundplane se situe entre $\qtyrange{30}{50}{\ohm}$.

<indepth>
En cas de mauvaise mise à la terre ou d'interaction avec le sol, une résistance d'alimentation supérieure à $\qty{37}{\ohm}$ peut également résulter pour une antenne Groundplane, même avec des radiaux posés horizontalement (par exemple sur la surface de la terre). La résistance supplémentaire résulte alors des pertes au sol.
</indepth>

[question:EG211]