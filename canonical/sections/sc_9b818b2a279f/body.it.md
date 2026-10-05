In questa e nella prossima sezione ci occupiamo di due importanti circuiti fondamentali di un transistor bipolare. Inizialmente consideriamo in questa sezione il *circuito a collettore comune*, nella sezione successiva la *configurazione a emettitore comune*. Entrambi i circuiti sono mostrati nella figura [ref:a_emitter_collector]. Possiedono proprietà diverse e sono quindi utilizzati per diverse applicazioni.

<margin>
[picture:1118:a_emitter_collector:Configurazione a emettitore comune e a collettore comune con denominazioni base (B), collettore (C) ed emettitore (E)]
</margin>

La denominazione dei circuiti fondamentali di un transistor bipolare si basa sul terminale che non serve né come ingresso né come uscita del circuito e che quindi costituisce il punto di riferimento comune per il circuito di ingresso e di uscita. Nel circuito a collettore comune questo è il collettore.

---

[question:AD401]

<tip>
I circuiti amplificatori dei transistor bipolari sono denominati in base al terminale a cui non sono direttamente collegati né l'ingresso né l'uscita (cfr. figura [ref:a_emitter_collector]).
</tip>

Poiché il collettore è tipicamente collegato alla tensione di alimentazione e per le tensioni alternate si trova approssimativamente a un potenziale fisso, la tensione all'emettitore segue la tensione alla base. Il circuito a collettore comune è quindi spesso chiamato anche *inseguitore di emettitore*.

Se ad esempio la tensione d’ingresso alla base aumenta durante una semionda positiva, aumenta la corrente di emettitore. Di conseguenza, la caduta di tensione sulla resistenza di emettitore aumenta e anche la tensione d’uscita sale. Il segnale di ingresso e di uscita sono quindi in fase; lo sfasamento è di $\qty{0}{\degree}$.

[question:AD405]

---

La figura [ref:a_collector_circuit] mostra un semplice circuito a collettore comune con alimentazione elettrica, resistenza di emettitore e condensatori di accoppiamento.

<margin>
[picture:140:a_collector_circuit:Circuito a collettore comune con alimentazione elettrica, resistenza di emettitore e condensatori di accoppiamento]
</margin>

---

Per funzionare come amplificatore di corrente lineare, il transistor nel circuito a collettore comune necessita di un punto di funzionamento definito (in inglese bias, polarizzazione), che normalmente è stabilito da un partitore di tensione alla base.

La figura [ref:a_kennlinie] mostra la caratteristica di un transistor NPN con il punto di funzionamento impostato dal partitore di tensione. La polarizzazione di base è scelta in modo da lavorare sulla parte lineare della caratteristica di ingresso. Ciò implica anche che scorre sempre una certa corrente di riposo, anche quando non è presente alcun segnale di ingresso. Questo lo esamineremo più in dettaglio nel capitolo delle classi di amplificatori.

Se viene applicato un segnale di ingresso, ad esempio una tensione alternata sinusoidale, come mostrato nell'immagine, questo segnale viene amplificato dalla caratteristica di ingresso. Si noti qui l'etichettatura degli assi, da microampere diventano milliampere. La tensione risultante all'uscita può essere letta anche da questa caratteristica.

<margin>
[picture:1119:a_kennlinie:Caratteristica di un transistor NPN con punto di funzionamento e sovrapposizione del segnale]
</margin>

La resistenza di emettitore converte la corrente che scorre attraverso il percorso collettore-emettitore in una caduta di tensione, che viene prelevata all'emettitore. La corrente di emettitore del transistor scorre (insieme alla componente di corrente di base normalmente trascurabile) attraverso l'emettitore e la resistenza di emettitore verso massa. La corrente attraverso la resistenza di emettitore, a causa della caduta di tensione che si genera su di essa, provoca un aumento del potenziale dell'emettitore (tensione di emettitore) e agisce quindi come controreazione per la tensione di base. Ciò stabilizza ulteriormente il punto di funzionamento del transistor, perché le variazioni termiche della corrente di collettore vengono così compensate.

L'accoppiamento in ingresso e in uscita dei segnali alla base e all'emettitore avviene tramite i cosiddetti condensatori di accoppiamento. Il loro compito è tenere lontane dalla fase amplificatrice le componenti di tensione continua, che porterebbero a una variazione del punto di funzionamento.

Il condensatore di disaccoppiamento nella tensione di servizio (+) serve a scaricare segnali HF e BF indesiderati, in modo da evitare effetti di retroazione sullo stadio e sulla tensione di alimentazione. Inoltre, il collettore viene collegato, dal punto di vista del segnale (per la tensione alternata), all'ingresso e all'uscita tramite il condensatore di disaccoppiamento.

Il guadagno di tensione del circuito a collettore comune, con una progettazione appropriata, si muove nell'intervallo da $\num{0,9}$ a $\num{0,98}$ ed è sempre leggermente inferiore a $1$.

Ci si potrebbe chiedere quale utilità abbia un amplificatore con un guadagno di tensione inferiore a $1$. Il circuito a collettore comune possiede tuttavia un vantaggio decisivo, che considereremo di seguito.

[question:AD402]

Il circuito a collettore comune possiede un notevole guadagno di corrente. La sua impedenza di ingresso è relativamente alta, perché solo una piccola corrente può fluire nella base. L'impedenza di uscita, invece, è relativamente bassa. Se la tensione d’uscita viene modificata da un carico collegato, ciò cambia la tensione base-emettitore e il transistor regola di conseguenza la sua corrente di emettitore in modo da contrastare questa variazione. Grazie a questa controreazione, il circuito a collettore comune può pilotare un carico a bassa impedenza senza che la sua tensione d’uscita cambi significativamente.

[question:AD403]

Per questo motivo, il circuito a collettore comune viene spesso utilizzato come *stadio buffer tra l'oscillatore e ulteriori parti del circuito*, che altrimenti caricherebbero l'oscillatore a bassa impedenza, per ottenere un disaccoppiamento e una migliore stabilizzazione di frequenza dell'oscillatore.

[question:AD404]
