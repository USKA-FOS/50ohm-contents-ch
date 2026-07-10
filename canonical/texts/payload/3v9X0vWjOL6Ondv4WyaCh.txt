<left>
[picture:795:a_einweggleichrichtung_c:Einweggleichrichtung mit Kondensator]
</left>
<right>
* Bei positiver Halbwelle lässt Diode $D$ Strom fließen
* Lädt Kondensator $C_L$ auf Spitzenwert der Wechselspannung und versorgt Lastwiderstand $R_L$
* Bei negativer Halbwelle sperrt Diode $D$
* Kondensator $C_L$ entlädt sich über Lastwiderstand $R_L$
</right>
---
<left>
[picture:75:a_Restwelligkeit:Welligkeit der Ausgangsgleichspannung $U_L$]
Am Lastwiderstand $R_L$ stellt sich eine pulsierende Gleichspannung $U_L$ ein
</left>
<right>
* Je größer die Kapazität, umso geglätteter die Gleichspannung
* Die Trafospannungen sind Effektivspannungen
* Für die Bemessung des Kondensators muss die Spitzenspannung bestimmt werden
* Für die Diode ist die Spitzen-Spitzen-Spannung relevant
</right>

---
[question:AD302]
---
#### Lösungsweg
* gegeben: $U_{\mathrm{eff}} = \qty{15}{\volt}$
* gesucht: $\hat{U}$

<fragment>
$\hat{U} = U_{\mathrm{eff}} \cdot \sqrt{2} = \qty{15}{\volt} \cdot 1,41 = \qty{21,21}{\volt}$
</fragment>
---
[question:AD303]
---
#### Lösungsweg
* gegeben: $U_P = \qty{230}{\volt}$
* gegeben: $ü = 20:1$
* gesucht: $\hat{U} + \qty{50}{\percent}$

<fragment>
$ü = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{ü} = \frac{\qty{230}{\volt}}{20} = \qty{11,5}{\volt}$
</fragment>
<fragment>
$\hat{U} = U_S \cdot \sqrt{2} = \qty{11,5}{\volt} \cdot 1,41 \approx \qty{16,26}{\volt}$
</fragment>
<fragment>
$\hat{U} + \qty{50}{\percent} \approx \qty{25}{\volt}$
</fragment>
---
[question:AD304]
---
#### Lösungsweg
* gegeben: $U_P = \qty{230}{\volt}$
* gegeben: $ü = 5:1$
* gesucht: $U_{SS} + \qty{20}{\percent}$

<fragment>
$ü = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{ü} = \frac{\qty{230}{\volt}}{5} = \qty{46}{\volt}$
</fragment>
<fragment>
$\hat{U} = U_S \cdot \sqrt{2} = \qty{46}{\volt} \cdot 1,41 \approx \qty{65,05}{\volt}$
</fragment>
<fragment>
$U_{SS} + \qty{20}{\percent} = 2 \cdot \hat{U} + \qty{20}{\percent} \approx \qty{156}{\volt}$
</fragment>