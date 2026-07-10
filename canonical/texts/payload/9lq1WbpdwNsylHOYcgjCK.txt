<margin>
[picture:735:aufbau_sender:Blockdiagramm eines einfachen Senders]
</margin>

In Abbildung [ref:aufbau_sender] wird gezeigt, aus welchen Komponenten man einen AM-Sender aufbauen kann. Einige der Blöcke kennen wir schon vom Empfänger, andere sind neu:
1. Mikrofon: Das Mikrofon wandelt die Schallwellen der Sprache in niederfrequente elektrische Schwingungen um. Man kann stattdessen aber auch, z. B. für digitale Übertragungsverfahren, das niederfrequente Signal vom Audio-Ausgang eines Computers verwenden.
2. Niederfrequenz-Verstärker: Das Signal vom Mikrofon bzw. Computer wird zunächst verstärkt.
3. Mischer: Der Mischer fügt den vom Oszillator (4) erzeugten Hochfrequenzträger mit der niederfrequenten Schwingung vom Mikrofon bzw. Computer zusammen. Das führt dazu, dass der Hochfrequenzträger mit dem Sprach- bzw. Datensignal amplitudenmoduliert wird.
4. Oszillator: Der Oszillator erzeugt die hochfrequente Schwingung mit der Frequenz, auf der gesendet werden soll, beispielsweise $\qty{29,5}{\mega\hertz}$.
5. Bandpassfilter: Da der Mischer aufgrund seiner Funktionsweise neben den gewünschten Frequenzen auch weitere, unerwünschte Frequenzen erzeugt, müssen diese mit einem Bandfilter gesperrt werden.
6. Hochfrequenz-Verstärker: Das Hochfrequenzsignal wird nun verstärkt, damit es über die gewünschte Sendeleistung verfügt.
7. Tiefpassfilter: Da auch die Verstärkung unerwünschte Frequenzen erzeugen kann, muss jetzt nochmal gefiltert werden.
8. Antenne: Das Hochfrequenzsignal wird nun an die Antenne gegeben und von dieser als Funkwelle abgestrahlt.

%[class:N]
<indepth>
Wenn ein Mischer zwei Signale zusammenfügt, dann entspricht das mathematisch einer Multiplikation der beiden Signale. Daher findet sich auch das Malkreuz im Block-Symbol für den Mischer wieder. Wie ein Mischer genau funktioniert, ist Inhalt des Kurses für die Klasse A.
</indepth>
%[/class]

[question:NF401]
[question:NF403]

Für die folgende Frage ist es wichtig, sich daran zu erinnern, dass ein Sender einen Oszillator und einen Mischer benötigt.

[question:NF402]

Eine Amateurfunkanlage muss nach den allgemein anerkannten Regeln der Technik aufgebaut und betrieben werden. Das gilt natürlich auch ganz besonders für Sender.

[question:VD106]

