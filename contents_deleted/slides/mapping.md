## Mapping in der digitalen Signalverarbeitung

* Wandelt digitale Daten in spezifische Signalpunkte (Symbole) um  
* Entscheidend für Modulationstechniken wie QAM und QPSK  
* Ermöglicht die Übertragung der Daten über das Kommunikationssystem

---

## Schritt 1: Binäre Daten in Symbole umwandeln

* Bei QPSK werden jeweils zwei Bits zu einem Symbol zusammengefasst  
* Es ergeben sich 4 mögliche Kombinationen: $\num{00}$, $\num{01}$, $\num{10}$, $\num{11}$
* Jede Kombination wird einem bestimmten Signalpunkt zugeordnet

---

## Schritt 2: Phasenvergabe

* Jedem Symbol wird eine eigene Phase zugewiesen  
* Typische Phasen in $\qty{90}{\degree}$-Schritten:
* $\num{00}$ entspricht $\qty{0}{\degree}$
* $\num{01}$ entspricht $\qty{90}{\degree}$
* $\num{10}$ entspricht $\qty{180}{\degree}$
* $\num{11}$ entspricht $\qty{270}{\degree}$

--- style="font-size: smaller;"
## Schritt 3: Mapping auf das Konstellationsdiagramm

<left>
[picture:697:a_8qam:I-Q-Diagramm für ein 8QAM-Mapping]
Die Darstellung ist für ein 8QAM-Mapping. QPSK im Beispiel entspricht dem äußeren Kreis.
</left>
<right>
* Das Konstellationsdiagramm stellt die Signalpunkte in einem quadratischen Diagramm dar  
* Die X-Achse (*I*n-Phase) und die Y-Achse (*Q*uadratur) zeigen die Amplituden der Signalbestandteile  
* Für QPSK liegen die vier Signalpunkte an den Enden eines Quadrats
</right>

---

## Darstellung der QPSK-Symbole

* $\num{00}$ bei $\qty{0}{\degree}$: Punkt auf der positiven X-Achse  
* $\num{01}$ bei $\qty{90}{\degree}$: Punkt auf der positiven Y-Achse  
* $\num{10}$ bei $\qty{180}{\degree}$: Punkt auf der negativen X-Achse  
* $\num{11}$ bei $\qty{270}{\degree}$: Punkt auf der negativen Y-Achse

* Die klare Trennung der Phasen erleichtert das Auseinanderhalten der Symbole – auch bei Rauschen
