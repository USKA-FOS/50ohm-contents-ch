## Fehlererkennung: Parity Bit

* Zusätzliches Prüfbit (Parity Bit) wird an Daten angehängt  
* Zwei Varianten:  
* *Even Parity*: Anzahl der Einsen wird auf gerade Anzahl festgelegt  
* *Odd Parity*: Anzahl der Einsen wird auf ungerade Anzahl festgelegt  
* Sender und Empfänger müssen sich über das verwendete Verfahren einigen

---

## Even Parity: Beispiel 1

<left>
[picture:677:byte:Ein Byte]
</left>
<right>
* Zu übertragendes Byte  
* Es werden 5 Einsen gezählt → ungerade Anzahl  
* Prüfbit muss auf $\num{1}$ gesetzt werden, um eine gerade Anzahl zu erreichen
</right>

---

<left>
[picture:678:even_parity:Das Byte mit Even Parity Bit]
</left>
<right>
* Das Prüfbit wurde auf $\num{1}$ gesetzt  
* Das resultierende Byte hat eine gerade Anzahl an Einsen
* Bei einer Fehlerübertragung stimmt das Prüfbit nicht mehr
</right>

---

## Even Parity: Beispiel 2

<left>
[picture:679:even_parity:Byte mit Even Parity]
</left>
<right>
* Ursprüngliches Byte: 4 Einsen (gerade)  
* Prüfbit wird auf $\num{0}$ gesetzt
</right>

---
## Fehlererkennung bei Bitfehlern

* Bei einem Ein-Bit-Fehler wird die Parität umgekehrt → Fehler erkannt  
* Bei zwei Fehlern bleibt die Parität gleich → Fehler unentdeckt  
* Bei drei Fehlern ändert sich die Parität wieder → Fehler erkannt

---

[question:AE411]

---

[question:AE412]

---

## Erweiterte Fehlererkennung

* Zusätzliche Prüfbits können Mehrbitfehler erkennen  
* Bei variablen Nachrichten werden oft Prüfsummenverfahren wie die *zyklische Redundanzprüfung (CRC)* eingesetzt  
* CRC erkennt Fehler bis auf eine gewisse Restwahrscheinlichkeit

<note>
Wird bei der IBAN oder bei Ausweisnummern eingesetzt
</note>

---

[question:AE410]
