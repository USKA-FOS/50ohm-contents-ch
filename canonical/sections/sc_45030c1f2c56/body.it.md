<margin>
[picture:1019:e_frequenzabhängiger_widerstand:Dipendenza dalla frequenza di condensatori e bobine rispetto a una resistenza classica]
[picture:1020:e_herleitung_tiefpass:Derivazione del circuito passa-basso partendo da un partitore di tensione]
</margin>

Nei capitoli sui condensatori e sulle bobine abbiamo già appreso che entrambi i componenti hanno una resistenza dipendente dalla frequenza. La figura [ref:e_frequenzabhängiger_widerstand] mostra qualitativamente che la resistenza di una resistenza ohmica è indipendente dalla frequenza, mentre la resistenza di un condensatore diminuisce iperbolicamente all’aumentare della frequenza e la resistenza di una bobina aumenta linearmente all’aumentare della frequenza.Da questi componenti si possono costruire i cosiddetti *filtri di frequenza passivi*, che ora esamineremo più da vicino. Nella prima parte di questo capitolo ci occupiamo di filtri semplici, ovvero di filtri passa-alto e passa-basso. Con questi filtri è possibile sopprimere le bande di frequenza indesiderate al di sopra o al di sotto di una frequenza di taglio. Nella seconda parte ci dedichiamo poi a filtri più complessi, come ad esempio i filtri passa-banda.

Iniziamo con la derivazione di un filtro passa-basso come *circuito RC*. Il punto di partenza, al passo (1), è il circuito di un partitore di tensione, come rappresentato nella figura [ref:e_herleitung_tiefpass], che abbiamo già imparato a conoscere. Ricordiamo che per un partitore di tensione vale la seguente relazione:

$\frac{U_1}{U_2} = \frac{R_1}{R_2}$

Questo significa, ad esempio: se la resistenza $R_2$ è doppia rispetto alla resistenza $R_1$, allora anche la tensione $U_2$ sarà doppia rispetto alla tensione $U_1$.

Al passo (2) sostituiamo la resistenza $R_2$ con il condensatore $C_1$. Successivamente, al passo (3), ridisegniamo il circuito in modo da ottenere la rappresentazione usuale di un filtro passa-basso.

---

Riassumendo: un filtro passa-basso non è altro che un partitore di tensione. Pertanto, possiamo analizzarlo allo stesso modo. Nella figura [ref:e_wiederstaende_tiefpass] sono mostrati gli andamenti delle resistenze in funzione della frequenza. Consideriamo inizialmente le basse frequenze: in questo caso la resistenza del condensatore è elevata, quindi all’uscita si ha una tensione elevata. All’aumentare della frequenza, la resistenza del condensatore diminuisce progressivamente e, secondo il principio del partitore di tensione, anche la tensione d’uscita si riduce.

In questo modo si ottiene l’andamento della tensione mostrato nella figura [ref:e_tiefpass_frequenzgang]. Questo spiega anche l’idea fondamentale del filtro passa-basso: le alte frequenze vengono fortemente attenuate, mentre le basse frequenze attraversano il filtro quasi senza attenuazione. Un esempio di applicazione di un filtro passa-basso è l’utilizzo dopo gli amplificatori di trasmissione per filtrare le armoniche che si generano a causa delle distorsioni.

<margin>
[picture:1021:e_wiederstaende_tiefpass:Comportamento qualitativo delle resistenze nel partitore di tensione del filtro passa-basso]
[picture:1024:e_tiefpass_frequenzgang:Andamento qualitativo della tensione d’uscita $U_\text{A}$ nel filtro passa-basso]
</margin>

[question:ED208]
[question:ED201]

