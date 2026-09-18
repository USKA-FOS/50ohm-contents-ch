Noi esseri umani siamo abituati a utilizzare le dieci cifre da $\num{0}$ a $\num{9}$. Si parla di sistema decimale o sistema a base dieci.

Per un computer, invece, è più semplice lavorare con sole $\num{2}$ cifre: $\num{0}$ e $\num{1}$. Questo corrisponde a due stati: ad esempio, spento e acceso, "transistor interdetto" e "transistor in conduzione" o anche $\qty{0}{\volt}$ e $\qty{5}{\volt}$. Si ottiene così un sistema numerico binario o sistema a base due.

[question:EA201]

Il conteggio funziona allo stesso modo in tutti i sistemi numerici (vedi tabella [ref:binaer_zahlensysteme]): si parte da $\num{0}$ e si incrementano le cifre. Quando si esaurisce la disponibilità di cifre, si ricomincia da capo e si antepone un $\num{1}$ a ogni numero. Per questo motivo, nel sistema decimale dopo il $\num{9}$ viene il $\num{10}$. La cifra più a destra ha il valore che rappresenta. Questo valore è detto valore posizionale $\num{1}$.

---

Nel sistema decimale, la seconda cifra da destra vale dieci volte il suo valore, quindi ha un valore posizionale $\num{10}$. Ogni cifra che si trova più a sinistra vale dieci volte quella alla sua destra. Ad esempio, il numero decimale $\num{5573}$ della tabella [ref:binaer_stellenwert_dezimal] significa in realtà $5 \cdot 1000 + 5 \cdot 100 + 7 \cdot 10 + 3 \cdot 1$.

<margin>
|c: |c: |c: |c: |
|$\num{1000}$ | $\num{100}$ | $\num{10}$ | $\num{1}$ |
| $\num{5}$ | $\num{5}$ | $\num{7}$ | $\num{3}$ |
[table:binaer_stellenwert_dezimal:Valori posizionali del numero decimale a quattro cifre $\num{5573}$]

|r: Decimale | r: Binario |
| $\num{0}$ | $\num{0}$ |
| $\num{1}$ | $\num{1}$ |
| $\num{2}$ | $\num{10}$ |
| $\num{3}$ | $\num{11}$ |
| $\num{4}$ | $\num{100}$ |
| $\num{5}$ | $\num{101}$ |
| $\num{6}$ | $\num{110}$ |
| $\num{7}$ | $\num{111}$ |
| $\num{8}$ | $\num{1000}$ |
| $\num{9}$ | $\num{1001}$ |
| $\num{10}$ | $\num{1010}$ |
| $\num{11}$ | $\num{1011}$ |
| $\num{12}$ | $\num{1100}$ |
| $\num{13}$ | $\num{1101}$ |
| $\num{14}$ | $\num{1110}$ |
| $\num{15}$ | $\num{1111}$ |
[table:binaer_zahlensysteme:Numeri nei sistemi decimale e binario]
</margin>

Nel sistema binario ci sono solo due cifre, cioè $\num{0}$ e $\num{1}$. Come si vede nella tabella [ref:binar_stellenwert_dual], la prima cifra da destra ha valore posizionale $\num{1}$, la seconda $\num{2}$, la terza $\num{4}$, la quarta $\num{8}$ e così via. I valori posizionali si raddoppiano invece di moltiplicarsi per dieci, perché ci sono solo due cifre e non dieci. Una cifra nel sistema binario è anche chiamata bit ($\unit{\bit}$).

|c: |c: |c: |c: |c: |c: |c: |c: |
| $\num{128}$ | $\num{64}$ | $\num{32}$ | $\num{16}$ | $\num{8}$ | $\num{4}$ | $\num{2}$ | $\num{1}$ |
| $\num{1}$ | $\num{0}$ | $\num{0}$ | $\num{0}$ | $\num{1}$ | $\num{1}$ | $\num{1}$ | $\num{0}$ |
[table:binar_stellenwert_dual:Valori posizionali del numero binario a otto cifre $\num{10001110}$]

Se si conoscono i valori posizionali, convertire i numeri binari in numeri decimali è semplice. Prendiamo un esempio dalla tabella [ref:binar_stellenwert_dual]. Il numero binario $\num{10001110}$ deve essere convertito in un numero decimale.

1. Si scrivono sopra ogni cifra del numero binario il suo valore posizionale.
2. Si sommano tutti i valori posizionali sotto i quali c'è un $\num{1}$: $128+8+4+2=142$

[question:EA206]
[question:EA207]
[question:EA208]

Su carta si possono scrivere numeri binari con quanti bit servono. Nella tecnologia digitale è diverso. L'hardware o il software impone un numero specifico di cifre, detto anche larghezza. Ad esempio, i microcontrollori o i computer hanno spesso larghezze di $\num{8}$, $\num{16}$, $\num{32}$ o $\qty{64}{\text{bit}}$. Nella rappresentazione, i numeri binari vengono spesso riempiti con zeri iniziali fino a raggiungere questa larghezza. Questo non cambia il valore del numero.

[question:EA205]

Una larghezza fissa limita l'intervallo di valori. Con un bit sono possibili due valori ($\num{0}$ e $\num{1}$), con due bit già quattro ($\num{00}$, $\num{01}$, $\num{10}$ e $\num{11}$) e con ogni bit aggiuntivo il numero raddoppia. Con $n$ bit si possono rappresentare $2^n$ numeri diversi.

[question:EA204]
[question:EA202]
[question:EA203]
