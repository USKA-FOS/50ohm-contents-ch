Tecnicamente, un moltiplicatore di frequenza viene realizzato inviando inizialmente il segnale di ingresso a uno stadio di distorsione non lineare. Questo può essere, ad esempio, un amplificatore di classe C. Successivamente, la armonica desiderata del segnale viene selezionata dalla miscela di segnali mediante filtri e trasmessa allo stadio successivo. Poiché la moltiplicazione di frequenza si basa sulle armoniche, sono possibili solo multipli interi della frequenza fondamentale. In pratica, (con poche eccezioni) viene utilizzata solo la seconda o la terza armonica della frequenza fondamentale (raddoppio, triplicazione).
Per ottenere moltiplicazioni di frequenza più elevate, gli stadi di raddoppio o triplicazione vengono quindi collegati in serie, in modo che i loro fattori si moltiplichino successivamente.

[question:AF311]

La moltiplicazione di frequenza e, se necessario, la loro connessione in serie generano frequenze intermedie che possono spesso causare disturbi. Pertanto, gli stadi di moltiplicazione di frequenza devono essere molto ben schermati per ridurre al minimo le emissioni indesiderate.

[question:AF313]

Un tipico circuito moltiplicatore (vedi figura [ref:a_frequenzvervielfacher_schaltung]) contiene uno stadio amplificatore che viene deliberatamente fatto funzionare senza polarizzazione di base. Ciò crea un amplificatore in classe C, che distorce fortemente il segnale di ingresso e dal cui uscita il segnale viene prelevato mediante filtri. Per i filtri vengono utilizzati circuiti oscillanti appropriati che sono in risonanza alla frequenza desiderata e sono generalmente sintonizzabili.

<margin>
[picture:489:a_frequenzvervielfacher_schaltung:Esempio di circuito di un moltiplicatore di frequenza con amplificatore di classe C senza polarizzazione di base]
</margin>

[question:AF312]

Se più stadi moltiplicatori sono collegati in serie all'interno di un apparecchio, possono verificarsi disturbi alle frequenze che si formano tra i singoli stadi moltiplicatori. Per determinare queste frequenze, è necessario calcolare il percorso del segnale attraverso i singoli stadi e le frequenze presenti successivamente. Pertanto, l'ordine dei rispettivi stadi moltiplicatori è di fondamentale importanza per determinare le frequenze di disturbo.

[question:AF314]
