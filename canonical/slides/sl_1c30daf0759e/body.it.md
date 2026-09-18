<left>
[photo:267:a_U_eilt_vor:Sfasamento di fase tra tensione e corrente in una bobina]
</left>
<right>
* Sfasamento di fase di $\qty{90}{\degree}$
* La tensione precede la corrente
</right>
<note>
Da ricordare: Nelle induttanze, le correnti si ritardano -oppure- Induttività, la corrente è in ritardo!
</note>

---
[question:AC201]

---
### Potenza attiva

<left>
[picture:944:a_Blindleistung Spule:Il prodotto di $U \cdot I$ genera la curva verde della potenza]
</left>
<right>
* La curva verde della potenza è il prodotto di corrente e tensione
* La potenza oscilla simmetricamente intorno alla linea dello zero e si bilancia
* *Potenza reattiva* su una *reattanza*
</right>

---

* La reattanza non assorbe energia attiva
* Una bobina ideale non si scalda
* Tuttavia, una bobina è realizzata con un filo e presenta quindi perdite ohmiche
* Inoltre, agisce l'*effetto pelle*

---
[question:AC202]

--- style="font-size: smaller;"
### Reattanza induttiva $X_{\textrm{L}}$

La bobina, collegata a tensione alternata, genera continuamente un campo magnetico variabile $\rightarrow$ impedenza / *reattanza induttiva*

1. Se la frequenza della tensione alternata in una bobina aumenta, la corrente diminuisce; ciò significa che la reattanza induttiva è maggiore.
2. Se l'*induttanza* della bobina aumenta, la corrente diminuisce ulteriormente, cioè la reattanza aumenta anch'essa.

<fragment>
$|X_{\textrm{L}}| = \omega \cdot L = 2\pi \cdot f \cdot L$
</fragment>

---
[question:AC203]
---
[question:AC204]
---
#### Procedimento di soluzione
* dati: $L = \qty{3}{\micro\henry}$
* dati: $f = \qty{100}{\mega\hertz}$
* richiesto: $X_{\textrm{L}}$

<fragment>
$\begin{split} |X_{\textrm{L}}| &= \omega \cdot L = 2\pi \cdot f \cdot L\\ &= 2\pi \cdot \qty{100}{\mega\hertz} \cdot \qty{3}{\micro\henry}\\ &\approx \qty{1885}{\ohm} \end{split}$
</fragment>

---
### Aumento dell'induttanza
<left>
Bobina cilindrica
<fragment>
$L = \dfrac{\mu_0 \cdot \mu_r \cdot N^2 \cdot A_S}{l}$
</fragment>

* Aumentare il numero di spire $N$
* Ridurre la lunghezza della bobina $l$
* Ingrandire la sezione trasversale $A_S$ della bobina

</left>
<right>
Bobina a nucleo toroidale
<fragment>
$L = N^2 \cdot A_{\textrm{L}}$
</fragment>

* Aumentare il numero di spire $N$
* Utilizzare un *materiale* con maggiore conducibilità magnetica (con costante di induttanza $A_{\textrm{L}}$ maggiore) come nucleo

</right>

<note>
Per questo motivo si utilizzano nuclei (toroidali)
</note>
---
[question:AC211]

---
[question:AC205]
---
#### Procedimento di soluzione
* dati: $N = 14$
* dati: $A_{\textrm{L}} = \qty{1,5}{\nano\henry}$
* richiesto: $L$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ &= 14^2 \cdot \qty{1,5}{\nano\henry}\\ &= \qty{0,294}{\micro\henry} \end{split}$
</fragment>

---
[question:AC206]
---
#### Procedimento di soluzione
* dati: $N = 300$
* dati: $A_{\textrm{L}} = \qty{1250}{\nano\henry}$
* richiesto: $L$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ &= 300^2 \cdot \qty{1250}{\nano\henry}\\ &= \qty{112,5}{\milli\henry} \end{split}$
</fragment>

---
[question:AC207]
---
#### Procedimento di soluzione
* dati: $L = \qty{2}{\milli\henry}$
* dati: $A_{\textrm{L}} = \qty{250}{\nano\henry}$
* richiesto: $N$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ N &= \sqrt{\frac{L}{A_{\textrm{L}}}} = \sqrt{\frac{\qty{2}{\milli\henry}}{\qty{250}{\nano\henry}}} \\ &= 89\,\text{spire} \end{split}$
</fragment>

---
[question:AC208]
---
#### Procedimento di soluzione
* dati: $L = \qty{12}{\micro\henry}$
* dati: $A_{\textrm{L}} = \qty{30}{\nano\henry}$
* richiesto: $N$

<fragment>
$\begin{split} L &= N^2 \cdot A_{\textrm{L}}\\ N &= \sqrt{\frac{L}{A_{\textrm{L}}}} = \sqrt{\frac{\qty{12}{\micro\henry}}{\qty{30}{\nano\henry}}} \\ &= 20\,\text{spire} \end{split}$
</fragment>

---
### Perdite della bobina

* Fattore di perdita $\tan(\delta) = \frac{R}{X_L}$
* Perdite nel conduttore

---
[question:AC209]

---
### Impedenza

* Circuito in *serie* di reattanza e resistenza attiva $\rightarrow$ impedenza $Z$
* Si verifica solo con tensione alternata
* Non può essere misurata con un ohmetro
* Bobina nella tecnica radio $\rightarrow$ *impedenza*
* Impedenza dell'antenna, impedenza di ingresso e di uscita, adattatori di impedenza, …
* Impedenza $Z$ in $\unit{\ohm}$

---
<left>
[picture:1067:a_impedanzdreieck:Impedenza $Z$ come somma geometrica di $R$ e $X$]

$Z = \sqrt{R^2 + X^2}$
</left>
<right>
* Resistenza attiva $R$
* Reattanza $X_{\textrm{L}}$
* L'impedenza si calcola con il teorema di Pitagora
</right>

---
[question:AA101]

---
### Schermatura dei campi magnetici

<left>
* Per la schermatura: un involucro in *materiale* altamente conduttivo.
* Esempio: copertura di schermatura in acciaio o ferro.
* Nucleo ferritico regolabile per modificare l'induttanza.
</left>
<right>
[photo:333:a_abschirmbecher:Esempio di bobine con copertura di schermatura per la schermatura dei campi magnetici]
</right>


---
[question:AC210]
