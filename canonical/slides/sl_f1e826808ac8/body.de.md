## Demodulation von Signalen

* Demodulation wandelt ein moduliertes HF-Signal in ein hörbares NF-Signal um  
* Abhängig von der verwendeten Modulation wird ein passendes Demodulationsverfahren gewählt  
* Ziel: Wiederherstellung der ursprünglichen NF

---
### AM-Demodulation

<left>
[picture:141:demodulator_huellkurvendemodulator_am:Hüllkurvendemodulator zur Demodulation von AM-Signalen]
</left>
<right>
* AM-Signale werden mit einem Hüllkurvendemodulator verarbeitet  
* HF-Signal wird über einen Schwingkreis selektiert und gleichgerichtet  
* Kondensator lädt auf $\rightarrow$ Widerstand entlädt mit definierter Zeitkonstante
</right>

---

[question:AD501]

---

<left>
[picture:607:demodulator_huellkurvendemodulator_am_2:Hüllkurvendemodulator mit ZF-Eingangssignal]

[picture:146:demodulator_huellkurvendemodulator_am_abbx:Demoduliertes Signal am Punkt X]
</left>
<right>
* Anschluss X: Anzeige der gleichgerichteten Spitzenspannung  
* Leichter Abfall der Spannung durch parallele Entladung  
* Hüllkurve entspricht der aufmodulierten NF, überlagert mit einem Sägezahnsignal  
* Nachfilterung entfernt den Trägeranteil
</right>

---

[question:AD502]

--- style="font-size: smaller;"
### FM-Demodulation

<left>
[picture:841:demodulator_flankendiskriminator:Schwingkreis als Flankendiskriminator]

[picture:149:demodulator_flankendiskriminator_schaltung:FM-Flankendiskriminator]
</left>
<right>
* FM-Demodulation mittels Flankendiskriminator  
* Signal aus der Zwischenfrequenz läuft in einen Schwingkreis  
* Schwingkreis: Resonanzfrequenz $f_\text{res}$ leicht versetzt zu $f_\text{ZF}$
* Frequenzänderungen werden in Amplitudenänderungen umgewandelt  
* Nachgeschalteter AM-Demodulator liefert die NF
</right>

---

[question:AD504]

---

####  FM-Demodulation mittels PLL  

<left>
[picture:77:a_fm_demodulation_pll:Blockschaltbild einer FM-Demodulation mittels PLL]
</left>
<right>
* PLL nutzt einen spannungsgesteuerten Oszillator (VCO), der dem Eingangssignal folgt  
* Regelspannung entspricht der FM-Modulation (aufmodulierte NF)
* Signalabgriff zur weiteren NF-Verarbeitung
</right>

---

[question:AD505]

---
### SSB-Demodulation

* SSB-Demodulation mittels Produktdetektor  
* Ringmischer mischt die Zwischenfrequenz (ZF) mit einem Beat Frequency Oscillator (BFO)  
* Entstehendes Mischprodukt ist das gewünschte SSB-NF-Signal  
* BFO muss exakt auf den unterdrückten Träger abgestimmt sein

---

[question:AD506]

