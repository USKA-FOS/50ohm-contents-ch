Nella raccolta di formule troviamo la seguente formula per il calcolo della frequenza di taglio dei circuiti RC, ad esempio dei filtri passa-alto o passa-basso:

$f_g = \frac{1}{2 \pi \cdot R \cdot C}$

Con questa formula possiamo risolvere una serie di domande d’esame.

<indepth>
Per i lettori interessati alla matematica: la formula per la frequenza di taglio di un circuito RC può essere derivata considerando le impedenze complesse di resistenza e condensatore. Consideriamo il filtro passa-basso RC come un partitore di tensione dipendente dalla frequenza.

[picture:175:a_rc_tiepass:Circuito RC passa-basso come partitore di tensione dipendente dalla frequenza]

Per il rapporto tra tensione d’uscita e tensione d’ingresso vale:

$\frac{|U_A|}{|U_E|} = \frac{|X_C|}{|R + X_C|}$

La reattanza capacitiva del condensatore è data da:

$X_C = \frac{1}{j\omega C}$

Da cui si ottiene:

$\frac{|U_A|}{|U_E|} = \frac{\left|\frac{1}{j\omega C}\right|}{\left|R + \frac{1}{j\omega C}\right|}$

Per i valori assoluti otteniamo:

$\frac{|U_A|}{|U_E|} = \frac{\frac{1}{\omega C}}{\sqrt{R^2 + \frac{1}{\omega^2 C^2}}}$

Moltiplicando numeratore e denominatore per $\omega C$, l’espressione si semplifica in:

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{1 + R^2\omega^2 C^2}}$

La frequenza di taglio è definita come il punto in cui la tensione d’uscita scende al fattore $\frac{1}{\sqrt{2}} \approx 0{,}707$ del valore originale. Questo corrisponde a circa il 70% della tensione d’uscita o a una riduzione del livello di $\qty{3}{\dB}$.

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{2}}$

Da cui segue:

$\frac{1}{\sqrt{1 + R^2\omega^2 C^2}} = \frac{1}{\sqrt{2}}$

Pertanto, deve valere:

$R^2\omega^2 C^2 = 1$

e quindi:

$\omega R C = 1$

Con $\omega = 2\pi f$ si ottiene:

$2\pi f_g R C = 1$

Da cui deriva la formula per la frequenza di taglio:

$f_g = \frac{1}{2\pi R C}$
</indepth>

[question:AD201]
[question:AD202]
[question:AD203]

---

Il diagramma del modulo della risposta in frequenza di un circuito oscillante serie composto da una resistenza, un’induttanza e un condensatore, come mostrato nella figura [ref:a_serienschwingkreis], si calcola con la seguente formula:

$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$

<margin>
[picture:181:a_serienschwingkreis:Circuito oscillante serie]
</margin>

---

Quando la reattanza dell’induttanza è esattamente uguale alla reattanza del condensatore, cioè $X_\text{L} = X_\text{C}$, l’impedenza risulta:

$Z=\sqrt{R^2+\left(0\right)^2}=\sqrt{R^2}=R$

In questo caso si parla di *frequenza di risonanza* $f_0$ del circuito oscillante, in cui l’impedenza è determinata esclusivamente dalla resistenza ohmica. A frequenze superiori o inferiori alla frequenza di risonanza, l’impedenza è maggiore della resistenza ohmica, poiché o l’induttanza o il condensatore presentano una reattanza più elevata. La figura [ref:a_serienschwingkreis_frequenzgang] mostra il diagramma del modulo della risposta in frequenza di un circuito oscillante serie, in cui la frequenza di risonanza è chiaramente riconoscibile. A frequenze superiori e inferiori alla frequenza di risonanza, il circuito oscillante serie presenta un’elevata impedenza totale. A frequenza elevata, l’induttanza presenta un’elevata resistenza; a frequenza bassa, il condensatore presenta un’elevata resistenza.

<margin>
[picture:1037:a_serienschwingkreis_frequenzgang:Diagramma del modulo della risposta in frequenza di un circuito oscillante serie]
</margin>

[question:AD206]
[question:AD207]
[question:AD204]

Nei circuiti oscillanti paralleli e serie, come mostrato sopra, vale la seguente relazione in condizioni di risonanza:

$X_\text{C} = X_\text{L}$

