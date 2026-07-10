Abbildung [ref:kanal] zeigt einen Sender und einen Empfänger, welche über einen Kanal miteinander verbunden sind. Beispielsweise durch das Wetter, andere atmosphärische Einflüsse oder Aussendungen anderer Stationen kann es zu Störungen auf dem Kanal kommen. Diese können zu Fehlern bei der Übertragung führen. 

<margin>
[picture:674:kanal:Kanal]
</margin>

Im Gegensatz zur Quellencodierung fügt die Kanalcodierung der zu übertragenden Information gezielt Redundanz hinzu, beispielsweise Wiederholungen oder Prüfsummen. Anders als die bei der Quellencodierung entfernte Redundanz kann diese systematisch hinzugefügte Redundanz zur automatischen Erkennung oder Korrektur von Übertragungsfehlern verwendet werden.

---

Abbildung [ref:kanalcodierer] zeigt ein Symbol für einen Kanalcodierer. Der Block stellt dar, dass Redundanz den Daten hinzugefügt wird.

<margin>
[picture:676:kanalcodierer:Kanalcodierer]
</margin>

[question:AE409]

Wir unterscheiden zwei Arten der Kanalcodierung:

* Fehlererkennung: Man kann erkennen, dass bei der Übertragung ein Fehler aufgetreten ist, und dann z. B. eine erneute Übertragung anfordern.
* Vorwärtsfehlerkorrektur: Fehler, die bei der Übertragung entstehen, werden mit Hilfe der Redundanz beim Empfänger korrigiert. 

Im Folgenden wollen wir uns diese beiden Arten genauer anschauen.