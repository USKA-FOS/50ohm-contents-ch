Nel capitolo precedente abbiamo imparato a conoscere il circuito a collettore comune di un transistor bipolare. In questo capitolo esaminiamo la *configurazione a emettitore comune*.

<margin>
[picture:1118:a_emitter_collector:Circuiti a emettitore e a collettore comune con denominazioni base (B), collettore (C) ed emettitore (E)]

Riassumiamo brevemente le proprietà dei circuiti a emettitore e a collettore comune nella seguente tabella:

| l: Proprietà | X: Configurazione a emettitore comune | X: Circuito a collettore comune |
| Sfasamento | $\qty{180}{\degree}$ | $\qty{0}{\degree}$ |
| Guadagno di tensione | $\num{100}\dots\num{300}$ | $\num{0,9}\dots\num{0,98}$ |
| Impedenza di ingresso | alta | alta |
| Impedenza di uscita | alta | bassa |
</margin>

Come abbiamo appreso nel capitolo precedente, la denominazione dei circuiti base di un transistor bipolare si basa sul terminale che non è né ingresso né uscita del circuito e che, quindi, costituisce il punto di riferimento comune per il circuito di ingresso e di uscita. Nella configurazione a emettitore comune, questo terminale è l’emettitore.

---

[question:AD409]

<tip>
I circuiti amplificatori dei transistor bipolari vengono denominati in base al terminale al quale non sono direttamente collegati né l’ingresso né l’uscita (cfr. figura [ref:a_emitter_collector]).
</tip>

---

La figura [ref:a_emitterschaltung] mostra una semplice configurazione a emettitore comune con alimentazione elettrica, resistenza di collettore e condensatori di accoppiamento.

Per funzionare come amplificatore lineare di tensione, il transistor nella configurazione a emettitore comune necessita di un punto di funzionamento definito (in inglese *bias*, polarizzazione), che viene generalmente stabilito da un partitore di tensione alla base.

<margin>
[picture:136:a_emitterschaltung:Configurazione a emettitore comune]
</margin>

[question:AD411]

La resistenza di collettore converte la corrente che scorre attraverso il percorso collettore-emettitore in una caduta di tensione prelevata al collettore. La corrente di collettore del transistor scorre (insieme alla componente di corrente di base, generalmente trascurabile) attraverso l’emettitore e la resistenza di emettitore verso massa. La corrente che attraversa la resistenza di emettitore, generando una caduta di tensione su di essa, provoca un aumento del potenziale dell’emettitore (tensione di emettitore) e agisce quindi come controreazione per la tensione di base. Questo stabilizza ulteriormente il punto di funzionamento del transistor, poiché le variazioni termiche della corrente di collettore vengono regolate.

L’ingresso e l’uscita dei segnali alla base e al collettore avviene tramite i cosiddetti condensatori di accoppiamento. Questi hanno il compito di bloccare le componenti in corrente continua dalla fase di amplificazione, che potrebbero alterare il punto di funzionamento.

[question:AD412]

Il condensatore di disaccoppiamento nell’alimentazione elettrica (+) serve a eliminare segnali indesiderati in HF e BF, evitando così effetti di reazione sulla fase e sull’alimentazione.

Lo sfasamento tra il segnale di ingresso e quello di uscita nella configurazione a emettitore comune è di $\qty{180}{\degree}$, poiché in una semionda positiva della tensione di ingresso alla base, la corrente di collettore aumenta e, di conseguenza, aumenta la caduta di tensione sulla resistenza di collettore. Questo fa sì che la tensione al condensatore di uscita diminuisca, generando una semionda negativa all’uscita della fase di amplificazione.

[question:AD407]
[question:AD408]

Il guadagno di tensione della configurazione a emettitore comune, se correttamente dimensionata, si attesta nell’intervallo di $100\dots 300$ ed è quindi molto elevato rispetto al circuito a collettore comune.

[question:AD410]

Il condensatore all’emettitore bypassa la resistenza di emettitore per i segnali in corrente alternata, riducendo la controreazione e aumentando il guadagno in tensione alternata, mentre il punto di funzionamento in corrente continua rimane invariato.

[question:AD413]

Se invece il condensatore di emettitore viene rimosso, il fattore di amplificazione del circuito diminuisce notevolmente (ad esempio da $\num{100}$ a $\num{10}$). In questo caso, il fattore di amplificazione è definito dal rapporto tra la resistenza di collettore e quella di emettitore.

[question:AD414]
[question:AD415]

Se una configurazione a emettitore comune viene utilizzata come nella domanda successiva senza una polarizzazione del punto di funzionamento tramite un partitore di tensione, il pilotaggio del transistor avviene esclusivamente tramite il segnale di ingresso fornito. Solo quando questo supera circa $\qty{0,6}{\volt}$, la giunzione base-emettitore del transistor diventa conduttiva. Di conseguenza, la corrente di collettore scorre solo nei picchi di tensione, generando una caduta di tensione all’uscita. Il segnale di uscita corrisponde alla tensione di alimentazione, che diminuisce nei momenti in cui il transistor entra nella regione di conduzione. Questo spiega il corrispondente segnale di uscita.

[question:AD406]
