## Formule necessarie

Formule da utilizzare dai materiali ausiliari dell’Agenzia federale delle reti per il calcolo della distanza di sicurezza nel campo lontano:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 

ed il rapporto di potenza tra EIRP e ERP:

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 10^{\frac{g_d + 2{,}15 - a}{10}}$

## Dati forniti dal testo del problema

1. Poiché si tratta di un’antenna Yagi-Uda, vale: $g_d = \qty{11,5}{\dBd}$ 
2. L’attenuazione del cavo è: $a = \qty{1,5}{\dB}$
3. La potenza è: $P_\mathrm{ERP} = \qty{75}{\watt}$
4. Il limite per la distanza di protezione delle persone è: $E = \qty{28}{\volt\per\metro}$

## Passaggi di soluzione

1. Calcolo di $P_\mathrm{EIRP}$:

$P_\mathrm{EIRP} = \qty{75}{\watt} \cdot 10^{\frac{11,5 + 2,15 - 1,5}{10}} = \qty{1230,44}{\watt}$

2. Calcolo della distanza di sicurezza $d$:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{1230,44}{\watt}}}{\qty{28}{\volt\per\metro}} = \frac{\qty{192,12}{\volt}}{\qty{28}{\volt\per\metro}} = \qty{6,86}{\metro}$

## Interpretazione

La distanza di sicurezza calcolata è di $\qty{6,86}{\metro}$.
