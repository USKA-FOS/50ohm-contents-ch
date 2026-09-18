Pour un dipôle demi-onde résonant, alimenté au centre, dans l’espace libre, l’impédance d’alimentation idéale est d’environ $\qty{73,1}{\ohm}$, soit approximativement $\qty{75}{\ohm}$. Cette valeur est déjà proche des $\qty{50}{\ohm}$ souhaités, mais ne correspond pas exactement. Si un tel dipôle est directement alimenté par une ligne d’alimentation de $\qty{50}{\ohm}$, il en résulte un léger déséquilibre d’adaptation. Pour une transmission optimale de puissance ou un ROS aussi bas que possible, une adaptation peut donc être judicieuse même pour un dipôle. Cela s’applique également en général pour des hauteurs de montage d’environ une longueur d’onde ou plus, l’impédance d’alimentation réelle pouvant légèrement varier en fonction du diamètre du fil, de l’environnement et de la hauteur de montage, comme nous allons le voir.


<margin>
[picture:788:e_fusspunktimpedanz_dipol:Impédance au point d’alimentation d’un dipôle en fonction de la hauteur de montage (simulé avec NECPP)]
</margin>

[question:EG207]


En cas d’interaction avec le sol en raison d’une faible hauteur de montage, l’impédance d’alimentation d’un dipôle alimenté au centre varie entre $\qty{40}{\ohm}$ et $\qty{90}{\ohm}$, comme illustré dans le graphique [ref:e_fusspunktimpedanz_dipol].


[question:EG208]
[question:EG209]


Si l’on réalise un dipôle en tant que dipôle replié, la tension appliquée est doublée en raison des sections d’antenne en série mais partiellement en parallèle, et le courant nécessaire est divisé par deux. Cela correspond à une multiplication par quatre de l’impédance d’alimentation. Un dipôle replié a donc une impédance au point d’alimentation de $\qtyrange{240}{300}{\ohm}$.

[question:EG210]

---

Pour une antenne Groundplane, un des brins du dipôle est supprimé et remplacé par une terre présentant une résistance aussi faible que possible. On obtient ainsi une impédance d’alimentation de $\frac{\qty{73,1}{\ohm}}{2} \approx \qty{37}{\ohm}$, soit la moitié de l’impédance d’alimentation d’un dipôle dans l’espace libre. Pour les antennes Groundplane avec des radiales inclinées de $\qty{45}{\degree}$ vers le bas, l’impédance d’alimentation est exactement de $\qty{50}{\ohm}$ grâce au rayonnement supplémentaire des radiales, ce qui rend toute adaptation supplémentaire à des câbles coaxiaux classiques inutile. L’impédance au point d’alimentation d’une antenne Groundplane se situe donc entre $\qtyrange{30}{50}{\ohm}$.


<indepth>
En cas de mauvaise mise à la terre ou d’interaction avec le sol, l’impédance d’alimentation d’une antenne Groundplane peut également dépasser $\qty{37}{\ohm}$ même avec des radiales posées horizontalement (par exemple sur la surface de la terre). La résistance supplémentaire provient alors des pertes dans le sol.
</indepth>

[question:EG211]