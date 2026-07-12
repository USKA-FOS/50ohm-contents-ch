### Principio del Trasformatore

<left>
[photo:239:e_Trafo mit getrennten Wicklungen:Trafo mit sichtbar getrennten Wicklungen]
</left>
<right>
* Bobine accoppiate magneticamente
* Corrente variabile in una bobina
* Genera tensione nell'altra bobina
* $\rightarrow$ Induzione mutua
</right>

---
[question:AC301]
---
<style="font-size: 0.7em;">
Il rapporto tra le spire tra lato primario e secondario è come il rapporto tra la tensione primaria e secondaria, ma come il rapporto tra la corrente secondaria e primaria:

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S} = \frac{I_S}{I_P}$

<fragment>
Il rapporto tra l'impedenza primaria e secondaria è come i rapporti sopra al quadrato:

$ü^2 = \frac{Z_P}{Z_S} = \left(\frac{N_P}{N_S}\right)^2 = \left(\frac{U_P}{U_S}\right)^2 = \left(\frac{I_S}{I_P}\right)^2$
</fragment>

<fragment>
Oppure dopo aver estratto la radice:

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S} = \frac{I_S}{I_P} = \sqrt{\frac{Z_P}{Z_S}}$
</fragment>

<note>
L'ultima formula è riportata così nella raccolta di formule
</note>
---
[question:AC302]
---
#### Percorso di soluzione
* dato: $U_P = \qty{230}{\volt}$
* dato: $U_S = \qty{6}{\volt}$
* dato: $I_S = \qty{1,15}{\ampere}$
* cercato: $I_P$

<fragment>
$\begin{split} \frac{U_P}{U_S} &= \frac{I_S}{I_P} \\ \Rightarrow I_P &= \frac{I_S \cdot U_S}{U_P} = \frac{\qty{1,15}{\ampere} \cdot \qty{6}{\volt}}{\qty{230}{\volt}} \\ &= \qty{30}{\milli\ampere} \end{split}$
</fragment>

---
## Adattamento di impedenza

<left>
[picture:260:a_impedanzanpassung:Adattamento da $\qty{2450}{\ohm}$ a $\qty{50}{\ohm}$ con un trasformatore con rapporto di spire da 1 a 7]
</left>
<right>
[photo:332:a_unun:Esempio di trasformatore Unun con rapporto di spire da 2 a 14, dove il lato primario e secondario sono avvolti bifilarmente (ritorti) insieme]
</right>

---
[question:AC306]
---
#### Percorso di soluzione
* dato: $Z_P = \qty{50}{\ohm}$
* dato: $Z_S = \qty{2,5}{\kilo\ohm}$
* cercato: $ü$

<fragment>
$\begin{split} ü &= \sqrt{\frac{Z_P}{Z_S}} = \sqrt{\frac{\qty{50}{\ohm}}{\qty{2,5}{\kilo\ohm}}} \\ &= \sqrt{\frac{1}{50}} \approx \frac{1}{7} \end{split}$
</fragment>

---
[question:AC303]
---
#### Percorso di soluzione
* dato: $Z_S = \qty{16}{\kilo\ohm}$
* dato: $ü = \frac{1}{4}$
* cercato: $Z_P$

<fragment>
$\begin{split} ü &= \sqrt{\frac{Z_P}{Z_S}} \\ \Rightarrow Z_P &= ü^2 \cdot Z_S = \frac{1^2}{4^2} \cdot \qty{16}{\kilo\ohm} \\ &= \frac{\qty{16}{\kilo\ohm}}{16} = \qty{1}{\kilo\ohm} \end{split}$
</fragment>

---
[question:AC304]
---
#### Percorso di soluzione
* dato: $Z_S = \qty{6,4}{\kilo\ohm}$
* dato: $ü = \frac{1}{4}$
* cercato: $Z_P$

<fragment>
$\begin{split} ü &= \sqrt{\frac{Z_P}{Z_S}} \\ \Rightarrow Z_P &= ü^2 \cdot Z_S = \frac{1^2}{4^2} \cdot \qty{6,4}{\kilo\ohm} \\ &= \frac{\qty{6,4}{\kilo\ohm}}{16} = \qty{0,4}{\kilo\ohm} \end{split}$
</fragment>

---
[question:AC305]
---
#### Percorso di soluzione
* dato: $Z_P = \qty{450}{\ohm}$
* dato: $Z_S = \qty{50}{\ohm}$
* cercato: $ü$

<fragment>
$\begin{split} ü &= \sqrt{\frac{Z_P}{Z_S}} = \sqrt{\frac{\qty{450}{\ohm}}{\qty{50}{\ohm}}} \\ &= \sqrt{\frac{9}{1}} = \frac{3}{1} \end{split}$
</fragment>


---
### Corrente massima
<left>
* La linea non deve scaldare troppo
* Altrimenti l'isolamento si scioglie
* O il conduttore si surriscalda
* $\rightarrow$ Densità della corrente ammissibile in relazione all'intensità di corrente rispetto alla sezione del conduttore
</left>
<right>
<fragment>
[photo:236:e_HF Übertrager:Trasformatore HF (BALUN) che può sciogliersi con troppa potenza]
</fragment>
</right>
<note>
I BALUN autocostruiti sciolti in custodie di plastica sono più comuni quando si applica "solo un po' più di potenza"
</note>

---
### Esempi di densità della corrente ammissibile

secondo VDE

* Conduttori in Rame liberi: $\frac{\qty{12}{\ampere}}{\qty{0,75}{\milli\meter\squared}}$
* Fusibili: fino a $\qty{3000}{\ampere\per\milli\meter\squared}$
* Trasformatori: $\qty{2,5}{\ampere\per\milli\meter\squared}$ (scarsa dissipazione del calore degli avvolgimenti)

---
[question:AC307]
---
#### Percorso di soluzione
* dato: $d = \qty{0,5}{\milli\meter}$
* dato: Densità della corrente $\frac{I}{A} = \frac{\qty{2,5}{\ampere}}{\qty{1}{\milli\meter\squared}}$
* cercato: $I_{\mathrm{max}}$

<fragment>
$A_{Dr} = \frac{d^2 \cdot \pi}{4} = \frac{(\qty{0,5}{\milli\meter})^2 \cdot \pi}{4} \approx \qty{0,196}{\milli\meter\squared}$
</fragment>
<fragment>
$I_{\mathrm{max}} = \frac{I}{A} \cdot A_{Dr} = \frac{\qty{2,5}{\ampere}}{\qty{1}{\milli\meter\squared}} \cdot \qty{0,196}{\milli\meter\squared} = \qty{0,49}{\ampere}$
</fragment>
