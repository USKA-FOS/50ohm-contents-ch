## Bandbreite
<left>
* Im Gegensatz zu AM wird weniger als die halbe Bandbreite verwendet
* Maximal $\qty{2,7}{\kilo\hertz}$
* Entspricht dem NF-Signal
</left>
<right>
[picture:743:e_bandbreite_am_ssb:Bandbreite von AM, USB und LSB]
</right>

---
[question:EE201]
---
[question:EE202]
---
[question:EJ210]

---

## Modulation

<left>
* Durch Mischung und Filterung
* Mit der Vorauswahl von USB und LSB wird die Trägerfrequenz gewählt
* Durch den Mischer entstehen zwei Frequenzen
* Im Bandfilter wird nur eine Frequenz durchgelassen
</left>
<right>
[picture:500:e_ssb_modulation:Blockschaltbild zur Modulation von SSB mit der Filtermethode]
</right>

---
<left>
* Der Trick ist hier, dass das Bandfilter nur eine Resonanzfrequenz hat
* Durch die Verschiebung der Trägerfrequenz im Oszillator wird dann das gewünschte Seitenband durchgelassen
</left>
<right>
[picture:500:e_ssb_modulation:Blockschaltbild zur Modulation von SSB mit der Filtermethode]
</right>
---
<left>
Beispiel LSB:
* Mikrofon: $\qty{300}{\hertz}$ - $\qty{3}{\kilo\hertz}$
* LSB-Oszillator: $\qty{9001,5}{\kilo\hertz}$
* DSB-Signal:<br/> a) $\qtyrange{8998,5}{9001,2}{\kilo\hertz}$<br/> b) $\qtyrange{9001,8}{9004,5}{\kilo\hertz}$
* Filter: $\qty{9000}{\kilo\hertz}\pm\qty{1,5}{\kilo\hertz}$
* SSB-Signal:<br/> $\qtyrange{8998,5}{9001,2}{\kilo\hertz}$
</left>
<right>
[picture:831:e_ssb_modulation_lsb:Frequenzen mit der Filtermethode bei LSB]
[picture:940:e_ssb_modulation_lsb_spektrum:Spektrum mit der Filtermethode bei LSB]
</right>
<note>
* Schalter im Bild sollte auf LSB stehen
* Nur das Signal von a) wird durchgelassen
* Das SSB-Signal kann wieder gemischt werden für eine Aussendung im Afu-Band
</note>
---
<left>
Beispiel USB:
* Mikrofon: $\qty{300}{\hertz}$ - $\qty{3}{\kilo\hertz}$
* USB-Oszillator: $\qty{8998,5}{\kilo\hertz}$
* DSB-Signal:<br/> a) $\qtyrange{8995,5}{8998,2}{\kilo\hertz}$<br/> b) $\qtyrange{8998,8}{9001,5}{\kilo\hertz}$
* Filter: $\qty{9000}{\kilo\hertz}\pm\qty{1,5}{\kilo\hertz}$
* SSB-Signal:<br/> $\qtyrange{8998,8}{9001,5}{\kilo\hertz}$
</left>
<right>
[picture:832:e_ssb_modulation_usb:Frequenzen mit der Filtermethode bei USB]
[picture:941:e_ssb_modulation_usb_spektrum:Spektrum mit der Filtermethode bei USB]
</right>
<note>
* Nur das Signal von b) wird durchgelassen
* Das SSB-Signal kann wieder gemischt werden für eine Aussendung im Afu-Band
</note>

---
[question:EE203]
---
[question:EE204]

---
### NF-Signal

<left>
* Für Sprache reicht zwischen $\qty{300}{\hertz}$ und $\qty{3000}{\hertz}$
* Entspricht $\qty{2,7}{\kilo\hertz}$
* Es werden auch kleinere Filter, z.B. $\qty{2,4}{\kilo\hertz}$ verwendet
* An vielen TRX lassen sich die Filter einstellen
</left>
<right>
* Wird ein NF-Signal mit größerer Bandbreite verwendet, steigt die HF-Bandbreite
* Sollte vermieden werden, um benachbarte Signale nicht zu stören
* Auf maximale Bandbreite im Bandplan achten
</right>

---
[question:EJ211]
<note>
* Wenn die unteren $\qty{300}{\hertz}$ der NF abgezogen werden, sind es wieder $\qty{2,7}{\kilo\hertz}$
</note>
---
[question:EF310]
---
[question:EE207]

---
## Mikrofonverstärkung
* Mit der NF-Leistung wird die Leistung der HF gesteuert
* Zu leises Mikrofon bewirkt weniger Ausgangleistung am Sender
* Eine zu starke Mikrofonverstärkung kann Störungen bei Stationen auf dicht benachbarten Frequenzen verursachen

---
[question:EE206]
---
[question:EE205]
---
[question:EJ215]












