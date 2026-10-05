Nelle sezioni [sec:ueberlagerungsempfaenger_einfachsuper_1] e [sec:ueberlagerungsempfaenger_einfachsuper_2] abbiamo già conosciuto il ricevitore supereterodina. In questa classe vogliamo ora occuparci del ricevitore supereterodina a doppia conversione. A differenza della supereterodina semplice, nella supereterodina a doppia conversione vengono utilizzate 2 frequenze intermedie, come mostrato nella figura [ref:doppelsuper_blockschaltbild].

<margin>
[picture:810:doppelsuper_blockschaltbild:schema a blocchi di una supereterodina a doppia conversione]
</margin>

Utilizzando un primo FI alto, come descritto nella sezione precedente, è possibile una buona soppressione della frequenza immagine. Le due possibili frequenze di ricezione sono quindi molto distanti tra loro e la soppressione della frequenza di ricezione indesiderata (frequenza immagine) è facilmente possibile tramite filtri d'ingresso prima del primo mixer.

Utilizzando un secondo FI basso, nel secondo passo si può ottenere un'elevata selettività del ricevitore, poiché per le basse frequenze i filtri con alto fattore di qualità e pendenza ripida sono tecnicamente molto ben realizzabili.

La prima FI e la più alta frequenza di ricezione desiderata in un ricevitore a onde corte, a seconda del concetto del ricevitore, dovrebbero anche essere il più possibile distanti l'una dall'altra per evitare una ricezione diretta della FI attraverso l'antenna. La prima FI dovrebbe quindi essere il doppio della massima frequenza di ricezione.

<tip>
Un'estensione del concetto di supereterodina a doppia conversione sarebbe la supereterodina a tripla conversione, in cui viene formata una terza FI bassa. Ciò può essere utile per speciali procedure di demodulazione o per l'implementazione di procedure di soppressione delle interferenze (filtri notch). Il calcolo delle frequenze intermedie e delle frequenze dell'oscillatore avviene qui di conseguenza come per la supereterodina a doppia conversione.
</tip>

[question:AF112]
[question:AF113]

Dopo il primo mixer, per migliorare la robustezza ai segnali forti, può essere utilizzato un filtro molto stretto, sintonizzato sulla prima FI. Questo filtro è chiamato *Roofing Filter*. La larghezza di banda del filtro roofing deve essere almeno grande quanto la larghezza di banda massima richiesta dalle modalità operative previste.

[question:AF114]
[question:AF116]

La supereterodina a doppia conversione è composta dai seguenti blocchi funzionali:

1. Parte HF con preselezione
2. Primo mixer con VFO per formare la prima FI. Qui la frequenza del VFO può essere sia sopra che sotto la frequenza di ricezione desiderata (ciascuna spostata della prima FI)
3. Primo amplificatore FI con filtro (filtro roofing)
4. Secondo mixer con CO (oscillatore a quarzo) per formare la seconda FI. Qui la frequenza del CO può essere sia sopra che sotto la prima FI (ciascuna spostata della seconda FI)
5. Secondo amplificatore FI con filtro (filtro FI a seconda del tipo di modulazione/modalità operativa, solitamente commutabile).
6. Rivelatore a prodotto o demodulatore (a seconda della modalità operativa) eventualmente con BFO. Questo stadio serve anche alla generazione di una tensione di controllo per la regolazione della sensibilità d'ingresso del ramo di ricezione (AGC)
7. Amplificatore BF con uscita altoparlante o connessione cuffie

[question:AF209]
[question:AF117]
[question:AF210]

Per calcolare le frequenze dell'oscillatore necessarie in dipendenza da una frequenza di ricezione desiderata, bisogna rendersi conto che le frequenze dell'oscillatore possono trovarsi rispettivamente sopra o sotto la frequenza d'ingresso desiderata del mixer. Pertanto, per ogni stadio mixer esistono due possibilità di soluzione.

1. Frequenza dell'oscillatore = Frequenza d'ingresso + Frequenza d'uscita
2. Frequenza dell'oscillatore = Frequenza d'ingresso - Frequenza d'uscita

Con questa conoscenza si possono rispondere le seguenti domande.

[question:AF120]
[question:AF118]
[question:AF119]
