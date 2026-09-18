Nella classe E abbiamo già imparato a conoscere la capacità di un condensatore e il suo comportamento qualitativo in presenza di tensione alternata: un condensatore si comporta come una resistenza dipendente dalla frequenza. Inizialmente abbiamo stabilito che la reattanza capacitiva è inversamente proporzionale alla frequenza. Se si riduce la frequenza, la reattanza $X_C$ aumenta. Se invece si aumenta la frequenza, la resistenza diminuisce di conseguenza. Il comportamento di un condensatore in presenza di tensione alternata può essere descritto dalla formula della reattanza capacitiva $X_C$:

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

Nella classe A esamineremo ora questo comportamento in modo più approfondito e scopriremo anche perché questa resistenza viene chiamata "reattanza". Prima di tutto, dobbiamo ricordare che la reattanza capacitiva di un condensatore è anche negativa, per poter rispondere alla seguente domanda:

[question:AC102]

<indepth>
Perché la reattanza capacitiva è negativa? La ragione risiede nel calcolo complesso della corrente alternata, che non è strettamente necessario per l’esame di radioamatore.

Per i lettori con conoscenze di numeri complessi, va notato che la rappresentazione corretta della reattanza capacitiva è in realtà

$X_C = \frac{1}{j\omega C}$

dove $j$ rappresenta l’unità immaginaria $\sqrt{-1}$.

Se si moltiplica questa espressione per $j$, si ottiene:

$X_C = \frac{1}{j\omega C} = \frac{1 \cdot j}{j\omega C \cdot j} = \frac{-j}{\omega C}$

Da ciò risulta evidente che la reattanza capacitiva non è solo negativa, ma anche complessa. Il segno negativo descrive la relazione di fase tra corrente e tensione nel condensatore, che approfondiremo in questo capitolo.
</indepth>

---

Gli strumenti di misura moderni e poco costosi utilizzati oggi dai radioamatori, come gli analizzatori di antenna o i Network Analyzer vettoriali (VNA), misurano la variazione della reattanza $X_C$ in funzione della frequenza e possono anche rappresentare graficamente i risultati delle misurazioni.

La figura [ref:a_kapazitiver_Blindwiderstand] mostra la variazione della reattanza capacitiva (linea blu) di un condensatore in styroflex da $\qty{1500}{\pico\farad}$ nella banda di frequenza da $\qtyrange{1}{4,5}{\mega\hertz}$.

<margin>
[photo:248:a_kapazitiver_Blindwiderstand:Reattanza capacitiva $X_C$ (curva blu) e relazione di fase (curva rossa) di un condensatore in styroflex da $\qty{1500}{\pico\farad}$ nella banda di frequenza da $\qtyrange{1}{4,5}{\mega\hertz}$.]
</margin>

Prova ora a rispondere alle seguenti domande utilizzando la formula sopra. Presta particolare attenzione alle unità di misura e alle potenze di dieci per ottenere i risultati corretti.

[question:AC104]
[question:AC105]
[question:AC106]
[question:AC107]

Nella domanda seguente si chiede di calcolare la capacità. Prova a riorganizzare la formula per calcolare la capacità $C$:

[question:AC108]

---

Se si effettua una misurazione simultanea di corrente e tensione su un condensatore con un oscilloscopio a due canali (cfr. [ref:a_strom_eilt_vor]), si ottiva un risultato inizialmente sorprendente: tra corrente e tensione esiste uno sfasamento di $\qty{90}{\degree}$, con la corrente che precede la tensione.

Ciò significa che la corrente raggiunge già il suo valore massimo mentre la tensione è ancora in aumento. Questo comportamento caratteristico è una proprietà fondamentale dei condensatori ed è di grande importanza nella tecnica della corrente alternata, in particolare nei filtri e nei circuiti risonanti.

La linea rossa nella figura [ref:a_kapazitiver_Blindwiderstand] rappresenta la relazione di fase della reattanza capacitiva, che si attesta a quasi costanti $\qty{-90}{\degree}$.

[question:AC101]

<margin>
[photo:268:a_strom_eilt_vor:Sfasamento tra tensione e corrente in un condensatore]
</margin>

