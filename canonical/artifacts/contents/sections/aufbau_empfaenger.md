Schauen wir uns zunächst an, wie ein Empfänger aufgebaut ist. In Abbildung [ref:aufbau_empfaenger_blockdiagramm] gehen wir zur Vereinfachung nicht auf die Ebene einzelner Bauteile, sondern betrachten Blöcke, die eine bestimmte Funktion haben. Diese Darstellung nennt man Blockdiagramm. Sie dient in der Elektrotechnik dazu, komplexe Geräte in einer vereinfachten Übersicht darzustellen. Hierzu lässt man Details weg, die zum Verständnis des gesamten Gerätes nicht erforderlich sind.

<margin>
[picture:736:aufbau_empfaenger_blockdiagramm:Blockdiagramm eines einfachen Empfängers]
</margin>

<indepth>
Der hier dargestellte Empfänger wird als Geradeausempfänger bezeichnet. Der Name kommt daher, dass das von der Antenne aufgenommene Signal in seiner Frequenz bis zum Demodulator nicht verändert wird.
</indepth>

---

Betrachten wir die einzelnen Blöcke des Empfängers der Reihe nach von links nach rechts im Detail:

1. Antenne: Die Antenne nimmt eine Vielzahl von Funkwellen auf und leitet sie als elektrische Schwingungen weiter.
2. Bandpassfilter: Um das gewünschte Signal herauszufiltern, folgt ein Bandpassfilter. Dieses lässt nur den gewünschten Frequenzbereich durch und sperrt alle anderen ungewünschten Frequenzen.
3. HF-Verstärker: Als nächstes folgt ein Verstärker, der das herausgefilterte Signal verstärkt. Es handelt sich hierbei um einen Hochfrequenz-Verstärker (HF-Verstärker), da das Signal eine hohe Frequenz aufweist, beispielsweise $\qty{144,3}{\mega\hertz}$.
4. Demodulator: Das verstärkte Signal wird vom Demodulator weiter verarbeitet. Demodulation ist das Gegenstück zur Modulation. Während bei der Modulation ein Signal (z. B. ein Sprachsignal) auf einen Hochfrequenzträger moduliert wird, passiert bei der Demodulation das Gegenteil: Aus dem modulierten Hochfrequenzträger wird das ursprüngliche Signal zurückgewonnen. Wir haben dann beispielsweise wieder das Sprachsignal, das am Sender in das Mikrofon gesprochen wurde. Man spricht auch vom Niederfrequenz-Signal, kurz NF-Signal, da es vergleichsweise niedrige Frequenzen aufweist, bei einem Sprachsignal beispielsweise Frequenzen unter $\qty{20}{\kilo\hertz}$.
5. NF-Verstärker: Das demodulierte Signal wird dann verstärkt. Diesmal handelt es sich um einen Niederfrequenz-Verstärker (NF-Verstärker) zum Verstärken des Signals für den Lautsprecher. Das Symbol für den NF-Verstärker ist dasselbe wie für den Hochfrequenzverstärker.
6. Lautsprecher: Das Signal wird jetzt durch den Lautsprecher von einer elektrischen Schwingung in eine Schallwelle umgewandelt und somit wieder hörbar gemacht.

<indepth>
Beim *Bandpassfilter* symbolisieren die beiden durchgestrichenen Wellen, dass Frequenzen ober- und unterhalb des gewünschten Frequenzbereichs gesperrt werden. Die mittlere Welle steht dafür, dass der gewünschte Frequenzbereich durchgelassen wird.
</indepth>

<indepth>
Der *Demodulator* wird durch das Schaltzeichen der Diode dargestellt, die das wichtigste Bestandteil vieler Demodulatoren ist. Die Funktionsweise einer Diode wird später im Kapitel "Bauteile und Schaltkreise" erklärt.
</indepth>

[question:NF201]

Je nachdem wie ein Empfänger genau aufgebaut ist, hat er unterschiedliche Eigenschaften. Eine wichtige Eigenschaft ist die Empfindlichkeit. Damit wird die Fähigkeit des Empfängers bezeichnet, schwache Signale zu empfangen. Je empfindlicher ein Empfänger ist, desto schwächere Signale kann er empfangen.

[question:NF303]
