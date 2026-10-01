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
# Rauschzahl

Die Rauschzahl beschreibt, wie stark ein elektronisches Bauteil oder eine Verstärkerstufe das Signal-Rausch-Verhältnis eines Signals verschlechtert.

## Anschaulich erklärt

Ein Verstärker soll ein schwaches Signal verstärken. Dabei entsteht im Verstärker selbst jedoch zusätzliches Rauschen.

Man vergleicht deshalb:

- das Signal-Rausch-Verhältnis am Eingang und
- das Signal-Rausch-Verhältnis am Ausgang.

Die Rauschzahl $F$ ist definiert als

$$
F = \frac{(S/N)_\mathrm{Eingang}}{(S/N)_\mathrm{Ausgang}}
$$

Dabei gilt:

- $S$ = Signalleistung
- $N$ = Rauschleistung
- $F$ = Rauschzahl als dimensionslose Grösse

Da ein realer Verstärker zusätzliches Rauschen erzeugt, ist

$$
F \geq 1 .
$$

Ein ideal rauschfreier Verstärker hätte also $F = 1$.

## Rauschzahl in Dezibel

Die Rauschzahl wird sehr häufig logarithmisch in Dezibel angegeben:

$$
NF = 10 \cdot \log_{10}(F)\;\mathrm{dB}
$$

Nach DIN wird der logarithmisch in Dezibel (dB) angegebene Wert der Rauschzahl als *Rauschmass* bezeichnet. Der Begriff ist jedoch nicht eindeutig, da „Rauschmass“ in der Fachliteratur auch für eine andere rauschbezogene Grösse verwendet wird. Um Verwechslungen zu vermeiden, wird deshalb häufig weiterhin der Begriff „Rauschzahl in dB“ verwendet.

### Beispiel

Für $F = 2$ ergibt sich

$$
NF = 10 \cdot \log_{10}(2) \approx 3{,}01\;\mathrm{dB} .
$$

Das bedeutet: Das Signal-Rausch-Verhältnis wird durch das Bauteil um den Faktor 2 verschlechtert.

## Begriffe sauber unterscheiden

| Begriff | Bedeutung | Einheit |
|---|---|---|
| Rauschzahl $F$ | Verhältnis der Signal-Rausch-Verhältnisse von Eingang und Ausgang | dimensionslos |
| Rauschzahl in dB (nach DIN: Rauschmass) | Logarithmische Darstellung der Rauschzahl | $\mathrm{dB}$ |
</indepth>
