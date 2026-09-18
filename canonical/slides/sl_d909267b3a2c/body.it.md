## Rilevamento errori: Bit di parità

* Viene aggiunto un bit di controllo (bit di parità) ai dati trasmessi
* Due varianti:
* *Parità pari*: il numero di 1 viene impostato a un valore pari
* *Parità dispari*: il numero di 1 viene impostato a un valore dispari
* Trasmettitore e ricevitore devono concordare il metodo utilizzato

---

## Parità pari: Esempio 1

<left>
[picture:677:byte:Un byte]
</left>
<right>
* Byte da trasmettere
* Vengono contati 5 uno → numero dispari
* Il bit di parità deve essere impostato a $\num{1}$ per ottenere un numero pari
</right>

---

<left>
[picture:678:even_parity:Il byte con bit di parità pari]
</left>
<right>
* Il bit di parità è stato impostato a $\num{1}$
* Il byte risultante ha un numero pari di uno
* In caso di errore di trasmissione il bit di parità non corrisponde più
</right>

---

## Parità pari: Esempio 2

<left>
[picture:679:even_parity:Byte con bit di parità pari]
</left>
<right>
* Byte originale: 4 uno (pari)
* Il bit di parità viene impostato a $\num{0}$
</right>

---
## Rilevamento errori in caso di errori di bit

* In caso di un errore a un bit la parità viene invertita → errore rilevato
* In caso di due errori la parità rimane invariata → errore non rilevato
* In caso di tre errori la parità viene nuovamente modificata → errore rilevato

---

[question:AE411]

---

[question:AE412]

---

## Rilevamento errori avanzato

* Bit di controllo aggiuntivi possono rilevare errori su più bit
* Per messaggi variabili vengono spesso utilizzati metodi di controllo come il *controllo di ridondanza ciclica (CRC)*
* Il CRC rileva errori fino a una certa probabilità residua

<note>
Viene utilizzato nell’IBAN o nei numeri di documento
</note>

---

[question:AE410]