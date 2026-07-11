## Messungen für Funkamateure

* Wichtige Messungen: Ausgangsleistung und HF-Spannungen
* Messung der Senderausgangsleistung erfordert definierten Abschluss
* Übliche Impedanz im Amateurfunk: $\qty{50}{\ohm}$
* Direktes Messen in der Schaltung nur bei kleinen Leistungen sinnvoll

---
## HF-Spannungsmessung

* HF-Spannung wird mit einem HF-Tastkopf gemessen
* Diodengleichrichtung und Glättung mit nachgeschaltetem Kondensator

---
### HF-Tastkopf mit einfacher Gleichrichtung



<left>
[picture:576:a_messung_hf_tastkopf_leistungsmessung:Messkopf zur HF-Leistungsmessung über einen Spannungsteiler]
</left>
<right>
* Eine Diode am Ausgang liefert die Spitzenspannung der HF-Spannung
* Abzüglich Forward-Spannung der Diode und evtl. Spannungsteiler
</right>

---
[question:AI608]

---
### HF-Tastkopf mit doppelter Gleichrichtung

<left>
[picture:770:a_messung_hf_tastkopf_doppeldiode:HF-Tastkopf mit zwei Dioden für beide Halbwellen]
</left>
<right>
* Zwei Dioden zur Erhöhung der Messgenauigkeit, insbesondere bei kleinen Leistungen
* Beide Halbwellen werden gleichgerichtet
* Ergebnis: Doppelte Spitzenspannung abzüglich zweimal der Forward-Spannung der Dioden
</right>

---
[question:AI605]

---
[question:AI604]

---
### Messen hoher HF-Leistungen

* Erfordert belastbares Dämpfungsglied
* Nimmt einen Großteil der Leistung auf
* Dämpfungsglied muss in die Berechnung einbezogen werden

---
[question:AI609]

<note>
Keine Berechnung notwendig, da es nur eine Antwort mit Dämpfungsglied gibt
</note>

---
## Kalibrierung von Messschaltungen

* Notwendig für exakte Leistungsmessungen
* Korrekturwerte müssen erstellt werden

---
[question:AI612]

---
### Berechnung eines HF-Tastkopfes

<left>
[picture:576:a_messung_messschaltung_beispiel_1:Beispiel einer HF-Messschaltung]
</left>
<right>
* Eingangssignal wird impedanzrichtig abgeschlossen
* Spannung wird durch Spannungsteiler halbiert
* Nach Gleichrichtung durch Diode verbleibt die Spitzenspannung abzüglich Forward-Spannung
</right>

---
[question:AI610]

--- style="font-size: smaller;"
#### Lösungsweg

* gegeben: $P_E = \qty{1}{\watt}$
* gegeben: $U_F = \qty{0,23}{\volt}$
* gegeben: $R_V = \qty{110}{\ohm}$, $R_T = \qty{330}{\ohm}$
* gesucht: $U_A$


<fragment>
$\begin{split}R &= \left(\frac{1}{R_T + R_T} + \frac{1}{R_V} + \frac{1}{R_V}\right)^{-1}\\ &= \left(\frac{1}{\qty{330}{\ohm} + \qty{330}{\ohm}} + \frac{1}{\qty{110}{\ohm}} + \frac{1}{\qty{110}{\ohm}}\right)^{-1}\\ &= \qty{50,77}{\ohm}\end{split}$
</fragment>

--- style="font-size: smaller;"
* gegeben: $P_E = \qty{1}{\watt}$
* gegeben: $U_F = \qty{0,23}{\volt}$
* berechnet: $R = \qty{50,77}{\ohm}$
* gesucht: $U_A$

<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ \Rightarrow U_{E,eff} &= \sqrt{P_E \cdot R}\\ &= \sqrt{\qty{1}{\watt} \cdot \qty{50,77}{\ohm}}\\ &= \qty{7,125}{\volt}\end{split}$
</fragment>

--- style="font-size: smaller;"
* gegeben: $U_F = \qty{0,23}{\volt}$
* berechnet: $U_{E,eff} = \qty{7,125}{\volt}$
* gesucht: $U_A$

<left>
<fragment>
$\begin{split}U_S &= U_{E,eff} \cdot \sqrt{2}\\ &= \qty{7,071}{\volt} \cdot 1,414\\ &= \qty{10,07}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_A &= \frac{U_S}{2}\,-\,U_F\\ &= \frac{\qty{10,07}{\volt}}{2}\,-\,\qty{0,23}{\volt}\\ &= \qty{5,035}{\volt}\,-\,\qty{0,23}{\volt}\\ &= \qty{4,805}{\volt} \approx \qty{4,8}{\volt}\end{split}$
</fragment>
</right>

---
### Berechnung der Eingangsleistung aus gemessener Gleichspannung

<left>
[picture:577:a_messung_messschaltung_beispiel_2:Beispiel einer HF-Messschaltung]
</left>
<right>
* Spannung am Spannungsteiler entspricht der Ausgangsspannung zzgl. der Diodenspannung
* Effektivwerte berechnen
* Ermittlung der Eingangsleistung über den Schaltungswiderstand
</right>

---
[question:AI611]

