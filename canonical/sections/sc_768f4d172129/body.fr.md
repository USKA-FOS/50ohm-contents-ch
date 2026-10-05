%TODO Vérifier les références de section. Peut-être en faut-il deux.
%TODO Corriger la coquille existante pour Mega. Sample.
%
Dans la section [sec:iq_verfahren], nous avons appris la représentation I/Q et le modulateur I/Q. Dans un système numérique, les deux composantes I et Q sont traitées comme deux flux de données numériques séparés. Ceux-ci peuvent être générés, modifiés et évalués par traitement numérique du signal.

Du côté récepteur, le signal d'entrée est mélangé avec deux signaux de même fréquence, déphasés de $\qty{90}{\degree}$ l'un par rapport à l'autre. Cela produit un signal I et un signal Q. Les deux signaux sont ensuite numérisés chacun par un convertisseur A/D et peuvent ensuite être traités numériquement. Du côté émetteur, le processus fonctionne à l'inverse : les flux de données numériques I et Q sont convertis en signaux analogiques par deux convertisseurs D/A et ensuite fournis à un modulateur I/Q.

Un flux de données numérique I/Q peut représenter une bande de fréquences autour d'une fréquence centrale spécifique. Les fréquences inférieures à la fréquence centrale sont décrites par des déviations de fréquence négatives et les fréquences supérieures par des déviations positives.

Si un signal d'entrée est mélangé, par exemple, avec deux signaux de $\qty{435}{\mega\hertz}$ chacun, déphasés de $\qty{90}{\degree}$ l'un par rapport à l'autre, le flux de données I/Q qui en résulte représente une bande de fréquences autour de la fréquence centrale de $\qty{435}{\mega\hertz}$.

La taille de cette bande de fréquences dépend de la fréquence d'échantillonnage. Si I et Q sont échantillonnés avec une fréquence d'échantillonnage de $f_\mathrm{S}$, idéalement une bande de fréquences de

$-\frac{f_\mathrm{S}}{2}\text{ à }+\frac{f_\mathrm{S}}{2}$

autour de la fréquence centrale peut être représentée. La bande passante totalement représentable correspond ainsi à la fréquence d'échantillonnage $f_\mathrm{S}$.

Si, par exemple, I et Q sont échantillonnés chacun à $\qty{10}{\mega sample\per\second}$, le flux de données I/Q peut représenter une bande de fréquences de $\qty{-5}{\mega\hertz}$ à $\qty{+5}{\mega\hertz}$ autour de la fréquence centrale. Pour une fréquence centrale de $\qty{435}{\mega\hertz}$, cela correspond à une bande de fréquences de $\qty{430}{\mega\hertz}$ à $\qty{440}{\mega\hertz}$.

[question:AF634]
[question:AF635]
[question:AF636]
