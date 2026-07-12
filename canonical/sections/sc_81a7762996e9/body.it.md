Gli oscillatori, a causa della dipendenza dalla temperatura dei componenti utilizzati al loro interno, hanno sempre una dipendenza della frequenza generata dalla temperatura ambiente. Transistor e diodi hanno una dipendenza relativamente forte dalle loro caratteristiche e dalla temperatura ambiente (fattore di amplificazione, tensione di soglia, capacità). Allo stesso modo, anche i parametri elettrici dei componenti passivi come condensatori, resistenze e in particolare i cristalli oscillanti dipendono dalla loro temperatura ambiente.
Per mantenere gli oscillatori il più stabili possibile nella loro frequenza, esistono diverse possibilità tecniche e fisiche:
1. Tutti gli oscillatori dovrebbero sempre essere il più possibile ben isolati termicamente da altre fonti di calore negli apparecchi.
2. Al posto di un oscillatore RC, LC o VCO, è preferibile un oscillatore a quarzo, poiché è molto più stabile in frequenza grazie all'alto fattore di qualità (Q) del quarzo. Questo tipo di oscillatore è chiamato *XO* - Crystal oscillator.
3. Utilizzo di un oscillatore a quarzo e compensazione degli influssi termici mediante l'uso di componenti nel circuito dell'oscillatore, in modo che gli influssi di temperatura nell'intervallo di temperatura operativa usuale si compensino a vicenda. Questo tipo di oscillatore è chiamato *TCXO* - Temperature compensated crystal oscillator.
4. Stabilizzazione artificiale della temperatura ambiente di un oscillatore a quarzo mediante un controllo della temperatura con un circuito termostatico e l'installazione in un involucro termicamente isolato, nonché isolamento da fonti di calore e freddo esterne. Questo tipo di oscillatore è chiamato *OCXO* - Oven controlled crystal oscillator. L'OCXO ha la più alta stabilità di frequenza rispetto agli altri tipi di oscillatori.

Fondamentalmente, gli oscillatori a frequenza stabile dovrebbero sempre essere il più possibile ben isolati termicamente da fonti di calore e freddo interne ed esterne all'apparecchio. Ciò può avvenire, ad esempio, mediante una distanza il più possibile grande dalle fonti di calore e freddo interne ed esterne, nonché dai flussi d'aria.

[question:AF215]
[question:AD602]
[question:AD603]
[question:AD605]

In particolare durante il funzionamento ad alte frequenze, la stabilità di frequenza dell'oscillatore di riferimento dei trasmettitore-ricevitore, transverter e convertitori è molto importante quando si utilizzano modi operativi che reagiscono in modo sensibile alle deviazioni di frequenza. Per raggiungere le alte frequenze di uscita o di ricezione, all'interno dell'apparecchio avviene una moltiplicazione di frequenza dell'oscillatore di riferimento. Ciò fa sì che le deviazioni di frequenza dell'oscillatore di riferimento si ripercuotano in modo moltiplicativo sulle frequenze di trasmissione o ricezione, il che può portare a elevate deviazioni di frequenza e instabilità di frequenza (ad esempio, deriva del segnale trasmesso o ricevuto).
Pertanto, si dovrebbe sempre utilizzare il miglior tipo di oscillatore disponibile (ad esempio, TCXO o OCXO).

[question:AD604]