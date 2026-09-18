Gli oscillatori sono uno degli elementi circuitali più importanti nel radioamatoriale. Sono, per così dire, il cuore di ogni apparecchio radio. Gli oscillatori servono per generare oscillazioni ad alta frequenza nei trasmettitori e nei ricevitori.

Il cuore di un oscillatore è un elemento amplificatore, il cui *segnale di uscita viene reimmesso nel suo ingresso*.

Affinché un oscillatore possa generare oscillazioni non smorzate, devono essere soddisfatte *due condizioni fondamentali*.
Da un lato, il *segnale di uscita deve essere reimmesso in fase nel punto di ingresso del circuito*.
Dall'altro, l'*ampiezza del segnale reimmesso deve essere almeno pari a quella del segnale di ingresso*. Si dice anche che il cosiddetto *guadagno d’anello deve essere maggiore di 1* affinché sia possibile l'autoeccitazione, che mantiene l'oscillazione.

[question:AD613]

<margin>
[picture:760:a_oszillator_schaltungen_oszillator:Circuito di un oscillatore a reazione capacitiva] 
</margin>

%TODO: Possibilmente derivare l'immagine 760 e aggiungere i 3 punti del circuito a tre punti (sul partitore di tensione capacitivo - in alto, al centro e in basso)

Il circuito mostrato nella figura [ref:a_oszillator_schaltungen_oszillator] rappresenta un oscillatore a tre punti a reazione capacitiva. Il segnale di uscita viene reimmesso dalla base del circuito, tramite un partitore di tensione capacitivo, sulla base del transistor. La frequenza dell'oscillatore è determinata principalmente dal circuito oscillante nella base (costituito da bobina e condensatore di taratura) nonché dal partitore di tensione capacitivo collegato in parallelo al circuito oscillante.
In questo circuito si tratta di un oscillatore in configurazione a collettore comune, poiché il collettore è collegato a massa in corrente alternata.

[question:AD614]
[question:AD616]

Per aumentare la stabilità in frequenza di un oscillatore, il suo componente determinante in frequenza (circuito oscillante) può essere sostituito con un quarzo. I quarzi possono essere eccitati a oscillare sia alla loro frequenza fondamentale che alle loro frequenze armoniche (armoniche/sovratoni). Tuttavia, affinché un quarzo possa funzionare su una frequenza armonica, l'amplificatore deve essere progettato per essere selettivo in frequenza (ad esempio tramite l'uso di un circuito oscillante). Se questo non è presente, si può dedurre che il quarzo funzioni alla sua frequenza fondamentale (vedi figura [ref:a_oszillator_schaltungen_quarzoszillator]).

<margin>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Circuito di un oscillatore al quarzo in configurazione a collettore comune con funzionamento del quarzo alla frequenza fondamentale] 
</margin>

[question:AD617]

Il segnale dell'oscillatore dovrebbe sempre essere disaccoppiato nel punto a impedenza più bassa di un oscillatore, per caricarlo il meno possibile. In una configurazione a collettore comune, questo punto è l'emettitore del transistor.

[question:AD610]

A un oscillatore dovrebbe sempre essere collegato uno stadio buffer, che garantisce che l'oscillatore sia disaccoppiato da altre parti del circuito e che la sua frequenza non venga influenzata dal carico dell'uscita. Uno stadio buffer è solitamente realizzato come circuito a collettore comune (inseguitore di emettitore) e presenta un'alta impedenza di ingresso, che carica minimamente l'oscillatore. Al suo uscita, il segnale dell'oscillatore può quindi essere ulteriormente elaborato a bassa impedenza.

Le misurazioni sugli oscillatori dovrebbero sempre essere effettuate dopo lo stadio buffer, poiché altrimenti l'oscillatore verrebbe caricato con capacità parassite e la sua frequenza ne risulterebbe influenzata.

[question:AD615]
[question:AD619]
[question:AD618]