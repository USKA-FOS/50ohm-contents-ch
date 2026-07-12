% TODO reformuler
% Idée DL9MJ : exemple avec une image, chaque bit dans I et Q et comment le signal pour 00, 01, 10, 11 apparaît

La QAM peut être générée particulièrement simplement à l'aide de deux porteuses de même fréquence. L'une des deux porteuses doit être déphasée de $\qty{90}{\degree}$. Les deux porteuses sont ensuite modulées en amplitude chacune avec un signal propre. L'un des signaux est appelé I (pour In-Phase Component) et l'autre signal est appelé Q (pour Quadrature Phase Component). La porteuse déphasée est modulée avec le signal Q. Ensuite, les deux porteuses modulées sont superposées, ce qui donne une porteuse qui change à la fois en amplitude et en phase.

<indepth>
[include:applet_iq]
</indepth>
  
%TODO IMAGE QAM4 QAM8 ou plus ?

[question:AE404]
[question:AF632]

L'idée de base de traiter un signal en deux parties séparément trouve également une large application dans le traitement numérique des signaux. Elle est désignée comme procédé I/Q après les deux signaux partiels. Le procédé I/Q permet de générer n'importe quel signal. À cet effet, le flux de données à moduler se compose d'une partie I et d'une partie Q. Deux convertisseurs N/A convertissent chacun une des deux parties en un signal I ou Q analogique. Avec le signal I et le signal Q, les deux porteuses déphasées sont à nouveau modulées. Dans la dernière étape, celles-ci sont superposées pour former une porteuse qui est émise.

De même, la procédure est suivie du côté du récepteur. Le signal d'entrée est mélangé avec une porteuse pour obtenir le signal I, qui est ensuite converti en partie I d'un flux de données au moyen d'un convertisseur A/N. Simultanément, le signal d'entrée est également mélangé avec une porteuse déphasée de $\qty{90}{\degree}$ pour obtenir le signal Q, qui est à son tour converti en partie Q du flux de données au moyen d'un convertisseur A/N.

[question:AF633]

Un tel flux de données numériques peut toujours représenter une certaine bande de fréquences du signal d'entrée, qui se situe autour d'une fréquence centrale. Si le signal d'entrée est par exemple mélangé avec une porteuse de $\qty{435}{\mega\hertz}$ et une porteuse de $\qty{435}{\mega\hertz}$ déphasée de $\qty{90}{\degree}$ et que les deux signaux résultants sont numérisés par des convertisseurs A/N, alors le flux de données I/Q résultant représente la bande de fréquences autour de $\qty{435}{\mega\hertz}$.

% TODO Référence au théorème d'échantillonnage ?
La bande passante couverte dépend de la fréquence d'échantillonnage de la conversion A/N. La bande passante en Hz correspond à la fréquence d'échantillonnage en échantillons par seconde. Si, dans notre exemple, à la fois la partie I et la partie Q sont échantillonnées à 10 millions d'échantillons par seconde, alors le flux de données I/Q résultant peut couvrir une bande de fréquences de $\qty{10}{\mega\hertz}$, c'est-à-dire de $\qty{-5}{\mega\hertz}$ à $\qty{+5}{\mega\hertz}$ par rapport à la fréquence centrale. Le flux de données couvre alors les fréquences de $\qty{430}{\mega\hertz}$ à $\qty{440}{\mega\hertz}$.

[question:AF634]
[question:AF635]
[question:AF636]
