La frequenza di un oscillatore dipende sempre dalla temperatura ambiente, poiché le proprietà dei componenti utilizzati variano al variare della temperatura. Nei transistor e nei diodi, ciò riguarda ad esempio il fattore di amplificazione, la tensione di soglia e le capacità. Anche i componenti passivi come i condensatori, le resistenze e in particolare i quarzi oscillatori presentano proprietà elettriche dipendenti dalla temperatura.

Per mantenere la frequenza di un oscillatore il più stabile possibile, esso dovrebbe essere ben schermato termicamente da altre fonti di calore e freddo all'interno dell'apparecchio. Questo può essere ottenuto, ad esempio, mantenendo una distanza il più possibile elevata da fonti di calore e freddo interne ed esterne, nonché da correnti d'aria. Inoltre, un oscillatore a quarzo è preferibile rispetto a un oscillatore RC, LC o VCO, poiché, grazie all'elevato fattore di qualità del quarzo, offre una stabilità di frequenza notevolmente superiore.

[question:AF215]

Esistono diversi tipi di oscillatori a quarzo, che differiscono per stabilità di frequenza:

* L'oscillatore a quarzo più semplice (cfr. figura [ref:a_xo]) è denominato *XO*, acronimo di *Crystal Oscillator*.
* Un *TCXO* (*Temperature Compensated Crystal Oscillator*) compensa gli effetti della temperatura tramite componenti aggiuntivi nel circuito dell'oscillatore, in modo che gli effetti dipendenti dalla temperatura si compensino reciprocamente entro il range di temperatura operativa usuale.
* Un *OCXO* (*Oven-Controlled Crystal Oscillator*) stabilizza la temperatura dell'oscillatore a quarzo mediante un riscaldamento regolato. A tal fine, l'oscillatore è collocato in un involucro termicamente isolato, che lo protegge in larga misura dagli influssi esterni di calore e freddo. Tra i tipi di oscillatori menzionati, l'OCXO offre la massima stabilità di frequenza.

<margin>
[photo:333:a_xo:Oscillatore a quarzo XO con $\qty{433,75}{\mega\hertz}$]
[photo:337:a_ocxo:Oscillatore a quarzo OCXO con $\qty{10}{\mega\hertz}$]
</margin>

[question:AD602]
[question:AD603]
[question:AD605]

In particolare, durante il funzionamento su frequenze elevate, la stabilità di frequenza dell'oscillatore di riferimento di ricetrasmettitori, trasverter e convertitori è molto importante quando si utilizzano metodi di trasmissione sensibili alle deviazioni di frequenza. Per raggiungere le elevate frequenze di trasmissione o ricezione, all'interno dell'apparecchio avviene una moltiplicazione di frequenza dell'oscillatore di riferimento. Ciò comporta che le deviazioni di frequenza dell'oscillatore di riferimento si ripercuotano in modo moltiplicativo sulle frequenze di trasmissione o ricezione, causando elevate deviazioni di frequenza e instabilità di frequenza (ad esempio, deriva del segnale di trasmissione o ricezione). Pertanto, ad esempio, sulla banda dei $\qty{3}{\centi\metro}$ o dei $\qty{10}{\giga\hertz}$, si dovrebbe utilizzare almeno un TCXO.

[question:AD604]