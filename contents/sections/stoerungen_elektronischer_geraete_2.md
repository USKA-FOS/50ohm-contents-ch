In den Lektionen der Klassen N und E haben wir bereits typische Beeinflussungen elektronischer Geräte und Anlagen kennengelernt – etwa durch direkte Einstrahlung in das Gehäuse oder durch Einkopplung in Zuleitungen – sowie passende Gegenmaßnahmen und Verhaltensweisen. In der Klasse A werden diese Aspekte noch etwas weiter vertieft. 

[question:AJ105]

Kommt es bei digitalen Eigenbauempfängern zu Empfangsstörungen so kann eine mögliche Ursache hierfür eine schlechte Schirmung des Empfängers sein. Hier bietet es sich an die Leiterplatte des Empfängers in ein geerdetes Metallgehäuse einzubauen. Insbesondere bei SDR-Empfängern oder Eigenbaulösungen in SDR-Technik ist eine gute Schirmung zur Vermeidung von Einstrahlungen unbedingt erforderlich. Umgekehrt werden so auch unerwünschte Abstrahlungen durch diese Geräte vermindert.

[question:AJ103]

---

In der Klasse E haben wir uns bereits mit Einkopplungen in Netzleitungen beschäftigt. Es gibt jedoch eine weitere Gegenmaßnahme, die wir uns im Folgenden genauer ansehen wollen. Sollten Störungen über die Netzzuleitung einströmen, so bietet sich der Einbau eines Netzfilters in Form eines Tiefpassfilters (Vgl. Abbildung [ref:a_netzfilter] und Abbildung [ref:a_netzfilter_draw]) an. Diese Filter sind unter Beachtung der VDE-Vorschriften als fertige Geräte erhältlich. 

[question:AJ116]
[question:AJ117]
[question:AJ118]

<margin>
[photo:244:a_netzfilter:Netzfilter]
[picture:367:a_netzfilter_draw:Schaltung eines Netzfilters]
</margin>

Unterschiedliche Übertragungsverfahren haben aufgrund ihrer Modulationscharakteristik unterschiedliche Wirkungen hinsichtlich Beeinflussungen von Geräten und Leitungen. Insbesondere die Modulationsarten CW sowie SSB (bei denen sich die Amplitude rasch ändert) führen oft zu Beeinflussungen in Lautsprecherzuleitungen und einer hierauf folgenden Gleichrichtung der HF an den Basis-Emitter-Strecken im NF-Teil von Verstärkern. Der Basis-Emitter-Übergang verhält sich hierbei wie eine Diode und richtet die HF gleich. Hierdurch wird die hierdurch demodulierte NF in den Lautsprechern hörbar.

[question:AJ107]
[question:AJ106]

Um DVB-T Empfänger vor starken Signalen eines VHF/UHF Amateurfunksenders in unmittelbarer Nähe zu schützen sollte in die Antennenzuleitung des DVB-T-Empfängers ein Hochpassfilter eingebaut werden. Dies ist jedoch nur bei passiven Empfangsantennen wirksam. Insbesondere unselektive TV-Antennenvorverstärker werden durch benachbarte Sendesignale schnell übersteuert, da diese einen breiten Frequenzbereich verstärken.
Bei aktiven Empfangsantennen muss ein Hochpassfilter vor dem Antennenvorverstärker der Antenne eingebaut werden.
Beim Einbau von Filtern ist auch die Einfügedämpfung der Filter im Durchlassbereich zu beachten. Diese sollte so gering wie möglich sein und nicht mehr als $\qtyrange{2}{3}{\dB}$ betragen um das gewünschte Empfangssignal möglichst ungehindert passieren zu lassen.

[question:AJ113]
[question:AJ114]
[question:AJ108]

Grundsätzlich macht es Sinn hinter einem starken Kurzwellensender ein Tiefpassfilter mit einer Grenzfrequenz von $\qtyrange{30}{40}{\mega\hertz}$ zu installieren. Auch durch Verwendung eines Antennen-Tuners in Tiefpass-Konfiguration (Pi- oder LC-Filter) kann eine Tiefpasswirkung erreicht werden, die Oberwellenaussendungen wirksam unterdrückt.

[question:AJ112]
[question:AJ104]

Starke Sendesignale einer Amateurfunkstation können bei DAB, TV und UKW-Empfängern Empfangsstörungen, Störgeräusche oder Aussetzer/Artefakte/Verstummen  (insbesondere bei digitalen Empfängern wie DAB/DVB-T) hervorrufen. Diese Störungen werden oft durch Übersteuerung des Empfängereingangs durch hohe Signalstärken am Empfangsort hervorgerufen und führen zur Verringerung der Empfindlichkeit des Empfängers oder Übersteuerung der Eingangsstufe des Empfängers.

[question:AJ110]
[question:AJ111]
[question:AJ109]

Um die vorgenannten Probleme zu vermeiden sollte seitens des Funkamateurs daher immer nur mit der minimal erforderlichen Sendeleistung für eine zufriedenstellende Kommunikation gearbeitet werden.

[question:AJ101]

Zum Abblocken von HF-Störungen in Schaltungen und Geräten werden oft Abblockkondensatoren verwendet. Diese müssen die Eigenschaft haben die HF möglichst effizient gegen Masse abzuleiten. Hierfür eignen sich insbesondere Keramik-Kondensatoren sehr gut. Ungeeignet sind Elektrolyt- und Kunststoff-Folienkondensatoren, da diese durch ihren gewickelten Aufbau eine hohe Eigeninduktivität besitzen. Bei Tantal-Kondensatoren wird oft aufgrund der besseren HF-Ableitungseigenschaften ein Keramik-Kondensator parallel geschaltet, da diese alleinig nur für mittlere HF-Frequenzen bis ca. $\qty{30}{\mega\hertz}$ geeignet sind und Keramik-Kondensatoren weitaus höhere Frequenzen abblocken können.
Um HF-Störungen wirksam abzuleiten muss eine wirksame Erdung mit niedriger Impedanz vorliegen.

[question:AJ119]
[question:AJ102]

In Stromversorgungsleitungen von HF-Stufen werden oft Hochfrequenz-Drosseln eingesetzt. Diese stellen eine Längsimpedanz für Hochfrequenz dar und blocken wirksam hochfrequente Einströmungen in Stufen sowie auch HF-Rückströmungen in die Stromversorgung der Stufen ab.
Bedingt durch den gewickelten Aufbau haben diese Drosseln auch Eigenkapazitäten, so dass sie in Verbindung mit Ihrer Induktivität unerwünschte Resonanzstellen (Schwingkreise) bilden. Hierdurch kann es in den HF-Stufen zu unerwünschten *Nebenresonanzen*, welche durch die *Eigenresonanzen* der HF-Drosseln hervorgerufen werden, kommen. Nebenresonanzen können die Charakteristik von HF-Stufen negativ beeinflussen. Hierdurch kann es zu unerwünschten Rückkopplungseffekten, insbesondere bei Verstärkern, kommen sowie zu Einbrüchen in der Leistungscharakteristik von HF-Stufen.

[question:AJ214]