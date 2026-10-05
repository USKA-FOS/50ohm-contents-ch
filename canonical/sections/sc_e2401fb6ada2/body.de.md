Ein Netzgerät wandelt die Wechselspannung von $\qty{230}{\volt}$ aus der Steckdose in eine kleinere Gleichspannung um. Im Amateurfunk verwenden wir häufig Netzgeräte, die an ihrem Ausgang eine Gleichspannung von $\qty{13,8}{\volt}$ bereitstellen, um damit beispielsweise einen Transceiver zu betreiben.

<margin>
[picture:740:n_netzgeraet:Netzgerät]
</margin>

<indepth>
Zur *Kontrolle des Betriebszustands* eines Netzgeräts gibt es beleuchtete Schalter, Kontroll-Leuchtdioden oder beleuchtete Anzeigeinstrumente. Die Anzeigeinstrumente können getrennt die Betriebsspannung in Volt und die aktuell fließenden Stromstärke in Ampere anzeigen. Es gibt auch umschaltbare Digitalanzeigen für diesen Zweck.
</indepth>

[question:ND101]
[question:ND102]

<danger>
Zweipolige Stecker dürfen nur für doppelt schutzisolierte Geräte verwendet werden.
</danger>

---
Ein Netzgerät wird häufig mit einem **Stecker mit Schutzkontakt** an die Netzsteckdose angeschlossen. In der Schweiz werden dafür Stecksysteme nach
*SN 441011* verwendet. Bei einer dreipoligen Steckdose sind die drei Anschlüsse für den *Aussenleiter (L)*, den *Neutralleiter (N)* und den *Schutzleiter (PE)* vorgesehen, wie in Abbildung [NE-10.3.2](https://50ohm.uska.ch/50ohm_review_de/NE_netzgeraet_1.html#ref_n_schutzkontakt) zu erkennen ist. Zwischen dem Aussenleiter L und dem Neutralleiter N liegt die Netzspannung von 230 V Wechselspannung an.

Der Schutzkontakt des Steckers stellt beim Einstecken die Verbindung zum Schutzleiter PE der Steckdose her. „PE“ ist die Abkürzung für den englischen Begriff „protective earth“, also Schutzleiter bzw. Schutzerdung.

Ist das Netzgerät mit einem leitfähigen Gehäuse und einem Schutzleiteranschluss ausgeführt, wird das Gehäuse über den PE-Leiter mit dem Schutzleitersystem der elektrischen Installation verbunden. Dadurch kann bei einem Isolationsfehler ein Fehlerstrom über den Schutzleiter abfliessen und die Schutzeinrichtung, beispielsweise ein Leitungsschutzschalter oder ein Fehlerstrom-Schutzschalter (Fi), auslösen. Das Gehäuse bleibt dadurch im Normalfall nicht dauerhaft auf einer gefährlichen Spannung. Ein zweipoliger Anschluss, also ohne den Schutzleiter, ist nur dann zulässig, wenn das Gerät doppelt schutzisoliert ist.

---

<margin>
[photo:86:n_schutzkontakt:Schweizer Stecker mit und ohne Schutzleiter]
</margin>

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
