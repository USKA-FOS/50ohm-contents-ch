Nel capitolo precedente abbiamo visto che esistono diversi tipi di oscillatori con stabilità e precisione in frequenza differenti. Gli oscillatori al quarzo, in particolare nella versione TCXO e soprattutto OCXO, raggiungono una stabilità particolarmente elevata. I moderni apparati radio, ad esempio, con un TCXO raggiungono una precisione in frequenza di $\pm\qty{0,5}{\ppm}$. A una frequenza desiderata di $\qty{10}{\mega\hertz}$, la frequenza effettiva si colloca quindi nell’intervallo $\qtyrange{9,999995}{10,000005}{\mega\hertz}$, ovvero al massimo $\pm\qty{5}{\hertz}$ dalla frequenza nominale. Tale deviazione è minima e, per le operazioni in onde corte, di solito più che sufficiente.

Se però non lavoriamo a $\qty{10}{\mega\hertz}$, ma a $\qty{10}{\giga\hertz}$, la possibile deviazione aumenta fino a $\pm\qty{5000}{\hertz}$. Essa può quindi già superare la larghezza di banda di un tipico filtro SSB. In un collegamento radio su una frequenza concordata, il segnale potrebbe quindi trovarsi al di fuori della banda di ricezione. Per applicazioni di questo tipo, ad esempio per il satellite geostazionario QO-100 che trasmette a $\qty{10}{\giga\hertz}$, sono quindi necessarie referenze di frequenza ancora più precise.

<margin>
[picture:1081:a_gpsdo:Oscillatore disciplinato GPS (GPSDO) nel contesto di una stazione QO-100]
</margin>

Si potrebbe investire molto per stabilizzare ulteriormente un OCXO o utilizzare altri tipi di oscillatori, come gli standard di frequenza al rubidio, che offrono una stabilità maggiore rispetto agli oscillatori al quarzo, soprattutto su lunghi periodi. Tuttavia, questi standard di frequenza presentano spesso svantaggi come un maggiore assorbimento di corrente, dimensioni più grandi e un prezzo più elevato, poiché sono sviluppati principalmente per applicazioni professionali.

Fortunatamente esiste un’altra soluzione: i sistemi di navigazione satellitare, in inglese Global Navigation Satellite Systems (GNSS), come GPS o Galileo, necessitano di riferimenti temporali molto precisi. La posizione del ricevitore viene determinata in base ai tempi di propagazione dei segnali trasmessi da più satelliti al ricevitore. Poiché ogni orologio preciso richiede un oscillatore stabile come base temporale, possiamo utilizzare il riferimento temporale ottenuto dai segnali satellitari per stabilizzare il nostro TCXO o OCXO. Un oscillatore di questo tipo viene chiamato oscillatore disciplinato GPS o, in inglese, GPS-Disciplined Oscillator (GPSDO). Come funziona tecnicamente questa regolazione verrà approfondito in un capitolo successivo sulle anse ad aggancio di fase (PLL). Nella figura [ref:a_gpsdo] è rappresentato un GPSDO nel contesto di una stazione QO-100, che fornisce al Software Defined Radio (SDR) una frequenza di riferimento stabile. Un modulo autocostruito è visibile nella figura [ref:a_gpsdo_homebrew].

---

A questo punto ci si potrebbe chiedere perché non utilizzare direttamente il riferimento temporale fornito dal GPS come segnale dell’oscillatore. Il ricevitore GPS ricava dai deboli segnali satellitari modulati un segnale temporale preciso, ad esempio un impulso al secondo. Tuttavia, il preciso istante di questo impulso può subire fluttuazioni a breve termine a causa di rumore, propagazione per cammini multipli, influenze atmosferiche e ritardi nel ricevitore. Su lunghi periodi, la frequenza derivata da esso risulta invece molto precisa.

Un TCXO o OCXO, invece, offre una buona o molto buona stabilità a breve termine, ma può deviare lentamente dalla frequenza nominale a lungo termine a causa di influenze residue di temperatura e dell’invecchiamento dei suoi componenti. In un GPSDO, quindi, vengono combinate entrambe le caratteristiche: il TCXO o OCXO locale fornisce un segnale d’uscita a breve termine stabile e a basso rumore, mentre un anello di regolazione lento corregge la sua deviazione a lungo termine grazie al riferimento temporale GPS. In questo modo, un GPSDO raggiunge sia una stabilità a breve termine molto elevata che un’elevata stabilità e precisione in frequenza a lungo termine.

[question:AD606]

<margin>
[photo:335:a_gpsdo_homebrew:GPSDO autocostruito con TCXO]
</margin>