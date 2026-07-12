È sempre necessario un convertitore di tensione quando una tensione elettrica deve essere convertita in un'altra tensione. In radioamatore, questo può essere, ad esempio, la generazione di $\qty{5}{\volt}$ per un microcontrollore da un alimentatore da $\qty{13,8}{\volt}$ o l'alimentazione di un laptop con $\qty{19}{\volt}$ da una batteria da $\qty{12}{\volt}$. Tali circuiti sono chiamati convertitori DC/DC. Se la tensione viene aumentata, si parla di convertitore Step-UP (elevatore), se viene ridotta, di convertitore Step-DOWN (riduttore).

Ad ogni conversione di tensione si verificano perdite. Pertanto, la potenza erogata è sempre inferiore alla potenza fornita. Il rapporto tra potenza d’uscita e potenza d’ingresso è chiamato rendimento $\eta$:

$ \eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} $

Per le seguenti domande, la formula della potenza $P = U \cdot I$ deve essere applicata per calcolare la potenza d’ingresso e la potenza d’uscita. Successivamente, il rendimento può essere determinato.

[question:AB213]
[question:AB214]

<indepth>
[photo:300:StepUpWandler: Convertitori Abwärts- (Buck) Aufwärts- (Boost). Qui impostato come convertitore di tensione ascendente da $\qty{7,2}{\volt}$ a $\qty{24}{\volt}$]
Questo convertitore Buck-Boost può essere impostato da $\qty{0,5}{\volt}$ a $\qty{25}{\volt}$ in uscita. La potenza massima è di $\qty{25}{\watt}$. Poiché il rendimento è molto elevato, i transistor di commutazione funzionano senza dissipatori di calore. La modalità operativa convertitore discendente (Step Down = Buck Mode) o convertitore ascendente (Step Up = Boost Mode) può essere attivata con il mini-interruttore destro.
</indepth>