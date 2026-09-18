Nella classe E abbiamo già imparato a conoscere i moltiplicatori di frequenza a livello di blocco. Nella classe A vogliamo capire come funzionano.

I diodi e i transistor hanno una caratteristica non lineare. Se vengono pilotati con un segnale sinusoidale, questo viene distorto. Come abbiamo già appreso, in questi processi non lineari si generano armoniche. In un moltiplicatore di frequenza questo effetto viene sfruttato intenzionalmente: il segnale di ingresso viene distorto in modo non lineare, generando numerose armoniche. Successivamente, l’armonica desiderata viene selezionata con un circuito oscillante o un filtro sintonizzato e utilizzata come segnale di uscita.

Tecnicamente, un moltiplicatore di frequenza viene realizzato inviando inizialmente il segnale di ingresso a uno stadio di distorsione non lineare. Questo può essere, ad esempio, un amplificatore di classe C, che tratteremo nel corso del capitolo. Successivamente, dal segnale misto vengono selezionate tramite filtri l’armonica desiderata e trasmesse allo stadio successivo. Poiché la moltiplicazione di frequenza si basa sulle armoniche, sono possibili solo multipli interi della frequenza fondamentale. In pratica, (con poche eccezioni) si utilizzano solo la 2ª armonica o la 3ª armonica della frequenza fondamentale (raddoppio, triplicazione).
Per ottenere moltiplicazioni di frequenza più elevate, gli stadi di raddoppio o triplicazione vengono collegati in cascata, in modo che i loro fattori si moltiplichino tra loro.

[question:AF311]

Attraverso la moltiplicazione di frequenza e, se necessario, la loro connessione in cascata, vengono generati prodotti di frequenza che spesso possono causare interferenze. Pertanto, gli stadi del moltiplicatore di frequenza devono essere molto ben schermati per ridurre al minimo le radiazioni indesiderate.

[question:AF313]

Un tipico circuito moltiplicatore di frequenza (vedi figura [ref:a_frequenzvervielfacher_schaltung]) contiene uno stadio amplificatore che viene fatto funzionare deliberatamente senza polarizzazione di base. In questo modo si ottiene un amplificatore in classe C, che distorce fortemente il segnale di ingresso e dal cui uscita il segnale viene prelevato tramite filtri. In questo caso, per i filtri vengono utilizzati circuiti oscillanti corrispondenti che sono in risonanza alla frequenza desiderata e sono generalmente sintonizzabili.

<margin>
[picture:489:a_frequenzvervielfacher_schaltung:Esempio di circuito di un moltiplicatore di frequenza con amplificatore di classe C senza polarizzazione di base]
</margin>

[question:AF312]

Se all’interno di un apparecchio sono collegate in cascata più stadi moltiplicatori, possono verificarsi interferenze a frequenze che si formano tra i singoli stadi. Per determinare queste frequenze, è necessario calcolare il percorso del segnale attraverso gli stadi e le frequenze risultanti. Pertanto, l’ordine degli stadi moltiplicatori è fondamentale per determinare le frequenze di interferenza, poiché solo alcune frequenze sono matematicamente possibili.

[question:AF314]