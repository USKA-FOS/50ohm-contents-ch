Nella classe E abbiamo già appreso la capacità di un condensatore e il suo comportamento qualitativo con tensione alternata: un condensatore si comporta come una resistenza dipendente dalla frequenza. Abbiamo inizialmente osservato che la reattanza capacitiva è inversamente proporzionale alla frequenza. Se si diminuisce la frequenza, la reattanza $X_C$ aumenta. Se si aumenta la frequenza, la resistenza diminuisce di conseguenza. Il comportamento di un condensatore con tensione alternata può essere descritto dalla formula della reattanza capacitiva $X_C$:

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

Nella classe A, ora esamineremo più da vicino questo comportamento e scopriremo anche perché questa resistenza è chiamata "reattanza". Innanzitutto, dobbiamo ricordare che la reattanza di un condensatore è anche negativa, per poter rispondere alla seguente domanda:

[question:AC102]

<indepth>
Perché la reattanza capacitiva è negativa? Lo sfondo risiede nel calcolo complesso della corrente alternata, che non è strettamente necessaria per l'esame di radioamatore.

Per i lettori con conoscenze di numeri complessi, si noti tuttavia che la corretta rappresentazione della reattanza capacitiva è in realtà

$X_C = \frac{1}{j\omega C}$

Dove $j$ sta per l'unità immaginaria $\sqrt{-1}$.

Moltiplicando questa espressione per $j$, si ottiene:

$X_C = \frac{1}{j\omega C} = \frac{1 \cdot j}{j\omega C \cdot j} =\frac{-j}{\omega C}$

Da ciò si evince che la reattanza capacitiva non è solo negativa, ma anche complessa. Il segno negativo descrive la fase tra corrente e tensione sul condensatore, che esamineremo più in dettaglio in questo capitolo.
</indepth>

---

Gli strumenti di misura moderni ed economici, che i radioamatori utilizzano oggi con piacere, sono gli analizzatori di antenna o gli analizzatori di rete vettoriali (VNA). Misurano la variazione della reattanza $X_C$ in funzione della frequenza e possono anche rappresentare graficamente il risultato della misurazione.
La figura [ref:a_kapazitiver_Blindwiderstand] mostra la variazione della reattanza capacitiva (linea blu) di un condensatore in polistirene da $\qty{1500}{\pico\farad}$ nell'intervallo di frequenza da $\qtyrange{1}{4,5}{\mega\hertz}$. 

