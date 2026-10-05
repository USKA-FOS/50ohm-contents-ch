Das Signal-to-Noise Ratio (SNR) ist definiert als das Verhältnis von Nutzsignal zu Rauschsignal (Noise), wie in Abbildung [ref:a_snr] dargestellt. Je höher das SNR eines empfangenen Signals ist, desto mehr hebt sich das Nutzsignal vom Rauschen bei gegebener Bandbreite ab.

<margin>
[picture:1097:a_snr:Signal-to-Noise Ratio (SNR)]
</margin>

[question:AF227]

Die Rauschzahl wird häufig bei HF-Vorverstärkern angegeben. Diese beschreibt die Verschlechterung des SNR bei Durchgang eines Signals durch diese Baugruppe. Hierbei wird die Rauschzahl als Verhältnis des eingehenden SNR-Wertes zum ausgehenden SNR-Wert bestimmt. Die Rauschzahl wird üblicherweise mittels Logarithmierung in Dezibel ($\unit{\dB}$) dargestellt. Eine Rauschzahl von $\num{2}$ in linearer Notation entspricht in logarithmischer Darstellung $\qty{3}{\dB}$.

[question:AF228]
[question:AF229]

<indepth>
Laut DIN wird die in $\unit{\decibel}$ dargestellte Rauschzahl als Rauschmaß bezeichnet. Leider gibt es noch eine anderslautende Definition des Rauschmaßes, sodass diese Bezeichnung nicht sehr verbreitet ist.
</indepth>

<indepth>
Die *Rauschzahl* beschreibt, wie stark ein elektronisches Bauteil oder eine Verstärkerstufe das Signal-Rausch-Verhältnis eines Signals verschlechtert.

Ein Verstärker soll ein schwaches Signal verstärken. Dabei entsteht im Verstärker selbst jedoch zusätzliches Rauschen.

Man vergleicht deshalb

- das Signal-Rausch-Verhältnis am Eingang mit dem

- Signal-Rausch-Verhältnis am Ausgang.

Die Rauschzahl $F$ ist definiert als

$F = \frac{(S/N)_\mathrm{Eingang}}{(S/N)_\mathrm{Ausgang}}$

Dabei gilt:

- $S$ = Signalleistung
- $N$ = Rauschleistung
- $F$ = Rauschzahl als dimensionslose Grösse

*Rauschzahl in Dezibel*

Die Rauschzahl (noise figure, NF) wird sehr häufig logarithmisch in Dezibel angegeben:

$NF = 10 \cdot \log_{10}(F)\;\mathrm{dB}$
</indepth>
