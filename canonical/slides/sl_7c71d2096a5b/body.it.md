## Campo vicino e sua suddivisione

* Il campo vicino si divide in campo vicino reattivo e campo vicino radiante
* Nella maggior parte dei casi, il campo vicino radiante può essere trattato come il campo lontano

---
### Campo vicino reattivo

* Nel campo vicino reattivo non esiste una relazione di fase costante tra intensità di campo elettrica e magnetica

---
[question:AK101]

---
## Campo lontano e relazione di fase costante

* Una relazione di fase costante tra intensità di campo elettrica e magnetica si verifica solo nel campo lontano
* Il vero campo lontano inizia solo a $4\cdot\lambda$
* Se la formula approssimata del campo lontano viene utilizzata nel campo vicino radiante, si ottiene un valore di intensità di campo più elevato e conservativo
* Questo non vale per antenne magnetiche e antenne molto corte

---
### Transizione dal campo vicino reattivo al campo vicino radiante

* La transizione dipende dalla lunghezza d’onda
* Condizione soddisfatta: $d > \frac{\lambda}{2\pi}$
* Esempio: Per $\lambda = \qty{20}{\meter}$, la transizione si verifica a circa $d \approx \qty{3,18}{\meter}$

---
### Distanze di protezione per le persone nel campo lontano

* Nel campo lontano può essere applicata una formula approssimata per calcolare le distanze di protezione per le persone
* Formula: $d = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_{\textrm{EIRP}}}}{E}$
* Vale per la maggior parte delle forme di antenna, se è soddisfatta la condizione $d > \frac{\lambda}{2\pi}$
* Per antenne piccole o distanze di sicurezza nel campo vicino, la formula non è applicabile

---
[question:AK103]

## Definizione del campo lontano

* Nel campo lontano, i vettori dell’intensità di campo elettrica (E), dell’intensità di campo magnetica (H) e della direzione di propagazione sono perpendicolari tra loro
* Non ci sono differenze di fase tra E e H
* L’impedenza d’onda del campo corrisponde a quella dello spazio libero

---
### Confine tra campo vicino e campo lontano

* Il confine dipende principalmente dalla lunghezza d’onda
* Per antenne a filo (ad es. dipoli), il campo lontano si forma tipicamente a una distanza di circa $4\cdot\lambda$
* Condizione di transizione nel campo vicino: $d > \frac{\lambda}{2\pi}$; per $\lambda = \qty{20}{\meter}$ circa $d \approx \qty{3,18}{\meter}$

---
### Applicazione della formula approssimata del campo lontano

* La formula approssimata $d = \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{E}$ vale per la maggior parte delle forme di antenna
* Viene applicata quando la distanza di sicurezza calcolata si trova nel campo vicino radiante o nel campo lontano
* La formula evita misurazioni o simulazioni complesse per determinare le distanze di protezione per le persone

---
### Procedura di valutazione secondo BEMFV

<left>
[photo:80:n_Bewertungsverfahren:In questo documento sono descritte le procedure di valutazione.]
</left>
<right>
Nelle [spiegazioni delle procedure di valutazione secondo BEMFV](https://50ohm.de/bemfv) l’Ufficio federale delle comunicazioni (BNetzA) ha descritto i concetti e le procedure per determinare le distanze di sicurezza.
</right>