Nei prossimi due capitoli ci occuperemo di due importanti circuiti base di un transistor bipolare. In questo capitolo analizzeremo innanzitutto il *circuito a collettore comune*, mentre nel capitolo successivo tratteremo la *configurazione a emettitore comune*. Entrambi i circuiti sono illustrati nella figura [ref:a_emitter_collector]. Presentano proprietà diverse e vengono quindi impiegati per applicazioni differenti.

<margin>
[picture:1118:a_emitter_collector:Circuiti a emettitore comune e a collettore comune con denominazioni Base (B), Collettore (C) ed Emettitore (E)]
</margin>

La denominazione dei circuiti base di un transistor bipolare si riferisce al terminale che non viene utilizzato né come ingresso né come uscita del circuito e che, quindi, costituisce il punto di riferimento comune per il circuito di ingresso e quello di uscita. Nel circuito a collettore comune questo terminale è il collettore.

---

[question:AD401]

<tip>
I circuiti amplificatori con transistor bipolari vengono denominati in base al terminale a cui non sono direttamente collegati né l’ingresso né l’uscita (cfr. figura [ref:a_emitter_collector]).
</tip>

Poiché il collettore è solitamente collegato alla tensione di alimentazione e, per le tensioni alternate, si trova approssimativamente a un potenziale fisso, la tensione sull’emettitore segue quella della base. Per questo motivo, il circuito a collettore comune viene spesso chiamato *inseguitore di emettitore*.

Se, ad esempio, la tensione d’ingresso alla base aumenta durante una semionda positiva, la corrente di emettitore aumenta. Di conseguenza, la caduta di tensione sulla resistenza di emettitore cresce e anche la tensione d’uscita sale. Il segnale d’ingresso e quello d’uscita sono quindi in fase; lo sfasamento è di $\qty{0}{\degree}$.

[question:AD405]

---

La figura [ref:a_collector_circuit] mostra un semplice circuito a collettore comune con alimentazione elettrica, resistenza di emettitore e condensatori di accoppiamento.

<margin>
[picture:140:a_collector_circuit:Circuito a collettore comune con alimentazione elettrica, resistenza di emettitore e condensatori di accoppiamento]
</margin>

---

Per funzionare come amplificatore lineare di corrente, il transistor nel circuito a collettore comune necessita di un definito punto di funzionamento (in inglese *bias* o polarizzazione), che viene generalmente impostato tramite un partitore di tensione alla base.

La figura [ref:a_kennlinie] mostra la curva caratteristica di un transistor NPN con il punto di funzionamento impostato dal partitore di tensione. La tensione di polarizzazione della base viene scelta in modo da lavorare sulla parte lineare della curva caratteristica d’ingresso. Questo implica anche che, anche in assenza di un segnale d’ingresso, circoli una certa corrente di riposo. Approfondiremo questo aspetto nel capitolo dedicato alle classi di amplificazione.

Se viene applicato un segnale d’ingresso, ad esempio una tensione alternata sinusoidale come mostrato nell’immagine, questo segnale viene amplificato attraverso la curva caratteristica d’ingresso. Si noti la scala degli assi: dai microampere ai milliampere. La tensione risultante all’uscita può essere letta anche da questa curva caratteristica.

<margin>
[picture:1119:a_kennlinie:Curva caratteristica di un transistor NPN con punto di funzionamento e sovrapposizione del segnale]
</margin>

La resistenza di emettitore converte la corrente che fluisce attraverso il percorso collettore-emettitore in una caduta di tensione prelevata all’emettitore. La corrente di emettitore del transistor (unitamente alla componente di corrente di base, solitamente trascurabile) fluisce attraverso la resistenza di emettitore verso massa. La corrente che attraversa la resistenza di emettitore, generando una caduta di tensione su di essa, provoca un aumento del potenziale dell’emettitore (tensione di emettitore) e agisce quindi come controreazione sulla tensione di base. Questo stabilizza ulteriormente il punto di funzionamento del transistor, poiché le variazioni termiche della corrente di collettore vengono compensate.

L’ingresso e l’uscita dei segnali alla base e all’emettitore avvengono tramite i cosiddetti condensatori di accoppiamento. Questi hanno il compito di separare le componenti in continua della tensione dallo stadio amplificatore, evitando così alterazioni del punto di funzionamento.

Il condensatore di disaccoppiamento sulla tensione di servizio (+) serve a eliminare eventuali segnali indesiderati in HF e BF, evitando effetti di reazione sullo stadio e sulla tensione di alimentazione. Inoltre, il condensatore di disaccoppiamento pone il collettore, dal punto di vista del segnale alternato, allo stesso potenziale di ingresso e uscita.

Il guadagno di tensione del circuito a collettore comune, con un dimensionamento appropriato, si attesta tra $\num{0,9}$ e $\num{0,98}$ ed è sempre leggermente inferiore a $1$.

Ci si potrebbe chiedere quale utilità abbia un amplificatore con un guadagno di tensione inferiore a $1$. Tuttavia, il circuito a collettore comune presenta un vantaggio decisivo, che analizzeremo di seguito.

[question:AD402]

Il circuito a collettore comune offre un notevole aumento di corrente. La sua impedenza d’ingresso è relativamente elevata, poiché solo una piccola corrente fluisce nella base. Al contrario, l’impedenza d’uscita è relativamente bassa. Se la tensione d’uscita viene modificata da un carico collegato, la tensione base-emettitore cambia e il transistor regola la corrente di emettitore in modo da contrastare questa variazione. Grazie a questa controreazione, il circuito a collettore comune può pilotare un carico a bassa impedenza senza che la sua tensione d’uscita subisca forti variazioni.

[question:AD403]

Per questo motivo, il circuito a collettore comune viene spesso utilizzato come *stadio buffer tra oscillatore e altre parti del circuito* che altrimenti caricherebbero l’oscillatore con un’impedenza troppo bassa, garantendo così un disaccoppiamento e una migliore stabilità in frequenza dell’oscillatore.

[question:AD404]