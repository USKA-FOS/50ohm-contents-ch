<left>
[picture:140:a_kollektorschaltung_schaltbild:Verstärker in Kollektorschaltung eines Bipolartransistors]
</left>
<right>
* Verstärkerschaltungen von Bipolartransistoren werden nach dem Anschluss benannt, der vom Eingangs- und Ausgangssignal durchflossen wird
* Oder andersrum: Der Anschluss, an dem weder Eingang noch Ausgang direkt angeschlossen sind
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Verstärker in Kollektorschaltung eines Bipolartransistors]
</left>
<right>
* Eingangssignal: Quelle $\rightarrow$ Basis $\rightarrow$ Kollektor $\rightarrow$ Versorgungspannung $\rightarrow$ Quelle
* Ausgangsignal: Kollektor $\rightarrow$ Last $\rightarrow$ Versorgungsspannung $\rightarrow$ Kollektor
</right>
---
[question:AD401]
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Verstärker in Kollektorschaltung eines Bipolartransistors]
</left>
<right>
* Transistor benötigt definierten Arbeitspunkt (BIAS)
* Wird durch den Spannungsteiler an der Basis festgelegt
</right>
--- 
<left>
[picture:140:a_kollektorschaltung_schaltbild:Verstärker in Kollektorschaltung eines Bipolartransistors]
</left>
<right>
* Der Emitterwiderstand erzeugt eine Spannung, wenn Strom durch den Transistor fließt.
* Der Strom fließt vom Emitter durch den Widerstand zur Masse.
* Je mehr Strom fließt, desto höher wird die Spannung am Emitter.
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Verstärker in Kollektorschaltung eines Bipolartransistors]
</left>
<right>
* Die Emitterspannung bremst den Stromfluss und verhindert starke Schwankungen.
* Temperaturänderungen beeinflussen den Transistor weniger.
* $\rightarrow$ Der Transistor bleibt zuverlässig und arbeitet gleichmäßig.
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Verstärker in Kollektorschaltung eines Bipolartransistors]
</left>
<right>
* Ein- und Auskopplung der Signale an Basis und Emitter über *Koppelkondensatoren*
* Halten Gleichspannungsanteile von der Verstärkerstufe fern
* Arbeitspunkt wird stabilisiert
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Verstärker in Kollektorschaltung eines Bipolartransistors]
</left>
<right>
* Abblockkondensator in der Betriebsspannung führt unerwünschte HF- und NF-Signale auf Masse ab
* Rückkopplungseffekte in der Stufe und auf die Versorungsspannung werden vermieden
* Kollektor wird auf Masse gelegt $\rightarrow$ Ausgang ist auf gleichem Potenzial wie Eingang
</right>
---
<left>
[picture:140:a_kollektorschaltung_schaltbild:Verstärker in Kollektorschaltung eines Bipolartransistors]
</left>
<right>
* Phasenverschiebung ist $\qty{0}{\degree}$
* Eingangsimpedanz relativ hoch
* $\rightarrow$ Spannungsverstärkung ca. $\num{0,9}$ bis $\num{0,98}$ (immer etwas kleiner als $1$)
* Ausgangsimpedanz sehr niedrig gegenüber Eingangsimpedanz
</right>

---
[question:AD405]
---
[question:AD402]
---
[question:AD403]
---
### Pufferstufe

* Häufig Anwendung als Pufferstufe zwischen Oszillator und weiteren Schaltungsteilen
* Belastet den Oszillator hochohmig
* $\rightarrow$ Weniger Strom vom Oszillator
* $\rightarrow$ Entkopplung
* $\rightarrow$ Bessere Frequenzstabilisierung des Oszillators

---
[question:AD404]