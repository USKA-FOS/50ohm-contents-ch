In der Frequenz steuerbare Oszillatoren lassen sich auf verschiedene Weisen realisieren. Eine Möglichkeit ist der sog. *spannungsgesteuerte Oszillator VCO - Voltage controlled oscillator*.

[question:AD601]

---

Damit die Frequenz des Oszillators veränderbar wird, kann man in dessen Schwingkreis eine Kapazitätsdiode einfügen, deren Kapazität über eine Gleichspannung beeinflusst werden kann (vgl. Abbildung [ref:a_vco_schaltung]). Eine Änderung dieser Gleichspannung führt dann zu einer entsprechenden Änderung der Oszillatorfrequenz. Hierdurch wird der Oszillator mittels einer Steuerspannung abstimmbar. 

<margin>
[picture:752:a_vco_schaltung:VCO-Schaltung mit Kapazitätsdiode]
</margin>

Kapazitätsdiode wird in in Sperrrichtung betrieben. Je höher die Gegenspannung der Diode wird, desto geringer wird deren Kapazität, welche durch die Größe der Grenzschicht (P-N-Übergang) bestimmt wird. Die Grenzschicht vergrößert sich bei Vergrößerung der angelegten Sperrspannung, wodurch sich die Kapazität verringert und damit die Frequenz des Schwingkreises gemäß Thomsonscher Schwingungsformel steigt.

Umgekehrt verkleinert sich die Grenzschicht der Kapazitätsdiode bei Verringerung der angelegten Sperrspannung, wodurch sich die Kapazität erhöht und damit die Frequenz des Schwingkreises kleiner wird. Die Sperrspannung kann z. B. durch ein Potentiometer oder einen Steuerkreis erzeugt werden.

%TODO: Evtl. Grafik zu Sperrschicht und Verhalten in Kapazitätsdiode.

[question:AD218] 

Für alle Oszillatorschaltungen, unabhängig von ihrer Ausführung, gilt, dass unerwünschte Rückkopplungen zu Frequenzinstabilitäten führen können. Dies gilt für VCOs als auch für VFOs (z.B. mit Drehkondensatoren) sowie andere Oszillatoren.

[question:AD611]