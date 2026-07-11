Bei der Amplitudenmodulation (AM) wird ein Modulationssignal, z. B. ein Sprachsignal, durch Änderung der Amplitude auf den Träger aufmoduliert. Die Frequenz des Trägers wird bei AM nicht beeinflusst, sondern bleibt unverändert.

Den einfachsten und zugleich extremsten Fall haben wir mit der Übertagung von Morsezeichen mittels Continuous Wave (CW) schon kennengelernt. Das Ein- und Ausschalten des Trägers im Rhythmus der Bedienung der Morsetaste kann man auch als Wechsel zwischen  minimaler und maximaler Amplitude beschreiben.

Um ein Sprachsignal mittels AM zu modulieren, wird auch der Bereich zwischen minimaler und maximaler Amplitude genutzt. Im Wasserfalldiagramm in Abbildung [ref:n_Wasserfall0] sehen wir ein amplitudenmoduliertes Sprachsignal. Man kann in der Mitte deutlich den Träger als schmale Linie mit konstanter Frequenz erkennen. Links und rechts vom Träger sieht man allerdings auch etwas, obwohl die Frequenz des Trägers gar nicht beeinflusst wurde!

<margin>
[picture:716:n_Wasserfall0:Signal eines AM-Radiosenders (Sprache / Musik)]
</margin>

Dieser unerwartete Effekt entsteht dadurch, dass sich durch die Änderung der Amplitude die Form des Trägers ändert und er nicht mehr einer reinen Sinusschwingung entspricht. Die zusätzlichen Frequenzen bezeichnen wir als *Seitenbänder*. In diesen steckt die übertragene Information, also z. B. die Sprache. In Abbildung [ref:n_seitenband] sehen wir eine übliche symbolhafte Darstellung von AM mit dem Träger in der Mitte und den beiden Seitenbändern links und rechts davon.

<margin>
[picture:476:n_seitenband:Symbolische Darstellung eines amplitudenmodulierten Signals mit Träger und Seitenbändern]
</margin>

<webindepth>
*Warum entstehen bei AM zusätzliche Frequenzen neben dem Träger?* Das lässt sich erklären, wenn man versteht, was in einem Amplitudenspektrum oder Wasserfalldiagramm genau dargestellt wird: Es zeigt für jede Frequenz an, wie groß die Amplitude ist. Genauer müssen wir sagen: Es zeigt für alle möglichen Sinusschwingungen mit verschiedenen Frequenzen an, wie stark deren Amplitude ist. Wenn also die Anzeige z. B. bei $\qty{144,3}{\mega\hertz}$ ausschlägt, dann wird eine reine Sinusschwingung mit einer Frequenz von $\qty{144,3}{\mega\hertz}$ gemessen. Schlägt die Anzeige aber beispielsweise gleichzeitig bei $\qty{144,300}{\mega\hertz}$ und bei $\qty{144,301}{\mega\hertz}$ aus, dann wurden zwei Sinusschwingungen gemessen.

Betrachten wir mit diesem Wissen noch einmal die AM-Sendung im Wasserfalldiagramm. Wir können jetzt erkennen, dass viele verschiedene Frequenzen zwischen $\qty{144,250}{\mega\hertz}$ und $\qty{144,350}{\mega\hertz}$ mit unterschiedlicher Amplitude auftreten. Es sind also viele verschiedene Sinusschwingungen gleichzeitig messbar.

[picture:738:n_seitenband_frequenzen_einzeln:Mehrere Sinusschwingungen unterschiedlicher Frequenz]

Es bleibt die Frage, wieso aus einer einzigen Sinusschwingung, die man durch Modulation verformt, plötzlich mehrere Sinusschwingungen werden. Um dies zu beantworten, schauen wir uns den Weg andersherum an. Wenn man mehrere Sinusschwingungen unterschiedlicher Frequenz hat und diese aufsummiert, entsteht eine "verformte" Schwingung!

[picture:739:n_seitenband_frequenzen_addiert:Summe mehrerer Sinusschwingungen unterschiedlicher Frequenz]

Es sind einfach zwei verschiedene Sichtweisen. Man kann es entweder als verformte Schwingung auffassen oder eben als Summe mehrerer Sinusschwingungen. Und das ist der Grund, warum die Änderung der Amplitude eines Trägers dazu führt, dass man weitere Frequenzen neben dem Träger im Wasserfalldiagramm sieht.
</webindepth>

[question:NE202]
[question:NE206]

Übrigens ist die von AM belegte Bandbreite doppelt so hoch wie die höchste Frequenz des Modulationssignals. Bei unserem Beispiel aus dem vorherigen Abschnitt war die höchste Frequenz $\qty{2700}{\hertz}$. Entsprechend würde dieses Signal als AM-Sendung eine Bandbreite von $\qty{5400}{\hertz}$ belegen.
