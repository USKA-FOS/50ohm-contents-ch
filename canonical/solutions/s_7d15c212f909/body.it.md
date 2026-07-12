Innanzitutto calcoliamo la corrente di base richiesta:

$I_B = \frac{I_C}{B} = \frac{\qty{2}{\milli\ampere}}{200} = \qty{10}{\micro\ampere}$

Attraverso la resistenza trasversale $R_2$ dovrebbe fluire dieci volte la corrente di base:

$I_2 = 10 \cdot I_B = \qty{100}{\micro\ampere}$

La corrente attraverso $R_1$ è composta dalla corrente attraverso $R_2$ e dalla corrente di base:

$I_1 = I_2 + I_B = \qty{100}{\micro\ampere} + \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$

Su $R_1$ cade la tensione di servizio meno la tensione base-emettitore:

$U_1 = \qty{10}{\volt} - \qty{0,6}{\volt} = \qty{9,4}{\volt}$

Ciò porta a:

$R_1 = \frac{U_1}{I_1} = \frac{\qty{9,4}{\volt}}{\qty{110}{\micro\ampere}} \approx \qty{85,5}{\kilo\ohm}$