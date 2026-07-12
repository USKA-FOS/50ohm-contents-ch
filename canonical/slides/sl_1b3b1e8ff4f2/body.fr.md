<left>
[picture:343:a_Brückenschaltung:Typische Brückenschaltung mit 4 Widerständen]
  
$\frac{R_1}{R_2} = \frac{R_3}{R_4}$
</left>
<right>
* Circuit composé de 4 résistances pour la mesure de résistance
* Deux diviseurs de tension connectés en parallèle
* Si les rapports des diviseurs de tension sont égaux, aucun courant ne circule à travers le pont
</right>
<note>
Pont de mesure de Wheatstone
</note>

---
[question:AD111]
---
[question:AD112]
---
[question:AD113]
--- style="font-size: 0.7em;"
#### Solution
* donné: $R_1 = R_4 = \qty{1}{\kilo\ohm}$
* donné: $R_2 = R_3 = \qty{10}{\kilo\ohm}$
* donné: $U = \qty{11}{\volt}$
* recherché: $U_{AB}$

<fragment>
$\frac{U_A}{U} = \frac{R_1}{R_1 + R_2} \Rightarrow U_A = \frac{R_1}{R_1 + R_2} \cdot U = \frac{\qty{1}{\kilo\ohm}}{\qty{1}{\kilo\ohm} + \qty{10}{\kilo\ohm}} \cdot \qty{11}{\volt} = \qty{1}{\volt}$
</fragment>
<fragment>
$\frac{U_B}{U} = \frac{R_3}{R_3 + R_4} \Rightarrow U_B = \frac{R_3}{R_3 + R_4} \cdot U = \frac{\qty{10}{\kilo\ohm}}{\qty{10}{\kilo\ohm} + \qty{1}{\kilo\ohm}} \cdot \qty{11}{\volt} = \qty{10}{\volt}$
</fragment>
<fragment>
$U_{AB} = |U_A - U_B| = |\qty{1}{\volt} - \qty{10}{\volt}| = \qty{9}{\volt}$
</fragment>