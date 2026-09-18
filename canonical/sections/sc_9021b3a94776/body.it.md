Il transistor bipolare era già stato discusso nei materiali di formazione per la classe E. Nella classe A approfondiremo ulteriormente l'argomento e considereremo anche un altro transistor.Il transistor bipolare è costituito da tre zone semiconduttrici alternate, drogate di tipo N e P. Queste zone sono chiamate emettitore, base e collettore. Nel transistor *NPN* l'emettitore è drogato di tipo N, la base di tipo P e il collettore di tipo N. Nel transistor PNP, invece, abbiamo un emettitore di tipo P, una base di tipo N e un collettore di tipo P.La figura [ref:a_bipolartransistor_aus] mostra un transistor NPN nello stato di interdizione. Non appena viene applicata la tensione base-emettitore $U_\mathrm{BE}$ tramite l'interruttore (tipicamente $\approx \qtyrange{0,6}{0,7}{\volt}$ per il silicio), il diodo base-emettitore diventa conduttivo. Di conseguenza scorre una piccola corrente di base $I_\mathrm{B}$ (cfr. figura [ref:a_bipolartransistor_ein]).Questa piccola corrente di base fa sì che molti elettroni vengano iniettati dall'emettitore nella sottile base. Poiché la base è molto stretta, la maggior parte di queste cariche elettriche raggiunge il collettore. Qui vengono "aspirate" dalla tensione collettore-emettitore $U_\mathrm{CE}$ applicata, e scorre la corrente di collettore $I_\mathrm{C}$. Essa è maggiore della corrente di base di un fattore $B$, dove $B$ è il cosiddetto guadagno di corrente del transistor. Valori tipici per $B$ vanno da $\num{20}$ a $\num{500}$. <margin>
[picture:1071:a_bipolartransistor_aus:Transistor bipolare NPN nello stato di interdizione]
[picture:1072:a_bipolartransistor_ein:Transistor bipolare NPN nello stato di conduzione]
</margin>
[question:AC503]Può essere utile ricordare il transistor NPN. Per il PNP tutto è invertito.[question:AC504]Dal punto di vista fisico, la tensione base-emettitore $U_{BE}$ controlla la corrente di collettore $I_C$ in modo esponenziale. Ad esempio, per un transistor NPN vale:$I_C = I_S \cdot e^{\frac{U_{BE}}{U_T}}$

