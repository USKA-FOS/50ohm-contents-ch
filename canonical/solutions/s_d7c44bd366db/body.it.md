## Formule necessarie

Formule da utilizzare dai sussidi della Bundesnetzagentur per il calcolo della distanza di sicurezza nel campo lontano:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 

e per la relazione tra potenza EIRP ed ERP:

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 10^{\frac{g_d + 2{,}15 - a}{10}}$

## Riorganizzazione della formula

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 
$d \cdot E = \sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}$
$(d \cdot E)^2 = \qty{30}{\ohm} \cdot P_\mathrm{EIRP}$
$\frac{(d \cdot E)^2}{\qty{30}{\ohm}} = P_\mathrm{EIRP}$
$P_\mathrm{EIRP} = \frac{(d \cdot E)^2}{\qty{30}{\ohm}}$

## Dati forniti dal problema

1. Il guadagno d'antenna rispetto al dipolo: $g_d = \qty{6}{\dBd}$ 
2. L'attenuazione del cavo è trascurabile: $a = \qty{0}{\dB}$
3. La distanza di sicurezza è: $d = \qty{5}{\meter}$
4. Il limite per la distanza di protezione delle persone è: $E = \qty{28}{\volt\per\meter}$


## Passaggi di soluzione

1. Calcolo di $P_\mathrm{EIRP}$:

$P_\mathrm{EIRP} = \frac{(\qty{5}{\meter} \cdot \qty{28}{\volt\per\meter})^2}{\qty{30}{\ohm}} = \qty{653,33}{\watt}$

2. Calcolo di $P_\mathrm{ERP}$:

$P_\mathrm{ERP} = \frac{P_\mathrm{EIRP}}{10^{\frac{g_d + 2{,}15 -a}{10}}} = \frac{\qty{653,33}{\watt}}{10^{\frac{6 + 2{,}15 -0}{10}}} = \frac{\qty{653,33}{\watt}}{6,531} \approx \qty{100}{\watt}$

## Interpretazione

La potenza d’uscita massima del trasmettitore non deve superare circa $\qty{100}{\watt}$. 