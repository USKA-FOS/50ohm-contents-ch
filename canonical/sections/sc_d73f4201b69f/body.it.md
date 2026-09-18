L’alimentatore a commutazione è stato già spiegato in modo introduttivo nelle classi N ed E. Ora esaminiamo più in dettaglio lo schema a blocchi semplificato.

<margin>
[immagine:35:a_schaltnetzteil:Schema di principio di un alimentatore a commutazione]
</margin>

L’importante interruttore elettronico nel blocco E serve anche per regolare la tensione d’uscita costante. Poiché non esistono stati intermedi tra transistor conduttore e interdetto, deve esserci un altro modo per regolare la tensione. Il trasporto di energia dal lato ingresso al lato di carico può essere variato modificando il tempo di commutazione. Se l’interruttore rimane chiuso più a lungo, viene trasportata più energia al lato di carico e la tensione d’uscita aumenta. Per rilevare questo, è necessaria una retroazione della tensione d’uscita al blocco di controllo dell’interruttore elettronico. Questo circuito di retroazione manca nello schema semplificato rappresentato. La regolazione della tensione d’uscita avviene quindi tramite il cosiddetto modulatore a larghezza d’impulsi. Ciò significa che lo stato conduttore dell’interruttore viene modificato, mentre la frequenza di commutazione rimane costante.

---

[domanda:AD311]


È importante anche la separazione galvanica tra lato ingresso e lato uscita, per evitare che i potenziali della tensione di rete raggiungano l’uscita. Questa separazione galvanica viene realizzata tramite il trasformatore con nucleo in ferrite.
Vedi figura [ref:a_innenansicht_eines_schaltnetzteils].


<margin>
[immagine:264:a_innenansicht_eines_schaltnetzteils:Vista interna di un alimentatore a commutazione]
</margin>

---

La variazione del tempo di commutazione genera segnali di disturbo aggiuntivi che devono essere assolutamente tenuti lontani dal lato della tensione di rete, per evitare che si diffondano sulla rete elettrica e disturbino altri dispositivi elettronici. La rete elettrica funziona anche come antenna e può quindi irradiare segnali di disturbo come onda elettromagnetica. Se l’interruttore elettronico viene azionato con una frequenza di commutazione di $\qty{30}{\kilo\hertz}$, si ottiene uno spettro di disturbo in cui compare un segnale di disturbo ogni $\qty{30}{\kilo\hertz}$. La figura [ref:a_störspektrum] mostra lo spettro di disturbo di un alimentatore a commutazione. Lo spettro di disturbo è stato ricevuto direttamente sopra l’involucro dell’alimentatore a commutazione. A $\qty{1}{\metro}$ di distanza, lo spettro di disturbo è appena misurabile.


[domanda:AD312]


Nei dispositivi non sufficientemente antidisturbo, lo spettro di disturbo compromette la ricezione radio.

[domanda:AD313]


<margin>
[immagine:277:a_störspektrum:Spettro di disturbo di un alimentatore a commutazione]
</margin>

---

Per impedire che i disturbi raggiungano la rete elettrica, nell’alimentatore a commutazione deve essere installato un filtro passa-basso di alta qualità sul lato di connessione alla rete a $\qty{230}{\volt}$ in corrente alternata. La struttura tipica del filtro è visibile nella figura [ref:a-schaltnetzteilfilter].


<margin>
[immagine:367:a-schaltnetzteilfilter:Filtro all’ingresso $\qty{230}{\volt}$ di un alimentatore a commutazione]
</margin>

Confronta anche i filtri nelle figure [ref:a_EMV_Filter1] e [ref:a_EMV_Filter2]
*Nota:* Il conduttore PE non deve essere collegato al conduttore L1 o al conduttore N.
La bobina d’arresto T non deve svolgere una funzione di trasformatore per la tensione alternata di rete.

[domanda:AD314]



<margin>
Filtro EMC = filtro antidisturbo contro disturbi condotti
[immagine:242:a_EMV_Filter1: Filtro antidisturbo per un alimentatore a commutazione]
[immagine:243:a_EMV_Filter2: Filtro direttamente all’ingresso $\qty{230}{\volt}$ in corrente alternata]
</margin>