$I_S$ è la corrente di saturazione, che dipende fortemente dal tipo di costruzione del [transistor](#). Essa va ricavata dal foglio dati. $U_T$ è la cosiddetta tensione termica, che a [temperatura ambiente](#) è pari a circa $\qty{26}{\milli\volt}$.

Una differenza rispetto al transistor ad effetto di campo, che verrà analizzato in seguito, è che nel [transistor](#) bipolare scorre sempre anche una [corrente](#) all'[ingresso](#) (la [base](#)), la corrente di [base](#) $I_B$. Anche questa dipende esponenzialmente da $U_{BE}$, con la differenza che $I_S$ è minore di un fattore $B$ rispetto alla corrente di collettore.

$I_B = \frac{I_S}{B} \cdot e^{\frac{U_{BE}}{U_T}}$

Il fattore $B$ è quindi il rapporto tra la corrente di [collettore](#) e quella di [base](#):

$B = \frac{I_C}{I_B}$

Sebbene il [transistor](#) bipolare sia controllato fisicamente tramite $U_\mathrm{BE}$, esso viene definito come *controllato in [corrente](#)*, poiché conduce solo quando scorre una corrente di [base](#).

[question:AC501]

Un [transistor](#) viene definito come "in conduzione" in [verso diretto](#) quando scorre una corrente di collettore significativa. A tal fine, il diodo base-emettitore deve sempre essere polarizzato in [verso diretto](#), quindi $U_{BE}$ positivo per i [transistor](#) npn e negativo per quelli pnp. Il diodo collettore-base, invece, deve essere in interdizione, poiché non devono essere iniettati portatori di carica dal collettore verso la [base](#).

[question:AC505]

Nei paragrafi seguenti esamineremo alcune semplici <i>Schaltungen</i> con <i>Transistor</i> basate sul transistor bipolare.---
[question:AC515]
Il <i>Arbeitspunkt</i> desiderato viene impostato facendo fluire una <i>Strom</i> di base attraverso $R_1$. La <i>Strom</i> di base è inferiore alla <i>Strom</i> di collettore di un fattore pari al guadagno di corrente dato, pari a $\num{298}$. Ai capi della <i>resistenza</i> cade la <i>Differenz</i> tra la <i>tensione di servizio</i> e il potenziale di base. Il potenziale di base è dato da $\qty{0,6}{\volt}$. Quindi calcoliamo:
$R_1 = 298 \cdot \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{0,005}{\ampere}} \approx \qty{680}{\kilo\ohm}$
<indepth>
Il <i>circuito</i> presenta tuttavia un grave svantaggio pratico: il guadagno di corrente di un <i>Transistor</i> bipolare non è ben controllato. Prendiamo come esempio il popolare BC547B. Secondo le specifiche, il suo guadagno di corrente può variare tra $\num{200}$ e $\num{450}$. Pertanto, con questo <i>circuito</i>, la <i>Strom</i> di collettore può discostarsi dal valore progettato anche di oltre un fattore 2.
</indepth>
Per ottenere una maggiore stabilità del <i>Arbeitspunkt</i>, il punto di funzionamento del <i>Transistor</i> bipolare viene generalmente impostato tramite un <i>Spannungsteiler</i>. La cosiddetta <i>Strom</i> di polarizzazione è la <i>Strom</i> che fluisce attraverso $R_2$. Essa dovrebbe essere almeno dieci volte superiore alla <i>Strom</i> di base, in modo che quest'ultima non influenzi in modo significativo il <i>Arbeitspunkt</i>.
---
[question:AC516]
<indepth>
Anche questo <i>circuito</i> non è molto consigliabile dal punto di vista pratico. Da un lato, la <i>Strom</i> di collettore dipende esponenzialmente dalla <i>tensione</i> base-emettitore. Le <i>resistenze</i> hanno una <i>Toleranz</i>, per cui il potenziale di base può discostarsi dal valore nominale, con un grande impatto sulla <i>Strom</i> di collettore. Inoltre, la <i>tensione</i> di soglia del diodo base-emettitore è piuttosto dipendente dalla temperatura, con una variazione di circa $\qty{-2}{\milli\volt\per\kelvin}$. Pertanto, questo <i>circuito</i> presenterà una forte dipendenza termica della <i>Strom</i> di collettore. Questo effetto può essere talvolta desiderato, ma deve essere tenuto in considerazione. In seguito impareremo a conoscere un <i>circuito</i> che include una controreazione per stabilizzare il <i>Arbeitspunkt</i>.
</indepth>
Anche per questo circuito esiste un esercizio di calcolo:[question:AC518]Il partitore di tensione formato da $R_1$ e $R_2$ imposta il potenziale di base, che, poiché l'emettitore è a massa, deve essere di circa $\qty{0,6}{\volt}$. Con una corrente di collettore di $\qty{2}{\milli\ampere}$ e un guadagno di corrente di $\num{200}$, la corrente di base è $\qty{2}{\milli\ampere} / 200 = \qty{10}{\micro\ampere}$. La corrente attraverso $R_2$ deve essere dieci volte la corrente di base, mentre attraverso $R_1$ fluisce $11 \cdot \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$. La resistenza $R_1$ è quindi:$R_1 = \frac{\qty{10}{\volt} - \qty{0,6}{\volt}}{\qty{110}{\micro\ampere}} = \qty{85,5}{\kilo\ohm}$Il circuito successivo mostra un tipico punto di lavoro per il transistor bipolare, come viene utilizzato anche nella pratica.---
[question:AC517]<indepth>
Questo è un buon circuito, spesso utilizzato anche nella pratica, perché la corrente di collettore viene determinata principalmente dalla resistenza di emettitore $R_E$, che rappresenta una controreazione in serie:Se la corrente di collettore $I_C$ aumenta, aumenta anche la corrente di emettitore $I_E$. Di conseguenza, ai capi della resistenza di emettitore $R_E$ si ha una caduta di tensione maggiore. L'emettitore diventa quindi più positivo. Poiché la tensione di base è quasi costante grazie al partitore di tensione formato da $R_1$ e $R_2$, la tensione base-emettitore $ U_{BE} = U_B - U_E $ diminuisce.Una tensione base-emettitore minore significa che il transistor diventa meno conduttivo. La corrente inizialmente aumentata viene quindi ridotta.Quindi il circuito reagisce automaticamente alle variazioni della corrente. Per questo motivo si parla di controreazione. Se la corrente aumenta, il transistor viene leggermente "chiuso". Se la corrente diminuisce, il transistor diventa nuovamente più conduttivo. In questo modo si stabilizza il punto di funzionamento del circuito.
</indepth>

Il potenziale della base viene definito tramite il partitore di tensione $R_1$ e $R_2$. Poiché ai capi della resistenza di emettitore $R_E$ deve cadere $\qty{1}{\volt}$, il potenziale della base deve essere di $\qty{1,6}{\volt}$. Con una corrente di collettore di $\qty{2}{\milli\ampere}$ e un guadagno di corrente di $\num{200}$, la corrente di base è di $\qty{10}{\micro\ampere}$. Poiché la corrente che scorre in $R_2$ deve essere dieci volte la corrente di base, in $R_1$ scorre una corrente pari a undici volte la corrente di base, quindi $\qty{110}{\micro\ampere}$. Ai capi di $R_1$ cade la differenza tra la tensione di servizio ($\qty{10}{\volt}$) e il potenziale della base, cioè $\qty{8,4}{\volt}$. Ora possiamo calcolare $R_1$:

$R_1 = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} = \qty{76,4}{\kilo\ohm}$

[question:AC519]

Se $R_1$ non viene attraversato da corrente a causa di un guasto, ai capi di $R_2$ non cade alcuna tensione: la base si trova al potenziale di massa. In questo caso, la condizione $U_{BE} \geq \qty{0,6}{\volt}$ non è soddisfatta e il transistor non conduce corrente. Poiché ai capi della resistenza di collettore $R_C$ non cade alcuna tensione, il potenziale del collettore sale alla tensione di servizio.

[question:AC520]

Nel caso di questo guasto, $R_2$ non è attraversato da corrente. La base è collegata alla tensione di servizio tramite $R_1$. Attraverso questo percorso viene iniettata una corrente di base. Con la consueta dimensione (la corrente di shunt è dieci volte la corrente di base regolare), la corrente di base è undici volte superiore alla corrente di base regolare: la corrente di collettore aumenterà notevolmente, la caduta di tensione ai capi di $R_C$ crescerà in modo significativo e la tensione collettore-emettitore scenderà al valore di saturazione di circa $\qty{0,1}{\volt}$. La corrente di collettore sarà limitata solo da $R_C$.

---

Nel prossimo esercizio si tratta di un relè che viene azionato tramite il transistor npn collegato in serie (cfr. figura [ref:a_relais_schaltung]). Supponiamo che inizialmente il transistor sia in conduzione, quindi scorra una corrente attraverso la bobina del relè e il relè sia stato attivato.

<margin>
[picture:426:a_relais_schaltung:Circuito del relè con transistor npn e diodo di protezione]
</margin>

Ora il transistor si blocca, il flusso di corrente crolla. Tuttavia, la forte variazione della corrente induce brevemente nella bobina del relè una tensione negativa elevata, che può portare alla distruzione del transistor.

Per evitarlo, si collega un diodo di protezione *in parallelo*. Esso è montato in modo da non condurre corrente durante il funzionamento normale (transistor in conduzione) – quindi deve essere installato in polarizzazione inversa. La tensione negativa che si genera brevemente durante la caduta della corrente porta il diodo in conduzione diretta, limitando la tensione risultante (per i diodi al silicio) a valori compresi tra $\qty{-0,7}{\volt}$ e $\qty{-0,8}{\volt}$.

[question:AC524]

---

I transistor a effetto di campo (FET) seguono un principio di controllo completamente diverso rispetto ai transistor bipolari. Mentre nei transistor bipolari si devono considerare sia gli elettroni che le lacune ("buchi") (da cui il termine "bipolare"), nei FET è coinvolta solo un tipo di portatore di carica ("unipolare"). Questi possono essere elettroni (transistor a effetto di campo a canale *n*) o lacune (transistor a effetto di campo a canale *p*).

Gli elettrodi del FET, rappresentati nella figura [ref:a_fet_schnitt_aus], sono denominati come segue:

* *Source*: è la "sorgente" (in inglese *source*) dei portatori di carica nel canale. Da non confondere: la cosiddetta *verso convenzionale della corrente* è definita in direzione opposta al flusso dei portatori di carica!
* *Drain*: è lo "scarico" (in inglese *drain*) dei portatori di carica nel canale.
* *Gate*: il *gate* (in inglese *gate*, cioè "porta") controlla il flusso dei portatori di carica nel canale.

[question:AC512]

Tutti i transistor a effetto di campo (o *FET*) hanno in comune il fatto che, durante il funzionamento normale, non scorre corrente nell'ingresso, cioè nell'elettrodo di *gate*. Il controllo della carica nel canale (la regione tra *source* e *drain*) dipende esclusivamente dalla tensione *gate-source*.

<margin>
[picture:1073:a_fet_schnitt_aus:FET in sezione trasversale, non conduttivo]
[picture:1074:a_fet_schnitt_ein:FET in sezione trasversale, conduttivo]
</margin>

Le immagini [ref:a_fet_schnitt_aus] e [ref:a_fet_schnitt_ein] mostrano la sezione trasversale di un MOSFET a canale N nello stato di interdizione e in quello di conduzione. Nell'immagine superiore non è applicata una tensione gate-source $U_{GS}$ sufficiente. Tra le regioni drogate di tipo N di Source e Drain si trova il substrato drogato di tipo P, per cui non è presente alcun canale conduttivo. Il transistor è interdetto e tra Source e Drain non può fluire alcuna corrente.

Se al Gate viene applicata una tensione positiva rispetto al Source (cfr. immagine [ref:a_fet_schnitt_ein]), attraverso lo strato isolante di SiO$_2$ si genera un campo elettrico. Questo campo attrae elettroni verso la superficie del substrato drogato di tipo P direttamente sotto il Gate. Qui si forma un canale conduttivo di tipo N che collega Source e Drain. Il MOSFET diventa conduttivo e può fluire una corrente tra Drain e Source.

È importante notare che il Gate è elettricamente isolato dallo strato di ossido. In condizioni ideali, quindi, non fluisce alcuna corrente di Gate; il MOSFET non viene comandato da una corrente di controllo, ma dal campo elettrico al Gate. Per questo motivo viene anche definito un componente *comandato in tensione*.

[question:AC502]

[question:AC513]

[question:AC514]

Come già stabilito, il FET è un componente *comandato in tensione* in cui non fluisce alcuna corrente di Gate. La risposta corretta è che la tensione gate-source controlla la *resistenza del canale*. Tuttavia, il comportamento del canale può essere descritto come una resistenza solo per tensioni drain-source molto piccole; pertanto, la formulazione della risposta risulta poco precisa. Meglio sarebbe: la tensione gate-source controlla la corrente di canale.

---

La linea verticale simboleggia il canale, che viene contato in alto (Drain) e in basso (Source). A sinistra è visibile il Gate: la freccia, insieme alla linea verticale, ricorda un diodo. Si tratta quindi di un FET, più precisamente di un JFET. L'immagine [ref:a_fet_overview] mostra una panoramica dei diversi tipi di FET con i loro simboli circuitali.

<margin>
[picture:1075:a_fet_overview:Panoramica dei FET con simboli]
</margin>

[question:AC506]

Nelle domande seguenti si tratta di associare determinati tipi di FET al loro simbolo elettrico. Ecco alcune regole di base:

* La corrente nel canale può essere trasportata da elettroni o da lacune. Nel primo caso parliamo di un *FET a canale n*, nel secondo di un *FET a canale p*.
* Possiamo anche distinguere i FET in base al fatto che, per una tensione gate-source $U_{GS}=0$, ci sia o meno una corrente nel canale. In tal caso si parla di FET *a conduzione spontanea* o *a interdizione spontanea*.
* Infine, possiamo distinguere i FET in base al fatto che l'elettrodo di gate sia una diodo o una struttura a condensatore. Se il gate è un diodo, parliamo di un *JFET* (junction field effect transistor) o di un *MESFET* (metal semiconductor field effect transistor). Nel MESFET il diodo di gate è una diodo Schottky. In un *FET a gate isolato* l'elettrodo di gate è separato dal canale da un isolante (un materiale dielettrico). La tensione applicata controlla la densità di portatori di carica nel canale. Se l'isolante è un ossido, ad esempio il biossido di silicio, parliamo anche di un *MOSFET* (metal oxide semiconductor FET). Grazie al loro impiego nei circuiti digitali, i MOSFET sono di gran lunga i transistor più diffusi.

La freccia indica se si tratta di un FET a canale n o p. Come nel diodo, la freccia punta verso il catodo, cioè la regione drogata n. Se la freccia punta verso il canale, si tratta di un FET a canale n. Nel JFET il canale contiene il gate, mentre nel FET a gate isolato la freccia si trova tra il canale e lo strato detto *bulk*, che si trova sotto il canale ed è solitamente collegato internamente all'elettrodo di source.

Nel FET a gate isolato, gate e canale formano graficamente anche un condensatore.

Nel FET a conduzione spontanea la linea tra source e drain è continua, mentre nel FET a interdizione spontanea è interrotta.

[question:AC507]
[question:AC508]
[question:AC509]
[question:AC510]
[question:AC511]

Nei circuiti seguenti considereremo anche alcune configurazioni con MOSFET, che si basano sulle domande precedenti.

[question:AC521]

Nell'elettrodo di gate di un MOSFET non scorre corrente continua. Pertanto si tratta di un *partitore di tensione* non caricato e vale:

$U_{GS} = \frac{R_2}{R_1 + R_2} \cdot U_B = \frac{\qty{1}{\kilo\ohm}}{\qty{11}{\kilo\ohm}} \cdot \qty{44}{\volt} = \qty{4}{\volt}$

[question:AC522]

Anche in questo caso si tratta di un <em>partitore di tensione</em> non caricato. Poiché le tensioni sono note, possiamo procedere nel modo più semplice:

$\frac{R_2}{R_1} = \frac{\qty{2,8}{\volt}}{\qty{44}{\volt} - \qty{2,8}{\volt}} \rightarrow R_2 = 0,068 \cdot \qty{10}{\kilo\ohm} = \qty{680}{\ohm}$

[question:AC523]

Il MOSFET di potenza è completamente acceso, il canale può essere rappresentato come una <em>resistenza</em> ohmica di (secondo il testo del problema) $R_\mathrm{DSon} = \qty{4}{\milli\ohm}$. Scorre una corrente di $\qty{25}{\ampere}$. La <em>potenza dissipata</em> viene calcolata semplicemente con la nota formula della potenza:

$P_V = I^2 \cdot R_{\mathrm{DSon}} = \qty{2,5}{\watt}$