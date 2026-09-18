Nella conversione A/D e D/A si collegano tra loro l’elaborazione digitale del segnale e quella analogica. In questo processo sono necessari filtri analogici sia prima del convertitore A/D che dopo il convertitore D/A. La figura [ref:a_adc_dac_filter] mostra l’intera catena del segnale. Sul lato di ingresso, prima del convertitore A/D, è presente un *filtro anti-aliasing*. Esso limita la banda di frequenza del segnale di ingresso analogico prima che venga campionato. Dopo l’elaborazione digitale del segnale, il convertitore D/A genera nuovamente un segnale analogico. Un *filtro di ricostruzione* posto a valle rimuove le componenti indesiderate ad alta frequenza del segnale. Perché entrambi i filtri siano necessari sarà spiegato nel paragrafo successivo.

<margin>
[picture:1131:a_adc_dac_filter:Conversione A/D e D/A con filtro anti-aliasing e filtro di ricostruzione]
</margin>

---

Dalla lezione sul teorema di campionamento sappiamo che un segnale deve essere campionato con una frequenza di campionamento sufficientemente elevata. Per un segnale con la frequenza massima $f_\mathrm{max}$ da acquisire, la frequenza di campionamento deve essere maggiore di $2\cdot f_\mathrm{max}$.

Tuttavia, tramite un’antenna riceviamo in genere molti segnali diversi, anche quelli con frequenze superiori alla banda che vogliamo effettivamente elaborare. Se tali componenti di frequenza raggiungono il convertitore A/D, nonostante la sua frequenza di campionamento non sia sufficiente per queste frequenze, possono apparire nel segnale digitale come altre frequenze, in realtà inesistenti. Queste vengono definite *aliasing*.

Per evitarlo, prima dell’ingresso del convertitore A/D viene inserito un *filtro anti-aliasing*. A seconda dell’applicazione, si tratta ad esempio di un filtro passa-basso o passa-banda. Un filtro passa-banda potrebbe essere utilizzato, ad esempio, per la voce. Il filtro deve attenuare in modo sufficiente le componenti indesiderate del segnale che potrebbero causare aliasing durante il campionamento. In particolare, le componenti di frequenza superiori alla metà della frequenza di campionamento non devono raggiungere il convertitore A/D senza essere attenuate.

[question:AF622]
[question:AF623]

<indepth>
Un esempio tangibile di *aliasing* lo incontriamo anche nella vita quotidiana con le immagini digitali. Fotografando con una fotocamera strutture molto fini e regolarmente ripetute, ad esempio una griglia a maglie strette, un tessuto a strisce sottili o una zanzariera, nell’immagine possono comparire improvvisamente motivi più grandi che non esistono nell’originale. Questi vengono chiamati *motivi moiré*.

La causa è simile a quella del campionamento di un segnale elettrico. Un sensore fotografico non può acquisire un’immagine in un numero arbitrario di punti, ma ha solo un numero finito di pixel. Se una struttura è più fine della risoluzione spaziale del sensore, non viene più campionata in modo univoco. Da una struttura fine in realtà presente può così generarsi apparentemente una struttura diversa, più grossolana.

Nel convertitore A/D avviene lo stesso principio sull’asse temporale: se una frequenza del segnale troppo elevata viene campionata con una frequenza di campionamento troppo bassa, nel segnale digitalizzato compare una frequenza diversa, più bassa, che in origine non era presente.

Un motivo moiré può quindi essere considerato come un esempio visibile di come, a causa di un campionamento insufficiente, possano nascere nuove strutture apparenti.

% TODO: Immagine da reperire
%<margin>
%[picture:XXXX:a_moire:Motivo moiré come esempio di aliasing spaziale]
%</margin>
</indepth>

---

Il convertitore A/D necessita inoltre di un generatore di clock, anche detto generatore di clock di campionamento. Questo determina in quali istanti il segnale di ingresso viene campionato e definisce quindi la frequenza di campionamento. La frequenza di campionamento può essere impostata in modo fisso o, ad esempio, controllata da un microcontrollore.

<margin>
[picture:1132:a_anit_alias:Filtro anti-aliasing, convertitore A/D e generatore di clock]
</margin>

[question:AF620]

---

Dall’altra parte dell’elaborazione digitale del segnale, il convertitore D/A esegue il processo inverso. Esso converte i campioni digitali in valori di tensione analogici. Poiché i singoli valori vengono emessi solo a intervalli di tempo fissi, all’uscita del convertitore D/A non si ottiene inizialmente un andamento del segnale idealmente liscio.

A causa dell’emissione a tempo discreto, oltre al segnale utile desiderato si generano anche componenti indesiderate ad alta frequenza (ad esempio, nella figura [ref:a_adc_4bit], le rapide transizioni tra i valori discreti del segnale di uscita contengono componenti ad alta frequenza). Per attenuare queste componenti, dopo il convertitore D/A viene inserito un *filtro di ricostruzione*. Anche in questo caso, a seconda dell’applicazione, si può utilizzare un filtro passa-basso o passa-banda.

Il filtro di ricostruzione lascia passare la banda di frequenza utile desiderata e attenua le componenti indesiderate ad alta frequenza del convertitore D/A. In questo modo, all’uscita si ottiene nuovamente un segnale analogico il più possibile pulito (cfr. figura [ref:a_adc_12bit], il filtro di ricostruzione smussa il segnale).

[question:AF624]
[question:AF625]

<margin>
[picture:300:a_adc_4bit:Segnale prima del filtro di ricostruzione]
[picture:299:a_adc_12bit:Segnale dopo il filtro di ricostruzione]
</margin>