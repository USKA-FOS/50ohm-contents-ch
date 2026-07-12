<margin>
[picture:1019:e_frequenzabhängiger_widerstand:Dipendenza dalla frequenza di condensatore e bobina rispetto a una resistenza classica]
[picture:1020:e_herleitung_tiefpass:Derivazione del circuito passa-basso partendo da un partitore di tensione]
</margin>

Nei capitoli sui condensatori e sulle bobine abbiamo già appreso che entrambi i componenti hanno una resistenza dipendente dalla frequenza. La figura [ref:e_frequenzabhängiger_widerstand] mostra qualitativamente che la resistenza di una resistenza ohmica è indipendente dalla frequenza, mentre la resistenza di un condensatore diminuisce iperbolicamente all'aumentare della frequenza e la resistenza di una bobina aumenta linearmente all'aumentare della frequenza.

Da questi componenti è possibile costruire i cosiddetti filtri di frequenza passivi, che ora esamineremo più da vicino. Nella prima parte di questo capitolo ci occupiamo di filtri semplici, ovvero passa-alto e passa-basso. Con questi filtri è possibile sopprimere le bande di frequenza indesiderate sopra o sotto una frequenza di taglio. Nella seconda parte, ci occuperemo quindi di filtri più complessi, come ad esempio i filtri passa-banda.

Iniziamo con la derivazione di un filtro passa-basso come cosiddetto *circuito RC*. Il punto di partenza nel passaggio (1) è il circuito di un partitore di tensione, come mostrato nella figura [ref:e_herleitung_tiefpass] e che abbiamo già imparato a conoscere. Ricordiamo che per un partitore di tensione vale quanto segue:

$\frac{U_1}{U_2} = \frac{R_1}{R_2}$

Ciò significa, ad esempio: se la resistenza $R_2$ è il doppio della resistenza $R_1$, allora anche la tensione $U_2$ è il doppio della tensione $U_1$.

Nel passaggio (2) sostituiamo la resistenza $R_2$ con il condensatore $C_1$. Successivamente, ridisegniamo il circuito nel passaggio (3) in modo da ottenere la rappresentazione usuale di un filtro passa-basso.

---

Constatiamo: un filtro passa-basso non è altro che un partitore di tensione. Pertanto, possiamo considerarlo esattamente allo stesso modo in seguito. Nella figura [ref:e_wiederstaende_tiefpass] sono rappresentati nuovamente gli andamenti della resistenza in funzione della frequenza. Consideriamo innanzitutto le basse frequenze: in questo caso la resistenza del condensatore è elevata, cosicché all'uscita è presente una tensione elevata. Se la frequenza aumenta, la resistenza del condensatore diminuisce progressivamente e, secondo il principio del partitore di tensione, anche la tensione d’uscita diminuisce.

In questo modo si ottiene l'andamento della tensione mostrato nella figura [ref:e_tiefpass_frequenzgang]. Viene così spiegata anche l'idea centrale del filtro passa-basso: le alte frequenze vengono attenuate fortemente, mentre le basse frequenze passano attraverso il filtro quasi senza ostacoli. Un esempio di applicazione di un filtro passa-basso è il suo utilizzo dopo amplificatori di trasmissione per filtrare le armoniche superiori generate da distorsioni.

<margin>
[picture:1021:e_wiederstaende_tiefpass:Comportamento qualitativo della resistenza nel partitore di tensione passa-basso]
[picture:1024:e_tiefpass_frequenzgang:Andamento qualitativo della tensione $U_\text{A}$ sul filtro passa-basso]
</margin>

[question:ED208]
[question:ED201]

<indepth>
La *frequenza di taglio* ($f_\text{g}$) di un filtro passa-basso è la frequenza alla quale il segnale di uscita inizia a essere attenuato in modo apprezzabile. Essa segna quindi il passaggio tra la banda di frequenza che viene trasmessa dal filtro quasi senza ostacoli e la banda in cui l'attenuazione aumenta chiaramente. Formalmente, la frequenza di taglio è definita in modo tale che la potenza d’uscita sia diminuita alla metà della potenza d’ingresso ($\qty{-3}{\dB}$). Poiché la potenza è proporzionale al quadrato della tensione, ciò corrisponde a una diminuzione della tensione d’uscita a circa il $\qty{70}{\percent}$ del suo valore originale ($\frac{1}{\sqrt{2}}$). In pratica, la frequenza di taglio viene spesso riconosciuta nel punto in cui la tensione d’uscita diventa notevolmente più piccola e la curva di risposta in frequenza inizia a "piegarsi". Al di sotto della frequenza di taglio, le basse frequenze vengono trasmesse quasi invariate, al di sopra della frequenza di taglio, le frequenze più alte vengono attenuate progressivamente.
</indepth>

