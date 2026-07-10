<left>
[picture:342:daempfungsglied_pi:Dämpfungsglied in PI-Konfiguration mit Quelle und Lastwiderstand]
</left>
<right>
* Schwächen Signalpegel definiert ab
* Vermeidung von Übersteuerung oder Beschädigung von Messgeräten
* Eingangspegel für Verstärker und Empfänger auf ein definiertes Maß reduzieren
</right>
<note>
Der Name PI-Konfiguration stammt vom Aufbau der Widerstände als &Pi;
</note>

---
<left>
[picture:342:daempfungsglied_pi:Dämpfungsglied in PI-Konfiguration mit Quelle und Lastwiderstand]
</left>
<right>
* Dämpfung über Widerstände und Umwandlung in Wärme
* Bei symmetrischen Dämpfungsgliedern sind Ein- und Ausgangsimpedanzen gleich
* Üblicherweise $\qty{50}{\ohm}$
</right>

---
<left>
[picture:341:daempfungsglied_t:Dämpfungsglied in T-Konfiguration mit Quelle und Lastwiderstand]
</left>
<right>
* Dämpfung wird in $\unit{\dB}$ angegeben
* z.B. $\qty{20}{\dB}$ = Faktor $\num{100}$
* $\qty{100}{\watt}$ Eingangsleistung $\rightarrow\qty{1}{\watt}$ Ausgangsleistung
</right>
<note>
Der Name T-Konfiguration stammt vom Aufbau der Widerstände als T
</note>

---
[question:AD806]
--- style="font-size: smaller;"
#### Lösungsweg
* gegeben: $P_1 = \qty{100}{\watt}$
* gegeben: $a = \qty{20}{\dB}$
* gesucht: $\Delta P = P_2 - P_1$

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
#### Lösungsweg

* $\qty{20}{\dB}$ entsprechen einer Leistungsdämpfung mit dem Faktor $\num{100}$

---
[question:AD804]
---
#### Lösungsweg

* $\qty{6}{\dB}$ entsprechen einer Leistungsdämpfung mit dem Faktor $\num{4}$

---
[question:AD805]
---
#### Lösungsweg

* Die Impedanz für die Gesamtschaltung ändert sich nicht – also $\qty{50}{\ohm}$


---
[question:AD801]
---
[question:AD802]