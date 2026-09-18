Nelle classi N ed E abbiamo già imparato come misurare correttamente corrente e tensione e quali caratteristiche hanno le resistenze interne degli strumenti di misura. Se gli strumenti non vengono collegati correttamente nel circuito, si ottengono letture errate o prive di senso, oppure, nel caso peggiore, si può danneggiare lo strumento. Nella classe A ci sono altre due domande che verificano la corretta misurazione di corrente e tensione, ma in un contesto leggermente più complesso.

La prima domanda riguarda la misurazione della potenza di un amplificatore (Power Amplifier, PA). Conosciamo già la relazione $P = U \cdot I$: la potenza può essere determinata misurando tensione e corrente e moltiplicando successivamente i due valori. Nella figura [ref:a_strom_spannung_messung] a sinistra è collegata l’alimentazione elettrica sotto forma di alimentatore, al centro si trova la PA e a destra è collegato un altro utilizzatore, il trasmettitore (TRX). Se vogliamo determinare la potenza della PA, possiamo misurare esclusivamente la corrente che fluisce nella PA.

<margin>
[picture:1003:a_strom_spannung_messung:Misurazione della potenza di un amplificatore (PA)]
</margin>

[question:AI101]


Per la domanda successiva ricordiamo le regole della classe E: gli voltmetri vanno sempre collegati in parallelo e gli amperometri sempre in serie. Grazie a questo, la domanda è molto facile da risolvere.

[question:AI102]


---


Di seguito vogliamo esaminare due parametri di misura che spesso vengono confusi:


- Risoluzione
- Accuratezza di misura (detta anche tolleranza o errore)


La *risoluzione* indica la minima variazione della grandezza misurata che uno strumento è in grado di indicare. Esempio: un multimetro con una risoluzione di $\qty{0,1}{\volt}$ non può distinguere tra $\qty{10,5}{\volt}$ e $\qty{10,45}{\volt}$ se la differenza è inferiore alla risoluzione. Un apparecchio con risoluzione di $\qty{0,01}{\volt}$ può invece distinguere con maggiore precisione. La risoluzione viene generalmente indicata dal produttore dello strumento di misura.


<tip>
Consideriamo inizialmente la *risoluzione* prendendo come esempio un orologio. Se l’orologio ha solo l’indicazione delle ore e dei minuti, il tempo può essere letto con precisione al minuto. Tuttavia, non è possibile distinguere se siano le 13:03:10 o le 13:03:59. *Un minuto* è quindi la *risoluzione minima* dell’orologio (analogamente, un orologio con lancetta dei secondi ha una risoluzione minima di un secondo).
</tip>


L’*accuratezza di misura* (detta anche errore di misura o tolleranza) di uno strumento descrive di quanto il valore indicato può discostarsi al massimo dal valore reale, sia in eccesso che in difetto, ad esempio $\pm\qty{5}{\percent}$. Una semplice regola empirica recita: più ampio è l’intervallo di misura che uno strumento deve coprire, minore è generalmente l’accuratezza della misurazione.


L’accuratezza di misura dipende, tra l’altro, dalla resistenza interna dello strumento di misura, poiché questa influisce sul risultato della misurazione.

Nella classe E abbiamo imparato che un amperometro ha una resistenza interna molto bassa (idealmente $\qty{0}{\ohm}$), mentre un voltmetro ha una resistenza interna molto alta (idealmente $\qty{\infty}{\ohm}$). Nella classe A vogliamo ora esaminare ulteriormente quanto accuratamente i nostri strumenti di misura rilevano la tensione o l’intensità di corrente effettivamente presenti. Il valore indicato si discosta infatti generalmente dal valore reale, e questo è dovuto alle resistenze interne non ideali degli strumenti, che influenzano la misurazione.

---


Esaminiamo lo schema equivalente di un voltmetro reale nella figura [ref:a_reale_spannungsmessung] relativa alla domanda d’esame seguente. Oltre all’amperometro ideale, un voltmetro reale contiene una resistenza collegata in parallelo, ad esempio di $\qty{10}{\mega\ohm}$. Se questa resistenza fosse infinita, non esisterebbe praticamente e avremmo uno strumento ideale. Tuttavia, questo significa che in una misurazione reale di tensione fluisce sempre una piccola corrente attraverso questa resistenza, che influisce sul risultato della misurazione. Immaginiamo, ad esempio, di voler misurare la tensione ai capi di un partitore di tensione: a causa della resistenza interna dello strumento, il partitore viene leggermente caricato, per cui non misuriamo esattamente la tensione che indicherebbe uno strumento ideale.


<margin>
[picture:1004:a_reale_spannungsmessung:Schema equivalente di un voltmetro reale]
</margin>

---


Analogamente al voltmetro, anche l’amperometro si comporta in modo simile. Un amperometro reale è costituito dallo strumento di misura vero e proprio e da una piccola resistenza collegata in serie, sulla quale cade sempre una piccola tensione.

<margin>
[picture:1007:a_reale_strommessung:Schema equivalente di un amperometro reale]
</margin>

---


[question:AI104]


<tip>
Per questa domanda, l’indicazione "Risoluzione minima $\qty{100}{\micro\volt}$" non è rilevante. Può essere risolta unicamente con l’aiuto della legge di Ohm.
</tip>

---


Come si comportano ora i parametri derivati da valori misurati – ad esempio la potenza nel nostro esempio iniziale ($P = U \cdot I$) dopo una misurazione di corrente e tensione? Le singole grandezze misurate come corrente e tensione si discostano, a causa degli errori di misura, dal valore reale, e queste deviazioni si ripercuotono di conseguenza nel calcolo.


Esaminiamo un esempio concreto: supponiamo di voler determinare la potenza e a tal fine misuriamo una tensione continua e una corrente continua. Entrambi gli strumenti indicano valori che sono inferiori del cinque percento rispetto al valore reale. Non si deve commettere l’errore di sommare semplicemente le deviazioni delle singole grandezze misurate. Dalla formula della potenza risulta chiaro che in questo caso gli errori si moltiplicano. Esaminiamo questo nel dettaglio:


$U_\text{Misurata}=0,95 \cdot U_\text{Reale}$ e $I_\text{Misurata}=0,95 \cdot I_\text{Reale}$


La potenza la calcoliamo con la nostra formula nota:


$P_\text{Misurata}=U_\text{Misurata} \cdot I_\text{Misurata}$


Ora inseriamo i valori reali:


$P_\text{Misurata} = 0,95 \cdot U_\text{Reale} \cdot 0,95 \cdot I_\text{Reale} = 0,9025 \cdot U_\text{Reale} \cdot I_\text{Reale}$


Ciò significa che la potenza misurata è circa $\qty{9,75}{\percent}$ inferiore rispetto a quella reale, poiché $1-0,9025 \equiv \qty{9,75}{\percent}$. Con questa conoscenza è risolvibile la domanda d’esame seguente, i valori concreti di corrente e tensione non sono rilevanti per la soluzione.


[question:AI103]