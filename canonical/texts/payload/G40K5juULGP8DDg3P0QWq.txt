Die Speisung einer Antenne erfolgt immer mit einer Spannung und einem Strom, die zu einander in einem bestimmten Verhältnis stehen. Dieses Verhältnis wird als Speisewiderstand bezeichnet.

Damit eine Leistung abgegeben werden kann, müssen immer Spannung *und* Strom vorhanden sein, denn die Leistung ergibt sich aus der Multiplikation von Spannung und Strom. Wäre entweder die Spannung oder der Strom Null, dann gäbe es auch keine Leistungsabgabe bzw. -aufnahme.

Dennoch sprechen wir bei bestimmten Antennen von *stromgespeisten* Antennen und bei bestimmten anderen Antennen von *spannungsgespeisten* Antennen. Damit ist gemeint, dass bei bestimmten Antennen ein hoher Strom bei vergleichsweise geringer Spannung am Speisepunkt vorliegt, oder eine hohe Spannung bei vergleichsweise geringem Strom.


---

Bei einem Halbwellendipol hängt der Speisewiderstand davon ab, wo die Einspeisung erfolgt. Dies liegt daran, dass beim Dipol die Ladungsträger hin- und herschwingen und dabei in der Mitte besonders viele Ladungsträger bewegt werden, was wir als Strombauch bezeichnen, und an den Enden besonders hohe Spannungen entstehen, was wir als Spannungsbauch bezeichnen. Dort wo keine Ladungen bewegt werden sprechen wir von einem Stromknoten, und dort wo die Spannung Null ist sprechen wir von einem Spannungsknoten. Die Abbildung [ref:e_strom_spannung_speisung_dipol] zeigt die Strom und Spannungsverteilung auf dem Dipol. 

[question:EG203]

<margin>
[picture:787:e_strom_spannung_speisung_dipol:Halbwellendipol mit Spannungs- und Stromverteilung]
</margin>

---

Speisen wir einen Halbwellendipol also in der Mitte, so müssen viele Ladungen bewegt werden und wir sprechen von einer stromgespeisten Antenne (niedriger Speisewiderstand). Ein endgespeister Halbwellendipol hingegen ist eine spannungsgespeiste Antenne (hoher Speisewiderstand). Für die Speisung am Ende, wie in Abbildung [ref:e_strom_spannung_speisung_dipol_ende] gezeigt, ist ein Anpassglied erforderlich. Das werden wir erst im HB9-Teil genauer besprechen. 

<margin>
[picture:851:e_strom_spannung_speisung_dipol_ende:Halbwellendipol Endgespeist]
</margin>

---

Stromgespeiste Antennen weisen dementsprechend einen niedrigen und spannungsgespeiste Antennen einen hohen Widerstand auf.

Das lässt sich gut mithilfe des Ohmschen Gesetzes veranschaulichen:

$ R = \frac{U}{I} $

Speist man einen Dipol in der Mitte, liegt dort eine vergleichsweise geringe Spannung bei gleichzeitig hohem Strom an. Der Quotient aus Spannung und Strom ist daher klein, der resultierende Widerstand entsprechend niedrig. Erfolgt die Speisung hingegen am Ende des Dipols, liegt dort eine hohe Spannung an, während der Strom gegen null geht. Dadurch wird der Quotient sehr groß, und der resultierende Widerstand nimmt entsprechend hohe Werte an.

Bei niedrigen Widerständen sprechen wir auch von *niederohmigem* Verhalten ($\downarrow\unit{\ohm}$) und bei hohen Widerständen entsprechend von *hochohmigem* Verhalten  ($\uparrow\unit{\ohm}$).

<indepth>
Eine übliche Größenordnung für den *Speisewiderstand* einer stromgespeisten Antenne ist z. B. $\qty{36}{\ohm}$ bis $\qty{100}{\ohm}$ und bei spannungsgespeisten Antennen $\qty{1500}{\ohm}$ bis $\qty{4000}{\ohm}$.
</indepth>

---

<indepth>
Die Stromverteilung auf einem Dipol hängt von der Frequenz ab, mit der die Antenne betrieben wird. Abbildung [ref:e_stromverteilungen] zeigt die Stromverteilung für ganzzahlige Vielfache der Grundfrequenz $f$ bei einem mittengespeisten Dipol. Dabei ist zu erkennen, dass bei geradzahligen Vielfachen der Grundfrequenz am Speisepunkt ein Stromknoten entsteht. In diesem Fall ist der Strom dort sehr klein, die Spannung hingegen hoch, und die Antenne erscheint am Speisepunkt hochohmig. Aus diesem Grund ist ein mittengespeister Dipol nur bei ungeraden ganzzahligen Vielfachen der Grundfrequenz resonant. Eine Nutzung mehrerer Bänder lässt sich erreichen, indem der Speisepunkt verlagert wird, etwa an einen der Strombäuche wie in Abbildung [ref:e_stromverteilungen]b (z. B. bei der Windom-Antenne) oder an das Antennenende (z. B. EFHW- oder Fuchsantenne). In diesen Fällen sind jedoch Anpassgeräte erforderlich, auf die wir erst im HB9-Teil näher eingehen werden.
  
[picture:1050:e_stromverteilungen:Stromverteilungen bei verschiedneen Grundfrequenzen]
</indepth>

[question:EG204]
[question:EG205]
[question:EG206]
