Abbiamo già discusso del transistor bipolare nei materiali didattici per la classe E. Nella classe A approfondiremo ulteriormente l'argomento e prenderemo in considerazione anche un altro transistor.

Il transistor bipolare è costituito da tre zone di semiconduttore, che sono dopate alternativamente n e p. Le zone sono denominate emettitore, base e collettore. Nel *transistor npn*, l'emettitore è drogato n, la base p e il collettore n. Nel transistor pnp, rispettivamente, è un emettitore p, una base n e un collettore p.

La figura [ref:a_bipolartransistor_aus] mostra un transistor npn nello stato spento.
Non appena la tensione base-emettitore $U_\mathrm{BE}$ viene applicata tramite l'accensione dell'interruttore (tipicamente $\approx \qtyrange{0,6}{0,7}{\volt}$ per il silicio), il diodo base-emettitore diventa conduttivo. Di conseguenza, scorre una piccola corrente di base $I_\mathrm{B}$ (cfr. figura [ref:a_bipolartransistor_ein]).

Questa piccola corrente di base fa sì che molti elettroni vengano immessi dall'emettitore nella sottile base. Poiché la base è molto stretta, la maggior parte di questi portatori di carica raggiunge il collettore. Lì vengono "aspirati" dalla tensione collettore-emettitore $U_\mathrm{CE}$ applicata, scorre la corrente di collettore $I_\mathrm{C}$. È maggiore della corrente di base del fattore $B$, dove $B$ è il cosiddetto guadagno di corrente del transistor. Valori tipici per $B$ sono nell'intervallo da $\num{20}$ a $\num{500}$.

<margin>
[picture:1071:a_bipolartransistor_aus:Transistor bipolare NPN nello stato spento]
[picture:1072:a_bipolartransistor_ein:Transistor bipolare NPN nello stato acceso]
</margin>

[question:AC503]

Si consiglia, ad esempio, di memorizzare il transistor NPN. Per il PNP, tutto è invertito.

[question:AC504]

Fisicamente, la tensione base-emettitore $U_{BE}$ controlla la corrente di collettore $I_C$ in modo esponenziale. Per il transistor npn, ad esempio, vale:

$I_C = I_S \cdot e^{\frac{U_{BE}}{U_T}}$

$I_S$ è la corrente di saturazione, che dipende fortemente dal tipo di transistor. Si trova nel datasheet. $U_T$ è la cosiddetta tensione termica, che a temperatura ambiente è di circa $\qty{26}{\milli\volt}$.

Una differenza rispetto al transistor a effetto di campo considerato successivamente è che nel transistor bipolare scorre sempre anche una corrente nell'ingresso (la base), la corrente di base $I_B$. Anche questa dipende esponenzialmente da $U_{BE}$, dove $I_S$ è inferiore di un fattore $B$ rispetto alla corrente di collettore.

$I_B = \frac{I_S}{B} \cdot e^{\frac{U_{BE}}{U_T}}$

Il fattore $B$ è quindi il quoziente tra corrente di collettore e corrente di base:

$B = \frac{I_C}{I_B}$

Anche se il transistor bipolare è fisicamente controllato da $U_\mathrm{BE}$, viene definito *comandato in corrente* perché conduce solo quando scorre una corrente di base.

[question:AC501]

Un transistor è definito "conduttivo" in "direzione di passaggio" quando scorre una corrente di collettore significativa. Per questo, la giunzione base-emettitore deve essere sempre polarizzata in avanti, quindi $U_{BE}$ positiva per i transistor npn e negativa per i transistor pnp. La giunzione collettore-base, invece, deve essere bloccata, poiché non devono essere iniettati portatori di carica dal collettore alla base.

[question:AC505]

Di seguito esamineremo alcuni semplici circuiti per transistor basati sul transistor bipolare.

---

[question:AC515]

Il punto di funzionamento desiderato viene impostato immettendo una corrente di base attraverso $R_1$. La corrente di base è inferiore di un fattore pari al guadagno di corrente dato di $\num{298}$ rispetto alla corrente di collettore. La differenza tra la tensione di servizio e il potenziale di base cade attraverso la resistenza. Il potenziale di base è dato come $\qty{0,6}{\volt}$. Quindi calcoliamo:

$R_1 = 298 \cdot \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{0,005}{\ampere}} \approx \qty{680}{\kilo\ohm}$

<indepth>
Il circuito ha però un enorme svantaggio pratico: il guadagno di corrente di un transistor bipolare non è particolarmente ben controllato. Prendiamo come esempio il popolare BC547B. Il suo guadagno di corrente può variare tra $\num{200}$ e $\num{450}$ secondo le specifiche. Con questo circuito, la corrente di collettore può quindi deviare dal progetto di oltre un fattore 2.
</indepth>