---

Al contrario, in un filtro passa-alto, le basse frequenze vengono attenuate fortemente, mentre le alte frequenze passano attraverso questo filtro con poca attenuazione. Ciò si ottiene scambiando condensatore e resistenza come mostrato nella figura [ref:e_wiederstaende_hochpass]. La curva di risposta in frequenza di un filtro passa-alto è mostrata qualitativamente in [ref:e_hochpass_frequenzgang]. Un esempio di applicazione di un filtro passa-alto è il suo utilizzo in un combinatore d'antenna per filtrare, ad esempio, la banda delle onde corte prima di un ricevitore VHF, al fine di evitare disturbi dovuti al funzionamento in onde corte.

<margin>
[picture:1025:e_wiederstaende_hochpass:Comportamento qualitativo della resistenza nel partitore di tensione passa-alto]
[picture:1022:e_hochpass_frequenzgang:Andamento qualitativo della tensione $U_\text{A}$ sul filtro passa-alto]
</margin>

[question:ED211]
[question:ED202]

---

I semplici circuiti RC hanno lo svantaggio che i loro fianchi nel range di taglio sono piuttosto piatti. La minima impedenza di un filtro passa-basso RC è determinata dalla resistenza $R$. Tuttavia, la resistenza $R$ può essere sostituita da una bobina, che si comporta in modo opposto a un condensatore in termini di comportamento in frequenza. È quindi logico combinare bobine e condensatori per creare filtri passa-alto e passa-basso.
Con *alte frequenze, la resistenza della bobina è alta*, mentre la resistenza del condensatore è piccola.
Con *basse frequenze, la resistenza della bobina è bassa*, mentre la resistenza del condensatore è alta.
A seconda di quale componente viene misurata la tensione d’uscita, si ottiene un filtro passa-alto o passa-basso. Se ci si ricorda che la resistenza della bobina $X_\text{L}$ è alta anche ad alta frequenza, è possibile identificare rapidamente un circuito come filtro passa-alto o passa-basso osservando attraverso quale componente viene misurata la tensione d’uscita.

<tip>
Anche nei circuiti con condensatore e bobina vale la seguente semplice regola: se nel ramo superiore del partitore di tensione si trova una *H* maiuscola – come in *H*ochpass (filtro passa-alto), allora si tratta di un filtro passa-alto. Se invece nel ramo superiore si trova una resistenza o una bobina, si tratta di un filtro passa-basso.
[picture:1023:e_hochpass_tipp:Suggerimento per ricordare]
</tip>

[question:ED209]
[question:ED212]

---

Le domande seguenti riguardano un'applicazione pratica dei nostri filtri. Naturalmente, è possibile utilizzare anche più componenti dipendenti dalla frequenza in un circuito, in modo che la transizione nel range della frequenza di taglio diventi più ripida. Dovresti ora essere in grado di riconoscere facilmente quale circuito viene utilizzato nelle due domande seguenti con il suggerimento menzionato.

[question:ED210]
[question:ED213] 

Un altro esempio pratico di concatenazione di bobine e condensatori come filtro è il diplexer spiegato a margine.

<indepth>
*Esempio pratico di diplexer:* I filtri passa-alto e passa-basso passivi vengono utilizzati anche nei divisori di frequenza. Nell'esempio sottostante è visibile un circuito per un cosiddetto diplexer per $\qty{2}{\meter}$ e $\qty{70}{\centi\meter}$. Questo può essere utilizzato, ad esempio, per utilizzare un apparrecchio radio per $\qty{2}{\meter}$ e un apparrecchio radio per $\qty{70}{\centi\meter}$ su un'antenna bi-banda comune. Viceversa, si potrebbero anche utilizzare antenne separate per $\qty{2}{\meter}$ e $\qty{70}{\centi\meter}$ su un apparecchio bi-banda VHF, per utilizzare ad esempio un'antenna omnidirezionale per la comunicazione diretta in $\qty{2}{\meter}$ e un'antenna direttiva per il funzionamento in relais in $\qty{70}{\centi\meter}$.
Prima dell'uscita per $\qty{2}{\meter}$ si vede un filtro passa-basso, prima dell'uscita per $\qty{70}{\centi\meter}$ un filtro passa-alto - ciascuno combinato da 5 componenti dipendenti dalla frequenza.
[picture:939:e_circuit_diplexer:Schema del diplexer $\qty{2}{\meter}$-/$\qty{70}{\centi\meter}$]
[photo:171:e_example_diplexer:Esempio di montaggio]
</indepth>

