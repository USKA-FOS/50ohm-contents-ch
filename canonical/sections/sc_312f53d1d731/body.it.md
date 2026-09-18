Già nel capitolo [sec:wellenlaenge] abbiamo imparato a conoscere la relazione tra la frequenza ($f$) e la lunghezza d’onda ($\lambda$). Allora sono state fornite due equazioni dimensionali appositamente adattate dalla *raccolta di formule* per l’esame.

$f[\unit{\mega\hertz}] = \dfrac{300}{\lambda[\unit{\meter}]}$

$\lambda[\unit{\meter}] = \dfrac{300}{f[\unit{\mega\hertz}]}$

<indepth>
Le equazioni in cui viene già indicata l’*unità* in cui devono essere inseriti i valori vengono chiamate *equazioni dimensionali adattate*.
</indepth>

In realtà si tratta solo di un’unica equazione, che in un caso è stata risolta rispetto alla frequenza e nell’altro rispetto alla lunghezza d’onda.

Nelle operazioni tecniche dobbiamo spesso risolvere le equazioni in modo che la grandezza cercata rimanga da sola su un lato. Per farlo, applichiamo le necessarie operazioni matematiche (moltiplicazione, divisione, addizione, sottrazione, ...) *contemporaneamente* a entrambi i lati dell’equazione. Con un po’ di pratica, questo metodo è molto più semplice che ricordare separatamente tutte le forme necessarie di una relazione. Nella classe E e anche nella classe A, questo è addirittura obbligatorio, poiché le equazioni nella *raccolta di formule* sono fornite solo nella loro forma di base.

---

<indepth>
Nella forma con *unità* di base ($\unit{\second}$, $\unit{\meter}$), la relazione tra lunghezza d’onda e frequenza nello *spazio libero* è:

$\lambda = \dfrac{c_0}{f}$

Qui $c_0$ è la *velocità di propagazione* delle onde elettromagnetiche nel vuoto ("velocità della luce"), $c_0 \approx \qty{300000000}{\meter\per\second}$
</indepth>

Consideriamo la relazione tra frequenza e lunghezza d’onda in questa forma più astratta:

$\lambda = \dfrac{c_0}{f}$

Ora vogliamo determinare la frequenza corrispondente a una lunghezza d’onda di 2,069 m.

Per farlo, moltiplichiamo inizialmente entrambi i lati dell’equazione per la frequenza.

$\lambda = \dfrac{c_0}{f} \quad\quad\quad | \cdot f$

Questo viene illustrato con "$|~\cdot f$", dove la barra verticale indica che l’operazione successiva viene eseguita su entrambi i lati.

Si ottiene così una nuova equazione:

$\lambda\cdot f = \dfrac{c_0 \cdot f}{f}$

dove a destra la frequenza si semplifica (infatti $f$ diviso $f$ dà 1):

$\lambda \cdot f = c_0$

Ora la frequenza si trova già sul lato sinistro dell’equazione, dove vogliamo che sia. Successivamente dividiamo entrambi i lati per la lunghezza d’onda:

$\lambda \cdot f = c_0 \quad\quad\quad |: \lambda$

Quindi otteniamo:

$\frac{\lambda\cdot f}{\lambda} = \frac{c_0}{\lambda}$

Sul lato sinistro, il lambda si semplifica di nuovo:

$f = \dfrac{c_0}{\lambda}$

Questa è la relazione cercata. Inseriamo i valori numerici:

$f = \dfrac{\qty{300000000}{\meter\per\second}}{\qty{2,069}{\meter}} = \dfrac{\num{300000000}}{\qty{2,069}{\second}}  = \qty{144997583}{\hertz} \approx \qty{145}{\mega\hertz} $

Abbiamo tenuto conto del fatto che $\frac{1}{\unit{\second}} = \qty{1}{\hertz}$.

Ora sappiamo come risolvere le formule utilizzando moltiplicazione e divisione. In seguito incontreremo altre formule in cui saranno necessarie anche addizione e sottrazione, potenze e radici. Nei capitoli [sec:dezibel_1] e [sec:dezibel_2] verranno infine introdotti anche i logaritmi. Non preoccupatevi: in ciascuno di questi casi spiegheremo passo dopo passo come risolvere queste formule.