Per ottenere una migliore stabilità del punto di funzionamento, il punto di funzionamento del transistor bipolare viene solitamente impostato tramite un partitore di tensione. La cosiddetta corrente trasversale è la corrente che scorre attraverso $R_2$. Dovrebbe essere almeno dieci volte superiore alla corrente di base, in modo che la corrente di base non abbia una grande influenza sul punto di funzionamento.

---

[question:AC516]

<indepth>
Anche questo circuito non è molto consigliabile dal punto di vista pratico. Da un lato, la corrente di collettore dipende esponenzialmente dalla tensione base-emettitore. Le resistenze hanno una tolleranza che può causare una leggera deviazione del potenziale di base dal valore nominale, con un grande impatto sulla corrente di collettore. Inoltre, la tensione di soglia della giunzione base-emettitore è piuttosto sensibile alla temperatura, con circa $\qty{-2}{\milli\volt\per\kelvin}$. Pertanto, questo circuito avrà una forte deriva della corrente di collettore con la temperatura. A volte questo può essere desiderabile, ma bisogna tenerne conto. Impareremo un circuito che include una retroazione negativa che stabilizza il punto di funzionamento.
</indepth>

Anche per questo circuito esiste un problema di calcolo:

[question:AC518]

Il partitore di tensione $R_1$ e $R_2$ imposta il potenziale di base, che, poiché l'emettitore è a massa, deve essere di circa $\qty{0,6}{\volt}$. Con una corrente di collettore di $\qty{2}{\milli\ampere}$ e un guadagno di corrente di $\num{200}$, la corrente di base è $\qty{2}{\milli\ampere} / 200 = \qty{10}{\micro\ampere}$. La corrente attraverso $R_2$ dovrebbe essere dieci volte la corrente di base, quindi attraverso $R_1$ scorre $11 \cdot \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$. La resistenza $R_1$ è quindi:

$R_1 = \frac{\qty{10}{\volt} - \qty{0,6}{\volt}}{\qty{110}{\micro\ampere}} = \qty{85,5}{\kilo\ohm}$

Il circuito successivo mostra un'impostazione tipica del punto di funzionamento per il transistor bipolare, come viene utilizzata anche nella pratica.

---

[question:AC517]

<indepth>
Questo è un buon circuito, che viene utilizzato frequentemente anche nella pratica, poiché la corrente di collettore è determinata principalmente dalla resistenza di emettitore $R_E$, che rappresenta una retroazione negativa in serie:

Se la corrente di collettore $I_C$ aumenta, aumenta anche la corrente di emettitore $I_E$. Di conseguenza, la tensione ai capi della resistenza di emettitore $R_E$ aumenta. L'emettitore diventa quindi più positivo. Poiché la tensione di base rimane quasi costante a causa del partitore di tensione formato da $R_1$ e $R_2$, la tensione base-emettitore $ U_{BE} = U_B - U_E $ diminuisce.

Una tensione base-emettitore inferiore significa che il transistor diventa meno conduttivo. La corrente originariamente aumentata viene quindi ridotta nuovamente.

Il circuito contrasta quindi automaticamente le variazioni di corrente. Per questo motivo si parla di retroazione negativa. Se la corrente aumenta, il transistor viene leggermente "chiuso". Se la corrente diminuisce, il transistor diventa nuovamente più conduttivo. In questo modo, il punto di funzionamento del circuito si stabilizza.
</indepth>

Il potenziale di base è impostato tramite il partitore di tensione $R_1$ e $R_2$. Poiché sulla resistenza di emettitore $R_E$ deve cadere $\qty{1}{\volt}$, il potenziale di base deve essere $\qty{1,6}{\volt}$. Con una corrente di collettore di $\qty{2}{\milli\ampere}$ e un guadagno di corrente di $\num{200}$, la corrente di base è $\qty{10}{\micro\ampere}$. Poiché la corrente attraverso $R_2$ deve essere dieci volte la corrente di base, attraverso $R_1$ scorre undici volte la corrente di base, ovvero $\qty{110}{\micro\ampere}$. La caduta di tensione su $R_1$ è la differenza tra la tensione di servizio ($\qty{10}{\volt}$) e il potenziale di base, ovvero $\qty{8,4}{\volt}$. Ora possiamo determinare $R_1$:

$R_1 = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} = \qty{76,4}{\kilo\ohm}$

[question:AC519]

