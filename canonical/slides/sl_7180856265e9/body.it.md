## Frequenza massima utilizzabile (MUF)

<left>
* Classe E: Frequenza massima con cui è possibile stabilire un collegamento tramite onda spaziale
</left>
<right>
[picture:997:e_muf_luf2:Simulazione delle distanze di salto per diverse frequenze e una MUF di circa $\qty{7,5}{\mega\hertz}$ in una notte di agosto 2024 con un angolo di irradiazione di $\qty{45}{\degree}$]
</right>

---

## Frequenza massima utilizzabile (MUF)

<left>
* Classe A: Dipendente dall'angolo di irradiazione $\alpha$
</left>
<right>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
</right>

---

## Frequenza massima utilizzabile (MUF)

<left>
* Se si irradia in modo ripido (ad es. $\qty{60}{\degree}$), la MUF diminuisce e l'onda radio potrebbe non essere più rifratta.
* Se si irradia in modo piatto (ad es. $\qty{30}{\degree}$), la MUF aumenta.
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
* Con un angolo di irradiazione di $\qty{90}{\degree}$, il segnale deve compiere una rotazione di $\qty{180}{\degree}$ nell'ionosfera
* Frequenza critica $f_c$ alla quale il segnale viene riflesso
* La MUF è maggiore di $f_c$, poiché in genere non si trasmette verticalmente verso l'alto
</left>
<right>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
<fragment>
$\mathrm{MUF} \approx \frac{f_c}{\sin(\alpha)}$
</fragment>
</right>

<note>
La frequenza critica viene indicata anche come $f_k$ o $f_\mathrm{krit}$
</note>

---

## Esempio Ionosonda Juliusruh

[picture:999:e_muf_fof2:MUF 3000 (irradiazione piatta) e $f_\text{c}$ il 08.09.2025]

---

[question:AH208]

--- style="font-size: smaller;"
## Frequenza ottimale

* La pianificazione commerciale delle frequenze utilizza una *Frequency of optimal transmition*, frequenza ottimale di trasmissione
* Frequenza che, su un determinato percorso di segnale, consente statisticamente un collegamento radio nel 90% dei giorni
* Si trova il 15% al di sotto della media mensile della MUF
* $f_{\mathrm{opt}} = \mathrm{MUF}\cdot 0,85$
* Ha poca rilevanza per il radioamatoriale, poiché non si stabilisce un collegamento permanente
* Nel radioamatoriale si lavora fino a valori prossimi alla MUF

---
[question:AH209]
---
### Percorso di soluzione
<left>
* dati: $\alpha = \qty{45}{\degree}$
* dati: $f_c = 3\text{MHz}$
</left>
<right>
* richiesto: $\mathrm{MUF}$
* richiesto: $f_{\mathrm{opt}}$
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

Frequenza minima con cui è possibile stabilire un collegamento tramite onda spaziale

---
[question:AH210]
---
[question:AH211]
---

## Frequenza critica

<left>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
Ripasso
</left>
<right>
* Con un angolo di irradiazione di $\qty{90}{\degree}$, il segnale deve compiere una rotazione di $\qty{180}{\degree}$ nell'ionosfera
* Frequenza critica $f_c$ alla quale il segnale viene riflesso
* La MUF è maggiore di $f_c$, poiché in genere non si trasmette verticalmente verso l'alto
</right>

<note>
La frequenza critica viene indicata anche come $f_k$ o $f_\mathrm{krit}$
</note>
---

* La frequenza critica varia a seconda della regione ionosferica, della posizione e del tempo
* Possibili indicazioni separate per regione ionosferica
* Simbolo: fo
* Integrato dallo strato, ad es. foF2

<note>
fo con la "o" minuscola per l'onda ordinaria
</note>
---
[question:AH204]
---
[question:AH205]