Gli oscillatori sono uno degli elementi circuitali più importanti nel radioamatore. Sono, per così dire, il cuore di ogni apparecchio radio. Gli oscillatori servono alla generazione di oscillazioni ad alta frequenza nei trasmettitori e nei ricevitori.

Il cuore di un oscillatore è un elemento amplificatore, il cui *segnale di uscita viene retroazionato sul suo ingresso*.

Affinché un oscillatore possa generare oscillazioni non smorzate, devono essere soddisfatte *due condizioni fondamentali*.
Da un lato, il *segnale di uscita deve essere retroazionato in fase sul punto di ingresso del circuito*.
Dall'altro, l'*ampiezza del segnale retroazionato deve essere almeno uguale* a quella del segnale di ingresso. Si dice anche che l'*amplificazione ad anello* debba essere maggiore di 1, affinché sia possibile l'auto-eccitazione che mantiene l'oscillazione.

[question:AD613]

<margin>
[picture:760:a_oszillator_schaltungen_oszillator:Circuito di un oscillatore a retroazione capacitiva]  
</margin>

%TODO: Eventualmente derivare l'immagine 760 e completarla con i 3 punti del circuito a tre punti (sul partitore di tensione capacitivo - in alto, al centro e in basso)

Il circuito mostrato nella figura [ref:a_oszillator_schaltungen_oszillator] rappresenta un oscillatore a tre punti a retroazione capacitiva. Il segnale di uscita viene retroazionato dall'emettitore del circuito, tramite un partitore di tensione capacitivo, alla base del transistor. La frequenza dell'oscillatore è determinata principalmente dal circuito oscillante nella base (composto da bobina e condensatore di trimmer) e dal partitore di tensione capacitivo collegato in parallelo al circuito oscillante.
Il circuito è un oscillatore in configurazione collettore, poiché il collettore è a massa per quanto riguarda la tensione alternata.

[question:AD614]
[question:AD616]

Per aumentare la stabilità di frequenza di un oscillatore, il suo componente che determina la frequenza (circuito oscillante) può essere sostituito da un quarzo. I quarzi possono essere eccitati a oscillare sia alla loro frequenza fondamentale sia alle loro frequenze armoniche (armoniche/sopratoni). Affinché un quarzo possa essere utilizzato su un'armonica, l'amplificatore deve essere progettato per essere selettivo in frequenza (ad esempio, utilizzando un circuito oscillante). Se questo non è presente, si può dedurre che il quarzo viene utilizzato alla sua frequenza fondamentale (vedi figura [ref:a_oszillator_schaltungen_quarzoszillator]).

<margin>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Circuito di un oscillatore a quarzo in configurazione collettore con funzionamento del quarzo alla frequenza fondamentale]  
</margin>

[question:AD617]

Il segnale dell'oscillatore dovrebbe sempre essere prelevato dal punto a più bassa impedenza di un oscillatore, per caricarlo il meno possibile. In una configurazione collettore, questo è l'emettitore del transistor.

[question:AD610]

A un oscillatore dovrebbe sempre essere collegato uno stadio cosiddetto di buffer, che assicura che l'oscillatore sia disaccoppiato da altre parti del circuito e che la sua frequenza non venga influenzata dal carico in uscita. Uno stadio di buffer è solitamente progettato come configurazione collettore (inseguitore di emettitore) e ha un'alta impedenza di ingresso, che carica l'oscillatore solo minimamente. Alla sua uscita, il segnale dell'oscillatore può quindi essere elaborato ulteriormente a bassa impedenza.

Le misurazioni sugli oscillatori dovrebbero sempre essere effettuate dopo lo stadio di buffer, altrimenti l'oscillatore viene caricato con capacità parassite e la sua frequenza viene influenzata da ciò.

[question:AD615]
[question:AD619]
[question:AD618]










