Nelle classi N ed E abbiamo già imparato come misurare correttamente corrente e tensione e quali sono le proprietà delle resistenze interne degli strumenti di misura. Se gli strumenti di misura non vengono installati correttamente nel circuito, si ottengono letture errate o insensate o, nel peggiore dei casi, si può danneggiare lo strumento di misura. Nella classe A ci sono altre due domande che verificano la corretta misurazione di corrente e tensione, ma in un contesto leggermente più complesso.

La prima domanda riguarda la misurazione della potenza di un amplificatore (Power Amplifier, PA). Conosciamo già la relazione $P = U \cdot I$: la potenza può essere determinata misurando tensione e corrente e moltiplicando successivamente entrambi i valori. Nella figura [ref:a_strom_spannung_messung] a sinistra è collegata l'alimentazione elettrica sotto forma di alimentatore, al centro si trova il PA e a destra è collegato un altro carico, il trasmettitore (TRX). Se ora vogliamo determinare la potenza del PA, solo la corrente che fluisce nel PA deve essere misurata.

<margin>
[picture:1003:a_strom_spannung_messung:Misurazione della potenza di un amplificatore (PA)]
</margin>

[question:AI101]

Per la domanda successiva, ricordiamo le regole della classe E, secondo cui gli strumenti di misura della tensione vengono sempre collegati in parallelo e gli strumenti di misura della corrente sempre in serie. Ciò rende la domanda molto facile da risolvere.

[question:AI102]

---

Di seguito esamineremo due parametri di misurazione che vengono spesso confusi:

- Risoluzione
- Precisione di misura (chiamata anche tolleranza o errore)

La *risoluzione* indica la più piccola variazione della grandezza misurata che uno strumento può ancora visualizzare. Esempio: un multimetro con una risoluzione di $\qty{0,1}{\volt}$ non può distinguere tra $\qty{10,5}{\volt}$ e $\qty{10,45}{\volt}$ se la differenza è inferiore alla risoluzione. Uno strumento con una risoluzione di $\qty{0,01}{\volt}$ può invece distinguere in modo significativamente più fine. La risoluzione è generalmente specificata dal produttore dello strumento di misura.

<tip>
Consideriamo prima la *risoluzione* con l'esempio di un orologio. Se l'orologio ha un display per ore e minuti, l'ora può essere indicata con una precisione di un minuto. Ma non si può leggere se sono le 13:03:10 o le 13:03:59. *Un minuto* è quindi la *risoluzione minima* dell'orologio (analogamente, un orologio con lancetta dei secondi ha una risoluzione minima di un secondo).
</tip>

La *precisione di misura* (anche errore di misura o tolleranza) di uno strumento indica quanto il valore visualizzato può discostarsi al massimo dal valore effettivo, sia verso l'alto che verso il basso, ad esempio $\pm\qty{5}{\percent}$. Una semplice regola pratica è: maggiore è il campo di misura che uno strumento deve coprire, minore è generalmente la precisione della misurazione.

La precisione di misura dipende, tra l'altro, dalla resistenza interna dello strumento di misura, poiché questa influenza il risultato della misurazione.
Nella classe E abbiamo imparato: uno strumento di misura della corrente ha una resistenza interna molto bassa (idealmente $\qty{0}{\ohm}$), mentre uno strumento di misura della tensione ha una resistenza interna molto alta (idealmente $\qty{\infty}{\ohm}$). Nella classe A esamineremo ora ulteriormente quanto accuratamente i nostri strumenti di misura possono rilevare la tensione o l'intensità di corrente effettivamente presente. Il valore misurato differisce infatti generalmente dal valore effettivo, e ciò è dovuto alle resistenze interne non perfette degli strumenti di misura, che influenzano la misurazione.

---

Esaminiamo lo schema equivalente di un reale strumento di misura della tensione nella figura [ref:a_reale_spannungsmessung] per la seguente domanda d'esame. Oltre all'ideale misuratore di corrente, un reale strumento di misura della tensione contiene una resistenza collegata in parallelo, ad esempio di $\qty{10}{\mega\ohm}$. Se questa resistenza fosse infinita, praticamente non esisterebbe e avremmo uno strumento ideale. Ciò significa tuttavia che in una reale misurazione di tensione scorre sempre una piccola corrente attraverso questa resistenza, che influenza il nostro risultato di misurazione. Immaginiamo, ad esempio, di voler misurare la tensione su un partitore di tensione: il partitore di tensione viene leggermente caricato dalla resistenza interna dello strumento di misura, in modo da non misurare esattamente la tensione che uno strumento ideale indicherebbe.

<margin>
[picture:1004:a_reale_spannungsmessung:Schema equivalente reale strumento di misura della tensione]
</margin>

---

Analogamente allo strumento di misura della tensione, si comporta anche lo strumento di misura della corrente. Un reale strumento di misura della corrente è costituito dall'effettivo misuratore di corrente e da una piccola resistenza collegata in serie, sulla quale cade sempre una piccola tensione. Se questa resistenza fosse zero, praticamente non esisterebbe e avremmo di nuovo lo strumento ideale.

<margin>
[picture:1007:a_reale_strommessung:Schema equivalente reale strumento di misura della corrente]
</margin>

---

[question:AI104]

<tip>
In questa domanda, l'indicazione "Risoluzione minima $\qty{100}{\micro\volt}$" non è importante. Può essere risolta solo con l'aiuto della legge di Ohm.
</tip>

---

Come si comportano ora le grandezze caratteristiche calcolate dai valori misurati, ad esempio la potenza nel nostro esempio iniziale ($P = U \cdot I$) dopo una misurazione di corrente e tensione? Le singole grandezze misurate come corrente e tensione deviano dal valore effettivo a causa di errori di misurazione, e queste deviazioni si ripercuotono di conseguenza nel calcolo.

Consideriamo un esempio concreto: supponiamo di voler determinare la potenza e misuriamo quindi una corrente continua e una tensione continua. Entrambi gli strumenti di misura indicano valori che sono inferiori del cinque percento ciascuno. Non si deve commettere l'errore di sommare semplicemente le deviazioni delle singole grandezze misurate. La formula della potenza rende chiaro che gli errori si moltiplicano in questo caso. Vediamo nel dettaglio:

$U_\text{Misurata}=0,95 \cdot U_\text{Vera}$ e $I_\text{Misurata}=0,95 \cdot I_\text{Vera}$

Calcoliamo la potenza con la nostra formula nota:

$P_\text{Misurata}=U_\text{Misurata} \cdot I_{Misurata}$

Ora inseriamo i valori veri:

$P_\text{Misurata} = 0,95 \cdot U_\text{Vera} \cdot 0,95 \cdot I_\text{Vera} = 0,9025 \cdot U_\text{Vera} \cdot I_\text{Vera}$

Ciò significa che la potenza misurata è circa $\qty{9,75}{\percent}$ inferiore alla potenza effettiva, poiché $1-0,9025 \equiv \qty{9,75}{\percent}$. Con queste conoscenze, la seguente domanda d'esame è risolvibile, i valori concreti di corrente e tensione non sono rilevanti per la soluzione.

[question:AI103]
