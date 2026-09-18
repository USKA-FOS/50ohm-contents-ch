<margin>
[picture:911:e_digitale_signalverarbeitung_blockschaltbild:Principio dell'elaborazione digitale del segnale]
</margin>

Negli ultimi 25 anni il mondo ha subito una trasformazione tecnologica massiccia. La potenza di calcolo dei computer è aumentata di molte volte e sempre più compiti nei dispositivi tecnici vengono eseguiti da microchip su uno spazio ridottissimo. Nei prossimi anni questa evoluzione continuerà a ritmo serrato. Tutto ciò sta cambiando il modo in cui i dispositivi, in particolare l'elaborazione dei segnali nei moderni apparecchi radio, vengono realizzati. L'elaborazione digitale del segnale è ormai uno standard tecnologico e ogni apparecchio moderno si basa su questa tecnologia. In questo contesto, i processori digitali di segnale e il principio fondamentale dell'elaborazione digitale del segnale svolgono un ruolo essenziale.

L'elaborazione digitale del segnale non si trova solo nel campo della tecnica radio. Molti dispositivi, siano essi telefoni cellulari, impianti stereo, sistemi di imaging in ambito medico e praticamente tutte le moderne applicazioni radio beneficiano di questa tecnica affascinante, che consente di realizzare funzioni e possibilità mai viste prima in questi dispositivi a costi contenuti.

Nel campo della tecnica radio, i dispositivi che elaborano i segnali mediante elaborazione digitale del segnale sono chiamati apparecchi SDR. In questi dispositivi almeno una parte dell'elaborazione del segnale è realizzata tramite software.

[question:EF603]

Per poter elaborare digitalmente i segnali analogici continui, questi devono essere prima campionati e convertiti in valori digitali tramite un convertitore analogico-digitale (A/D). Si parla in questo caso di digitalizzazione del segnale analogico di ingresso.

[question:EF602]

---
<margin>
[picture:411:e_digitale_signalverarbeitung:Rappresentazione semplificata di un'onda sinusoidale composta da $\num{16}$ campioni e $\num{7}$ valori]
</margin>

In questo processo, il segnale analogico viene campionato a intervalli di tempo fissi e mappato in un intervallo di valori digitali (ad esempio da $\num{-128}$ a $\num{+127}$). Ogni valore rappresenta una determinata tensione del segnale misurata, dove generalmente ai valori negativi vengono associate tensioni negative e ai valori positivi tensioni positive. Si può paragonare questo processo, ad esempio, a una telecamera che scatta immagini di una scena a intervalli di tempo fissi. Le immagini acquisite hanno sempre una distanza temporale fissa rispetto all'immagine precedente e successiva e rappresentano la scena momentanea in piccoli intervalli di tempo. Questo processo è chiamato *sampling* (in italiano si potrebbe tradurre con "campionamento"). I singoli valori di tensione del segnale misurati vengono chiamati *samples*. Nel prossimo paragrafo esamineremo questo processo più nel dettaglio.

Dopo la conversione A/D, i *samples* disponibili come valori digitali possono essere elaborati ulteriormente tramite l'elaborazione digitale del segnale.

Successivamente, per la riproduzione tramite altoparlante o per l'emissione tramite antenna, si desidera convertire i segnali elaborati digitalmente in un segnale analogico. Per questo scopo, è necessario un convertitore digitale-analogico (D/A), che rappresenta in pratica l'opposto del convertitore A/D descritto in precedenza. Il convertitore D/A converte i valori digitali in valori di tensione analogici e consente così la ricostruzione di un segnale analogico dai valori digitali.

[question:EF601]