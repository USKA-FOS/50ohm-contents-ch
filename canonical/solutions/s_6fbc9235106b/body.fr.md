## Formules nécessaires

Formules à utiliser issues des outils de la Bundesnetzagentur pour le calcul de la distance de sécurité en champ lointain :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}$ 

et pour la relation entre puissance EIRP et ERP :

$P_{EIRP} = P_{ERP} \cdot 10^{\frac{g_d + 2,15 - a}{10}}$


## Données issues de l’énoncé

1. Comme il s’agit d’un réflecteur parabolique, on a : $g_d = \qty{18}{\dBd}$ 
2. L’atténuation des câbles s’élève à : $a = \qty{2}{\dB}$
3. La puissance est de : $P_{ERP} = \qty{40}{\watt}$
4. La valeur limite pour la distance de sécurité liée à la protection des personnes est : $E = \qty{61}{\volt\per\meter}$


## Étapes de résolution

1. Calcul de $P_{EIRP}$ :

$P_{EIRP} = \qty{40}{\watt} \cdot 10^{\frac{18 + 2,15 - 2}{10}} = \qty{2612,52}{\watt}$


2. Calcul de la distance de sécurité $d$ :

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{2612,52}{\watt}}}{\qty{61}{\volt\per\meter}} = \frac{\qty{279,96}{\volt}}{\qty{61}{\volt\per\meter}} \approx \qty{4,6}{\meter}$


## Interprétation

La distance de sécurité s’élève à $\qty{4,6}{\meter}$.