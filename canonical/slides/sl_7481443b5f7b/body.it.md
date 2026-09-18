* La tensione d’ingresso può variare
* Ad esempio nei dispositivi alimentati da batteria
* I moduli sensibili (ad esempio gli oscillatori) cambierebbero frequenza
* Soluzione: stabilizzazione della tensione

---
## Stabilizzazione con diodo Zener
<left>
[picture:323:a_Stabilisierung mit Z-Diode:Stabilizzazione della tensione con diodo Zener]
</left>
<right>
* Circuito molto semplice
* Può mantenere la tensione d’uscita entro certi limiti
</right>
<note>
</note>
---
[question:AD321]
--- style="font-size: 0.7em;"
#### Procedimento di soluzione
* dati: $R_L = \qty{470}{\ohm}$
* dati: $I_L = \qty{10}{\milli\ampere}$
* dati: $I_Z = \qty{15}{\milli\ampere}$
* dati: $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* richiesto: $\eta = \frac{P_L}{P_{\mathrm{in}}}$

<fragment>
$P_L = I_L^2 \cdot R_L = (\qty{10}{\milli\ampere})^2 \cdot \qty{470}{\ohm} = \qty{47}{\milli\watt}$
</fragment>
<fragment>
$P_{\mathrm{in}} = U_{\mathrm{in}} \cdot I_{\mathrm{in}} = U_{\mathrm{in}} \cdot (I_Z + I_L) = \qty{13,8}{\volt} \cdot (\qty{15}{\milli\ampere} + \qty{10}{\milli\ampere}) = \qty{345}{\milli\watt}$
</fragment>
<fragment>
$\eta = \frac{P_L}{P_{\mathrm{in}}} = \frac{\qty{47}{\milli\watt}}{\qty{345}{\milli\watt}} \approx \num{0,14}$
</fragment>
---
## Regolatore lineare di tensione

<left>
[picture:985:a_spannungsregler_linear:Schema di un regolatore lineare di tensione]
</left>
<right>
* Il transistor di potenza funziona come una resistenza variabile
* Insieme alla resistenza di carico forma un partitore di tensione
* Il rendimento è spesso molto basso
</right>

---
[question:AD315]
---
[question:AD319]
---
#### Procedimento di soluzione
* dati: $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* dati: $U_{\mathrm{out}} = \qty{9}{\volt}$
* dati: $I = \qty{900}{\milli\ampere}$
* richiesto: $P_V$

<fragment>
$U_{IC1} = U_{\mathrm{in}} - U_{\mathrm{out}} = \qty{13,8}{\volt} - \qty{9}{\volt} = \qty{4,8}{\volt}$
</fragment>
<fragment>
$P_V = U_{IC1} \cdot I = \qty{4,8}{\volt} \cdot \qty{900}{\milli\ampere} = \qty{4,32}{\watt}$
</fragment>
---
[question:AD320]
---
#### Procedimento di soluzione
* dati: $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* dati: $U_{\mathrm{out}} = \qty{5}{\volt}$
* dati: $I_{\mathrm{in}} = \qty{455}{\milli\ampere}$
* dati: $I_{\mathrm{out}} = \qty{450}{\milli\ampere}$
* richiesto: $\eta$

<fragment>
$\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}} = \frac{\qty{5}{\volt} \cdot \qty{450}{\milli\ampere}}{\qty{13,8}{\volt} \cdot \qty{455}{\milli\ampere}} \approx \num{0,36}$
</fragment>
---
## Regolatore di tensione a valore fisso
<left>
[picture:200:a_Festspannungsregler:Regolatore di tensione a valore fisso]
</left>
<right>
* Realizzato come circuito integrato
* Funziona come un regolatore lineare con una sorgente di riferimento di tensione molto precisa e una regolazione elettronica ottimale
* Anche in caso di forti fluttuazioni sulla tensione d’ingresso, la tensione d’uscita rimane molto stabile
</right>

---
[question:AD317]
---
[question:AD316]
---
[question:AD318]