## Formules nécessaires

Formules à utiliser issues des aides de la Bundesnetzagentur pour le calcul de la distance de sécurité en champ lointain :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 

ou, réarrangé :

$E = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{d}$ 

et pour la relation de puissance entre EIRP et ERP :

$P_\mathrm{EIRP} = P_{S} \cdot 10^{\frac{g_d + 2,15 - a}{10}}$

ainsi que :

$g_i = g_d + 2,15$

d’où :

$P_\mathrm{EIRP} = P_{S} \cdot 10^{\frac{g_i - a}{10}}$


## Données issues de l’énoncé

1. Comme il s’agit d’une antenne Yagi-Uda, on a : $g_i = \qty{12,15}{\dBi}$ 
2. La puissance est de : $P_{S} = \qty{250}{\watt}$
3. L’atténuation du câble est de : $a = \qty{0}{\dB}$
3. La distance est de : $d = \qty{30}{\m}$

## Étapes de résolution

1. Calcul de $P_\mathrm{EIRP}$ :

$P_\mathrm{EIRP} = \qty{250}{\watt} \cdot 10^{\frac{12,15 - 0}{10}} = \qty{4101,47}{\watt}$

2. Calcul de $E$ :

$E = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{4101,47}{\watt}}}{\qty{30}{\m}} = \qty{11,7}{\volt\per\m}$


## Interprétation

L’intensité du champ électrique déterminée est de $\qty{11,7}{\volt\per\m}$.