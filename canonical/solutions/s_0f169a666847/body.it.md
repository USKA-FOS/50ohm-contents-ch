Come mostrato nel circuito, per la frequenza di uscita del VCO nello stato agganciato della PLL vale:

$f_{VCO} = n \cdot f_A$

Riorganizzando rispetto al rapporto di divisione *n* si ottiene:

$n = \frac{f_{VCO}}{f_A}$

Per il *limite inferiore* della banda di uscita desiderata con $f_{VCO} = \qty{12,000}{\mega\hertz}$ e $f_A = \qty{12,5}{\kilo\hertz}$ si ha:

$n_{min} = \frac{\qty{12000000}{\hertz}}{\qty{12500}{\hertz}} = 960$

Per il *limite superiore* con $f_{VCO} = \qty{14,000}{\mega\hertz}$ si ottiene:

$n_{max} = \frac{\qty{14000000}{\hertz}}{\qty{12500}{\hertz}} = 1120$

Il rapporto di divisione *n* deve quindi variare nell'intervallo da *960* a *1120*.