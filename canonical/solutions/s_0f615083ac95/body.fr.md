Pour la BLU USB, la bande latérale supérieure doit se situer dans la bande passante du **filtre à quartz de $\qty{9}{\mega\hertz}$**.

[picture:941:a_balancemodulator_usb:Modulateur équilibré avec porteuse supprimée et filtre à quartz pour USB]
[picture:941:a_balancemodulator_lsb:Modulateur équilibré avec porteuse supprimée et filtre à quartz pour LSB]

Le filtre à quartz a une largeur d’environ $\qty{3}{\kilo\hertz}$. Ses limites de filtrage se situent donc environ $\qty{1,5}{\kilo\hertz}$ en dessous et au-dessus de la fréquence centrale de $\qty{9}{\mega\hertz}$.

Pour la LSB, la fréquence de la porteuse supprimée est placée à la limite supérieure du filtre. La bande latérale inférieure se retrouve alors dans la bande passante du filtre.

Pour la USB, la fréquence de la porteuse supprimée est placée à la limite inférieure du filtre. La bande latérale supérieure se retrouve alors dans la bande passante du filtre :


$f_\mathrm{OSZ} = \qty{9}{\mega\hertz} - \qty{1,5}{\kilo\hertz} = \qty{8,9985}{\mega\hertz}$


Avec le signal BF, on mélange ainsi une fréquence d’oscillateur de $\qty{8,9985}{\mega\hertz}$.