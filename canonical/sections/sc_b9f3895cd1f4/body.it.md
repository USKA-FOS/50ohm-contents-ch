Un multimetro semplice non è adatto per misurare resistenze dipendenti dalla frequenza. Invece, si può usare un analizzatore di rete vettoriale (VNA). Questo è uno strumento di misura attivo che, per una varietà di frequenze (una banda di frequenza regolabile), determina come corrente e tensione si relazionano tra loro (rapporto delle ampiezze e sfasamento tra tensione e corrente).

<margin>
[photo:201:e_vna_tiefpassmessung:Misurazione di un filtro passa-basso da $\qty{0}{\mega\hertz}$ a $\qty{100}{\mega\hertz}$ con frequenza di taglio a $\qty{30}{\mega\hertz}$]
</margin>

---

In questo modo, ad esempio, si può determinare a quale frequenza un circuito oscillante o un filtro presenta una resistenza (o impedenza) particolarmente alta o bassa (cfr. figura [ref:e_vna_tiefpassmessung]). Allo stesso modo, si può determinare a quale frequenza un'antenna è in risonanza, osservando il ROS su una banda di frequenza, come mostrato nella figura [ref:e_vna_swr].

<margin>
[photo:323:e_vna_swr:Misurazione ROS di un'antenna filare a alimentazione finale. Il ROS è quasi $1$ a $\qty{14}{\mega\hertz}$]
</margin>

[question:EI201]
[question:EI202]
[question:EI203]
[question:EI204]

Molti VNA dovrebbero essere calibrati prima dell'uso per ottenere un risultato di misura il più accurato possibile.

[question:EI205]

---

Per la calibrazione e il test di funzionamento, si misurano spesso gli stati "aperto" (resistenza infinita), "cortocircuito" (resistenza vicina a zero) e "adattato" (resistenza di carico corrispondente all'impedenza caratteristica di uscita dello strumento di misura).

<margin>
[photo:327:e_vna_solt:Kit di calibrazione SOL(T). Da sinistra a destra - Load, Open, Closed]
</margin>

Con un terminatore collegato (ad es. una Resistenza di terminazione da $\qty{50}{\ohm}$), il VNA dovrebbe mostrare un ROS vicino a $\num{1}$, poiché nessuna potenza viene riflessa. Se non è collegato nulla al connettore di misura o se questo viene cortocircuitato, si ottiene un ROS vicino all'infinito (riflessione completa).

[question:EI206]