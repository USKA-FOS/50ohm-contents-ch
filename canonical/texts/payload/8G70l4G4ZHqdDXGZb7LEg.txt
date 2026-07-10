Ein *Notch-Filter (Kerbfilter)* ist ein sehr schmalbandiges Filter, welches eine bestimmte Frequenz im NF-Spektrum des Empfangssignals unterdrücken soll. Dies dient zum Beispiel dazu einen störenden Träger in einer Übertragung gezielt auszublenden, den Rest der Übertragung jedoch nahezu unbeeinflusst hiervon zu lassen. Notchfilter können sowohl im NF-Bereich als auch im ZF-Bereich realisiert werden. Filter im ZF-Bereich haben hierbei den Vorteil, dass diese insbesondere stärkere Störsignale wirksamer unterdrücken und deren Einfluss auf die AGC reduzieren können.

[question:EF215]

<margin>
[picture:242:frequenzverlauf_notchfilter:Filtercharakteristik eines Notch-Filters]
</margin>

---

Die Filtercharakteristik eines Notch-Filters ist derart gestaltet, dass nur ein kleiner Frequenzteil des NF-Signals sehr stark unterdrückt wird. Hierdurch ergibt sich eine Kerbe im Spektrum. Daher auch der Name Notch-Filter.

[question:EF216]

<tip>
Viele moderne Geräte realisieren Notch-Filter mittels digitaler Filtertechnologie. Hierbei können oft Bandbreite sowie die Filtercharakteristik und Frequenz genau parametrisiert werden. Ein weiterer Vorteil sind in diesem Zusammenhang sog. Auto-Notch-Filter, die feste Trägerkomponenten im NF-Signal automatisch erkennen und automatisch ausblenden können.
</tip>