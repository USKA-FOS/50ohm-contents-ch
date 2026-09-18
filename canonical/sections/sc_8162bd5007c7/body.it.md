Come abbiamo già imparato, le batterie forniscono una tensione elettrica perché in esse vengono separate le cariche. Questo processo avviene grazie a reazioni elettrochimiche che si innescano non appena il circuito viene chiuso. Gli accumulatori, chiamati brevemente anche accu, funzionano in modo simile, ma hanno la particolarità di essere ricaricabili. In questo caso, viene applicata una tensione alla batteria e la reazione elettrochimica procede in senso inverso. Successivamente, è possibile iniziare nuovamente la scarica. Le batterie, invece, non possono essere ricaricate e sono utilizzabili una sola volta.

Nei ricetrasmettitori portatili vengono impiegati perlopiù accu, ma a volte anche batterie. Per far funzionare le stazioni radio in modo indipendente dalla rete elettrica, ad esempio durante un Fieldday, si utilizzano spesso accu.

La scritta presente sulle batterie (Figura [ref:n_Bat_AA]) indica ad esempio il polo positivo e quello negativo e segnala l’importanza di rispettare la corretta polarità. Per le batterie, è fondamentale osservare sempre l’avvertenza "Non ricaricabile".

La Figura [ref:n_schaltzeichen_batt] mostra il simbolo di circuito di una batteria o di un accu. La linea più lunga nel simbolo indica il polo positivo, quella più corta il polo negativo. Un utile trucco mnemonico è il seguente: un segno più (+) richiede due linee, mentre un segno meno (–) ne richiede solo una.

[question:NB201]
[question:NB203]

<margin>
[photo:89:n_Bat_AA:Una batteria con indicazione dei poli e avvertenze]
</margin>

<margin>
[picture:517:n_schaltzeichen_batt:Simbolo di circuito di una batteria]
</margin>

<webindepth>
Esistono batterie e accu di vario tipo, con tensioni, capacità e forme costruttive differenti:
* Le tensioni più comuni per batterie o accu sono ad esempio $\qty{1,5}{\volt}$ o $\qty{9}{\volt}$. Tuttavia, ne esistono anche con altre tensioni. Ad esempio, i modellini radiocomandati utilizzano perlopiù $\qty{7,2}{\volt}$. Nei trapani a batteria si trovano spesso accu con $\qty{18}{\volt}$, $\qty{20}{\volt}$ o $\qty{40}{\volt}$.
* La capacità di una batteria o di un accu viene indicata in amperora ($\unit{\ampere\hour}$). Se un accu ha una capacità di $\qty{5}{\ampere\hour}$, può erogare una corrente di un ampere per 5 ore, oppure ad esempio una corrente di 0,5 ampere per 10 ore, o una corrente di $\qty{5}{\ampere}$ solo per un’ora. Nelle batterie spesso non viene indicata la capacità. Le batterie di uso domestico hanno spesso una capacità inferiore a $\qty{5}{\ampere\hour}$. Gli accu di grandi dimensioni possono avere una capacità di $\qty{100}{\ampere\hour}$ o più. A differenza delle batterie, negli accu la capacità viene quasi sempre indicata.
* Per quanto riguarda le forme costruttive, le celle cilindriche AA e AAA sono molto diffuse e vengono impiegate nella maggior parte dei dispositivi domestici. Tuttavia, soprattutto tra gli accu, esistono moltissime altre forme, spesso specifiche per un singolo apparecchio.
</webindepth>

<margin>
[photo:209:batterien_und_akkus_sammlung:Varie batterie e accu]
</margin>

<attention>
Gli accu non devono mai essere completamente scaricati. Questa cosiddetta scarica profonda può danneggiare l’accu. In pratica, la scarica si riconosce dal fatto che la tensione dell’accu diminuisce gradualmente. L’erogazione di corrente deve essere interrotta prima che venga superata la tensione minima indicata dal produttore.
</attention>

Molti apparecchi richiedono più batterie. Di norma, questo serve per aumentare la tensione quando la tensione di una singola batteria, ad esempio $\qty{1,5}{\volt}$, non è sufficiente per il funzionamento. Nel vano batterie dell’apparecchio, queste vengono collegate in serie, in modo che il polo negativo della batteria precedente si colleghi al polo positivo di quella successiva. La tensione ai capi di questa catena si calcola come segue:

$\text{tensione totale} = \text{numero batterie} \cdot \text{tensione batteria}$

[question:NB204]

---

In generale, occorre evitare cortocircuiti nelle batterie e negli accu. Soprattutto con accu moderni e ad alta potenza, esiste il rischio di surriscaldamento. Questi possono prendere fuoco o, a causa della corrente di cortocircuito generata, causare un incendio.

<danger>
Mentre negli alimentatori di rete, in caso di guasto, un fusibile può interrompere il flusso di corrente, questo meccanismo di protezione è perlopiù assente nelle batterie o negli accu. L’intensità di corrente che le batterie e gli accu possono erogare supera spesso di molte volte il valore massimo degli alimentatori di rete. Questo vale in particolare per gli accu ad alta capacità, come ad esempio le batterie delle auto, che possono erogare correnti di picco di $\qty{1000}{\ampere}$ o più. Quando si utilizzano accu esterni ad alta capacità, è assolutamente necessario prevedere un fusibile aggiuntivo, come quello mostrato nella Figura [ref:n_Bat_Sicherung]!
[photo:90:n_Bat_Sicherung:Scatola di connessione con fusibili per auto e uscite protette contro l’inversione di polarità per la protezione di accu ad alta potenza]
</danger>

[question:ND110]

Nei accu vengono impiegate diverse tecnologie basate su reazioni elettrochimiche differenti: da decenni, le batterie al piombo vengono utilizzate nelle auto. Piccoli apparecchi portatili utilizzavano in passato accu al nichel e cadmio (NiCd) e in seguito la tecnologia nichel-metallo idruro (NiMH). Nei telefoni cellulari, nelle macchine fotografiche digitali o nei notebook, oggi dominano gli accu con tecnologia ioni di litio. Nel radioamatoriale vengono utilizzate sempre più spesso miscele di litio-ferro-fosfato (LiFePO4).

Le differenze tra le reazioni elettrochimiche devono essere prese in considerazione durante la carica di questi diversi tipi di accu. È necessario utilizzare caricabatterie specifici per ogni tecnologia. Cariche e scariche non corrette possono causare il surriscaldamento degli accu. Al contatto, possono verificarsi pericolose ustioni. È inoltre possibile che gli accu esplodano o prendano fuoco a causa del surriscaldamento. Il rilascio di liquidi può provocare ustioni chimiche o avvelenamenti.

<attention>
Le batterie e gli accu devono sempre essere smaltiti correttamente. Non vanno gettati nella spazzatura domestica! Questo è indicato dal simbolo del bidone della spazzatura barrato (si veda la Figura [ref:n_Bat_AA]).
</attention>

[question:NK306]

<latexonly>
\newpage
</latexonly>