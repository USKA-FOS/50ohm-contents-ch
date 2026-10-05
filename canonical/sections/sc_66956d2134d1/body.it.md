La figura [ref:kanal] mostra un trasmettitore e un ricevitore, collegati tra loro tramite un canale. Ad esempio, a causa del tempo, di altre influenze atmosferiche o delle emissioni di altre stazioni, possono verificarsi interferenze sul canale. Queste possono portare a errori nella trasmissione.

<margin>
[picture:674:kanal:Kanal]
</margin>

A differenza della codifica di sorgente, la codifica di canale aggiunge intenzionalmente ridondanza all'informazione da trasmettere, ad esempio ripetizioni o checksum. A differenza della ridondanza rimossa nella codifica di sorgente, questa ridondanza aggiunta sistematicamente può essere utilizzata per il rilevamento o la correzione automatica degli errori di trasmissione.

---

La figura [ref:kanalcodierer] mostra un simbolo per un codificatore di canale. Il blocco rappresenta l'aggiunta di ridondanza ai dati.

<margin>
[picture:676:kanalcodierer:Kanalcodierer]
</margin>

[question:AE409]

Distinguiamo due tipi di codifica di canale:

* Rilevamento degli errori: È possibile rilevare che si è verificato un errore durante la trasmissione e quindi richiedere, ad esempio, una ritrasmissione.
* Correzione degli errori in avanti: Gli errori che si verificano durante la trasmissione vengono corretti presso il ricevitore con l'aiuto della ridondanza.

Nelle due sezioni seguenti [sec:fehlererkennung] e [sec:fehlerkorrektur] esamineremo più da vicino questi due tipi.