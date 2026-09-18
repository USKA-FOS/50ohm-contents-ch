Données :

$ U_\mathrm{CC} = \qty{9}{\volt} $

$ R_\text{BIAS} = \qty{470}{\ohm} $

D’après le circuit, on a également :

$ U_D = \qty{4}{\volt} $

La différence de tension aux bornes de la résistance $R_\text{BIAS}$ est donc :

$ U_{\text{BIAS}} = U_\mathrm{CC} - U_D = \qty{9}{\volt} - \qty{4}{\volt} = \qty{5}{\volt} $

Le courant traversant $R_\text{BIAS}$ et le MMIC est alors :

$ I_D = \frac{U_{\text{BIAS}}}{R_\text{BIAS}} = \frac{\qty{5}{\volt}}{\qty{470}{\ohm}} \approx \qty{10,6}{\milli\ampere} $

La puissance thermique dissipée dans le MMIC est :

$ P_D = U_D \cdot I_D = \qty{4}{\volt} \cdot \qty{10,6}{\milli\ampere} \approx \qty{42,6}{\milli\watt} $

En arrondissant, on obtient :

$ P_D \approx \qty{43}{\milli\watt} $