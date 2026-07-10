Wichtige Messungen für den Funkamateur an Sendern sind Messungen von Ausgangsleistungen an Sendern oder die Messung von HF-Spannungen in HF-Schaltungsteilen.

Bei Messung von Senderausgangsleistungen muss der Sender mit einer definierten Impedanz, die zur Ausgangsimpedanz des Senders passt, abgeschlossen werden. Im Amateurfunk beträgt die übliche Impedanz (Senderabschluss) $\qty{50}{\ohm}$. Der Abschluss kann auch direkt in der Messschaltung erfolgen, was jedoch nur bei kleine Leistungen sinnvoll ist.

Die Messung von HF-Spannungen erfolgt mittels eines HF-Tastkopfes über Diodengleichrichtung und anschließende Glättung der entstehenden Gleichspannung mit einem nachgeschalteten Kondensator.

Bei HF-Tastköpfen mit nur einer Diode ist am Messausgang die Spitzenspannung der zugeführten HF-Spannung abzüglich der Forward-Spannung der verwendeten Diode und eines ggf. vorhandenen vorgeschalteten Spannungsteilers messbar.

[question:AI608]

Zur Erhöhung der Messgenauigkeit, insbesondere bei kleinen Leistungen im VHF/UHF-Bereich, verwendet man oft eine doppelte Gleichrichtung über 2 Dioden, so dass beide Halbwellen der HF gleichgerichtet werden (Doppelte Spitzenspannung) und, abzüglich 2 mal der Forward-Spannung der verwendeten Dioden, als addierte Messspannung am Messausgang zur Verfügung stehen.

[question:AI605]
[question:AI604]

Bei höheren HF-Leistungen muss ein entsprechend belastbares Dämpfungsglied vorgeschaltet werden, das einen Großteil der Senderausgangsleistung, die gemessen werden soll, aufnimmt. Das Dämpfungsglied ist bei der Berechnung der Leistung zu berücksichtigen.

[question:AI609]

Um Leistungen und HF-Spannungen mit den vorgenannten Schaltungen exakt messen zu können, müssen diese kalibriert werden um entsprechende Korrekturwerte für die Messungen zu erstellen.

[question:AI612]

Betrachten wir nun die Berechnung der Schaltungen im Detail.
Ein HF-Tastkopf mit einfacher Gleichrichtung und anschließender Glättung wird wie folgt berechnet:

Das HF-Eingangssignal wird durch den vorhandenen Widerstand (oder Kombination aus Einzelwiderständen) am Eingang impedanzrichtig abgeschlossen. In der dargestellten Schaltung wird die HF-Spannung durch den nachfolgenden Spannungsteiler halbiert (wobei dieser ebenfalls bzgl. der Impedanz wirksam ist). Anschließend erfolgt die Spitzenwert-Gleichrichtung mittels Diode, deren Ausgangsspannung sich als Spitzenwert abzüglich der Forward-Spannung der Diode berechnet und im nachgeschalteten Kondensator gepuffert wird.

Bei $\qty{1}{\watt}$ Eingangsleistung in einem $\qty{50}{\ohm}$-System ergibt sich eine Eingangsspannung von $\qty{7,07}{\volt}$ Effektiv-Spannung und $\qty{10}{\volt}$ Spitzenspannung.
Der nachgeschaltete Spannungsteiler halbiert diese Spannung auf $\qty{5}{\volt}$ Spitzenspannung, die nach Gleichrichtung durch die Diode abzüglich deren Forward-Spannung von $\qty{0,23}{\volt}$ noch $\qty{4,77}{\volt}$ beträgt. Gemessen werden dann gerundet ca. $\qty{4,8}{\volt}$ am Ausgang der Schaltung.

[question:AI610]

Umgekehrt kann aus der gemessenen Gleichspannung die der Schaltung zugeführte Leistung berechnet werden.

Gemessen werden am Ausgang der Schaltung $\qty{14,9}{\volt}$ Spitzenspannung. Wegen der Forward-Spannung der Diode beträgt der HF-Spitzenwert vor der Diode $\qty{15,6}{\volt}$. Unter Berücksichtigung des vorgeschalteten Spannungsteilers ergibt dies eine HF-Spitzenspannung von $\qty{31,2}{\volt}$.  Dies entspricht einer Eingangsleistung an einem $\qty{50}{\ohm}$-System von $\qty{9,73}{\watt}$ und damit ca. $\qty{9,7}{\watt}$.

[question:AI611]

Bei HF-Tastköpfen und Leistungsmessern mit doppelter Spitzenwertgleichrichtung (2 Dioden) erfolgt die Berechnung wie bei Einfachgleichrichtung, jedoch ist die doppelte Spitzenspannung am Ausgang und der doppelte Spannungsabfall durch 2 Dioden zu berücksichtigen.

[question:AI607]
[question:AI606]

Um anzuzeigen, dass ein Sender über seine Antenne Leistung abstrahlt kann ein Feldstärkeanzeiger verwendet werden. Hierbei wird über eine Messantenne einer Diode die empfangene HF zugeführt und durch die Diode gleichgerichtet. Anschließend wir die gleichgerichtete Spannung über HF-Drosseln einem Kondensator zugeführt, der die gleichgerichtete Spannung puffert. Die Anzeige erfolgt durch ein empfindliches Strommessgerät. Je höher der Zeigerausschlag des Messinstruments ausfällt, desto höher ist die an der Antenne gemessene HF-Feldstärke. Um exakte Messungen vornehmen zu können muss sowohl die Messantenne als auch der Feldstärkemesser kalibriert werden.

[question:AI613]