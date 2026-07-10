Es gibt kaum Funkgeräte, bei denen man die Empfangsfrequenz direkt messen kann. Die üblichen Empfängerschaltungen weisen keinen Punkt auf, an dem sie anliegt. Deshalb schließt man zum Überprüfen der Frequenzanzeige einen möglichst genauen Oszillator oder Frequenzgenerator an die Antennenbuchse an. Dessen Frequenz wird mit der Anzeige am Empfänger verglichen.

<attention>
Ein direkt angeschlossener Frequenzgenerator kann einen Empfängereingang leicht beschädigen. Im Zweifelsfall sollte die Messung mit der niedrigsten Spannung des Generators und einem Dämpfungsglied begonnen werden.
</attention>

Natürlich gilt auch hier, dass GPS-disziplinierte Oszillatoren und OCXOs in aller Regel genauer sind als einfachere Schaltungen.

[question:AI511]
[question:AI504]

---

Bei Sendern ist die Frequenzmessung einfacher. Ein Frequenzzähler wird über ein Dämpfungsglied an die Antennenbuchse angeschlossen. Sinnvoll ist diese Messung natürlich nur bei einem unmodulierten Träger.

<indepth>
SSB-Sender erzeugen ohne Modulation kein Signal. Um ihre Sendefrequenz zu messen, kann man ein Audiosignal mit bekannter Frequenz in die Mikrofonbuchse einspeisen. Von Messwert des Frequenzzählers am Senderausgang wird bei USB die Audiofrequenz abgezogen, um die Frequenz des nicht ausgesendeten Trägers zu erhalten. Bei LSB wird sie addiert.
</indepth>

% AI502
[question:AI502]


[question:AI501]


% TODO Der Text wird noch fertig geschrieben. - DB7YI 2024-04-22

Die Frequenzmessung mittels Oszilloskop ist nur Notbehelf, weil diese Geräte nur selten eine so genaue Zeitbasis haben wie Frequenzzähler.
% AI503
[question:AI503]

Einfache Frequenzzähler arbeiten fast immer mit einer sogenannten *Torzeit*. Das Gerät schaltet den Eingang für eine bestimme Zeit ein, zählt die Perioden des Eingangssignals und berechnet daraus dessen Frequenz. Besonders einfach ist das bei einer Torzeit von einer Sekunde, denn sie ergibt direkt die Zahl der Schwingungen pro Sekunde und damit die Frequenz in Hertz.

Die Torzeit kann man bei den meisten Frequenzzählern einstellen. Eine kurze Torzeit sorgt dafür, dass die Anzeige in kurzen Abständen aktualisiert wird. Bei einer langen Torzeit dagegen wird die Messung genauer.

% TODO Bild, das die Ungenauigkeit bei kurzer Torzeit veranschaulicht

%AI505
[question:AI505]

% Fünf Fragen zu Genauigkeit und Toleranz, die ursprünglich hier standen, habe ich in den Abschnitt "Frequenzgenauigkeit" verschoben. - DB7YI 2024-04-28