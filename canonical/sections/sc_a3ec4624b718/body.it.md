Nella classe E abbiamo già imparato a conoscere il *vettoriale analizzatore di rete* (VNA) (cfr. figura [ref:a_vna_swr]). Nella classe A vogliamo esaminarne il funzionamento in modo più approfondito.

Per una misurazione, il VNA genera inizialmente un segnale RF con una frequenza di partenza prestabilita e lo invia all'oggetto da misurare, ad esempio un'antenna o un circuito oscillante. Successivamente, misura il segnale di ritorno o riflesso dall'oggetto in esame. In questa fase vengono rilevate sia l'ampiezza che la fase del segnale. Per ridurre l'influenza di disturbi, è possibile eseguire più misurazioni per ogni punto di frequenza e calcolarne la media.

Dopo la misurazione, la frequenza viene incrementata di un passo prestabilito e il processo viene ripetuto. In questo modo, il VNA attraversa gradualmente l'intero intervallo dalla frequenza di partenza a quella di arresto. Questo procedimento è noto anche come *sweep di frequenza*, o in passato occasionalmente come *wobbulazione*.

Dai valori misurati per i singoli punti di frequenza, il VNA può determinare e rappresentare graficamente diverse grandezze in funzione della frequenza. Tra queste figurano, ad esempio, l'impedenza dell'oggetto in esame e il rapporto d'onda stazionaria (ROS). In questo modo è possibile riconoscere immediatamente a quali frequenze un'antenna è ben adattata o presenta una risonanza.

<margin>
[photo:323:a_vna_swr:Misurazione del ROS di un'antenna filare a estremità alimentata. Il ROS è quasi $1$ a $\qty{14}{\mega\hertz}$]
[picture:526:a_vna_swr_2:Possibile andamento del ROS di un'antenna.]
</margin>

[question:AI201]
[question:AI202]
[question:AI203]

---

Una possibile modalità di visualizzazione del VNA consiste nella suddivisione dell'impedenza nelle sue componenti attiva e reattiva (resistenza attiva $R$ e reattanza $X$). La resistenza attiva viene spesso espressa in $\unit{\ohm}$, mentre la reattanza viene talvolta indicata come $j\unit{\ohm}$. Le visualizzazioni dei diversi apparecchi non sono uniformi. Il simbolo $j$ deriva da una notazione dell'elettrotecnica in cui rappresenta l'unità immaginaria ($i$) della matematica. Una reattanza positiva indica un comportamento induttivo, mentre una reattanza negativa indica un comportamento capacitivo.

<indepth>
*I numeri immaginari* sono uno strumento molto utilizzato nell'elettrotecnica e nella matematica. Per risolvere equazioni come $x^2 = -1$, si è introdotto un numero immaginario ($i$) che, moltiplicato per se stesso, dà un numero negativo: $i^2 = -1$. Nessun numero reale soddisfa questa equazione, poiché un numero negativo moltiplicato per un altro numero negativo dà un numero positivo. Per questo motivo $i$ viene definito "immaginario". Questo numero "fittizio", moltiplicato per se stesso, dà un numero negativo, ovvero $-1$. Se si sommano numeri reali (ad esempio $54$) con un numero immaginario (ad esempio $-12i$), si ottiene un numero complesso: $54 - 12i$. Un numero complesso può essere utilizzato, ad esempio, per descrivere la componente attiva e reattiva di una resistenza. Inoltre, è possibile convertire un numero complesso in un'ampiezza e una fase. Nell'elettrotecnica, invece della lettera $i$, si utilizza la lettera $j$ per evitare confusione con il simbolo di corrente $i$.
</indepth>

[question:AI204]
[question:AI205]
[question:AI206]

---

Molti VNA offrono la possibilità di visualizzare graficamente l'andamento del ROS in funzione della frequenza. Se la frequenza di risonanza di un'antenna è troppo bassa, si sa che l'antenna deve essere accorciata. Se è troppo alta, l'antenna deve essere allungata.

[question:AI207]
[question:AI208]