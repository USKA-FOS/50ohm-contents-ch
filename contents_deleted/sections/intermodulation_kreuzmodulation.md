In einem Empfänger, an dessen Eingang zwei starke HF-Signale anliegen, können Störungen durch Intermodulation oder Kreuzmodulation verursacht werden.
Bei Intermodulation äußert sich dieser Effekt so, dass durch nichtlineares Verhalten der Empfängerstufe (Betrieb im nichtlinearen Grenzbereich), ähnlich wie in einem Mischer, zusätzliche unerwünschte Frequenzen erzeugt werden. Diese können erwünschte Empfangssignale überlagern und stören.
Bei Kreuzmodulation äußert sich dieser Effekt so, dass das gewünschte Empfangssignal durch die Modulation eines starken frequenzmäßig benachbarten AM-Signals beeinflusst wird. Hierdurch wird die Modulation des benachbarten Senders im Empfangssignal hörbar und stört dieses.

[question:AF217]
[question:AF219]
[question:AF222]
[question:AF218]

Um ein starkes unerwünschtes Signal bereits vor dem Empfängereingang zu unterdrücken kann beispielsweise ein Saugkreis, welcher auf die exakte Frequenz des störenden Signals abgestimmt wird vor dem Empfängereingang für Abhilfe sorgen.

[question:AF223]

Die Großsignalfestigkeit eines Empfängers kann durch den sog. Intercept Point dritter Ordnung (IP3) beschrieben werden. Er ist ein Maß für den Punkt an dem unerwünschte Mischprodukte 3. Ordnung den Amplitudenwert des Eingangssignales erreichen. Je höher der IP3 eines Empfängers ist, desto größere Signale kann dieser noch störungsfrei verarbeiten.

%TODO: Weitere Informationen zu IP3 ggf. Tipp, Grafik zu IP3

[question:AF221]

Um das Entstehen von unerwünschten Mischprodukten im Empfängereingang durch starke Signale zu verringern kann ein schaltbares Dämpfungsglied (Attenuator) am Empfängereingang vorgeschaltet werden. Hierdurch werden Intermodulationsprodukte sowie Kreuzmodulation im Empfänger verringert. Das Nutzsignal wird hierbei nur um den Faktor des Dämpfungsgliedes reduziert - störende Mischprodukte werden jedoch aufgrund der mathematischen Gegebenheiten beim Mischprozess um den Faktor $\num{3}$ (3. Ordnung) in $\unit{\dB}$ abgeschwächt. Beispielsweise reduziert ein $\qty{10}{\dB}$ Dämpfungsglied das Nutzsignal nur um $\qty{10}{\dB}$ während unerwünschte Mischprodukte bereits um $\qty{30}{\dB}$ gedämpft werden.

[question:AF220]