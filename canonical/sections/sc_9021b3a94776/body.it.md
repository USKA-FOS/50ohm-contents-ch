Il transistor bipolare lo avevamo già discusso nei materiali didattici nella sezione [sec:transistor_1]. In questa sezione approfondiremo ulteriormente l'argomento e prenderemo in considerazione anche un altro transistor.

Il transistor bipolare è costituito da tre zone semiconduttrici, drogate alternativamente di tipo N e P. Le zone sono denominate emettitore, base e collettore. Nel *transistor npn*, l'emettitore è drogato di tipo N, la base di tipo P e il collettore di tipo N. Nel transistor pnp, corrispondentemente, si ha un emettitore di tipo P, una base di tipo N e un collettore di tipo P.

La figura [ref:a_bipolartransistor_aus] mostra un transistor npn nello stato spento.
Non appena la tensione base-emettitore $U_\mathrm{BE}$ viene applicata accendendo l'interruttore (tipicamente $\approx \qtyrange{0,6}{0,7}{\volt}$ per il silicio), il diodo base-emettitore diventa conduttivo. Di conseguenza, scorre una piccola corrente di base $I_\mathrm{B}$ (cfr. figura [ref:a_bipolartransistor_ein]).

Questa piccola corrente di base fa sì che dall'emettitore vengano introdotti molti elettroni nella sottile base. Poiché la base è molto stretta, la maggior parte di questi portatori di carica procede ulteriormente verso il collettore. Lì vengono "aspirati" dalla tensione collettore-emettitore applicata $U_\mathrm{CE}$, scorre la corrente di collettore $I_\mathrm{C}$. Essa è maggiore della corrente di base di un fattore $B$, dove $B$ è il cosiddetto guadagno di corrente del transistor. Valori tipici per $B$ sono compresi tra $\num{20}$ e $\num{500}$.

<margin>
[picture:1071:a_bipolartransistor_aus:Transistor bipolare NPN nello stato spento]
[picture:1072:a_bipolartransistor_ein:Transistor bipolare NPN nello stato acceso]
</margin>

[question:AC503]

Si consiglia, ad esempio, di memorizzare il transistor NPN. Per il PNP, tutto è invertito.

[question:AC504]

Fisicamente, la tensione base-emettitore $U_{BE}$ controlla la corrente di collettore $I_C$, e lo fa in modo esponenziale. Per il transistor npn vale ad esempio:

$I_C = I_S \cdot e^{\frac{U_{BE}}{U_T}}$

$I_S$ è la corrente di saturazione, che dipende fortemente dal tipo di costruzione del transistor. Può essere ricavata dal datasheet. $U_T$ è la cosiddetta tensione termica, che a temperatura ambiente è di circa $\qty{26}{\milli\volt}$.

Una differenza rispetto al transistor ad effetto di campo, che verrà considerato in seguito, è che nel transistor bipolare scorre sempre anche una corrente nell'ingresso (la base), la corrente di base $I_B$. Anche essa dipende esponenzialmente da $U_{BE}$, dove $I_S$ è minore di un fattore $B$ rispetto alla corrente del collettore.

$I_B = \frac{I_S}{B} \cdot e^{\frac{U_{BE}}{U_T}}$

Il fattore $B$ è quindi il quoziente tra la corrente del collettore e la corrente di base:

$B = \frac{I_C}{I_B}$

Anche se il transistor bipolare è fisicamente controllato da $U_\mathrm{BE}$, viene definito *controllato in corrente*, perché conduce solo quando scorre una corrente di base.

[question:AC501]

Un transistor è definito "conduttore" in "verso diretto" quando scorre una significativa corrente di collettore. A tal fine, il diodo base-emettitore deve essere sempre polarizzato in direzione diretta, cioè $U_{BE}$ positiva per i transistor npn e negativa per quelli pnp. Il diodo collettore-base, invece, deve essere in interdizione, poiché non devono essere iniettati portatori di carica dal collettore nella base.

[question:AC505]

Di seguito esaminiamo ancora alcuni semplici circuiti a transistor basati sul transistor bipolare.

---

[question:AC515]

Il punto di funzionamento desiderato viene impostato applicando una corrente di base attraverso $R_1$. La corrente di base è inferiore alla corrente del collettore per il dato guadagno di corrente di $\num{298}$. Sulla resistenza cade la differenza tra la tensione di servizio e il potenziale di base. Il potenziale di base è dato come $\qty{0,6}{\volt}$. Quindi calcoliamo:

$R_1 = 298 \cdot \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{0,005}{\ampere}} \approx \qty{680}{\kilo\ohm}$

