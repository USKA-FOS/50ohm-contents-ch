## Misurazione della frequenza nei ricevitori

* La frequenza di ricezione di solito non può essere misurata direttamente, poiché non è disponibile un punto di misurazione.
* Per il controllo, un oscillatore o un generatore di frequenza preciso viene collegato alla presa dell'antenna.
* Confronto della frequenza del generatore con l'indicazione del ricevitore.
* Gli oscillatori/OCXO sincronizzati con GPS offrono una maggiore precisione.

<note>
Un generatore di frequenza collegato direttamente può danneggiare leggermente l'ingresso del ricevitore. In caso di dubbio, la misurazione dovrebbe iniziare con la tensione più bassa del generatore e un attenuatore.
</note>

---

[question:AI511]

---

[question:AI504]

---

## Misurazione della frequenza nei trasmettitori

* La misurazione della frequenza nei trasmettitori è più semplice.
* Un frequenzimetro viene collegato alla presa dell'antenna tramite un attenuatore.
* La misurazione è sensata solo con una portante non modulata.

<note>
I trasmettitori SSB non generano alcun segnale senza modulazione. Per misurare la loro frequenza di trasmissione, si può immettere un segnale audio di frequenza nota nella presa del microfono. Con USB, la frequenza audio viene sottratta dal valore di misurazione del frequenzimetro all'uscita del trasmettitore, con LSB viene aggiunta.
</note>

---

[question:AI502]

---

[question:AI501]

---

* La misurazione della frequenza tramite oscilloscopio è solo un rimedio di emergenza, poiché questi apparecchi hanno raramente una base dei tempi precisa come i frequenzimetri.

---

[question:AI503]

---

* I frequenzimetri semplici lavorano quasi sempre con un cosiddetto *tempo di gate*.
* L'apparecchio collega l'ingresso per un tempo definito, conta i periodi e calcola da questi la frequenza.
* Un tempo di gate di $\qty{1}{\second}$ fornisce direttamente la frequenza in $\unit{\hertz}$.
* Tempo di gate breve: aggiornamento rapido.
* Tempo di gate lungo: maggiore precisione di misurazione.

---

[question:AI505]