Se $R_1$ non è attraversata da corrente a causa del guasto, non cade alcuna tensione su $R_2$ - la base è a potenziale di massa. Allora $U_{BE} \geq \qty{0,6}{\volt}$ non è soddisfatta e il transistor è senza corrente. Poiché non cade alcuna tensione sulla resistenza di collettore $R_C$, il potenziale di collettore sale alla tensione di servizio.

[question:AC520]

Nel caso di guasto qui presentato, $R_2$ è senza corrente. La base è collegata alla tensione di servizio tramite $R_1$. Tramite questo percorso viene immessa una corrente di base. Con il dimensionamento usuale (la corrente trasversale è dieci volte la corrente di base normale), la corrente di base è 11 volte superiore alla corrente di base normale - la corrente di collettore aumenterà notevolmente, la caduta di tensione su $R_C$ aumenterà notevolmente, la tensione collettore-emettitore scenderà al valore di saturazione di circa $\qty{0,1}{\volt}$. La corrente di collettore è limitata solo da $R_C$.

---

Nel prossimo esercizio si tratta di un relè, che viene commutato tramite il transistor npn mostrato in serie (cfr. figura [ref:a_relais_schaltung]). Supponiamo che il transistor sia inizialmente conduttivo, scorra una corrente nella bobina del relè, il relè si sia attivato.

<margin>
[picture:426:a_relais_schaltung:Circuito relè con transistor npn e diodo di ricircolo]
</margin>

Ora il transistor si spegne, il flusso di corrente si interrompe. La forte variazione della corrente induce tuttavia brevemente nella bobina del relè una tensione negativa elevata, che può distruggere il transistor.

Per evitare ciò, colleghiamo una diodo di ricircolo in *parallelo*. È collegata in modo tale che nel funzionamento normale (transistor conduttivo) non scorra corrente in essa - deve quindi essere installata in direzione bloccata. La tensione negativa che si presenta brevemente al collasso della corrente, commuta la diodo in direzione passante, la tensione risultante viene (con diodi al silicio) limitata a $\qty{-0,7}{\volt} \ldots \qty{-0,8}{\volt}$.

[question:AC524]

---

I transistor a effetto di campo hanno un principio di controllo completamente diverso rispetto ai transistor bipolari. Mentre nei transistor bipolari devono essere considerati sia gli elettroni che i difetti di elettroni ("lacune") (da qui "bipolare"), nei transistor a effetto di campo è coinvolta solo una specie di portatori di carica ("unipolare"). Questi possono essere elettroni (transistor a effetto di campo a *canale n*) o lacune (transistor a effetto di campo a *canale p*).

Gli elettrodi del FET, mostrati nella figura [ref:a_fet_schnitt_aus], sono denominati come segue:

* *Source*: questa è la "sorgente" (ingl. source) per i portatori di carica nel canale. Non lasciarsi confondere: la cosiddetta direzione tecnica della corrente è definita in senso opposto alla direzione del flusso dei portatori di carica!
* *Drain*: questo è lo scarico (ingl. drain) per i portatori di carica nel canale.
* *Gate*: Il Gate (inglese per cancello) controlla il flusso dei portatori di carica nel canale.

[question:AC512]

