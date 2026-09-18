## Parte 1 dell'approccio alla soluzione
Dalla *raccolta di formule* negli strumenti ausiliari dell'Agenzia federale delle reti, nel capitolo "livello", si può desumere che un'attenuazione di $\qty{-6}{\dB}$ nel rapporto di potenza corrisponde a un fattore di 0,25.

In formule:

$P_{\qty{40}{^\circ}} = 0{,}25 \cdot P_\mathrm{EIRP}$

## Parte 2 dell'approccio alla soluzione
Dalla *raccolta di formule* negli strumenti ausiliari dell'Agenzia federale delle reti, nel capitolo "potenza irradiata e guadagno" delle antenne, si può desumere la seguente formula:

$E = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{d}$

Poiché si deve determinare una distanza di sicurezza, la formula deve essere risolta rispetto a $d$:

$d = \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}$

## Inserimento dei valori

$d_{\qty{40}{^\circ}} = \frac{\sqrt{\qty{30}{\ohm} \cdot P_{\qty{40}{^\circ}}}}{E} = \frac{\sqrt{\qty{30}{\ohm} \cdot 0,25 \cdot P_\mathrm{EIRP}}}{E} = \frac{\sqrt{0,25} \cdot \sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E} = \sqrt{0,25} \cdot \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E} = 0,5 \cdot \frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E} = 0,5 \cdot d$

## Interpretazione della formula

La distanza di sicurezza a $\qty{40}{^\circ}$ si dimezza rispetto alla distanza di sicurezza nella direzione di massima radiazione. 
Essa si riduce quindi dal valore predefinito di $\qty{20}{\meter}$ al valore cercato di $\qty{10}{\meter}$.