Dati:

$ U = \qty{15}{\volt} $

e

$ R_1 = R_2 = R_3 = \qty{10}{\kilo\ohm} $

Innanzitutto, viene calcolata la resistenza equivalente della connessione in parallelo di $R_2$ e $R_3$:

$ R_{23} = \frac{R_2 \cdot R_3}{R_2 + R_3} $

Poiché entrambe le resistenze hanno la stessa grandezza, si ottiene:

$ R_{23} = \qty{5}{\kilo\ohm} $

La resistenza totale del circuito è quindi:

$ R_\mathrm{ges} = R_1 + R_{23} = \qty{10}{\kilo\ohm} + \qty{5}{\kilo\ohm} = \qty{15}{\kilo\ohm} $

Ora è possibile calcolare la corrente totale:

$ I_\mathrm{ges} = \frac{U}{R_\mathrm{ges}} = \frac{\qty{15}{\volt}}{\qty{15}{\kilo\ohm}} = \qty{1}{\milli\ampere} $

Questa corrente scorre inizialmente attraverso $R_1$ e poi si divide nei due resistori di uguale grandezza $R_2$ e $R_3$.

Poiché entrambe le resistenze hanno la stessa grandezza, attraverso ogni ramo scorre esattamente la metà della corrente totale:

$ I_3 = \frac{I_\mathrm{ges}}{2} = \frac{\qty{1}{\milli\ampere}}{2} = \qty{0,5}{\milli\ampere} $