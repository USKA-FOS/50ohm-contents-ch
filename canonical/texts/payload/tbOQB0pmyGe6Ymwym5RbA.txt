<left>
[picture:965:a_brueckenlgeichrichter:Brückengleichrichter]
</left>
<right>
* Erweiterte und häufige Gleichrichterschaltung
* Beide Halbwellen werden verwendet
* Pulsierende Gleichspannung am Ausgang mit doppelter Frequenz wie Eingangsspannung
</right>
--- style="font-size: smaller;"
[include:applet_gleichrichter_2]

---
[question:AD305]
---
### Siebung
<left>
[picture:66:a_netzteil_Ucs:Gleichrichterschaltung mit Siebung]
</left>
<right>
* Mit Ladekondensator $C_L$ und LC-Siebglied mit $C_S$
* Kleinere Amplituden der pulsierenden Gleichspannung
* Kondensatoren laden sich auf die sekundäre Spitzenspannung auf
</right>
<note>
</note>
---
[question:AD306]
---
#### Lösungsweg
* gegeben: $U_P = \qty{230}{\volt}$
* gegeben: $ü = 8:1$
* gegeben: $U_D = \qty{0,6}{\volt}$
* gesucht: $\hat{U}$

<fragment>
$ü = \frac{U_P}{U_S} \Rightarrow U_S = \frac{U_P}{ü} = \frac{\qty{230}{\volt}}{8} = \qty{28,75}{\volt}$
</fragment>
<fragment>
Im Leerlauf kann die Diodenspannung vernachlässigt werden.
$\hat{U} = U_S \cdot \sqrt{2} = \qty{28,75}{\volt} \cdot 1,41 \approx \qty{40}{\volt}$
</fragment>
