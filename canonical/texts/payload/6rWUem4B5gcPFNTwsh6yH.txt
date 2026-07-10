## Vorwärtsfehlerkorrektur (FEC)

* Erkennt der Empfänger einen Fehler (z. B. mittels Prüfbits), kann er um eine erneute Übertragung bitten  
* Bei der Vorwärtsfehlerkorrektur wird zusätzliche Redundanz (z. B. weitere Prüfbits) hinzugefügt  
* So wird nicht nur erkannt, dass ein Fehler vorliegt, sondern auch an welcher Stelle $\rightarrow$ das fehlerhafte Bit kann berichtigt werden
* Im Englischen spricht man von Forward Error Correction (FEC)

---

[question:AE413]

---

[question:AE414]

---

## Hamming-Code – Fehlerkorrektur im Detail

* Der Hamming-Code nutzt mehrere Parity Bits, um nicht nur Fehler zu erkennen, sondern auch zu korrigieren  
* Ziel: Ein einzelner Bitfehler soll lokalisiert und berichtigt werden

---

<left>
[picture:683:hamming1:Übertragung von 11 Bits]
</left>
<right>
* Beispiel: Übertragung eines 11-Bit-Datenworts  
* Ziel: Fehlererkennung und -korrektur bei einem Bitfehler
</right>

---

<left>
[picture:682:hamming2:Alphabetische Benennung der Bitpositionen]
</left>
<right>
* Die Positionen der Bits werden alphabetisch benannt, um die einzelnen Bereiche zu identifizieren
</right>

---

<left>
[picture:684:hamming3:Neuordnung mit zusätzlichen Bits]
</left>
<right>
* Anordnung der Datenbits mit zusätzlichen Bit-Positionen für Parity Bits
</right>

---

<left>
[picture:685:hamming4:Vier Parity Bits im Hamming-Code]
</left>
<right>
* Anstelle eines einzelnen Prüfbit werden vier Parity Bits ($p_1$–$p_4$) eingesetzt  
* Diese decken unterschiedliche Bereiche der Datenbits ab – ähnlich einem Kreuzworträtsel
</right>

---

<left>
[picture:686:hamming5:Zuweisung der Parity-Bereiche]
</left>
<right>
* Jedes Parity Bit sichert einen bestimmten Bereich der Daten ab
</right>

---

<left>
[picture:687:hamming6:Berechnung der Parity Bits (Even Parity)]
</left>
<right>
* Für jeden Bereich wird das Parity Bit mittels Even Parity berechnet  
* Tritt ein Fehler auf, können die fehlerhaften Bereiche identifiziert und korrigiert werden
</right>

---

<left>
[picture:687:hamming6:Berechnung der Parity Bits (Even Parity)]
</left>
<right>
* Durch die Kombination der Parity-Bereiche lässt sich der fehlerhafte Bit-Standort bestimmen  
* Beispiel: Wird ein bestimmtes Bit (z. B. Bit $k$) während der Übertragung verändert, schlagen alle zugehörigen Paritätsprüfungen fehl – der Fehler liegt also bei Bit $k$
</right>

