## Konverter

* Signale auf einem Frequenzband werden in ein anderes Frequenzband umgesetzt
* z.B. wird ein $\qty{2}{\meter}$-Signal im Empfang als ein $\qty{70}{\centi\meter}$-Signal ausgesendet
* Signal wird nur in eine Richtung umgewandelt
* Im Grunde ein einfacher Mischer

---
[question:EF504]

<note>
* TCXO und PLL kommen später dran
* Aber die Mischung kann berechnet werden
</note>

---
[question:EF505]
---
## Transverter

* Beim Transverter funktioniert die Umsetzung in beide Richtungen
* Die Umsetzung erfolgt auch hier durch Mischung

---
[question:EF501]
---
[question:EF502]
---
[question:EF503]
<note>
* Lösungsweg auf der kommenden Folie
</note>
---
### Lösungsweg

Frequenz des Generators wird ver-3-facht: $\qty{38,666}{\mega\hertz} \cdot 3 = \qty{116}{\mega\hertz}$

<left>
*TX Weg*
* Die $\qtyrange{28}{30}{\mega\hertz}$ vom TRX werden mit $\qty{116}{\mega\hertz}$ gemischt
* Das Signal kann $\qtyrange{86}{88}{\mega\hertz}$ oder $\qtyrange{144}{146}{\mega\hertz}$ sein
</left>
<right>
[picture:843:e_transverter_tx:Transverter im TX-Pfad]
</right>

---

<left>
*RX Weg*
* Das Antennensignal wird mit $\qty{116}{\mega\hertz}$ gemischt und es kommen $\qtyrange{28}{30}{\mega\hertz}$ raus
* Das Antennensignal liegt somit u.a. bei $\qtyrange{144}{146}{\mega\hertz}$
* $\rightarrow$ Es ist nur die Antwort mit $\qty{2}{\meter}$ und der Transverter richtig
</left>
<right>
[picture:842:e_transverter_rx:Transverter im RX-Pfad]
</right>

---
## Frequenzstabilität

* Konverter und Transverter sollten mit frequenzstabilen Oszillatoren gebaut werden
* Weicht die Frequenz ab, ist die Ausgangsfrequenz auch abweichend

---
<left>
* Grafik aus vorheriger Frage
* Aus $\qty{10}{\mega\hertz}$ werden $\qty{2,256}{\giga\hertz}$, also $\num{225,6}$ Vervielfachung
* Statt $\qty{10}{\mega\hertz}$ erzeugt der Oszillator aufgrund eines Fehlers $\qty{10,01}{\mega\hertz}$
* $\qty{10,01}{\mega\hertz} \cdot 225,6 = \qty{2,258256}{\giga\hertz}$
* Mischer: $\qty{144}{\mega\hertz} + \qty{2,258256}{\giga\hertz} = \qty{2,402256}{\giga\hertz} \rightarrow \qty{2,256}{\mega\hertz}$ daneben
</left>
<right>
[picture:651:e_konverter_13cm:Konverter für das $\qty{13}{\centi\meter}$-Band]
</right>