A causa del principio di funzionamento, in un ricevitore supereterodina (vedi figura [ref:spiegelfrequenzen_mischen1]) il processo di miscelazione con la frequenza dell’oscillatore del ricevitore genera sempre due possibili frequenze di ricezione:

$f_\text{ZF} = \left|f_\text{e} \pm f_\text{o}\right|$

Poiché nel ricevitore supereterodina si desidera convertire verso il basso a una frequenza intermedia più bassa, è particolarmente interessante la frequenza di differenza:

$f_\text{ZF} = \left|f_\text{e} - f_\text{o}\right|$

Il valore assoluto è determinante: per una frequenza dell’oscillatore $f_\text{o}$ e una frequenza intermedia $f_\text{ZF}$ fisse, esistono due possibili frequenze di ricezione che generano entrambe la stessa frequenza intermedia. Una di queste è la frequenza di ricezione desiderata, mentre l’altra viene chiamata *frequenza immagine*.

<margin>
[picture:807:spiegelfrequenzen_mischen1:Processo di miscelazione con frequenza di ricezione $f_\text{e}$, frequenza dell’oscillatore $f_\text{o}$ e frequenza intermedia $f_\text{ZF}$]
</margin>

---

<margin>
[picture:806:spiegelfrequenzen_fe1_fe2:Frequenze di ricezione che portano entrambe alla stessa $f_\text{ZF}$]
</margin>

Esempio: Supponiamo che il nostro oscillatore oscilli, come mostrato nella figura [ref:spiegelfrequenzen_fe1_fe2], alla frequenza $f_\text{o}=\qty{3,955}{\mega\hertz}$. La frequenza intermedia $f_\text{ZF}$ deve essere $\qty{0,455}{\mega\hertz}$. Grazie al valore assoluto nella formula, esistono ora due possibilità per le frequenze di ricezione che si possono ascoltare, ovvero $f_\text{e1} = \qty{3,500}{\mega\hertz}$ e $f_\text{e2} = \qty{4,410}{\mega\hertz}$. Per entrambi i valori, la formula restituisce la frequenza intermedia $f_\text{ZF}$.

Se $f_\text{e1}$ è la frequenza di ricezione desiderata, allora $f_\text{e2}$ viene chiamata frequenza immagine di $f_\text{e1}$. Se $f_\text{e2}$ è la frequenza di ricezione desiderata, allora $f_\text{e1}$ viene chiamata frequenza immagine di $f_\text{e2}$.

La distanza tra la frequenza di ricezione desiderata e la frequenza immagine è sempre pari al doppio della frequenza intermedia (IF), come si può facilmente vedere nella figura [ref:spiegelfrequenzen_fe1_fe2].

Se l’oscillatore oscilla *sopra* la frequenza di ricezione ($f_\mathrm{E} < f_\mathrm{OSZ}$), anche la frequenza immagine si trova *sopra* la frequenza di ricezione di una quantità pari al doppio della IF ($f_\mathrm{S} = f_\mathrm{E} + 2\cdot f_\mathrm{ZF}$).

Se invece l’oscillatore si trova *sotto* la frequenza di ricezione ($f_\mathrm{E} > f_\mathrm{OSZ}$), anche la frequenza immagine si trova *sotto* la frequenza di ricezione di una quantità pari al doppio della IF ($f_\mathrm{S} = f_\mathrm{E} - 2\cdot f_\mathrm{ZF}$). Questo rapporto è riportato anche nella raccolta di formule.

Ora prova a risolvere le seguenti domande con queste informazioni.

[question:AF106]
[question:AF201]
[question:AF202]
[question:AF203]
[question:AF107]
[question:AF108]

---
<margin>
[picture:808:spiegelfrequenzen_mischen2:Filtro passa-banda aggiuntivo per la soppressione della frequenza immagine]
</margin>

La frequenza immagine, se non viene sufficientemente soppressa, può causare disturbi di ricezione, poiché i segnali sulla frequenza immagine vengono anch’essi convertiti alla stessa frequenza intermedia e possono quindi essere udibili nel ricevitore. Per evitarlo, la frequenza di ricezione desiderata viene selezionata, come mostrato nella figura [ref:spiegelfrequenzen_mischen2], già prima del mixer tramite un filtro passa-banda. La frequenza immagine deve essere il più possibile attenuata.

Per una soppressione efficace della frequenza immagine, è vantaggioso che ci sia una distanza il più possibile grande tra la frequenza di ricezione desiderata e la frequenza immagine. Questa distanza aumenta se si sceglie una frequenza intermedia più alta.

Questo può essere osservato anche nella figura [ref:spiegelfrequenzen_fe1_fe2]: all’aumentare della IF, le due possibili frequenze di ricezione $f_\text{e1}$ e $f_\text{e2}$ si allontanano tra loro.

Più grande è questa distanza in frequenza, più facilmente il filtro passa-banda a monte può far passare la frequenza di ricezione desiderata e attenuare contemporaneamente la frequenza immagine. Se la distanza è molto piccola, il filtro dovrebbe invece avere pendenze molto più ripide o una selettività più elevata. In questo caso, i requisiti per la preselezione del ricevitore sarebbero notevolmente più elevati.

[question:AF109]
[question:AF110]
[question:AF111]
[question:AF204]