<indepth>
[photo:320:e_tiefpass_selbstbau:Filtro passa-basso autocostruito]
I filtri sopra menzionati possono naturalmente essere calcolati e costruiti da sé per tutte le bande di frequenza. Nella raccolta di formule si trovano le formule necessarie, anche se naturalmente esistono molti suggerimenti di costruzione e programmi di calcolo. Le bobine necessarie possono spesso essere prodotte facilmente da sé. Per piccoli valori di bobina, una piccola scorta di filo di rame smaltato da $\qty{0,8}{\milli\meter}$ è sufficiente per bobine ad aria stabili. Per grandi valori di bobina, ad esempio per le bande delle onde corte, si può utilizzare filo di rame smaltato da $\qty{0,2}{\milli\meter}$ e materiale del nucleo con i corrispondenti valori $A_\text{L}$, per poter produrre sempre i valori corretti da sé. Le dimensioni necessarie, gli avvolgimenti, ecc. si possono trovare solitamente facilmente tramite la raccolta di formule, i suggerimenti di costruzione o i programmi di calcolo.
</indepth>

---

Abbiamo ora imparato a conoscere semplici circuiti RC e LC come filtri passa-alto e passa-basso. Tuttavia, da condensatori e bobine si possono realizzare altri tipi di filtri che vanno oltre i semplici passa-alto e passa-basso. Questi li esamineremo ora più da vicino nella seconda parte, ovvero i cosiddetti *circuiti oscillanti*.

<margin>
[picture:1026:e_rp_schwingkreis:(a) Circuito oscillante in serie - (b) Circuito oscillante in parallelo]
</margin>

Nei circuiti oscillanti, la bobina e il condensatore vengono disposti – a seconda dell'effetto filtrante desiderato – in modo tale che a una determinata frequenza si verifichi una resistenza particolarmente alta o particolarmente bassa. Ciò attenua o lascia passare selettivamente le frequenze al di sopra o al di sotto di questa frequenza.

La disposizione della bobina e del condensatore può avvenire in serie o in parallelo. Si distingue quindi tra circuiti oscillanti in serie (a) e circuiti oscillanti in parallelo (b), come mostrato nella figura [ref:e_rp_schwingkreis]. 

---

Se si collegano in parallelo bobina e condensatore e si applica, ad esempio, un impulso a onda quadra a questa disposizione, questa entra in oscillazione. Il condensatore carico ha ora immagazzinato energia nel campo elettrico, che tuttavia si dissolve attraverso la bobina. A causa del flusso di corrente attraverso la bobina, si forma un campo magnetico in essa, che inizialmente oppone resistenza al flusso di corrente. Una volta che il campo magnetico si è formato, il condensatore si scarica completamente. L'energia è ora immagazzinata nel campo magnetico della bobina. Poiché tuttavia il condensatore non può scaricarsi ulteriormente e non può mantenere un flusso di corrente, il campo magnetico non può essere mantenuto. Il campo magnetico della bobina si scarica e genera una tensione in direzione opposta. Questa tensione carica ora il condensatore in direzione opposta, finché il campo magnetico nella bobina non si è dissipato e non può più opporre resistenza al campo elettrico nel condensatore. Il processo ricomincia quindi.

<margin>
[include:applet_schwingkreis]
</margin>

---

Per questo motivo si parla di circuito oscillante. La frequenza con cui questo circuito oscillante oscilla è chiamata frequenza di risonanza ($f_0$). È paragonabile alla frequenza di risonanza di una diapason che viene messa in vibrazione da un colpo. In caso di risonanza, le impedenze della bobina $X_\text{L}$ e del condensatore $X_\text{C}$ sono uguali. Tali circuiti oscillanti possono essere utilizzati da un lato per generare oscillazioni, cosa che esamineremo più in dettaglio nel capitolo sugli oscillatori. Dall'altro lato, possono anche essere utilizzati come filtri – e questo è esattamente l'argomento di questo capitolo.