<indepth>
Tuttavia, questo circuito presenta nella pratica un enorme svantaggio: il guadagno di corrente di un transistor bipolare non è particolarmente ben controllato. Prendiamo come esempio il popolare BC547B. Secondo le specifiche, il suo guadagno di corrente può variare tra $\num{200}$ e $\num{450}$. Pertanto, con questo circuito, la corrente di collettore può facilmente deviare dal progetto di più di un fattore $2$.
</indepth>

Per ottenere una migliore stabilità del punto di funzionamento, il punto di funzionamento del transistor bipolare viene generalmente impostato tramite un partitore di tensione. La cosiddetta corrente di shunt è la corrente che qui scorre attraverso $R_2$. Dovrebbe essere almeno dieci volte superiore alla corrente di base, in modo che la corrente di base non abbia una grande influenza sul punto di funzionamento.

---

[question:AC516]

<indepth>
Anche questo circuito non è molto raccomandabile dal punto di vista pratico. Da un lato, la corrente di collettore dipende esponenzialmente dalla tensione base-emettitore. Le resistenze hanno una tolleranza, a causa della quale il potenziale di base può deviare leggermente dal valore nominale, con un grande impatto sulla corrente di collettore. Inoltre, la tensione di soglia del diodo base-emettitore è piuttosto dipendente dalla temperatura, circa $\qty{-2}{\milli\volt\per\kelvin}$. Pertanto, questo circuito avrà una forte deriva termica della corrente di collettore. A volte ciò può essere desiderabile, ma bisogna tenerlo presente. Conosceremo ancora un circuito che contiene una controreazione che stabilizza il punto di funzionamento.
</indepth>

Anche per questo circuito c'è un esercizio di calcolo:

[question:AC518]

Il partitore di tensione $R_1$ e $R_2$ imposta il potenziale di base che, poiché l'emettitore è a massa, deve essere di circa $\qty{0,6}{\volt}$. Con una corrente di collettore di $\qty{2}{\milli\ampere}$ e un guadagno di corrente di $\num{200}$, la corrente di base è $\qty{2}{\milli\ampere} / 200 = \qty{10}{\micro\ampere}$. La corrente attraverso $R_2$ dovrebbe essere dieci volte la corrente di base, attraverso $R_1$ scorre $11 \cdot \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$. La resistenza $R_1$ è quindi:

$R_1 = \frac{\qty{10}{\volt} - \qty{0,6}{\volt}}{\qty{110}{\micro\ampere}} = \qty{85,5}{\kilo\ohm}$

Il circuito successivo mostra una tipica impostazione del punto di lavoro per il transistor bipolare, come viene utilizzata anche nella pratica.

---

[question:AC517]

<indepth>
Questo è un buon circuito, che viene anche frequentemente utilizzato nella pratica, perché la corrente di collettore è determinata principalmente dalla resistenza di emettitore $R_E$, che rappresenta una controreazione in serie:

Se la corrente di collettore $I_C$ aumenta, aumenta anche la corrente di emettitore $I_E$. Di conseguenza, ai capi della resistenza di emettitore $R_E$ cade una tensione maggiore. L'emettitore diventa quindi più positivo. Poiché la tensione di base rimane quasi costante grazie al partitore di tensione formato da $R_1$ e $R_2$, la tensione base-emettitore $ U_{BE} = U_B - U_E $ diminuisce.

Una tensione base-emettitore più piccola significa che il transistor conduce meno. Di conseguenza, l'aumento iniziale della corrente viene ridotto.

Il circuito contrasta automaticamente le variazioni di corrente. Per questo si parla di controreazione. Se la corrente aumenta, il transistor viene leggermente "chiuso". Se la corrente diminuisce, il transistor conduce di nuovo più fortemente. In questo modo si stabilizza il punto di funzionamento del circuito.
</indepth>

Il potenziale di base è fissato dal partitore di tensione $R_1$ e $R_2$. Poiché attraverso la resistenza di emettitore $R_E$ deve diminuire $\qty{1}{\volt}$, il potenziale di base deve essere $\qty{1,6}{\volt}$. Con una corrente di collettore di $\qty{2}{\milli\ampere}$ e un guadagno di corrente di $\num{200}$, la corrente di base è $\qty{10}{\micro\ampere}$. Poiché la corrente attraverso $R_2$ deve essere dieci volte la corrente di base, attraverso $R_1$ scorre undici volte la corrente di base, cioè $\qty{110}{\micro\ampere}$. Attraverso $R_1$ diminuisce la differenza tra la tensione di servizio ($\qty{10}{\volt}$) e il potenziale di base, quindi $\qty{8,4}{\volt}$. Ora possiamo determinare $R_1$:

$R_1 = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} = \qty{76,4}{\kilo\ohm}$

[question:AC519]

