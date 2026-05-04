Im Gegensatz zur Modulation, die auf der Senderseite stattfindet, bewirkt die Demodulation von Signalen im Empfänger, dass ein moduliertes Signal wieder in NF umgewandelt wird und somit hörbar wird.

Je nachdem welche Modulationsart auf der Senderseite verwendet wurde muss auf der Empfängerseite eine entsprechende Demodulation stattfinden.
Hierfür gibt es unterschiedliche Schaltungskonzepte, die die Demodulation ermöglichen.

Die einfachste Form der Demodulation eines Hochfrequenz-Signals stellt die Amplituden-Modulation (AM) dar.
AM-Signale können mittels eines sog. Hüllkurven-Demodulator wie in Abbildung [ref:demodulator_huellkurvendemodulator_am] demoduliert werden. Hierzu wird das hochfrequente Signal zunächst nach der gewünschten Empfangsfrequenz selektiert z.B. mittels eines angepassten Schwingkreises und anschließend über eine Diode gleichgerichtet. Ein der Diode nachgeschalteter Kondensator wird auf den momentanen Spitzenwert des Signals aufgeladen und gleichzeitig über einen zu diesem parallell geschalteten Widerstand mit einer geeigneten Zeitkonstante entladen. Diese Zeitkonstante liegt deutlich über der Periodendauer des HF-Signals jedoch deutlich unter der Periodendauer des NF-Signals.

<margin>
[picture:141:demodulator_huellkurvendemodulator_am:Hüllkurvendemodulator zur Demodulation von AM-Signalen]
</margin>

[question:AD501]

Am Anschluss X in Abbildung [ref:demodulator_huellkurvendemodulator_am_2] wird jeweils die gleichgerichtete Spitzenspannung des HF-Signals abgebildet, die zwischen den Spitzen des HF-Signals entsprechend der Zeitkonstante des parallell zum Kondensator geschalteten Widerstandes leicht abfällt. Die Hüllkurve des Signals entspricht damit der aufmodulierten NF, die aufgrund der Zeitkonstante des Kondensators mit einem Sägezahn-Signal (Trägerfrequenz) überlagert ist und entspricht dem Signal in Abbildung [ref:demodulator_huellkurvendemodulator_am_abbx]. In den nachfolgenden NF-Verarbeitungsstufen (nicht abgebildet) werden die Reste dieser Trägerfrequenz dann ausgefiltert, so dass die reine NF als Ausgangssignal verbleibt.

<margin>
[picture:607:demodulator_huellkurvendemodulator_am_2:Hüllkurvendemodulator zur Demodulation von AM-Signalen mit Darstellung des ZF-Eingangssignals welches am Eingang des Demodulators anliegt]
[picture:146:demodulator_huellkurvendemodulator_am_abbx:Demoduliertes Signal am Punkt X des Hüllkurvendemodulators]
</margin>

[question:AD502]

---
<margin>
[picture:841:demodulator_flankendiskriminator:Schwingkreis der als Flankendiskriminator verwendet wird]

[picture:149:demodulator_flankendiskriminator_schaltung:FM-Flankendiskriminator]
</margin>

Eine sehr ähnliche Schaltung wie der vorgenannte Hüllkurven-Demodulator kann zur Demodulation von FM-Signalen verwendet werden.
Ausgehend von der Zwischenfrequenz im FM-Empfänger läuft, wie in Abbildung [ref:demodulator_flankendiskriminator], das Signal in einen Schwingkreis, der mit seiner Resonanzfrequenz $f_\text{res}$ leicht oberhalb oder unterhalb der ZF-Frequenz $f_\text{ZF}$ abgestimmt ist. Hierdurch liegt das zu demodulierende FM-Signal auf der Flanke des Schwingkreises und wandelt Frequenzänderungen der FM in Amplitudenänderungen um. Mittels des nachgeschalteten AM-Demodulators wird das nunmehr in ein AM-Signal umgewandelte FM-Signal dann demoduliert und hörbar gemacht. Diese Schaltung, gezeigt in Abbildung [ref:demodulator_flankendiskriminator_schaltung] wird Flankendiskriminator genannt.

[question:AD504]

FM-modulierte Signale lassen sich ebenfalls mittels einer PLL (Phase Locked Loop) demodulieren. In einer PLL wird ein spannungsgesteuerter Oszillator (VCO) über eine Phasenregelschleife frequenzfolgend an ein Eingangssignal gekoppelt. Wenn sich die Frequenz des Eingangssignals ändert (FM-Modulation) folgt die Regelspannung des VCO der FM-Modulation. Diese Regelspannung entspricht dann genau der Modulation des FM-Signals und somit der aufmodulierten NF und kann an der PLL abgegriffen werden zur weiteren Verarbeitung.

[question:AD505]

Um SSB-Modulierte Signale zu demodulieren verwendet man einen sog. Produktdetektor. Dieser ist im wesentlichen ein Ringmischer, der als Eingangssignale die ZF des Empfängers sowie einen BFO (Beat Frequency Oscillator) verwendet. Durch Mischung (Produkt) dieser beiden Eingangssignale entsteht als eines der Mischprodukte das gewünschte NF-Signal (SSB-Signal), welches am Ausgang zur weiteren Verarbeitung abgegriffen werden kann. Für bestmögliche Verständlichkeit der demodulierten NF muss der BFO auf die Frequenz des unterdrückten Trägers des SSB-Signals abgestimmt werden.

[question:AD506]