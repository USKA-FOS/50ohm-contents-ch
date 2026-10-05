Nella sezione [sec:kondensator_1] abbiamo già conosciuto la capacità di un condensatore e il suo comportamento qualitativo con tensione alternata: un condensatore si comporta come una resistenza dipendente dalla frequenza. Abbiamo inizialmente notato che la reattanza capacitiva è inversamente proporzionale alla frequenza. Se si riduce la frequenza, la reattanza $X_C$ aumenta. Se invece si aumenta la frequenza, la resistenza diminuisce di conseguenza. Il comportamento di un condensatore con tensione alternata può essere descritto dalla formula per la reattanza capacitiva $X_C$:

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

Qui vogliamo ora esaminare questo comportamento più in dettaglio e anche capire perché questa resistenza è chiamata "reattanza". Innanzitutto, però, dobbiamo ricordare che la reattanza di un condensatore è anche negativa, per poter risolvere la seguente domanda:

[question:AC102]

<indepth>
Perché la reattanza capacitiva è negativa? Il motivo risiede nel calcolo complesso dei circuiti in corrente alternata, che non è strettamente necessario per l'esame di radioamatore.

Per i lettori con conoscenze di numeri complessi, si noti però che la rappresentazione corretta della reattanza capacitiva è in realtà

$X_C = \frac{1}{j\omega C}$

dove $j$ rappresenta l'unità immaginaria $\sqrt{-1}$.

Se si amplifica questa espressione con $j$, si ottiene:

$X_C = \frac{1}{j\omega C} = \frac{1 \cdot j}{j\omega C \cdot j} =\frac{-j}{\omega C}$

Da ciò si vede che la reattanza capacitiva non è solo negativa, ma anche complessa. Il segno negativo descrive la relazione di fase tra corrente e tensione sul condensatore, che esamineremo più in dettaglio in questo capitolo.
</indepth>

---

Gli strumenti di misura moderni ed economici che i radioamatori oggi amano usare sono gli analizzatori di antenna o i Vector Network Analyzer (VNA). Misurano la variazione della reattanza $X_C$ in funzione della frequenza e possono anche visualizzare graficamente il risultato della misura.
La figura [ref:a_kapazitiver_Blindwiderstand] mostra la variazione della reattanza capacitiva (linea blu) di un condensatore Styroflex da $\qty{1500}{\pico\farad}$ nella banda di frequenza da $\qtyrange{1}{4,5}{\mega\hertz}$.

<margin>
[photo:248:a_kapazitiver_Blindwiderstand:Reattanza capacitiva $X_C$ (curva blu) e fase (curva rossa) di un condensatore Styroflex da $\qty{1500}{\pico\farad}$ nella banda di frequenza da $\qtyrange{1}{4,5}{\mega\hertz}$.]
</margin>


Ora prova a rispondere alle seguenti domande utilizzando la formula sopra. Presta particolare attenzione alle unità o alle potenze di dieci, in modo da ottenere i risultati corretti.

[question:AC104]
[question:AC105]
[question:AC106]
[question:AC107]

Nella domanda seguente si cerca la capacità. Prova a risolvere la formula per calcolare la capacità $C$:

[question:AC108]

---

Se si esegue una misura simultanea di corrente e tensione su un condensatore con un oscilloscopio a due canali (cfr. [ref:a_strom_eilt_vor]), si ottiene un risultato inizialmente sorprendente: tra corrente e tensione c'è uno sfasamento di $\qty{90}{\degree}$, in cui la corrente è in anticipo rispetto alla tensione.

Ciò significa che la corrente raggiunge già il suo valore massimo mentre la tensione è ancora in aumento. Questo comportamento caratteristico è una proprietà fondamentale dei condensatori e svolge un ruolo importante nella tecnologia a corrente alternata, specialmente nei filtri e nei circuiti risonanti.
La linea rossa nella figura [ref:a_kapazitiver_Blindwiderstand] rappresenta la fase della reattanza capacitiva a quasi costanti $\qty{-90}{\degree}$.

[question:AC101]

<margin>
[photo:268:a_strom_eilt_vor:Sfasamento sul condensatore tra tensione e corrente]
</margin>

