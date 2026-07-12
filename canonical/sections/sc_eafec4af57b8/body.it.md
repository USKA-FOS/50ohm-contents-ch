La modulazione a spostamento di fase (Phase Shift Keying, PSK) è un metodo di modulazione digitale utilizzato per la trasmissione di dati nelle telecomunicazioni e nel radioamatore. La PSK si basa sulla variazione della fase di un segnale portante per rappresentare diversi stati di dati. Rispetto alla modulazione di ampiezza o di frequenza, la PSK è meno suscettibile al rumore di ampiezza e può raggiungere una maggiore velocità di trasmissione dati a parità di larghezza di banda.

[picture:705:psk:Modulazione a spostamento di fase (Phase-shift Keying)]

Principio della modulazione a spostamento di fase (PSK)

Nella sua forma più semplice, la **BPSK (Binary Phase Shift Keying)**, ci sono due angoli di fase, ad esempio $\qty{0}{\degree}$ e $\qty{180}{\degree}$. Ogni angolo di fase rappresenta un valore di bit ($\num{0}$ o $\num{1}$). Quando i valori dei bit cambiano, la fase della portante cambia di $\qty{180}{\degree}$.

Per velocità di trasmissione dati più elevate, esistono varianti come la **QPSK (Quadrature Phase Shift Keying)** e la **8-PSK**, che utilizzano quattro o otto posizioni di fase per trasmettere più bit per simbolo:
- **QPSK**: Utilizza quattro fasi ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ e $\qty{270}{\degree}$) per codificare due bit per simbolo.
- **8-PSK**: Utilizza otto fasi per codificare tre bit per simbolo.

Segnali nella rappresentazione temporale

Nella rappresentazione temporale di un segnale PSK, la modulazione a spostamento di fase si manifesta come un brusco cambiamento nell'angolo di fase del segnale portante, mentre l'ampiezza rimane costante. Questa è una chiara differenza rispetto alla modulazione di ampiezza o di frequenza, poiché l'altezza e la frequenza del segnale rimangono le stesse, cambia solo la fase ad ogni cambio di simbolo.

Esempio: BPSK nella rappresentazione temporale
- Con la BPSK, il segnale è diviso in due fasi: ad esempio, ampiezza positiva per una fase ($\qty{0}{\degree}$) e ampiezza negativa per la fase opposta ($\qty{180}{\degree}$).
- In un diagramma temporale, si osserva quindi un salto del segnale ad ogni cambio di bit, ad esempio da positivo a negativo o viceversa.

Esempio: QPSK nella rappresentazione temporale
- Qui si osservano quattro diversi angoli di fase. Le transizioni possono essere anch'esse brusche, ma l'ampiezza non cambia.
- Poiché vengono utilizzati più angoli di fase, i salti di fase sono minori e la curva ha un andamento leggermente "più liscio" rispetto alla BPSK.

Come riconoscere i segnali

In un oscilloscopio o in un diagramma di fase, le transizioni di fase sono visibili:
- **Nel dominio temporale**: Un'inversione brusca della fase del segnale (da positivo a negativo o tra diverse posizioni di fase).
- **Nel diagramma di fase** (spesso visualizzato come diagramma di costellazione): Ogni angolo di fase è rappresentato come un punto su un cerchio, che indica i diversi stati (bit). Con un segnale pulito, i punti rimangono stabili in posizioni fisse.

La PSK è particolarmente utile nella comunicazione digitale, poiché consente elevate velocità di trasmissione dati con una trasmissione relativamente robusta. La variazione di fase a parità di ampiezza aiuta a riconoscere meglio il segnale anche in presenza di rumore e interferenze, consentendo così una trasmissione più stabile.

[question:AE401]