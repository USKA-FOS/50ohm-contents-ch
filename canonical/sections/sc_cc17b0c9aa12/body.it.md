[question:AC401]

Il diodo pn è costituito da due regioni semiconduttrici che, tramite il processo di drogaggio, presentano un eccesso di elettroni liberi (n) o di lacune libere (p). A destra e a sinistra dell’interfaccia si forma una cosiddetta zona di carica spaziale, che non contiene praticamente portatori di carica liberi. La regione n rappresenta il catodo, quella p l’anodo.

Se al diodo viene applicata una tensione diretta (positiva all’anodo, negativa al catodo), gli elettroni provenienti dalla regione drogata n vengono inviati verso la regione p e le lacune dalla regione p verso quella n. In questo modo si ottiene la risposta corretta.

Può risultare confuso il fatto che il verso convenzionale della corrente sia opposto alla direzione del flusso degli elettroni. La freccia della corrente punta quindi dall’anodo al catodo, sebbene il flusso degli elettroni vada dal catodo all’anodo.

[question:AC403]

I diodi pn mostrano una dipendenza esponenziale della corrente del diodo dalla tensione del diodo. La corrente di saturazione aumenta con l’aumento della temperatura. Questo fa sì che la tensione del diodo necessaria per una determinata corrente del diodo diminuisca all’aumentare della temperatura. La "tensione diretta" quindi diminuisce (come regola empirica di circa $\qty{-2}{\milli\volt\per\kelvin}$ di aumento della temperatura).
<indepth>

La corrente del diodo è:

$I_D(T) = I_S(T) \cdot e^{\frac{U_D}{U_T}}$

$I_S$ è la corrente di saturazione, $U_T = k T/q$ la cosiddetta tensione termica. Qui $k$ è la costante di Boltzmann, $q$ la carica elementare.

Con l’aumento della temperatura, la corrente di saturazione aumenta e la funzione esponenziale diminuisce. Tuttavia, prevale la dipendenza dalla temperatura della corrente di saturazione.

</indepth>

[question:AC404]

---

Il diodo a capacità variabile (cfr. figura [ref:a_diode_kapazitaet]) sfrutta la capacità tra le regioni n e p attraverso la zona di carica spaziale, analogamente a un condensatore a piastre. Tuttavia, non deve scorrere una corrente continua apprezzabile, quindi il diodo deve essere polarizzato in polarizzazione inversa.

<margin>
[picture:1068:a_diode_kapazitaet:Simbolo di circuito del diodo a capacità variabile]
</margin>

Più negativa è la tensione del diodo (o più alta la tensione inversa), più la zona di carica spaziale si espande e minore diventa la capacità del diodo.

Nelle domande AC405 e AC406 vengono utilizzati *diodi antiparalleli* per limitare l’ampiezza di una tensione alternata. Tali circuiti vengono impiegati, ad esempio, per proteggere gli ingressi dei ricevitori da tensioni che potrebbero danneggiare i transistor di ingresso.

[question:AC405]

In questo caso si tratta di diodi al silicio, che hanno una tensione di soglia di circa $\qty{0,6}{\volt}$. Se quindi la tensione d’ingresso supera $\qty{0,6}{\volt}$, il diodo di destra si polarizza in conduzione. Se scende sotto $\qty{-0,6}{\volt}$, si polarizza in conduzione il diodo di sinistra.

Nel primo semiperiodo la tensione necessaria non viene ancora raggiunta, quindi viene trasmessa invariata. I due semiperiodi successivi, invece, hanno ampiezze che superano la tensione di soglia. Le ampiezze vengono "tagliate" a $\qty{\pm 0,6}{\volt}$.

[question:AC406]

La soluzione è analoga al compito precedente, ma in questo caso i diodi sono *diodi al germanio*, con una tensione di soglia di circa $\qty{0,3}{\volt}$. Pertanto, tutte le semi-onde vengono tagliate.

[question:AC407]

Di seguito vengono descritti componenti che interagiscono con la luce: la fotoresistenza e il fotodiodo.

La fotoresistenza è un componente dotato di due contatti non bloccanti. Si comporta come una normale resistenza ohmica: la corrente aumenta linearmente con la tensione applicata. Il valore della resistenza può essere ridotto dall’assorbimento di luce: i fotoni assorbiti aumentano la densità dei portatori di carica liberi. Se non viene applicata alcuna tensione, non scorre alcuna corrente.

---

Il fotodiodo, invece, è un diodo pn (cfr. figura [ref:a_photodiode]). Qui la luce viene assorbita nella zona di carica spaziale, generando coppie elettrone-lacuna che vengono separate dal campo elettrico della zona di carica spaziale. Questo campo esiste anche senza polarizzazione esterna. Anche per $U_D=0$ scorre una corrente (una corrente di cortocircuito). Questa corrente ha direzione opposta a quella della corrente convenzionale del diodo.

<margin>
[picture:1069:a_photodiode:Simbolo di circuito del fotodiodo]
</margin>

---

[question:AC408]

Gli optoisolatori combinano un diodo luminoso e un fotodiodo in un unico contenitore, dove il lato di ingresso (diodo luminoso) e il lato di uscita (fotodiodo) sono isolati tra loro (isolamento galvanico).

Questi componenti vengono utilizzati per isolare galvanicamente le interfacce, ad esempio per evitare loop di massa che possono causare il ronzio della rete elettrica.

<margin>
[picture:1070:a_optokoppler:Simbolo di circuito dell’optocoupler]
</margin>