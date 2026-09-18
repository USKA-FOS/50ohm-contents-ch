## Applicazione

<left>
* Un diodo permette il flusso di corrente solo in una direzione
* Nella direzione opposta agisce come una resistenza molto elevata
* I diodi vengono utilizzati, tra l'altro, per la rettificazione di tensione alternata
</left>
<right>
[picture:689:e_led:Diversi LED in varie forme costruttive e colori]
</right>
<note>
* Una particolare variante l'abbiamo già conosciuta come LED
</note>

---
[question:EC501]
---
[question:EC502]
---

## Tensione di soglia

<left>
* Affinché un diodo conduca in polarizzazione diretta, deve essere superata una determinata tensione – la tensione di soglia o tensione diretta
* A seconda del materiale di base, la tensione di soglia è diversa
</left>
<right>
* Germanio: $\qtyrange{0,2}{0,4}{\volt}$
* Silicio: $\qtyrange{0,6}{0,8}{\volt}$
* LED (rosso): $\qtyrange{1,6}{2,2}{\volt}$
* LED (giallo, verde): $\qtyrange{1,9}{2,5}{\volt}$
* LED (blu, bianco): $\qtyrange{2,7}{3,5}{\volt}$
</right>

---
[question:EC503]
---

## Diodo Schottky

* Consente un'elevata frequenza di commutazione
* È necessaria solo una tensione di soglia molto bassa, da $\qty{0,4}{\volt}$ a meno di $\qty{0,1}{\volt}$

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

## Diodo in conduzione

<left>
* Un diodo conduce sempre quando la tensione sull'anodo è più positiva di quella sul catodo di una quantità pari alla tensione di soglia
* Vale anche per tensioni negative
* Negli esami vengono considerati solo diodi al silicio con tensione di soglia di $\qty{0,7}{\volt}$
</left>
<right>
[picture:113:e_leitende_siliziumdiode:Tensioni su un diodo al silicio in conduzione]
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
* Un LED funge da indicatore luminoso
</left>
<right>
[picture:324:e_led_schaltung:LED con resistenza in serie]
</right>

---
[question:EC514]
---
### Resistenza in serie

<left>
* Poiché il LED stesso ha una resistenza quasi nulla, se collegato direttamente a una sorgente di tensione si comporterebbe come un cortocircuito
* Con una resistenza in serie si limita la corrente di conduzione
</left>
<right>
[picture:324:e_led_schaltung:LED con resistenza in serie]
</right>

---
* Calcolo: $R = \dfrac{U_q - U_{\mathrm{LED}}}{I_D}$
* $U_q$: sorgente di tensione
* $U_{\mathrm{LED}}$: tensione di soglia del LED
* $I_D$: corrente di conduzione

---
[question:EC515]
---
[question:EC516]
---

## Diodo Zener

<left>
* Normalmente la tensione inversa massima di un diodo si aggira intorno a $\qty{1000}{\volt}$
* Nei diodi Zener si verifica una rottura della tensione, a seconda del modello, tra $\qty{3}{\volt}$ e $\qty{100}{\volt}$
* Vengono utilizzati per la stabilizzazione della tensione
</left>
<right>
[picture:560:_e_z_diode:Simbolo di circuito del diodo Zener]
</right>
<note>
* In passato prendevano il nome da Clarence Melvin Zener
* Oggi sono altri gli effetti determinanti, ma il nome diodo Zener è rimasto
</note>

---
### Polarizzazione

<left>
* I diodi Zener vengono utilizzati con una resistenza in serie in polarizzazione inversa
</left>
<right>
[picture:549:e_z_diode_polung:Diodo Zener correttamente inserito in polarizzazione inversa]
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
[picture:753:e_z_diode_spannungsstabilisierung:Diodo Zener per stabilizzazione della tensione]
</left>
<right>
* $U_Z$ è la tensione alla quale il diodo Zener stabilizza
* $U_V = U_1 - U_Z = \qty{13,8}{\volt} - \qty{5}{\volt} = \qty{8,8}{\volt}$
* $R_V = \frac{U_V}{I} = \frac{\qty{8,8}{\volt}}{\qty{30}{\milli\ampere}} \approx \qty{293}{\ohm}$
</right>
---
[question:EC521]
---
[question:EC522]

<note>
* Le correnti sulla resistenza in serie si sommano
* Le regole di Kirchhoff non sono ancora state trattate
</note>