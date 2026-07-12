* *Integrated Circuit (IC)*: Circuiti integrati
* Circuito complesso su un substrato semiconduttore
* Semplificano la costruzione di circuiti elettronici

---
[question:AC601]
---
## Circuito Integrato Monolitico a Microonde (MMIC)

* Amplificatore a banda larga con pochi componenti
* Tipicamente impedenza di ingresso e uscita di $\qty{50}{\ohm}$
* Unisce componenti attivi e passivi

---
[question:AC602]
---
[question:AC603]
---
[question:AC604]
---
### Collegamento MMIC

<left>
[picture:773:a_mmic:Circuito MMIC]
</left>
<right>
* Il punto di funzionamento viene impostato tramite $R_{\textrm{BIAS}}$
* I condensatori isolano la tensione continua
* I collegamenti 2 e 4 sono a massa rispetto a $U_{\textrm{CC}}$
* Il collegamento 1 è aperto
* $U_{\textrm{CC}}$ cade attraverso $R_{\textrm{BIAS}}$ e MMIC
</right>
<note>
</note>

---
[question:AF425]
---
#### Percorso di soluzione
* dato: $U_{\textrm{D}} = \qty{4}{\volt}$
* dato: $U_{\textrm{CC}} = \qty{13,5}{\volt}$
* dato: $I_{\textrm{D}} = \qty{10}{\milli\ampere}$
* cercato: $R_{\textrm{BIAS}}$

<fragment>
$R_{\textrm{BIAS}} = \frac{U_{\textrm{CC}} - U_{\textrm{D}}}{I_{\textrm{D}}} = \frac{\qty{13,5}{\volt} - \qty{4}{\volt}}{\qty{10}{\milli\ampere}} = \qty{950}{\ohm}$
</fragment>

---
[question:AF426]
---
#### Percorso di soluzione
* dato: $U_{\textrm{D}} = \qty{4}{\volt}$
* dato: $U_{\textrm{CC}} = \qty{13,8}{\volt}$
* dato: $I_{\textrm{D}} = \qty{15}{\milli\ampere}$
* cercato: $R_{\textrm{BIAS}}$

<fragment>
$R_{\textrm{BIAS}} = \frac{U_{\textrm{CC}} - U_{\textrm{D}}}{I_{\textrm{D}}} = \frac{\qty{13,8}{\volt} - \qty{4}{\volt}}{\qty{15}{\milli\ampere}} = \qty{653,3}{\ohm} \rightarrow \qty{680}{\ohm}$
</fragment>

---
[question:AF427]
---
#### Percorso di soluzione
* dato: $U = \qty{9}{\volt}$
* dato: $R_{\textrm{BIAS}} = \qty{470}{\ohm}$
* dato: $U_{\textrm{D}} = \qty{4}{\volt}$
* cercato: $P$
* approccio: la corrente attraverso $R_{\textrm{BIAS}}$ è ovunque la stessa, poiché non ci sono altri carichi resistivi nel circuito

<fragment>
$I_{\textrm{D}} = \frac{U_{\textrm{BIAS}}}{R_{\textrm{BIAS}}} = \frac{U-U_{\textrm{D}}}{R_{\textrm{BIAS}}} = \frac{\qty{9}{\volt}-\qty{4}{\volt}}{\qty{470}{\ohm}} = \qty{10,64}{\milli\ampere}$
</fragment>
<fragment>
$P = U_{\textrm{D}} \cdot I_{\textrm{D}} = \qty{4}{\volt} \cdot \qty{10,64}{\milli\ampere} \approx \qty{43}{\milli\watt}$
</fragment>