<tip>
Aiuto mnemonico: Nel condensat*ore* la corrente va v*anti*!
</tip>

---

Lo sfasamento tra tensione e corrente è quindi di $\qty{90}{\degree}$, con la corrente (rossa) che precede la tensione (blu), come mostrato nella figura [ref:a_blindleistung_kondensator]. Se si considera la potenza istantanea con $P = U \cdot I$, si ottiene una curva di potenza (verde) che oscilla simmetricamente intorno alla linea dello zero, anch’essa rappresentata nella figura [ref:a_blindleistung_kondensator].

<margin>
[picture:943:a_blindleistung_kondensator:Il prodotto di $U \cdot I$ dà la curva di potenza verde]
</margin>

Il valore medio di questa potenza è zero, il che significa che non viene convertita potenza attiva. Al contrario, l’energia viene immagazzinata periodicamente nel campo elettrico del condensatore e poi restituita alla sorgente. Pertanto, in un condensatore ideale senza perdite si parla di potenza reattiva e di reattanza.

Solo una resistenza ohmica assorbe potenza attiva, poiché in essa tensione e corrente sono in fase, cioè non c’è sfasamento. Ciò significa che tensione e corrente sono contemporaneamente positive o negative, quindi la potenza istantanea $P = U \cdot I$ è sempre positiva.

Una reattanza ideale, invece, non assorbe potenza attiva e quindi, in teoria, non si riscalda. Al contrario, l’energia viene immagazzinata periodicamente e poi restituita alla sorgente.

[question:AC111]

[question:AC103]

---

Se un condensatore si riscalda in applicazioni ad alta frequenza, ciò è un’indicazione di perdite nel componente. Un condensatore ideale non convertirebbe energia in calore, ma i condensatori reali presentano proprietà parassite che causano perdite.

Queste perdite possono essere osservate nello schema equivalente: la resistenza $R_\text{ESR}$ (Equivalent Series Resistance) descrive le perdite ohmiche nel condensatore, mentre $R_\text{Isolator}$ modella le perdite nel materiale dielettrico. Inoltre, l’induttanza parassita $L_\text{ESL}$ influisce sul comportamento alle alte frequenze.

Per valutare tecnicamente queste perdite, si utilizzano il fattore di qualità $Q$ (Quality Factor) e il fattore di perdita $\tan\delta$. Entrambe le grandezze descrivono quanto un condensatore reale si discosta dal comportamento ideale.

Esiste una relazione diretta tra queste due grandezze:

$Q = \frac{1}{\tan\delta}$

Da ricordare: elevate perdite portano a un basso fattore di qualità $Q$ e quindi a un elevato fattore di perdita $\tan\delta$. Maggiore è la frequenza, maggiore è l’effetto di queste perdite, poiché la reattanza $X_C$ diminuisce all’aumentare della frequenza, mentre le resistenze parassite rimangono costanti.

<margin>
[picture:1065:a_ersatzchaltbild_kondensator:Schema equivalente di un condensatore reale con perdite parassite.]
</margin>

---

[question:AC109]

[question:AC110]

<indepth>
Attraverso il calcolo complesso della corrente alternata, è possibile rappresentare la reattanza $X_C$ con le perdite parassite $R$ sotto forma di un diagramma vettoriale:
[picture:1066:a_tan_delta:$\tan\delta$ nel diagramma vettoriale complesso]

La tangente descrive infatti il rapporto tra il cateto opposto e il cateto adiacente, cioè in questo caso le perdite $R$ rispetto alla reattanza capacitiva ideale $X_C$.

$\tan\delta = \frac{R}{|X_C|}$

Maggiori sono le perdite, maggiore è l’angolo $\delta$ e quindi anche il fattore di perdita $\tan\delta$. Un condensatore ideale avrebbe un angolo $\delta = 0$ gradi, poiché non presenta perdite.

Attraverso questa addizione complessa o geometrica si ottiene la grandezza $Z$. Essa viene chiamata *impedenza* e descrive la resistenza totale complessa di un componente. Il valore assoluto dell’impedenza $|Z|$ corrisponde alla cosiddetta *impedenza apparente*.
</indepth>