La *Automatic-Level-Control (ALC)* regola la modulazione dell’**uscita del trasmettitore** dell’apparato radio e riduce l’**ampiezza** del **segnale** nel **ramo di trasmissione** in caso di **sovraeccitazione**. In questo contesto, l’ALC non va confusa con l’AGC (*Automatic-Gain-Control*), che opera nel **ramo di ricezione** (vedi figura [ref:e_alc]).

<margin>
[picture:914:e_alc:Automatic-Level-Control in un trasmettitore]
</margin>

L’ALC rileva la **potenza d’uscita** dell’**uscita del trasmettitore** e la confronta con un valore massimo preimpostato. Se questo limite viene superato, l’ALC invia una tensione di regolazione allo stadio amplificatore RF a monte nel **ramo di trasmissione**, riducendo così l’**ampiezza** del **segnale** di trasmissione.

Finché la **visualizzazione** dell’ALC non reagisce, si può assumere che la regolazione non intervenga e che il **trasmettitore** non sia **sovramodulato** da un **segnale BF** troppo forte. Non appena la **visualizzazione** dell’ALC reagisce, si può dedurre che la regolazione, almeno in parte, è attiva.

Nelle trasmissioni in SSB, un leggero intervento dell’ALC è addirittura auspicabile, poiché consente di compensare le fluttuazioni di volume della voce e di sfruttare al meglio la **potenza di trasmissione** disponibile. Molti **trasmettitore-ricevitore** dispongono di una **visualizzazione** dell’ALC, che di solito indica fino a quale **grado** l’ALC può reagire (zona verde) e da quale **grado** in poi si verifica una **sovramodulazione** troppo forte che l’ALC non può più compensare senza distorsioni (zona rossa).

<margin>
[picture:915:e_alc_trx:ALC nel display di un apparato radio]
</margin>

<tip>
In pratica, è possibile trovare il punto ottimale in cui l’ALC non interviene ancora aumentando lentamente la modulazione **BF** fino al punto in cui l’ALC reagisce. Successivamente, si riduce leggermente la modulazione **BF** in modo che l’ALC non reagisca più e la **visualizzazione** della **potenza di trasmissione** mostri ancora la **potenza d’uscita** desiderata (eventualmente leggermente inferiore).
</tip>

---

Nelle trasmissioni con metodi di trasmissione digitali come FT8 o WSPR, l’intervento dell’ALC è spesso un’indicazione che il **segnale audio** proveniente dal PC è troppo forte e **sovramodulato**. Ciò può causare **splatter** indesiderati sulla **banda**. Pertanto, in questi metodi di trasmissione, il **segnale audio** deve essere sempre controllato con attenzione.

<indepth>
Il [manuale](https://wsjt.sourceforge.io/wsjtx-main_en.html#TRANSCEIVER) del software WSJT-X fornisce una buona raccomandazione: come primo passo, premendo il **tasto** TUNE si deve attivare la modalità di trasmissione del **trasmettitore-ricevitore** per generare un tono uniforme. Questo tono può essere verificato tramite la funzione di monitoraggio dell’apparecchio ascoltando o controllando visivamente nel waterfall del **trasmettitore-ricevitore**. Non devono verificarsi distorsioni, clic o altri disturbi. Successivamente, si regola il comando PWR dal suo massimo verso il basso finché l’**uscita HF** del **trasmettitore** non diminuisce leggermente: questo è generalmente considerato un buon livello per la modulazione **BF**. Anche la **visualizzazione** dell’ALC e la **potenza d’uscita** del **trasmettitore-ricevitore** possono aiutare a trovare il livello ottimale del **segnale audio**.
</indepth>

[question:EF305]