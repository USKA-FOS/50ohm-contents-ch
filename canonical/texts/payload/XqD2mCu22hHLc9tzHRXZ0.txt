[picture:810:doppelsuper_blockschaltbild:Blockschaltbild eines Doppelsuper]

1. HF-Teil mit Vorselektion
2. Erster Mischer mit VFO
3. Erster ZF-Verstärker mit Roofing-Filter
4. Zweiter Mischer mit CO

--- data-transition="none"
[picture:810:doppelsuper_blockschaltbild:Blockschaltbild eines Doppelsuper]

5. Zweiter ZF-Verstärker mit Filter
6. Dritter Mischer als Produktdetektor oder Demodulator ggf. mit BFO
7. NF-Verstärker

--- data-transition="none"
[picture:810:doppelsuper_blockschaltbild:Blockschaltbild eines Doppelsuper]

* Verwendung von zwei Zwischenfrequenzen
* Hohe 1. ZF $\rightarrow$ gute Spiegelfrequenzunterdrückung
* Niedrige 2. ZF $\rightarrow$ hohe Trennschärfe

---
* Nach 1. ZF ist ein Eingangsfilter vor 2. Mischer
* Spiegelfrequenz lässt sich durch großen Abstand gut unterdrücken
* Nach 2. ZF Filter mit hoher Güte
* Lässt sich für niedrige Frequenzen gut realisieren
* ZF und gewünschte Empfangsfrequenz weit entfernt legen $\rightarrow$ Vermeidung des Direktempfangs der ZF
* Die 1. ZF sollte das Doppelte der maximalen Empfangsfrequenz sein

---
[question:AF112]
---
[question:AF113]
---
[question:AF114]
---
### Roofing Filter

* Nach 1. Mischer schmales Filter (*Roofing Filter*)
* Auf 1. ZF abgestimmt
* Bandbreite mindestens so groß wie größte benötigte Empfangsbandbreite

---
[question:AF116]
---
[question:AF209]
---
[question:AF117]
---
### Oszillator-Frequenzen
* Oszillatorfrequenzen sind jeweils ober- oder unterhalb der gewünschten Eingangsfrequenz
* Es existieren für jeden Mischer zwei Lösungsmöglichkeiten

<fragment>
1. $f_\text{OSZ} = f_\text{ZF}\,+\,f_\text{E}$
2. $f_\text{OSZ} = f_\text{ZF}\,-\,f_\text{E}$
</fragment>

---
[question:AF210]
--- style="font-size: smaller;"
#### Lösungsweg
* gegeben: $f_\text{E} = 3\dots\qty{30}{\mega\hertz}$
* gegeben: $f_\text{ZF1} = \qty{50}{\mega\hertz}$
* gesucht: $f_\text{OSZ}$

<fragment>
$f_\text{ZF} = |f_\text{E} − f_\text{OSZ}| \Rightarrow f_\text{OSZ} = f_\text{ZF} \pm f_\text{E}$
</fragment>
<fragment>
<left>
1. Lösung:
$\begin{split}f_\text{OSZ} &= f_\text{ZF} \, + \, f_\text{E}\\ &= \qty{50}{\mega\hertz} \, + \, 3\dots\qty{30}{\mega\hertz}\\ &= 53\dots\qty{80}{\mega\hertz}\end{split}$
</left>
</fragment>
<fragment>
<right>
2. Lösung:
$\begin{split}f_\text{OSZ} &= f_\text{ZF} \, - \, f_\text{E}\\ &= \qty{50}{\mega\hertz} \, - \, 3\dots\qty{30}{\mega\hertz}\\ &= 47\dots\qty{20}{\mega\hertz}\end{split}$
</right>
</fragment>
---
[question:AF120]
--- style="font-size: smaller;"
### Lösungsweg
<left>
* gegeben: $f_\text{E} = \qty{3,65}{\mega\hertz}$
* gegeben: $f_\text{ZF1} = \qty{50}{\mega\hertz}$
</left>
<right>
* gegeben: $f_\text{ZF2} = \qty{9}{\mega\hertz}$
* gegeben: $f_\text{NF} = \qty{455}{\kilo\hertz}$
</right>
* gesucht: $f_\text{OSZ}$ für $f_\text{VFO}$, $f_\text{CO1}$, $f_\text{CO2}$

