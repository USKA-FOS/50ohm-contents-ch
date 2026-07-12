Il modo più semplice per rilevare errori è aggiungere un bit aggiuntivo, il bit di parità. Viene chiamato anche *Parity Bit*. Esistono due varianti di questa procedura. Con la parità pari (*Even Parity*), il valore di questo bit viene scelto per ogni blocco in modo che il numero di bit impostati su $\num{1}$ sia sempre pari. Con la parità dispari (*Odd Parity*), invece, il numero deve essere sempre dispari. Il trasmettitore e il ricevitore devono concordare prima della trasmissione quale delle due varianti verrà utilizzata.

<indepth>
Supponiamo di voler trasmettere il seguente byte con parità pari (*Even Parity*):

[picture:677:byte:Un Byte]

Contiamo 5 uni, quindi un numero dispari. Il bit di parità deve quindi essere impostato su $\num{1}$ per ottenere un numero pari di uni:

[picture:678:even_parity:Il Byte con Bit di Parità Pari]

Se ora un errore di trasmissione modifica *un* bit (da $\num{1}$ a $\num{0}$ o viceversa), il numero di uni diventa dispari. Il ricevitore lo riconosce come un errore.

Segue un altro esempio:

[picture:679:even_parity:Byte con Parità Pari]

Nel byte originale contiamo 4 uni, che corrisponde a un numero pari. Pertanto, dobbiamo inserire uno $\num{0}$ come bit di parità.
</indepth>

Questa procedura raggiunge rapidamente i suoi limiti, ovvero quando si verificano più di un errore durante la trasmissione. Se due bit vengono modificati durante la trasmissione, il numero di uni rimane pari. Il ricevitore non può più riconoscere che si sono verificati errori. Se si verificano tre errori durante la trasmissione, si ottiene nuovamente un numero dispari di uni e il ricevitore riconosce gli errori.

La parità dispari (*Odd Parity*) funziona in linea di principio allo stesso modo, con una sola differenza: il numero di uni non deve essere pari, ma sempre dispari. Per la parità dispari vale quanto vale per la parità pari, ovvero che viene riconosciuto solo un numero dispari di bit trasmessi erroneamente. Una trasmissione priva di errori, d'altra parte, non può essere distinta da un numero pari di errori.

[question:AE411]
[question:AE412]

Per rilevare errori multi-bit, è possibile aggiungere ulteriori bit di parità. Questo funziona molto bene con messaggi di lunghezza fissa. Se la lunghezza dei dati è variabile, si utilizzano spesso procedure speciali di somma di controllo come il *controllo di ridondanza ciclica (CRC)*, che rileva errori fino a una certa probabilità residua. Procedure simili si trovano anche nella vita di tutti i giorni, ad esempio nei numeri di identificazione o nell'IBAN.

[question:AE410]
