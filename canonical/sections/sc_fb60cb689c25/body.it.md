---

Molti apparecchi radio dispongono di una cosiddetta **porta DATA**, spesso indicata come *DATA* o *$\qty{9600}{\baud}$*, come mostrato nella figura [ref:e_9600_port]. Questa porta è stata originariamente sviluppata per applicazioni Packet-Radio, oggi in gran parte sostituite da HAMNET. Tuttavia, può essere utilizzata anche per altri metodi, ad esempio per il sistema di trasmissione digitale vocale M17. In questo caso, si collega un modem corrispondente, spesso indicato anche come TNC, come illustrato nella figura [ref:m17_tnc].

<margin>
[photo:303:e_9600_port:Apparecchio radio con porta DATA]
[photo:185:m17_tnc:Modulo M17, un TNC per il sistema di trasmissione M17]
</margin>

La porta $\qty{9600}{\baud}$ offre una connessione diretta al modulatore e al demodulatore del trasmettitore-ricevitore, consentendo di elaborare i segnali con elevata precisione e basse distorsioni. Per velocità di trasmissione dati più elevate, come quelle utilizzate nei segnali digitali ad esempio nel Packet-Radio a $\qty{9600}{\baud}$ (protocollo AX.25), è necessario bypassare l'intero percorso audio con la sua risposta in frequenza limitata e i suoi filtri (ad esempio il filtro del microfono e il preamplificatore). Il percorso audio di un trasmettitore-ricevitore è generalmente sintonizzato per i segnali vocali e ha una larghezza di banda limitata, che spesso si attesta tra $\qty{300}{\hertz}$ e $\qty{3000}{\hertz}$. Questa larghezza di banda non è sufficiente per trasmettere in modo affidabile $\qty{9600}{\baud}$, poiché un tasso così elevato richiede una larghezza di banda del segnale maggiore. Attraverso la porta dati, i segnali vengono trasmessi senza i filtri, l'elaborazione DSP e il processo di de-enfasi presenti nel percorso audio. Questo riduce distorsioni e latenze, fondamentale per le trasmissioni digitali al fine di minimizzare il tasso di errore.

In sintesi: la porta $\qty{9600}{\baud}$ è specificamente progettata per elaborare dati digitali direttamente, senza i vincoli del percorso audio, il che è necessario per una trasmissione dati digitale ad alta velocità affidabile ed efficiente.


---

Nei quesiti seguenti viene utilizzato un trasmettitore-ricevitore FM. Per la trasmissione, la porta DATA deve essere collegata prima del modulatore FM, mentre per la ricezione deve essere collegata dopo il demodulatore FM.

[question:EF309]
[question:EF219]

<indepth>
Perché proprio $\qty{9600}{\baud}$?

$\qty{9600}{\baud}$ ($\qty{9,6}{\kilo\bit\per\second}$ se si utilizza una modulazione con un bit per simbolo) è una velocità comune per le comunicazioni digitali nel radioamatoriale, in particolare nel Packet-Radio. Questo tasso di trasmissione rappresenta un compromesso tra velocità raggiungibile e fattibilità tecnica nella banda VHF/UHF, dove operano la maggior parte dei trasmettitori-ricevitori FM.
</indepth>