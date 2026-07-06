%YPA: Issue #11 von ARK beachten.

Wie wir gelernt haben, hängt die belegte Sendebandbreite von der Modulationsart und bei FM auch noch vom Hub ab. Für die verschiedenen Amateurfunkbänder sind jeweils maximal zulässige Bandbreiten festgelegt. Diese findet man in der [Anlage 1](https://50ohm.de/a1) der Amateurfunkverordnung, aus der wir auch schon die Bandgrenzen entnommen haben. Diese Bandbreiten dürfen nicht überschritten werden. Jeder Funkamateur ist selbst für die Einhaltung verantwortlich.

<webmargin>
| l: Frequenzbereiche | l: Status | X: zus. Nutzungsbedingungen|
| $\qtyrange{135,7}{137,8}{\kilo\hertz}$| S | 1 2 10 |
| $\qtyrange{472}{479}{\kilo\hertz}$| S | 1 |
| $\qtyrange{3500}{3800}{\kilo\hertz}$ | P | 3 |
| $\qtyrange{10100}{10150}{\kilo\hertz}$ | S | 1 10 12 |
| $\qtyrange{28}{29,7}{\mega\hertz}$ | P | 4 13 |
| $\qtyrange{144}{146}{\mega\hertz}$ | P | 6 13 |
| $\qtyrange{430}{440}{\mega\hertz}$ | P | 7 13 |
[table:n_tab_afuv:Auszug AfuV Anlage 1]
</webmargin>

<webmargin>
Die Zahlen bei den zusätzlichen Nutzungsbedingungen in der oben genannten Tabelle bedeuten (die nicht wiedergegebenen Zahlen sind für die Bandbreite unerheblich):
* *1* Maximal zulässige belegte Bandbreite einer Amateurfunk-Aussendung: $\qty{800}{\hertz}$.
* *3* Maximal zulässige belegte Bandbreite einer Amateurfunk-Aussendung: $\qty{2,7}{\kilo\hertz}$.
* *4* Maximal zulässige belegte Bandbreite einer Amateurfunk-Aussendung unterhalb $\qty{29}{\mega\hertz}$: $\qty{7}{\kilo\hertz}$, oberhalb $\qty{29}{\mega\hertz}$: $\qty{40}{\kilo\hertz}$.
* *6* Maximal zulässige belegte Bandbreite einer Amateurfunk-Aussendung: $\qty{40}{\kilo\hertz}$.
* *7* Maximal zulässige belegte Bandbreite einer Amateurfunk-Aussendung: $\qty{2}{\mega\hertz}$; bei amplitudenmodulierten Fernsehaussendungen: $\qty{7}{\mega\hertz}$.
</webmargin>

Die folgenden Fragen lassen sich alle mit Hilfe der Fußnoten in der Anlage 1 der Amateurfunkverordnung lösen, die - wie schon erwähnt - während der Prüfung als Hilfsmittel zur Verfügung steht. Wir empfehlen, sich vor der Prüfung mit der Anlage vertraut zu machen!

[question:VD738]
[question:VD739]
[question:VD740]
[question:VD741]
[question:VD742]

---

Besonders aufpassen muss man bei Sendungen in der Nähe der Grenzen der Amateurfunkbänder. Ein Beispiel: Nehmen wir an, ein FM-Signal belegt eine Bandbreite von $\qty{15}{\kilo\hertz}$, und wir stellen den Sender auf die untere Bandgrenze des $\qty{70}{\centi\meter}$-Bandes ein, also auf $\qty{430}{\mega\hertz}$. Das Sendesignal befindet sich um die Trägerfrequenz herum, also jeweils $\qty{7,5}{\kilo\hertz}$ unterhalb und oberhalb. Es würde sich also von $\qty{429,9925}{\mega\hertz}$ bis $\qty{430,0075}{\mega\hertz}$ erstrecken. Da das Signal somit zur Hälfte außerhalb des Bandes wäre, dürfen wir nicht auf PTT drücken! Wir müssen also bei FM, aber auch bei AM, immer mindestens einen Abstand von der halben belegten Bandbreite zur Bandgrenze hin einhalten.

<indepth>
[picture:908:n_bandbreite_falsch:Falsch -- Senden außerhalb der Bandgrenzen]
[picture:909:n_bandbreite_richtig:Richtig -- Senden innerhalb der Bandgrenzen]
</indepth>

<indepth>
Bei SSB verhält es sich an der Bandgrenze ein wenig anders. Hier ist das Signal nur auf einer Seite der (unterdrückten) Trägerfrequenz zu finden. Bei LSB ist das Signal vollständig unterhalb der Trägerfrequenz, bei USB ist es vollständig oberhalb der Trägerfrequenz. Wenn man also beispielsweise als Sendefrequenz die obere Bandgrenze einstellt, dann dürfte man mit LSB durchaus senden, da das gesamte Signal innerhalb des Bandes bleibt. Mit USB dürfte man dort allerdings nicht senden, da das gesamte Signal außerhalb des Bandes wäre.
</indepth>

[question:NE305]
[question:BC225]
