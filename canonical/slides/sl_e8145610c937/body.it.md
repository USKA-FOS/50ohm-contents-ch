<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificatore in circuito a collettore comune di un transistor bipolare]
</left>
<right>
* I circuiti amplificatori con transistor bipolari vengono denominati in base al terminale attraversato dal segnale di ingresso e di uscita
* O, in alternativa: il terminale a cui né l'ingresso né l'uscita sono direttamente collegati
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificatore in circuito a collettore comune di un transistor bipolare]
</left>
<right>
* Segnale di ingresso: sorgente $\rightarrow$ base $\rightarrow$ collettore $\rightarrow$ tensione di alimentazione $\rightarrow$ sorgente
* Segnale di uscita: collettore $\rightarrow$ carico $\rightarrow$ tensione di alimentazione $\rightarrow$ collettore
</right>
---
[question:AD401]
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificatore in circuito a collettore comune di un transistor bipolare]
</left>
<right>
* Il transistor necessita di un punto di funzionamento definito (BIAS)
* Viene stabilito tramite il partitore di tensione sulla base
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificatore in circuito a collettore comune di un transistor bipolare]
</left>
<right>
* La resistenza di emettitore genera una tensione quando la corrente attraversa il transistor.
* La corrente fluisce dall'emettitore attraverso la resistenza verso massa.
* Maggiore è la corrente, maggiore è la tensione sull'emettitore.
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificatore in circuito a collettore comune di un transistor bipolare]
</left>
<right>
* La tensione di emettitore rallenta il flusso di corrente e impedisce forti oscillazioni.
* Le variazioni di temperatura influenzano meno il transistor.
* $\rightarrow$ Il transistor rimane affidabile e funziona in modo uniforme.
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificatore in circuito a collettore comune di un transistor bipolare]
</left>
<right>
* Ingresso e uscita dei segnali sulla base e sull'emettitore tramite *condensatori di accoppiamento*
* Mantengono lontani dalla fase di amplificazione i componenti in corrente continua
* Il punto di funzionamento viene stabilizzato
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificatore in circuito a collettore comune di un transistor bipolare]
</left>
<right>
* Il condensatore di disaccoppiamento sulla tensione di servizio devia verso massa i segnali indesiderati in HF e BF
* Si evitano effetti di retroazione nella fase e sulla tensione di alimentazione
* Il collettore viene collegato a massa $\rightarrow$ l'uscita è allo stesso potenziale dell'ingresso
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Amplificatore in circuito a collettore comune di un transistor bipolare]
</left>
<right>
* Lo sfasamento è $\qty{0}{\degree}$
* L'impedenza di ingresso è relativamente alta
* $\rightarrow$ Il guadagno di tensione è circa $\num{0,9}$ fino a $\num{0,98}$ (sempre leggermente inferiore a $1$)
* L'impedenza di uscita è molto bassa rispetto a quella di ingresso
</right>

---
[question:AD405]
---
[question:AD402]
---
[question:AD403]
---
### Stadio buffer

* Spesso utilizzato come stadio buffer tra oscillatore e altre parti del circuito
* Carica l'oscillatore con un'impedenza elevata
* $\rightarrow$ Minor corrente prelevata dall'oscillatore
* $\rightarrow$ Disaccoppiamento
* $\rightarrow$ Migliore stabilità di frequenza dell'oscillatore

---
[question:AD404]