<tip>
Aiuto mnemonico: Nel condensat*ooo*re, la corrente è in ant*ooo*ipo!
</tip>

---

Lo sfasamento tra tensione e corrente è quindi di $\qty{90}{\degree}$, con la corrente (rossa) in anticipo rispetto alla tensione (blu), come mostrato in figura [ref:a_blindleistung_kondensator]. Considerando la potenza istantanea con $P = U \cdot I$, si ottiene una curva di potenza (verde) che oscilla simmetricamente attorno alla linea zero, anch'essa mostrata in figura [ref:a_blindleistung_kondensator].

<margin>
[picture:943:a_blindleistung_kondensator:Il prodotto di $U \cdot I$ dà la curva di potenza verde]
</margin>

Il valore medio di questa potenza è zero, cioè non viene convertita alcuna potenza attiva. Invece, l'energia viene periodicamente immagazzinata nel campo elettrico del condensatore e restituita alla sorgente. Pertanto, per un condensatore ideale senza perdite, si parla di potenza reattiva e di reattanza.

Solo una resistenza ohmica assorbe potenza attiva, poiché in essa tensione e corrente sono in fase, cioè non c'è sfasamento. Ciò significa che tensione e corrente sono positive o negative contemporaneamente, in modo che la potenza istantanea $P = U \cdot I$ sia sempre positiva.

Una reattanza ideale, invece, non assorbe potenza attiva e quindi, in condizioni ideali, non si riscalda. Invece, l'energia viene periodicamente immagazzinata e restituita alla sorgente.

[question:AC111]

[question:AC103]

---

Se un condensatore nelle applicazioni ad alta frequenza si riscalda comunque, questo è un segno di perdite nel componente. Un condensatore ideale non convertirebbe energia in calore, ma i condensatori reali hanno proprietà parassite che portano a perdite.

Queste perdite possono essere viste nello schema equivalente: La resistenza $R_\text{ESR}$ (Equivalent Series Resistance) descrive le perdite ohmiche nel condensatore, mentre $R_\text{Isolator}$ modella le perdite nel materiale dielettrico/isolante. Inoltre, l'induttanza parassita $L_\text{ESL}$ influenza il comportamento ad alte frequenze.

Per la valutazione tecnica di queste perdite si utilizza il fattore di qualità $Q$ (Quality Factor) e il fattore di perdita $\tan\delta$. Entrambe le grandezze descrivono quanto un condensatore reale si discosta dal comportamento ideale.

Tra le due grandezze esiste una relazione diretta:

$Q = \frac{1}{\tan\delta}$

Ricorda: Perdite elevate portano a un basso fattore di qualità $Q$ e quindi a un grande fattore di perdita $\tan\delta$. Più alta è la frequenza, più forti sono questi effetti, poiché la reattanza $X_C$ diminuisce con l'aumentare della frequenza, mentre le resistenze parassite rimangono costanti.

<margin>
[picture:1065:a_ersatzchaltbild_kondensator:Schema equivalente di un condensatore reale con perdite parassite.]
</margin>

---

[question:AC109]

[question:AC110]

<indepth>
Attraverso il calcolo complesso dei circuiti in corrente alternata, la reattanza $X_C$ con le perdite parassite $R$ può essere rappresentata sotto forma di diagramma vettoriale:
[picture:1066:a_tan_delta:$\tan\delta$ nel diagramma vettoriale complesso]

La tangente descrive il rapporto tra cateto opposto e cateto adiacente, quindi in questo caso le perdite $R$ rispetto alla reattanza capacitiva senza perdite $X_C$.

$\tan\delta = \frac{R}{|X_C|}$

Maggiore è la perdita, maggiore è l'angolo $\delta$ e quindi anche il fattore di perdita $\tan\delta$. Un condensatore ideale avrebbe un angolo di $\delta = 0$ gradi, poiché non ha perdite.

Attraverso questa addizione complessa o geometrica si ottiene la grandezza $Z$. Viene chiamata *impedenza* e descrive la resistenza totale complessa di un componente. Il valore assoluto dell'impedenza $|Z|$ corrisponde alla cosiddetta *impedenza*.
</indepth>
