* Tensione d’ingresso può variare
* Ad esempio, per apparecchi alimentati a batteria
* Gruppi sensibili (ad es. oscillatori) cambierebbero la frequenza
* Rimedio: stabilizzazione della tensione

---
## Stabilizzazione con diodo Zener
<left>
[picture:323:a_Stabilisierung mit Z-Diode:Spannungsstabilisierung mit Z-Diode]
</left>
<right>
* Circuito molto semplice
* Può mantenere la tensione d’uscita stabile entro certi limiti
</right>
<note>
</note>
---
[question:AD321]
--- style="font-size: 0.7em;"
#### Percorso di soluzione
* dato: $R_L = \qty{470}{\ohm}$
* dato: $I_L = \qty{10}{\milli\ampere}$
* dato: $I_Z = \qty{15}{\milli\ampere}$
* dato: $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* cercato: $\eta = \frac{P_L}{P_{\mathrm{in}}}$

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
## Regolatore di tensione lineare

<left>
[picture:985:a_spannungsregler_linear:Schema di un regolatore di tensione lineare]
</left>
<right>
* Il transistor di potenza viene utilizzato come resistenza variabile
* Forma un partitore di tensione insieme alla resistenza di carico
* Il rendimento è spesso molto basso
</right>

---
[question:AD315]
---
[question:AD319]
---
#### Percorso di soluzione
* dato: $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* dato: $U_{\mathrm{out}} = \qty{9}{\volt}$
* dato: $I = \qty{900}{\milli\ampere}$
* cercato: $P_V$

<fragment>
$U_{IC1} = U_{\mathrm{in}} - U_{\mathrm{out}} = \qty{13,8}{\volt} - \qty{9}{\volt} = \qty{4,8}{\volt}$
</fragment>
<fragment>
$P_V = U_{IC1} \cdot I = \qty{4,8}{\volt} \cdot \qty{900}{\milli\ampere} = \qty{4,32}{\watt}$
</fragment>
---
[question:AD320]
---
#### Percorso di soluzione
* dato: $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* dato: $U_{\mathrm{out}} = \qty{5}{\volt}$
* dato: $I_{\mathrm{in}} = \qty{455}{\milli\ampere}$
* dato: $I_{\mathrm{out}} = \qty{450}{\milli\ampere}$
* cercato: $\eta$

<fragment>
$\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} = \frac{U_{\mathrm{out}} \cdot I_{\mathrm{out}}}{U_{\mathrm{in}} \cdot I_{\mathrm{in}}} = \frac{\qty{5}{\volt} \cdot \qty{450}{\milli\ampere}}{\qty{13,8}{\volt} \cdot \qty{455}{\milli\ampere}} \approx \num{0,36}$
</fragment>
---
## Regolatori di tensione fissi
<left>
[picture:200:a_Festspannungsregler:Regolatori di tensione fissi]
</left>
<right>
* Progettati come IC
* Funzionano come regolatori di tensione lineari con una sorgente di riferimento di tensione molto precisa e una regolazione elettronica ottimale
* Anche in caso di forti fluttuazioni sul lato di ingresso, il lato di uscita è molto stabile
</right>

---
[question:AD317]
---
[question:AD316]
---
[question:AD318]
---
#### Percorso di soluzione
* dato: $U_{\mathrm{in}} = \qty{13,8}{\volt}$
* dato: $U_{\mathrm{out}} = \qty{5}{\volt}$
* dato: $R_L = \qty{10}{\ohm}$
* cercato: $P_V$

<fragment>
$I = \frac{U_{\mathrm{in}}}{R_L} = \frac{\qty{5}{\volt}}{\qty{10}{\ohm}} = \qty{500}{\milli\ampere}$
</fragment>
<fragment>
$U_{IC1} = U_{\mathrm{in}} - U_{\mathrm{out}} = \qty{13,8}{\volt} - \qty{5}{\volt} = \qty{8,8}{\volt}$
</fragment>
<fragment>
$P_V = U_{IC1} \cdot I = \qty{8,8}{\volt} \cdot \qty{500}{\milli\ampere} = \qty{4,4}{\watt}$
</fragment>
