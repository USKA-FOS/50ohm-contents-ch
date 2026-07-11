<left>
[picture:343:a_Brückenschaltung:Tipico circuito a ponte con 4 resistenze]
  
$\frac{R_1}{R_2} = \frac{R_3}{R_4}$
</left>
<right>
* Circuito composto da 4 resistenze per la misurazione della resistenza
* Due partitori di tensione collegati in parallelo
* Se i rapporti dei partitori di tensione sono uguali, non scorre corrente attraverso il ponte
</right>
<note>
Ponte di misura di Wheatstone
</note>

---
[question:AD111]
---
[question:AD112]
---
[question:AD113]
--- style="font-size: 0.7em;"
#### Percorso di soluzione
* dato: $R_1 = R_4 = \qty{1}{\kilo\ohm}$
* dato: $R_2 = R_3 = \qty{10}{\kilo\ohm}$
* dato: $U = \qty{11}{\volt}$
* cercato: $U_{AB}$

<fragment>
$\frac{U_A}{U} = \frac{R_1}{R_1 + R_2} \Rightarrow U_A = \frac{R_1}{R_1 + R_2} \cdot U = \frac{\qty{1}{\kilo\ohm}}{\qty{1}{\kilo\ohm} + \qty{10}{\kilo\ohm}} \cdot \qty{11}{\volt} = \qty{1}{\volt}$
</fragment>
<fragment>
$\frac{U_B}{U} = \frac{R_3}{R_3 + R_4} \Rightarrow U_B = \frac{R_3}{R_3 + R_4} \cdot U = \frac{\qty{10}{\kilo\ohm}}{\qty{10}{\kilo\ohm} + \qty{1}{\kilo\ohm}} \cdot \qty{11}{\volt} = \qty{10}{\volt}$
</fragment>
<fragment>
$U_{AB} = |U_A - U_B| = |\qty{1}{\volt} - \qty{10}{\volt}| = \qty{9}{\volt}$
</fragment>