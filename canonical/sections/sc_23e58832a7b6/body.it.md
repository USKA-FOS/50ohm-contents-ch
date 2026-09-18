Nella digitalizzazione di un segnale analogico è necessario considerare due proprietà: in quali istanti temporali viene misurato il segnale e con quale precisione i valori misurati possono essere rappresentati. I due passaggi corrispondenti sono denominati *campionamento* e *quantizzazione*.

I termini *a tempo continuo*, *a tempo discreto*, *a valori continui* e *a valori discreti* descrivono due proprietà indipendenti di un segnale. Da un lato si può considerare se il segnale è definito in ogni istante temporale arbitrario. Dall'altro si può considerare se può assumere valori arbitrari.

Un segnale analogico ideale è sia *a tempo continuo* che *a valori continui*. È definito in ogni istante temporale arbitrario e può assumere qualsiasi valore intermedio all'interno del suo intervallo di valori. Un segnale di questo tipo è mostrato nella figura [ref:a_wertkont_zeitkont].

---

I segnali analogici non possiedono una risoluzione temporale minima e sono continui nel tempo. Per questo motivo sono definiti *a tempo continuo*. Nel campionamento, invece, un segnale di questo tipo viene misurato solo in istanti temporali specifici, cioè viene campionato. I singoli valori di campionamento sono chiamati *campioni*.

I campioni rappresentano solo lo stato istantaneo del segnale al momento del campionamento. Tra due istanti di campionamento il segnale analogico può continuare a variare. Poiché dopo il campionamento sono disponibili solo valori separati nel tempo, il segnale campionato viene definito *a tempo discreto*.

La figura [ref:a_wertkont_zeitdisk] mostra un segnale campionato in modo ideale. È *a tempo discreto* poiché sono disponibili valori solo in istanti di campionamento specifici. Tuttavia, i singoli campioni possono inizialmente assumere ancora valori arbitrari e sono quindi *a valori continui*.

<margin>
[picture:408:a_wertkont_zeitkont:Segnale a valori e tempo continui]
[picture:409:a_wertkont_zeitdisk:Segnale a valori continui e tempo discreto]
</margin>

[question:AF601]
[question:AF603]

Il processo in cui un segnale a tempo continuo viene campionato in istanti specifici e convertito in un segnale a tempo discreto è chiamato *campionamento*.


[question:AF606]

La velocità con cui viene effettuato il campionamento di un segnale analogico è chiamata *frequenza di campionamento* o *Abtastrate*. Essa indica quanti campioni vengono acquisiti per unità di tempo, ad esempio per secondo.

I segnali audio analogici nei supporti digitali come i CD vengono campionati, ad esempio, con una frequenza di campionamento di $\num{44100}$ campioni al secondo (unità $\unit{\sps}$), o brevemente $\qty{44,1}{\kilo\sps}$.

[question:AF615]

---

Oltre alla risoluzione temporale, nella digitalizzazione riveste un ruolo importante anche la risoluzione dei valori misurati. I segnali analogici possono assumere valori di tensione arbitrari e variare tra questi senza stadi intermedi fissi. Per questo motivo sono definiti *a valori continui*.

Nella digitalizzazione, invece, è disponibile solo un numero limitato di valori numerici possibili. Un valore di tensione misurato deve quindi essere assegnato a uno di questi stadi fissi. Il segnale diventa quindi *a valori discreti*.

Se un valore di segnale analogico si trova tra due stadi possibili, è necessario decidere a quale stadio assegnare il valore misurato. Questo processo è chiamato *quantizzazione*. Il segnale precedentemente a valori continui viene così mappato su un numero finito di valori possibili.

[question:AF605]

La figura [ref:a_wertdisk_zeitkont] mostra, a titolo di esempio, un segnale *a valori discreti ma a tempo continuo*. Il segnale è ancora definito in ogni istante temporale, ma può assumere solo valori specifici e predefiniti. I valori possibili sono quindi già quantizzati, mentre il tempo non è ancora stato discretizzato.

Se il campionamento e la quantizzazione vengono combinati, si ottiene un segnale *a valori e tempo discreti*, come mostrato nella figura [ref:a_wertdisk_zeitdisk]. Sono disponibili campioni solo in istanti temporali specifici e anche i loro valori possibili sono limitati a stadi fissi. Questo corrisponde alla rappresentazione digitale di un segnale precedentemente analogico.

<tip>
Per visualizzare il concetto, si può paragonare un dimmer analogico a un interruttore a gradini. Con un dimmer analogico è possibile regolare la luminosità di una lampada in modo estremamente preciso. Con un interruttore a gradini con, ad esempio, $\num{5}$ gradini, sono disponibili solo $\num{5}$ valori di luminosità diversi. Non sono possibili valori intermedi.

Se si vuole riprodurre una luminosità impostata con il dimmer analogico utilizzando l'interruttore a gradini, è necessario scegliere il gradino più adatto. Questo corrisponde esattamente al principio della quantizzazione: un valore continuo viene assegnato a uno di diversi valori predefiniti.
</tip>

<margin>
[picture:410:a_wertdisk_zeitkont:Segnale a valori discreti e tempo continuo]
[picture:411:a_wertdisk_zeitdisk:Segnale a valori e tempo discreti]
</margin>

[question:AF602]
[question:AF604]

<indepth>
Qui è possibile sperimentare il tutto in modo pratico. Un segnale sinusoidale a tempo continuo viene digitalizzato da un convertitore AD e successivamente riconvertito da un convertitore DA in un segnale analogico a tempo continuo, ma ancora a valori discreti. Con i regolatori è possibile impostare la quantizzazione temporale e dei valori dei convertitori AD/DA.

[include:quantisierung_und_sampling]
</indepth>