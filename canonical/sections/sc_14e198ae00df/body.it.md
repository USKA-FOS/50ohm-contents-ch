Se il ricevitore rileva un errore di trasmissione, ad esempio tramite bit di controllo, può richiedere al trasmettitore una ritrasmissione dei dati. Con la *correzione d’errore in avanti* (FEC, *Forward Error Correction*), invece, spesso non è necessario ritrasmettere. A tal fine, ai dati utili vengono aggiunte informazioni aggiuntive, ad esempio più bit di controllo. In questo modo, il ricevitore può, in determinate condizioni, non solo rilevare che si è verificato un errore, ma anche identificare quale bit è errato e correggerlo. In inglese, questa procedura è chiamata *Forward Error Correction* (FEC).


Come funziona nel dettaglio è illustrato nell’approfondimento accanto, prendendo come esempio un codice di Hamming. Il procedimento esatto non è rilevante per l’esame.


[question:AE413]
[question:AE414]

<indepth>
Il codice di Hamming è un metodo di correzione degli errori che utilizza più bit di parità. Supponiamo di voler trasmettere i seguenti $\num{11}$ bit di dati:


[picture:683:hamming1:]


Affinché un singolo errore di bit possa non solo essere rilevato, ma anche corretto, dobbiamo essere in grado di determinare in quale posizione si è verificato l’errore. Per fare ciò, consideriamo innanzitutto le posizioni dei singoli bit e le indichiamo con lettere:


[picture:682:hamming2:]


Ora disponiamo i bit di dati in modo diverso e aggiungiamo quattro bit di parità aggiuntivi $p_1$ a $p_4$:


[picture:684:hamming3:]


I quattro bit di parità controllano gruppi diversi e sovrapposti di bit:


[picture:685:hamming4:]


Ogni bit di parità protegge un gruppo specifico:


[picture:686:hamming5:]


Per ciascuno di questi gruppi calcoliamo ora il corrispondente bit di parità con *parità pari* (*Even Parity*):


[picture:687:hamming6:]


Se durante la trasmissione si verifica un singolo errore di bit, alcuni controlli di parità falliscono. Dalla combinazione dei controlli falliti si può determinare la posizione in cui si è verificato l’errore. Il bit errato può quindi essere invertito e corretto.


Ad esempio, se il bit $k$ viene trasmesso come $\num{0}$, tutti e quattro i controlli di parità $p_1$ a $p_4$ falliscono. Solo il bit $k$ appartiene a tutti e quattro i gruppi controllati. L’errore deve quindi trovarsi nel bit $k$.


Se invece si verifica un errore nel bit $a$, falliscono solo i controlli di parità di $p_1$ e $p_2$, mentre i controlli di $p_3$ e $p_4$ hanno successo. Dal modello risultante, il ricevitore può riconoscere che il bit $a$ è errato.


Anche un errore in un bit di parità stesso può essere rilevato e corretto. Se, ad esempio, $p_1$ è errato, fallisce solo il controllo di parità relativo a $p_1$, mentre i controlli di $p_2$, $p_3$ e $p_4$ hanno successo. L’errore deve quindi trovarsi in $p_1$.


Il codice di Hamming mostrato qui è progettato per correggere un singolo errore di bit. Se si verificano più errori di bit contemporaneamente, dalle verifiche di parità non è più possibile determinare in modo affidabile la posizione effettiva dell’errore. Codici di Hamming avanzati possono, ad esempio, rilevare in modo sicuro due errori di bit che si verificano contemporaneamente.