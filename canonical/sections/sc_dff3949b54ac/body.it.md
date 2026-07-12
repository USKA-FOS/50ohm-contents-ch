Nei segnali di corrente alternata sinusoidale, la potenza viene calcolata dai valori efficaci di corrente e tensione. Pertanto, non si possono semplicemente sostituire la tensione picco-picco $U_\text{SS}$ o la tensione di picco $\hat{U}$.

<margin>
[picture:834:a_wechselstrom_leistung:Valori efficaci per il calcolo della potenza]
</margin>

Quindi, per il calcolo della potenza si ottiene
$P_\text{Wechselstrom} = U_\text{eff} \cdot I_\text{eff} = \dfrac{{U_\text{eff}}^2}{R} = I_\text{eff}^2 \cdot R$


Per segnali sinusoidali vale tuttavia anche:

$U_\text{eff} = \dfrac {\hat{U}} {\sqrt{2}} = \dfrac {U_\text{SS}} {2 \cdot \sqrt{2}}$ 
$I_\text{eff} = \dfrac {\hat{I}} {\sqrt{2}} = \dfrac {I_\text{SS}} {2 \cdot \sqrt{2}}$ 

Di conseguenza, per segnali sinusoidali si ottengono le seguenti relazioni, che possono essere calcolate anche con valori di picco e valori picco-picco:

$\begin{split} P_\text{Wechselstrom} &=  U_\text{eff} \cdot I_\text{eff} \\ &= \frac{\hat{U}\cdot\hat{I}}{\sqrt{2}\cdot\sqrt{2}} = \frac{\hat{U} \cdot \hat{I}}{2} \\ &= \frac{U_\text{eff}^2}{R} = \left(\frac{\hat{U}}{\sqrt{2}}\right)^2 \cdot \frac{1}{R} = \frac{\hat{U}^2}{2 \cdot R} \\ &= I_\text{eff}^2 \cdot R = \left(\frac{\hat{I}}{\sqrt{2}}\right)^2 \cdot R = \frac{\hat{I}^2\cdot R}{2} \end{split}$

La seguente domanda può essere risolta molto facilmente con queste considerazioni ($I_\mathrm{max}$ è solo un'altra denominazione per $\hat{I}$):

[question:AB301]

Nell'ambito del radioamatore, abbiamo a che fare con tensioni di frequenze diverse (ad es. kilo o gigahertz) e forme d'onda (tensione a onda quadra, tensione sinusoidale, tensione continua). Queste possono anche essere distorte e non presentarsi come, ad es., una pura tensione sinusoidale. Queste diverse tensioni generano diverse correnti elettriche in un circuito. In linea di principio, si avrebbero quindi bisogno di diversi apparecchi per misurare questa larghezza di banda di correnti elettriche con una ragionevole precisione di misurazione. 

Nel settore del radioamatore si utilizza quindi spesso un cosiddetto *convertitore termico*.
Si sfrutta il fatto che il flusso di corrente riscalda il filo conduttore (cfr. resistenza dei fili). Più corrente scorre, più il filo si scalda. Il riscaldamento è quindi proporzionale all'intensità di corrente. Il convertitore termico misura questo riscaldamento e lo visualizza come intensità di corrente. Si noti che con questo metodo di misurazione otteniamo il *valore efficace* dell'intensità di corrente. Il vantaggio è che l'intensità di corrente può essere determinata quasi *indipendentemente* dalla forma d'onda o dalla frequenza. Il convertitore termico può quindi coprire un ampio intervallo di segnali. 

[question:AI105]
