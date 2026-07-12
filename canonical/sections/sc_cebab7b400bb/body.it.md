Nelle lezioni delle classi N ed E abbiamo già appreso le interferenze tipiche dei dispositivi e degli impianti elettronici – ad esempio dovute a irraggiamento diretto nell'involucro o a accoppiamento nelle linee di alimentazione – nonché le contromisure e i comportamenti appropriati. Nella classe A, questi aspetti vengono approfonditi ulteriormente. 

[question:AJ105]

Se si verificano disturbi di ricezione nei ricevitori autocostruiti digitali, una possibile causa può essere una scarsa schermatura del ricevitore. In questo caso, è opportuno installare il circuito stampato del ricevitore in un involucro metallico messo a terra. Soprattutto per i ricevitori SDR o le soluzioni autocostruite basate sulla tecnologia SDR, una buona schermatura è assolutamente necessaria per evitare irraggiamenti. Viceversa, in questo modo si riducono anche le emissioni indesiderate da parte di questi dispositivi.

[question:AJ103]

---

Nella classe E abbiamo già trattato gli accoppiamenti nelle linee di alimentazione. Esiste tuttavia un'altra contromisura che vogliamo esaminare più da vicino di seguito. Se i disturbi si propagano attraverso la linea di alimentazione, l'installazione di un filtro di rete sotto forma di filtro passa-basso (cfr. figura [ref:a_netzfilter] e figura [ref:a_netzfilter_draw]) è una soluzione. Questi filtri sono disponibili come dispositivi pronti all'uso, nel rispetto delle normative VDE. 

[question:AJ116]
[question:AJ117]
[question:AJ118]

<margin>
[photo:244:a_netzfilter:Netzfilter]
[picture:367:a_netzfilter_draw:Schaltung eines Netzfilters]
</margin>

Diversi metodi di trasmissione hanno effetti diversi per quanto riguarda le interferenze con dispositivi e linee, a causa delle loro caratteristiche di modulazione. In particolare, i tipi di modulazione CW e SSB (in cui l'ampiezza cambia rapidamente) causano spesso interferenze nelle linee di alimentazione degli altoparlanti e un conseguente raddrizzamento dell'HF sulle giunzioni base-emettitore nella sezione BF degli amplificatori. La giunzione base-emettitore si comporta qui come un diodo e raddrizza l'HF. In questo modo, la BF demodulata diventa udibile negli altoparlanti.

[question:AJ107]
[question:AJ106]

Per proteggere i ricevitori DVB-T da segnali forti di un trasmettitore radioamatore VHF/UHF nelle immediate vicinanze, è necessario installare un filtro passa-alto nella linea di alimentazione dell'antenna del ricevitore DVB-T. Questo è tuttavia efficace solo con antenne di ricezione passive. In particolare, i preamplificatori di antenna TV non selettivi vengono rapidamente sovraeccitati da segnali di trasmissione adiacenti, poiché amplificano un ampio campo di frequenza.
Con antenne di ricezione attive, un filtro passa-alto deve essere installato prima del preamplificatore dell'antenna.
Quando si installano filtri, è necessario considerare anche l'attenuazione di inserzione dei filtri nella banda passante. Questa dovrebbe essere il più bassa possibile e non superare i $\qtyrange{2}{3}{\dB}$ per consentire al segnale ricevuto desiderato di passare il più liberamente possibile.

[question:AJ113]
[question:AJ114]
[question:AJ108]

Fondamentalmente, ha senso installare un filtro passa-basso con una frequenza di taglio di $\qtyrange{30}{40}{\mega\hertz}$ dietro un potente trasmettitore a onde corte. Anche utilizzando un accordatore d'antenna in configurazione passa-basso (filtro Pi o LC) si può ottenere un effetto passa-basso che sopprime efficacemente le emissioni di armoniche superiori.

[question:AJ112]
[question:AJ104]

Forti segnali di trasmissione da una stazione radioamatoriale possono causare disturbi di ricezione, rumori o interruzioni/artefatti/silenzio (in particolare nei ricevitori digitali come DAB/DVB-T) nei ricevitori DAB, TV e FM. Questi disturbi sono spesso causati dalla sovraeccitazione dell'ingresso del ricevitore a causa di elevate intensità di segnale nel luogo di ricezione e portano a una riduzione della sensibilità del ricevitore o alla sovraeccitazione dello stadio di ingresso del ricevitore.

[question:AJ110]
[question:AJ111]
[question:AJ109]

Per evitare i problemi sopra menzionati, il radioamatore dovrebbe quindi lavorare sempre solo con la potenza di trasmissione minima necessaria per una comunicazione soddisfacente.

[question:AJ101]

Per bloccare i disturbi HF nei circuiti e nei dispositivi vengono spesso utilizzati condensatori di blocco. Questi devono avere la proprietà di scaricare l'HF verso massa nel modo più efficiente possibile. I condensatori ceramici sono particolarmente adatti a questo scopo. I condensatori elettrolitici e a film plastico sono inadatti, poiché la loro costruzione avvolta presenta un'elevata autoinduttanza. Nel caso dei condensatori al tantalio, spesso viene collegato in parallelo un condensatore ceramico per migliorare le proprietà di scarico HF, poiché questi ultimi sono adatti solo per frequenze HF medie fino a circa $\qty{30}{\mega\hertz}$, mentre i condensatori ceramici possono bloccare frequenze molto più elevate.
Per scaricare efficacemente i disturbi HF è necessaria una messa a terra efficace con bassa impedenza.

[question:AJ119]
[question:AJ102]

Nelle linee di alimentazione degli stadi HF vengono spesso utilizzate induttanze di alta frequenza. Queste rappresentano un'impedenza in serie per l'alta frequenza e bloccano efficacemente le correnti di ingresso ad alta frequenza negli stadi, nonché le correnti di ritorno HF nell'alimentazione degli stadi.
A causa della loro costruzione avvolta, queste induttanze hanno anche capacità parassite, in modo che, in combinazione con la loro induttanza, formino risonanze indesiderate (circuiti oscillanti). Ciò può portare a *risonanze secondarie* indesiderate negli stadi HF, causate dalle *auto-risonanze* delle induttanze HF. Le risonanze secondarie possono influenzare negativamente le caratteristiche degli stadi HF. Ciò può portare a effetti di retroazione indesiderati, in particolare negli amplificatori, nonché a cali nelle caratteristiche di potenza degli stadi HF.

[question:AJ214]