Se $R_1$ non è attraversato da corrente a causa del guasto, allora non diminuisce alcuna tensione su $R_2$ - la base è al potenziale di massa. Quindi $U_{BE} \geq \qty{0,6}{\volt}$ non è soddisfatta e il transistor è senza corrente. Poiché non diminuisce alcuna tensione sulla resistenza di collettore $R_C$, il potenziale del collettore sale alla tensione di servizio.

[question:AC520]

In questo caso di guasto presentato, $R_2$ non è percorso da corrente. La base è collegata alla tensione di servizio tramite $R_1$. Attraverso questo percorso viene iniettata una corrente di base. Con la consueta progettazione (la corrente di shunt è dieci volte la corrente di base regolare), la corrente di base è 11 volte superiore alla corrente di base regolare - la corrente di collettore aumenterà notevolmente, la caduta di tensione su $R_C$ aumenta fortemente, la tensione collettore-emettitore scende al valore di saturazione di circa $\qty{0,1}{\volt}$. La corrente di collettore è limitata solo da $R_C$.

---

Nel prossimo esercizio si tratta di un relè che viene commutato tramite il transistor npn rappresentato in serie (cfr. figura [ref:a_relais_schaltung]). Supponiamo che inizialmente il transistor sia in conduzione, scorre una corrente attraverso la bobina del relè, il relè è eccitato.

<margin>
[picture:426:a_relais_schaltung:Circuito a relè con transistor npn e diodo di ricircolo]
</margin>

Ora il transistor si spegne, il flusso di corrente crolla. Tuttavia, la forte variazione della corrente induce brevemente nella bobina del relè un'alta tensione negativa, che può portare alla distruzione del transistor.

Per evitare ciò, colleghiamo un diodo di ricircolo *in parallelo*. È collegato in modo che durante il funzionamento normale (transistor in conduzione) non conduca corrente - deve quindi essere installato in polarizzazione inversa. La tensione negativa che si manifesta brevemente durante il crollo della corrente polarizza il diodo in conduzione, la tensione risultante è limitata (per i diodi al silicio) a $\qty{-0,7}{\volt} \ldots \qty{-0,8}{\volt}$.

[question:AC524]

---

I transistor ad effetto di campo hanno un principio di controllo completamente diverso rispetto ai transistor bipolari. Mentre nei transistor bipolari devono essere considerati sia gli elettroni che le lacune (da qui "bipolare"), nel transistor ad effetto di campo è coinvolto solo un tipo di portatore di carica ("unipolare"). Questi possono essere elettroni (*transistor ad effetto di campo a canale n*) o lacune (*transistor ad effetto di campo a canale p*).

Gli elettrodi del FET, che sono rappresentati nella figura [ref:a_fet_schnitt_aus], sono denominati come segue:

* *Source*: questa è la "fonte" (in inglese source) per i portatori di carica nel canale. Non confondersi: il cosiddetto verso convenzionale della corrente è definito in direzione opposta al flusso dei portatori di carica!
* *Drain*: questo è lo scarico (in inglese drain) per i portatori di carica nel canale.
* *Gate*: Il gate (in inglese per cancello) controlla il flusso dei portatori di carica nel canale.

[question:AC512]

