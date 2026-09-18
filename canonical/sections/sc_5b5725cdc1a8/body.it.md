Un convertitore di tensione è necessario ogniqualvolta si voglia convertire una tensione elettrica in un’altra. Nel radioamatore, questo può essere ad esempio la generazione di $\qty{5}{\volt}$ per un microcontrollore da una sorgente a $\qty{13,8}{\volt}$ oppure l’alimentazione di un portatile con $\qty{19}{\volt}$ da una batteria a $\qty{12}{\volt}$. Tali circuiti sono detti convertitori DC/DC. Se la tensione viene aumentata, si parla di convertitore Step-UP (elevatore), se viene ridotta, di convertitore Step-DOWN (riduttore).

Ad ogni conversione di tensione si generano perdite. Pertanto, la potenza erogata è sempre inferiore a quella assorbita. Il rapporto tra potenza d’uscita e potenza d’ingresso è detto rendimento $\eta$:

$ \eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} $

Per rispondere alle domande seguenti, è necessario applicare la formula della potenza $P = U \cdot I$ per calcolare la potenza d’ingresso e d’uscita. Successivamente si può determinare il rendimento.

[question:AB213]
[question:AB214]

<indepth>
[photo:300:StepUpWandler: Convertitori Buck (riduttore) e Boost (elevatore). Qui impostato come convertitore elevatore da $\qty{7,2}{\volt}$ a $\qty{24}{\volt}$]
Questo convertitore Buck-Boost può fornire in uscita da $\qty{0,5}{\volt}$ a $\qty{25}{\volt}$. La potenza massima è $\qty{25}{\watt}$. Grazie all’elevato rendimento, i transistor di commutazione non necessitano di dissipatore. La modalità di funzionamento come convertitore riduttore (Step Down = Buck Mode) o elevatore (Step Up = Boost Mode) può essere attivata con l’interruttore miniaturizzato a destra.
</indepth>