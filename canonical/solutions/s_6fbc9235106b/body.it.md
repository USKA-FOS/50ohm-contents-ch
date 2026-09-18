## Formule necessarie

Formule da utilizzare tratte dagli strumenti ausiliari dell’Agenzia federale delle reti per il calcolo della distanza di sicurezza nel campo lontano:


$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_{EIRP}}}{E}$ 

e per la relazione tra potenza EIRP e ERP:


$P_{EIRP} = P_{ERP} \cdot 10^{\frac{g_d + 2,15 - a}{10}}$


## Dati dal testo del problema

1. Poiché si tratta di un riflettore parabolico, vale: $g_d = \qty{18}{\dBd}$ 
2. Le perdite del cavo ammontano a: $a = \qty{2}{\dB}$
3. La potenza è: $P_{ERP} = \qty{40}{\watt}$
4. Il valore limite per la distanza di protezione personale è: $E = \qty{61}{\volt\per\meter}$


## Passaggi della soluzione

1. Calcolo di $P_{EIRP}$:


$P_{EIRP} = \qty{40}{\watt} \cdot 10^{\frac{18 + 2,15 - 2}{10}} = \qty{2612,52}{\watt}$


2. Calcolo della distanza di sicurezza $d$:


$d = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{2612,52}{\watt}}}{\qty{61}{\volt\per\meter}} = \frac{\qty{279,96}{\volt}}{\qty{61}{\volt\per\meter}} \approx \qty{4,6}{\meter}$



## Interpretazione

La distanza di sicurezza ammonta a $\qty{4,6}{\meter}$.