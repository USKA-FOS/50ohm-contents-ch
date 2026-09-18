La potenza di trasmissione generata dal trasmettitore deve essere irradiata dall'antenna in modo il più completo possibile e senza perdite. Per questo motivo sono necessarie linee di antenna speciali, che nella terminologia tecnica vengono chiamate *linee di trasmissione*.

<margin>
[photo:65:n_Koax_Detail:Cavo coassiale in dettaglio]
</margin>

Il tipo di linea di trasmissione più diffuso è il *cavo coassiale* (Figura [ref:n_Koax_Detail]). Nel linguaggio comune si parla spesso semplicemente di cavi coassiali. I cavi coassiali sono composti da un conduttore interno e uno esterno, isolati tra loro. Hanno una struttura tubolare e sono rivestiti da una guaina protettiva. Esistono cavi coassiali di varie tipologie:
* spessi o sottili
* con conduttore interno flessibile o rigido
* con conduttore esterno in treccia metallica e/o lamina o addirittura in tubo di rame massiccio

Ma anche nel miglior cavo coassiale si verificano perdite, poiché una parte della potenza di trasmissione viene convertita in calore. Il livello delle perdite di una linea di trasmissione è indicato dalla cosiddetta *attenuazione del cavo*, che nei datasheet viene solitamente espressa in decibel ($\unit{\dB}$) per $\qty{100}{\meter}$. Più lungo è un cavo coassiale, maggiore è la perdita dovuta all'attenuazione. Anche la frequenza dell'oscillazione elettrica gioca un ruolo: all'aumentare della frequenza, aumenta l'attenuazione del cavo.

[question:NG207]

Un'altra caratteristica importante delle linee di trasmissione è la cosiddetta *impedenza caratteristica*, espressa in ohm ($\unit{\ohm}$). Si tratta di una proprietà che dipende dalla struttura della linea, tra l'altro dalla distanza tra conduttore interno ed esterno. La lunghezza della linea non influisce sull'impedenza caratteristica.

Se si collegano linee di trasmissione con impedenza caratteristica diversa, nella zona di giunzione si verificano riflessioni indesiderate delle oscillazioni ad alta frequenza. Di conseguenza, una parte della potenza di trasmissione viene riflessa verso il trasmettitore e non può essere irradiata; nel peggiore dei casi, può addirittura danneggiare il trasmettitore.

La presa antenna dei dispositivi radioamatoriali è quasi sempre progettata per un'impedenza caratteristica di $\qty{50}{\ohm}$. Di conseguenza, i cavi coassiali comunemente utilizzati nel radioamatore hanno un'impedenza caratteristica di $\qty{50}{\ohm}$. Nella tecnica televisiva sono invece comuni cavi coassiali con un'impedenza caratteristica di $\qty{75}{\ohm}$. Più raramente si trovano cavi coassiali con $\qty{60}{\ohm}$.

[question:NG201]