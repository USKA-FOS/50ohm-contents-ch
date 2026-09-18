Nei segnali di corrente alternata sinusoidali la potenza viene calcolata utilizzando i valori efficaci di corrente e tensione. Pertanto, non è possibile utilizzare semplicemente la tensione picco-picco $U_\text{SS}$, o la tensione di picco $\hat{U}$ al posto dei valori efficaci.


<margin>
[picture:834:a_wechselstrom_leistung:Valori efficaci per il calcolo della potenza]
</margin>

Pertanto, la formula per il calcolo della potenza è:
$P_\text{corrente alternata} = U_\text{eff} \cdot I_\text{eff} = \dfrac{{U_\text{eff}}^2}{R} = I_\text{eff}^2 \cdot R$


Nei segnali sinusoidali vale inoltre:

$U_\text{eff} = \dfrac {\hat{U}} {\sqrt{2}} = \dfrac {U_\text{SS}} {2 \cdot \sqrt{2}}$
$I_\text{eff} = \dfrac {\hat{I}} {\sqrt{2}} = \dfrac {I_\text{SS}} {2 \cdot \sqrt{2}}$


Di conseguenza, per i segnali sinusoidali valgono le seguenti relazioni, che permettono di calcolare anche con valori di picco e picco-picco:

$\begin{split} P_\text{corrente alternata} &=  U_\text{eff} \cdot I_\text{eff} \\ &= \frac{\hat{U}\cdot\hat{I}}{\sqrt{2}\cdot\sqrt{2}} = \frac{\hat{U} \cdot \hat{I}}{2} \\ &= \frac{U_\text{eff}^2}{R} = \left(\frac{\hat{U}}{\sqrt{2}}\right)^2 \cdot \frac{1}{R} = \frac{\hat{U}^2}{2 \cdot R} \\ &= I_\text{eff}^2 \cdot R = \left(\frac{\hat{I}}{\sqrt{2}}\right)^2 \cdot R = \frac{\hat{I}^2\cdot R}{2} \end{split}$


La seguente domanda può essere risolta molto facilmente con queste considerazioni ($I_\mathrm{max}$ è solo un'altra denominazione per $\hat{I}$):


[question:AB301]


Nel campo della radioamatorialistica si incontrano tensioni con frequenze diverse (ad esempio in kilohertz o gigahertz) e forme d'onda (tensione rettangolare, tensione sinusoidale, tensione continua). Queste possono anche essere distorte e non presentarsi, ad esempio, come una pura tensione sinusoidale. Queste diverse tensioni generano correnti elettriche diverse in un circuito. In linea di principio, per misurare con una precisione ragionevole questa varietà di correnti elettriche, sarebbero necessari diversi strumenti.


Nel campo della radioamatorialistica si utilizza spesso un cosiddetto *convertitore termico*.
Con questo metodo si sfrutta il fatto che il flusso di corrente riscalda il filo conduttore (cfr. resistenza dei fili). Maggiore è la corrente che fluisce, più il filo si riscalda. Il riscaldamento è quindi proporzionale all'intensità di corrente. Il convertitore termico misura questo riscaldamento e lo visualizza come intensità di corrente. È importante notare che con questo metodo di misura si ottiene il *valore efficace* dell'intensità di corrente. Il vantaggio è che l'intensità di corrente può essere determinata quasi *indipendentemente* dalla forma d'onda o dalla frequenza. Il convertitore termico può quindi coprire un'ampia gamma di segnali.

[question:AI105]