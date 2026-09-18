## Formule necessarie

Formule da utilizzare dagli strumenti della Bundesnetzagentur per il calcolo della distanza di sicurezza nel campo lontano:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$

e per la relazione tra potenza EIRP e ERP:

$P_\mathrm{EIRP} = P_\mathrm{ERP} \cdot 10^{\frac{g_i - a}{10}}$


## Dati forniti dal testo del problema

1. Poiché si tratta di un dipolo a semionda, vale: $g_i = \qty{2,15}{\dBi}$
2. La perdita del cavo è trascurabile: $a = \qty{0,0}{\dB}$
3. La potenza di trasmissione è di 100 watt: $P_\mathrm{ERP} = \qty{100}{\watt}$
4. Il limite per la distanza di sicurezza per la protezione delle persone è: $E = \qty{28}{\volt\per\metro}$
5. Si considera la banda dei $\qty{10}{\metro}$: $\lambda = \qty{10}{\metro}$


## Passaggi della soluzione

1. Calcolo di $P_\mathrm{EIRP}$:

$P_\mathrm{EIRP} = \qty{100}{\watt} \cdot 10^{\frac{2{,}15 - 0{,}0}{10}} = \qty{100}{\watt} \cdot 10^{0{,}215} \approx \qty{164,1}{\watt}$

2. Calcolo della distanza di sicurezza $d$:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot \qty{164,1}{\watt}}}{\qty{28}{\volt\per\metro}} = \frac{\qty{70,2}{\volt}}{\qty{28}{\volt\per\metro}} \approx \qty{2,50}{\metro}$

3. Verifica della condizione di campo lontano:

$d > \frac{\lambda}{2\pi} = \frac{\qty{10}{\metro}}{2\pi} \approx \qty{1,59}{\metro}$


## Interpretazione

La condizione di campo lontano è soddisfatta per la banda dei $\qty{10}{\metro}$. La distanza di sicurezza è di $\qty{2,50}{\metro}$.