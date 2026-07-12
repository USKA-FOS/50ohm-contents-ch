[question:AC401]

La diodo pn è composta da due regioni semiconduttrici che, tramite il processo di drogaggio, hanno un eccesso di elettroni liberi (n) o di lacune (p). A destra e a sinistra della superficie di separazione si forma una cosiddetta zona di svuotamento, che praticamente non contiene portatori di carica liberi. La regione n rappresenta il catodo, la regione p l'anodo.

Se alla diodo viene applicata una tensione di conduzione (positiva all'anodo, negativa al catodo), gli elettroni vengono inviati dalla regione drogata n verso la regione p e le lacune dalla regione p verso la regione n. In questo modo si ottiene la risposta corretta.

Ciò che può essere un po' confusionario è che la direzione tecnica della corrente è opposta alla direzione del flusso di elettroni. La freccia della corrente punta quindi dall'anodo al catodo, sebbene il flusso di elettroni avvenga dal catodo all'anodo.

[question:AC403]

Le diodi pn mostrano una dipendenza esponenziale della corrente di diodo dalla tensione di diodo. La corrente di saturazione aumenta con l'aumentare della temperatura. Ciò fa sì che la tensione di diodo necessaria per una determinata corrente di diodo diminuisca con l'aumentare della temperatura. La "tensione di conduzione" diminuisce quindi (come regola empirica di circa $\qty{-2}{\milli\volt\per\kelvin}$ per aumento di temperatura).
<indepth>

La corrente di diodo è:
  
$I_D(T) = I_S(T) \cdot e^{\frac{U_D}{U_T}}$
  
$I_S$ è la corrente di saturazione, $U_T = k T/q$ la cosiddetta tensione di temperatura. Qui $k$ è la Costante di Boltzmann, $q$ la carica elementare.
  
Con l'aumentare della temperatura, la corrente di saturazione aumenta e la funzione esponenziale diminuisce. Tuttavia, la dipendenza dalla temperatura della corrente di saturazione prevale.

</indepth>

[question:AC404]

---

La diodo capacità (cfr. figura [ref:a_diode_kapazitaet]) sfrutta la capacità tra le regioni n e p attraverso la zona di svuotamento, analogamente a un Condensatore a piastre. Tuttavia, non deve fluire alcuna corrente continua apprezzabile, quindi la diodo deve essere polarizzata inversamente.

<margin>
[picture:1068:a_diode_kapazitaet:simbolo di circuito diodo capacità]
</margin>

Quanto più negativa è la tensione di diodo (o quanto maggiore è la tensione inversa), tanto più si espande la zona di svuotamento e tanto minore diventa la capacità di diodo.

Nelle domande AC405 e AC406 vengono utilizzate *diodi antiparalleli* per limitare l'ampiezza di una tensione alternata. Tali circuiti vengono utilizzati, ad esempio, per proteggere gli ingressi dei ricevitori da tensioni che potrebbero distruggere i transistor di ingresso.

[question:AC405]

Si tratta di diodi al silicio, che hanno una tensione di soglia di circa $\qty{0,6}{\volt}$. Quindi, se la tensione d’ingresso supera $\qty{0,6}{\volt}$, la diodo di destra conduce. Se scende al di sotto di $\qty{-0,6}{\volt}$, la diodo di sinistra conduce.

Nella prima mezza onda la tensione necessaria non viene ancora raggiunta, quindi viene trasmessa invariata. Le due successive mezze onde, tuttavia, hanno ampiezze che superano la tensione di soglia. Le ampiezze vengono "tagliate" a $\qty{\pm 0,6}{\volt}$.

[question:AC406]

La soluzione è analoga al problema precedente, ma qui le diodi sono *diodi al germanio*, la tensione di soglia è di circa $\qty{0,3}{\volt}$. Pertanto, tutte le mezze onde vengono tagliate.

[question:AC407]

Di seguito vengono descritti componenti che interagiscono con la luce: il fotoresistore e la fotodiodo.

Il fotoresistore è un componente che dispone di due contatti non bloccanti. Si comporta come una resistenza ohmica convenzionale: la corrente aumenta linearmente con la tensione applicata. Il valore della resistenza può essere ridotto dall'assorbimento di luce: i fotoni assorbiti aumentano la densità dei portatori di carica liberi. Se non c'è tensione, non scorre corrente.

---

La fotodiodo, invece, è una diodo pn (cfr. figura [ref:a_photodiode]). La luce viene qui assorbita nella zona di svuotamento, si creano coppie elettrone-lacuna che vengono separate nel campo elettrico della zona di svuotamento. Questo campo esiste anche senza polarizzazione esterna. Anche per $U_D=0$ scorre una corrente (una Corrente di cortocircuito). Questa corrente ha la direzione opposta alla corrente di diodo convenzionale.

<margin>
[picture:1069:a_photodiode:simbolo di circuito fotodiodo]
</margin>

---

[question:AC408]

Gli optoisolatori combinano una diodo emettitrice di luce e una fotodiodo in un unico alloggiamento, dove il lato di ingresso (diodo emettitrice di luce) e il lato di uscita (fotodiodo) sono isolati l'uno dall'altro (separati galvanicamente).

Questi componenti vengono utilizzati per separare galvanicamente le interfacce, ad esempio per evitare anelli di massa che possono causare ronzio di rete indotto.

<margin>
[picture:1070:a_optokoppler:simbolo di circuito optoisolatore]
</margin>