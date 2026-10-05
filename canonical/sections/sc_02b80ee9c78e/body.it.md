Nella sezione [sec:frequenzvervielfacher_1] abbiamo già conosciuto i moltiplicatori di frequenza a livello di blocco. Ora vogliamo capire come funzionano.

I diodi e i transistor hanno una caratteristica non lineare. Se vengono pilotati da un segnale sinusoidale, questo viene distorto. Come abbiamo già imparato, in tali processi non lineari si generano armoniche. In un moltiplicatore di frequenza, questo effetto viene sfruttato intenzionalmente: il segnale di ingresso viene prima distorto in modo non lineare, in modo che si generino numerose armoniche. Successivamente, l'armonica superiore desiderata viene selezionata utilizzando un circuito oscillante sintonizzato o un filtro e utilizzata come segnale di uscita.

Tecnicamente, un moltiplicatore di frequenza viene realizzato in modo che il segnale di ingresso venga prima inviato a uno stadio di distorsione non lineare. Questo può essere, ad esempio, un amplificatore funzionante in classe C, che discuteremo nel corso del capitolo. Successivamente, dal miscuglio di segnali, l'armonica superiore desiderata del segnale viene selezionata mediante filtri e inviata allo stadio successivo. Poiché la moltiplicazione di frequenza si basa su armoniche superiori/armoniche, sono possibili solo multipli interi della frequenza fondamentale. In pratica (con poche eccezioni) viene utilizzata solo la 2a armonica o la 3a armonica della frequenza fondamentale (raddoppio, triplicazione).
Per ottenere moltiplicazioni di frequenza più elevate, vengono quindi collegati in cascata stadi con raddoppio o triplicazione, in modo che i loro fattori si moltiplichino successivamente.

[question:AF311]

Attraverso la moltiplicazione di frequenza e, se necessario, il loro collegamento in cascata, vengono generati prodotti di frequenza che spesso possono causare interferenze. Pertanto, gli stadi di moltiplicazione di frequenza devono essere ben schermati per ridurre al massimo le emissioni indesiderate.

[question:AF313]

Un tipico circuito moltiplicatore (vedi figura [ref:a_frequenzvervielfacher_schaltung]) contiene uno stadio amplificatore, che viene intenzionalmente pilotato senza polarizzazione di base. Ciò crea un amplificatore in funzionamento in classe C, che distorce fortemente il segnale di ingresso e alla cui uscita il segnale viene prelevato mediante filtri. Per i filtri vengono utilizzati circuiti oscillanti corrispondenti, che risuonano alla frequenza desiderata e sono solitamente sintonizzabili.

<margin>
[picture:489:a_frequenzvervielfacher_schaltung:Esempio di un circuito di un moltiplicatore di frequenza con amplificatore in classe C senza polarizzazione di base]
</margin>

[question:AF312]

Se più stadi moltiplicatori sono collegati in cascata all'interno di un dispositivo, possono verificarsi interferenze su frequenze che si formano tra i singoli stadi moltiplicatori. Per determinare queste frequenze, è necessario calcolare il percorso del segnale attraverso i singoli stadi e le sue frequenze successive. Pertanto, l'ordine dei corrispondenti stadi moltiplicatori è di cruciale importanza per determinare le frequenze di interferenza, poiché solo alcune frequenze sono matematicamente possibili.

[question:AF314]
