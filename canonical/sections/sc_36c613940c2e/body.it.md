Gli oscillatori controllabili in frequenza possono essere realizzati in diversi modi. Una possibilità è l’**oscillatore controllato in tensione VCO** (*Voltage Controlled Oscillator*).

[question:AD601]

<margin>
[picture:752:a_vco_schaltung:Circuito VCO con diodo a capacità variabile]
</margin>

---

Per modificare la frequenza dell’oscillatore, è possibile inserire nel suo circuito oscillante un **diodo a capacità variabile**, la cui capacità può essere influenzata da una tensione continua (cfr. figura [ref:a_vco_schaltung]). Una variazione di questa tensione continua porta quindi a una corrispondente variazione della frequenza dell’oscillatore. In questo modo, l’oscillatore diventa sintonizzabile tramite una tensione di controllo.

Il diodo a capacità variabile viene utilizzato in **polarizzazione inversa**. Maggiore è la tensione inversa applicata al diodo, minore diventa la sua capacità, che è determinata dalla dimensione della **giunzione** (giunzione P-N). La giunzione si allarga con l’aumento della tensione inversa applicata, riducendo la capacità e quindi aumentando la frequenza del circuito oscillante secondo la formula di oscillazione di Thomson.

Viceversa, la giunzione del diodo a capacità variabile si restringe con la diminuzione della tensione inversa applicata, aumentando la capacità e quindi riducendo la frequenza del circuito oscillante. La tensione inversa può essere generata, ad esempio, da un potenziometro o da un circuito di controllo.

<tip>
Maggiore è la tensione applicata al diodo a capacità variabile, maggiore diventa la distanza tra le "piastre" ($d$). È sempre consigliabile consultare la **raccolta di formule** per comprendere queste catene di effetti.

$C = \epsilon_0 \cdot \epsilon_r \cdot \frac{A}{d}$

$f = \frac{1}{2\pi\sqrt{L\cdot C}}$

$U \uparrow \quad\rightarrow\quad C \downarrow \quad\rightarrow\quad f \uparrow$

$U \downarrow \quad\rightarrow\quad C \uparrow \quad\rightarrow\quad f \downarrow$
</tip>

[question:AD218]

Per tutti i circuiti oscillatori, indipendentemente dalla loro realizzazione, vale il principio che i **ritorni indesiderati** possono portare a instabilità di frequenza. Questo vale sia per i VCO che per i VFO (ad esempio con condensatori variabili) e altri oscillatori.

[question:AD611]