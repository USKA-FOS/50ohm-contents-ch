Im Rahmen der digitalen Signalverarbeitung beschreibt das *Mapping* den Schritt, bei dem digitale Daten in spezifische Signalpunkte (Symbole) umgewandelt werden, die über das Übertragungssystem gesendet werden können. Dies ist ein entscheidender Prozess in der Modulation, insbesondere bei Quadraturamplitudenmodulationen (QAM) und Phasenumtastungen wie QPSK (Quadrature Phase Shift Keying).

Um die Symbole zu visualisieren, verwenden wir ein *Konstellationsdiagramm* wie in Abbildung [ref:a_konstellation], das die möglichen Signalpunkte in einem zweidimensionalen Raum darstellt. Man bezeichnet die Achsen oft als In-Phase (I) und Quadrature (Q). Jeder Punkt im Diagramm repräsentiert eine bestimmte Amplitude und Phase, die durch das Mapping einer bestimmten Bitkombination zugeordnet ist, wie in Abbildung [ref:a_qpsk] dargestellt.

<margin>
[picture:1060:a_konstellation:Konstellationsdiagramm]
</margin>

---

Schauen wir uns im ersten Schritt QPSK in Abbildung [ref:a_qpsk] an: Bei QPSK werden jeweils zwei Bits zu einem Symbol zusammengefasst. Da wir zwei Bits pro Symbol haben, ergeben sich vier mögliche Kombinationen ($\num{00}$, $\num{01}$, $\num{10}$, $\num{11}$). Jede dieser Kombinationen wird einem spezifischen Signalpunkt zugeordnet, der durch eine bestimmte Phase repräsentiert wird.

<margin>
[picture:1059:a_qpsk:I-Q-Diagramm für ein QPSK-Mapping]
</margin>

---

Bei QPSK hat jedes Symbol eine eigene Phase. Die Phasen werden typischerweise in $\qty{90}{\degree}$-Schritten definiert und auf die vier möglichen Bitkombinationen gemapped, zum Beispiel:

- $\num{11}$ entspricht $\qty{45}{\degree}$
- $\num{01}$ entspricht $\qty{135}{\degree}$
- $\num{00}$ entspricht $\qty{225}{\degree}$
- $\num{10}$ entspricht $\qty{315}{\degree}$

Die Amplitude der Signale bleibt dabei konstant, und die Information wird ausschließlich durch die Phasenlage übertragen. Deshalb liegen die vier Punkte im Konstellationsdiagramm für QPSK auf einem Kreis. 

<indepth>
Genau genommen gibt es aber auch noch andere Möglichkeiten, die Phasen den Bitkombinationen zuzuordnen, solange sie eindeutig sind. Das hier gezeigte Mapping ist nur ein Beispiel. In dem hier gezeigten Beispiel wurden die Zuordnungen so gewählt, dass sich zwischen benachbarten Symbolen nur wenige Bits ändern. Das hat den Vorteil, dass unter Rauscheinfluss nur wenige Bitfehler entstehen. Dafür wird der Gray-Code verwendet, der in den meisten digitalen Übertragungsverfahren Anwendung findet.
</indepth>

---

Jeder dieser Punkte repräsentiert ein Symbol. Der Empfänger kann anhand der Phasenlage bestimmen, welche Bitkombination gesendet wurde. Das Konstellationsdiagramm bei QPSK zeigt vier Signalpunkte im rechten Winkel zueinander, die den vier verwendeten Phasen entsprechen. Die große Trennung zwischen den einzelnen Phasen ermöglicht eine zuverlässige Decodierung auch unter rauschbehafteten Bedingungen.

Ändert man neben der Phase auch die Amplitude, so spricht man von einer Quadraturamplitudenmodulation (QAM). Bei QAM werden sowohl die Amplitude als auch die Phase variiert, um mehr Bits pro Symbol zu übertragen. Zum Beispiel kann bei 16-QAM jedes Symbol vier Bits repräsentieren, was zu 16 möglichen Signalpunkten im Konstellationsdiagramm führt. Ein Beispiel für ein 16-QAM-Mapping ist in Abbildung [ref:a_qam] dargestellt.

<margin>
[picture:1061:a_qam:I-Q-Diagramm für ein 16-QAM-Mapping]
</margin>