Se inseriamo le formule per le reattanze di induttanza e condensatore nella relazione precedente, otteniamo:

$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$

Da cui deriva la formula:

$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$

---

Questa formula è nota come formula di Thomson e vale sia per i circuiti oscillanti paralleli che per quelli serie. Nella raccolta di formule, la troviamo nella sezione "circuiti oscillanti". Essa afferma che la frequenza di risonanza di un circuito oscillante dipende esclusivamente dall’induttanza della bobina e dalla capacità del condensatore. Le resistenze ohmiche e le perdite non influenzano la frequenza di risonanza. Con questa formula possiamo calcolare la frequenza di risonanza dei circuiti oscillanti.

<indepth>
Le resistenze ohmiche nei circuiti oscillanti paralleli e serie influenzano tuttavia il fattore di qualità ($Q$) e, di conseguenza, la larghezza di banda ($B$) del circuito oscillante. Su questo argomento torneremo in seguito in modo più approfondito.
</indepth>

[question:AD208]
[question:AD209]
[question:AD210]

---

La frequenza di risonanza dei circuiti oscillanti paralleli si calcola esattamente come per quelli serie, utilizzando la formula di Thomson già citata.

[question:AD211]
[question:AD212]

---

Per modificare la frequenza di risonanza di un circuito oscillante, è possibile variare l’induttanza della bobina o la capacità del condensatore nel circuito.
Come si evince dalla formula di Thomson, le grandezze $L$ e $C$ si trovano entrambe al denominatore. Pertanto, un aumento di $L$ o $C$ comporta una riduzione della frequenza del circuito oscillante, poiché il denominatore della formula diventa più grande. Viceversa, una diminuzione di $L$ e $C$ comporta un aumento della frequenza di risonanza del circuito oscillante.

<indepth>
La radice quadrata non influisce su questa relazione, poiché la radice di un numero più grande è anch’essa un numero più grande. Tuttavia, la relazione non è lineare.
</indepth>

L’induttanza di una bobina può essere aumentata aumentando il numero di spire, avvicinando le spire o inserendo un nucleo in ferrite. Al contrario, l’induttanza di una bobina può essere ridotta diminuendo il numero di spire, allontanando le spire, rimuovendo un nucleo in ferrite o inserendo un nucleo in rame. La capacità dei condensatori può essere modificata sostituendo il componente o utilizzando condensatori variabili o trimmer.

Con queste conoscenze possiamo ora rispondere alle seguenti domande.

[question:AD213]
[question:AD214]
[question:AD215]
[question:AD216]
[question:AD217]

Una combinazione di circuiti oscillanti paralleli e serie, se disposti in modo opportuno, può essere utilizzata come filtro passa-banda. In condizioni di risonanza, i circuiti oscillanti paralleli si comportano come resistenze ad alta impedenza, mentre il circuito oscillante serie si comporta come una resistenza a bassa impedenza.

[question:AD205]

La larghezza di banda dei filtri e dei filtri passa-banda viene spesso specificata in relazione a un determinato valore di attenuazione. L’attenuazione descrive quanto un segnale viene attenuato rispetto al massimo passaggio.

Generalmente, la *larghezza di banda* di un filtro è definita in corrispondenza del cosiddetto punto a $\qty{-3}{\dB}$.

Al punto a $\qty{-3}{\dB}$ vale:

- Solo metà della potenza passa attraverso il filtro
- La tensione del segnale è circa 0,7 volte il valore massimo

La larghezza di banda si ottiene dalla differenza tra la frequenza di taglio superiore e inferiore al punto a $\qty{-3}{\dB}$:

$ B = f_\mathrm{o} - f_\mathrm{u} $

[question:AD220]

Dove:

- $f_\mathrm{o}$: frequenza di taglio superiore
- $f_\mathrm{u}$: frequenza di taglio inferiore

La larghezza di banda a $\qty{-3}{\dB}$ viene utilizzata per descrivere l’idoneità di un filtro per determinate modalità operative:

- Filtro a banda stretta con larghezza di banda di circa $\qty{500}{\hertz}$: adatto per CW (telegrafia)
- Filtro a banda più larga con larghezza di banda di circa $\qty{2,7}{\kilo\hertz}$: adatto per la trasmissione vocale SSB

[question:AD221]
[question:AD222]

