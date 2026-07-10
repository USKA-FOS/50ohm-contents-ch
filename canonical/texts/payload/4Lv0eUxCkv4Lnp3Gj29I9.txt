Ein Netzgerät wandelt die Wechselspannung von $\qty{230}{\volt}$ aus der Steckdose in eine kleinere Gleichspannung um. Im Amateurfunk verwenden wir häufig Netzgeräte, die an ihrem Ausgang eine Gleichspannung von $\qty{13,8}{\volt}$ bereitstellen, um damit beispielsweise einen Transceiver zu betreiben.

<margin>
[picture:740:n_netzgeraet:Netzgerät]
</margin>

<indepth>
Zur *Kontrolle des Betriebszustands* eines Netzgeräts gibt es beleuchtete Schalter, Kontroll-Leuchtdioden oder beleuchtete Anzeigeinstrumente. Die Anzeigeinstrumente können getrennt die Betriebsspannung in Volt und die aktuell fließenden Stromstärke in Ampere anzeigen. Es gibt auch umschaltbare Digitalanzeigen für diesen Zweck.
</indepth>

[question:ND101]
[question:ND102]

---

Ein Netzgerät wird oft mittels *Schutzkontaktstecker* (kurz Schukostecker) an der Steckdose angeschlossen. Beim Schutzkontaktstecker spielt die Einsteckrichtung keine Rolle, da sich die Polarität bei Wechselspannung ständig ändert. Stecker und Steckdose haben jeweils 3 Pole, wie in Abbildung [ref:n_schutzkontakt] zu erkennen ist. Die Stifte des Steckers passen in die Öffnungen der Steckdose und erlauben die Verbindung zu den sogenannten L- und N-Leitern, zwischen denen die gefährliche Wechselspannung von $\qty{230}{\volt}$ anliegt.

<margin>
[photo:86:n_schutzkontakt:Schutzkontakt an einer Steckdose und Schukostecker]
</margin>

Den äußeren Schleifkontakt des Schukosteckers nennt man *Schutzkontakt* (in der Abbildung [ref:n_schutzkontakt] rot markiert). Der Schutzkontakt verbindet sich beim Einstecken mit dem sogenannten *PE-Leiter* der Steckdose. "PE" ist die Abkürzung für den englischen Begriff "protective earth", der soviel wie Schutzerdung bedeutet. Beim Einstecken des Steckers wird das metallische Gehäuse des Netzgeräts also geerdet. Eine gefährliche Spannung auf dem Gehäuse wird dadurch ausgeschlossen.

[question:ND109]

---

Der Ausgang des Netzteils und die Verbindungsleitung zum Transceiver sind zweipolig ausgelegt, damit sich ein geschlossener Stromkreis ergeben kann. Das ist die Voraussetzung dafür, dass der Strom vom Netzgerät zum Transceiver, durch diesen hindurch und wieder zurück zum Netzgerät fließen kann. 

<webmargin>
[picture:680:n_Netzgeraet_TRX:Anschluss von Netzgerät und TRX]
</webmargin>

Die Ausgangsklemmen für die Gleichspannung sind farbig ausgeführt: Rot steht für Plus und schwarz für Minus. Beim Anschluss der Verbindungsleitung zum Transceiver ist diese Polung unbedingt zu beachten. Ansonsten kann es zum Kurzschluss oder im Extremfall sogar zur Zerstörung des Transceivers kommen. Erst wenn alle Leitungen angeschlossen sind und die Polung kontrolliert wurde, sollte das Netzgerät eingeschaltet werden. 

[question:ND104]
[question:ND103]
[question:ND105]
[question:ND106]
[question:ND107]

---

Im Netzgerät und in der Verbindungsleitung zum Transceiver gibt es sogenannte Feinsicherungen. Diese können einen Fehlerfall (Kurzschluss oder Überlastung) erkennen und den Stromfluss unterbrechen. Häufig handelt es sich dabei um Schmelzsicherungen, in denen ein dünner Draht schmilzt, wenn zuviel Strom fließt. Dann ist der Stromkreis nicht mehr geschlossen und es kann kein Strom mehr fließen. Man spricht dann von einer *durchgebrannten Sicherung* oder in der Fachsprache auch von einer *thermischen Abschaltung*.

<margin>
[photo:88:n_feinsicherungen:Feinsicherungen]
</margin>

<indepth>
*Vertiefung:* Feinsicherungen sind $\qty{5}{\milli\meter} \times \qty{20}{\milli\meter}$ groß und in unterschiedlichen Ausführungen erhältlich. Sie unterscheiden sich nach Stromstärken und Auslösecharakteristiken. Träge Sicherungen werden immer dann eingesetzt, wenn der Einschaltstrom deutlich höher als der Nennstrom ist, z. B. in Netzgeräten. Die Auslösezeit der Sicherung hängt von der Stromstärke und der Dauer des Stromflusses ab. In Tabelle [ref:n_feinsicherung] sind übliche Werte für die Auslösezeit zusammengestellt. Genauere Angaben geben die Hersteller über Kennlinien in ihren Datenblättern an.
</indepth>

Nachdem eine Schmelzsicherung ausgelöst hat und man die Ursache erkannt und behoben hat, muss man sie austauschen. Defekte Sicherungen dürfen aber nur durch gleichartige ersetzt werden! Dabei ist sowohl auf Stromstärke als auch die sogenannte Auslösecharakteristik zu achten, die angibt, wie schnell eine Sicherung auslöst (flink, mittelträge, träge).

<webmargin>
| l: Auslösecharakteristik | l: Kennzeichen | X: Abschaltzeit |
| flink | F | max. $\qty{30}{\milli\second}$ |
| mittelträge | MT | max. $\qty{90}{\milli\second}$ |
| träge | T | max. $\qty{300}{\milli\second}$ |
[table:n_feinsicherung:Kenngrößen von Feinsicherungen, Abschaltzeit bei zehnfachem Nennstrom]
</webmargin>

<danger>
*ACHTUNG:* Die manchmal praktizierte Überbrückung einer defekten Sicherung, z. B. mit Alufolie, ist unzulässig und sehr gefährlich. Es besteht die Gefahr von Bränden!
</danger>

Hochwertige Netzgeräte besitzen oft auch eine elektronische Begrenzung von Strömen. Im Kurzschlussfall sorgt diese dafür, dass die Stromstärke begrenzt wird. Dies nennt sich *Kurzschlussstrombegrenzung*. Nachdem der Fehler beseitigt ist, muss keine Sicherung ausgetauscht werden.

[question:ND108]
[question:NK305]
