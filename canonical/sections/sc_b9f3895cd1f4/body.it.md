Un multimetro semplice non è adatto per misurare resistenze dipendenti dalla frequenza. In alternativa, si può utilizzare un analizzatore di rete vettoriale (VNA). Si tratta di uno strumento di misura attivo che, per una vasta gamma di frequenze (una banda di frequenza regolabile), determina come corrente e tensione si relazionano tra loro (rapporto delle ampiezze e sfasamento tra tensione e corrente).

<margin>
[photo:201:e_vna_tiefpassmessung:Misurazione di un filtro passa-basso da $\qty{0}{\mega\hertz}$ a $\qty{100}{\mega\hertz}$ con frequenza di taglio a $\qty{30}{\mega\hertz}$]
</margin>

---

In questo modo, ad esempio, è possibile determinare a quale frequenza un circuito oscillante o un filtro presenta una resistenza (o impedenza) particolarmente elevata o particolarmente bassa (cfr. figura [ref:e_vna_tiefpassmessung]). Allo stesso modo, si può rilevare a quale frequenza un'antenna è in risonanza osservando il SWR su una banda di frequenza, come mostrato nella figura [ref:e_vna_swr].

<margin>
[photo:323:e_vna_swr:Misurazione del SWR di un'antenna filare alimentata all'estremità. Il SWR è quasi $1$ a $\qty{14}{\mega\hertz}$]
</margin>

[question:EI201]
[question:EI202]
[question:EI203]
[question:EI204]

Molti VNA devono essere calibrati prima dell'uso per ottenere un risultato di misura il più preciso possibile.

[question:EI205]

---

Per la calibrazione e per i test di funzionamento, si misurano spesso gli stati "aperto" (resistenza infinita), "cortocircuito" (resistenza prossima a zero) e "adattato" (resistenza di carico corrispondente alla resistenza di uscita dello strumento di misura).

<margin>
[photo:327:e_vna_solt:Kit di calibrazione SOL(T). Da sinistra a destra - Load, Open, Closed]
</margin>

Con un carico collegato (ad esempio una resistenza di terminazione da $\qty{50}{\ohm}$), il VNA dovrebbe indicare un SWR prossimo a $\num{1}$, poiché non viene riflessa alcuna potenza. Se non è collegato nulla alla porta di misura o questa viene cortocircuitata, si ottiene un SWR prossimo all'infinito (riflessione totale).

[question:EI206]