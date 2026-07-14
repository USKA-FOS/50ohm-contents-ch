# Gegeben
Ausgangspegel: $p_\text{Ausgang} = \qty{20}{\dBW}$  

# Lösungsweg
Wir nutzen die $\unit{\dBW}$-Formel aus der Formelsammlung (Pegel, Leistungs- und Spannungspegel):  
$ p = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW}$ 
und lösen nach $P$ auf:
$P = \qty{1}{\watt}\cdot 10^{\frac{p}{\qty{10}{\dBW}}}$
Mit $p_\text{Ausgang}$ aus der Aufgabenstellung ergibt sich die Ausgangsleistung zu:
$P = \qty{1}{\watt}\cdot 10^{\frac{p_\text{Ausgang}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{\frac{\qty{20}{\dBW}}{\qty{10}{\dBW}}}= \qty{1}{\watt}\cdot 10^{2} = \qty{10^2}{\watt}$

# Abkürzung
Wer ein wenig mit Logarithmen und der Tabelle aus den Hilfsmittel gearbeitet hat, weiß, dass $\qty{20}{\dB} \rightarrow 100$ entspricht und somit $\qty{20}{\dBW} \rightarrow \qty{100}{\watt} = \qty{10^2}{\watt} $ entsprechen.
