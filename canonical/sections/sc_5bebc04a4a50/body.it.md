Per evitare di dover costruire e accordare oscillatori separati per ogni banda di frequenza nei trasmettitori multi-banda per radioamatori, si utilizzava il principio della moltiplicazione di frequenza. A tal fine, un oscillatore stabile veniva fatto funzionare alla frequenza della banda più bassa (ad es. $\qty{3,5}{\mega\hertz}$), il cui segnale di uscita veniva poi convertito alle bande radioamatoriali desiderate mediante moltiplicatori di frequenza. È vantaggioso che le singole bande di frequenza abbiano rapporti fissi tra loro (ad es. $\qty{3,5}{\mega\hertz}$, $\qty{7}{\mega\hertz}$, $\qty{14}{\mega\hertz}$, ecc.) e siano per lo più multipli interi della banda più bassa. In questo modo, anche le armoniche superiori ricadono in una banda radioamatoriale, cosa che è desiderata dalle autorità di regolamentazione per evitare interferenze con altri servizi causate dalle armoniche superiori. In generale, gli oscillatori a basse frequenze possono essere costruiti e realizzati con maggiore stabilità rispetto a quelli ad alte frequenze. 

---

L'illustrazione [ref:n_f_vervielfacher] mostra lo schema a blocchi di un moltiplicatore di frequenza con un fattore di $2$, in cui la frequenza di ingresso di $\qty{3,5}{\mega\hertz}$ viene aumentata a $\qty{7}{\mega\hertz}$. Un moltiplicatore di frequenza viene tipicamente generato da una non linearità (ad es. una Diode) che crea armoniche mirate del segnale di ingresso, dalle quali viene poi selezionata la frequenza multipla desiderata con un filtro passa-banda.

<margin>
[picture:1042:n_f_vervielfacher:Schema a blocchi di un moltiplicatore di frequenza]
</margin>

Spesso si utilizza una catena di moltiplicatori di frequenza per ottenere i fattori di moltiplicazione desiderati. In questo caso, quando si collegano in serie più moltiplicatori, i singoli fattori vengono moltiplicati tra loro.
Al contrario, una tale configurazione può ovviamente essere calcolata a ritroso. In questo caso, è necessario dividere per i rispettivi fattori parziali.

[question:EF303]
[question:EF302]
[question:EF301]