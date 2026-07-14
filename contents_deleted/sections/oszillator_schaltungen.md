Oszillatoren sind eines der wichtigsten Schaltungselemente im Amateurfunk. Sie sind sozusagen das Herz eines jeden Funkgerätes. Oszillatoren dienen der Erzeugung von hochfrequenten Schwingungen in Sendern und Empfängern.

Herzstück eines Oszillators ist ein Verstärkerelement, dessen *Ausgangssignal wieder auf dessen Eingang rückgekoppelt* wird.

Damit ein Oszillator ungedämpfte Schwingungen erzeugen kann, müssen *zwei Grundbedingungen* erfüllt sein.
Zum einen muss das *Ausgangssignal gleichphasig auf den Eingangspunkt der Schaltung rückgekoppelt* werden.
Hierbei muss zum anderen die *Amplitude des rückgekoppelten Signals mindestens die gleiche Größe* wie die des Eingangssignals haben. Man sagt auch, dass die sog. *Schleifenverstärkung größer 1* sein muss, damit eine Selbsterregung möglich ist, die die Schwingung aufrechterhält.

[question:AD613]

<margin>
[picture:760:a_oszillator_schaltungen_oszillator:Schaltung eines kapazitiv rückgekoppelten Oszillators]  
</margin>

%TODO: Evtl. Bild 760 ableiten und noch um die 3 Punkte der Dreipunktschaltung ergänzen (am kapazitiven Spannungsteiler - oben, in der Mitte und unten)

Die in Abbildung [ref:a_oszillator_schaltungen_oszillator] abgebildete Schaltung stellt einen kapazitiv rückgekoppelten Dreipunktoszillator dar. Das Ausgangssignal wird vom Emitter der Schaltung über einen kapazitiven Spannungsteiler auf die Basis des Transistors rückgekoppelt. Die Frequenz des Oszillators wird überwiegend durch den Schwingkreis in der Basis (bestehend aus Spule und Trimmkondensator) sowie den zum Schwingkreis parallel geschalteten kapazitiven Spannungsteiler bestimmt.
Bei der Schaltung handelt es sich um einen Oszillator in Kollektorschaltung, da der Kollektor wechselspannungsmäßig auf Masse liegt.

[question:AD614]
[question:AD616]

Zur Erhöhung der Frequenzstabilität eines Oszillators kann dessen frequenzbestimmende Komponente (Schwingkreis) durch einen Quarz ersetzt werden. Quarze können sowohl bei ihrer Grundfrequenz als auch auf ihren harmonischen Frequenzen (Oberschwingungen/Obertöne) zum Schwingen angeregt werden. Damit ein Quarz jedoch auf einer Oberschwingung betrieben werden kann, muss der Verstärker frequenzselektiv (z.B. durch Verwendung eines Schwingkreises) ausgelegt sein. Ist dieser nicht vorhanden, so kann man daraus ersehen, dass der Quarz auf seiner Grundfrequenz betrieben wird (siehe Abbildung [ref:a_oszillator_schaltungen_quarzoszillator] ).

<margin>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Schaltung eines Quarzoszillators in Kollektorschaltung mit Betrieb des Quarzes auf Grundfrequenz]  
</margin>

[question:AD617]

Das Oszillatorsignal sollte immer am niederohmigsten Punkt eines Oszillators ausgekoppelt werden, um diesen möglichst wenig zu belasten. In einer Kollektorschaltung ist dies der Emitter des Transistors.

[question:AD610]

Einem Oszillator sollte immer eine sog. Pufferstufe nachgeschaltet werden, die dafür sorgt, dass der Oszillator von weiteren Schaltungsteilen entkoppelt wird und in seiner Frequenz nicht durch Belastung des Ausgangs beeinflusst wird. Eine Pufferstufe ist meist als Kollektorschaltung ausgelegt (Emitterfolger) und hat eine hohe Eingangsimpedanz, die den Oszillator nur minimal belastet. An dessen Ausgang kann das Oszillatorsignal dann niederohmig weiterverarbeitet werden.

Messungen an Oszillatoren sollten immer nach der Pufferstufe durchgeführt werden, da ansonsten der Oszillator mit parasitären Kapazitäten belastet wird und in dessen Frequenz hierdurch beeinflusst wird.

[question:AD615]
[question:AD619]
[question:AD618]










