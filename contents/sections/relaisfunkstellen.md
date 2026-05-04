Eine Relaisfunkstelle ermöglicht eine größere Reichweite als dies bei direkter Verbindung zwischen zwei Amateurfunkstellen oftmals möglich ist. Relaisfunkstellen werden meist an exponierten Standorten, z. B. auf Berggipfeln, Hochhäusern, Kirch- und sonstigen Türmen, errichtet. Es gibt auch Relaisfunkstellen in Satelliten, die um die Erde kreisen. Aufbau und Funktion einer solchen Funkstelle sind in Bild [ref:n_relaisfunkstellen_aufbau] dargestellt. 

[picture:648:n_relaisfunkstellen_aufbau:Schematische Darstellung einer Relaisfunkstelle mit Nutzern]

Ist zum Beispiel ein Berg zwischen zwei Funkstationen, so ist es unmöglich, durch den Berg hindurchzusenden. Eine Relaisfunkstelle auf dem Berggipfel ermöglicht es trotzdem, eine Verbindung aufzubauen, da beide Stationen das Relais direkt erreichen  können.

Relaisfunkstellen werden auch kurz als Relais oder als Repeater bezeichnet. Man kann sie daran erkennen, dass sie regelmäßig ihr Rufzeichen aussenden. Das Rufzeichen einer Relaisfunkstelle beginnt gemäß [Rufzeichenplan](https://50ohm.de/rzp) in der Regel mit DB0, DM0 oder DO0.

Die amtliche Definition von Repeatern liest sich etwas trockener: *"Relaisfunkstelle": eine fernbediente Amateurfunkstelle (auch in Satelliten), die empfangene Amateurfunkaussendungen, Teile davon oder sonstige eingespeiste oder eingespeicherte Signale fern ausgelöst aussendet und dabei zur Erhöhung der Erreichbarkeit von Amateurfunkstellen dient*

Die folgende Frage zu dieser Definition lässt sich aber auch gut im Ausschlussverfahren lösen, wenn man folgendes weiß:
* Relaisfunkstellen werden nicht mit persönlichen Rufzeichen betrieben.
* Relaisfunkstellen sind üblicherweise nicht ständig besetzt.
* Relaisfunkstellen müssen nicht zwingend an geografisch exponierten Standorten betrieben werden.

[question:VD118]

---

Eine Relaisfunkstelle empfängt auf ihrer Eingabefrequenz das Signal einer Amateurfunkstation und sendet es zeitgleich auf ihrer Ausgabefrequenz aus. Damit der Sender der Relaisfunkstelle den eigenen Empfänger nicht stört, sind Sende- und Empfangsfrequenz in der Regel unterschiedlich. Den Abstand zwischen Sende- und Empfangsfrequenz nennt man Frequenzablage oder auch einfach nur Ablage. Die in Deutschland üblicherweise verwendeten Ablagen findest du in der Tabelle [ref:n_relaisfunkstellen_ablage].

<margin>
| r: Band | X: Ablage |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Frequenzablage]
</margin>

Beispielsweise wird die Frequenz eines $\qty{70}{\centi\meter}$ Relais so angegeben:
* Eingabefrequenz: $\qty{431,275}{\mega\hertz}$
* Ablage: $\qty{+7,600}{\mega\hertz}$
* Ausgabefrequenz: $\qty{438,875}{\mega\hertz}$

[question:BE401]
[question:BE402]
[question:BE403]

<indepth>
Einige Relaisfunkstationen arbeiten auch im sogenannten *Crossband-Betrieb*. Das bedeutet: Eine Station sendet und empfängt auf einem Band (z. B. $\qty{70}{\centi\meter}$), eine andere Station auf dem gleichen Relais, aber auf einem anderen Band (z. B. $\qty{2}{\meter}$). Die Relaissteuerung vermittelt die Gespräche auf die beiden Bänder. Es kann auch eine Umsetzung der Sendeart erfolgen, beispielsweise von SSB auf FM.
</indepth>

