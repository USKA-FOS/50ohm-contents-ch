Ce circuit fonctionne en tant que doubleur de tension ou détecteur de crête à crête. Il capte l’amplitude positive et négative du signal HF, de sorte qu’en sortie, on obtient approximativement la tension crête à crête moins les chutes de tension directe des deux diodes.

$U_{\mathrm{SS}} = \qty{15,3}{\volt} + 2 \cdot \qty{0,23}{\volt} = \qty{15,76}{\volt}$


D’après


$U_{\mathrm{SS}} = 2 \cdot \hat{U}$


on en déduit la valeur de crête de la tension HF à la prise intermédiaire de $\qty{5}{\ohm}$ :


$\hat{U} = \frac{U_{\mathrm{SS}}}{2} = \qty{7,88}{\volt}$


La tension est mesurée sur une prise intermédiaire de $\qty{5}{\ohm}$ d’une charge fictive de $\qty{50}{\ohm}$ au total. Comme le même courant circule dans toute la charge fictive, les tensions sont proportionnelles aux résistances. La tension de crête HF aux bornes de la charge fictive complète s’élève donc à :


$\hat{U}_{\mathrm{Émetteur}} = \frac{\qty{50}{\ohm}}{\qty{5}{\ohm}} \cdot \hat{U} = 10 \cdot \qty{7,88}{\volt} = \qty{78,8}{\volt}$


Avec


$\hat{U} = U_{\mathrm{eff}} \cdot \sqrt{2}$

et


$P = \frac{U_{\mathrm{eff}}^2}{R}$


on obtient :


$P = \frac{\hat{U}_{\mathrm{Émetteur}}^2}{2R} = \frac{(\qty{78,8}{\volt})^2}{2 \cdot \qty{50}{\ohm}} \approx \qty{62}{\watt}$


La puissance HF de l’émetteur est donc d’environ $\qty{60}{\watt}$.