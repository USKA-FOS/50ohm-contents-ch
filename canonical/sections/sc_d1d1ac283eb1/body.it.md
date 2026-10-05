Nella sezione [sec:dynamik_kompressor_1] abbiamo già conosciuto il *Dynamic Compressor*. Un segnale vocale BF presenta, a causa dei diversi livelli di volume durante la parlata, grandi fluttuazioni tra ampiezze di segnale piccole e grandi. Questo intervallo è chiamato *gamma dinamica*. Un *compressore dinamico BF o processore vocale BF* funziona come processore vocale per la riduzione della gamma dinamica nella modulazione: le parti forti del segnale vengono amplificate meno rispetto alle parti più deboli, in modo che le differenze tra di esse diventino minori. Successivamente, il livello complessivo può essere aumentato (cfr. figura [ref:a_kompressor]).

In questo modo aumenta il livello medio del segnale vocale e quindi anche il livello medio di trasmissione, senza che la potenza di picco debba essere aumentata di conseguenza. In questo modo, la potenza di trasmissione media può essere aumentata con poca distorsione. Un compressore dinamico viene quindi spesso utilizzato nelle connessioni DX e nei contest, dove un segnale forte e ben comprensibile è particolarmente importante.

[question:AE210]
[question:AE211]

<margin>
[picture:1043:a_kompressor:Funzionamento di un compressore]
</margin>

Tuttavia, quando si utilizza un compressore vocale, si dovrebbe prestare attenzione a evitare una compressione troppo elevata. Una compressione troppo forte può rendere il segnale vocale innaturale e meno comprensibile. Se il processore vocale o gli stadi successivi vengono sovramodulati, possono inoltre verificarsi distorsioni e un allargamento del segnale trasmesso (*splatter*). Pertanto, la compressione dovrebbe essere aumentata solo fino al punto in cui il segnale rimane pulito e ben comprensibile.

[question:AE212]

<tip>
Per una regolazione ottimale del Dynamic Compressor, si dovrebbe procedere come segue:
  1. Regolare il guadagno del microfono senza attivare il Dynamic Compressor, in modo che il misuratore ALC del transceiver inizi appena a rispondere o si trovi nel suo intervallo di regolazione.
  2. Attivare gradualmente il Dynamic Compressor e verificare la comprensibilità e la chiarezza del segnale, ad esempio attraverso un QSO con una stazione corrispondente e un rapporto sulla comprensibilità e qualità del segnale. In alternativa, alcuni dispositivi dispongono di una funzione di monitoraggio, in modo che il segnale trasmesso possa essere ascoltato anche tramite questa funzione. Anche con un 2° ricevitore e terminando il trasmettitore con un carico fittizio, il segnale trasmesso può essere ascoltato. In questo modo si evitano anche disturbi ad altre stazioni causati da trasmissioni di prova.
</tip>
