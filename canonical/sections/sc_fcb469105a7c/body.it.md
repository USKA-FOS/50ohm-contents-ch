Nella sezione precedente abbiamo conosciuto il [sec:kollektorschaltung] di un transistor bipolare. In questa sezione esaminiamo la *configurazione a emettitore comune*.

<margin>
[picture:1118:a_emitter_collector:Configurazione a emettitore comune e a collettore comune con denominazioni base (B), collettore (C) ed emettitore (E)]

Riassumiamo brevemente le caratteristiche della configurazione a collettore comune e a emettitore comune nella seguente tabella:

| l: Caratteristica | X: Configurazione a emettitore comune | X: Configurazione a collettore comune |
| Sfasamento | $\qty{180}{\degree}$ | $\qty{0}{\degree}$ |
| Guadagno di tensione | $\num{100}\dots\num{300}$ | $\num{0,9}\dots\num{0,98}$ |
| Impedenza di ingresso | alta | alta |
| Impedenza di uscita | alta | bassa |
</margin>

Come abbiamo appreso nella sezione precedente, la denominazione delle configurazioni fondamentali di un transistor bipolare dipende dal terminale che non serve né come ingresso né come uscita del circuito e quindi costituisce il punto di riferimento comune per il circuito di ingresso e di uscita. Nella configurazione a emettitore comune questo è l'emettitore.

---

[question:AD409]

<tip>
Le configurazioni amplificatrici dei transistor bipolari sono denominate in base al terminale a cui né l'ingresso né l'uscita sono direttamente collegati (cfr. figura [ref:a_emitter_collector]).
</tip>

---

La figura [ref:a_emitterschaltung] mostra una semplice configurazione a emettitore comune con alimentazione elettrica, resistenza di collettore e condensatori di accoppiamento.

Per il funzionamento come amplificatore di tensione lineare, il transistor nella configurazione a emettitore comune richiede un punto di funzionamento definito (inglese: bias, polarizzazione), che normalmente è stabilito da un partitore di tensione alla base.

<margin>
[picture:136:a_emitterschaltung:Configurazione a emettitore comune]
</margin>

[question:AD411]

La resistenza di collettore converte la corrente che scorre attraverso il percorso collettore-emettitore in una caduta di tensione, che viene prelevata al collettore. La corrente di collettore del transistor scorre (insieme alla componente normalmente trascurabile della corrente di base) attraverso l'emettitore e la resistenza di emettitore verso massa. La corrente attraverso la resistenza di emettitore, a causa della caduta di tensione che si genera su di essa, provoca un aumento del potenziale dell'emettitore (tensione dell'emettitore) e agisce quindi come controreazione per la tensione della base. Ciò stabilizza ulteriormente il punto di funzionamento del transistor, perché le variazioni termicamente indotte della corrente di collettore vengono così compensate.

L'accoppiamento in ingresso e in uscita dei segnali alla base e al collettore avviene tramite i cosiddetti condensatori di accoppiamento. Il loro compito è tenere lontane dalla fase amplificatrice le componenti di tensione continua, che porterebbero a una variazione del punto di funzionamento.

[question:AD412]

Il condensatore di disaccoppiamento nella tensione di servizio (+) serve a deviare segnali HF e BF indesiderati, in modo da evitare effetti di retroazione sullo stadio e sulla tensione di alimentazione.

Lo sfasamento tra il segnale di ingresso e di uscita nella configurazione a emettitore comune è di $\qty{180}{\degree}$, poiché durante una semionda positiva nella tensione d’ingresso alla base, la corrente di collettore aumenta e quindi la caduta di tensione sulla resistenza di collettore aumenta. Di conseguenza, la tensione sul condensatore di uscita diminuisce. Si verifica una semionda negativa all'uscita dello stadio amplificatore.

[question:AD407]
[question:AD408]

Il guadagno di tensione della configurazione a emettitore comune, con un dimensionamento appropriato, si trova nell'intervallo di $100\dots 300$ ed è quindi molto alto rispetto alla configurazione a collettore comune.

[question:AD410]

Il condensatore all'emettitore bypassa la resistenza di emettitore per le tensioni alternate, riducendo così la controreazione e aumentando il guadagno in tensione alternata, mentre il punto di funzionamento in corrente continua rimane invariato.

[question:AD413]

Tuttavia, se il condensatore dell'emettitore viene rimosso, il fattore di guadagno del circuito diminuisce considerevolmente (ad esempio da $\num{100}$ a $\num{10}$). Alla fine è definito solo dal rapporto tra la resistenza di collettore e la resistenza di emettitore.

[question:AD414]
[question:AD415]

Se una configurazione a emettitore comune, come nella domanda seguente, viene pilotata senza una predisposizione del punto di funzionamento tramite un partitore di tensione, il pilotaggio del transistor avviene esclusivamente tramite il segnale d’ingresso applicato. Solo quando questo supera il valore di circa $\qty{0,6}{\volt}$, il percorso base-emettitore del transistor diventa conduttivo. Di conseguenza, una corrente di collettore scorre solo durante i picchi di tensione, causando una caduta di tensione all'uscita. Come segnale di uscita appare la tensione di alimentazione, che diminuisce nei momenti in cui il transistor entra nella regione conduttiva. Questo spiega il corrispondente segnale di uscita.

[question:AD406]

