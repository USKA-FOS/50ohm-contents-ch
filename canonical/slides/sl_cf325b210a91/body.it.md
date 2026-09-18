## Trasformazione dell’impedenza nella linea di alimentazione

* Se l’impedenza caratteristica non corrisponde alla resistenza di carico, oltre alle onde stazionarie si verifica anche una trasformazione dell’impedenza
* La sorgente del segnale "vede" resistenze diverse alle estremità del cavo
* Le linee di $\lambda/4$ trasformano le resistenze piccole in grandi e quelle grandi in piccole
* Le linee di $\lambda/2$ non provocano alcuna trasformazione dell’impedenza

---
[question:AG412]

---
[question:AG416]
---

### Alimentazione di dipoli a semionda e a onda intera

<left>
[picture:312:a_impedanztransformation_speiseleitung:Dipolo a semionda con trasformazione dell’impedenza tramite linea di alimentazione]
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

### Calcolo dell’impedenza caratteristica
* Per una trasformazione mirata dell’impedenza vale: $Z = \sqrt{Z_\mathrm{E} \cdot Z_\mathrm{A}}$
* L’impedenza caratteristica risulta essere la media geometrica tra impedenza di alimentazione e resistenza di carico

---
[question:AG417]
---
#### Procedimento di soluzione
* dato: $Z_A = \qty{60}{\ohm}$
* dato: $Z_E = \qty{240}{\ohm}$
* cercato: $Z$

<fragment>
$\begin{split}Z &= \sqrt{Z_E \cdot Z_A}\\ &= \sqrt{\qty{240}{\ohm} \cdot \qty{60}{\ohm}}\\ &= \qty{120}{\ohm}\end{split}$ 
</fragment>
---
[question:AG418]
---
#### Procedimento di soluzione
* dato: $Z_A = \qty{240}{\ohm}$
* dato: $Z_E = \qty{600}{\ohm}$
* cercato: $Z$

<fragment>
$\begin{split}Z &= \sqrt{Z_E \cdot Z_A}\\ &= \sqrt{\qty{600}{\ohm} \cdot \qty{240}{\ohm}}\\ &= \qty{380}{\ohm}\end{split}$ 
</fragment>
---

### Adattamento dell’impedenza con filtri Pi

<left>
[picture:425:a_impedanztransformation_pi_filter:Filtro Pi per adattamento dell’impedenza]
</left>
<right>
* Per l’adattamento dell’impedenza si utilizzano induttori e condensatori
* I filtri Pi agiscono come filtri passa-basso e trasformano l’impedenza
* Possono essere impiegati come accordatori d’antenna
</right>

<note>
Il nome "filtro Pi" deriva dall’aspetto dei componenti, che ricorda la lettera greca $\pi$, e non ha nulla a che fare con la *costante Pi*.
</note>

---
[question:AG406]
