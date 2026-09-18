La figura [ref:kanal] mostra un trasmettitore e un ricevitore collegati tra loro tramite un canale. A causa di condizioni meteorologiche, altri influssi atmosferici o trasmissioni di altre stazioni, possono verificarsi disturbi sul canale. Questi possono portare a errori nella trasmissione.

<margin>
[picture:674:kanal:Canale]
</margin>

A differenza della codifica della sorgente, la codifica del canale aggiunge deliberatamente ridondanza alle informazioni da trasmettere, ad esempio ripetizioni o checksum. A differenza della ridondanza rimossa durante la codifica della sorgente, questa ridondanza aggiunta sistematicamente può essere utilizzata per il rilevamento automatico o la correzione degli errori di trasmissione.

---

La figura [ref:kanalcodierer] mostra un simbolo per un codificatore di canale. Il blocco rappresenta l'aggiunta di ridondanza ai dati.

<margin>
[picture:676:kanalcodierer:Codificatore di canale]
</margin>

[question:AE409]

Distinguiamo due tipi di codifica del canale:

* Rilevamento degli errori: è possibile rilevare che si è verificato un errore durante la trasmissione e, ad esempio, richiedere una nuova trasmissione.
* Correzione degli errori in avanti: gli errori che si verificano durante la trasmissione vengono corretti dal ricevitore con l'aiuto della ridondanza.

Nei paragrafi seguenti esamineremo più da vicino questi due tipi.