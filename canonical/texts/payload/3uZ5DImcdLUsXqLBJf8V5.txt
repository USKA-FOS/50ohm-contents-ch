Eine Phasenregelschleife (PLL) dient dazu, einen variablen, potenziell instabilen Oszillator (VCO – Voltage Controlled Oscillator) mithilfe eines stabilen Referenzoszillators zu synchronisieren. Dabei wird der Phasenvergleich zwischen beiden Signalen genutzt, um eine stabile Ausgangsfrequenz zu erzeugen.

Grundaufbau und Elemente einer PLL

Eine PLL besteht im Wesentlichen aus folgenden Komponenten:
1. **Phasenvergleicher:** Vergleicht die Phasen der Signale vom VCO und vom Referenzoszillator.
2. **Tiefpassfilter:** Wandelt die vom Phasenvergleicher erzeugten Impulse in eine Gleichspannung um.
3. **Spannungsgesteuerter Oszillator (VCO):** Erzeugt das Ausgangssignal, dessen Frequenz durch die vom Tiefpassfilter ausgegebene Gleichspannung gesteuert wird.

Zusätzlich kann die PLL durch einen **Frequenzteiler** ergänzt werden, um die Frequenz des VCOs auf Vielfache der Referenzfrequenz zu synchronisieren.

Funktionsprinzip

1. **Phasenvergleich und Korrektur**:  

Der Phasenvergleicher misst die Phasendifferenz zwischen den Signalen des VCO und des Referenzoszillators. Bei einer Phasenabweichung gibt er Impulse aus, die dem Fehler entsprechen. Diese Impulse werden durch den Tiefpassfilter geglättet und in eine proportionale Gleichspannung umgewandelt.

2. **Regelung des VCOs**:  

Die erzeugte Gleichspannung dient als Steuersignal für den VCO, das dessen Frequenz nachreguliert, sodass sich die Phasendifferenz schrittweise auf null reduziert. Ist dieser Zustand erreicht, sagt man, die PLL ist „eingelockt“ (locked).

3. **Eingelockter Zustand**:  

Im stabilen Zustand der PLL sind die Frequenzen und Phasenlagen der beiden Signale identisch. Die Ausgangsfrequenz ist stabil und entspricht im Wesentlichen der Referenzfrequenz oder deren Vielfachen (je nach gewähltem Teilverhältnis des Frequenzteilers).

<margin>
[picture:45:a_oszillator_pll_pll:Darstellung einer Phasenregelschleife (PLL)]  
</margin>

[question:AD701]
[question:AD702]

Genauigkeit und Stabilität

Die Genauigkeit und Stabilität der PLL-Ausgangsfrequenz hängt in erster Linie von der Qualität des Referenzoszillators ab, welcher üblicherweise ein Quarzoszillator ist.

[question:AD705]

Frequenzteilung und Abstimmbarkeit

Um eine PLL auf unterschiedliche Frequenzen einzustellen, kann ein Frequenzteiler innerhalb des Regelkreises eingesetzt werden. Dadurch wird es möglich, die Ausgangsfrequenz als ein ganzzahliges Vielfaches der Referenzfrequenz zu erzeugen. Das kleinste wählbare Frequenzintervall entspricht dabei der Frequenz des Referenzoszillators, da die Teilung nur in ganzzahligen Schritten erfolgen kann.

[question:AD703]

Berechnung des Teilverhältnisses

Um bei gegebener Referenzfrequenz eine bestimmte Ausgangsfrequenz zu erreichen, wird der Teilfaktor so gewählt, dass an den Eingängen des Phasenvergleichers dieselbe Frequenz anliegt. Dadurch lässt sich das benötigte Teilverhältnis für die gewünschte Ausgangsfrequenz berechnen.

[question:AD704]