Eine Relaisstation, die nicht Sprache sondern Daten übermittelt, wird Digipeater genannt. Ein Digipeater ist in der Lage, Datenpakete zu empfangen und wieder auszusenden. Hierbei ist die Besonderheit, dass die Aussendung nur in Teilen oder zeitversetzt geschehen kann. Ebenso können Datenpakete wiederholt oder einzelne Datenfelder geändert werden.

[question:NF118]

---

Bevor man über eine Relaisfunkstelle den Funkbetrieb aufnehmen kann, muss man ihre technischen Besonderheiten und Parameter kennen. Für bestimmte Relais sind zusätzlich zur Frequenz noch weitere Einstellungen an deinem Transceiver notwendig, um einen störungsfreien Betrieb zu gewährleisten. Neben analogem FM (Frequenzmodulation) werden noch digitale Verfahren, wie zum Beispiel DMR und D-Star, als Sprachübertragungsverfahren genutzt.

<tip>
Informationen zu Relaisfunkstellen sowie den technischen Parametern und Besonderheiten erhält man vom nächstgelegenen DARC-Ortsverband, der relaisverantwortlichen Person oder aus dem Internet.
</tip>

[question:NE309]
[question:NE308]

Eine wichtige Einstellung ist die Kanalbandbreite bei FM-Betrieb. Wir erinnern uns: Die Bandbreite gibt an, wieviel "Platz" man im Frequenzspektrum mit der Aussendung belegt. Hier gibt es einerseits das Wide-FM, die Bandbreite beträgt hier $\qty{25}{\kilo\hertz}$ und wird am Display beispielsweise als *FM-W* angezeigt. Andererseits gibt es das Schmalband-FM (Narrow-FM), welches eine Bandbreite von nur $\qty{12,5}{\kilo\hertz}$ belegt und z. B. am Funkgerät als *FM-N* dargestellt wird. Viele Repeater mögen es gar nicht, wenn die Signale zu breit sind. Denn dadurch können verzerrte Signale entstehen und benachbarte Relaisfrequenzen gestört werden.

[question:BE407]

Der Funkbetrieb über fernbediente Amateurfunkstellen ist grundsätzlich allen Funkamateuren mit zugeteiltem Rufzeichen zu gestatten. Zur Sicherstellung eines störungsfreien Betriebs kann der Betreiber allerdings andere Funkamateure von der Nutzung der Amateurfunkstelle ausschließen. Die BNetzA ist hiervon zu unterrichten.

[question:VD504]

Bei Funkbetrieb über Relaisstationen sollten die Durchgänge möglichst kurz gehalten werden, damit mobile und portable Stationen das Relais leichter nutzen können, insbesondere, wenn sie sich nur kurzzeitig im Empfangsbereich befinden. Zwischen den Durchgängen sollte man eine Pause einhalten, um weiteren Stationen eine Möglichkeit zu geben, sich reinzumelden.

[question:BE406]
[question:BE404]

Bei einer gleichzeitigen Spracheingabe zweier unterschiedlicher Stationen wird die Aussendung des Relais bis zur Unlesbarkeit gestört. Um dieses sogenannte Doppeln zu vermeiden, sollte stets eine ordentliche Übergabe zwischen den Repeaternutzern erfolgen. Das bedeutet auch, erst dann mit der Aussendung zu beginnen, wenn die vorherige Station ihre Aussendung beendet hat.

[question:NE310]
[question:BE405]

In der bereits besprochenen Anlage 1 der AFuV finden sich auch Vorgaben für die Sendeleistungen von Relaisstationen. Oberhalb von 30 MHz darf eine automatisch arbeitende Station mit maximal 50 W ERP betrieben werden.

[question:VD503]

Eine Besonderheit gibt es bei der Beurteilung einer Funkverbindung über eine Relaisfunkstation. Da die Signalstärke, mit der man den Funkpartner empfängt, die Signalstärke der Relaisstation ist und nicht die Signalstärke des Funkpartners, verzichtet man auf deren Angabe. Im Rapport wird nur die Lesbarkeit (R) beurteilt.

[question:BE408]