Comune a tutti i transistor ad effetto di campo (o *FET*) è che, in condizioni normali di funzionamento, non scorre corrente nell'ingresso, l'elettrodo di gate. Il controllo della carica nel canale (l'area tra *Source* e *Drain*) dipende esclusivamente dalla tensione gate-source.

<margin>
[picture:1073:a_fet_schnitt_aus:FET in sezione trasversale, non conduttivo]
[picture:1074:a_fet_schnitt_ein:FET in sezione trasversale, conduttivo]
</margin>

Le figure [ref:a_fet_schnitt_aus] e [ref:a_fet_schnitt_ein] mostrano la sezione trasversale di un MOSFET a canale N nello stato di interdizione e in quello di conduzione. Nell'immagine superiore non è applicata una sufficiente tensione gate-source $U_{GS}$. Tra le regioni drogate di tipo N di source e drain si trova il substrato drogato di tipo P, quindi non è presente un canale conduttivo. Il transistor è in interdizione e tra source e drain non può fluire corrente.

Se al gate viene applicata una tensione positiva rispetto al source (cfr. figura [ref:a_fet_schnitt_ein]), attraverso lo strato isolante di SiO$_2$ si genera un campo elettrico. Questo campo attrae elettroni verso la superficie del substrato drogato di tipo P direttamente sotto il gate. In questo modo si forma lì un canale conduttivo di tipo N, che collega source e drain. Il MOSFET diventa conduttivo e può fluire una corrente tra drain e source.

È importante notare che il gate è elettricamente isolato dallo strato di ossido. In condizioni ideali, quindi, non scorre corrente di gate; il MOSFET non è controllato da una corrente di controllo, ma dal campo elettrico al gate. Per questo motivo è anche definito come un componente *controllato in tensione*.

[question:AC502]

[question:AC513]

[question:AC514]

Come avevamo già stabilito, il FET è un componente *controllato in tensione*, in cui non scorre corrente di gate. La risposta desiderata è che la tensione gate-source controlla la *resistenza del canale*. Tuttavia, il comportamento del canale può essere descritto come una resistenza solo per tensioni drain-source molto piccole, quindi la risposta è formulata in modo un po' infelice. Sarebbe meglio dire: la tensione gate-source controlla la corrente del canale.

---

La linea verticale simboleggia il canale, che viene contattato in alto (Drain) e in basso (Source). A sinistra si vede il gate - la freccia insieme al tratto verticale ricorda un diodo. Si tratta quindi di un FET, più precisamente di un JFET. La figura [ref:a_fet_overview] mostra una panoramica dei diversi tipi di FET con i loro simboli schematici.

<margin>
[picture:1075:a_fet_overview:Panoramica dei FET con simboli]
</margin>

[question:AC506]

Le seguenti domande riguardano l'associazione di specifici tipi di FET ai loro simboli elettrici. Ecco alcune regole di base:

* La corrente nel canale può essere trasportata da elettroni o da lacune. Nel primo caso parliamo di *FET a canale n*, nel secondo caso di *FET a canale p*.
* Possiamo anche distinguere i FET in base al fatto che per una tensione gate-source $U_{GS}=0$ scorra o meno una corrente nel canale. Si chiamano quindi rispettivamente *a canale intrinseco* (o a svuotamento) o *a canale indotto* (o ad arricchimento).
* Infine, possiamo distinguere i FET in base al fatto che l'elettrodo di gate sia un diodo o una struttura a condensatore. Se il gate è un diodo, parliamo di JFET. Esempi sono il JFET (junction field effect transistor) e il MESFET (metal semiconductor field effect transistor). Nel MESFET il diodo di gate è un diodo Schottky. In un *FET a gate isolato* l'elettrodo di gate è separato dal canale da un isolante (un materiale dielettrico/isolante). La tensione applicata controlla la densità dei portatori di carica nel canale. Se l'isolante è un ossido, ad esempio biossido di silicio, parliamo anche di MOSFET (metal oxide semiconductor FET). A causa del loro utilizzo nei circuiti digitali, i MOSFET sono di gran lunga i tipi di transistor più comuni.

La freccia indica se si tratta di un FET a canale n o p. Come nel diodo, la freccia punta verso il catodo, cioè la regione drogata n. Quindi, se la freccia punta verso il canale, si tratta di un FET a canale n. Nel JFET, il gate porta il canale, mentre nel FET a gate isolato la freccia è visibile tra il canale e il cosiddetto strato di bulk, che si trova sotto il canale ed è solitamente collegato internamente all'elettrodo di source.

Nel FET a gate isolato, il gate e il canale formano graficamente anche un condensatore.

Nel FET a canale intrinseco la linea tra source e drain è continua, mentre nel FET a canale ad arricchimento è interrotta.

[question:AC507]
[question:AC508]
[question:AC509]
[question:AC510]
[question:AC511]

Nel seguito esamineremo anche alcuni circuiti MOSFET che si basano sulle domande precedenti.

[question:AC521]

Nel terminale di gate di un MOSFET non scorre corrente continua. Pertanto, si tratta di un *partitore di tensione* non caricato e vale:

$U_{GS} = \frac{R_2}{R_1 + R_2} \cdot U_B = \frac{\qty{1}{\kilo\ohm}}{\qty{11}{\kilo\ohm}} \cdot \qty{44}{\volt} = \qty{4}{\volt}$

[question:AC522]

Anche qui si tratta di un partitore di tensione non caricato. Poiché le tensioni sono date, il modo più semplice per procedere è:

$\frac{R_2}{R_1} = \frac{\qty{2,8}{\volt}}{\qty{44}{\volt} - \qty{2,8}{\volt}} \rightarrow R_2 = 0,068 \cdot \qty{10}{\kilo\ohm} = \qty{680}{\ohm}$

[question:AC523]

Il MOSFET di potenza è qui completamente in conduzione, il canale può essere rappresentato come una resistenza ohmica di (secondo la specifica del problema) $R_\mathrm{DSon} = \qty{4}{\milli\ohm}$. Scorre una corrente di $\qty{25}{\ampere}$. Calcoliamo la potenza dissipata semplicemente con la nota formula della potenza:

$P_V = I^2 \cdot R_{\mathrm{DSon}} = \qty{2,5}{\watt}$
