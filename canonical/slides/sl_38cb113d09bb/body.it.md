## Decibel

* Indicazione logaritmica di rapporti, in particolare per le potenze
* Semplifica il lavoro con potenze piccole e grandi
* Amplificazioni e attenuazioni possono essere calcolate più facilmente

---

## Perché i decibel?

[picture:877:e_signalkette:Catena di segnale con tre amplificatori]

[picture:1053:e_signalkette_2:Catena di segnale con due amplificatori e un attenuatore]

--- style="font-size: 0.7em;"
## Livello di potenza

Fattore 10

*Potenza riferita a $\qty{1}{\milli\watt}$*
$p = 10\cdot \log_{10}\left(\frac{P}{\qty{1}{\milli\watt}}\right)\unit{\dBm}$
<fragment>
$\rightarrow\qty{0}{\dBm}$ corrisponde a $P = \qty{1}{\milli\watt}$
</fragment>

<fragment>
*Potenza riferita a $\qty{1}{\watt}$*
$p = 10\cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}$
</fragment>
<fragment>
$\rightarrow\qty{0}{\dBW}$ corrisponde a $P = \qty{1}{\watt}$
</fragment>

---
[question:AD428]
---
#### Procedimento di soluzione
* dato: $P_1 = \qty{38}{\watt}$
* dato: $P_2 = \qty{2,5}{\watt}$
* cercato: $g$


<fragment>
$\begin{split} g &= \qty{10\cdot \log_{10}{\left(\frac{P_2}{P_1}\right)}}{\dB}\\ &= \qty{10\cdot \log_{10}{\left(\frac{\qty{38}{\watt}}{\qty{2,5}{\watt}}\right)}}{\dB} = \qty{11,8}{\dB} \end{split}$
</fragment>

---
[question:AA110]
<note>
Solo inserire
</note>
---
[question:AA105]

---
--- style="font-size: 0.7em;"

## Livello di tensione

Fattore $20$


u = 20\cdot \log_{10}\left(\frac{U}{\qty{0,775}{\volt}}\right)\unit{\dBu}$


<fragment>
*Tensione riferita a $\qty{0,775}{\volt}$*
$\rightarrow\qty{0}{\dBu}$ corrisponde a $U = \qty{0,775}{\volt}$
</fragment>
<fragment>
*Tensione riferita a $\qty{1}{\volt}$*
$\rightarrow\qty{0}{\dBV}$ corrisponde a $U = \qty{1}{\volt}$
</fragment>
<fragment>
*Tensione riferita a $\qty{1}{\micro\volt}$*
$\rightarrow\qty{0}{\dBuV}$ corrisponde a $U = \qty{1}{\micro\volt}$
</fragment>

<note>
I dettagli sul calcolo del fattore 20 sono nel corso online. In breve: nel rapporto di tensione si opera con i quadrati, che possono essere estratti come fattore dal logaritmo.
</note>

---

[question:AD427]

---
#### Procedimento di soluzione
* dato: $U_1 = \qty{1}{\milli\volt}$
* dato: $U_2 = \qty{4}{\milli\volt}$
* cercato: $g$


<fragment>
$\begin{split} g &= \qty{20\cdot \log_{10}{\left(\frac{U_2}{U_1}\right)}}{\dB}\\ &= \qty{20\cdot \log_{10}{\left(\frac{\qty{4}{\milli\volt}}{\qty{1}{\milli\volt}}\right)}}{\dB} = \qty{12}{\dB} \end{split}$
</fragment>

---

[question:AA111]

---
[question:AA108]

---

### Procedimento di soluzione
* dato: $p = \qty{20}{\dBW}$
* cercato: $P$


<fragment>
$\begin{split} p &= 10\cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}\\ \Rightarrow P &= 10^{\frac{p}{10}} \cdot \qty{1}{\watt} = 10^{\frac{\qty{20}{\dBW}}{10}} \cdot \qty{1}{\watt} = \qty{10^2}{\watt} \end{split}$
</fragment>
---
[question:AA107]
---
[question:AA109]
---
### Procedimento di soluzione

$\qty{1}{\watt} = \qty{1000}{\milli\watt}$
$\qty{10}{\dB} = \text{Fattore 10}$
$\qty{1000}{\milli\watt} \cdot 10 = \qty{10000}{\milli\watt} = \qty{40}{\dBm}$
---
[question:AA106]
---
## Procedimento di soluzione
* $\qty{16}{\dB} = \qty{10}{\dB} + \qty{6}{\dB} = 10 \cdot 4 = 40$
* $\qty{1}{\watt} \cdot 40 = \qty{40}{\watt}$

<note>
Dalla tabella nella raccolta di formule
</note>

---
[question:AD426]
---
#### Procedimento di soluzione
* dato: $g = \qty{16}{\dB}$
* dato: $P_1 = \qty{1}{\watt}$
* cercato: $P_2$


<fragment>
$g = \qty{16}{\dB} = \qty{10}{\dB} + \qty{6}{\dB} = 10 \cdot 4 = 40$
</fragment>
<fragment>
$P_2 = P_1 \cdot g = \qty{1}{\watt} \cdot 40 = \qty{40}{\watt}$
</fragment>

---
[question:AA112]
---
### Procedimento di soluzione
* dato: $u = \qty{120}{\dBuV\per\meter}$
* cercato: $U$


<fragment>
$\begin{split} u &= 20\cdot \log_{10}\left(\frac{U}{\qty{1}{\micro\volt}}\right)\unit{\dBuV}\\ \Rightarrow U &= 10^{\frac{u}{20}} \cdot \qty{1}{\micro\volt} = 10^{\frac{\qty{120}{\dBuV\per\meter}}{20}} \cdot \qty{1}{\micro\volt} = \qty{1}{\volt\per\meter} \end{split}$
</fragment>
<fragment>
In letteratura si trova spesso: $\qty{120}{\dBuV} = \qty{1}{\volt}$
