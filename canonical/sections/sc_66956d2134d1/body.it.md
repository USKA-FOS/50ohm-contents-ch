La figura [ref:kanal] mostra un trasmettitore e un ricevitore collegati tra loro tramite un canale. Ad esempio, a causa del tempo, di altre influenze atmosferiche o delle trasmissioni di altre stazioni, possono verificarsi disturbi sul canale. Questi possono portare a errori nella trasmissione. 

<margin>
[picture:674:kanal:Kanal]
</margin>

A differenza della codifica sorgente, la codifica di canale aggiunge deliberatamente ridondanza all'informazione da trasmettere, ad esempio ripetizioni o somme di controllo. A differenza della ridondanza rimossa nella codifica sorgente, questa ridondanza aggiunta sistematicamente può essere utilizzata per il rilevamento o la correzione automatica degli errori di trasmissione.

---

La figura [ref:kanalcodierer] mostra un simbolo per un codificatore di canale. Il blocco rappresenta l'aggiunta di ridondanza ai dati.

<margin>
[picture:676:kanalcodierer:Kanalcodierer]
</margin>

[question:AE409]

Distinguamo due tipi di codifica di canale:

* Rilevamento errori: Si può rilevare che si è verificato un errore durante la trasmissione e quindi richiedere, ad esempio, una ritrasmissione.
* Correzione errori in avanti: Gli errori che si verificano durante la trasmissione vengono corretti dal ricevitore con l'aiuto della ridondanza. 

Di seguito esamineremo più da vicino questi due tipi.