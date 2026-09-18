In una sintesi di frequenza PLL, la frequenza di uscita del VCO nel ramo di retroazione viene divisa per *n* tramite il divisore e confrontata al rilevatore di fase $\varphi$ con la frequenza di riferimento nel punto A.

Il circuito di controllo garantisce che, al rilevatore di fase, le due frequenze di ingresso siano uguali:

$f_A = \frac{f_{VCO}}{n}$

o, equivalentemente,

$f_{VCO} = n \cdot f_A$

Il fattore di divisione *n* viene impostato tramite gli ingressi B e C ed è sempre un *numero intero*. Se *n* viene aumentato di esattamente 1, la frequenza di uscita aumenta di esattamente $f_A$:

$\Delta f_{VCO} = (n+1) \cdot f_A - n \cdot f_A = f_A$

Il più piccolo passo di frequenza possibile all'uscita – cioè la *spaziatura dei canali* – corrisponde quindi direttamente alla frequenza di riferimento nel punto A.

Poiché è richiesta una spaziatura dei canali di $\qty{12,5}{\kilo\hertz}$, la frequenza nel punto A deve essere anch'essa

$f_A = \qty{12,5}{\kilo\hertz}$
