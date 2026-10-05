Già nel capitolo [sec:wellenlaenge] abbiamo appreso la relazione tra la frequenza ($f$) e la lunghezza d’onda ($\lambda$). Lì sono state fornite due equazioni dimensionali specificamente adattate.
% Inserire questa frase nella frase precedente se le formule sono incluse nella raccolta. "... dalla raccolta di formule per l'esame..."

$f[\unit{\mega\hertz}] = \dfrac{300}{\lambda[\unit{\meter}]}$

$\lambda[\unit{\meter}] = \dfrac{300}{f[\unit{\mega\hertz}]}$

<indepth>
Le equazioni in cui è già indicata l'unità in cui devono essere espressi i valori si chiamano *equazioni dimensionali adattate*.
</indepth>

In realtà, però, si tratta solo di un'unica equazione, che nel primo caso è stata risolta rispetto alla frequenza e nel secondo rispetto alla lunghezza d’onda.

Nei calcoli tecnici dobbiamo continuamente riscrivere le equazioni in modo che la grandezza cercata si trovi da sola su un lato. Per fare ciò, applichiamo le necessarie operazioni matematiche (moltiplicazione, divisione, addizione, sottrazione, ...) a entrambi i lati dell'equazione *contemporaneamente*. Con un po' di pratica, è molto più semplice che memorizzare separatamente tutte le forme necessarie di una relazione. Nella raccolta di formule, le equazioni semplici sono indicate solo nella loro forma base. La riscrittura di formule semplici è materia d'esame.

---

<indepth>
Nelle unità di base ($\unit{\second}$, $\unit{\meter}$), la relazione tra lunghezza d’onda e frequenza nello spazio libero è:

$\lambda = \dfrac{c_0}{f}$

Dove $c_0$ è la velocità di propagazione delle onde elettromagnetiche nel vuoto ("velocità della luce"), $c_o \approx \qty{300000000}{\meter\per\second}$
</indepth>

Consideriamo qui la relazione tra frequenza e lunghezza d’onda nella forma più astratta:

$\lambda = \dfrac{c_0}{f}$

Ora vogliamo determinare la frequenza corrispondente a una lunghezza d’onda di 2,069 m.

Per ottenere ciò, moltiplichiamo prima entrambi i lati dell'equazione per la frequenza.

$\lambda = \dfrac{c_0}{f} \quad\quad\quad | \cdot f$

Questo è illustrato da "$|~\cdot f$", dove la barra verticale significa che l'operazione seguente viene eseguita su entrambi i lati.

Si ottiene così una nuova equazione:

$\lambda\cdot f = \dfrac{c_0 \cdot f}{f}$

Dove a destra la frequenza si semplifica (poiché $f$ diviso per $f$ dà 1):

$\lambda \cdot f = c_0$

Ora la frequenza si trova già sul lato sinistro dell'equazione, dove la vogliamo. Successivamente, dividiamo entrambi i lati per la lunghezza d’onda:

$\lambda \cdot f = c_0 \quad\quad\quad |: \lambda$

Risulta quindi:

$\frac{\lambda\cdot f}{\lambda} = \frac{c_0}{\lambda}$

Sul lato sinistro, il lambda si semplifica di nuovo:

$f = \dfrac{c_0}{\lambda}$

Questa è la relazione cercata. Sostituiamo i valori numerici:

$f = \dfrac{\qty{300000000}{\meter\per\second}}{\qty{2,069}{\meter}} = \dfrac{\num{300000000}}{\qty{2,069}{\second}}  = \qty{144997583}{\hertz} \approx \qty{145}{\mega\hertz} $

Qui abbiamo considerato che $\frac{1}{\unit{\second}} = \qty{1}{\hertz}$.

Ora possiamo riscrivere le formule utilizzando moltiplicazione e divisione. In seguito incontreremo altre formule che richiedono anche addizione e sottrazione, potenze e radici. Nei capitoli [sec:dezibel_1] e [sec:dezibel_2] si aggiungono infine persino i logaritmi. Niente paura, nei rispettivi punti spiegheremo esattamente come riscrivere queste formule passo dopo passo.
