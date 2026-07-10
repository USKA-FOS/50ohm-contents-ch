* Stabilisierung eines variablen, potenziell instabilen Oszillators (z.B. VCO) mittels eines stabilen Referenzoszillators
* Phasenvergleich zwischen den beiden Signalen
* Ausgangsfrequenz entspricht der Referenzfrequenz oder einem Vielfachen und bleibt stabil

--- style="font-size: smaller;"
[picture:45:a_oszillator_pll_pll:Darstellung einer Phasenregelschleife (PLL)]

* *Phasenvergleicher* vergleicht Phasen von VCO und Referenzoszillator
* *Tiefpassfilter* wandelt Impulse des Phasenvergleichers in Gleichspannung um
* *VCO* erzeugt die Ausgangsfrequenz abhängig von der Gleichspannung aus dem Tiefpassfilter
* *Frequenzteiler* (optional) synchronisiert VCO-Frequenz auf ein Vielfaches der Referenzfrequenz

<note>
Phasenvergleicher gibt bei Phasenabweichungen Impulse aus, die vom Tiefpassfilter in eine Gleichspannung geglättet werden. Durch die Frequenzänderung am VCO wird die Phasendifferenz schrittweise reduziert.
</note>

---
[question:AD701]
---
[question:AD702]
---
### Genauigkeit und Stabilität

* Ist abhängig von der Qualität des Referenzoszillators
* Oft ein Quarzoszillator

---
[question:AD705]
---
### Frequenzteilung und Abstimmbarkeit

* Frequenzteiler erlaubt die Einstellung der PLL auf verschiedene Frequenzen
* Ausgangsfrequenz ist ganzzahliges Vielfaches der Referenzfrequenz
* Kleinste wählbare Frequenz entspricht dem Referenzoszillator

---
[question:AD703]
---
[question:AD704]
--- style="font-size: 0.7em;"
#### Lösungsweg
* gegeben: $f_\text{Osc} = \qty{12,5}{\kilo\hertz}$
* gegeben: $f_\text{Out,low} = \qty{12,000}{\mega\hertz}$
* gegeben: $f_\text{Out,high} = \qty{14,000}{\mega\hertz}$
* gesucht: $n$

<fragment>
Bei $f_{Out,low} = \qty{12,000}{\mega\hertz}$:
$n = \frac{f_\text{Out,low}}{f_\text{Osc}} = \frac{\qty{12,000}{\mega\hertz}}{\qty{12,5}{\kilo\hertz}} = 960$
</fragment>
<fragment>
Bei $f_\text{Out,high} = \qty{14,000}{\mega\hertz}$:
$n = \frac{f_\text{Out,high}}{f_\text{Osc}} = \frac{\qty{14,000}{\mega\hertz}}{\qty{12,5}{\kilo\hertz}} = 1120$
</fragment>