--- style="font-size: smaller;"
#### Lösungsweg
* gegeben: $U_A = \qty{14,9}{\volt}\text{ DC}$
* gegeben: $U_F = \qty{0,7}{\volt}$
* gegeben: $R_1 = \qty{54,1}{\ohm}$, $R_T = \qty{330}{\ohm}$
* gesucht: $P_E$

<left>
<fragment>
$\begin{split}R &= \left(\frac{1}{R_T + R_T} + \frac{1}{R_1}\right)^{-1}\\ &= \left(\frac{1}{\qty{330}{\ohm} + \qty{330}{\ohm}} + \frac{1}{\qty{54,1}{\ohm}}\right)^{-1}\\ &= \qty{50}{\ohm}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_S &= \left(U_A + U_F\right) \cdot 2\\ &= \left(\qty{14,9}{\volt} + \qty{0,7}{\volt}\right) \cdot 2\\ &= \qty{31,2}{\volt}\end{split}$
</fragment>
</right>

--- style="font-size: smaller;"
<left>
* berechnet: $R = \qty{50}{\ohm}$
* berechnet: $U_S = \qty{31,2}{\volt}$
* gesucht: $P_E$

<fragment>
$\begin{split}U_{E,eff}\\ &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{31,2}{\volt}}{1,414}\\ &= \qty{22,06}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ &= \frac{(\qty{22,06}{\volt})^2}{\qty{50}{\ohm}}\\ &\approx \qty{9,7}{\watt}\end{split}$
</fragment>
</right>

---
### HF-Tastkopf mit doppelter Spitzenwertgleichrichtung

<left>
[picture:771:a_messung_hf_tastkopf_doppeldiode_2:HF-Tastkopf mit doppelter Spitzenwertgleichrichtung]
</left>
<right>
* Berechnung wie bei einfacher Gleichrichtung
* Zusätzliche Berücksichtigung der doppelten Spitzenspannung
* Doppelte Forward-Spannung der Dioden beachten
</right>

---
[question:AI607]

--- style="font-size: smaller;"
#### Lösungsweg

* gegeben: $U_A = \qty{15,3}{\volt}\text{ DC}$
* gegeben: $U_F = \qty{0,23}{\volt}$
* gegeben: $R_{V1} = \qty{56}{\ohm}$, $R_{V2} = \qty{470}{\ohm}$
* gesucht: $P_E$

<left>
<fragment>
$\begin{split}R &= \left(\frac{1}{R_{V1}} + \frac{1}{R_{V2}}\right)^{-1}\\ &= \left(\frac{1}{\qty{56}{\ohm}} + \frac{1}{\qty{470}{\ohm}}\right)^{-1}\\ &= \qty{50,04}{\ohm}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_S &= \frac{U_A}{2} + U_F\\ &= \frac{\qty{15,3}{\volt}}{2} + \qty{0,23}{\volt}\\ &= \qty{7,88}{\volt}\end{split}$
</fragment>
</right>

--- style="font-size: smaller;"
<left>
* berechnet: $R = \qty{50,04}{\ohm}$
* berechnet: $U_S = \qty{7,88}{\volt}$
* gesucht: $P_E$

<fragment>
$\begin{split}U_{E,eff} &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{7,88}{\volt}}{1,414}\\ &= \qty{5,57}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}P_E &= \frac{U_{E,eff}^2}{R}\\ &= \frac{{\qty{5,57}{\volt}}^2}{\qty{50,04}{\ohm}}\\ &\approx \qty{600}{\milli\watt}\end{split}$
</fragment>
</right>

---
[question:AI606]

--- style="font-size: smaller;"
#### Lösungsweg

* gegeben: $U_A = \qty{15,3}{\volt}\text{ DC}$
* gegeben: $U_F = \qty{0,23}{\volt}$
* gegeben: $R = \qty{50}{\ohm}$ aus dem Messsystem
* gesucht: $P_E$

<left>
<fragment>
$\begin{split}U_S &= \frac{U_A}{2} + U_F\\ &= \frac{\qty{15,3}{\volt}}{2} + \qty{0,23}{\volt}\\ &= \qty{7,88}{\volt}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split}U_{E,eff} &= \frac{U_S}{\sqrt{2}}\\ &= \frac{\qty{7,88}{\volt}}{1,414}\\ &= \qty{5,57}{\volt}\end{split}$
</fragment>
</right>
  
--- style="font-size: smaller;"
* berechnet: $U_{E,eff} = \qty{5,57}{\volt}$
* gegeben: $R = \qty{50}{\ohm}$ aus dem Messsystem
* gesucht: $P_E$

<fragment>
$\begin{split}P_E &= \frac{(U_{E,eff} \cdot 10)^2}{R}\\ &= \frac{(\qty{5,57}{\volt} \cdot 10)^2}{\qty{50}{\ohm}}\\ &\approx \qty{60}{\watt}\end{split}$
</fragment>

--- style="font-size: smaller;"
## Feldstärkeanzeiger zur Leistungsmessung

<left>
[picture:496:a_messung_feldstaerkeanzeiger:Feldstärkeanzeiger]
</left>
<right>
* Messung der HF-Leistung über eine Antenne
* Empfangene HF wird gleichgerichtet und gepuffert
* Anzeige über empfindliches Strommessgerät
* Je höher der Zeigerausschlag, desto höher die HF-Feldstärke
* Exakte Messungen erfordern Kalibrierung
</right>

---
[question:AI613]
