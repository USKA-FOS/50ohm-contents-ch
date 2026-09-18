## Formule necessarie

Formule da utilizzare tratte dagli strumenti ausiliari della Bundesnetzagentur per il calcolo della distanza di sicurezza nel campo lontano:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 

e per la relazione di potenza tra EIRP e ERP:

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 10^{\frac{g_i - a}{10}}$

## Dati forniti dal testo del problema

1. Poiché si tratta di un dipolo, vale: $g_i = \qty{2,15}{\dBi}$ 
2. L’attenuazione del cavo è: $a = \qty{0,5}{\dB}$
3. La potenza è: $P_\mathrm{ERP} = \qty{300}{\watt}$
4. Il limite per la distanza di protezione delle persone è: $E = \qty{28}{\volt\per\metro}$

## Passaggi di soluzione

1. Calcolo di $P_\mathrm{EIRP}$:

$P_\mathrm{EIRP} = \qty{300}{\watt} \cdot 10^{\frac{2,15 - 0,5}{10}} = \qty{438,65}{\watt}$

2. Calcolo di $d$:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{438,65}{\watt}}}{\qty{28}{\volt\per\metro}} = \frac{\qty{114,71}{\volt}}{\qty{28}{\volt\per\metro}} \approx \qty{4,10}{\metro}$


## Interpretazione

La distanza di sicurezza richiesta è di $\qty{4,10}{\metro}$.

