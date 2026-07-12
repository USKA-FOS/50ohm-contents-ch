---

Molti apparecchi radio dispongono di una cosiddetta porta DATA, spesso contrassegnata anche come *DATA* o *$\qty{9600}{\baud}$*, come mostrato nella figura [ref:e_9600_port]. Questa porta è stata originariamente sviluppata per applicazioni Packet-Radio, che oggi sono state in gran parte sostituite da HAMNET. Ciononostante, questa porta può essere utilizzata anche per altre procedure, ad esempio per la procedura di trasmissione vocale digitale M17. In questo caso, viene collegato un modem appropriato, spesso chiamato anche TNC, come mostrato nella figura [ref:m17_tnc].

<margin>
[photo:303:e_9600_port:Apparecchio radio con porta DATA]
[photo:185:m17_tnc:Modulo M17 un TNC per la procedura di trasmissione M17]
</margin>

La porta $\qty{9600}{\baud}$ offre una connessione diretta al modulatore e al demodulatore del trasmettitore-ricevitore, per elaborare i segnali con alta precisione e basse distorsioni. Per velocità di trasmissione dati più elevate, come quelle utilizzate nei segnali digitali, ad esempio nel Packet-Radio $\qty{9600}{\baud}$ (protocollo AX.25), è necessario bypassare l'intero percorso audio con le sue limitate risposte in frequenza e filtri (ad esempio, filtro microfonico e preamplificatore). Il percorso audio di un trasmettitore-ricevitore è normalmente ottimizzato per segnali vocali e ha una larghezza di banda limitata, spesso compresa tra $\qty{300}{\hertz}$ e $\qty{3000}{\hertz}$. Questa larghezza di banda non è sufficiente per trasmettere in modo affidabile $\qty{9600}{\baud}$, poiché una velocità così elevata richiede una maggiore larghezza di banda del segnale. Tramite la porta dati, i segnali vengono trasmessi senza i filtri, l'elaborazione DSP e il processo di de-enfasi presenti nel percorso audio. Ciò riduce le distorsioni e le latenze, che sono critiche per le trasmissioni digitali al fine di minimizzare il tasso di errore. 

In sintesi: la porta $\qty{9600}{\baud}$ è specificamente progettata per elaborare dati digitali direttamente e senza le limitazioni del percorso audio, il che è necessario per una trasmissione dati ad alta velocità affidabile ed efficiente.


---

Nelle seguenti domande verrà utilizzato un trasmettitore-ricevitore FM. Per la trasmissione, la porta DATA deve essere collegata prima del modulatore FM e, per la ricezione, dopo il demodulatore FM.

[question:EF309]
[question:EF219]

<indepth>
Perché proprio $\qty{9600}{\baud}$?
  
$\qty{9600}{\baud}$ ($\qty{9,6}{\kilo\bit\per\second}$, se si utilizza una modulazione con un bit per simbolo) è una velocità comune per la comunicazione digitale nel radioamatore, in particolare nel Packet-Radio. Questa velocità di trasmissione dati rappresenta un compromesso tra la velocità raggiungibile e la fattibilità tecnica nella gamma di frequenze VHF/UHF, dove operano la maggior parte dei trasmettitori-ricevitori FM.
</indepth>