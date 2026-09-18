## Regola dei nodi e delle maglie

*Regola delle maglie*: In ogni circuito chiuso (maglia) la somma delle tensioni è uguale a zero.
*Regola dei nodi*: In ogni nodo la somma delle correnti in entrata è uguale alla somma delle correnti in uscita.

<note>
Leggi di Kirchhoff
</note>
---
[question:AD106]
---
#### Procedimento di soluzione
* dati: $R_1 = R_2 = R_3 = \qty{10}{\kilo\ohm}$
* dati: $I_3 = I_2 = \qty{1}{\milli\ampere}$
* richiesto: $U$

<fragment>
$R_{\mathrm{ges}} = R_1 + \frac{R_2 \cdot R_3}{R_2 + R_3} = \qty{10}{\kilo\ohm} + \frac{\qty{10}{\kilo\ohm} \cdot \qty{10}{\kilo\ohm}}{\qty{10}{\kilo\ohm} + \qty{10}{\kilo\ohm}} = \qty{15}{\kilo\ohm}$
</fragment>
<fragment>
$I = I_2 + I_3 = \qty{1}{\milli\ampere} + \qty{1}{\milli\ampere} = \qty{2}{\milli\ampere}$
</fragment>
<fragment>
$U = R_{\mathrm{ges}} \cdot I = \qty{15}{\kilo\ohm} \cdot \qty{2}{\milli\ampere} = \qty{30}{\volt}$
</fragment>

---
[question:AD107]
---
#### Procedimento di soluzione
* dati: $R_1 = R_2 = R_3 = \qty{10}{\kilo\ohm}$
* dati: $U=\qty{15}{\volt}$
* richiesto: $I_3$

<fragment>
$R_{\mathrm{ges}} = R_1 + \frac{R_2 \cdot R_3}{R_2 + R_3} = \qty{10}{\kilo\ohm} + \frac{\qty{10}{\kilo\ohm} \cdot \qty{10}{\kilo\ohm}}{\qty{10}{\kilo\ohm} + \qty{10}{\kilo\ohm}} = \qty{15}{\kilo\ohm}$
</fragment>

<fragment>
$\frac{U_3}{U} = \frac{R_2 \parallel R_3}{R_{\mathrm{ges}}} \Rightarrow U_3 = \frac{R_2 \parallel R_3}{R_{\mathrm{ges}}} \cdot U = \frac{\qty{5}{\kilo\ohm}}{\qty{15}{\kilo\ohm}} \cdot \qty{15}{\volt} = \qty{5}{\volt}$
</fragment>

<fragment>
$I_3 = \frac{U_3}{R_3} = \frac{\qty{5}{\volt}}{\qty{10}{\kilo\ohm}} = \qty{0,5}{\milli\ampere}$
</fragment>

---
[question:AD108]
---
#### Procedimento di soluzione
* dati: $R_1 = R_2 = R_3 = \qty{10}{\kilo\ohm}$
* dati: $U=\qty{15}{\volt}$
* richiesto: $P_2$

<fragment>
$\frac{U_2}{U} = \frac{R_2 \parallel R_3}{R_{\mathrm{ges}}} \Rightarrow U_2 = \frac{R_2 \parallel R_3}{R_{\mathrm{ges}}} \cdot U = \frac{\qty{5}{\kilo\ohm}}{\qty{15}{\kilo\ohm}} \cdot \qty{15}{\volt} = \qty{5}{\volt}$
</fragment>

<fragment>
$P_2 = \frac{U_2^2}{R_2} = \frac{(\qty{5}{\volt})^2}{\qty{10}{\kilo\ohm}} = \qty{2,5}{\milli\watt}$
</fragment>
---
[question:AD109]
--- style="font-size: 0.7em;"
#### Procedimento di soluzione

<left>
* dati: $R = \qtyrange{0}{1}{\kilo\ohm}$
* dati: $R_1 = \qty{200}{\ohm}$
* dati: $R_2 = \qty{100}{\ohm}$
* dati: $R_3 = \qty{200}{\ohm}$
</left>

<right>
$R_{\mathrm{ges}} = R_1 + \frac{R_2 \cdot (R_3 + R)}{R_2 + (R_3 + R)}$
</right>

<fragment>
Per $R = \qty{0}{\ohm}$:
$R_{\mathrm{ges}} = \qty{200}{\ohm} + \frac{\qty{100}{\ohm} \cdot (\qty{200}{\ohm} + \qty{0}{\ohm})}{\qty{100}{\ohm} + \qty{200}{\ohm} + \qty{0}{\ohm}} \approx \qty{267}{\ohm}$
</fragment>

<fragment>
Per $R = \qty{1}{\kilo\ohm}$:
$R_{\mathrm{ges}} = \qty{200}{\ohm} + \frac{\qty{100}{\ohm} \cdot (\qty{200}{\ohm} + \qty{1}{\kilo\ohm})}{\qty{100}{\ohm} + \qty{200}{\ohm} +\qty{1}{\kilo\ohm}} \approx \qty{292}{\ohm}$
</fragment>

---
[question:AD110]
---
#### Procedimento di soluzione
* dati: $R_1 = R_3 = \qty{2,2}{\kilo\ohm}$
* dati: $R_2 = R_4 = \qty{220}{\ohm}$
* richiesto: $R_{\mathrm{ges}}$

<fragment>
$R_1 || R_3 + R_2 || R_4 = \qty{1100}{\ohm} + \qty{110}{\ohm} = \qty{1210}{\ohm}$
</fragment>
---
[question:AD114]
--- style="font-size: 0.7em;"
#### Procedimento di soluzione
* dati: $R_1 = \qty{10}{\kilo\ohm}$
* dati: $R_2 = \qty{2,2}{\kilo\ohm}$
* dati: $R_L = \qty{8,2}{\kilo\ohm}$
* dati: $U_B = \qty{12}{\volt}$
* richiesto: $U_2$

<fragment>
$\frac{U_2}{U_B} = \frac{R_2 \parallel R_L}{R_{\mathrm{ges}}}$
$R_2 \parallel R_L = \frac{R_2 \cdot R_L}{R_2 + R_L} = \frac{\qty{2,2}{\kilo\ohm} \cdot \qty{8,2}{\kilo\ohm}}{\qty{2,2}{\kilo\ohm} + \qty{8,2}{\kilo\ohm}} = \qty{1,74}{\kilo\ohm}$
$R_{\mathrm{ges}} = R_1 + R_2 \parallel R_L = \qty{10}{\kilo\ohm} + \qty{1,74}{\kilo\ohm} = \qty{11,74}{\kilo\ohm}$
</fragment>
<fragment>
$U_2 = \frac{R_2 \parallel R_L}{R_{\mathrm{ges}}} \cdot U_B = \frac{\qty{1,74}{\kilo\ohm}}{\qty{11,74}{\kilo\ohm}} \cdot \qty{12}{\volt} \approx \qty{1,8}{\volt}$
</fragment>
