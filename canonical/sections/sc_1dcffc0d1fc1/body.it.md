Con le antenne dobbiamo distinguere tra *lunghezza meccanica* e *lunghezza elettrica*. La lunghezza meccanica è semplicemente la lunghezza effettivamente misurabile del filo dell'antenna o del radiatore. La lunghezza elettrica, invece, descrive come l'antenna si comporta elettricamente alla frequenza considerata. Essa può essere modificata, tra l'altro, con bobine e condensatori, senza che sia necessario cambiare la lunghezza meccanica del radiatore.

Consideriamo inizialmente le antenne vicino alla loro risonanza fondamentale. Un dipolo a semionda è approssimativamente risonante a una lunghezza totale di $\lambda/2$, mentre una groundplane con un singolo radiatore verticale è approssimativamente risonante a una lunghezza del radiatore di $\lambda/4$. Se una tale antenna è troppo corta per la frequenza desiderata, la sua impedenza di alimentazione presenta una componente reattiva *capacitiva*. Una bobina può compensare questa componente reattiva capacitiva. Si parla allora di *allungamento elettrico* dell'antenna. Se invece l'antenna è troppo lunga per la frequenza desiderata, la sua impedenza di alimentazione presenta una componente reattiva *induttiva*. Questa può essere compensata con un condensatore. Si parla allora di *accorciamento elettrico*. Una bobina allunga quindi elettricamente un'antenna, mentre un condensatore la accorcia elettricamente. La lunghezza meccanica del radiatore rimane invariata.

<margin>
[picture:1134:a_5_8_lambda_strahlung:Modello di irradiazione e distribuzione della corrente di antenne verticali con terra ideale]
</margin>

---

Un esempio interessante è l'antenna verticale $\frac{5}{8}\lambda$ con una lunghezza di $\qty{0.625}{\lambda}$ (cfr. figura [ref:a_5_8_lambda]). Il radiatore è quindi meccanicamente circa 2,5 volte più lungo di quello di una normale groundplane $\frac{\lambda}{4}$ ($\qty{0.25}{\lambda}$). La maggiore lunghezza del radiatore modifica favorevolmente il diagramma di irradiazione verticale, come mostrato nella figura [ref:a_5_8_lambda_strahlung]: una maggiore parte della potenza irradiata viene concentrata verso l'orizzonte, mentre meno potenza viene irradiata verso l'alto o verso il basso. Questo comporta, in genere, una maggiore portata nelle comunicazioni terrestri a parità di potenza. Una lunghezza del radiatore di circa $\frac{5}{8} \lambda$ è ottimale per questo effetto: se il radiatore viene ulteriormente allungato, una maggiore potenza viene nuovamente persa verso l'alto e verso il basso.

Tuttavia, a una lunghezza del radiatore di $\frac{5}{8}\lambda=\qty{0.625}{\lambda}$, questa antenna non è risonante. Per la risonanza, la lunghezza del radiatore dovrebbe essere ridotta a $\frac{\lambda}{2}=\qty{0.5}{\lambda}$ o aumentata a $\frac{3}{4}\lambda=\qty{0.75}{\lambda}$. Entrambe le soluzioni porterebbero a una minore potenza all'orizzonte. Si consiglia quindi, per il migliore effetto di concentrazione, di mantenere la lunghezza del radiatore a $\frac{5}{8}\lambda$ e di ottenere la risonanza elettricamente, cioè di allungare elettricamente l'antenna. Una delle possibili soluzioni è l'uso di una bobina di base. La bobina fornisce una componente reattiva induttiva che compensa la componente reattiva capacitiva del radiatore $\frac{5}{8}\lambda$. L'impedenza così ottenuta è molto simile a quella di un'antenna con lunghezza del radiatore $\frac{3}{4}\lambda=\qty{0.75}{\lambda}$.

<margin>
[picture:650:a_5_8_lambda:Antenna verticale $\qty{5}{8}\lambda$]
</margin>

[question:AG106]

---

Viceversa, un'antenna che è meccanicamente leggermente troppo lunga rispetto alla sua risonanza fondamentale può essere elettricamente accorciata con un condensatore (cfr. figura [ref:a_verkuerzung]). Il condensatore fornisce una componente reattiva capacitiva e compensa così la componente reattiva induttiva del radiatore troppo lungo.

[question:AG107]

<margin>
[picture:563:a_verkuerzung:Antenna verticale con condensatore di accorciamento]
</margin>

---

Anche per un dipolo si può inizialmente stimare, in base alla sua lunghezza meccanica, se sia necessaria un'estensione o un accorciamento elettrico per ottenere la risonanza fondamentale desiderata.

[question:AG108]