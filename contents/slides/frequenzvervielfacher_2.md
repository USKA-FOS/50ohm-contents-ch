<left>
[picture:489:a_frequenzvervielfacher_schaltung:Beispiel für eine Schaltung eines Frequenzvervielfachers mit Klasse-C-Verstärker ohne Basis-Vorspannung]
</left>
<right>
* Eingangssignal wird einer nichtlinearen Verzerrerstufe zugeführt
* Z.B. Klasse-C-Verstärker, durch Betrieb ohne Basis-Vorspannung
* Signal wird stark verzerrt
* Mit Filter wird die gewünschte Oberschwingung selektiert
</right>
<note>
Verstärkerschaltungen kommen später im Kapitel.
</note>
---
<left>
[picture:489:a_frequenzvervielfacher_schaltung:Beispiel für eine Schaltung eines Frequenzvervielfachers mit Klasse-C-Verstärker ohne Basis-Vorspannung]
</left>
<right>
* Nur ganzzahlige Vielfache möglich
* In der Regel wird die 2. oder 3. Harmonische verwendet
* Höhere Frequenzvervielfachung mit hintereinander geschalteten Stufen
</right>
<note>
</note>
---
[question:AF312]
---
[question:AF311]
---
### Schirmung

* Es werden Zwischenfrequenzen erzeugt
* Diese führen oft zu Störungen
* Alle Stufen müssen gut abgeschirmt sein

---
[question:AF313]
---
### Mehrere Vervielfacher-Stufen

* Die einzelnen Frequenzen zwischen den Vervielfacher-Stufen können zu Störungen führen
* Weg durch die einzelnen Stufen verfolgen und die einzelnen Frequenzen berechnen
* Die Reihenfolge der Stufen ist wichtig zur Ermittlung der Störfrequenzen

---
[question:AF314]
---
#### Lösungsweg
* gegeben: $f_\text{Sender} = \qty{432}{\mega\hertz}$
* gegeben: $f_\text{Grund} = \qty{12}{\mega\hertz}$
* gegeben: $f_\text{QRM} = \qty{144}{\mega\hertz}$
* gesucht: Vervielfachungskombination

<fragment>
$n = \frac{f_\text{Sender}}{f_\text{QRM}} = \frac{\qty{432}{\mega\hertz}}{\qty{144}{\mega\hertz}} = 3$
</fragment>
<fragment>
Es ist nur die Kombination aus $\textrm{Grundfrequenz}\,\cdot 2\cdot 2\cdot 3\cdot 3$ möglich, da diese als letzte eine Verdreifachung der Frequenz vornimmt.
</fragment>
---
Gegenprobe:
$\begin{split}f_\text{Sender} &= f_\text{Grund}\cdot 2\cdot 2\cdot 3\cdot 3\\ &= \qty{12}{\mega\hertz}\cdot 2\cdot 2\cdot 3\cdot 3\\ &= \qty{24}{\mega\hertz}\cdot 2\cdot 3\cdot 3\\ &= \qty{48}{\mega\hertz}\cdot 3\cdot 3\\ &= \bold{\qty{144}{\mega\hertz}}\cdot 3\\ &= \qty{432}{\mega\hertz}\end{split}$
