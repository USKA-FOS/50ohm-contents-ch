## Formules nécessaires

Formules à utiliser issues des outils de la Bundesnetzagentur pour le calcul de la distance de sécurité en champ lointain :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 

et pour la relation de puissance entre EIRP et ERP :

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 10^{\frac{g_d + 2{,}15 - a}{10}}$

## Réarrangement de la formule

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 
$d \cdot E = \sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}$
$(d \cdot E)^2 = \qty{30}{\ohm} \cdot P_\mathrm{EIRP}$
$\frac{(d \cdot E)^2}{\qty{30}{\ohm}} = P_\mathrm{EIRP}$
$P_\mathrm{EIRP} = \frac{(d \cdot E)^2}{\qty{30}{\ohm}}$

## Données issues de l'énoncé

1. Le gain d'antenne indiqué par rapport au dipôle : $g_d = \qty{6}{\dBd}$ 
2. L'atténuation du câble est négligeable : $a = \qty{0}{\dB}$
3. La distance de sécurité est de : $d = \qty{5}{\meter}$
4. La limite pour la distance de protection des personnes est : $E = \qty{28}{\volt\per\meter}$


## Étapes de résolution

1. Calcul de $P_\mathrm{EIRP}$ :

$P_\mathrm{EIRP} = \frac{(\qty{5}{\meter} \cdot \qty{28}{\volt\per\meter})^2}{\qty{30}{\ohm}} = \qty{653,33}{\watt}$

2. Calcul de $P_\mathrm{ERP}$ :

$P_\mathrm{ERP} = \frac{P_\mathrm{EIRP}}{10^{\frac{g_d + 2{,}15 -a}{10}}} = \frac{\qty{653,33}{\watt}}{10^{\frac{6 + 2{,}15 -0}{10}}} = \frac{\qty{653,33}{\watt}}{6,531} \approx \qty{100}{\watt}$

## Interprétation

La puissance de sortie maximale de l'émetteur ne doit pas dépasser environ $\qty{100}{\watt}$. 