Passiamo ora più in dettaglio al contraltare del convertitore A/D: il convertitore D/A. Il convertitore D/A genera da un flusso di dati (campioni) presente in formato digitale un segnale analogico. In questo caso, il convertitore D/A, proprio come il convertitore A/D, non può generare valori di ampiezza arbitrariamente precisi, ma ha, proprio come il convertitore A/D, una risoluzione massima (in bit). Per questo motivo, esiste anche in questo caso un numero finito di valori di segnale analogico che il convertitore D/A può generare. Il numero di livelli possibili si calcola come descritto in precedenza per il convertitore A/D.

[question:AF609]

Un convertitore D/A può generare solo tensioni all'interno di un determinato intervallo di valori (ad es. da $\qty{0}{\volt}$ a $\qty{1}{\volt}$ o da $\qty{-2}{\volt}$ a $\qty{2}{\volt}$). In questo caso, il numero di livelli descritti in precedenza (risoluzione del convertitore D/A) si distribuisce su questo intervallo di valori per un convertitore D/A che opera linearmente (lineare significa qui che la distanza tra i singoli livelli è sempre la stessa). Se il convertitore D/A ha, ad esempio, una risoluzione di soli $\qty{4}{\bit}$, abbiamo $\num{16}$ livelli possibili. Questi si distribuiscono poi, ad esempio, su un intervallo di valori di tensione da $\qty{0}{\volt}$ a $\qty{1}{\volt}$. Per calcolare la passo tra due livelli, è sufficiente dividere l'intervallo di valori per il numero di livelli possibili. Nel nostro esempio precedente, ciò produce una distanza (passo) di $\qty{6,25}{\milli\volt}$.

[question:AF611]
[question:AF610]

