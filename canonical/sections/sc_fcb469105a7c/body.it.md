La denominazione del circuito base di un transistor bipolare dipende da quale terminale (base, collettore o emettitore) è attraversato sia dal segnale di ingresso che da quello di uscita.

Nella *circuito dell'emettitore*, il segnale di ingresso scorre dalla sorgente attraverso la base, l'*emettitore* e la massa tornando alla sorgente. Il segnale di uscita scorre dal collettore attraverso il carico (pozzo) e attraverso la massa tornando all'*emettitore*.

[question:AD409]

%TODO: Inserire eventualmente uno schema con i percorsi di corrente.

Funzionamento di un amplificatore in circuito dell'emettitore:

%TODO: Inserire immagine del circuito dell'emettitore con partitore di tensione e condensatori di accoppiamento

Per funzionare come amplificatore di tensione lineare, il transistor nel circuito dell'emettitore necessita di un punto di funzionamento (BIAS) definito, che di solito è determinato da un partitore di tensione sulla base.

[question:AD411]

La resistenza di collettore converte la corrente che scorre attraverso la giunzione collettore-emettitore in una caduta di tensione che viene prelevata al collettore. La corrente di collettore del transistor scorre (insieme alla frazione di corrente di base normalmente trascurabile) attraverso l'emettitore attraverso la resistenza di emettitore verso massa. La corrente attraverso la resistenza di emettitore provoca, a causa della caduta di tensione risultante su di essa, un aumento del potenziale dell'emettitore (tensione dell'emettitore) e agisce quindi come controreazione per la tensione di base. Ciò stabilizza ulteriormente il punto di funzionamento del transistor, poiché le variazioni della corrente di collettore dovute a cause termiche vengono regolate.

Per mantenere la controreazione il più bassa possibile per l'amplificazione dei segnali di tensione alternata, la resistenza di emettitore viene bypassata capacitivamente (tramite un condensatore).

[question:AD413]

L'accoppiamento e lo scollegamento dei segnali in ingresso e in uscita avvengono tramite i cosiddetti condensatori di accoppiamento. Questi hanno il compito di impedire che componenti di tensione continua raggiungano lo stadio di amplificazione, il che porterebbe a una modifica del punto di funzionamento.

[question:AD412]

Il condensatore di disaccoppiamento nella tensione di alimentazione (+) serve a scaricare segnali indesiderati HF e NF, in modo da evitare effetti di retroazione sullo stadio e sulla tensione di alimentazione.

Lo sfasamento tra segnale di ingresso e di uscita nel circuito dell'emettitore è di $\qty{180}{\degree}$, poiché per una semionda positiva della tensione di ingresso la corrente di collettore aumenta e quindi aumenta la caduta di tensione sulla resistenza di collettore. Ciò riduce la tensione sul condensatore di uscita. Si verifica una semionda negativa all'uscita dello stadio di amplificazione.

[question:AD407]
[question:AD408]

Se un circuito dell'emettitore viene utilizzato senza preimpostazione del punto di funzionamento tramite un partitore di tensione, come nella domanda successiva, l'azionamento del transistor avviene esclusivamente tramite il segnale di ingresso applicato. Solo quando questo supera il valore di circa $\qty{0,6}{\volt}$, la giunzione base-emettitore del transistor diventa conduttiva. In questo modo, una corrente di collettore scorre solo nei picchi di tensione, che provoca una caduta di tensione in uscita. Come segnale di uscita appare la tensione di alimentazione, che diminuisce nei momenti in cui il transistor entra nella regione conduttiva. Ciò spiega il segnale di uscita corrispondente.

[question:AD406]

L'amplificazione di tensione del circuito dell'emettitore si muove, con un'adeguata progettazione, nell'intervallo di $100\dots 300$ ed è quindi elevata. Tuttavia, se il condensatore dell'emettitore viene rimosso, il fattore di amplificazione del circuito diminuisce notevolmente. Viene infine definito solo dal rapporto tra la resistenza di collettore e la resistenza di emettitore.

[question:AD414]
[question:AD415]
[question:AD410]










