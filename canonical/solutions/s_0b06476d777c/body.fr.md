## Formules requises

Formules à utiliser à partir des outils de l'Agence fédérale des réseaux pour calculer la distance de sécurité en champ lointain :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 

et pour la relation entre puissance EIRP et ERP :

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 10^{\frac{g_i - a}{10}}$

## Données issues de l'énoncé

1. Comme il s'agit d'un dipôle, on a : $g_i = \qty{2,15}{\dBi}$ 
2. L'affaiblissement du câble est de : $a = \qty{0,5}{\dB}$
3. La puissance est de : $P_\mathrm{ERP} = \qty{300}{\watt}$
4. La limite pour la distance de protection des personnes est de : $E = \qty{28}{\volt\per\meter}$

## Étapes de résolution

1. Calcul de $P_\mathrm{EIRP}$ :

$P_\mathrm{EIRP} = \qty{300}{\watt} \cdot 10^{\frac{2,15 - 0,5}{10}} = \qty{438,65}{\watt}$

2. Calcul de $d$ :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{438,65}{\watt}}}{\qty{28}{\volt\per\meter}} = \frac{\qty{114,71}{\volt}}{\qty{28}{\volt\per\meter}} \approx \qty{4,10}{\meter}$


## Interprétation

La distance de sécurité recherchée est de $\qty{4,10}{\meter}$.
