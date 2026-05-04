Jeder hat bestimmt schon einmal einen übersteuerten Verstärker oder eine übersteuerte Tonaufnahme gehört. Wird beim Aufzeichnen oder beim Abspielen die Lautstärke zu sehr aufgedreht, dann kann es zu Verzerrungen kommen.

Wird beispielsweise ein zu starkes Audiosignal an den Eingang eines Senders angelegt, können Oberschwingungen entstehen und ausgesendet werden. In Abbildung [ref:uebersteuerung_ft8] ist ein derart übersteuertes FT8-Signal im Wasserfalldiagramm dargestellt: Links ist in Gelb das erwünschte Signal zu sehen und rechts davon die unerwünschten Oberschwingungen.

<margin>
[picture:720:uebersteuerung_ft8:Ein übersteuertes FT8-Signal, ganz links das erwünschte, rechts davon die unerwünschten Oberschwingungen]
[photo:328:uebersteuerung_ft8_wsjtx:Ein übersteuertes FT8-Signal im Wasserfall der Software WSJTX]
</margin>

Zu Verzerrungen durch Übersteuerung kann es auch im Sendeverstärker kommen. Um das zu verhindern, verfügen viele Funkgeräte über eine automatische Pegelregelung (englisch: Automatic Level Control, ALC). Sie kann eingreifen, indem sie die Verstärkung herunterregelt.

---

Bei Aussendungen mit digitalen Übertragungsverfahren wie z. B. FT8, WSPR oder RTTY mit konstanter Amplitude ist das Ansprechen der ALC oft ein Hinweis darauf, dass das Audiosignal vom PC zu stark ist und übersteuert wird. Das kann zu unerwünschtem *Splatter* auf dem Band führen. Deshalb sollte das Audiosignal bei diesen Übertragungsverfahren stets sorgfältig kontrolliert werden. Ein Herunterregeln des Pegels durch die ALC wäre für sich genommen zunächst unkritisch, da bei diesen Verfahren die Information in der Frequenzumtastung steckt. Trotzdem ist das Auslösen der ALC ein starkes Indiz, dass das NF-Signal bereits übersteuert ist.

<indepth>
Das [Handbuch](https://50ohm.de/wsjtx) der Software WSJTX gibt hierzu eine gute Empfehlung: Im ersten Schritt sollte man durch Drücken der TUNE-Taste den Transceiver in den Sendemodus schalten, um einen gleichmäßigen Ton zu erzeugen. Dieser Ton lässt sich mit der Monitor-Funktion des Geräts durch Hören überprüfen oder im Wasserfall des TRX optisch kontrollieren. Dabei sollten keine Verzerrungen, Klicks oder andere Störungen auftreten. Anschließend stellt man den PWR-Regler von seinem Maximum langsam nach unten, bis der HF-Ausgang des Senders leicht abfällt – dies gilt allgemein als gutes Niveau für die Audioaussteuerung. Auch die ALC-Anzeige sowie die Ausgangsleistung des Transceivers können dabei helfen, den optimalen NF-Signalpegel zu finden.
</indepth>

Bei digitalen Übertragungsverfahren mit veränderlicher Amplitude (z. B. PSK31, QPSK, 16-QAM) kann die ALC jedoch zu neuen Problemen führen. Das Signal könnte je nach Lautstärke oder Frequenz die ALC zu verschiedenen Zeitpunkten unterschiedlich stark auslösen und somit die Amplitude über den Verlauf der Zeit unerwünscht verändern. Das heißt, unser eigentliches Nutzsignal wird zusätzlich amplitudenmoduliert. Dadurch entstehen weitere Frequenzanteile, die als Nebenaussendungen ausgestrahlt werden. Einerseits können dadurch andere Funkamateure oder Funkdienste auf benachbarten Frequenzen gestört werden. Andererseits wird die Decodierung beim Empfänger erschwert.

Ob es durch die ALC zu Problemen kommt und wie stark diese ausfallen, hängt von vielen Faktoren ab. Neben dem verwendeten Übertragungsverfahren spielt auch die konkrete Umsetzung der ALC im Transceiver, z. B. hinsichtlich der Reaktions- und Haltezeit, eine Rolle. Auch die Anzeige der ALC ist in verschiedenen Geräten unterschiedlich. Ein Blick ins Handbuch kann Aufschluss geben, wann die Pegelregelung eingreift und wie dies angezeigt wird. Allgemein lässt sich jedoch sagen: Wenn die ALC nicht eingreift, erzeugt sie auch keine Probleme.

Merke: Bei digitalen Übertragungsverfahren mittels NF-Signal ist darauf zu achten, den NF-Pegel so klein zu halten, dass keine Übersteuerung eintritt und die automatische Pegelregelung nicht eingreift.

[question:EJ218]
[question:EJ217]
[question:EJ219]