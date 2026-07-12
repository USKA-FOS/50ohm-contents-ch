Il *Controllo Automatico del Livello (ALC)* regola la modulazione dello stadio finale del trasmettitore dell'apparecchio radio e riduce l'ampiezza del segnale nel ramo di trasmissione in caso di sovraeccitazione. L'ALC non deve essere confusa con l'AGC (Automatic-Gain-Control), che si trova nel ramo del ricevitore (vedi figura [ref:e_alc]).

<margin>
[picture:914:e_alc:Controllo Automatico del Livello in un trasmettitore]
</margin>

L'ALC rileva la potenza d'uscita dello stadio finale del trasmettitore e la confronta con un valore massimo predefinito. Se questo valore limite viene superato, l'ALC invia una corrispondente tensione di controllo allo stadio amplificatore HF a monte nel ramo di trasmissione, riducendo così l'ampiezza del segnale di trasmissione.

Finché l'indicatore ALC non si attiva, si può presumere che la regolazione non intervenga e che il trasmettitore non sia sovraeccitato da un segnale audio troppo forte. Non appena l'indicatore ALC reagisce, si può presumere che la regolazione, almeno parzialmente, diventi attiva.

Nelle trasmissioni SSB, un leggero intervento dell'ALC è del tutto desiderabile, poiché compensa le fluttuazioni di volume della voce e consente un utilizzo ottimale della potenza di trasmissione disponibile. Molti trasmettitori-ricevitori dispongono di un apposito indicatore ALC, che solitamente mostra fino a che punto l'ALC può reagire (area verde) e da quale area si verifica una sovraeccitazione che l'ALC non può più compensare senza distorsioni (area rossa).

<margin>
[picture:915:e_alc_trx:ALC nel display di un apparecchio radio]
</margin>

<tip>
In pratica, è possibile trovare il punto ottimale in cui l'ALC non interviene ancora, aumentando lentamente la modulazione audio fino al punto in cui l'ALC si attiva. Successivamente, si riduce nuovamente un po' la modulazione audio, in modo che l'ALC non intervenga più e l'indicatore di potenza di trasmissione mostri ancora la potenza d'uscita desiderata (eventualmente leggermente inferiore).
</tip>

---

Nelle trasmissioni con metodi di trasmissione digitale come FT8 o WSPR, l'intervento dell'ALC è spesso un segnale che il segnale audio dal PC è troppo forte e viene sovraeccitato. Ciò può causare uno *splatter* indesiderato sulla banda. Pertanto, il segnale audio in questi metodi di trasmissione dovrebbe sempre essere controllato attentamente.

<indepth>
Il [manuale](https://wsjt.sourceforge.io/wsjtx-main_en.html#TRANSCEIVER) del software WSJTX fornisce una buona raccomandazione a riguardo: nel primo passaggio, si dovrebbe mettere il trasmettitore-ricevitore in modalità di trasmissione premendo il tasto TUNE per generare un tono uniforme. Questo tono può essere verificato ascoltandolo tramite la funzione monitor dell'apparecchio o controllato visivamente nella cascata del TRX. Non dovrebbero verificarsi distorsioni, clic o altri disturbi. Successivamente, si regola lentamente il controllo PWR dal suo massimo verso il basso finché l'uscita RF del trasmettitore non diminuisce leggermente – questo è generalmente considerato un buon livello per la modulazione audio. Anche l'indicatore ALC e la potenza d'uscita del trasmettitore-ricevitore possono aiutare a trovare il livello ottimale del segnale audio.
</indepth>

[question:EF305]