<fragment>
$f_\text{ZF1} = \begin{cases}f_\text{E}\,+\,f_\text{OSZ}\\ f_\text{OSZ}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSZ}\end{cases} \Rightarrow f_\text{OSZ} = \begin{cases}f_\text{ZF}\,-\,f_\text{E}\\ f_\text{E}\,+\,f_\text{ZF}\\ f_\text{E}\,-\,f_\text{ZF}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = \begin{cases}f_\text{ZF1}\,-\,f_\text{E} = \qty{50}{\mega\hertz}\,-\,\qty{3,65}{\mega\hertz} = \qty{46,35}{\mega\hertz}\\ f_\text{E}\,+\,f_\text{ZF1} = \qty{3,65}{\mega\hertz}\,+\,\qty{50}{\mega\hertz} = \qty{53,64}{\mega\hertz}\\ f_\text{E}\,-\,f_\text{ZF1} = \qty{3,65}{\mega\hertz}\,-\,\qty{50}{\mega\hertz} = \cancel{\qty{-46,35}{\mega\hertz}}\end{cases}$
</fragment>
--- style="font-size: smaller;"‚
<fragment>
$f_\text{CO1} = \begin{cases}f_\text{ZF2}\,-\,f_\text{ZF1} = \qty{9}{\mega\hertz}\,-\,\qty{50}{\mega\hertz} = \cancel{\qty{-41}{\mega\hertz}}\\ f_\text{ZF1}\,+\,f_\text{ZF2} = \qty{50}{\mega\hertz}\,+\,\qty{9}{\mega\hertz} = \qty{59}{\mega\hertz}\\ f_\text{ZF1}\,-\,f_\text{ZF2} = \qty{50}{\mega\hertz}\,-\,\qty{9}{\mega\hertz} = \qty{41}{\mega\hertz}\end{cases}$
</fragment>
<fragment>
$f_\text{CO2} = \begin{cases}f_\text{NF}\,-\,f_\text{ZF2} = \qty{455}{\kilo\hertz}\,-\,\qty{9}{\mega\hertz} = \cancel{\qty{-8,545}{\mega\hertz}}\\ f_\text{ZF2}\,+\,f_\text{NF} = \qty{9}{\mega\hertz}\,+\,\qty{455}{\kilo\hertz} = \qty{9,455}{\mega\hertz}\\ f_\text{ZF2}\,-\,f_\text{NF} = \qty{9}{\mega\hertz}\,-\,\qty{455}{\kilo\hertz} = \qty{8,545}{\mega\hertz}\end{cases}$
</fragment>
<fragment>
VFO: $\bold{\qty{46,35}{\mega\hertz}} \And \qty{53,65}{\mega\hertz}$, CO1: $\bold{\qty{41}{\mega\hertz}} \And \qty{59}{\mega\hertz}$, CO2: $\qty{8,545}{\mega\hertz} \And \bold{\qty{9,455}{\mega\hertz}}$
</fragment>
---
[question:AF118]
--- style="font-size: smaller;"‚
#### Lösungsweg
<left>
* gegeben: $f_\text{E} = \qty{21,1}{\mega\hertz}$
* gegeben: $f_\text{ZF1} = \qty{9}{\mega\hertz}$
</left>
<right>
* gegeben: $f_\text{ZF2} = \qty{460}{\kilo\hertz}$
</right>
* gesucht: $f_\text{VFO} \gt f_\text{E}$, $f_\text{CO} \lt f_\text{ZF1}$

<fragment>
$f_\text{ZF} = \begin{cases}f_\text{OSZ}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSZ}\end{cases} \Rightarrow f_\text{OSZ} = \begin{cases}f_\text{E}\,+\,f_\text{ZF}\\ f_\text{E}\,-\,f_\text{ZF}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = f_\text{E}\,+\,f_\text{ZF1} = \qty{21,1}{\mega\hertz}\,+\,\qty{9}{\mega\hertz} = \qty{30,1}{\mega\hertz}$
</fragment>
<fragment>
$f_\text{CO} = f_\text{ZF1}\,-\,f_\text{ZF2} = \qty{9}{\mega\hertz}\,-\,\qty{460}{\kilo\hertz} = \qty{8,54}{\mega\hertz}$
</fragment>

---
[question:AF119]
--- style="font-size: smaller;"‚
#### Lösungsweg
<left>
* gegeben: $f_\text{E} = \qty{28}{\mega\hertz}$
* gegeben: $f_\text{ZF1} = \qty{10,7}{\mega\hertz}$
</left>
<right>
* gegeben: $f_\text{ZF2} = \qty{460}{\kilo\hertz}$
</right>
* gesucht: $f_\text{VFO} \gt f_\text{E}$, $f_\text{CO} \gt f_\text{ZF1}$

<fragment>
$f_\text{ZF} = \begin{cases}f_\text{OSZ}\,-\,f_\text{E}\\ f_\text{E}\,-\,f_\text{OSZ}\end{cases} \Rightarrow f_\text{OSZ} = \begin{cases}f_\text{E}\,+\,f_\text{ZF}\\ f_\text{E}\,-\,f_\text{ZF}\end{cases}$
</fragment>
<fragment>
$f_\text{VFO} = f_\text{E}\,+\,f_\text{ZF1} = \qty{28}{\mega\hertz}\,+\,\qty{10,7}{\mega\hertz} = \qty{38,70}{\mega\hertz}$
</fragment>
<fragment>
$f_\text{CO} = f_\text{ZF1}\,+\,f_\text{ZF2} = \qty{10,7}{\mega\hertz}\,+\,\qty{460}{\kilo\hertz} = \qty{11,16}{\mega\hertz}$
</fragment>
