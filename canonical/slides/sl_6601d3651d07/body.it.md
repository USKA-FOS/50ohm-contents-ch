## Tipi di batterie

I tipi di batterie più comuni nel radioamatore:
* Batteria al piombo (Pb)
* Nichel-metallo idruro (NiMH)
* Litio-ferro-fosfato (LiFePO4)

---
[photo:175:a_akku_lifepo4:LiFePO4]

<left>
* Capacità: $\qty{4200}{\milli\ampere\hour}$
* Tensione: 4S1P / $\qty{13,2}{\volt}$
</left>
<right>
* Scarica: 30C costante / 40C burst
* Connettore bilanciamento: JST-XH
</right>

---
### Collegamenti

Esempi:

* 4S1P: 4 celle in serie, 1 in parallelo
* 4S2P: 4 celle in serie, 2 in parallelo

<fragment>
Per cella circa $\qty{3,2}{\volt}$ fino a $\qty{3,3}{\volt}$, quindi<br/>$\qty{3,3}{\volt} \cdot 4 = \qty{13,2}{\volt}$
</fragment>

---
### Capacità

Batteria di esempio: $\qty{4200}{\milli\ampere\hour} = \qty{4,2}{\ampere\hour}$

<fragment>
$\rightarrow$ Caricare per 1 ora con $\qty{4,2}{\ampere}$ o per 2 ore con $\qty{2,1}{\ampere}$
</fragment>
<fragment>
$t = \frac{Q}{I}$
</fragment>
<fragment>
$t = \frac{\qty{4,2}{\ampere\hour}}{\qty{4,2}{\ampere}} = \qty{1}{\hour}$
</fragment>
<note>
convertire eventualmente le ore in secondi con $\qty{1}{\hour} = \qty{3600}{\second}$ 
</note>
---
### Energia elettrica

Energia elettrica immagazzinata nella batteria

$E = Q \cdot U$

<fragment>
Batteria di esempio: $E = \qty{4,2}{\ampere\hour} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\hour}$
</fragment>
---
### Corrente di scarica

Indicazione sulla batteria di esempio: 30C

La scarica può avvenire con 30 volte la capacità $Q$

<fragment>
Corrente di scarica = $30 \cdot \frac{1}{\unit{\hour}} \cdot \qty{4,2}{\ampere\hour} = \qty{126}{\ampere}$
</fragment>

<fragment>
La batteria si scaricherebbe in 128 secondi.
</fragment>

<note>
Considerare la sezione del cavo
</note>

---
### Collegamento in serie di batterie

<left>
[photo:176:a_akku_4S1P:Collegamento in serie]
</left>
<right>
* Le tensioni si sommano
* Collegare solo celle con dati uguali
</right>
<note>
In caso di dati diversi, le celle si influenzano o si danneggiano
</note>

---
### Collegamento in parallelo di batterie

<left>
[photo:177:a_akku_4S2P:Collegamento in parallelo]
</left>
<right>
* Le tensioni rimangono uguali
* Le capacità si sommano
</right>
<note>
</note>

---
### Bilanciatore

<left>
[photo:178:a_akku_lifepo4_anschluss:Connessioni LiFePO4]
</left>
<right>
* Il connettore del bilanciatore può accedere alla tensione di ogni cella
* Circuito del bilanciatore per compensare le tensioni
* Protezione delle celle
* Monitor batteria
</right>
<note>
</note>

---
[question:AB210]
---
[question:AB209]
---
#### Percorso di soluzione
* dato: $U = \qty{2}{\volt}$
* dato: $Q = \qty{10}{\ampere\hour}$
* dato: $N = 6$
* cercato: $U_{\mathrm{totale}}, Q_{\mathrm{totale}}$

<fragment>
$U_{\mathrm{totale}} = N \cdot U = 6 \cdot \qty{2}{\volt} = \qty{12}{\volt}$
</fragment>
<fragment>
$Q_{\mathrm{totale}} = Q \cdot 1 = \qty{10}{\ampere\hour}$
</fragment>
---

[question:AB211]
---
#### Percorso di soluzione
* dato: $Q_{\mathrm{max}} = \qty{60}{\ampere\hour}$
* dato: $Q_{\qty{10}{\percent}} = 0,1 \cdot Q_\mathrm{max} = \qty{6}{\ampere\hour}$
* dato: $I = \qty{0,8}{\ampere}$
* cercato: $t$

<fragment>
$Q = I \cdot t \Rightarrow t = \frac{Q}{I} = \frac{Q_{\mathrm{max}} - Q_{10\%}}{I} = \frac{\qty{54}{\ampere\hour}}{\qty{0,8}{\ampere}} = \qty{67,5}{\hour}$
</fragment>

---
[question:AB501]
---
#### Percorso di soluzione
* dato: $U = \qty{12}{\volt}$
* dato: $Q = \qty{5}{\ampere\hour}$
* cercato: $W$

<fragment>
$W = P \cdot t = U \cdot I \cdot t = U \cdot Q = \qty{12}{\volt} \cdot \qty{5}{\ampere\hour} = \qty{60,0}{\watt\hour}$
</fragment>