A tutti i transistor a effetto di campo (o *FET*) è comune che nel funzionamento normale non scorra corrente nell'ingresso, l'elettrodo di Gate. Il controllo della carica nel canale (l'area tra *Source* e *Drain*) dipende esclusivamente dalla tensione Gate-Source.

<margin>
[picture:1073:a_fet_schnitt_aus:FET in sezione trasversale, non conduttivo]
[picture:1074:a_fet_schnitt_ein:FET in sezione trasversale, conduttivo]
</margin>

Le figure [ref:a_fet_schnitt_aus] e [ref:a_fet_schnitt_ein] mostrano la sezione trasversale di un MOSFET a canale n nello stato bloccato e conduttivo. Nell'immagine superiore non è applicata una tensione Gate-Source $U_{GS}$ sufficiente. Tra le aree drogate n di Source e Drain si trova il substrato drogato p, in modo che non sia presente un canale conduttivo. Il transistor è bloccato e nessun corrente può fluire tra Source e Drain.

Se si applica una tensione positiva al Gate rispetto a Source (cfr. figura [ref:a_fet_schnitt_ein]), si crea un campo elettrico attraverso lo strato isolante SiO$_2$. Questo campo attira elettroni alla superficie del substrato drogato p direttamente sotto il Gate. In questo modo si forma lì un canale conduttivo n, che collega Source e Drain. Il MOSFET diventa conduttivo e può fluire una corrente tra Drain e Source.

È importante che il Gate sia elettricamente isolato dallo strato di ossido. Idealmente, quindi, nessuna corrente di Gate scorre; il MOSFET non è controllato da una corrente di pilotaggio, ma dal campo elettrico sul Gate. Per questo motivo è anche definito un componente a *controllo di tensione*.

[question:AC502]

[question:AC513]

[question:AC514]

Come avevamo già stabilito, il FET è un componente a *controllo di tensione*, in cui non scorre corrente di Gate. La risposta desiderata è che la tensione Gate-Source controlla la *resistenza del canale*. Tuttavia, il comportamento del canale può essere descritto come resistenza solo per tensioni Drain-Source molto piccole, quindi la risposta è formulata in modo un po' infelice. Sarebbe meglio dire: la tensione Gate-Source controlla la corrente di canale.

---

La linea verticale simboleggia il canale, che è contattato in alto (Drain) e in basso (Source). A sinistra si vede il Gate - la freccia ricorda, insieme alla linea verticale, una diodo. Si tratta quindi di un FET, più precisamente di un FET a giunzione. La figura [ref:a_fet_overview] mostra una panoramica dei diversi tipi di FET con i loro simboli di circuito.

<margin>
[picture:1075:a_fet_overview:Panoramica FET con simboli]
</margin>

[question:AC506]

Le seguenti domande riguardano l'associazione di specifici tipi di FET al loro simbolo di circuito. A questo proposito, alcune regole di base:

* La corrente nel canale può essere trasportata da elettroni o da lacune. Nel primo caso parliamo di un *FET a canale n*, nel secondo caso di un *FET a canale p*.
* Possiamo anche distinguere i FET in base al fatto che per una tensione Gate-Source $U_{GS}=0$ scorra o meno una corrente nel canale. In tal caso si chiamano rispettivamente *a conduzione propria* o *a blocco proprio*.
* Infine, possiamo distinguere i FET in base al fatto che l'elettrodo di Gate sia una diodo o una struttura a condensatore. Se il Gate è una diodo, parliamo di un FET a giunzione. Esempi sono il JFET (junction field effect transistor) e il MESFET (metal semiconductor field effect transistor). Nel MESFET la diodo di Gate è una diodo Schottky. In un *FET a strato isolante*, l'elettrodo di Gate è separato dal canale da uno strato isolante (un dielettrico). La tensione applicata controlla la densità dei portatori di carica nel canale. Se l'isolante è un ossido, ad esempio diossido di silicio, parliamo anche di MOSFET (metal oxide semiconductor FET). A causa del loro utilizzo nei circuiti digitali, i MOSFET sono di gran lunga i tipi di transistor più comuni.

La freccia indica se si tratta di un FET a canale n o p. Come per la diodo, la freccia punta verso il catodo, cioè la zona drogata n. Quindi, se la freccia punta verso il canale, si tratta di un FET a canale n. Nel FET a giunzione, il Gate è collegato al canale, mentre nel FET a strato isolante la freccia si trova tra il canale e il cosiddetto strato Bulk, che si trova sotto il canale ed è solitamente collegato internamente all'elettrodo Source.

Nel FET a strato isolante, Gate e canale formano anche graficamente un condensatore.

Nel FET a conduzione propria, la linea attraversa il canale tra Source e Drain, mentre nel FET a blocco proprio è interrotta.

[question:AC507]
[question:AC508]
[question:AC509]
[question:AC510]
[question:AC511]

Di seguito esamineremo anche alcuni circuiti MOSFET che si basano sulle domande precedenti.

[question:AC521]

Nella connessione Gate di un MOSFET non scorre corrente continua. Pertanto, si tratta di un partitore di tensione *non caricato* e vale:

$U_{GS} = \frac{R_2}{R_1 + R_2} \cdot U_B = \frac{\qty{1}{\kilo\ohm}}{\qty{11}{\kilo\ohm}} \cdot \qty{44}{\volt} = \qty{4}{\volt}$

[question:AC522]

Anche qui si tratta di un partitore di tensione non caricato. Poiché le tensioni sono date, procediamo nel modo più semplice:

$\frac{R_2}{R_1} = \frac{\qty{2,8}{\volt}}{\qty{44}{\volt} - \qty{2,8}{\volt}} \rightarrow R_2 = 0,068 \cdot \qty{10}{\kilo\ohm} = \qty{680}{\ohm}$

[question:AC523]

Il MOSFET di potenza è completamente conduttivo qui, il canale può essere rappresentato come una resistenza ohmica di (secondo la specifica) $R_\mathrm{DSon} = \qty{4}{\milli\ohm}$. La corrente che scorre è di $\qty{25}{\ampere}$. Calcoliamo la potenza dissipata semplicemente secondo la nota formula della potenza:

$P_V = I^2 \cdot R_{\mathrm{DSon}} = \qty{2,5}{\watt}$