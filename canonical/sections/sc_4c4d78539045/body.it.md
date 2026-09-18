È possibile distribuire un flusso di dati su più portanti che si trovano su frequenze diverse ma vicine. Tuttavia, le portanti non possono essere posizionate arbitrariamente vicine tra loro, poiché generano inevitabilmente bande laterali che occupano una certa larghezza di banda.

Nella tecnica di multiplazione di frequenza ortogonale (Orthogonal Frequency-Division Multiplexing, OFDM), le singole portanti vengono posizionate esattamente alla distanza necessaria per minimizzare il disturbo reciproco (il cosiddetto "diafonia").

Maggiore è la velocità di simbolo per portante, maggiore deve essere la distanza tra le portanti. Per questo motivo, si sceglie spesso una velocità di simbolo più bassa per ogni singola portante, in modo da poter utilizzare un numero maggiore di portanti. La quantità di informazioni trasmesse rimane invariata, poiché, sebbene ogni portante trasmetta meno informazioni, è possibile utilizzare più portanti affiancate. Un maggiore distanziamento delle portanti è utile, ad esempio, per rendere il segnale più tollerante agli errori di frequenza, dovuti a deviazioni di frequenza tra trasmettitore e ricevitore o a spostamenti Doppler in caso di trasmettitori o ricevitori in movimento.

Un vantaggio di questo approccio risiede nel fatto che disturbi a banda stretta influenzano solo una o poche portanti. In combinazione con tecniche di correzione degli errori che prevedono una trasmissione ridondante dei dati, appresi in alcuni capitoli precedenti, è possibile ottenere una trasmissione senza errori nonostante la presenza di disturbi a banda stretta.

<margin>
[picture:704:ofdm:Spettro di frequenza di un segnale OFDM semplice]
</margin>

[question:AE421]

Un ulteriore vantaggio deriva dalla minore velocità di simbolo di ogni singola portante. Grazie alla minore velocità di simbolo, la durata di ogni simbolo è più lunga. In caso di ritardi temporali dovuti alla propagazione per cammini multipli, la sovrapposizione tra i segnali (il cosiddetto *interferenza intersimbolica* o *diafonia tra simboli*) risulta minore. Può anche verificarsi che alcune frequenze vengano annullate o almeno fortemente attenuate a causa della propagazione per cammini multipli (fenomeno noto come *fading selettivo in frequenza*). Questo può essere compensato con gli stessi meccanismi utilizzati per i disturbi a banda stretta menzionati in precedenza. In caso di propagazione per cammini multipli, l'OFDM risulta particolarmente vantaggioso.

[question:AE422]