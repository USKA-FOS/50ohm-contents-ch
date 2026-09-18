## Misurazione della frequenza nei ricevitori

* La frequenza di ricezione di solito non può essere misurata direttamente, poiché non è disponibile un punto di misura
* Per verificare la frequenza, un oscillatore o generatore di frequenza preciso viene collegato alla presa dell'antenna
* Confronto tra la frequenza del generatore e l'indicazione del ricevitore
* Gli oscillatori/OCXO sincronizzati con GPS offrono una maggiore precisione

<note>
Un generatore di frequenza collegato direttamente può danneggiare facilmente un ingresso del ricevitore. In caso di dubbio, la misurazione dovrebbe iniziare con la tensione più bassa del generatore e con un attenuatore.
</note>

---

[question:AI511]

---

[question:AI504]

---

## Misurazione della frequenza nei trasmettitori

* La misurazione della frequenza nei trasmettitori è più semplice
* Un frequenzimetro viene collegato tramite un attenuatore alla presa dell'antenna
* La misurazione è significativa solo con la portante non modulata

<note>
I trasmettitori SSB non generano alcun segnale senza modulazione. Per misurare la loro frequenza di trasmissione, è possibile iniettare un segnale audio di frequenza nota nella presa del microfono. Per USB, la frequenza audio viene sottratta dal valore misurato dal frequenzimetro all'uscita del trasmettitore, mentre per LSB viene aggiunta.
</note>

---

[question:AI502]

---

[question:AI501]

---

* La misurazione della frequenza tramite oscilloscopio è solo un ripiego, poiché questi apparecchi raramente hanno una base temporale accurata come i frequenzimetri.

---

[question:AI503]

---

* I frequenzimetri semplici funzionano quasi sempre con un cosiddetto *tempo di porta*
* L'apparecchio attiva l'ingresso per un tempo determinato, conta i periodi e calcola da essi la frequenza
* Un tempo di porta di $\qty{1}{\second}$ fornisce direttamente la frequenza in $\unit{\hertz}$
* Tempo di porta breve: aggiornamento rapido
* Tempo di porta lungo: maggiore precisione di misura

---

[question:AI505]