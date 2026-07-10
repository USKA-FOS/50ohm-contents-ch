In der drahtlosen Kommunikation spielen verschiedene Zugriffsverfahren eine zentrale Rolle, um mehreren Nutzern gleichzeitig die Nutzung eines gemeinsamen Frequenzspektrums zu ermöglichen. Die gängigen Verfahren sind Frequenzmultiplex (FDMA), Zeitmultiplex (TDMA) und Codemultiplex (CDMA). Jedes dieser Verfahren teilt das Frequenzspektrum auf unterschiedliche Weise auf, um Interferenzen zu minimieren und eine effiziente Übertragung zu gewährleisten. Die Wahl des Verfahrens hängt dabei von den spezifischen Anforderungen an Bandbreite, Nutzerzahl und Störanfälligkeit ab. Im Folgenden werden die Unterschiede dieser Verfahren beschrieben.

---

Beim Frequenzmultiplexverfahren (FDMA – Frequency Division Multiple Access) wird das zur Verfügung stehende Frequenzband in mehrere voneinander getrennte Frequenzkanäle aufgeteilt (vgl. Abbildung [ref:e_fdma]). Jeder dieser Kanäle wird einem einzelnen Nutzer fest zugewiesen, sodass die gleichzeitige Nutzung des Systems durch mehrere Teilnehmer möglich ist. Die Trennung der Nutzer erfolgt ausschließlich über unterschiedliche Frequenzen, wodurch sich die Signale der einzelnen Teilnehmer nicht gegenseitig stören, solange die Kanalabstände eingehalten werden. FDMA ist ein technisch einfaches und seit vielen Jahren etabliertes Verfahren, das sich besonders für Systeme mit wenigen Nutzern und geringem Interferenzbedarf eignet. Ein Nachteil besteht jedoch in der vergleichsweise schlechten Bandbreiteneffizienz bei einer großen Anzahl von Nutzern, da jedem Teilnehmer dauerhaft ein eigener Frequenzbereich reserviert bleibt, selbst wenn dieser zeitweise keine Daten überträgt. Typische Anwendungsbeispiele für FDMA sind frühe analoge Mobilfunksysteme wie AMPS (Advanced Mobile Phone Service) in den USA oder GSM (Global System for Mobile Communications) in Europa sowie verschiedene Formen der Satellitenkommunikation.

[question:EE410]

<margin>
[picture:845:e_fdma:Frequenzmultiplexing]
</margin>

---

Beim Zeitmultiplexverfahren (TDMA – Time Division Multiple Access) nutzen mehrere Teilnehmer denselben Frequenzkanal, indem ihnen der Zugriff zeitlich aufgeteilt wird. Jeder Nutzer erhält dabei fest definierte Zeitintervalle, sogenannte Zeitschlitze, in denen er senden und empfangen darf (vgl. Abbildung [ref:e_tdma]). Durch diese zeitliche Trennung der Übertragungen wird verhindert, dass sich die Signale der einzelnen Teilnehmer gegenseitig überlagern oder stören.

TDMA ermöglicht eine vergleichsweise effiziente Nutzung der verfügbaren Frequenzressourcen, insbesondere in Systemen mit vielen Nutzern und hohem Datenaufkommen. Voraussetzung für den reibungslosen Betrieb ist jedoch eine sehr genaue zeitliche Synchronisation aller Teilnehmer, was den technischen Aufwand und die Systemkomplexität erhöht. Bekannte Anwendungsbeispiele für TDMA sind das GSM-Mobilfunksystem der zweiten Generation sowie das schnurlose Telefonsystem DECT und im Amateurfunk DMR.

[question:EE409]

<margin>
[picture:844:e_tdma:Zeitmultiplexing]
</margin>

---

Beim Codemultiplexverfahren (CDMA – Code Division Multiple Access) nutzen alle Teilnehmer gleichzeitig denselben Frequenzbereich und dieselbe Zeit. Die Trennung der einzelnen Nutzer erfolgt nicht über Frequenz oder Zeit, sondern über individuelle Spreizcodes (vgl. Abbildung [ref:e_cdma]). Jedem Nutzer wird ein eigener Code zugewiesen, mit dem sein Signal moduliert wird. Diese Codes sind so gewählt, dass sich die überlagerten Signale am Empfänger wieder voneinander trennen lassen, obwohl sie gleichzeitig im selben Frequenzband übertragen werden. CDMA zeichnet sich durch eine hohe Flexibilität und eine große Systemkapazität aus, da viele Nutzer gleichzeitig aktiv sein können. Zudem ist das Verfahren sehr robust gegenüber Störungen und Mehrwegeausbreitung. Dem stehen jedoch eine vergleichsweise komplexe Signalverarbeitung und erhöhte Anforderungen an die Hardware gegenüber, insbesondere bei einer großen Anzahl aktiver Teilnehmer. Typische Anwendungsbeispiele für CDMA sind Mobilfunksysteme der dritten Generation wie UMTS sowie das satellitengestützte Navigationssystem GPS.

[question:EE411]

<margin>
[picture:846:e_cdma:Codemultiplexing]  
</margin>

Zusammenfassend lässt sich sagen, dass FDMA die einfachste Methode ist, während TDMA und CDMA zunehmend effizienter und komplexer werden, insbesondere bei der Nutzung beschränkter Bandbreiten und hohen Nutzerzahlen. CDMA ermöglicht die größte Flexibilität, erfordert jedoch auch die aufwändigste Technologie zur Umsetzung.
