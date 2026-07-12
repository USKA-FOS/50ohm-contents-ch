Poiché tutte le resistenze sono uguali, vale:

$ R_1 = R_2 = R_3 = \qty{10}{\kilo\ohm} $

Attraverso $R_3$ scorre una corrente di:

$ I_{R_3} = \qty{1}{\milli\ampere} $

Poiché $R_2$ e $R_3$ sono collegate in parallelo e hanno la stessa resistenza, attraverso $R_2$ scorre anch'essa:

$ I_{R_2} = \qty{1}{\milli\ampere} $

La corrente attraverso $R_1$ è la somma delle due correnti parziali:

$ I_{R_1} = I_{R_2} + I_{R_3} = \qty{1}{\milli\ampere} + \qty{1}{\milli\ampere} = \qty{2}{\milli\ampere} $

Ora viene calcolata prima la resistenza equivalente del collegamento in parallelo di $R_2$ e $R_3$:

$ R_{23} = \frac{R_2 \cdot R_3}{R_2 + R_3} = \frac{\qty{10}{\kilo\ohm} \cdot \qty{10}{\kilo\ohm}}
{\qty{10}{\kilo\ohm} + \qty{10}{\kilo\ohm}} = \qty{5}{\kilo\ohm} $

La resistenza totale del circuito è quindi:

$ R_\mathrm{ges} = R_1 + R_{23} = \qty{10}{\kilo\ohm} + \qty{5}{\kilo\ohm} = \qty{15}{\kilo\ohm} $

Con la corrente totale si ottiene la tensione totale:

$ U = I \cdot R = \qty{2}{\milli\ampere} \cdot \qty{15}{\kilo\ohm} = \qty{30}{\volt} $