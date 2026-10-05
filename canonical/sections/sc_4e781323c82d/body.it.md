Nella conversione A/D e D/A, l'elaborazione analogica e digitale del segnale vengono combinate. In questo processo, sono necessari filtri analogici sia prima del convertitore analogico che dopo del convertitore digitale. La figura [ref:a_adc_dac_filter] mostra l'intera catena del segnale. Sul lato di ingresso, prima del convertitore analogico, si trova un *filtro anti-aliasing*. Esso limita la banda di frequenza del segnale di ingresso analogico prima che questo venga campionato. Dopo l'elaborazione digitale del segnale, il convertitore digitale genera nuovamente un segnale analogico. Un *filtro di ricostruzione* posto a valle rimuove le componenti di segnale ad alta frequenza indesiderate. Perché entrambi i filtri sono necessari, lo esamineremo nella sezione seguente.

<margin>
[picture:1131:a_adc_dac_filter:Conversione A/D e D/A con filtro anti-aliasing e filtro di ricostruzione]
</margin>

---

Dalla lezione sul teorema di campionamento nella sezione [sec:abtasttheorem] sappiamo che un segnale deve essere campionato con una frequenza di campionamento sufficientemente alta. Per un segnale con la frequenza massima da acquisire $f_\mathrm{max}$, la frequenza di campionamento deve essere maggiore di $2\cdot f_\mathrm{max}$.

Tuttavia, tramite un'antenna riceviamo generalmente molti segnali diversi – anche quelli con frequenze al di sopra della banda di frequenza che vogliamo effettivamente elaborare. Se tali componenti di segnale raggiungono il convertitore analogico, anche se la sua frequenza di campionamento per queste frequenze non è sufficiente, possono apparire nel segnale digitale come altre frequenze, in realtà non presenti. Queste vengono chiamate *alias*.

Per evitare ciò, viene utilizzato un *filtro anti-aliasing* prima dell'ingresso del convertitore analogico. A seconda dell'applicazione, si tratta ad esempio di un filtro passa-basso o passa-banda. Un filtro passa-banda potrebbe essere utilizzato, ad esempio, per la voce. Il filtro deve sopprimere sufficientemente le componenti di segnale indesiderate che potrebbero causare aliasing durante il campionamento. In particolare, le componenti di frequenza al di sopra della metà della frequenza di campionamento non devono raggiungere il convertitore analogico senza ostacoli.

[question:AF622]
[question:AF623]

<indepth>
Un esempio illustrativo di *aliasing* lo incontriamo anche nella vita quotidiana con le immagini digitali. Se si fotografano strutture molto fini e regolarmente ripetute con una fotocamera, ad esempio una griglia a maglie strette, un tessuto con strisce sottili o una zanzariera, nell'immagine possono apparire improvvisamente motivi più grandi che nell'originale non erano affatto presenti. Questi sono chiamati *motivi moiré*.

La causa è simile al campionamento di un segnale elettrico. Un sensore di fotocamera non può acquisire un'immagine in un numero arbitrario di punti, ma ha solo un numero finito di pixel. Se una struttura è più fine della risoluzione spaziale del sensore, non viene più campionata in modo univoco. Dalla struttura fine effettivamente presente può così apparentemente emergere un'altra struttura più grossolana.

Nel convertitore analogico avviene lo stesso principio sull'asse del tempo: se una frequenza di segnale troppo alta viene campionata con una frequenza di campionamento troppo bassa, nel segnale digitalizzato appare un'altra frequenza più bassa, che originariamente non era affatto presente.

Un motivo moiré può quindi essere considerato un esempio visibile di come, attraverso un campionamento insufficiente, possano emergere nuove strutture apparenti.

% TODO: Immagine da procurarsi
%<margin>
%[picture:XXXX:a_moire:Motivo moiré come esempio di aliasing spaziale]
%</margin>
</indepth>

---

Il convertitore analogico necessita inoltre di un generatore di clock, chiamato anche generatore di clock di campionamento. Questo determina in quali istanti il segnale di ingresso viene campionato e definisce quindi la frequenza di campionamento. La frequenza di campionamento può essere fissata o, ad esempio, controllata da un microcontrollore.

<margin>
[picture:1132:a_anit_alias:Filtro anti-aliasing, convertitore analogico e generatore di clock]
</margin>

[question:AF620]

---

Dall'altro lato dell'elaborazione digitale del segnale, il convertitore digitale svolge il processo inverso. Converte i campioni digitali nuovamente in valori di tensione analogici. Poiché i singoli valori vengono emessi solo a intervalli di tempo fissi, inizialmente all'uscita del convertitore digitale non si forma un andamento del segnale idealmente liscio.

A causa dell'emissione a tempo discreto, oltre al segnale utile desiderato, si generano anche componenti di segnale ad alta frequenza indesiderate (ad esempio nella figura [ref:a_adc_4bit], le rapide transizioni tra i valori discreti del segnale di uscita contengono le componenti ad alta frequenza). Per sopprimerle, viene utilizzato un *filtro di ricostruzione* dopo il convertitore digitale. Anche qui, a seconda dell'applicazione, può essere utilizzato ad esempio un filtro passa-basso o passa-banda.

Il filtro di ricostruzione lascia passare la banda di frequenza utile desiderata e sopprime le componenti di segnale ad alta frequenza indesiderate del convertitore digitale. In questo modo, all'uscita si forma nuovamente un segnale analogico il più pulito possibile (cfr. figura [ref:a_adc_12bit], il filtro di ricostruzione leviga il segnale).

[question:AF624]
[question:AF625]

<margin>
[picture:300:a_adc_4bit:Segnale prima del filtro di ricostruzione]
[picture:299:a_adc_12bit:Segnale dopo il filtro di ricostruzione]
</margin>
