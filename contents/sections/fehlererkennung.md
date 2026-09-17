Die einfachste Art der Fehlererkennung wird durch das Hinzufügen eines zusätzlichen Bits realisiert, dem Prüfbit. Es wird auch *Parity Bit* genannt. Es gibt zwei Varianten dieses Verfahrens. Bei *Even Parity* wird der Wert dieses Bits für jeden Block so gewählt, dass die Anzahl der auf $\num{1}$ gesetzten Bits immer gerade ist. Bei *Odd Parity* hingegen muss die Anzahl immer ungerade sein. Sender und Empfänger müssen sich vor der Übertragung einig sein, welche der beiden Varianten verwendet wird.

<indepth>
Nehmen wir an, wir wollen folgendes Byte mit Even Parity übertragen:

[picture:677:byte:Ein Byte]

Wir zählen 5 Einsen, also eine ungerade Anzahl. Das Prüfbit muss demnach auf $\num{1}$ gesetzt werden, damit eine gerade Anzahl an Einsen herauskommt:

[picture:678:even_parity:Das Byte mit Even Parity Bit]

Wenn nun ein Übertragungsfehler *ein* Bit verändert (von $\num{1}$ zu $\num{0}$ oder umgekehrt), dann wird die Anzahl der Einsen ungerade. Der Empfänger erkennt daran, dass ein Fehler vorliegt.

Ein weiteres Beispiel folgt hier: 

[picture:679:even_parity:Byte mit Even Parity]

Im ursprünglichen Byte zählen wir 4 Einsen, was einer geraden Anzahl entspricht. Deshalb müssen wir als Prüfbit eine $\num{0}$ einfügen.
</indepth>

Dieses Verfahren stößt schnell an seine Grenzen, nämlich dann, wenn mehr als ein Fehler bei der Übertragung passiert. Werden bei der Übertragung zwei Bits verändert, so bleibt die Anzahl der Einsen gerade. Der Empfänger kann nicht mehr erkennen, dass Fehler aufgetreten sind. Treten bei der Übertragung drei Fehler auf, so entsteht wieder eine ungerade Anzahl von Einsen und der Empfänger erkennt die Fehler.

Odd Parity funktioniert im Prinzip genauso, mit einem einzigen Unterschied: Die Anzahl der Einsen muss nicht gerade, sondern immer ungerade sein. Für Odd Parity gilt genauso wie für Even Parity, dass nur eine ungerade Anzahl falsch übertragener Bits erkannt wird. Eine fehlerfreie Übertragung kann hingegen nicht von einer geraden Anzahl an Fehlern unterschieden werden.

[question:AE411]
[question:AE412]

Um Mehrbitfehler zu erkennen, kann man weitere Prüfbits hinzufügen. Dies funktioniert sehr gut bei Nachrichten mit einer festen Länge. Ist die Länge der Daten variabel, verwendet man oft spezielle Prüfsummenverfahren wie die *zyklische Redundanzprüfung (CRC)*, welche Fehler bis auf eine gewisse Restwahrscheinlichkeit erkennen. Ähnliche Verfahren sind auch im Alltag anzutreffen, beispielsweise bei Ausweisnummern oder der IBAN.

[question:AE410]
