Se il ricevitore rileva un errore, ad esempio tramite bit di parità, può chiedere al trasmettitore di ritrasmettere i dati per correggere l'errore. Con la correzione degli errori in avanti, invece, spesso non è necessaria una ritrasmissione. A tale scopo, vengono aggiunti ulteriori ridondanze ai dati, ad esempio più bit di parità. In questo modo non solo viene rilevato che esiste un errore, ma anche dove. Il metodo può quindi correggere l'errore correggendo il bit rilevato come errato. Come ciò funzioni in dettaglio, puoi leggere nel riquadro di approfondimento. Tuttavia, non è rilevante per l'esame. In inglese si parla di Forward Error Correction (FEC).

[question:AE413]
[question:AE414]

<indepth>

Il codice di Hamming è un metodo di correzione degli errori che utilizza più bit di parità. Supponiamo di voler trasmettere i seguenti 11 bit:

[picture:683:hamming1: ]

L'obiettivo dovrebbe essere quello di poter non solo rilevare, ma anche correggere un errore di un bit. A tale scopo, è utile dare un'occhiata più da vicino alle posizioni dei singoli bit. A tale scopo, denominiamo le posizioni alfabeticamente:

[picture:682:hamming2: ]

Ora disponiamo i bit in modo leggermente diverso e aggiungiamo alcuni bit aggiuntivi:

[picture:684:hamming3: ]

Invece di un singolo bit di parità, ora ne usiamo quattro ($p_1$-$p_4$), che coprono diverse aree dei nostri bit di dati, in modo simile a un cruciverba:

[picture:685:hamming4: ]

Ogni bit di parità protegge una certa area:

[picture:686:hamming5: ]

Guardiamo di nuovo il tutto con i nostri dati. Per ogni area calcoliamo il bit di parità con parità pari:

[picture:687:hamming6: ]

Se si verifica un errore durante la trasmissione, questo può essere localizzato e corretto dalla combinazione delle diverse aree. 

Se, ad esempio, il bit $k$ viene convertito in un $\num{0}$ durante la trasmissione, tutti i controlli di parità ($p_1$-$p_4$) falliranno. L'errore deve quindi trovarsi nel bit $k$.

Se, ad esempio, si verifica un errore nel bit $a$, il controllo di parità di $p_1$ e $p_2$ fallisce, mentre quello di $p_3$ e $p_4$ ha successo. L'errore deve quindi trovarsi nel bit $a$.

Anche gli errori nei bit di parità possono essere rilevati e corretti. Se, ad esempio, si verifica un errore nel bit $p_1$, il controllo di parità di $p_1$ fallisce, mentre quello di $p_2$, $p_3$ e $p_4$ ha successo. L'errore deve quindi trovarsi nel bit $p_1$.

Se si verificano più di 1 errore, il codice di Hamming non può più rilevarli e correggerli correttamente. Esistono tuttavia estensioni del codice di Hamming che possono rilevare anche errori multi-bit.
</indepth>
