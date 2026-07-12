## Trasformazione di impedenza nel cavo di alimentazione

* Un'impedenza caratteristica diversa dalla resistenza di carico porta, oltre alle onde stazionarie, alla trasformazione di impedenza.
* La sorgente del segnale "vede" resistenze diverse alle estremità del cavo.
* Le linee di $\lambda/4$ trasformano resistenze di carico basse in alte e alte in basse.
* Le linee di $\lambda/2$ non provocano trasformazione di impedenza.

---
[question:AG412]

---
[question:AG416]
---

### Alimentazione per dipoli a semionda e onda intera

<left>
[picture:312:a_impedanztransformation_speiseleitung:Dipolo a semionda con trasformazione di impedenza tramite linea di alimentazione]
</left>
<right>
* Dipolo a semionda: alimentato in corrente (bassa impedenza)
* Dipolo a onda intera: alimentato in tensione (alta impedenza)
</right>

---
[question:AG413]

---
[question:AG414]

---
[question:AG415]
---

### Calcolo dell'impedenza caratteristica
* Per una trasformazione di impedenza mirata, vale: $Z = \sqrt{Z_\mathrm{E} \cdot Z_\mathrm{A}}$
* L'impedenza caratteristica risulta come media geometrica tra l'impedenza di alimentazione e la resistenza di carico.

---
[question:AG417]
---
#### Percorso di soluzione
* Dato: $Z_A = \qty{60}{\ohm}$
* Dato: $Z_E = \qty{240}{\ohm}$
* Cercato: $Z$

<fragment>
$\begin{split}Z &= \sqrt{Z_E \cdot Z_A}\\ &= \sqrt{\qty{240}{\ohm} \cdot \qty{60}{\ohm}}\\ &= \qty{120}{\ohm}\end{split}$ 
</fragment>
---
[question:AG418]
---
#### Percorso di soluzione
* Dato: $Z_A = \qty{240}{\ohm}$
* Dato: $Z_E = \qty{600}{\ohm}$
* Cercato: $Z$

<fragment>
$\begin{split}Z &= \sqrt{Z_E \cdot Z_A}\\ &= \sqrt{\qty{600}{\ohm} \cdot \qty{240}{\ohm}}\\ &= \qty{380}{\ohm}\end{split}$ 
</fragment>
---

### Adattamento di impedenza con filtri a Pi

<left>
[picture:425:a_impedanztransformation_pi_filter:Filtro a Pi per la trasformazione di impedenza]
</left>
<right>
* Bobine e condensatori vengono utilizzati per l'adattamento di impedenza.
* I filtri a Pi agiscono come filtri passa-basso e trasformano l'impedenza.
* Possono essere utilizzati come accordatori d’antenna.
</right>

<note>
Il nome "filtro a Pi" deriva dalla disposizione dei componenti, che ricorda la lettera greca $\pi$ e non ha nulla a che fare con la costante Pi.
</note>

---
[question:AG406]
