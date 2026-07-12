## Applicazione

<left>
* Un diodo lascia passare la corrente solo in una direzione
* Nell'altra direzione agisce come un'alta resistenza
* I diodi vengono utilizzati, tra l'altro, per la rettifica della tensione alternata
</left>
<right>
[picture:689:e_led:Diversi LED in varie forme e colori]
</right>
<note>
* Abbiamo già conosciuto una forma speciale come LED
</note>

---
[question:EC501]
---
[question:EC502]
---

## Tensione di soglia

<left>
* Affinché un diodo conduca nella direzione di passaggio, è necessario superare una certa tensione, la tensione di soglia o tensione di passaggio
* A seconda della base dell'elemento chimico, la tensione di soglia è più o meno alta
</left>
<right>
* Germanio: $\qtyrange{0,2}{0,4}{\volt}$
* Silicio: $\qtyrange{0,6}{0,8}{\volt}$
* LED (Rosso): $\qtyrange{1,6}{2,2}{\volt}$
* LED (Giallo, Verde): $\qtyrange{1,9}{2,5}{\volt}$
* LED (Blu, Bianco): $\qtyrange{2,7}{3,5}{\volt}$
</right>

---
[question:EC503]
---

## Diodo Schottky

* Consente un'elevata frequenza di commutazione
* È necessaria solo una tensione di soglia molto bassa da $\qty{0,4}{\volt}$ a meno di $\qty{0,1}{\volt}$

---
[question:EC504]
---

## Curve caratteristiche

---
[question:EC506]
---
[question:EC507]
---
[question:EC508]
---
[question:EC505]
---

## Diodo conduttore

<left>
* Un diodo conduce ogni volta che la tensione sull'anodo è superiore di una tensione di soglia rispetto al catodo
* Vale anche per le tensioni negative
* Nell'esame compaiono solo diodi al silicio con una tensione di soglia di $\qty{0,7}{\volt}$
</left>
<right>
[picture:113:e_leitende_siliziumdiode:Tensioni su un diodo al silicio conduttore]
</right>

---
[question:EC513]
---
[question:EC510]
---
[question:EC509]
---
[question:EC511]
---
[question:EC512]
---

## Applicazione LED 

<left>
* Un LED serve come indicatore luminoso
</left>
<right>
[picture:324:e_led_schaltung:LED con resistenza in serie]
</right>

---
[question:EC514]
---
### Resistenza in serie

<left>
* Poiché il LED stesso ha poca resistenza, agirebbe come un cortocircuito se collegato direttamente a una fonte di tensione
* Con una resistenza in serie, la corrente di passaggio viene limitata
</left>
<right>
[picture:324:e_led_schaltung:LED con resistenza in serie]
</right>

---
* Calcolo: $R = \dfrac{U_q - U_{\mathrm{LED}}}{I_D}$
* $U_q$: fonte di tensione
* $U_{\mathrm{LED}}$: tensione di soglia LED
* $I_D$: corrente di passaggio

---
[question:EC515]
---
[question:EC516]
---

## Diodo Z

<left>
* Normalmente, la massima tensione inversa di un diodo è di circa $\qty{1000}{\volt}$
* Nei diodi Z, si verifica una rottura di tensione a seconda del tipo tra $\qty{3}{\volt}$ e $\qty{100}{\volt}$
* Servono per la stabilizzazione della tensione
</left>
<right>
[picture:560:_e_z_diode:Simbolo di circuito diodo Z]
</right>
<note>
* In passato chiamato Clarence Melvin Zener
* Oggi altri effetti sono determinanti, ma Z-Diode è rimasto come nome
</note>

---
### Polarità

<left>
* I diodi Z vengono utilizzati con una resistenza in serie in direzione inversa
</left>
<right>
[picture:549:e_z_diode_polung:Diodo Z correttamente inserito in direzione inversa]
</right>

---
[question:EC517]
---
[question:EC518]
---
[question:EC519]
---
[question:EC520]
---

### Resistenza in serie

<left>
[picture:753:e_z_diode_spannungsstabilisierung:Diodo Z per la stabilizzazione della tensione]
</left>
<right>
* $U_Z$ è la tensione alla quale il diodo Z si stabilizza
* $U_V = U_1 - U_Z = \qty{13,8}{\volt} - \qty{5}{\volt} = \qty{8,8}{\volt}$
* $R_V = \frac{U_V}{I} = \frac{\qty{8,8}{\volt}}{\qty{30}{\milli\ampere}} \approx \qty{293}{\ohm}$
</right>
---
[question:EC521]
---
[question:EC522]

<note>
* Le correnti sul resistore in serie si sommano
* Le regole di Kirchhoff non sono ancora state trattate
</note>