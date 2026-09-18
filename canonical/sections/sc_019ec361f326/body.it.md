Abbiamo già imparato a conoscere le tre grandezze più importanti dell'elettrotecnica, ovvero la tensione elettrica, la corrente elettrica e la resistenza:
* Prima di tutto, abbiamo imparato che le cariche elettriche vengono separate nelle sorgenti di tensione e che in questo modo si genera una tensione elettrica. La indichiamo con la lettera $U$ e la misuriamo in volt ($\unit{V}$).
* Poi abbiamo imparato che la tensione elettrica fa sì che in un circuito chiuso circoli una corrente elettrica, che indichiamo con la lettera $I$ e misuriamo in ampere ($\unit{A}$).
* E all'inizio di questo capitolo abbiamo imparato che i carichi in un circuito esercitano una resistenza e quindi rallentano il flusso di corrente. La resistenza viene indicata con la lettera $R$ e la misuriamo in ohm ($\unit{\ohm}$).

%<margin>
%[p-h-o-t-o:147:ohmsches_gesetz_comic:Rappresentazione grafica dei rapporti della legge di Ohm]
%</margin>

[question:NA203]

---

Ma come sono correlate queste tre grandezze? Guardiamo un esempio nell'immagine [ref:n_ohmsches_gesetz_stromkreis_mit_batterie]. Abbiamo un circuito composto da una batteria come sorgente di tensione e da una resistenza. Conosciamo la tensione e possiamo misurare la corrente. La batteria ha una tensione di $\qty{10}{\volt}$ e circola una corrente di $\qty{1}{\milli\ampere}$.

<margin>
[picture:664:n_ohmsches_gesetz_stromkreis_mit_batterie:Circuito con batteria]
</margin>

Se nella batteria dell'esempio si sostituisce la batteria da $\qty{10}{\volt}$ con una da $\qty{20}{\volt}$, anche la corrente aumenterebbe da $\qty{1}{\milli\ampere}$ a $\qty{2}{\milli\ampere}$. Se quindi si raddoppia la tensione, anche la corrente raddoppia. Allo stesso modo, la corrente si dimezzerebbe a $\qty{0,5}{\milli\ampere}$ se si dimezzasse la tensione a $\qty{5}{\volt}$.

Possiamo riconoscere uno schema: nell'esempio la tensione $U$ in volt è sempre 10000 volte maggiore della corrente $I$ in ampere. Oppure, espresso matematicamente:

$\dfrac{U}{I} = \dfrac{\qty{10}{\volt}}{\qty{0,001}{\ampere}} = \dfrac{\qty{20}{\volt}}{\qty{0,002}{\ampere}} = \dfrac{\qty{5}{\volt}}{\qty{0,0005}{\ampere}} = 10000 \frac{\unit{\volt}}{\unit{\ampere}}$

---

Nel linguaggio tecnico questo viene chiamato *proporzionalità*: $I$ è proporzionale a $U$. Trascurando le unità di misura, il cosiddetto *fattore di proporzionalità* nel nostro esempio è 10000: se si moltiplica un valore per 10000, si ottiene l'altro valore.
%Di nuovo, questo comportamento può essere paragonato a un circuito idraulico: se la pompa esercita una pressione maggiore, anche più acqua fluirà nel circuito.

<indepth>
Il *fattore di proporzionalità* è il rapporto numerico tra due grandezze che sono proporzionali tra loro.
</indepth>

Rimane però una domanda: da dove viene questo fattore di 10000? La risposta è semplice: è la nostra resistenza $R$! E se ora consideriamo anche le unità di misura, tutto torna: l'unità di misura ohm è infatti definita in modo che $\qty{1}{\ohm}$ sia equivalente a $\qty{1}{\volt\per\ampere}$. Pertanto, invece di $\qty{10000}{\volt\per\ampere}$ possiamo semplicemente scrivere $\qty{10000}{\ohm}$. La nostra resistenza è quindi $\qty{10000}{\ohm}$ o, in breve, $\qty{10}{\kilo\ohm}$:

$\qty{10000}{\volt\per\ampere} = \qty{10000}{\ohm}$

%Ma rimane ancora una domanda: perché nel nostro esempio circola esattamente $\qty{1}{\milli\ampere}$ quando la tensione è $\qty{10}{\volt}$? L'entità della corrente dipende dal valore della resistenza. Se la resistenza è grande, la corrente sarà piccola; se invece la resistenza è piccola, la corrente sarà grande.

Abbiamo imparato che il valore della resistenza può essere calcolato dalla tensione e dalla corrente. È il *rapporto tra tensione e corrente*, o in altre parole: se si divide la tensione per la corrente, si ottiene il valore della resistenza.

---

Questa relazione può essere rappresentata dalla seguente formula, nota come *legge di Ohm*:

$ R = \dfrac{U}{I} $

<person>
Il fisico tedesco *Georg Simon Ohm* ha scoperto nel 1826 la relazione tra tensione elettrica, corrente elettrica e resistenza. In suo onore, la formula $ R = \frac{U}{I} $ è chiamata legge di Ohm.
</person>

[question:NB505]

Se però si conoscono solo la resistenza e la tensione e si vuole calcolare la corrente corrispondente, la legge di Ohm può essere utilizzata come segue:

$ I = \dfrac{U}{R} $

Nel caso in cui si conoscano solo la resistenza e la corrente e si voglia calcolare la tensione corrispondente, esiste un'altra variante della formula:

$ U = R\cdot I $

[question:NB504]

Non è necessario ricordare necessariamente queste formule. Si trovano anche nella *raccolta di formule*, che viene fornita come strumento ausiliario durante l'esame. Per i calcoli, durante l'esame è possibile utilizzare una calcolatrice.

[question:NB502]
[question:NB503]
[question:NB501]
