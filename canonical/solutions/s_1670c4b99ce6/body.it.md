## Formule necessarie

Formule da utilizzare dai sussidi della Bundesnetzagentur per il calcolo della distanza di sicurezza nel campo lontano:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$ 

o, in forma inversa:

$E = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{d}$ 

e per la relazione tra potenza EIRP ed ERP:

$P_\mathrm{EIRP} = P_{S} \cdot 10^{\frac{g_d + 2,15 - a}{10}}$

e inoltre:

$g_i = g_d + 2,15$


quindi:

$P_\mathrm{EIRP} = P_{S} \cdot 10^{\frac{g_i - a}{10}}$



## Dati del problema

1. Poiché si tratta di un’antenna Yagi-Uda, vale: $g_i = \qty{12,15}{\dBi}$ 
2. La potenza è: $P_{S} = \qty{250}{\watt}$
3. L’attenuazione del cavo è: $a = \qty{0}{\dB}$
3. La distanza è: $d = \qty{30}{\meter}$


## Passaggi della soluzione

1. Calcolo di $P_\mathrm{EIRP}$:


$P_\mathrm{EIRP} = \qty{250}{\watt} \cdot 10^{\frac{12,15 - 0}{10}} = \qty{4101,47}{\watt}$


2. Calcolo di $d$:


$E = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{4101,47}{\watt}}}{\qty{30}{\meter}} = \qty{11,7}{\volt\per\meter}$



## Interpretazione

L’intensità del campo elettrico calcolata è di $\qty{11,7}{\volt\per\meter}$.