# Gegeben
Verstärkung: $g_\text{Verstärkung} = \qty{10}{\dezibel}$  
Eingangsleitung: $P = \qty{1}{\watt}$ (Die Ausgangsleistung des Senders ist Eingangsleistung der Endstufe.)

# Lösungsweg
Wir berechnen den Eingangspegel mit der $\unit{\dBW}$-Formel aus der Formelsammlung (Pegel, Leistungs- und Spannungspegel):  
$ p_\text{Eingang} = 10 \cdot \log_{10}\left(\frac{P}{\qty{1}{\watt}}\right)\unit{\dBW} = \qty{0}{\dBW}$  
Der Ausgangspegel ergibt sich dann durch einfach Addition zu:
$ p_\text{Ausgang} = p_\text{Eingang} + g_\text{Verstärkung} = \qty{0}{\dBW} + \qty{10}{\dB} = \qty{10}{\dBW}$

# Abkürzung
Noch schneller kann die Aufgabe gelöst werden, wenn man weiß, dass $\log\left(1\right) = 0$ ist und somit $\qty{1}{\watt} \rightarrow \qty{0}{\dBW}$ entspricht. Damit entspricht der Ausgangspegel genau der Verstärkung von $\qty{10}{\dBW}$.