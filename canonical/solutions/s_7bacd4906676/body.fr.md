La connexion au centre garantit que les deux points centraux sont électriquement identiques.

Cela signifie que :

* $R_1$ et $R_3$ sont en parallèle entre a et le point central
* $R_2$ et $R_4$ sont en parallèle entre le point central et b

Le circuit se compose donc de deux montages en parallèle qui sont ensuite en série.

On commence par regrouper $R_1$ et $R_3$ :

$ R_{13} = \frac{R_1 \cdot R_3}{R_1 + R_3} $

Comme les deux résistances sont de même valeur :

$ R_{13} = \frac{\qty{2,2}{\kilo\ohm}}{2} = \qty{1,1}{\kilo\ohm} $

On regroupe ensuite $R_2$ et $R_4$ :

$ R_{24} = \frac{R_2 \cdot R_4}{R_2 + R_4} $

Ces résistances sont également de même valeur :

$ R_{24} = \frac{\qty{220}{\ohm}}{2} = \qty{110}{\ohm} $

Les deux résistances équivalentes sont en série :

$ R_\mathrm{ges} = R_{13} + R_{24} = \qty{1100}{\ohm} + \qty{110}{\ohm} = \qty{1210}{\ohm} $