<left>
[picture:342:daempfungsglied_pi:Attenuatore in configurazione PI con sorgente e resistenza di carico]
</left>
<right>
* Riduzione del livello del segnale a un valore definito
* Evita sovraeccitazione o danni agli strumenti di misura
* Riduce la potenza d’ingresso per amplificatori e ricevitori a un livello definito
</right>
<note>
Il nome "configurazione PI" deriva dalla struttura delle resistenze a forma di &Pi;
</note>

---
<left>
[picture:342:daempfungsglied_pi:Attenuatore in configurazione PI con sorgente e resistenza di carico]
</left>
<right>
* Attenuazione tramite resistenze e conversione in calore
* Negli attenuatori simmetrici, le impedenze d’ingresso e d’uscita sono uguali
* Generalmente $\qty{50}{\ohm}$
</right>

---
<left>
[picture:341:daempfungsglied_t:Attenuatore in configurazione T con sorgente e resistenza di carico]
</left>
<right>
* L’attenuazione è espressa in $\unit{\dB}$
* ad es. $\qty{20}{\dB}$ = fattore $\num{100}$
* $\qty{100}{\watt}$ di potenza d’ingresso $\rightarrow\qty{1}{\watt}$ di potenza d’uscita
</right>
<note>
Il nome "configurazione T" deriva dalla struttura delle resistenze a forma di T
</note>

---
[question:AD806]
--- style="font-size: smaller;"
#### Procedimento di soluzione
* dati: $P_1 = \qty{100}{\watt}$
* dati: $a = \qty{20}{\dB}$
* cercato: $\Delta P = P_2 - P_1$

<fragment>
$\begin{split} a &= \qty{10 \cdot \log_{10}{\left(\frac{P_1}{P_2}\right)}}{\dB}\\ \Rightarrow \frac{a}{\qty{10}{\dB}} &= \log_{10}{\left(\frac{P_1}{P_2}\right)}\\ \Rightarrow 10^{\frac{a}{\qty{10}{\dB}}} &= \frac{P_1}{P_2}\\ \Rightarrow P_2 &= \frac{P_1}{10^{\frac{a}{\qty{10}{\dB}}}}\end{split}$
</fragment>
---
<fragment>
$P_2 = \frac{P_1}{10^{\frac{a}{10}}} = \frac{\qty{100}{\watt}}{10^{\frac{20}{10}}} = \qty{1}{\watt}$
</fragment>
<fragment>
$\Delta P = P_2 - P_1 = \qty{100}{\watt} - \qty{1}{\watt} = \qty{99}{\watt}$
</fragment>
---
[question:AD803]
---
#### Procedimento di soluzione

* $\qty{20}{\dB}$ corrispondono a un’attenuazione di potenza con fattore $\num{100}$

---
[question:AD804]
---
#### Procedimento di soluzione

* $\qty{6}{\dB}$ corrispondono a un’attenuazione di potenza con fattore $\num{4}$

---
[question:AD805]
---
#### Procedimento di soluzione

* L’impedenza del circuito complessivo non cambia – quindi $\qty{50}{\ohm}$

---
[question:AD801]
---
[question:AD802]