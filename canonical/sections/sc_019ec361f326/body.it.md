Abbiamo già conosciuto le tre grandezze più importanti dell'elettrotecnica, ovvero la tensione elettrica, la corrente elettrica e la Resistenza:
* Innanzitutto, abbiamo imparato che le cariche elettriche vengono separate nelle fonti di tensione e che ciò crea una tensione elettrica. La indichiamo con la lettera $U$ e la misuriamo in volt ($\unit{V}$).
* Poi, abbiamo imparato che la tensione elettrica fa sì che in un circuito chiuso scorra una corrente elettrica, che indichiamo con la lettera $I$ e misuriamo in ampere ($\unit{A}$).
* E all'inizio di questo capitolo, abbiamo imparato che i consumatori in un circuito oppongono una Resistenza e quindi rallentano il flusso di corrente. La Resistenza la indichiamo con la lettera $R$ e la misuriamo in ohm ($\unit{\ohm}$).

%<margin>
%[p-h-o-t-o:147:ohmsches_gesetz_comic:Rappresentazione grafica delle relazioni della Legge di Ohm]
%</margin>

[question:NA203]

---

Ma come sono collegate queste tre grandezze? Diamo un'occhiata a un esempio nella figura [ref:n_ohmsches_gesetz_stromkreis_mit_batterie]. Abbiamo un circuito composto da una batteria come fonte di tensione e una Resistenza. Conosciamo la tensione e possiamo misurare la corrente. La batteria ha una tensione di $\qty{10}{\volt}$ e scorre una corrente di $\qty{1}{\milli\ampere}$.

<margin>
[picture:664:n_ohmsches_gesetz_stromkreis_mit_batterie:Circuito con batteria]
</margin>

Se la batteria da $\qty{10}{\volt}$ nell'esempio venisse sostituita con una batteria da $\qty{20}{\volt}$, anche la corrente da $\qty{1}{\milli\ampere}$ aumenterebbe a $\qty{2}{\milli\ampere}$. Quindi, se si raddoppia la tensione, si raddoppia anche la corrente. Allo stesso modo, la corrente si dimezzerebbe a $\qty{0,5}{\milli\ampere}$ se la tensione venisse dimezzata a $\qty{5}{\volt}$.

Possiamo riconoscere uno schema: nel nostro esempio, la tensione $U$ in volt è sempre 10000 volte maggiore della corrente $I$ in ampere. O espresso matematicamente:

$\dfrac{U}{I} = \dfrac{\qty{10}{\volt}}{\qty{0,001}{\ampere}} = \dfrac{\qty{20}{\volt}}{\qty{0,002}{\ampere}} = \dfrac{\qty{5}{\volt}}{\qty{0,0005}{\ampere}} = 10000 \frac{\unit{\volt}}{\unit{\ampere}}$

---

Nel linguaggio tecnico, questo si chiama proporzionalità: $I$ è proporzionale a $U$. Lasciando da parte le unità, il cosiddetto *fattore di proporzionalità* nel nostro esempio è 10000: se si moltiplica un valore per 10000, si ottiene l'altro valore.
%Possiamo anche immaginare questo comportamento di nuovo nel ciclo dell'acqua: se la pompa pompa con più pressione, scorrerà anche più acqua nel ciclo.

<indepth>
Il *fattore di proporzionalità* è il rapporto numerico tra due grandezze che sono proporzionali tra loro.
</indepth>

Rimane una domanda. Da dove viene questo fattore di 10000? La risposta è semplice: è la nostra Resistenza $R$! E se consideriamo anche le unità, si forma un quadro completo: l'unità ohm è definita in modo tale che $\qty{1}{\ohm}$ sia lo stesso di $\qty{1}{\volt\per\ampere}$. Pertanto, possiamo scrivere $\qty{10000}{\ohm}$ invece di $\qty{10000}{\volt\per\ampere}$! La nostra Resistenza è quindi $\qty{10000}{\ohm}$ o, in breve, $\qty{10}{\kilo\ohm}$:

$\qty{10000}{\volt\per\ampere} = \qty{10000}{\ohm}$

%Rimane ancora la seguente domanda: perché nel nostro esempio scorrono esattamente $\qty{1}{\milli\ampere}$ quando la tensione è di $\qty{10}{\volt}$? L'entità della corrente dipende dal valore della Resistenza. Se la Resistenza è grande, la corrente sarà piccola; se la Resistenza è piccola, la corrente sarà grande.

Abbiamo imparato: il valore della Resistenza può essere calcolato dalla tensione e dalla corrente. È il *rapporto tra tensione e corrente*, o in altre parole: se si divide la tensione per la corrente, si ottiene il valore della Resistenza.

---

Questa relazione può essere rappresentata dalla seguente formula, chiamata *Legge di Ohm*: 

$ R = \dfrac{U}{I} $

<person>
Il fisico tedesco *Georg Simon Ohm* scoprì nel 1826 la relazione tra la tensione elettrica, la corrente elettrica e la Resistenza. In suo onore, la formula $ R = \frac{U}{I} $ è chiamata Legge di Ohm.
</person>

[question:NB505]

Se invece si conosce solo la Resistenza e la tensione e si vuole calcolare la corrente corrispondente, si può usare la Legge di Ohm nel seguente modo: 

$ I = \dfrac{U}{R} $

Nel caso in cui si conoscano solo la Resistenza e la corrente e si voglia calcolare la tensione corrispondente, esiste un'altra variante della formula: 

$ U = R\cdot I $

[question:NB504]

Non è necessario memorizzare queste formule. Si trovano anche nella raccolta di formule, che viene fornita come ausilio durante l'esame. Per i calcoli, è possibile utilizzare una calcolatrice durante l'esame.

[question:NB502]
[question:NB503]
[question:NB501]
