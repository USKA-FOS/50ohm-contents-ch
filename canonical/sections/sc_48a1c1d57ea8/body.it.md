Nella classe E abbiamo già incontrato una formula approssimata per calcolare la distanza di sicurezza da un'antenna:

$d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_{\textrm{EIRP}}}}{E}$

Questa formula può essere applicata a molte forme di antenna, a condizione che sia soddisfatta la condizione

$d > \frac{\lambda}{2\pi}$

ovvero che ci si trovi al di fuori del campo vicino reattivo. Di seguito esaminiamo da dove derivi questa limitazione e il valore di $\qty{30}{\ohm}$ che compare nella formula.

In forma generale, la formula approssimata è:

$d = \frac{\sqrt{\frac{Z_0}{4\pi}\cdot P_{\textrm{EIRP}}}}{E}$

Qui, $Z_0$ indica l'impedenza d’onda dello spazio libero. Come abbiamo visto nel capitolo precedente, questa grandezza si avvicina al valore del campo lontano

$Z_0 \approx \qty{120\pi}{\ohm} \approx \qty{377}{\ohm}$

con l’aumentare della distanza dall’antenna (cfr. figura [ref:a_feldwellenwiderstand]). Sostituendo questo valore nell’espressione $\frac{Z_0}{4\pi}$, otteniamo:

$\frac{Z_0}{4\pi} \approx \frac{\qty{120\pi}{\ohm}}{4\pi} = \qty{30}{\ohm}$

Da cui deriva la formula approssimata nota dalla classe E. Allo stesso tempo, risulta chiaro perché non possa essere utilizzata nel campo vicino reattivo: in questa regione l'impedenza d’onda non è costante, ma dipende fortemente dalla distanza, dalla forma dell’antenna e dalla direzione considerata. Per calcoli nel campo vicino reattivo, quindi per distanze $d \le \frac{\lambda}{2\pi}$, sono generalmente necessari calcoli più approfonditi, simulazioni numeriche o misurazioni.

<margin>
[immagine:1116:a_feldwellenwiderstand:Andamento dell'impedenza d’onda nei campi vicino e lontano (scala logaritmica).]
</margin>

Se la formula approssimata del campo lontano viene applicata a un’antenna a dipolo già nel campo vicino radiante, in genere si ottiene una distanza di sicurezza maggiore di quella effettivamente necessaria. In questa regione, l'impedenza d’onda è inferiore a $\qty{377}{\ohm}$, mentre la formula approssimata utilizza il valore più elevato del campo lontano. Il risultato è quindi conservativo e si colloca sul lato della sicurezza. Questo approccio è accettato dalla Bundesnetzagentur.

Tuttavia, ciò non vale per le antenne magnetiche e per quelle elettricamente molto corte. La figura [ref:a_feldwellenwiderstand] mostra, ad esempio, che l'impedenza d’onda di un’antenna a loop magnetica nel campo vicino radiante può essere notevolmente superiore a $\qty{377}{\ohm}$. In questo caso, la formula approssimata del campo lontano fornirebbe una distanza di sicurezza troppo ridotta. Per tali antenne, è quindi necessario utilizzare altri metodi, ad esempio programmi specifici per il calcolo del campo vicino (simulazioni) o misurazioni.

[domanda:AK103]

Per il calcolo delle distanze di protezione delle persone, nel campo lontano può essere utilizzata la nota formula approssimata. In questo modo, spesso si possono evitare misurazioni o simulazioni complesse. In particolare nel funzionamento portatile, consente una rapida stima approssimativa della distanza di sicurezza necessaria.