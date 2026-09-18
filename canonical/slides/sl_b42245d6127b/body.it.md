## Correzione degli errori in avanti (FEC)

* Se il ricevitore rileva un errore (ad esempio tramite bit di controllo), può richiedere una nuova trasmissione
* Con la correzione degli errori in avanti viene aggiunta una ridondanza aggiuntiva (ad esempio ulteriori bit di controllo)
* In questo modo non solo si rileva la presenza di un errore, ma anche la posizione in cui si trova $\rightarrow$ il bit errato può essere corretto
* In inglese si parla di *Forward Error Correction* (FEC)

---

[question:AE413]

---

[question:AE414]

---

## Codice di Hamming – Correzione degli errori nel dettaglio

* Il codice di Hamming utilizza più bit di parità per non solo rilevare, ma anche correggere gli errori
* Obiettivo: localizzare e correggere un singolo errore di bit

---

<left>
[picture:683:hamming1:Trasmissione di 11 bit]
</left>
<right>
* Esempio: trasmissione di una parola dati di 11 bit
* Obiettivo: rilevamento e correzione di un errore di bit
</right>

---

<left>
[picture:682:hamming2:Denominazione alfabetica delle posizioni dei bit]
</left>
<right>
* Le posizioni dei bit vengono denominate alfabeticamente per identificare le singole aree
</right>

---

<left>
[picture:684:hamming3:Riorganizzazione con bit aggiuntivi]
</left>
<right>
* Organizzazione dei bit dati con posizioni aggiuntive per i bit di parità
</right>

---

<left>
[picture:685:hamming4:Quattro bit di parità nel codice di Hamming]
</left>
<right>
* Invece di un singolo bit di controllo, vengono utilizzati quattro bit di parità ($p_1$–$p_4$)
* Questi coprono aree diverse dei bit dati, simile a un cruciverba
</right>

---

<left>
[picture:686:hamming5:Assegnazione delle aree di parità]
</left>
<right>
* Ogni bit di parità protegge una specifica area dei dati
</right>

---

<left>
[picture:687:hamming6:Calcolo dei bit di parità (parità pari)]
</left>
<right>
* Per ogni area, il bit di parità viene calcolato tramite parità pari
* Se si verifica un errore, è possibile identificare e correggere le aree errate
</right>

---

<left>
[picture:687:hamming6:Calcolo dei bit di parità (parità pari)]
</left>
<right>
* Combinando le aree di parità, è possibile determinare la posizione del bit errato
* Esempio: se un determinato bit (ad esempio il bit $k$) viene modificato durante la trasmissione, tutti i controlli di parità associati falliscono: l'errore si trova quindi nel bit $k$
