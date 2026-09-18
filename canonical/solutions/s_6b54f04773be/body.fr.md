## Formules nécessaires

Formules à utiliser à partir des outils de l’Agence fédérale des réseaux pour calculer la distance de sécurité en champ lointain :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 

et pour la relation de puissance entre EIRP et ERP :

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 10^{\frac{g_d + 2{,}15 - a}{10}}$

## Données issues de l’énoncé

1. Comme il s’agit d’une antenne Yagi-Uda, on a : $g_d = \qty{10,5}{\dBd}$ 
2. L’atténuation du câble est de : $a = \qty{1,5}{\dB}$
3. La puissance est de : $P_\mathrm{ERP} = \qty{100}{\watt}$
4. La valeur limite pour la distance de protection des personnes est : $E = \qty{28}{\volt\per\meter}$

## Étapes de résolution

1. Calcul de $P_\mathrm{EIRP}$ :

$P_\mathrm{EIRP} = \qty{100}{\watt} \cdot 10^{\frac{10,5 + 2,15 - 1,5}{10}} = \qty{1303,17}{\watt}$

2. Calcul de la distance de sécurité $d$ :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1303,17}{\watt}}}{\qty{28}{\volt\per\meter}} = \frac{\qty{197,72}{\volt}}{\qty{28}{\volt\per\meter}} = \qty{7,06}{\meter}$


## Interprétation

La distance de sécurité déterminée est de $\qty{7,06}{\meter}$.

