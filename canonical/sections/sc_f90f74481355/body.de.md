In jedem Funkgerät sind eine oder mehrere Spannungsstabilisierungen vorhanden, da die Eingangsspannung, vor allem bei mit Akku betriebenen Geräten, schwanken kann und dann empfindliche Baugruppen, wie z. B. Oszillatoren, ihre Frequenz ändern würden.

Spannungsstabilisierungen gibt es in 3 Varianten:
1. *Schaltung mit Z-Diode* 
2. *Lineare Spannungsregler* 
3. *Festspannungsregler* in einer integrierten Schaltung

Die *Schaltung mit Z-Diode* (vgl. Abbildung [ref:a_stab_z_diode]) stellt eine sehr einfache Schaltung zur Stabilisierung der Ausgangsspannung dar, da die Z-Diode die Ausgangsspannung in Grenzen stabil halten kann.

Die Z-Diode wird immer mit einem Vorwiderstand und in Sperrrichtung ($-U_Z$) betrieben. Z-Dioden mit Durchbruchspannungen $U_Z$ ab $\qty{5}{\volt}$, zeigen einen sehr steilen Verlauf der Kennlinie (vgl. Abbildung [ref:a_z_diode_kennlinie]) und eignen sich deshalb sehr gut zur Spannungsstabilisierung. Der Wirkungsgrad der Schaltung ist sehr niedrig, da die Verluste im Vorwiderstand $R_V$ und in der Z-Diode berücksichtigt werden müssen. 

<margin>
[picture:323:a_stab_z_diode:Spannungsstabilisierung mit Z-Diode]
[picture:862:a_z_diode_kennlinie:Kennline einer Z-Diode]
</margin>

Die Lösung der folgenden Aufgabe ist etwas aufwändiger. Zuerst wird aus Lastwiderstand und Laststrom die Ausgangsleistung bestimmt. Anschließend berechnet man aus Versorgungsspannung sowie der Summe aus Laststrom und Z-Diodenstrom die aufgenommene Eingangsleistung. Der Wirkungsgrad ergibt sich dann aus dem Verhältnis von abgegebener zu aufgenommener Leistung.

[question:AD321]

---

*Lineare Spannungsregler* stabilisieren die Ausgangsspannung dadurch, indem ein Leistungstransistor als veränderlicher Widerstand betrieben wird und zusammen mit dem Lastwiderstand einen Spannungsteiler bildet.

<margin>
[picture:1079:a_diskrete_pannungsstabilisierung:diskret aufgebaute Spannungsstabilisierung]
</margin>

In der folgenden Frage ist eine diskrete Spannungsstabilisierung mit Längstransistor dargestellt. Über eine Z-Diode wird eine Referenzspannung von $\qty{5,6}{\volt}$ an der Basis des Transistors erzeugt. Das Emitterpotential ist im Betriebszustand eines Siliziumtransistor um etwa $\qty{0,6}{\volt}$ niedriger als das Basispotential. Die geregelte Ausgangsspannung liegt dann bei etwa $\qty{5}{\volt}$.

Der Laststrom fließt auch durch den Transistor und dadurch wird er bei hohem Laststrom sehr warm. Die sogenannten Längstransistoren befinden sich deshalb bei linear geregelten Spannungsstabilisierungen immer auf einem Kühlkörper. 

<margin>
[photo:246:a_Längstransistor 2N3055 auf Kühlkörper:Der Längstransistor in einem linear geregelten Netzteil muss große Verlustleistungen aushalten und wird deshalb auf einen Kühlkörper montiert.]
</margin>

[question:AD315]

Die Verlustleistung $P_V$ ergibt sich aus der Differenz von  $P_{\mathrm{in}} - P_{\mathrm{out}}$. Zusammen mit der Leistungsformel $P = U \cdot I$ kann die Verlustleistung berechnet werden.

[question:AD319]

Bei linearen Spannungsreglern ist der Wirkungsgrad systembedingt oft sehr niedrig. Hierzu gibt es eine Frage zum Wirkungsgrad, welche mit der bekannten Formel von oben $\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$ gelöst werden kann. 

[question:AD320]

---

Neben Z-Diode und Linearspannungsregler gibt es auch *Festspannungsregler* in einer integrierten Schaltung. Festspannungsregler arbeiten wie lineare Spannungsregler mit Längstransistor und  beinhalten eine sehr genaue Spannungsreferenzquelle zusammen mit einer optimalen elektronischen Regelung. Auch wenn die Eingangsspannung stark  schwankt (z.B. $\qty{\pm 2}{\volt}$) ist auf der Lastseite die Spannungsänderung nur im Millivoltbereich messbar. Die Kondensatoren auf beiden Seiten des Festspannungsreglers müssen nach Vorgaben des Herstellers gewählt werden, sonst kann es zu unerwünschten Schwingungen im Regelverhalten der Schaltung kommen.

<margin>
[picture:200:a_Festspannungsregler:Festspannungsregler]
</margin>

---

Ein Festspannungsregler hält seine Ausgangsspannung weitgehend konstant, solange die Eingangsspannung ausreichend über der Ausgangsspannung liegt. Die Ausgangsspannung bleibt daher nahezu unverändert, auch wenn die Eingangsspannung schwankt.

[question:AD316]
[question:AD317]

<tip>
Damit die interne Regelschaltung optimal funktioniert, muss die Eingangsspannung bei Standard-Festspannungsregler (z.B. Typ 7812 für eine Festpannung von $\qty{12}{\volt}$) um ca. $\qty{3}{\volt}$ größer als die Ausgangsspannung sein, also mindestens $\qty{15}{\volt}$. Es gibt Festspannungsregler, bei denen die Eingangsspannung nur um $\qty{1}{\volt}$ größer als die Ausgangsspannung sein muss. Diese Regler heißen Low-Drop-Spannungsregler.
</tip>

---

Zur Lösung der folgenden Aufgabe nutzen wir erneut die bekannte Beziehung: Die Verlustleistung $P_V$ des Festspannungsreglers ergibt sich aus der Differenz von $P_{\mathrm{in}}$ und $P_{\mathrm{out}}$.

[question:AD318]

<tip>
Der Lösungsweg beginnt mit der Berechnung des Laststromes: $I_L$. Hinweis: Der Strom in der Masseleitung des Festspannungsreglers ist vernachlässigbar klein und wird deshalb nicht berücksichtigt.
</tip>

<margin>
[photo:245:a_Festspannungsregler:Festspannungsregler für $\qty{5}{\volt}$, $\qty{12}{\volt}$ und $\qty{9}{\volt}$ auf Kühlkörper]
</margin>
  