<margin>
[picture:1037:e_rsk_frequenzgang:Risposta in frequenza qualitativa di un circuito oscillante in serie]
</margin>

---

In un *circuito oscillante in serie* o *circuito oscillante in serie* come nella figura [ref:e_rp_schwingkreis]a, l'impedenza totale è minima in caso di risonanza. La figura [ref:e_rsk_frequenzgang] mostra la risposta in frequenza. A frequenze superiori alla frequenza di risonanza, l'impedenza della bobina aumenta, così come l'impedenza totale del circuito oscillante in serie. Lo stesso accade anche a frequenze inferiori alla frequenza di risonanza, anche se qui l'impedenza del condensatore è elevata. Nei circuiti oscillanti in serie, l'impedenza è quindi minima alla frequenza di risonanza. A causa del collegamento in serie, a frequenze diverse dalla frequenza di risonanza, il componente con l'impedenza maggiore determina l'impedenza del circuito oscillante.

<indepth>
La risposta in frequenza in ampiezza di un circuito oscillante in serie composto da una resistenza, una bobina e un condensatore si calcola secondo la seguente formula:
  
$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$
  
In caso di risonanza, quando $X_\text{C}$ = $X_\text{L}$, rimane solo la resistenza $R$. Nel caso ideale, quando la resistenza $R=\qty{0}{\ohm}$, la resistenza è addirittura zero. Inserendo i valori per $X_\text{L}$ e $X_\text{C}$ otteniamo:
  
$Z = \sqrt{R^2+\left(2\pi f \cdot L~-~\frac{1}{2\pi f \cdot C} \right)^2}$
  
Nella formula si può vedere molto bene la risposta in frequenza della figura [ref:e_rsk_frequenzgang]: se si fa tendere la frequenza a $\qty{0}{\hertz}$, la parte della bobina scompare e agisce solo il condensatore. Se invece si fa tendere la frequenza all'infinito, agisce solo la bobina e la parte del condensatore scompare.
  
Si può persino calcolare la frequenza di risonanza. Se vale $X_\text{L} = X_\text{C}$, si può risolvere la formula per $f$:
  
$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$
  
Si ottiene quindi la formula: 
  
$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$
  
