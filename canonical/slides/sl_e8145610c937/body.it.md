<left>
[picture:140:a_kollektorschaltung_schaltbild:Schema di un amplificatore in configurazione collettore di un transistor bipolare]
</left>
<right>
* Gli schemi degli amplificatori a transistor bipolari sono denominati in base al collegamento che viene attraversato dal segnale di ingresso e di uscita
* O viceversa: Il collegamento a cui né l'ingresso né l'uscita sono direttamente collegati
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Schema di un amplificatore in configurazione collettore di un transistor bipolare]
</left>
<right>
* Segnale di ingresso: Sorgente $\rightarrow$ Base $\rightarrow$ Collettore $\rightarrow$ Tensione di alimentazione $\rightarrow$ Sorgente
* Segnale di uscita: Collettore $\rightarrow$ Carico $\rightarrow$ Tensione di alimentazione $\rightarrow$ Collettore
</right>
---
[question:AD401]
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Schema di un amplificatore in configurazione collettore di un transistor bipolare]
</left>
<right>
* Il transistor richiede un punto di funzionamento (BIAS) definito
* Viene determinato dal partitore di tensione sulla base
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Schema di un amplificatore in configurazione collettore di un transistor bipolare]
</left>
<right>
* La resistenza di emettitore genera una tensione quando scorre corrente attraverso il transistor.
* La corrente scorre dall'emettitore attraverso la resistenza verso massa.
* Maggiore è la corrente che scorre, maggiore sarà la tensione sull'emettitore.
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Schema di un amplificatore in configurazione collettore di un transistor bipolare]
</left>
<right>
* La tensione di emettitore rallenta il flusso di corrente e previene forti fluttuazioni.
* Le variazioni di temperatura influenzano meno il transistor.
* $\rightarrow$ Il transistor rimane affidabile e funziona in modo uniforme.
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Schema di un amplificatore in configurazione collettore di un transistor bipolare]
</left>
<right>
* Accoppiamento dei segnali in ingresso e in uscita tramite *condensatori di accoppiamento*
* Mantengono lontane le componenti di corrente continua dallo stadio amplificatore
* Il punto di funzionamento viene stabilizzato
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Schema di un amplificatore in configurazione collettore di un transistor bipolare]
</left>
<right>
* Il condensatore di disaccoppiamento nella tensione di alimentazione scarica sulla massa segnali indesiderati HF e NF
* Si evitano effetti di retroazione nello stadio e sulla tensione di alimentazione
* Il collettore viene collegato a massa $\rightarrow$ l'uscita si trova allo stesso potenziale dell'ingresso
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Schema di un amplificatore in configurazione collettore di un transistor bipolare]
</left>
<right>
* Lo sfasamento è di $\qty{0}{\degree}$
* Impedenza di ingresso relativamente alta
* $\rightarrow$ Guadagno di tensione circa $\num{0,9}$ a $\num{0,98}$ (sempre leggermente inferiore a $1$)
* Impedenza di uscita molto bassa rispetto all'impedenza di ingresso
</right>

---
[question:AD405]
---
[question:AD402]
---
[question:AD403]
---
### Stadio buffer

* Applicazione frequente come stadio buffer tra oscillatore e altre parti del circuito
* Carica l'oscillatore con alta impedenza
* $\rightarrow$ Meno corrente dall'oscillatore
* $\rightarrow$ Disaccoppiamento
* $\rightarrow$ Migliore stabilizzazione della frequenza dell'oscillatore

---
[question:AD404]