Nella domanda seguente non si deve leggere la larghezza di banda al punto a $\qty{-3}{\dB}$, ma al punto a $\qty{-60}{\dB}$.

[question:AD219]

Il fattore di qualità di un circuito oscillante (in inglese Q-factor) è determinato dal rapporto tra le reattanze di capacità e induttanza in condizioni di risonanza e la resistenza di perdita ohmica. Se un circuito oscillante non contenesse alcuna resistenza di perdita ohmica, il suo fattore di qualità sarebbe infinito. Tuttavia, i componenti reali presentano sempre perdite. Le induttanze hanno sempre una resistenza di perdita ohmica, i condensatori hanno perdite dielettriche che si manifestano anch’esse come resistenza ohmica. Maggiore è la resistenza ohmica in un circuito oscillante, minore è il suo fattore di qualità. Per ottenere filtri con alta qualità e pendenze ripide, si utilizzano spesso filtri a quarzo.

Per il calcolo del fattore di qualità utilizziamo le formule corrispondenti dalla raccolta di formule, a seconda che si tratti di un circuito oscillante serie o parallelo:

Per il circuito oscillante serie vale in condizioni di risonanza ($X_\text{L} = X_\text{C}$):

$Q = \frac{f_0}{B} = \frac{X_\text{L}}{R_\text{S}}$

Per il circuito oscillante parallelo vale in condizioni di risonanza ($X_\text{L} = X_\text{C}$):

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD225]

---

In base all’esempio di calcolo precedente, possiamo ora calcolare anche il fattore di qualità del circuito oscillante parallelo. La frequenza di risonanza viene calcolata come nell’esempio precedente. Tuttavia, per il calcolo di $Q$ è necessario utilizzare la formula per il circuito oscillante parallelo:

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD226]

La larghezza di banda dei circuiti oscillanti paralleli e serie può essere calcolata facilmente a partire dalla frequenza di risonanza del circuito oscillante e dal suo fattore di qualità, come segue (la formula è disponibile nella raccolta di formule):

$Q = \frac{f_0}{B}$

Riorganizzando la formula, si ottiene la larghezza di banda $B$:

$B = \frac{f_0}{Q}$

La formula sopra vale sia per il circuito oscillante serie che per quello parallelo!

[question:AD224]

Con le conoscenze acquisite, possiamo ora risolvere passo dopo passo anche la domanda seguente.
[question:AD223]

---

Per la trasmissione di segnali tra stadi di circuito, nonché nei filtri di trasmettitori e ricevitori, si utilizzano spesso circuiti oscillanti accoppiati. In questo caso, due circuiti oscillanti vengono accoppiati tra loro in modo induttivo o capacitivo. La figura [ref:a_gekoppelte_schwingkreise] mostra un accoppiamento induttivo. A seconda dell’applicazione, questo accoppiamento può essere:

- *debole* (d),
- *sottocritico* (c),
- *critico* (b) o
- *sovracritico* (a)

Il grado di accoppiamento determina l’interazione reciproca e, di conseguenza, la larghezza di banda e la curva di risposta del sistema complessivo.

<margin>
[picture:184:a_gekoppelte_schwingkreise:Accoppiamento di circuiti oscillanti]
</margin>

Con accoppiamento debole o sottocritico, l’interazione reciproca è minima; tuttavia, l’attenuazione d’inserzione dell’intero sistema è relativamente elevata e la larghezza di banda è ridotta.

Con accoppiamento critico, i due circuiti oscillanti si influenzano a vicenda in modo tale da ottenere una curva di risposta piatta con bassa attenuazione nel campo di passaggio e completamente piana (piattaforma) nella zona desiderata di passaggio. La larghezza di banda del sistema è maggiore rispetto all’accoppiamento debole o sottocritico. Questo è anche un buon modo per riconoscere un accoppiamento critico.

Con accoppiamento sovracritico, l’interazione reciproca dei due circuiti oscillanti è molto forte, il che porta a una forte variazione di entrambe le frequenze di risonanza e, di conseguenza, a una grande larghezza di banda. La curva di risposta nel campo di passaggio viene fortemente distorta e si formano due punti di risonanza a sinistra e a destra della frequenza centrale. La curva di risposta presenta una "insenatura". Questo è un buon modo per riconoscere un accoppiamento sovracritico.

[question:AD227]
[question:AD228]
[question:AD229]