# Lösung über Ausschlussverfahren
Es hilft zu erkennen, dass es sich hier um den im Kapitel "Demodulator" dargestellten Hüllkurvendemodulator handelt.  
Auf der linken Seite der Schaltung ist zu sehen, dass dort das ZF-Signal am Eingang der Schaltung anliegt.  
$\rightarrow$ Damit fällt die Antwort "Der Ausgang für das ZF-Signal." weg.

Der Anschluss $\text{X}$ liegt hinter einem RC-Tiefpassfilter, der mit einem Elektrolytkondensator (zu erkennen am kleinen "+") aufgebaut ist. Elektrolytkondensatoren haben eine relativ hohe Kapazität. Für den Zusammenhang von Grenzfrequenz ($f_\text{g}$) und Kapazität ($C$) betrachten wir die Formel (Filter, RC-Tiefpass) aus der Formelsammlung: 

$f_\text{g} = \frac{1}{2\cdot\pi\cdot R \cdot C}$

Eine große Kapazität ($C$) erzeugt einen großen Nenner und damit eine kleine Grenzfrequenz ($f_\text{g}$) für den RC-Tiefpassfilter.  
$\rightarrow$ Damit fallen die Antworten "Der Ausgang für das NF-Signal." und "Der Ausgang für das Oszillatorsignal." weg.

Am Anschluss $\text{X}$ liegt eine niederfrequente Spannung an, die für die Regelung genutzt werden kann.