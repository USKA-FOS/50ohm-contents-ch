## Formules nécessaires

Formules à utiliser issues des outils de la Bundesnetzagentur pour le calcul de la distance de sécurité en champ lointain :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$

et pour la relation entre puissance EIRP et ERP :

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 10^{\frac{g_i - a}{10}}$


## Données issues de l’énoncé

1. L’antenne étant un dipôle demi-onde, on a : $g_i = \qty{2,15}{\dBi}$
2. L’affaiblissement du câble est négligeable : $a = \qty{0,0}{\dB}$
3. La puissance d’émission est de 100 watts : $P_\mathrm{ERP} = \qty{100}{\watt}$
4. La limite pour la distance de sécurité est : $E = \qty{28}{\volt\per\meter}$
5. On considère la bande des $\qty{10}{\meter}$ : $\lambda = \qty{10}{\meter}$


## Étapes de résolution

1. Calcul de $P_\mathrm{EIRP}$ :

$P_\mathrm{EIRP} = \qty{100}{\watt} \cdot 10^{\frac{2{,}15 - 0{,}0}{10}} = \qty{100}{\watt} \cdot 10^{0{,}215} \approx \qty{164,1}{\watt}$

2. Calcul de la distance de sécurité $d$ :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{164,1}{\watt}}}{\qty{28}{\volt\per\meter}} = \frac{\qty{70,2}{\volt}}{\qty{28}{\volt\per\meter}} \approx \qty{2,50}{\meter}$

3. Vérification de la condition de champ lointain :

$d > \frac{\lambda}{2\pi} = \frac{\qty{10}{\meter}}{2\pi} \approx \qty{1,59}{\meter}$


## Interprétation

La condition de champ lointain est respectée pour la bande des $\qty{10}{\meter}$. La distance de sécurité est de $\qty{2,50}{\meter}$.