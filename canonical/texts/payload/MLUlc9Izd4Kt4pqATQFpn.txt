Um bei Transvertern die benötigten Oszillatorfrequenzen zu berechnen, ist die Kenntnis der gewünschten Ein- und Ausgabefrequenzen notwendig. Weiter benötigt man die Information, ob sich der Oszillator unterhalb oder oberhalb des Nutzsignals befinden soll.

<indepth>
Wenn sich die Oszillatorfrequenz unterhalb des Nutzsignals befindet, bleibt die Seitenbandlage eines SSB-Signals (USB/LSB) erhalten.
Befindet sich die Oszillatorfrequenz oberhalb des Nutzsignals, wird die Seitenbandlage eines SSB-Signals invertiert (aus USB wird LSB und umgekehrt).
</indepth>

Rechenbeispiel:

Liegt die Oszillatorfrequenz unterhalb des Nutzsignals, so gehört zur höheren Frequenz des Nutzsignals auch die höhere Frequenz des Ausgangssignals des Konverters/Transverters.

Soll z.B. ein Frequenzbereich von $\qtyrange{438}{440}{\mega\hertz}$ auf einen Frequenzbereich von $\qtyrange{28}{30}{\mega\hertz}$ umgesetzt werden (bei Annahme, dass sich die Oszillatorfrequenz unterhalb des Nutzsignals befindet), so benötigt man eine Oszillatorfrequenz von $\qty{440}{\mega\hertz} - \qty{30}{\mega\hertz}$ oder $\qty{438}{\mega\hertz} - \qty{28}{\mega\hertz}$, was in beiden Fällen $\qty{410}{\mega\hertz}$ ergibt. Wird diese Oszillatorfrequenz mittels Frequenzvervielfachung erzeugt, so muss man diese bei der Rückrechnung auf die benötigte Frequenz des Quarzoszillators noch durch Teilen berücksichtigen.

Gleich verhält es sich für den Frequenzbereich von $\qtyrange{436}{438}{\mega\hertz}$, wenn dieser wieder auf einen Frequenzbereich von $\qtyrange{28}{30}{\mega\hertz}$ umgesetzt werden soll (ebenfalls bei Annahme, dass sich die Oszillatorfrequenz unterhalb des Nutzsignals befindet).
Hierbei ergibt sich bei der Rechnung $\qty{438}{\mega\hertz}$ - $\qty{30}{\mega\hertz}$ bzw. $\qty{436}{\mega\hertz}$ - $\qty{28}{\mega\hertz}$ eine Oszillatorfrequenz von $\qty{408}{\mega\hertz}$.

Werden die oben berechneten $\qty{408}{\mega\hertz}$ bzw. $\qty{410}{\mega\hertz}$ durch Verneunfachung der Quarz-Oszillatorfrequenz gewonnen, so ergeben sich die beiden Quarz-Oszillatorfrequenzen zu $\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ und $\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (jeweils gerundet).

[question:AF501]
[question:AF502]

%TODO: Die Frage 1472 gehört aus unserer Sicht nicht hier her, da es sich um einen Sender handelt und diese Frage nichts mit Konvertern oder Transvertern zu tun hat. Müsste evtl. in das Kapitel Sender und Senderstufen verschoben werden
[question:AF301]