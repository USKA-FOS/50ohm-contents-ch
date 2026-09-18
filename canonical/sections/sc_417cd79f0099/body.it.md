Un Low Noise Block Converter (LNB) viene spesso utilizzato nell'*elaborazione* di frequenze elevate nell'intervallo dei $\unit{\giga\hertz}$ nel traffico radioamatoriale via satellite. La figura [ref:a_lnb] mostra una possibile implementazione di una stazione QO-100. In questo caso, la frequenza di ricezione molto elevata, tipicamente ricevuta tramite un riflettore parabolico SAT, viene già convertita verso il basso a una frequenza notevolmente inferiore direttamente nell'LNB, per evitare elevate perdite del cavo che si verificherebbero a frequenze elevate.

<margin>
[picture:1094:a_lnb:LNB (blu) e Bias-T (rosso) in un trasmettitore-ricevitore QO-100]
</margin>

[question:AF230]

Un LNB è un componente attivo che richiede un'alimentazione elettrica. Questa viene solitamente fornita direttamente tramite il cavo coassiale che porta all'LNB. A tale scopo, nella stazione di ricezione viene inserito nel cavo coassiale un cosiddetto Bias-T. Il suo compito è fornire l'alimentazione in corrente continua all'LNB e separare la tensione continua dal segnale ad alta frequenza nel percorso del segnale verso il ricevitore.
Un LNB può ricevere segnali sia polarizzati orizzontalmente che verticalmente. La commutazione tra le due direzioni di polarizzazione avviene tramite la tensione di servizio con cui viene alimentato l'LNB. I valori tipici sono ad esempio $\qty{12}{\volt}$ e $\qty{18}{\volt}$.

[question:AF231]