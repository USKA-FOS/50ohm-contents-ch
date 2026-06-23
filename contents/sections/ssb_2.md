In der Klasse N haben wir gelernt, dass bei der Amplitudenmodulation neben dem Träger zwei Seitenbänder entstehen, ein unteres (LSB) und ein oberes (USB), in denen die gesamte Information des Modulationssignals enthalten ist, während der Träger selbst keine Information überträgt. Da beide Seitenbänder die gleiche Information enthalten, reicht es aus, nur eines davon zu senden und den Träger zu unterdrücken (vgl. Abbildung [ref:e_ssb_am_modulation]). Dieses Verfahren nennt man Einseitenbandmodulation beziehungsweise Single Sideband (SSB), welches wir auch in der Klasse N bereits kennen gelernt hatten. Der Vorteil von SSB besteht darin, dass keine Sendeleistung für den Träger und das zweite Seitenband verschwendet wird, wodurch die gesamte Leistung effizient für die Informationsübertragung genutzt werden kann und gleichzeitig die benötigte Bandbreite deutlich geringer ist als bei AM.


Bei der Einseitenbandmodulation (SSB) enthält das Sendesignal – abhängig vom am Transceiver gewählten Seitenband – entweder die Trägerfrequenz plus der NF-Modulationsfrequenz (bei USB) oder die Trägerfrequenz minus der NF-Modulationsfrequenz (bei LSB). Die Abbildung [ref:e_ssb_einzelsignal] zeigt hierfür zwei Beispiele: Moduliert man einen Sender mit der Trägerfrequenz $\qty{7,100}{\mega\hertz}$ mit einem NF-Signal von $\qty{1}{\kilo\hertz}$ in USB, so wird vom Sender eine Frequenz von $\qty{7,100}{\mega\hertz} + \qty{1}{\kilo\hertz} = \qty{7,101}{\mega\hertz}$ abgestrahlt. Moduliert man den Sender hingegen in LSB, so wird vom Sender eine Frequenz von $\qty{7,100}{\mega\hertz} -\qty{1}{\kilo\hertz} = \qty{7,099}{\mega\hertz}$ abgestrahlt.

<margin>
[picture:1056:e_ssb_einzelsignal:Seitenbänder bei AM und SSB]
</margin>

Die folgenden Fragen können nach diesem Schema gelöst werden.

[question:EE203]
[question:EE204]

---

AM-Signale übertragen beide Seitenbänder und den Träger und haben daher eine Bandbreite von etwas mehr als dem Doppelten des modulierenden NF-Signals (vgl. Abbildung [ref:e_ssb_einzelsignal]). Die Bandbreite eines SSB-Signals entspricht in etwa der Bandbreite des modulierenden NF-Signals (nach Filterung und Begrenzung der Bandbreite des NF-Signals). Bei SSB werden auch Signalanteile unterhalb von $\qty{300}{\hertz}$ und der Träger ($\qty{0}{\hertz}$) nicht übertragen und unterdrückt. Daher hat SSB etwas weniger als die halbe Bandbreite von AM.

<margin>
[picture:743:e_ssb_einzelsignal:Seitenbänder bei AM und SSB]
</margin>

[question:EE202]
[question:EE201]

---

Wie wir bereits in der Klasse N beim Thema Morsetelegrafie mit *Continuous Wave* (CW) gelernt haben, wird dabei ein konstanter Hochfrequenzträger in einem bestimmten Rhythmus ein- und ausgeschaltet. CW-Signale benötigen im Vergleich zu sprachmodulierten Signalen wie AM und SSB die geringste Bandbreite. Dies liegt daran, dass bei CW lediglich eine einzige Frequenz getastet wird und nicht, wie bei Sprachsignalen, mehrere Frequenzanteile eines NF-Signals gleichzeitig übertragen werden müssen.

<indepth>
Die Bandbreite von CW-Signalen ist von der Zeichengeschwindigkeit (Geschwindigkeit der Tastung) abhängig und beträgt bei durchschnittlichen Gebegeschwindigkeiten von 20 Wörtern pro Minute (100 Zeichen pro Minute) ca. $\qty{300}{\hertz}$.
</indepth>

[question:EE207]

Um Störungen benachbarter Stationen im Frequenzband zu vermeiden, sollte die belegte Bandbreite eines SSB-Signals auf maximal etwa $\qty{2,7}{\kilo\hertz}$ begrenzt werden. Diese Bandbreite ist für eine gute Sprachverständlichkeit vollkommen ausreichend. Aus diesem Grund wird das NF-Signal des Mikrofons im Sender bandbegrenzt: Frequenzanteile unterhalb von etwa $\qty{300}{\hertz}$ sowie oberhalb von etwa $\qty{3}{\kilo\hertz}$ werden unterdrückt, da sie nur wenig zur Sprachverständlichkeit beitragen.

[question:EJ211]
[question:EJ210]

In der Praxis besitzen SSB-Filter zur Erzeugung eines SSB-Signals häufig eine Bandbreite von nur etwa $\qty{2,4}{\kilo\hertz}$. Auch diese geringere Bandbreite reicht in vielen Fällen für eine gute Sprachverständlichkeit aus und ermöglicht zugleich eine noch effizientere Nutzung des verfügbaren Frequenzspektrums.

[question:EF310]

Störungen benachbarter Stationen können auch durch sog. *Splatter* auftreten, die durch eine zu hoch eingestellte Mikrofonverstärkung und somit Übersteuerung der NF-Stufen erfolgen können. Im Sendesignal wirkt sich dies so aus, dass die Bandbreite der SSB-Übertragung steigt, was andere Stationen stören kann.

[question:EJ215]

Eine zu geringe Mikrofonverstärkung (NF-Amplitude) führt zu einer geringeren Modulation des SSB-Senders, was eine Verkleinerung der Ausgangsleistung zur Folge hat. Daher ist es wichtig, dass die Mikrofonverstärkung für gute Kommunikation in SSB optimal angepasst wird (nicht zu groß und nicht zu klein). Im Kapitel Dynamikkompressor gehen wir darauf nochmal genauer ein. 

[question:EE206]
[question:EE205]
