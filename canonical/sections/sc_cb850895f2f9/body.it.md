Nella classe E abbiamo già imparato a conoscere il ricevitore supereterodina. In questa classe affronteremo ora il ricevitore supereterodina a doppia conversione. A differenza della supereterodina semplice, nella supereterodina a doppia conversione vengono utilizzate 2 frequenze intermedie, come mostrato nella figura [ref:doppelsuper_blockschaltbild].


<margin>
[picture:810:doppelsuper_blockschaltbild:Schema a blocchi di una supereterodina a doppia conversione]
</margin>

Utilizzando una prima IF elevata, come descritto nel paragrafo precedente, è possibile ottenere una buona soppressione della frequenza immagine. Le due possibili frequenze di ricezione risultano così molto distanti tra loro e la soppressione della frequenza di ricezione indesiderata (frequenza immagine) è facilmente ottenibile tramite filtri d’ingresso posti prima del primo mixer.


Utilizzando una seconda IF bassa, nella seconda fase si può ottenere un’elevata selettività del ricevitore, poiché per frequenze basse è tecnicamente molto più semplice realizzare filtri con un elevato fattore di qualità e con pendenze molto ripide.


La prima IF e la frequenza di ricezione massima desiderata dovrebbero essere, in un ricevitore in onde corte, il più possibile distanti tra loro, a seconda del concetto del ricevitore, per evitare la ricezione diretta dell’IF tramite l’antenna. La prima IF dovrebbe quindi essere pari al doppio della frequenza di ricezione massima.


<tip>
Un’estensione del concetto di supereterodina a doppia conversione è la supereterodina a tripla conversione, nella quale viene generata una terza IF bassa. Questo può essere utile per particolari metodi di demodulazione o per la realizzazione di sistemi di soppressione dei disturbi (filtri notch). Il calcolo delle frequenze intermedie e delle frequenze dell’oscillatore avviene in questo caso in modo analogo a quello della supereterodina a doppia conversione.
</tip>

[question:AF112]
[question:AF113]


Dopo il primo mixer, per migliorare la robustezza nei confronti di segnali forti, può essere inserito un filtro molto stretto, sintonizzato sulla prima IF. Questo filtro viene chiamato *Roofing Filter*. La larghezza di banda del Roofing Filter deve essere almeno pari alla larghezza di banda massima necessaria per le modalità operative previste.

[question:AF114]
[question:AF116]


La supereterodina a doppia conversione è composta dai seguenti blocchi funzionali:

1. Parte RF con preselezione
2. Primo mixer con VFO per la generazione della prima IF. In questo caso, la frequenza del VFO può essere sia superiore che inferiore alla frequenza di ricezione desiderata (spostata rispettivamente della prima IF)
3. Primo amplificatore IF con filtro (Roofing Filter)
4. Secondo mixer con CO (oscillatore a quarzo) per la generazione della seconda IF. In questo caso, la frequenza del CO può essere sia superiore che inferiore alla prima IF (spostata rispettivamente della seconda IF)
5. Secondo amplificatore IF con filtro (filtro IF a seconda della modalità di modulazione/operativa, solitamente commutabile)
6. Rivelatore a prodotto o demodulatore (a seconda della modalità operativa), eventualmente con BFO. Questo stadio serve anche per generare una tensione di regolazione per il controllo della sensibilità d’ingresso del ramo ricevente (AGC)
7. Amplificatore BF con uscita altoparlante o connettore cuffie

[question:AF209]
[question:AF117]
[question:AF210]


Per calcolare le frequenze dell’oscillatore necessarie in funzione di una frequenza di ricezione desiderata, occorre considerare che le frequenze dell’oscillatore possono essere sia superiori che inferiori alla frequenza d’ingresso desiderata del mixer. Pertanto, per ogni stadio di miscelazione esistono due possibili soluzioni:

1. Frequenza dell’oscillatore = Frequenza d’ingresso + Frequenza d’uscita
2. Frequenza dell’oscillatore = Frequenza d’ingresso - Frequenza d’uscita


Con queste informazioni è possibile rispondere alle seguenti domande.

[question:AF120]
[question:AF118]
[question:AF119]