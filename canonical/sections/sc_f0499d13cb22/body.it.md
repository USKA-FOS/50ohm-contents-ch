Ci sono pochi apparecchi radio per i quali è possibile misurare direttamente la frequenza di ricezione. I circuiti del ricevitore usuali non presentano un punto in cui questa sia presente. Pertanto, per verificare l'indicazione della frequenza, si collega un oscillatore o un generatore di frequenza il più preciso possibile alla presa dell'antenna. La sua frequenza viene confrontata con l'indicazione sul ricevitore.

<attention>
Un generatore di frequenza collegato direttamente può danneggiare facilmente l'ingresso di un ricevitore. In caso di dubbio, la misurazione dovrebbe iniziare con la tensione più bassa del generatore e un attenuatore.
</attention>

Naturalmente, anche qui vale che gli oscillatori disciplinati da GPS e gli OCXO sono di norma più precisi dei circuiti più semplici.

[question:AI511]
[question:AI504]

---

Con i trasmettitori, la misurazione della frequenza è più semplice. Un frequenzimetro viene collegato tramite un attenuatore alla presa dell'antenna. Naturalmente, questa misurazione ha senso solo con una portante non modulata.

<indepth>
I trasmettitori SSB non generano alcun segnale senza modulazione. Per misurare la loro frequenza di trasmissione, si può immettere un segnale audio di frequenza nota nella presa del microfono. Dal valore di misurazione del frequenzimetro all'uscita del trasmettitore, per USB viene sottratta la frequenza audio per ottenere la frequenza della portante non trasmessa. Per LSB viene aggiunta.
</indepth>

% AI502
[question:AI502]


[question:AI501]


% TODO Il testo è ancora in fase di scrittura. - DB7YI 2024-04-22

La misurazione della frequenza tramite oscilloscopio è solo un ripiego, poiché questi apparecchi hanno raramente una base dei tempi precisa come i frequenzimetri.
% AI503
[question:AI503]

I frequenzimetri semplici lavorano quasi sempre con un cosiddetto *tempo di gate*. L'apparecchio apre l'ingresso per un determinato tempo, conta i periodi del segnale di ingresso e ne calcola la frequenza. Questo è particolarmente semplice con un tempo di gate di un secondo, poiché fornisce direttamente il numero di oscillazioni al secondo e quindi la frequenza in hertz.

Il tempo di gate può essere impostato sulla maggior parte dei frequenzimetri. Un tempo di gate breve assicura che l'indicazione venga aggiornata a brevi intervalli. Con un tempo di gate lungo, invece, la misurazione diventa più precisa.

% TODO Immagine che illustra l'imprecisione con un tempo di gate breve

%AI505
[question:AI505]

% Le cinque domande su precisione e tolleranza, che originariamente si trovavano qui, sono state spostate nella sezione "Precisione della frequenza". - DB7YI 2024-04-28