<indepth>
La *frequenza di taglio* ($f_\text{g}$) di un *filtro passa-basso* è la frequenza alla quale il *segnale di uscita* inizia a essere attenuato in modo significativo. Essa segna quindi il confine tra la banda di frequenza che il filtro lascia passare quasi senza attenuazione e quella in cui l’*attenuazione* aumenta in modo marcato. Formalmente, la frequenza di taglio è definita come il punto in cui la *potenza d’uscita* scende alla metà della *potenza d’ingresso* ($\qty{-3}{\dB}$). Poiché la potenza è proporzionale al quadrato della *tensione*, ciò corrisponde a una diminuzione della *tensione d’uscita* a circa $\qty{70}{\percent}$ del suo valore originale ($\frac{1}{\sqrt{2}}$). In pratica, la frequenza di taglio viene spesso identificata nel punto in cui la *tensione d’uscita* diminuisce sensibilmente e la *risposta in frequenza* inizia a "piegarsi". Al di sotto della frequenza di taglio, le frequenze basse vengono trasmesse quasi invariati, mentre al di sopra di essa le frequenze più alte vengono attenuate progressivamente.
</indepth>
---
In un *filtro passa-alto*, invece, le frequenze basse vengono fortemente attenuate, mentre quelle alte passano attraverso il filtro quasi senza attenuazione. Questo si ottiene scambiando il *condensatore* e la *resistenza* come mostrato nella figura [ref:e_wiederstaende_hochpass]. La *risposta in frequenza* di un *filtro passa-alto* è rappresentata qualitativamente in [ref:e_hochpass_frequenzgang]. Un esempio pratico di applicazione di un *filtro passa-alto* è l’utilizzo in un *ricevitore* per separare le bande HF da quelle VHF, ad esempio per evitare interferenze causate dall’uso della banda HF su un ricevitore VHF.
<margin>
[picture:1025:e_wiederstaende_hochpass:Comportamento qualitativo delle resistenze nel partitore di tensione del filtro passa-alto]
[picture:1022:e_hochpass_frequenzgang:Andamento qualitativo della tensione d’uscita $U_\text{A}$ nel filtro passa-alto]
</margin>
[question:ED211]
[question:ED202]
---
I semplici circuiti RC presentano lo svantaggio che i loro fianchi nella zona di transizione sono piuttosto *piatti*. In un *filtro passa-basso* RC, la minima *impedenza* è determinata dalla *resistenza* $R$. Tuttavia, la *resistenza* $R$ può essere sostituita da una *bobina*, che si comporta in modo opposto a un *condensatore* in termini di risposta in frequenza. È quindi logico combinare *bobine* e *condensatori* per realizzare *filtri passa-alto* e *filtri passa-basso*.
Alle *frequenze alte*, la *impedenza* della *bobina* è elevata, mentre quella del *condensatore* è bassa.
Alle *frequenze basse*, la *impedenza* della *bobina* è bassa, mentre quella del *condensatore* è elevata.
A seconda del *componente* su cui viene misurata la *tensione d’uscita*, si ottiene un *filtro passa-alto* o un *filtro passa-basso*. Se si ricorda che la *impedenza* della *bobina* $X_\text{L}$ è elevata alle alte frequenze, è possibile identificare rapidamente un circuito come *filtro passa-alto* o *filtro passa-basso* osservando su quale *componente* viene misurata la *tensione d’uscita*.
<tip>
Anche nei circuiti con *condensatore* e *bobina* vale la seguente regola semplice: se nel ramo superiore del partitore di tensione si trova una *H* dritta – come in *H*ochpass (filtro passa-alto) – allora si tratta di un *filtro passa-alto*. Se invece nel ramo superiore si trova una *resistenza* o una *bobina*, si tratta di un *filtro passa-basso*.
[picture:1023:e_hochpass_tipp:Suggerimento per ricordare]
</tip>
[question:ED209]
[question:ED212]
---
Nelle domande seguenti si tratta di un'applicazione pratica dei nostri filtri. Naturalmente, in un circuito possono essere utilizzati anche più componenti dipendenti dalla frequenza, in modo che la transizione nell'area della frequenza di taglio diventi più ripida. Con il suggerimento fornito, dovresti ora riconoscere facilmente quale circuito viene utilizzato nelle prossime due domande.

[question:ED210]
[question:ED213]

Un altro esempio pratico di concatenazione di induttanze e condensatori come filtro è il diplexer spiegato a margine.

<indepth>
*Esempio pratico di diplexer:* I filtri passa-basso e passa-alto passivi vengono utilizzati anche nei separatori di frequenza. Nell'esempio sottostante è visibile un circuito per un cosiddetto diplexer per $\qty{2}{\meter}$ e $\qty{70}{\centi\meter}$. Questo può essere utilizzato, ad esempio, per collegare un apparecchio radio $\qty{2}{\meter}$ e uno $\qty{70}{\centi\meter}$ a un'antenna Duoband comune. Viceversa, si potrebbero utilizzare antenne separate per $\qty{2}{\meter}$ e $\qty{70}{\centi\meter}$ con un apparecchio radio VHF Duoband, ad esempio per utilizzare un'antenna omnidirezionale per il traffico diretto in $\qty{2}{\meter}$ e un'antenna direzionale per il traffico di ripetizione in $\qty{70}{\centi\meter}$. 
Prima dell'uscita $\qty{2}{\meter}$ è visibile un filtro passa-basso, mentre prima dell'uscita $\qty{70}{\centi\meter}$ è presente un filtro passa-alto, ciascuno composto da 5 componenti dipendenti dalla frequenza.
[picture:939:e_circuit_diplexer:Schema del diplexer $\qty{2}{\meter}$/$\qty{70}{\centi\meter}$]
[photo:171:e_example_diplexer:Esempio di montaggio]
</indepth>

