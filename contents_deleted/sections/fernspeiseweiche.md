An den Antennen montierte, abgesetzte Vorverstärker oder Empfangskonverter benötigen eine Gleichspannungsversorgung. Um eine zusätzliche Gleichspannungsversorgungsleitung einzusparen, kann die Versorgungsspannung auch über das Koaxialkabel, parallel zum HF-Signal, übertragen werden, ohne dass sich die beiden Signale gegenseitig stören. Zur Einspeisung der Gleichspannung in das Koaxialkabel wird deshalb eine Fernspeiseweiche oder englisch BIAS-T eingesetzt. Die Abbildung [ref:a_qo100_bias_t] zeigt eine QO-100 Station mit Fernspeiseweiche zur Spannungsversorgung des Vorverstärkers (LNB).

<margin>
[picture:1080:a_qo100_bias_t:QO-100 Station mit Fernspeiseweiche zur Spannungsverorgung des LNBs]
</margin>

[question:AD322]

Technisch kann dieser Aufbau, wie in Abbildung [ref:a_bias_t] dargestellt, mit einer sehr einfachen Schaltung realisiert werden. Die Fernspeiseweiche (BIAS-T) besteht neben den Anschlüssen lediglich aus zwei Kondensatoren und einer Induktivität. Diese Schaltung haben wir bereits beim MMIC kennengelernt, dessen Versorgungsspannung über den Ausgang mit einem BIAS-T eingespeist wird.

<margin>
[picture:399:a_bias_t:Fernspeiseweiche (BIAS-T)]
</margin>

[question:AD323]

Ein BIAS-T erkennt man daran, dass auf der einen Seite das HF-Signal zum Empfänger (RX) geführt wird, während auf der anderen Seite ein Vorverstärker oder Empfangskonverter (LNA) angeschlossen ist. Zusätzlich wird über den DC-Anschluss eine Versorgungsgleichspannung eingespeist. Diese Gleichspannung gelangt über die Induktivität auf den Innenleiter des Koaxialkabels und versorgt so den angeschlossenen LNA. Die Induktivität wirkt dabei für Hochfrequenz hochohmig, sodass das HF-Signal nicht in die Spannungsversorgung abfließt.

Der Koppelkondensator $C_1$ verhindert, dass die eingespeiste Gleichspannung zum Empfängereingang gelangt. Ohne den Kondensator $C_1$ könnte die Versorgungsspannung daher gegen Masse kurzgeschlossen werden.

[question:AD324]

---

Die Induktivität dient dazu, die Versorgungsgleichspannung in die Leitung einzuspeisen, während sie für Hochfrequenz einen hohen Widerstand darstellt. Dadurch kann die Gleichspannung zum LNA gelangen, ohne dass das HF-Signal in die Spannungsversorgung abfließt. Der Kondensator $C_2$ leitet verbleibende Hochfrequenzanteile gegen Masse ab. Dadurch wird verhindert, dass HF-Signale in die Spannungsversorgung einkoppeln.

<indepth>
[photo:288:a_Bias T Platine:BIAS - T Platine - mit KiCAD erstellt]
So könnte die praktische Umsetzung des abgebildeten Schaltbildes in eine Platine aussehen. $C_2$ und $C_3$ sind Abblockkondensatoren für unterschiedliche Frequenzbereiche, damit die Funktion über einen großen Frequenzbereich gewährleistet ist. $L_1$ dient zur Zuführung der Gleichspannung und muss für den Laststrom gezielt dimensioniert werden. Der Abblockkondensator $C_2$ auf der Gleichspannungseite soll HF-Spannung unterdrücken. Er muss so gewählt werden, dass er bei der HF-Nutzfrequenz einen Blindwiderstand kleiner 1 Ohm darstellt.
</indepth>

Die Spule zwischen DC-Seite (Gleichspannungsseite z.B. $\qty{12}{\volt}$) und der HF-Seite (z.B. $\qty{10}{\giga\hertz}$ Empfangssignal) soll  Hochfrequenzanteile nicht zur DC-Seite durchlassen. Es handelt sich deshalb um eine Drosselspule, die bei der Nutzfrequenz hochohmig wirken muss (z.B. $X_L = \qty{10}{\kilo\ohm}$). Durch diese Drosselspule fließt der Versorgungstrom für den Vorverstärker oder Konverter (LNA). Der Drahtdurchmesser der Drosselspule muss so groß sein, dass der Versorgungsgleichstrom keine Erwärmung der Drosselspule bewirkt. Anders ausgedrückt: Die Spule muss eine entsprechende Strombelastbarkeit aufweisen. 

[question:AD325]