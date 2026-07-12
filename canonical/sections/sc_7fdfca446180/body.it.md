Nella sezione seguente vengono descritti i singoli passaggi di una catena di trasmissione e ricezione. La figura [ref:a_sdr_sender] mostra un esempio di trasmettitore SDR per la comunicazione vocale. Nel primo passaggio, il segnale del microfono viene digitalizzato da un convertitore A/D. Il segnale digitale viene quindi compresso da un codificatore di sorgente per ridurre la larghezza di banda necessaria. Nel passaggio successivo, un codificatore di canale aggiunge deliberatamente ridondanza al segnale compresso, in modo che gli errori di trasmissione possano essere rilevati e corretti. I dati codificati vengono infine convertiti in simboli da un mapper e quindi modulati da un modulatore I/Q, che verrà trattato più in dettaglio in un capitolo successivo. La catena di trasmissione si conclude con un amplificatore di potenza e l'antenna, attraverso cui viene irradiato il segnale.

<margin>
[picture:1062:a_sdr_sender:Trasmettitore SDR per comunicazione vocale]
</margin>

I blocchi evidenziati in blu nella figura [ref:a_sender] rappresentano i passaggi di elaborazione del segnale che possono essere implementati, ad esempio, puramente via software o con l'aiuto di un FPGA. L'ordine di questi passaggi di elaborazione per un trasmettitore è sempre il seguente e dovrebbe essere ben memorizzato per le domande d'esame:

1. Codificatore di sorgente: Compressione dei dati
2. Codificatore di canale: Aggiunta di ridondanza per il rilevamento e la correzione degli errori
3. Mapper: Mappatura dei dati binari su simboli, ad esempio ampiezza e fase per QAM

[question:AF626]
[question:AF627]

---

Per un ricevitore, il processo funziona al contrario: l'antenna riceve il segnale, che viene amplificato da un amplificatore di potenza. Successivamente, avviene la demodulazione tramite un demodulatore I/Q per estrarre i simboli. Il de-mapper riassegna questi simboli ai dati binari originali. Dopodiché, il decodificatore di canale si occupa di rilevare e correggere gli errori che potrebbero essersi verificati durante la trasmissione. Infine, il decodificatore di sorgente decomprime i dati per ripristinare il segnale originale, che viene poi riconvertito in un segnale analogico tramite un convertitore D/A e emesso, ad esempio, tramite un amplificatore a un altoparlante.

Riassumiamo l'elaborazione digitale del segnale nel ricevitore nei seguenti tre passaggi:

1. De-mapper: Mappatura dei simboli su dati binari
2. Decodificatore di canale: Rilevamento e correzione degli errori
3. Decodificatore di sorgente: Decompressione dei dati

<margin>
[picture:1063:a_sdr_empfänger:Ricevitore SDR per comunicazione vocale]
</margin>

[question:AF628]
[question:AF629]
