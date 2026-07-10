In der Praxis erreichbare Datenübertragungsraten unterscheiden sich je nach Übertragungsverfahren und Funkbedingungen deutlich. WLAN und 5G unterstützen bei optimalen Bedingungen Datenübertragungsraten bis in den Bereich von Gigabits pro Sekunde. FT8 hingegen kann selbst unter widrigen Bedingungen eingesetzt werden, überträgt aber nur wenige Bits pro Sekunde.

Welche Datenübertragungsrate erreichbar ist, hängt von der nutzbaren Bandbreite und dem Signal-Rausch-Verhältnis ($P_\text{S}/P_\text{N}$) ab. Aus diesen beiden Größen kann mit dem Shannon-Hartley-Gesetz die theoretisch maximal erreichbare Datenübertragungsrate für einen Übertragungskanal berechnet werden:

$C=B \cdot \log_2 \left(1+{\dfrac{P_\text{S}}{P_\text{N}}}\right) \unit{\bit\per\second}$

[question:AE416]

---

Ein leicht zu merkender Wert stellt sich bei einem Signal-Rausch-Verhältnis von $\qty{0}{\dB}$ ein. Hier entspricht die Bandbreite in $\unit{\hertz}$ genau der maximal erreichbaren Datenrate in $\unit{\bit\per\second}$. Schlechtere Signal-Rausch-Verhältnisse ermöglichen entsprechend geringere Datenraten, bessere Signal-Rausch-Verhältnisse größere Datenraten. Mit dieser Merkhilfe lassen sich die entsprechenden Prüfungsfragen auch ohne lange Rechnung schnell beantworten.

<margin>
Setzen wir für $\frac{P_\text{S}}{P_\text{N}} = \qty{0}{\dB}$, also den Faktor $\num{1}$ ein so ergibt sich:
  
$\begin{split} C&=B \cdot \log_2 \left(1+1\right) \unit{\bit\per\second}\\ C&=B \cdot \log_2 \left(2\right) \unit{\bit\per\second}\\C &= \qty{B}{\bit\per\second}\end{split}$
</margin>

---

Wenn deutlich mehr Bits pro Sekunde übertragen werden sollen, als Bandbreite in $\unit{\hertz}$ zur Verfügung steht, steigt das benötigte Signal-Rausch-Verhältnis stark an. Über schmalbandige Verbindungen auf der Kurzwelle lassen sich also praktisch keine hohen Datenraten erzielen. So wird das Hamnet als schnelles Datennetz in der Regel im oberen UHF- und unteren SHF-Bereich betrieben, wo höhere Bandbreiten zur Verfügung stehen.

<indepth>
Hierbei wird nur die Rauschenergie betrachtet, die innerhalb der genutzten Bandbreite liegt. Einige Computerprogramme hingegen verwenden die Rauschenergie eines $\qty{2,4}{\kilo\hertz}$ breiten Kanals, auch wenn das eigentliche Nutzsignal deutlich schmaler ist; dies ist jedoch eine andere Größe, die sich nicht direkt in die Formel für das Shannon-Hartley-Gesetz einsetzen lässt.
</indepth>

Durch Absenken der Datenrate hingegen lassen sich Verfahren entwickeln, die nicht nur eine kleine Bandbreite benötigen, sondern auch noch bei einem extrem schlechten Signal-Rausch-Verhältnis funktionieren.  Beispiele hierfür sind digitale Übertragungsverfahren wie WSPR oder FT8, die nur wenige Zeichen pro Zeit austauschen. Damit ist auch bei schlechten Funkbedingungen zumindest die Übermittlung einer kurzen Nachricht möglich.

[question:AE417]
[question:AE418]
[question:AE420]
[question:AE419]

Zu beachten ist, dass das Shannon-Hartley-Gesetz nur eine Obergrenze für die erreichbare Datenübertragungsrate bestimmt. Die tatsächlich erreichbaren Datenraten liegen immer darunter. Nur mittels guter Fehlerkorrekturverfahren, die wir später kennenlernen werden, kann man sich dieser Obergrenze annähern. 
