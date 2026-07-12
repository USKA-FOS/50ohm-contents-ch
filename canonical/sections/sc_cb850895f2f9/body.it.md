A differenza della supereterodina semplice, nella doppia supereterodina vengono utilizzate 2 frequenze intermedie.

<margin>
[picture:810:doppelsuper_blockschaltbild:Schema a blocchi di una doppia supereterodina]
</margin>

Utilizzando una prima FI alta, è possibile ottenere una buona soppressione della frequenza immagine. Le due possibili stazioni di ricezione sono quindi molto distanti tra loro e la soppressione della stazione di ricezione indesiderata (frequenza immagine) è facilmente realizzabile tramite filtri d'ingresso prima del primo mixer. Utilizzando una seconda FI bassa, è possibile ottenere un'elevata selettività del ricevitore nel secondo stadio, poiché per le basse frequenze i filtri con alto fattore di qualità e fianchi ripidi sono tecnicamente molto ben realizzabili.
Nel caso di un ricevitore per onde corte, la prima FI e la frequenza di ricezione più alta desiderata dovrebbero anche essere il più possibile distanti tra loro, a seconda del concetto del ricevitore, per evitare la ricezione diretta della FI tramite l'antenna. La 1ª FI dovrebbe quindi essere il doppio della frequenza di ricezione massima.

<tip>
Un'estensione del concetto di doppia supereterodina sarebbe la tripla supereterodina, in cui viene generata una terza FI bassa. Questo può essere utile per metodi di demodulazione speciali o per la realizzazione di metodi di soppressione delle interferenze (filtro notch). Il calcolo delle frequenze intermedie e delle frequenze dell'oscillatore viene effettuato in modo analogo a quello della doppia supereterodina.
</tip>

[question:AF112]
[question:AF113]

Dopo il primo mixer, per migliorare la resistenza ai segnali forti, può essere utilizzato un filtro molto stretto, accordato sulla 1ª FI. Questo filtro viene chiamato *filtro roofing*. La larghezza di banda del filtro roofing deve essere almeno pari alla larghezza di banda massima richiesta per i modi operativi previsti.

[question:AF114]
[question:AF116]

La doppia supereterodina è composta dai seguenti blocchi funzionali:
1. Sezione RF con preselezione
2. Primo mixer con VFO per la generazione della prima FI. La frequenza del VFO può trovarsi sia al di sopra che al di sotto della frequenza di ricezione desiderata (ciascuna sfalsata di 1ª FI)
3. Primo amplificatore FI con filtro (filtro roofing)
4. Secondo mixer con CO (oscillatore a quarzo) per la generazione della seconda FI. La frequenza del CO può trovarsi sia al di sopra che al di sotto della 1ª FI (ciascuna sfalsata di 2ª FI)
5. Secondo amplificatore FI con filtro (filtro FI a seconda del tipo di modulazione/modo operativo, solitamente commutabile).
6. Detettore di prodotto o demodulatore (a seconda del modo operativo) eventualmente con BFO. Questo stadio serve anche per generare una tensione di controllo per la regolazione della sensibilità d'ingresso del ramo di ricezione (AGC)
7. Amplificatore AF con uscita altoparlante o connessione cuffie.

[question:AF209]
[question:AF117]
[question:AF210]

Per calcolare le frequenze dell'oscillatore necessarie in dipendenza di una frequenza di ricezione desiderata, bisogna tenere presente che le frequenze dell'oscillatore possono trovarsi sopra o sotto la frequenza di ingresso desiderata del mixer. Pertanto, per ogni stadio mixer esistono due possibili soluzioni.
1. Frequenza dell’oscillatore = Frequenza di ingresso + Frequenza di uscita
2. Frequenza dell’oscillatore = Frequenza di ingresso - Frequenza di uscita

Con queste conoscenze è possibile rispondere alle seguenti domande.

[question:AF120]
[question:AF118]
[question:AF119]