## Strom- und Spannungsmessung

<left>
* Spannung wird parallel zum Bauteil gemessen
* Strom wird in Reihe mit dem Bauteil gemessen
</left>
<right>
[picture:1003:a_strom_spannung_messung:Messen der Leistung eines Verstärkers (PA)]
</right>

---
[question:AI101]
---
[question:AI102]
---
## Messgenauigkeit

Der angezeigte Messwert unterscheidet sich meist vom tatsächlichen Wert
* Innenwiderstand des Messgeräts
* Auflösungsvermögen $\rightarrow$ *kleinste Auflösung*
* Anzeige verändert sich erst nach Änderung um die kleinste Auflösung
* Hersteller ermittelt die Abweichung
* Abweichung wird im Datenblatt angegeben

---

<left>
[picture:1004:a_reale_spannungsmessung:Ersatzschaltbild reales Spannungsmessgerät]
</left>

<right>
[picture:1007:a_reale_strommessung:Ersatzschaltbild reales Strommessgerät]
</right>

---
[question:AI103]
--- style="font-size: smaller;"
### Lösungsweg

* Prozentrechnung – die absoluten Werte sind nicht relevant
* gegeben: $U_{\mathrm{Abw}}$ mit $\qty{95}{\percent}$ vom Realwert
* gegeben: $I_{\mathrm{Abw}}$ mit $\qty{95}{\percent}$ vom Realwert
* gesucht: Abweichung der Leistung $P = U \cdot I$

<fragment>
$\begin{split} P_{\textrm{Abw}} &= 100\% - (U_{\mathrm{Abw}} \cdot I_{\mathrm{Abw}})\\ &= 100\% - (95\% \cdot 95\%)\\ &= 100\% - 90,25\%\\ &= 9,75\% \end{split}$
</fragment>

---
## Strom durch Multimeter

* Auch bei einer Spannungsmessung fließt ein Strom durch ein Messgerät
* Es findet eine Stromteilung statt
* Durch den hohen Innenwiderstand ist der abfließende Strom verhältnismäßig klein

---
[question:AI104]
---
### Lösungsweg
* gegeben: $U = \qty{0,5}{\volt}$
* gegeben: $R = \qty{10}{\mega\ohm}$
* gesucht: $I$

<fragment>
$$I = \frac{U}{R} = \frac{\qty{0,5}{\volt}}{\qty{10}{\mega\ohm}} = \qty{50}{\nano\ampere}$$
</fragment>