La derivazione esatta delle formule può essere letta, ad esempio, su [Wikipedia](https://50ohm.de/schwk). Va menzionato a questo punto che tutte le risposte in frequenza sono registrate qualitativamente e nella realtà potrebbero apparire leggermente diverse.
</indepth>

[question:ED205]

---

Se si collegano condensatore e bobina in un *circuito oscillante in parallelo*, come nella figura [ref:e_rp_schwingkreis]b, accade esattamente il contrario: l'impedenza *$Z$* è molto alta alla frequenza di risonanza, cfr. figura [ref:e_psk_frequenzgang]. A frequenze superiori alla frequenza di risonanza, tuttavia, il condensatore ha una bassa impedenza, quindi l'impedenza di questo circuito oscillante diminuisce. A frequenze inferiori alla frequenza di risonanza, invece, la bobina ha una bassa impedenza, quindi l'impedenza del circuito oscillante diminuisce anche a frequenze più basse. 
Nei circuiti oscillanti in parallelo, l'impedenza è quindi massima alla frequenza di risonanza. A frequenze diverse dalla frequenza di risonanza, il componente con l'impedenza inferiore determina l'impedenza del circuito oscillante in parallelo. 

<margin>
[picture:1036:e_psk_frequenzgang:Risposta in frequenza qualitativa di un circuito oscillante in parallelo]
</margin>

[question:ED206] 
[question:ED207]

% TODO ////

A seconda di come i circuiti oscillanti paralleli e in serie vengono utilizzati nel percorso del segnale, è ora possibile attenuare o filtrare determinate bande di frequenza. A tal fine, vogliamo utilizzare nuovamente il nostro approccio con il partitore di tensione.

---

Iniziamo innanzitutto con i circuiti per i *filtri passa-banda*. Esistono due modi per realizzarli come partitore di tensione: primo, il *circuito trappola* (cfr. figura [ref:e_saugkreis]) e secondo, il *filtro passa-banda* (cfr. figura [ref:e_sperrkreis]). Nelle figure sono rappresentati rispettivamente la resistenza dipendente dalla frequenza e la tensione d’uscita. Utilizzando le nostre note regole per il partitore di tensione, queste relazioni possono essere derivate e comprese in modo del tutto analogo ai circuiti RC trattati in precedenza. Poiché i circuiti oscillanti paralleli hanno un'elevata resistenza in risonanza, possono essere utilizzati efficacemente come circuiti trappola in serie nel percorso del segnale. Oppure si utilizza la bassa resistenza di risonanza di un circuito oscillante in serie in parallelo al percorso del segnale come circuito di aspirazione. Spesso, tuttavia, entrambi vengono utilizzati in combinazione. Un'applicazione per i filtri passa-banda è, ad esempio, la soppressione di singole bande di frequenza, ad esempio quando una stazione radio FM vicina disturba la ricezione.

[question:ED204]
[question:ED214] 
[question:ED215]

<margin>
[picture:1038:e_saugkreis:Andamenti qualitativi della frequenza di un circuito trappola]
[picture:1040:e_sperrkreis:Andamenti qualitativi della frequenza di un filtro passa-banda]
</margin>

---

La seconda categoria di circuiti che si possono sviluppare dai circuiti oscillanti sono i *filtri passa-banda*. Anche qui ci sono due modi per realizzarli come partitore di tensione: primo, il *circuito di conduzione* (cfr. figura [ref:e_leitkreis]) e secondo, il *filtro passa-banda* (cfr. figura [ref:e_bandpass]). Anche qui la derivazione avviene come al solito attraverso il comportamento di un partitore di tensione. Per un filtro passa-banda, i circuiti oscillanti paralleli vengono posti in parallelo al percorso del segnale, poiché questi hanno una bassa resistenza per frequenze diverse da quella di risonanza e la "cortocircuitano", per così dire. Un circuito oscillante in serie, posto in serie nel percorso del segnale, provoca un'ulteriore attenuazione al di fuori della frequenza di risonanza, mentre ha una bassa resistenza alla frequenza desiderata.

[question:ED203]

<margin>
[picture:1039:e_leitkreis:Andamenti qualitativi della frequenza di un circuito di conduzione]
[picture:1041:e_bandpass:Andamenti qualitativi della frequenza di un filtro passa-banda]
</margin>

Un esempio di applicazione dei filtri passa-banda è il loro utilizzo nei ricevitori, dove è necessaria una pre-filtratura di determinate bande di frequenza. In questo caso, viene utilizzato un filtro che lascia passare solo una banda di frequenza desiderata, mentre tutte le altre frequenze vengono attenuate. Tali filtri passa-banda si trovano quindi in quasi tutti i ricevitori, spesso anche separatamente per ogni singola banda delle onde corte. Progettati per potenze elevate, i filtri passa-banda vengono utilizzati anche in trasmissione, ad esempio durante contest o field day comuni, per minimizzare le interferenze reciproche tra stazioni adiacenti.

Pertanto, sia i circuiti oscillanti in serie che quelli paralleli possono essere utilizzati per costruire filtri passa-banda e filtri passa-banda. È fondamentale considerare come si comportano i rispettivi circuiti oscillanti in caso di risonanza. In base al loro comportamento, possono essere collegati in serie o in parallelo al percorso del segnale, eventualmente anche combinati più volte tra loro.

Nei filtri si possono utilizzare solo determinati tipi di condensatori adatti.
I condensatori elettrolitici, ad esempio, non sono adatti per circuiti ad alta frequenza, poiché la loro capacità dipende fortemente dalla frequenza e, inoltre, hanno un'elevata resistenza interna ad alte frequenze. I condensatori a film, invece, non sono adatti perché, a causa dei loro avvolgimenti (induttanza parassita), la loro capacità dipende fortemente dalla frequenza, specialmente a partire dalla gamma delle onde corte, e hanno un basso fattore di qualità.
I condensatori ceramici, al contrario, hanno basse perdite e la capacità dipende poco dalla frequenza e dalla temperatura. Inoltre, sono facilmente reperibili anche per alte tensioni.
Sono adatti anche i condensatori con piastre e aria come isolante, che si trovano più comunemente come condensatori variabili. Per alte tensioni, i condensatori variabili vengono utilizzati anche negli accordatori d’antenna.

[question:ED216]