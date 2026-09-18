Il modo più semplice per rilevare gli errori consiste nell'aggiungere un bit aggiuntivo, il bit di parità. Viene anche chiamato *Parity Bit*. Esistono due varianti di questo metodo. Con la *parità pari* (*Even Parity*), il valore di questo bit viene scelto per ogni blocco in modo che il numero di bit impostati a $\num{1}$ sia sempre pari. Con la *parità dispari* (*Odd Parity*), invece, il numero deve essere sempre dispari. Trasmettitore e ricevitore devono accordarsi prima della trasmissione su quale delle due varianti verrà utilizzata.

<indepth>
Supponiamo di voler trasmettere il seguente byte con parità pari:

[picture:677:byte:Un byte]

Contiamo 5 uno, quindi un numero dispari. Il bit di parità deve quindi essere impostato a $\num{1}$ per ottenere un numero pari di uno:

[picture:678:even_parity:Il byte con il bit di parità pari]

Se durante la trasmissione si verifica un errore che altera *un solo* bit (da $\num{1}$ a $\num{0}$ o viceversa), il numero di uno diventa dispari. Il ricevitore rileva così la presenza di un errore.

Ecco un altro esempio:

[picture:679:even_parity:Byte con parità pari]

Nel byte originale contiamo 4 uno, che corrisponde a un numero pari. Pertanto, dobbiamo inserire come bit di parità un $\num{0}$.
</indepth>

Questo metodo ha però dei limiti: quando durante la trasmissione si verificano più di un errore, la situazione cambia. Se due bit vengono alterati durante la trasmissione, il numero di uno rimane pari. Il ricevitore non può più rilevare la presenza di errori. Se invece si verificano tre errori, il numero di uno diventa dispari e il ricevitore rileva gli errori.

La parità dispari funziona in linea di principio allo stesso modo, con una sola differenza: il numero di uno deve essere dispari, non pari. Anche con la parità dispari, come con quella pari, vengono rilevati solo un numero dispari di bit trasmessi in modo errato. Tuttavia, non è possibile distinguere una trasmissione senza errori da un numero pari di errori.

[question:AE411]
[question:AE412]

Per rilevare errori su più bit, è possibile aggiungere ulteriori bit di parità. Questo metodo funziona molto bene per messaggi di lunghezza fissa. Se la lunghezza dei dati è variabile, si utilizzano spesso metodi di controllo della somma come il *controllo di ridondanza ciclica (CRC)*, che rileva gli errori con una certa probabilità residua. Metodi simili si trovano anche nella vita quotidiana, ad esempio nei numeri di documento d'identità o nell'IBAN.

[question:AE410]