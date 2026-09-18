Nella modulazione di ampiezza (AM), un segnale di modulazione, ad esempio un segnale vocale, viene impresso sulla portante modificando l'ampiezza. La frequenza della portante non viene influenzata nella AM e rimane invariata.

Il caso più semplice e al contempo estremo l'abbiamo già incontrato con la trasmissione di caratteri Morse tramite Continuous Wave (CW). L'accensione e lo spegnimento della portante seguendo il ritmo della manipolazione del tasto Morse può essere descritto anche come alternanza tra ampiezza minima e massima.

Per modulare un segnale vocale tramite AM, viene sfruttato anche l'intervallo tra ampiezza minima e massima. Nel diagramma a cascata nell'immagine [ref:n_Wasserfall0] vediamo un segnale vocale modulato in ampiezza. Al centro si può riconoscere chiaramente la portante come una linea sottile con frequenza costante. Tuttavia, a sinistra e a destra della portante si vedono anche delle componenti, nonostante la frequenza della portante non sia stata modificata!

<margin>
[picture:716:n_Wasserfall0:Segnale di una stazione radio AM (voce / musica)]
</margin>

Questo effetto inaspettato si verifica perché la modifica dell'ampiezza altera la forma della portante, che non corrisponde più a un'oscillazione sinusoidale pura. Le frequenze aggiuntive vengono definite *bande laterali*. In queste bande è contenuta l'informazione trasmessa, ad esempio la voce. Nell'immagine [ref:n_seitenband] vediamo una rappresentazione simbolica usuale della AM con la portante al centro e le due bande laterali a sinistra e a destra.

<margin>
[picture:476:n_seitenband:Rappresentazione simbolica di un segnale modulato in ampiezza con portante e bande laterali]
</margin>

<webindepth>
*Perché nella AM si generano frequenze aggiuntive accanto alla portante?* Questo può essere spiegato se si comprende cosa viene rappresentato esattamente in uno spettro di ampiezza o in un diagramma a cascata: esso mostra, per ogni frequenza, quanto è grande l'ampiezza. Più precisamente, dobbiamo dire: mostra, per tutte le possibili oscillazioni sinusoidali con diverse frequenze, quanto è forte la loro ampiezza. Se quindi, ad esempio, la visualizzazione indica $\qty{144,3}{\mega\hertz}$, allora viene misurata un'oscillazione sinusoidale pura con una frequenza di $\qty{144,3}{\mega\hertz}$. Se invece la visualizzazione indica contemporaneamente, ad esempio, $\qty{144,300}{\mega\hertz}$ e $\qty{144,301}{\mega\hertz}$, allora sono state misurate due oscillazioni sinusoidali.

Con questa conoscenza, consideriamo di nuovo la trasmissione AM nel diagramma a cascata. Ora possiamo riconoscere che tra $\qty{144,250}{\mega\hertz}$ e $\qty{144,350}{\mega\hertz}$ compaiono molte frequenze diverse con ampiezze differenti. Quindi sono misurabili contemporaneamente molte oscillazioni sinusoidali diverse.

[picture:738:n_seitenband_frequenzen_einzeln:Più oscillazioni sinusoidali con frequenze diverse]

Rimane la domanda: perché da un'unica oscillazione sinusoidale, deformata tramite modulazione, si generano improvvisamente più oscillazioni sinusoidali? Per rispondere, consideriamo il processo al contrario. Se si hanno più oscillazioni sinusoidali con frequenze diverse e le si sommano, si ottiene un'oscillazione "deformata"!

[picture:739:n_seitenband_frequenzen_addiert:Somma di più oscillazioni sinusoidali con frequenze diverse]

Si tratta semplicemente di due punti di vista diversi. Si può interpretare il risultato come un'oscillazione deformata oppure come somma di più oscillazioni sinusoidali. Ed è questo il motivo per cui la modifica dell'ampiezza di una portante porta a vedere, nel diagramma a cascata, ulteriori frequenze accanto alla portante.
</webindepth>

[question:NE202]
[question:NE206]

Tra l'altro, la larghezza di banda occupata dalla AM è doppia rispetto alla frequenza più alta del segnale di modulazione. Nel nostro esempio del paragrafo precedente, la frequenza più alta era $\qty{2700}{\hertz}$. Di conseguenza, questo segnale, trasmesso come AM, occuperebbe una larghezza di banda di $\qty{5400}{\hertz}$.