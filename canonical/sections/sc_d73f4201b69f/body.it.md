L'alimentatore a commutazione è stato introdotto nella sezione [sec:schaltnetzteil_1]. Ora esaminiamo più da vicino lo schema a blocchi semplificato [ref:a_schaltnetzteil].

<margin>
[picture:35:a_schaltnetzteil:Schema di principio di un alimentatore a commutazione]
</margin>

L'importante interruttore elettronico nel blocco E serve anche per regolare una tensione d’uscita costante.
Poiché non esistono stati intermedi tra il transistor in conduzione e quello in interdizione, deve esserci un altro metodo di regolazione. Il trasferimento di energia dal lato di ingresso al carico può essere variato modificando il tempo di commutazione. Se l'interruttore rimane chiuso più a lungo, viene trasferita più energia al carico e la tensione d’uscita aumenta. Per rilevare ciò, è necessario un feedback della tensione d’uscita al blocco di controllo dell'interruttore elettronico. Questo anello di retroazione manca nello schema semplificato mostrato. La regolazione della tensione d’uscita avviene tramite il cosiddetto modulatore a larghezza di impulso. Ciò significa che viene modificato lo stato di conduzione dell'interruttore, mentre la frequenza di commutazione rimane costante.

---

[question:AD311]

È importante anche l'isolamento galvanico tra il lato di ingresso e quello di uscita, per tenere i potenziali della tensione di rete lontani dall'uscita. Questo isolamento di rete avviene tramite il trasformatore con nucleo in ferrite.
Vedi figura [ref:a_innenansicht_eines_schaltnetzteils].

<margin>
[photo:264:a_innenansicht_eines_schaltnetzteils:Vista interna di un alimentatore a commutazione]
</margin>

---

La variazione del tempo di commutazione genera ulteriori segnali di disturbo, che devono assolutamente essere tenuti lontani dal lato della tensione di rete, per evitare che si diffondano attraverso la rete elettrica e disturbino altri dispositivi elettronici. La rete elettrica agisce anche come un'antenna e può quindi irradiare segnali di disturbo come onde elettromagnetiche. Se l'interruttore elettronico opera a una frequenza di commutazione di $\qty{30}{\kilo\hertz}$, si genera uno spettro di disturbo in cui appare un segnale di disturbo ogni $\qty{30}{\kilo\hertz}$. La figura [ref:a_störspektrum] mostra lo spettro di disturbo di un alimentatore a commutazione. Lo spettro di disturbo è stato ricevuto direttamente sopra il contenitore dell'alimentatore a commutazione. A una distanza di $\qty{1}{\meter}$, lo spettro di disturbo è difficilmente misurabile.

[question:AD312]

Negli alimentatori a commutazione con insufficiente protezione antidisturbo, lo spettro di disturbo compromette la ricezione radio.

[question:AD313]

<margin>
[photo:277:a_störspektrum:Spettro di disturbo di un alimentatore a commutazione]
</margin>

---

Per impedire che i disturbi entrino nella rete elettrica, nell'alimentatore a commutazione deve essere installato un filtro passa-basso di alta qualità sul lato del collegamento alla rete a corrente alternata di $\qty{230}{\volt}$. La tipica struttura del filtro è visibile nella figura [ref:a-schaltnetzteilfilter].

<margin>
[picture:367:a-schaltnetzteilfilter:Filtro all'ingresso $\qty{230}{\volt}$ di un alimentatore a commutazione]
</margin>

Confronta anche i filtri nelle figure [ref:a_EMV_Filter1] e [ref:a_EMV_Filter2]
*Nota:* Il conduttore PE non deve essere collegato al conduttore L1 o al conduttore N.
La bobina d’arresto T non deve avere una funzione di trasformatore per la tensione alternata di rete.

[question:AD314]


<margin>
Filtro EMC = filtro antidisturbo per disturbi condotti
[photo:242:a_EMV_Filter1: Filtro antidisturbo per un alimentatore a commutazione]
[photo:243:a_EMV_Filter2: Filtro direttamente all'ingresso della tensione CA di $\qty{230}{\volt}$]
</margin>
