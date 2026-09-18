*Convertitori* e *transverter* vengono utilizzati nel radioamatoriale per estendere, con apparecchi radio esistenti, le bande di frequenza che questi non coprono originariamente. Un *convertitore* converte il segnale solo in una direzione, sia nel percorso di trasmissione che in quello di ricezione. Un *trasmettitore-ricevitore* (transverter), invece, dispone di un sistema interno di commutazione tra trasmissione e ricezione e gestisce la conversione di frequenza sia in trasmissione che in ricezione. La conversione di frequenza nei convertitori e nei trasmettitori-ricevitori avviene sempre tramite miscelazione in uno o più mixer.

Ad esempio, con un trasmettitore-ricevitore adatto e un transceiver per onde corte esistente, è possibile operare anche nelle bande VHF/UHF/SHF. In questo caso, ad esempio, si potrebbe convertire la banda dei $\qty{10}{\metro}$ del transceiver per onde corte, tramite un trasmettitore-ricevitore, nelle bande $\qty{2}{\metro}$/$\qty{70}{\centi\metro}$ o $\qty{23}{\centi\metro}$ in entrambe le direzioni.

[question:EF501]
[question:EF502]

---

Consideriamo innanzitutto lo [schema a blocchi](#) di un convertitore nell’immagine [ref:e_konverter]. Un convertitore di questo tipo potrebbe essere utilizzato, ad esempio, per convertire un segnale da un apparecchio radio VHF per il satellite radioamatoriale QO-100, che richiede una frequenza di ingresso nella banda $\qty{2,4}{\giga\hertz}$. In questo caso, un trasmettitore-ricevitore potrebbe non essere necessario, poiché la ricezione avviene tramite una chiavetta SDR e un LNB.

Dallo schema a blocchi si evince che un intervallo di frequenza di ingresso definito viene convertito in un altro intervallo di frequenza di uscita tramite almeno un mixer. Non è prevista alcuna commutazione tra trasmissione e ricezione. Un convertitore può quindi convertire un segnale solo in una direzione, sia nel percorso di ricezione (RX) che in quello di trasmissione (TX). Nei convertitori per il funzionamento in trasmissione è spesso presente un controllo PTT che, in caso di trasmissione, attiva gli stadi amplificatori del convertitore.

La banda di frequenza in cui un convertitore converte il segnale può essere determinata calcolando la frequenza dell’oscillatore fornita al mixer e la frequenza di ingresso o di uscita. Nell’esempio concreto, la frequenza di destinazione risulta dal prodotto di miscelazione di
$\qty{144}{\mega\hertz} + \qty{2,256}{\giga\hertz} = \qty{2,4}{\giga\hertz}$,
dove il prodotto desiderato viene poi selezionato tramite filtri appropriati.

<margin>
[picture:651:e_konverter:Circuito del convertitore, ad esempio per QO-100]
</margin>

[question:EF504]

---

Il circuito di un trasmettitore-ricevitore si distingue chiaramente da quello di un convertitore. Le immagini [ref:e_transverter_rx] e [ref:e_transverter_tx] mostrano lo schema a blocchi di un trasmettitore-ricevitore che consente di operare nella banda $\qty{2}{\metro}$ utilizzando un transceiver per onde corte nella banda $\qty{10}{\metro}$. A tale scopo, vengono utilizzati una commutazione tra trasmissione e ricezione, due mixer e due percorsi di segnale separati: uno per la ricezione (RX) e uno per la trasmissione (TX).

Nel percorso TX, in trasmissione, il trasmettitore-ricevitore converte il segnale di uscita del transceiver nella banda di frequenza più alta desiderata, mentre nel percorso RX, in ricezione, converte il segnale proveniente dall’antenna nella banda di frequenza adatta al transceiver. La banda di frequenza tra cui opera il trasmettitore-ricevitore può essere determinata conoscendo la frequenza dell’oscillatore fornita ai mixer e le rispettive frequenze di ingresso e uscita. Queste relazioni sono illustrate nelle immagini.

L’oscillatore stabilizzato a quarzo ($G$) genera una frequenza di $\qty{38,666}{\mega\hertz}$, che viene moltiplicata per 3 tramite un moltiplicatore di frequenza 1:3 fino a $\qty{116}{\mega\hertz}$. In ricezione, illustrato nell’immagine [ref:e_transverter_rx], il segnale di ingresso dalla banda $\qtyrange{144}{146}{\mega\hertz}$ viene convertito nella banda $\qtyrange{28}{30}{\mega\hertz}$. In trasmissione, mostrato nell’immagine [ref:e_transverter_tx], il segnale di uscita dell’apparecchio radio dalla banda $\qtyrange{28}{30}{\mega\hertz}$ viene convertito nella banda $\qtyrange{144}{146}{\mega\hertz}$. Come di consueto, in entrambi i percorsi di segnale vengono utilizzati filtri appropriati per selezionare i prodotti di miscelazione desiderati, che per chiarezza non sono rappresentati nelle immagini.

[question:EF503]

<margin>
[picture:842:e_transverter_rx:Trasmettitore-ricevitore nel percorso RX]
[picture:843:e_transverter_tx:Trasmettitore-ricevitore nel percorso TX]
</margin>

<indepth>
*TCXO* (Temperature Compensated Crystal Oscillator): Un oscillatore a quarzo con compensazione della temperatura. Le variazioni di frequenza dovute alle fluttuazioni di temperatura vengono compensate elettronicamente.
*OCXO* (Oven Controlled Crystal Oscillator): Un oscillatore a quarzo controllato da forno. Il quarzo viene mantenuto a una temperatura costante in un piccolo forno a temperatura controllata, garantendo così una stabilità di frequenza molto elevata.

La differenza principale è quindi:

*TCXO*: La temperatura può variare, ma la deviazione di frequenza viene compensata elettronicamente.
*OCXO*: La temperatura del quarzo viene mantenuta attivamente costante. Di conseguenza, la stabilità di frequenza è generalmente maggiore rispetto a un TCXO.
</indepth>

I trasmettitori-ricevitori e i convertitori progettati per frequenze di ingresso o uscita elevate (nell’ordine dei GHz) devono disporre di un oscillatore molto stabile. Errori nella frequenza dell’oscillatore, a causa della moltiplicazione interna della frequenza e delle bande strette delle modalità operative o della SSB, portano a deviazioni inaccettabili nella frequenza di destinazione. Una deviazione nella frequenza dell’oscillatore viene moltiplicata dalla stessa moltiplicazione. Spesso si utilizzano un cosiddetto TCXO o OCXO, che può essere sincronizzato anche con una sorgente di riferimento esterna (ad esempio GPS) per stabilizzare al massimo la frequenza dell’oscillatore e ridurre al minimo le deviazioni nella frequenza di destinazione.

[question:EF505]