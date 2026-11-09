%ARK: Grundhelvetisierung durchgeführt, Fragen abgeglichen, alte Fragen gelöscht, neue Fragen eingefügt 

<left>
[picture:648:n_relaisfunkstellen_aufbau:Schematische Darstellung einer Relaisfunkstelle mit Nutzern]
</left>
<right>
* Ermöglicht eine größere Reichweite als bei direkter Verbindung
* Meist an exponierten Standorten, z.B. Berggipfeln, Hochhäusern, (Kirch-)Türmen
* Oder in Satelliten
</right>

<note>
* Durch den Berg lässt sich nicht durchfunken
* Mit dem Relais können beide Funkamateure eine Verbindung aufbauen
* Mehr zu Satelliten später
</note>

---

## Definition Relais
eine fernbediente Amateurfunkstation (auch in Satelliten), die empfangene Amateurfunkaussendungen, Teile davon oder sonstige eingespeiste oder eingespeicherte Signale fernausgelöst aussendet und dabei zur Erhöhung der Erreichbarkeit von Amateurfunkstationen dient

---
<left>
* Auch kurz genannt: Relais oder Repeater
* Senden regelmäßig ihr Rufzeichen aus
</left>
<fragment>
<right>
* Relais werden nicht mit persönlichen Rufzeichen betrieben.
* Relais sind üblicherweise nicht ständig besetzt.
* Relais müssen nicht zwingend an geografisch exponierten Standorten betrieben werden.
* Geografisch exponierte Standorte erhöhen die Reichweite beträchtlich
</right>
</fragment>

---
[question:VN007]
---

## Funktionsweise
<left>
* Empfängt auf der Eingangsfrequenz das Signal einer Amateurfunkstation
* Strahlt es zeitgleich auf der Ausgabefrequenz aus
* Damit der Sender nicht stört, sind die Frequenzen unterschiedlich
</left>
<right>
<fragment>
Den Abstand nennt man *Frequenzablage* oder kurz *Ablage*

| r: Band | r: Ablage |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Frequenzablage]
</fragment>
</right>

---
Beispiel eines $\qty{70}{\centi\meter}$-Relais:
* Eingabefrequenz: $\qty{431,275}{\mega\hertz}$
* Ablage: $\qty{+7,600}{\mega\hertz}$
* Ausgabefrequenz: $\qty{438,875}{\mega\hertz}$

---
[question:BE401]
---
[question:BE402]
---
[question:BE403]

---

## Crossband-Betrieb
* Sendet und empfängt gleichzeitig auf zwei verschiedenen Bändern, z.B. $\qty{10}{\meter}$ und $\qty{70}{\centi\meter}$
* Umsetzung der Sendeart auch möglich, z.B. SSB auf FM

---

## Digipeater
* Vermittelt Daten statt Sprache
* Empfängt und sendet Datenpakete
* Aussendung kann nur in Teilen oder zeitversetzt geschehen
* Datenpakete können wiederholt werden
* Einzelne Datenfelder können geändert werden

<note>
* Für Packet Radio, was in den 90ern vor dem Internet beliebt war
* Kommt später etwas ausführlicher
</note>

---
[question:NF118]
---

## Besondere Einstellungen
* Ggf. sind weitere Einstellungen ( z. Bsp. Subton mit CTCSS) für die Verbindung zum Relais notwendig
* Diese Informationen sind in Repeaterverzeichnissen, auf Webseiten oder beim Relaisverantwortlichen erhältlich
* Neben FM-Repeatern gibt es welche für digitale Sprache wie DMR oder D-Star

<note>
Ein Beispiel für weitere Einstellungen ist ein Subton mit CTCSS
</note>

---
[question:NE309]
---
[question:NE308]
---

## Kanalbandbreite
* Der benötigte Platz im Frequenzspektrum
* Wide-FM: $\qty{25}{\kilo\hertz}$
* Narrow-FM: $\qty{12,5}{\kilo\hertz}$
* Repeater mögen Narrow-FM, da sonst Signale verzerrt sind und benachbarte Frequenzen gestört werden

---
[question:BE407]
---

## Störungsfreier Betrieb
* Grundsätzlich können alle Funkamateure mit ihrem zugeteilten Rufzeichen Relais nutzen
%* Betreiber kann zur Sicherstellung des störungsfreien Betriebs Funkamateure ausschließen
%* Das BAKOM ist hiervon zu unterrichten

---
[question:BE417]
---

## Funkbetrieb auf Repeatern
* Kurze Durchgänge
* keine CQ-Rufe, nur das eigene Rufzeichen nennen
* beim Auftasten zum Testen immer das eigene Rufzeichen nennen
* Mobile und portable Stationen sind oft nur kurzzeitig in Empfangsreichweite
* Pause zwischen den Durchgängen zum Reinmelden anderer Stationen

---
[question:BE406]
---
[question:BE404]
---

## Doppeln
* Bei gleichzeitiger Spracheingabe wird die Aussendung bis zur Unlesbarkeit gestört
* "Doppeln" durch ordentliche Übergabe vermeiden
* Aussendung erst dann beginnen, wenn die vorige Station beendet hat

---
[question:NE310]
---
[question:BE405]

%## Sendeleistung
%* Nach Anlage 1 der AFuV
%* Für automatische Station oberhalb von $\qty{30}{\mega\hertz}$ mit $\qty{50}{\watt}$ ERP

---
[question:BE408]
---

## Rapport
* Empfangene Signalstärke (S) ist die des Relais
* Es wird darauf verzichtet
* Nur die Lesbarkeit (R) wird im Rapport beurteilt
* Es ist nicht üblich, QSOs über Relais mit einer QSL zu bestätigen
