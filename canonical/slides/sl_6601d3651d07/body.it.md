## Tipi di accumulatori

I tipi di accumulatori più comuni nel radioamatoriale:
* Accumulatore al piombo (Pb)
* Nickel-metallo idruro (NiMH)
* Litio-fosfato di ferro (LiFePO₄)

---
[photo:175:a_akku_lifepo4:LiFePO₄]

<left>
* Capacità: $\qty{4200}{\milli\ampere\hour}$
* Tensione: 4S1P / $\qty{13,2}{\volt}$
</left>
<right>
* Scarica: 30C costante / 40C burst
* Connettore di bilanciamento: JST-XH
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

Esempio di accumulatore: $\qty{4200}{\milli\ampere\hour} = \qty{4,2}{\ampere\hour}$

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
Eventualmente convertire le ore in secondi con $\qty{1}{\hour} = \qty{3600}{\second}$
</note>
---
### Energia elettrica

Energia elettrica immagazzinata nell'accumulatore

$E = Q \cdot U$

<fragment>
Esempio di accumulatore: $E = \qty{4,2}{\ampere\hour} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\hour}$
</fragment>
---
### Corrente di scarica

Dati dell'esempio di accumulatore: 30C

La scarica può avvenire con 30 volte la capacità $Q$

<fragment>
Corrente di scarica = $30 \cdot \frac{1}{\unit{\hour}} \cdot \qty{4,2}{\ampere\hour} = \qty{126}{\ampere}$
</fragment>

<fragment>
L'accumulatore si scaricherebbe in 128 secondi.
</fragment>

<note>
Attenzione alla sezione dei cavi
</note>

---
### Collegamento in serie di accumulatori

<left>
[photo:176:a_akku_4S1P:collegamento in serie]
</left>
<right>
* Le tensioni si sommano
* Collegare solo celle con dati identici
</right>
<note>
Con dati non omogenei le celle si influenzano o danneggiano reciprocamente
</note>

---
### Collegamento in parallelo di accumulatori

<left>
[photo:177:a_akku_4S2P:collegamento in parallelo]
</left>
<right>
* Le tensioni rimangono invariate
* Le capacità si sommano
</right>
<note>
</note>

---
### Bilanciatore

<left>
[photo:178:a_akku_lifepo4_anschluss:Connessioni LiFePO₄]
</left>
<right>
* Il connettore del bilanciatore permette l'accesso alla tensione di ogni cella
* Circuito di bilanciamento per l'equilibrio delle tensioni
* Protezione delle celle
* Monitor della batteria
</right>
<note>
</note>

---
[question:AB210]
---
[question:AB209]
---
#### Soluzione
* dati: $U = \qty{2}{\volt}$
* dati: $Q = \qty{10}{\ampere\hour}$
* dati: $N = 6$
* richiesto: $U_{\mathrm{tot}}, Q_{\mathrm{tot}}$

<fragment>
$U_{\mathrm{tot}} = N \cdot U = 6 \cdot \qty{2}{\volt} = \qty{12}{\volt}$
</fragment>
<fragment>
$Q_{\mathrm{tot}} = Q \cdot 1 = \qty{10}{\ampere\hour}$
</fragment>
---

[question:AB211]
---
#### Soluzione
* dati: $Q_{\mathrm{max}} = \qty{60}{\ampere\hour}$
* dati: $Q_{\qty{10}{\percent}} = 0,1 \cdot Q_\mathrm{max} = \qty{6}{\ampere\hour}$
* dati: $I = \qty{0,8}{\ampere}$
* richiesto: $t$

<fragment>
$Q = I \cdot t \Rightarrow t = \frac{Q}{I} = \frac{Q_{\mathrm{max}} - Q_{10\%}}{I} = \frac{\qty{54}{\ampere\hour}}{\qty{0,8}{\ampere}} = \qty{67,5}{\hour}$
</fragment>

---
[question:AB501]
---
#### Soluzione
* dati: $U = \qty{12}{\volt}$
* dati: $Q = \qty{5}{\ampere\hour}$
* richiesto: $W$

<fragment>
$W = P \cdot t = U \cdot I \cdot t = U \cdot Q = \qty{12}{\volt} \cdot \qty{5}{\ampere\hour} = \qty{60,0}{\watt\hour}$
</fragment>