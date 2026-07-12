La denominazione del circuito fondamentale di un transistor bipolare dipende da quale terminale (base, collettore o emettitore) viene attraversato dal segnale di ingresso e di uscita.

Nella *circuito del collettore*, il segnale di ingresso fluisce dalla sorgente attraverso la base, il *collettore* e la tensione di alimentazione di ritorno alla sorgente. Il segnale di uscita fluisce dal collettore attraverso il carico (sink) e attraverso la tensione di alimentazione di ritorno al *collettore*.

[question:AD401]

Per il funzionamento come amplificatore di corrente lineare, il transistor nel circuito del collettore necessita di un punto di funzionamento (BIAS) definito, che viene normalmente stabilito da un partitore di tensione sulla base.

La resistenza di emettitore converte la corrente che fluisce attraverso la sezione collettore-emettitore in una caduta di tensione che viene prelevata all'emettitore. La corrente di emettitore del transistor fluisce (insieme alla componente di corrente di base normalmente trascurabile) attraverso l'emettitore attraverso la resistenza di emettitore verso massa. La corrente attraverso la resistenza di emettitore causa, a causa della caduta di tensione risultante su di essa, un aumento del potenziale dell'emettitore (tensione dell'emettitore) e agisce quindi come controreazione per la tensione di base. Ciò stabilizza ulteriormente il punto di funzionamento del transistor, poiché le variazioni della corrente di collettore dovute a fattori termici vengono così compensate.

L'accoppiamento e lo scollegamento dei segnali su base ed emettitore avviene tramite i cosiddetti condensatori di accoppiamento. Questi hanno il compito di impedire che componenti di tensione continua vengano immesse nello stadio amplificatore, il che porterebbe a una modifica del punto di funzionamento.

Il condensatore di disaccoppiamento nella tensione di servizio (+) serve a scaricare segnali indesiderati ad alta e bassa frequenza, in modo da evitare effetti di retroazione sullo stadio e sulla tensione di alimentazione. Inoltre, il collettore viene collegato all'ingresso e all'uscita tramite il condensatore di disaccoppiamento per quanto riguarda il segnale (per tensione alternata).

Lo sfasamento tra segnale di ingresso e di uscita nel circuito del collettore è di $\qty{0}{\degree}$, poiché durante una semionda positiva della tensione di ingresso la corrente di emettitore aumenta e quindi aumenta la caduta di tensione sulla resistenza di emettitore. Ciò provoca un aumento della tensione sul condensatore di uscita. Si verifica una semionda positiva all'uscita dello stadio amplificatore.

L'amplificazione di tensione del circuito del collettore, con un dimensionamento appropriato, si muove nell'intervallo da $\num{0,9}$ a $\num{0,98}$ ed è sempre leggermente inferiore a $1$. L'amplificazione di corrente del circuito del collettore, invece, è molto elevata, poiché l'impedenza di ingresso del circuito è relativamente alta. L'impedenza di uscita, invece, è molto bassa rispetto all'impedenza di ingresso.

[question:AD405]
[question:AD402]
[question:AD403]

Il *circuito del collettore viene spesso utilizzato come stadio di buffer tra l'oscillatore e altre parti del circuito*, che altrimenti caricherebbero l'oscillatore con bassa impedenza, per ottenere un disaccoppiamento e una migliore stabilizzazione della frequenza dell'oscillatore.

[question:AD404]

