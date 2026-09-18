Dans un chapitre précédent, nous avons abordé la représentation I/Q et le modulateur I/Q. Dans un système numérique, les deux composantes I et Q sont traitées comme deux flux de données numériques distincts. Ceux-ci peuvent être générés, modifiés et évalués par un traitement numérique du signal.

Du côté récepteur, le signal d'entrée est mélangé avec deux signaux de même fréquence, déphasés de $\qty{90}{\degree}$ l'un par rapport à l'autre. Cela produit un signal I et un signal Q. Ces deux signaux sont ensuite numérisés chacun par un convertisseur numérique et peuvent ensuite être traités numériquement. Du côté émetteur, le processus fonctionne à l'inverse : les flux de données numériques I et Q sont convertis en signaux analogiques par deux convertisseurs numérique-analogique et ensuite transmis à un modulateur I/Q.

Un flux de données I/Q numérique peut représenter une bande de fréquences autour d'une fréquence centrale donnée. Les fréquences inférieures à la fréquence centrale sont décrites par des écarts de fréquence négatifs, tandis que les fréquences supérieures sont représentées par des écarts positifs.

Si un signal d'entrée est par exemple mélangé avec deux signaux déphasés de $\qty{90}{\degree}$ à $\qty{435}{\mega\hertz}$ chacun, le flux de données I/Q résultant représente une bande de fréquences autour de la fréquence centrale de $\qty{435}{\mega\hertz}$.

L'étendue de cette bande de fréquences dépend de la fréquence d'échantillonnage. Si I et Q sont échantillonnés chacun à une fréquence d'échantillonnage de $f_\mathrm{S}$, une bande de fréquences allant de

$-\frac{f_\mathrm{S}}{2}\text{ à }+\frac{f_\mathrm{S}}{2}$

autour de la fréquence centrale peut idéalement être représentée. La bande passante totale correspond donc à la fréquence d'échantillonnage $f_\mathrm{S}$.

Si I et Q sont par exemple échantillonnés chacun à $\qty{10}{\mega\sample\per\second}$, le flux de données I/Q peut représenter une bande de fréquences de $\qty{-5}{\mega\hertz}$ à $\qty{+5}{\mega\hertz}$ autour de la fréquence centrale. Avec une fréquence centrale de $\qty{435}{\mega\hertz}$, cela correspond à une bande de fréquences de $\qty{430}{\mega\hertz}$ à $\qty{440}{\mega\hertz}$.

[question:AF634]
[question:AF635]
[question:AF636]