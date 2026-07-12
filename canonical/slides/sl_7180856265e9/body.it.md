## Frequenza massima utilizzabile (MUF)

<left>
* Classe E: Frequenza massima con cui è possibile stabilire un collegamento tramite onda riflessa
</left>
<right>
[picture:997:e_muf_luf2:Simulazione delle distanze di salto per diverse frequenze e una MUF di circa $\qty{7,5}{\mega\hertz}$ in una notte di agosto 2024 con un angolo di emissione di $\qty{45}{\degree}$]
</right>

---

## Frequenza massima utilizzabile (MUF)

<left>
* Classe A: Dipende dall'angolo di emissione $\alpha$
</left>
<right>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
</right>

---

## Frequenza massima utilizzabile (MUF)

<left>
* Se si emette con un angolo elevato (es. $\qty{60}{\degree}$), la MUF diminuisce e l'onda radio potrebbe non essere più rifratta.
* Se si emette con un angolo basso (es. $\qty{30}{\degree}$), la MUF aumenta.
</left>
<right>
[picture:998:e_muf_winkel2:Distanza di salto a 7 MHz nell'estate 2024]
</right>

---

[question:AH206]

---

[question:AH207]

---

## Frequenza critica

<left>
* Con un angolo di emissione di $\qty{90}{\degree}$, il segnale deve compiere una rotazione di $\qty{180}{\degree}$ nella ionosfera
* Frequenza critica $f_c$ alla quale il segnale viene riflesso
* La MUF è maggiore di $f_c$, poiché di solito non si trasmette perpendicolarmente verso l'alto
</left>
<right>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
<fragment>
$\mathrm{MUF} \approx \frac{f_c}{\sin(\alpha)}$
</fragment>
</right>

<note>
La frequenza critica è indicata anche come $f_k$ o $f_\mathrm{krit}$
</note>

---

## Esempio Ionosonda Juliusruh

[picture:999:e_muf_fof2:MUF 3000 (emissione piana) e $f_\text{c}$ il 08.09.2025]

---

[question:AH208]

--- style="font-size: smaller;"
## Frequenza ottimale

* La pianificazione delle frequenze commerciali utilizza una *Frequency of optimal transmition*, frequenza di trasmissione ottimale
* Frequenza che consente un collegamento radio su un determinato percorso del segnale nel 90% di tutti i giorni statisticamente
* È inferiore del 15% alla media mensile della MUF
* $f_{\mathrm{opt}} = \mathrm{MUF}\cdot 0,85$
* Non ha molta importanza per il radioamatore, poiché non viene stabilito un collegamento permanente
* Nel radioamatore si lavora fino a quasi la MUF

---
[question:AH209]
---
### Percorso di soluzione
<left>
* dato: $\alpha = \qty{45}{\degree}$
* dato: $f_c = 3MHz$
</left>
<right>
* cercato: $\mathrm{MUF}$
* cercato: $f_{\mathrm{opt}}$
</right>

<left>
<fragment>
$\begin{split} \text{MUF} & \approx \frac{f_c}{\sin(\alpha)}\\&\approx \frac{\qty{3}{\mega\hertz}}{\num{0,71}}\\&\approx \qty{4,2}{\mega\hertz}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split} f_{\mathrm{opt}} &= \mathrm{MUF}\cdot 0,85\\ &= \qty{4,2}{\mega\hertz} \cdot 0,85\\ &= \qty{3,6}{\mega\hertz} \end{split}$
</fragment>
</right>

---
## Frequenza minima utilizzabile (LUF)

Frequenza minima con cui è possibile stabilire un collegamento tramite onda riflessa

---
[question:AH210]
---
[question:AH211]
---

## Frequenza critica

<left>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
Ripetizione
</left>
<right>
* Con un angolo di emissione di $\qty{90}{\degree}$, il segnale deve compiere una rotazione di $\qty{180}{\degree}$ nella ionosfera
* Frequenza critica $f_c$ alla quale il segnale viene riflesso
* La MUF è superiore a $f_c$, poiché di solito non si trasmette perpendicolarmente verso l'alto
</right>

<note>
La frequenza critica è indicata anche come $f_k$ o $f_\mathrm{krit}$
</note>
---

* La frequenza critica varia a seconda della regione ionosferica, del luogo e dell'ora
* Possibili indicazioni separate per regione ionosferica
* Simbolo: fo
* Completato con lo strato, ad es. foF2

<note>
fo con "o" minuscolo per onda ordinaria
</note>
---
[question:AH204]
---
[question:AH205]