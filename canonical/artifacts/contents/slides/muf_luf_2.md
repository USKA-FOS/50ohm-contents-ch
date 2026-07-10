## Höchste brauchbare Frequenz (MUF)

<left>
* Klasse E: Höchste Frequenz mit der eine Verbindung über die Raumwelle hergestellt werden kann
</left>
<right>
[picture:997:e_muf_luf2:Simulation der Sprungdistanzen für verschiedene Frequenzen und einer MUF bei ca. $\qty{7,5}{\mega\hertz}$ in einer Augustnacht 2024 bei einem Abstrahlwinkel von $\qty{45}{\degree}$]
</right>

---

## Höchste brauchbare Frequenz (MUF)

<left>
* Klasse A: Abhängig vom Abstrahlwinkel $\alpha$
</left>
<right>
[picture:870:e_muf_winkel:Die Winkel zur Berechnung der MUF]
</right>

---

## Höchste brauchbare Frequenz (MUF)

<left>
* Strahlt man steil ab (z. B. $\qty{60}{\degree}$), sinkt die MUF und die Funkwelle wird ggf. nicht mehr refraktiert.
* Strahlt man flach ab (z. B. $\qty{30}{\degree}$), so erhöht sich die MUF. 
</left>
<right>
[picture:998:e_muf_winkel2:Sprungdistanz bei 7 MHz im Sommer 2024]
</right>

---

[question:AH206]

---

[question:AH207]

---

## Kritische Frequenz

<left>
* Bei $\qty{90}{\degree}$ Abstrahlwinkel muss das Signal in der Ionosphäre eine $\qty{180}{\degree}$-Wendung vollziehen
* Kritische Frequenz $f_c$ bei der das Signal reflektiert wird
* MUF ist größer als $f_c$, da in der Regel nicht senkrecht nach oben gesendet wird
</left>
<right>
[picture:870:e_muf_winkel:Die Winkel zur Berechnung der MUF]
<fragment>
$\mathrm{MUF} \approx \frac{f_c}{\sin(\alpha)}$
</fragment>
</right>

<note>
Kritische Frequenz wird auch als $f_k$ oder $f_\mathrm{krit}$ angegeben
</note>

---

## Beispiel Ionosonde Juliusruh

[picture:999:e_muf_fof2:MUF 3000 (Flache Abstrahlung) und $f_\text{c}$ am 08.09.2025]

---

[question:AH208]

--- style="font-size: smaller;"
## Optimale Frequenz

* Kommerzielle Frequenzplanung verwendet eine *Frequency of optimal transmition*, optimale Sendefrequenz
* Frequenz, die auf einem bestimmten Signalweg statistisch an 90% aller Tage eine Funkverbindung erlaubt
* Liegt 15% unter dem monatlichen Mittel der MUF
* $f_{\mathrm{opt}} = \mathrm{MUF}\cdot 0,85$
* Spielt für Amateurfunk keine große Rolle, da keine dauerhafte Verbindung aufgebaut wird
* Im Amateurfunk wird bis nahe an der MUF gearbeitet

---
[question:AH209]
---
### Lösungsweg
<left>
* gegeben: $\alpha = \qty{45}{\degree}$
* gegeben: $f_c = 3MHz$
</left>
<right>
* gesucht: $\mathrm{MUF}$
* gesucht: $f_{\mathrm{opt}}$
</right>

<left>
<fragment>
$\begin{split} \text{MUF} & \approx \frac{f_c}{\sin(\alpha)}\\&\approx \frac{\qty{3}{\mega\hertz}}{\num{0,71}}\\&\approx \qty{4,2}{\mega\hertz}\end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split} f_{\mathrm{opt}} &= \mathrm{MUF}\cdot 0,85\\ &= \qty{4,2}{\mega\hertz} \cdot 0,85\\ &= \qty{3,6}{\mega\hertz} \end{split}$
</fragment>
</right>

---
## Niedrigste brauchbare Frequenz (LUF)

Niedrigste Frequenz mit der eine Verbindung über die Raumwelle hergestellt werden kann

---
[question:AH210]
---
[question:AH211]
---

## Kritische Frequenz

<left>
[picture:870:e_muf_winkel:Die Winkel zur Berechnung der MUF]
Wiederholung
</left>
<right>
* Bei $\qty{90}{\degree}$ Abstrahlwinkel muss das Signal in der Ionosphäre eine $\qty{180}{\degree}$-Wendung vollziehen
* Kritische Frequenz $f_c$ bei der das Signal reflektiert wird
* MUF liegt höher als $f_c$, da in der Regel nicht senkrecht nach oben gesendet wird
</right>

<note>
Kritische Frequenz wird auch als $f_k$ oder $f_\mathrm{krit}$ angegeben
</note>
---

* Kritische Frequenz ist je nach ionosphärische Region, dem Ort und der Zeit unterschiedlich
* Separate Angaben je nach Ionosphären-Region möglich
* Formelzeichen: fo
* Ergänzt durch die Schicht, z.B. foF2

<note>
fo mit kleinem "o" für ordinary wave
</note>
---
[question:AH204]
---
[question:AH205]