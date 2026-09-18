Nel seguente paragrafo vengono descritti i singoli passaggi di una catena di trasmissione e ricezione. La figura [ref:a_sdr_sender] mostra ad esempio un trasmettitore SDR per comunicazioni vocali. Nel primo passaggio, il segnale del microfono viene digitalizzato tramite un convertitore analogico-digitale. Successivamente, il segnale digitale viene compresso da un codificatore di sorgente per ridurre la larghezza di banda necessaria. Nel passaggio successivo, un codificatore di canale aggiunge al segnale compresso una ridondanza mirata, in modo da poter rilevare e correggere eventuali errori di trasmissione. I dati codificati vengono infine convertiti in simboli da un mapper e modulati tramite un modulatore I/Q. La catena di trasmissione si conclude con un amplificatore di potenza e l'antenna, tramite la quale il segnale viene irradiato.

<margin>
[immagine:1062:a_sdr_sender:Trasmettitore SDR per comunicazioni vocali]
</margin>

I blocchi evidenziati in blu nella figura [ref:a_sdr_sender] rappresentano i passaggi di elaborazione del segnale che possono essere implementati, ad esempio, esclusivamente via software o tramite un FPGA. L'ordine di questi passaggi di elaborazione per un trasmettitore è sempre il seguente e dovrebbe essere ben memorizzato per le domande d'esame:

1. Codificatore di sorgente: compressione dei dati
2. Codificatore di canale: aggiunta di ridondanza per il rilevamento e la correzione degli errori
3. Mapper: mappatura dei dati binari su simboli, ad esempio ampiezza e fase per la QAM

[question:AF626]
[question:AF627]

---

Per un ricevitore, il processo funziona al contrario: l'antenna riceve il segnale, che viene amplificato da un amplificatore di potenza. Successivamente avviene la demodulazione tramite un demodulatore I/Q per estrarre i simboli. Il de-mapper associa questi simboli ai dati binari originali. Successivamente, il decodificatore di canale si occupa di rilevare e correggere eventuali errori verificatisi durante la trasmissione. Infine, il decodificatore di sorgente decomprime i dati per ricostruire il segnale originale, che viene poi convertito in un segnale analogico tramite un convertitore digitale-analogico e, ad esempio, inviato a un altoparlante tramite un amplificatore.

Riassumiamo l'elaborazione digitale del segnale nel ricevitore nei seguenti tre passaggi:

1. De-mapper: conversione dei simboli in dati binari
2. Decodificatore di canale: rilevamento e correzione degli errori
3. Decodificatore di sorgente: decompressione dei dati

<margin>
[immagine:1063:a_sdr_empfänger:Ricevitore SDR per comunicazioni vocali]
</margin>

[question:AF628]
[question:AF629]
