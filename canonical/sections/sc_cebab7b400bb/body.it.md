Nella sezione [sec:stoerungen_elektronischer_geraete_1] abbiamo già conosciuto i tipici disturbi dei dispositivi e degli impianti elettronici – ad esempio attraverso l'irradiazione diretta nel telaio o attraverso l'accoppiamento nei cavi di alimentazione – nonché le appropriate contromisure e comportamenti. In questa sezione approfondiremo ulteriormente questi aspetti.

[question:AJ105]

Se nei ricevitori digitali autocostruiti si verificano disturbi di ricezione, una possibile causa potrebbe essere una schermatura insufficiente del ricevitore. In questo caso è consigliabile montare il circuito stampato del ricevitore in un telaio metallico collegato a massa. Soprattutto per i ricevitori SDR o le soluzioni autocostruite in tecnologia SDR, una buona schermatura è assolutamente necessaria per evitare l'irradiazione. Viceversa, anche le indesiderate emissioni da questi dispositivi vengono ridotte.

[question:AJ103]

---

Nella sezione [sec:stoerungen_vermeiden] ci siamo già occupati degli accoppiamenti nelle linee di rete. Tuttavia, esiste un'ulteriore contromisura che esamineremo più in dettaglio di seguito. Se i disturbi entrano attraverso il cavo di alimentazione, è consigliabile installare un filtro di rete sotto forma di un filtro passa-basso (cfr. figura [ref:a_netzfilter] e figura [ref:a_netzfilter_draw]). Questi filtri sono disponibili come dispositivi già pronti, nel rispetto delle normative VDE.

[question:AJ116]
[question:AJ117]
[question:AJ118]

<margin>
[photo:244:a_netzfilter:Filtro di rete]
[picture:367:a_netzfilter_draw:Circuito di un filtro di rete]
</margin>

Diverse tecniche di trasmissione hanno, a causa delle loro caratteristiche di modulazione, effetti differenti riguardo ai disturbi di dispositivi e cavi. In particolare, i tipi di modulazione CW e SSB (in cui l'ampiezza cambia rapidamente) spesso causano disturbi nei cavi degli altoparlanti e una conseguente rettifica dell'alta frequenza nelle giunzioni base-emettitore nella parte BF degli amplificatori. La giunzione base-emettitore si comporta in questo caso come un diodo e raddrizza l'alta frequenza. Ciò rende udibile la BF demodulata negli altoparlanti.

[question:AJ107]
[question:AJ106]

Per proteggere i ricevitori DVB-T da segnali forti di un trasmettitore radioamatoriale VHF/UHF nelle immediate vicinanze, dovrebbe essere installato un filtro passa-alto nel cavo dell'antenna del ricevitore DVB-T. Tuttavia, questo è efficace solo con antenne riceventi passive. In particolare, i preamplificatori d'antenna TV non selettivi vengono rapidamente sovramodulati da segnali trasmessi vicini, poiché amplificano un'ampia banda di frequenza.
Con le antenne riceventi attive, un filtro passa-alto deve essere installato prima del preamplificatore d'antenna dell'antenna.
Quando si installano filtri, bisogna anche considerare l'attenuazione di inserzione dei filtri nella banda passante. Questa dovrebbe essere il più bassa possibile e non superare $\qtyrange{2}{3}{\dB}$ per permettere al segnale ricevuto desiderato di passare il più liberamente possibile.

[question:AJ113]
[question:AJ114]
[question:AJ108]

In generale, ha senso installare dietro un forte trasmettitore in onde corte un filtro passa-basso con una frequenza di taglio di $\qtyrange{30}{40}{\mega\hertz}$. Anche utilizzando un accordatore d'antenna in configurazione passa-basso (filtro Pi o LC) si può ottenere un effetto passa-basso che sopprime efficacemente le emissioni di armoniche.

[question:AJ112]
[question:AJ104]

Forti segnali trasmessi da una stazione radioamatoriale possono causare nei ricevitori DAB, TV e FM disturbi di ricezione, rumori parassiti o interruzioni/artefatti/silenzi (specialmente nei ricevitori digitali come DAB/DVB-T). Questi disturbi sono spesso causati dalla sovraeccitazione dell'ingresso del ricevitore dovuta ad alte intensità di segnale nel luogo di ricezione e portano a una riduzione della sensibilità del ricevitore o alla sovraeccitazione dello stadio d'ingresso del ricevitore.

[question:AJ110]
[question:AJ111]
[question:AJ109]

Per evitare i problemi sopra menzionati, il radioamatore dovrebbe quindi sempre operare solo con la potenza di trasmissione minima necessaria per una comunicazione soddisfacente.

[question:AJ101]

Per disaccoppiare i disturbi ad alta frequenza nei circuiti e nei dispositivi, vengono spesso utilizzati condensatori di disaccoppiamento. Questi devono avere la proprietà di deviare l'alta frequenza verso massa nel modo più efficiente possibile. A questo scopo, i condensatori in ceramica sono particolarmente adatti. I condensatori elettrolitici e quelli a film plastico sono inadatti, poiché a causa della loro struttura avvolta possiedono un'elevata induttanza propria. Con i condensatori al tantalio, spesso viene collegato in parallelo un condensatore in ceramica a causa delle migliori proprietà di deviazione dell'alta frequenza, poiché questi da soli sono adatti solo per frequenze ad alta frequenza medie fino a circa $\qty{30}{\mega\hertz}$ e i condensatori in ceramica possono disaccoppiare frequenze molto più elevate.
Per deviare efficacemente i disturbi ad alta frequenza, deve essere presente una messa a massa efficace con bassa impedenza.

[question:AJ119]
[question:AJ102]

Nei cavi di alimentazione degli stadi ad alta frequenza vengono spesso utilizzati induttori per alta frequenza. Questi rappresentano un'impedenza longitudinale per l'alta frequenza e bloccano efficacemente le correnti entranti ad alta frequenza negli stadi, così come i riflussi ad alta frequenza nell'alimentazione elettrica degli stadi.
A causa della struttura avvolta, questi induttori hanno anche capacità proprie, così che in combinazione con la loro induttanza formano punti di risonanza indesiderati (circuiti oscillanti). Ciò può causare negli stadi ad alta frequenza *risonanze parassite* indesiderate, provocate dalle *risonanze proprie* degli induttori ad alta frequenza. Le risonanze parassite possono influenzare negativamente le caratteristiche degli stadi ad alta frequenza. Ciò può portare a effetti di retroazione indesiderati, specialmente negli amplificatori, nonché a cali nelle caratteristiche di potenza degli stadi ad alta frequenza.

[question:AJ214]
