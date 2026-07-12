Nella modulazione di ampiezza (AM) un segnale di modulazione, ad esempio un segnale vocale, viene modulato sull'onda portante modificandone l'ampiezza. La frequenza della portante non viene influenzata dall'AM, ma rimane invariata.

Abbiamo già conosciuto il caso più semplice ed estremo con la trasmissione di segnali Morse tramite Continuous Wave (CW). L'accensione e lo spegnimento della portante a ritmo con la pressione del tasto Morse può anche essere descritto come un passaggio tra ampiezza minima e massima.

Per modulare un segnale vocale tramite AM, viene utilizzato anche il campo tra ampiezza minima e massima. Nel diagramma a cascata nella figura [ref:n_Wasserfall0] vediamo un segnale vocale modulato in ampiezza. Al centro si può riconoscere chiaramente la portante come una linea sottile a frequenza costante. Tuttavia, a sinistra e a destra della portante si vede anche qualcosa, sebbene la frequenza della portante non sia stata influenzata!

<margin>
[picture:716:n_Wasserfall0:Segnale di un trasmettitore radio AM (voce / musica)]
</margin>

Questo effetto inaspettato si verifica perché la modifica dell'ampiezza cambia la forma della portante e non corrisponde più a una pura oscillazione sinusoidale. Le frequenze aggiuntive le chiamiamo *bande laterali*. In esse si trova l'informazione trasmessa, cioè ad esempio la voce. Nella figura [ref:n_seitenband] vediamo una rappresentazione simbolica comune dell'AM con la portante al centro e le due bande laterali a sinistra e a destra.

<margin>
[picture:476:n_seitenband:Rappresentazione simbolica di un segnale modulato in ampiezza con portante e bande laterali]
</margin>

<webindepth>
*Perché nell'AM si creano frequenze aggiuntive accanto alla portante?* Questo può essere spiegato comprendendo cosa viene rappresentato esattamente in uno spettro di ampiezza o in un diagramma a cascata: indica per ogni frequenza quanto è grande l'ampiezza. Più precisamente dobbiamo dire: indica per tutte le possibili oscillazioni sinusoidali con diverse frequenze quanto è forte la loro ampiezza. Quindi, se l'indicazione ad esempio a $\qty{144,3}{\mega\hertz}$ aumenta, significa che viene misurata una pura oscillazione sinusoidale con una frequenza di $\qty{144,3}{\mega\hertz}$. Se invece l'indicazione aumenta contemporaneamente, ad esempio, a $\qty{144,300}{\mega\hertz}$ e a $\qty{144,301}{\mega\hertz}$, significa che sono state misurate due oscillazioni sinusoidali.

Con questa conoscenza, guardiamo di nuovo la trasmissione AM nel diagramma a cascata. Ora possiamo riconoscere che molte frequenze diverse tra $\qty{144,250}{\mega\hertz}$ e $\qty{144,350}{\mega\hertz}$ si presentano con ampiezze diverse. Quindi, molte oscillazioni sinusoidali diverse sono misurabili contemporaneamente.

[picture:738:n_seitenband_frequenzen_einzeln:Molteplici oscillazioni sinusoidali di frequenza diversa]

Resta la domanda del perché da una singola oscillazione sinusoidale, che viene deformata dalla modulazione, improvvisamente diventino più oscillazioni sinusoidali. Per rispondere a questo, guardiamo il percorso al contrario. Se si hanno più oscillazioni sinusoidali di frequenza diversa e le si sommano, si ottiene un'oscillazione "deformata"!

[picture:739:n_seitenband_frequenzen_addiert:Somma di molteplici oscillazioni sinusoidali di frequenza diversa]

Sono semplicemente due diverse prospettive. Si può interpretarlo sia come un'oscillazione deformata, sia come la somma di più oscillazioni sinusoidali. E questo è il motivo per cui la modifica dell'ampiezza di una portante porta a vedere frequenze aggiuntive accanto alla portante nel diagramma a cascata.
</webindepth>

[question:NE206]
[question:NE20]

Tra l'altro, la larghezza di banda occupata dall'AM è doppia rispetto alla frequenza più alta del segnale di modulazione. Nel nostro esempio della sezione precedente, la frequenza più alta era $\qty{2700}{\hertz}$. Di conseguenza, questa trasmissione come trasmissione AM occuperebbe una larghezza di banda di $\qty{5400}{\hertz}$.