<margin>
[photo:248:a_kapazitiver_Blindwiderstand:Reattanza capacitiva $X_C$ (curva blu) e fase (curva rossa) di un condensatore in polistirene da $\qty{1500}{\pico\farad}$ nell'intervallo di frequenza da $\qtyrange{1}{4,5}{\mega\hertz}$.]
</margin>


Prova ora a rispondere alle seguenti domande utilizzando la formula sopra. Presta particolare attenzione alle unità e alle potenze di dieci, in modo da ottenere i risultati corretti.

[question:AC104]
[question:AC105]
[question:AC106]
[question:AC107]

Nella seguente domanda si cerca la capacità. Prova a riorganizzare la formula per poter calcolare la capacità $C$:

[question:AC108]

---

Se si effettua una misurazione simultanea di corrente e tensione su un condensatore con un oscilloscopio a due canali (cfr. [ref:a_strom_eilt_vor]), si ottiene un risultato inizialmente sorprendente: c'è uno sfasamento di $\qty{90}{\degree}$ tra corrente e tensione, con la corrente che precede la tensione.

Ciò significa che la corrente raggiunge già il suo valore massimo mentre la tensione sta ancora aumentando. Questo comportamento caratteristico è una proprietà fondamentale dei condensatori e svolge un ruolo importante nella tecnologia a corrente alternata, in particolare nei filtri e nei circuiti oscillanti.
La linea rossa nella figura [ref:a_kapazitiver_Blindwiderstand] rappresenta la fase della reattanza capacitiva a quasi costanti $\qty{-90}{\degree}$.

[question:AC101]

<margin>
[photo:268:a_strom_eilt_vor:Sfasamento sul condensatore tra tensione e corrente]
</margin>

<tip>
Aiuto mnemonico: Con il condensat*ooo*re, la corrente prec*ooo*de!
</tip>

---

Lo sfasamento tra tensione e corrente è quindi di $\qty{90}{\degree}$, con la corrente (rossa) che precede la tensione (blu), come mostrato nella figura [ref:a_blindleistung_kondensator]. Se si considera la potenza istantanea con $P = U \cdot I$, si ottiene una curva di potenza (verde) che oscilla simmetricamente attorno alla linea dello zero, anch'essa mostrata nella figura [ref:a_blindleistung_kondensator].

<margin>
[picture:943:a_blindleistung_kondensator:Il prodotto di $U \cdot I$ dà la curva di potenza verde]
</margin>

Il valore medio di questa potenza è zero, il che significa che non viene convertita potenza attiva. Invece, l'energia viene immagazzinata periodicamente nel campo elettrico del condensatore e restituita alla sorgente. Pertanto, per un condensatore idealmente privo di perdite, si parla di potenza reattiva e reattanza.

Solo una resistenza ohmica assorbe potenza attiva, poiché tensione e corrente sono in fase, cioè non c'è sfasamento. Ciò significa che tensione e corrente sono contemporaneamente positive o negative, in modo che la potenza istantanea $P = U \cdot I$ sia sempre positiva.

Un resistore reattivo ideale, al contrario, non assorbe potenza attiva e quindi, idealmente, non si scalda. Invece, l'energia viene immagazzinata periodicamente e restituita alla sorgente.

[question:AC111]

[question:AC103]

---

Se un condensatore si riscalda nelle applicazioni ad alta frequenza, ciò indica perdite nel componente. Un condensatore ideale non convertirebbe energia in calore, ma i condensatori reali hanno proprietà parassite che causano perdite.

Queste perdite possono essere osservate nel circuito di sostituzione: la resistenza $R_\text{ESR}$ (Equivalent Series Resistance) descrive le perdite ohmiche nel condensatore, mentre $R_\text{Isolator}$ modella le perdite nel dielettrico. Inoltre, l'induttanza parassita $L_\text{ESL}$ influenza il comportamento ad alte frequenze.

Per la valutazione tecnica di queste perdite si utilizzano il fattore di qualità $Q$ (Quality Factor) e il fattore di perdita $\tan\delta$. Entrambe le grandezze descrivono quanto un condensatore reale si discosti dal comportamento ideale.

Esiste una relazione diretta tra le due grandezze:

$Q = \frac{1}{\tan\delta}$

Ricorda: elevate perdite portano a un basso fattore di qualità $Q$ e quindi a un grande fattore di perdita $\tan\delta$. Maggiore è la frequenza, maggiori sono queste perdite, poiché la reattanza $X_C$ diminuisce all'aumentare della frequenza, mentre le resistenze parassite rimangono costanti.

<margin>
[picture:1065:a_ersatzchaltbild_kondensator:Circuito di sostituzione di un condensatore reale con perdite parassite.]
</margin>

---

[question:AC109]

[question:AC110]

<indepth>
Attraverso il calcolo complesso della corrente alternata, la reattanza $X_C$ con le perdite parassite $R$ può essere rappresentata sotto forma di diagramma vettoriale: 
[picture:1066:a_tan_delta:$\tan\delta$ nel diagramma vettoriale complesso]

La tangente descrive il rapporto tra il cateto opposto e il cateto adiacente, quindi in questo caso le perdite $R$ in rapporto alla reattanza capacitiva $X_C$ priva di perdite. 

$\tan\delta = \frac{R}{|X_C|}$

Maggiori sono le perdite, maggiore è l'angolo $\delta$ e quindi anche il fattore di perdita $\tan\delta$. Un condensatore ideale avrebbe un angolo di $\delta = 0$ gradi, poiché non ha perdite.

Attraverso questa somma complessa o geometrica si ottiene la grandezza $Z$. Viene chiamata *impedenza* e descrive la resistenza totale complessa di un componente. Il modulo dell'impedenza $|Z|$ corrisponde alla cosiddetta *resistenza apparente*.
</indepth>
