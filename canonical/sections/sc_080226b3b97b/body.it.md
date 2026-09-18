Nella classe E abbiamo già imparato a conoscere il rosmetro e il suo utilizzo. Nella classe A vogliamo capire come funziona internamente un misuratore di ROS. Un rosmetro è composto solitamente da due accoppiatori direzionali. Prima di tutto vogliamo familiarizzare con il loro funzionamento.

Un *accoppiatore direzionale* serve a prelevare una piccola parte di un segnale RF da una linea di alimentazione. La sua particolarità consiste nel poter distinguere la direzione di propagazione dell'onda sulla linea. A questo scopo, il segnale viene rilevato in due modi diversi. Tramite un accoppiamento capacitivo si ottiene una tensione $U_C$ che dipende dalla tensione presente sulla linea di alimentazione. Allo stesso tempo, l'accoppiamento induttivo genera una tensione $U_I$ che dipende dalla corrente sulla linea di alimentazione. L'accoppiatore direzionale viene dimensionato in modo che le componenti del segnale ottenute per via capacitiva e induttiva siano di uguale ampiezza alle sue uscite. Tuttavia, alle due uscite queste componenti vengono combinate con segno opposto.

Per un'onda che si propaga in una direzione specifica sulla linea, ad esempio da sinistra a destra come mostrato nella figura [ref:a_richtkoppler_rechts_links], le tensioni ottenute per via capacitiva e induttiva si sommano a una delle uscite. All'altra uscita sono invece opposte e, in condizioni ideali, si annullano a vicenda. Il segnale appare quindi principalmente a una sola delle due uscite.

<margin>
[picture:1109:a_richtkoppler_rechts_links:Accoppiatore direzionale, l'onda si propaga da sinistra a destra]
</margin>

---

Se la direzione di propagazione dell'onda si inverte, ad esempio da destra a sinistra come mostrato nella figura [ref:a_richtkoppler_rechts_links], anche la direzione della corrente rispetto alla tensione si inverte. Di conseguenza, la tensione accoppiata induttivamente $U_I$ cambia segno, mentre la tensione accoppiata capacitivamente $U_C$ dipende dalla tensione sulla linea.

<margin>
[picture:1110:a_richtkoppler_rechts_links:Accoppiatore direzionale, l'onda si propaga da destra a sinistra]
</margin>

In questo modo si invertono anche le due uscite dell'accoppiatore direzionale: l'uscita in cui precedentemente le componenti si sommavano viene ora ampiamente annullata, mentre all'altra uscita si sommano.

In questo modo un accoppiatore direzionale può distinguere tra un'*onda in anticipo di fase* diretta verso l'antenna e un'*onda riflessa* diretta verso il trasmettitore.

---

Questa proprietà degli accoppiatori direzionali viene sfruttata in un *misuratore di ROS* o *rosmetro*: per misurare, si rilevano le tensioni di uscita di due accoppiatori direzionali inseriti nella linea e funzionanti in direzioni opposte. Le tensioni RF alle uscite degli accoppiatori direzionali vengono rettificate e filtrate con diodi. In questo modo si ottengono tensioni continue che possono essere visualizzate con uno strumento di misura.

[question:AI401]

La figura [ref:a_rswr_meter] mostra la struttura di principio di un rosmetro con due accoppiatori direzionali. Supponiamo che il trasmettitore si trovi sul lato sinistro e l'antenna su quello destro.

[question:AI402]

Il conduttore superiore fa parte della linea di alimentazione tra trasmettitore e antenna. Su di esso vengono rilevate due grandezze: tramite l'accoppiamento capacitivo viene prelevata una piccola parte della tensione RF. Contemporaneamente, tramite l'accoppiamento induttivo, viene ottenuta una componente che dipende dalla corrente sulla linea di alimentazione.

Il lato della linea di accoppiamento non utilizzato per la misura viene terminato con una *resistenza di terminazione*. Questa resistenza corrisponde approssimativamente all'impedenza caratteristica $Z_0$ della linea di accoppiamento. In questo modo, la potenza RF che giunge viene assorbita e non riflessa nuovamente nella linea di accoppiamento. Tali riflessioni peggiorerebbero la separazione tra onda in anticipo di fase e onda riflessa.

Queste due componenti del segnale vengono combinate nell'accoppiatore direzionale. Per un'onda che viaggia dal trasmettitore all'antenna, le componenti si sommano in uno dei due accoppiatori, mentre nell'altro si annullano quasi completamente. Per un'onda che viaggia nella direzione opposta, avviene il contrario.

I due circuiti, costruiti quasi specularmente, possono quindi rilevare direzioni di propagazione diverse:

* Un accoppiatore direzionale fornisce un segnale proporzionale all'*onda in anticipo di fase* dal trasmettitore all'antenna.
* L'altro accoppiatore direzionale fornisce un segnale proporzionale all'*onda riflessa* dall'antenna al trasmettitore.

I segnali prelevati sono inizialmente tensioni alternate RF. I diodi rettificano queste tensioni e i condensatori le filtrano. In questo modo si ottengono tensioni continue che possono essere visualizzate con le due lancette di un strumento a bobina mobile incrociata o misurate tramite un microcontrollore con convertitore digitale. Le resistenze regolabili servono per la regolazione o la calibrazione della visualizzazione. Vanno distinte dalle resistenze di terminazione delle linee di accoppiamento, che garantiscono una terminazione a bassa riflessione con $Z_0$.

<margin>
[picture:499:a_rswr_meter:Rosmetro con due accoppiatori direzionali]
</margin>