## Akku-Typen

Die häufigsten Akku-Typen im Amateurfunk:
* Bleiakku (Pb)
* Nickel-Metallhydrid (NiMH)
* Lithium-Eisenphosphat (LiFePO4)

---
[photo:175:a_akku_lifepo4:LiFePO4]

<left>
* Kapazität: $\qty{4200}{\milli\ampere\hour}$
* Spannung: 4S1P / $\qty{13,2}{\volt}$
</left>
<right>
* Entladung: 30C Constant / 40C Burst
* Balance-Stecker: JST-XH
</right>

---
### Verschaltungen

Beispiele:

* 4S1P: 4 Zellen in Serie, 1 in Parallel
* 4S2P: 4 Zellen in Serie, 2 in Parallel

<fragment>
Pro Zelle ca. $\qty{3,2}{\volt}$ bis $\qty{3,3}{\volt}$, also<br/>$\qty{3,3}{\volt} \cdot 4 = \qty{13,2}{\volt}$
</fragment>

---
### Kapazität

Beispiel-Akku: $\qty{4200}{\milli\ampere\hour} = \qty{4,2}{\ampere\hour}$

<fragment>
$\rightarrow$ 1 Stunde mit $\qty{4,2}{\ampere}$ oder 2 Stunden mit $\qty{2,1}{\ampere}$ belasten
</fragment>
<fragment>
$t = \frac{Q}{I}$
</fragment>
<fragment>
$t = \frac{\qty{4,2}{\ampere\hour}}{\qty{1}{\ampere}} = \qty{1}{\hour}$
</fragment>
<note>
ggf. Stunden in Sekunden mit $\qty{1}{\hour} = \qty{3600}{\second}$ umrechnen
</note>
---
### Elektrische Energie

Gespeicherte elektrische Energie im Akku

$E = Q \cdot U$

<fragment>
Beispiel-Akku: $E = \qty{4,2}{\ampere\hour} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\hour}$
</fragment>
---
### Entladestrom

Angabe auf dem Beispiel-Akku: 30C

Die Entladung kann mit 30 mal der Kapazität $Q$ erfolgen

<fragment>
Entladestrom = $30 \cdot \frac{1}{\unit{\hour}} \cdot \qty{4,2}{\ampere\hour} = \qty{126}{\ampere}$
</fragment>

<fragment>
Der Akku wäre in 128 Sekunden entladen.
</fragment>

<note>
Kabelquerschnitt ist zu beachten
</note>

---
### Reihenschaltung von Akkus

<left>
[photo:176:a_akku_4S1P:Reihenschaltung]
</left>
<right>
* Spannungen addieren sich
* Nur Zellen mit gleichen Daten zusammenschalten
</right>
<note>
Bei ungleichen Daten beeinflussen oder beschädigen sich die Zellen
</note>

---
### Parallelschaltung von Akkus

<left>
[photo:177:a_akku_4S2P:Parallelschaltung]
</left>
<right>
* Spannungen bleiben gleich
* Kapazitäten addieren sich
</right>
<note>
</note>

---
### Balancer

<left>
[photo:178:a_akku_lifepo4_anschluss:LiFePO4 Anschlüsse]
</left>
<right>
* Balanceranschluss kann auf die Spannung jeder Zelle zugreifen
* Balancerschaltung zum Ausgleich der Spannungen
* Schutz der Zellen
* Batteriemonitor
</right>
<note>
</note>

---
[question:AB210]
---
[question:AB209]
---
#### Lösungsweg
* gegeben: $U = \qty{2}{\volt}$
* gegeben: $Q = \qty{10}{\ampere\hour}$
* gegeben: $N = 6$
* gesucht: $U_{\mathrm{ges}}, Q_{\mathrm{ges}}$

<fragment>
$U_{\mathrm{ges}} = N \cdot U = 6 \cdot \qty{2}{\volt} = \qty{12}{\volt}$
</fragment>
<fragment>
$Q_{\mathrm{ges}} = Q \cdot 1 = \qty{10}{\ampere\hour}$
</fragment>
---

[question:AB211]
---
#### Lösungsweg
* gegeben: $Q_{\mathrm{max}} = \qty{60}{\ampere\hour}$
* gegeben: $Q_{10\%} = 0,1 \cdot Q_{\mathrm{max}} = \qty{6}{\ampere\hour}$
* gegeben: $I = \qty{0,8}{\ampere}$
* gesucht: $t$

<fragment>
$Q = I \cdot t \Rightarrow t = \frac{Q}{I} = \frac{Q_{\mathrm{max}} - Q_{10\%}}{I} = \frac{\qty{54}{\ampere\hour}}{\qty{0,8}{\ampere}} = \qty{67,5}{\hour}$
</fragment>

---
[question:AB501]
---
#### Lösungsweg
* gegeben: $U = \qty{12}{\volt}$
* gegeben: $Q = \qty{5}{\ampere\hour}$
* gesucht: $W$

<fragment>
$W = P \cdot t = U \cdot I \cdot t = U \cdot Q = \qty{12}{\volt} \cdot \qty{5}{\ampere\hour} = \qty{60,0}{\watt\hour}$
</fragment>