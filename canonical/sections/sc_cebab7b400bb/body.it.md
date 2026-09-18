Nelle lezioni delle classi N ed E abbiamo già affrontato le tipiche interferenze su dispositivi e impianti elettronici – ad esempio dovute a irradiazioni dirette all’interno dell’involucro o a accoppiamenti nelle linee di alimentazione – nonché le contromisure e i comportamenti appropriati. Nella classe A questi aspetti vengono approfonditi ulteriormente.

[question:AJ105]

Se in un ricevitore digitale autocostruito si verificano disturbi di ricezione, una possibile causa potrebbe essere una schermatura insufficiente del ricevitore. In questi casi è consigliabile montare la scheda del ricevitore all’interno di un involucro metallico collegato a massa. In particolare, per i ricevitori SDR o le soluzioni autocostruite basate su tecnologia SDR, una buona schermatura è fondamentale per evitare irradiazioni indesiderate. Viceversa, questo metodo riduce anche le emissioni indesiderate di questi dispositivi.

[question:AJ103]

---

Nella classe E abbiamo già trattato gli accoppiamenti nelle linee di rete. Tuttavia, esiste un’altra contromisura che esamineremo più in dettaglio di seguito. Se i disturbi penetrano attraverso la linea di alimentazione, è opportuno installare un filtro di rete sotto forma di filtro passa-basso (cfr. figura [ref:a_netzfilter] e figura [ref:a_netzfilter_draw]). Questi filtri sono disponibili come dispositivi pronti all’uso, nel rispetto delle norme VDE.

[question:AJ116]
[question:AJ117]
[question:AJ118]

<margin>
[photo:244:a_netzfilter:Filtro di rete]
[picture:367:a_netzfilter_draw:Circuito di un filtro di rete]
</margin>

I diversi metodi di trasmissione, a causa delle loro caratteristiche di modulazione, hanno effetti diversi in termini di interferenze su dispositivi e linee. In particolare, le modalità di modulazione CW e SSB (nelle quali l’ampiezza varia rapidamente) spesso causano interferenze nelle linee degli altoparlanti e una successiva rettificazione dell’alta frequenza (HF) nei tratti di base-emettitore della sezione audio degli amplificatori. La giunzione base-emettitore si comporta come un diodo e rettifica l’HF. Di conseguenza, l’audio demodulato diventa udibile negli altoparlanti.

[question:AJ107]
[question:AJ106]

Per proteggere i ricevitori DVB-T da segnali forti di un trasmettitore radioamatoriale VHF/UHF nelle immediate vicinanze, è necessario installare un filtro passa-alto nella linea di antenna del ricevitore DVB-T. Tuttavia, questo metodo è efficace solo con antenne riceventi passive. In particolare, gli amplificatori di antenna TV non selettivi vengono sovraeccitati rapidamente da segnali trasmittenti vicini, poiché amplificano un’ampia banda di frequenza. 
Nei casi di antenne riceventi attive, un filtro passa-alto deve essere installato prima dell’amplificatore di antenna.
Durante l’installazione dei filtri, è necessario considerare anche l’attenuazione di inserzione dei filtri nella banda passante. Questa deve essere il più bassa possibile e non superare $\qtyrange{2}{3}{\dB}$, per consentire al segnale ricevuto di passare il più possibile senza ostacoli.

[question:AJ113]
[question:AJ114]
[question:AJ108]

In generale, è opportuno installare un filtro passa-basso con una frequenza di taglio di $\qtyrange{30}{40}{\mega\hertz}$ dopo un trasmettitore ad onde corte potente. Anche l’utilizzo di un accordatore d’antenna in configurazione passa-basso (filtro Pi o LC) può garantire un effetto passa-basso che sopprime efficacemente le emissioni di armoniche.

[question:AJ112]
[question:AJ104]

Segnali trasmittenti forti di una stazione radioamatoriale possono causare disturbi di ricezione, rumori parassiti o interruzioni/artefatti/silenzi (in particolare nei ricevitori digitali come DAB/DVB-T) nei ricevitori DAB, TV e FM. Questi disturbi sono spesso provocati dalla sovraeccitazione dell’ingresso del ricevitore a causa di livelli di segnale elevati nel luogo di ricezione e portano a una riduzione della sensibilità del ricevitore o alla sovraeccitazione dello stadio di ingresso.

[question:AJ110]
[question:AJ111]
[question:AJ109]

Per evitare i problemi sopra menzionati, il radioamatore dovrebbe quindi utilizzare sempre solo la potenza di trasmissione minima necessaria per una comunicazione soddisfacente.

[question:AJ101]

Per disaccoppiare i disturbi di HF nei circuiti e nei dispositivi, vengono spesso utilizzati condensatori di disaccoppiamento. Questi devono essere in grado di deviare la HF verso massa in modo efficiente. A questo scopo, i condensatori ceramici sono particolarmente adatti. Sono invece inadeguati i condensatori elettrolitici e quelli a film plastico, poiché il loro avvolgimento interno conferisce loro un’elevata induttanza parassita. Nei condensatori al tantalio, per migliorare le proprietà di smaltimento della HF, viene spesso collegato in parallelo un condensatore ceramico, poiché questi ultimi da soli sono adatti solo per frequenze HF medie fino a circa $\qty{30}{\mega\hertz}$, mentre i condensatori ceramici possono smaltire frequenze molto più elevate.
Per smaltire efficacemente i disturbi di HF, è necessaria una messa a terra efficace con bassa impedenza.

[question:AJ119]
[question:AJ102]

Nelle linee di alimentazione dei stadi HF vengono spesso utilizzate le induttanze ad alta frequenza. Queste rappresentano un’impedenza longitudinale per l’alta frequenza e bloccano efficacemente le correnti entranti di HF negli stadi, nonché i flussi di ritorno di HF nell’alimentazione degli stadi.
A causa del loro avvolgimento, queste induttanze presentano anche capacità parassite, cosicché, in combinazione con la loro induttanza, formano punti di risonanza indesiderati (circuiti oscillanti). Ciò può portare a *risonanze parassite* negli stadi HF, che sono causate dalle *risonanze proprie* delle induttanze HF. Le risonanze parassite possono influenzare negativamente le caratteristiche degli stadi HF. Questo può portare a effetti di reazione indesiderati, in particolare negli amplificatori, nonché a cali nelle caratteristiche di potenza degli stadi HF.

[question:AJ214]