<indepth>
*Due termini simili, ma che significano cose diverse:*

Un *diplexer* separa o combina diverse bande di frequenza, come descritto sopra.

Un *duplexer* consente di trasmettere e ricevere contemporaneamente sulla stessa antenna, anche se trasmettitore e ricevitore operano su frequenze vicine tra loro, come ad esempio nei ripetitori FM. In Svizzera, il gruppo UHF HB9UF ([https://www.hb9uf.ch/](https://www.hb9uf.ch/)) gestisce, insieme ad altri operatori, tali stazioni di ripetizione o "repeater", come vengono chiamate nel linguaggio inglese.

</indepth>

<indepth>
[photo:320:e_tiefpass_selbstbau:Filtro passa-basso autocostruito]
I filtri sopra menzionati possono naturalmente essere calcolati e costruiti in modo eccellente per tutte le bande di frequenza. Nella raccolta di formule sono disponibili le formule necessarie, ma esistono anche numerose proposte di costruzione e programmi di calcolo. Le induttanze necessarie possono essere facilmente autoprodotte. A tale scopo, per valori di induttanza piccoli è sufficiente un piccolo stock di filo di rame smaltato da $\qty{0,8}{\milli\meter}$ per bobine aeree stabili. Per valori di induttanza più grandi, ad esempio per le bande delle onde corte, si può utilizzare filo di rame smaltato da $\qty{0,2}{\milli\meter}$ e materiale del nucleo con valori $A_\text{L}$ appropriati, per poter produrre autonomamente i valori corretti in qualsiasi momento. Le dimensioni, il numero di spire e altri parametri necessari possono essere facilmente ottenuti tramite la raccolta di formule, le proposte di costruzione o i programmi di calcolo.
</indepth>

---

Ora abbiamo imparato a conoscere semplici componenti RC e LC come filtri passa-alto e passa-basso. Tuttavia, con condensatori e bobine è possibile realizzare ulteriori tipi di filtri che vanno oltre i semplici filtri passa-alto e passa-basso. Ora li esamineremo più da vicino nel secondo capitolo, ovvero i cosiddetti *circuiti oscillanti*.
<margin>
[immagine:1026:e_rp_schwingkreis:(a) Circuito oscillante in serie (b) Circuito oscillante in parallelo]
</margin>
Nei circuiti oscillanti, la bobina e il condensatore vengono disposti in modo tale – a seconda dell’effetto filtrante desiderato – che a una determinata frequenza si verifichi una resistenza particolarmente elevata o particolarmente bassa. In questo modo, le frequenze al di sopra o al di sotto di questa frequenza vengono attenuate o lasciate passare selettivamente.
La disposizione di bobina e condensatore può avvenire in serie o in parallelo. Si distinguono quindi circuiti oscillanti in serie (a) e circuiti oscillanti in parallelo (b), come illustrato nella figura [rif:e_rp_schwingkreis].
---
Se si collegano in parallelo una bobina e un condensatore e si applica, ad esempio, un impulso rettangolare a questa disposizione, il circuito entra in oscillazione. Il condensatore carico immagazzina ora energia nel campo elettrico, che si dissipa attraverso la bobina. Il flusso di corrente attraverso la bobina genera un campo magnetico al suo interno, che inizialmente oppone resistenza al flusso di corrente. Non appena il campo magnetico è completamente formato, il condensatore si scarica completamente. L’energia è ora immagazzinata nel campo magnetico della bobina. Tuttavia, poiché il condensatore non può più scaricarsi e mantenere il flusso di corrente, il campo magnetico non può essere mantenuto. Il campo magnetico della bobina si scarica e genera una tensione in direzione opposta. Questa tensione ricarica il condensatore in direzione opposta finché il campo magnetico nella bobina non si è esaurito e non oppone più resistenza al campo elettrico nel condensatore. Il processo ricomincia poi da capo.
<margin>
[include:applet_schwingkreis]
</margin>
---
Per questo motivo si parla di circuito oscillante. La frequenza alla quale questo circuito oscilla viene chiamata frequenza di risonanza ($f_0$). Essa è paragonabile alla frequenza di risonanza di un diapason, che entra in oscillazione quando viene colpito. In condizioni di risonanza, le resistenze della bobina $X_\text{L}$ e del condensatore $X_\text{C}$ sono uguali. Tali circuiti oscillanti possono essere utilizzati sia per la generazione di oscillazioni – come approfondiremo nel capitolo sugli oscillatori – sia come filtri, ed è proprio questo l’argomento di questo capitolo.
<margin>
[immagine:1037:e_rsk_frequenzgang:Risposta in frequenza qualitativa di un circuito oscillante in serie]
</margin>
---

In un *circuito risonante serie* come quello mostrato in figura [ref:e_rp_schwingkreis]a, la resistenza totale è minima alla frequenza di risonanza. La figura [ref:e_rsk_frequenzgang] illustra la risposta in frequenza. A frequenze superiori alla frequenza di risonanza, la resistenza della bobina aumenta, causando un aumento della resistenza totale del circuito risonante serie. Lo stesso accade anche a frequenze inferiori alla frequenza di risonanza, ma in questo caso è la resistenza del condensatore a essere elevata. Nei circuiti risonanti serie, quindi, la resistenza è minima alla frequenza di risonanza. A causa della connessione in serie, a frequenze diverse dalla frequenza di risonanza, il componente con la resistenza più elevata determina l'impedenza del circuito risonante.

<indepth>
La risposta in frequenza del modulo di un circuito risonante serie composto da una resistenza, una bobina e un condensatore si calcola con la seguente formula:
  
$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$
  
In condizioni di risonanza, quando $X_\text{C}$ = $X_\text{L}$, rimane solo la resistenza $R$. In condizioni ideali, se la resistenza $R=\qty{0}{\ohm}$, la resistenza è addirittura nulla. Sostituendo i valori di $X_\text{L}$ e $X_\text{C}$, otteniamo:
  
$Z = \sqrt{R^2+\left(2\pi f \cdot L~-~\frac{1}{2\pi f \cdot C} \right)^2}$
  
Nella formula si può osservare chiaramente la risposta in frequenza mostrata in figura [ref:e_rsk_frequenzgang]: se si porta la frequenza verso $\qty{0}{\hertz}$, il contributo della bobina scompare e rimane solo il condensatore. Se invece si porta la frequenza verso infinito, agisce solo la bobina e il contributo del condensatore scompare.
  
È possibile calcolare anche la frequenza di risonanza. Se $X_\text{L} = X_\text{C}$, si può risolvere la formula per $f$:
  
$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$
  
Da cui si ottiene la formula:
  
$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$
  
La derivazione dettagliata delle formule può essere consultata, ad esempio, su [Wikipedia](https://50ohm.de/schwk). A questo punto va sottolineato che tutti i grafici della risposta in frequenza sono rappresentati in modo qualitativo e, nella realtà, possono presentare differenze.
</indepth>

[question:ED205]

---

Se si collegano il condensatore e la bobina in un *circuito risonante parallelo*, come mostrato nella figura [ref:e_rp_schwingkreis]b, il comportamento è esattamente opposto: l'impedenza *$Z$* è molto elevata alla frequenza di risonanza, cfr. figura [ref:e_psk_frequenzgang]. Tuttavia, a frequenze superiori alla frequenza di risonanza, il condensatore presenta un'impedenza bassa, per cui l'impedenza di questo circuito risonante diminuisce. A frequenze inferiori alla frequenza di risonanza, invece, la bobina presenta un'impedenza bassa, motivo per cui anche a frequenze più basse l'impedenza del circuito risonante diminuisce.
Nei circuiti risonanti paralleli, quindi, l'impedenza è massima alla frequenza di risonanza. A frequenze diverse dalla frequenza di risonanza, è il componente con l'impedenza minore a determinare l'impedenza del circuito risonante parallelo.

<margin>
[picture:1036:e_psk_frequenzgang:Andamento qualitativo della risposta in frequenza di un circuito risonante parallelo]
</margin>

[question:ED206] 
[question:ED207]

% TODO ////

A seconda di come i circuiti risonanti paralleli e serie vengono impiegati nel percorso del segnale, è possibile attenuare o filtrare determinate bande di frequenza. Per questo scopo, utilizzeremo nuovamente l'approccio del partitore di tensione.

---

Iniziamo con le configurazioni per i *circuiti trappola*. Esistono due modi principali per realizzarli come partitori di tensione: in primo luogo il *circuito trappola* (cfr. figura [ref:e_saugkreis]) e in secondo luogo il *circuito trappola* (cfr. figura [ref:e_sperrkreis]). Nelle figure sono rappresentati rispettivamente la resistenza dipendente dalla frequenza e la tensione d’uscita. Utilizzando le regole note per il partitore di tensione, queste relazioni possono essere derivate e comprese in modo del tutto analogo ai precedenti circuiti RC. Poiché i circuiti oscillanti paralleli presentano un’elevata resistenza in risonanza, possono essere utilizzati efficacemente come circuito trappola in serie al percorso del segnale. Oppure si può utilizzare la bassa resistenza di risonanza di un circuito oscillante serie in parallelo al percorso del segnale come circuito trappola. Spesso, tuttavia, in questo caso si ricorre anche a una combinazione di entrambi. Un’applicazione dei circuiti trappola è ad esempio la soppressione di singole gamme di frequenza, ad esempio quando una stazione radio FM vicina interferisce con la ricezione.[question:ED204]
[question:ED214]
[question:ED215]
<margin>
[picture:1038:e_saugkreis:Andamenti qualitativi della frequenza di un circuito trappola]
[picture:1040:e_sperrkreis:Andamenti qualitativi della frequenza di un circuito trappola]
</margin>
---
La seconda categoria di configurazioni che si possono sviluppare con i circuiti oscillanti sono i *filtri passa-banda*. Anche in questo caso esistono due modi principali per realizzarli come partitori di tensione: in primo luogo il *circuito trappola* (cfr. figura [ref:e_leitkreis]) e in secondo luogo il *filtro passa-banda* (cfr. figura [ref:e_bandpass]). Anche in questo caso la derivazione avviene come di consueto attraverso il comportamento di un partitore di tensione. Per un filtro passa-banda si collegano i circuiti oscillanti paralleli in parallelo al percorso del segnale, poiché questi presentano una bassa resistenza alle frequenze lontane dalla risonanza e quindi "cortocircuitano" tali frequenze. Un circuito oscillante serie in serie al percorso del segnale provoca un’ulteriore attenuazione lontano dalla risonanza, mentre presenta una bassa resistenza alla frequenza desiderata.[question:ED203]
<margin>
[picture:1039:e_leitkreis:Andamenti qualitativi della frequenza di un circuito trappola]
[picture:1041:e_bandpass:Andamenti qualitativi della frequenza di un filtro passa-banda]
</margin>
Un esempio di applicazione evidente dei filtri passa-banda è il loro utilizzo nei ricevitore, dove è necessaria una pre-filtrazione di determinate gamme di frequenza. In questo caso si utilizza un filtro che lascia passare solo una gamma di frequenza desiderata, attenuando tutte le altre. Tali filtri passa-banda si trovano quindi in quasi tutti i ricevitore, spesso anche separatamente per ogni singola banda delle onde corte. Progettati per potenze elevate, i filtri passa-banda vengono utilizzati anche nel funzionamento in trasmissione, ad esempio durante contest o Fielddays comuni, per minimizzare le interferenze reciproche tra stazioni vicine.Per costruire filtri passa-banda e circuiti trappola, quindi, si possono utilizzare sia circuiti oscillanti serie che paralleli. È fondamentale tenere conto del comportamento dei rispettivi circuiti oscillanti in condizioni di risonanza. A seconda del loro comportamento, questi possono essere posizionati in serie o in parallelo al percorso del segnale, eventualmente anche combinati tra loro più volte.Nei filtri, come condensatori possono essere utilizzati solo determinati tipi idonei.
I condensatori elettrolitici, ad esempio, non sono adatti per circuiti ad alta frequenza, poiché la loro capacità dipende fortemente dalla frequenza e, inoltre, presentano un’elevata resistenza interna alle alte frequenze. I condensatori a film non sono invece adatti perché, a causa dei loro avvolgimenti (induttanza propria), sono fortemente dipendenti dalla frequenza soprattutto a partire dalle onde corte e hanno un basso fattore di qualità. 
I condensatori ceramici, invece, presentano solo piccole perdite e la capacità dipende poco da frequenza e temperatura. Inoltre, sono facilmente reperibili anche per tensioni elevate.
Anche i condensatori a piastre con isolamento in aria, che si trovano più comunemente nei condensatori variabili, sono adatti. Per tensioni elevate, i condensatori variabili vengono utilizzati anche nei sintonizzatori d’antenna.[question:ED216]
