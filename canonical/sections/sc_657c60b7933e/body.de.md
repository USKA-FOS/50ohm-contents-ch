Bislang hatten wir elektrische und magnetische Felder für den Fall betrachtet, dass Felder zeitlich nicht veränderlich sind. In der Funktechnik sind solche Felder aber eigentlich uninteressant, denn wir beschäftigen uns mit Spannungen und Strömen, die zeitlich veränderlich sind. Ebenso sind die erzeugten elektrischen und magnetischen Felder zeitlich variabel. 

<margin>
[picture:885:e_vertikalantenne_em:Elektrisches und magnetisches Feld an einer Antenne]
</margin>

Dabei treten zusätzliche Effekte auf. Bereits 1831 entdeckte Michael Faraday, dass ein zeitlich veränderliches Magnetfeld in einem benachbarten Leiter eine elektrische Spannung erzeugt. Dieser *Induktion* genannte Effekt wird zum Beispiel im Transformator genutzt: ein zeitlich variabler (z.B. sinusförmiger) Strom in der Primärwindung erzeugt ein zeitlich variables Magnetfeld, das wiederum in der Sekundärwindung eine Spannung induziert.

Um zu erkennen, dass umgekehrt die Änderung eines elektrischen Felds zu einem Magnetfeld führt, stellen wir uns einen Plattenkondensator vor, dessen Platten mit einer externen Spannungsquelle einen Stromkreis bilden. Wenn wir das elektrische Feld im Inneren des Kondensators ändern, müssen im äußeren Stromkreis Ladungen bewegt werden. Das Bewegen von Ladungsträgern bedingt aber einen elektrischen Strom. Dieser elektrische Strom erzeugt aber wiederum ein Magnetfeld um den Leiter.

Während Modellvorstellungen mit elektrischen Leitern für uns anschaulich sind, ist es aber ganz wichtig, dass diese Leiter nicht notwendig sind. Magnetische und elektrische Felder existieren  auch außerhalb von Leitern, sogar im Vakuum. Auch hier ist es so, dass ein zeitlich verändertes Magnetfeld ein zeitlich veränderliches elektrisches Feld erzeugt. Dieses zeitlich veränderliche Feld wiederum führt zu einem zeitlich veränderlichen Magnetfeld. *Zeitlich veränderliche magnetische Felder und zeitlich veränderliche elektrische Felder sind also immer gekoppelt.* Wir sprechen deshalb auch vom *elektromagnetischen Feld*. Zusammengefasst: Eine elektromagnetische Welle, die sich frei im Raum ausbreiten kann, beruht auf der Wechselwirkung zwischen zeitlich veränderlichen magnetischen und elektrischen Feldern.

[question:EB302]

Wie oben schon beschrieben, zeitlich konstante Spannungen und Ströme können kein elektromagnetisches Feld erzeugen. Dazu benötigen wir einen zeitlich veränderlichen Strom in einem Leiter.

[question:EB301]

<indepth>
Magnetfeld und elektrisches Feld werden eigentlich durch *Vektoren* beschrieben, also durch Größen, die eine Richtung im Raum haben. Mathematisch lässt sich zeigen, dass im *Fernfeld*, also hinreichend weit weg von der Antenne, die Vektoren der beiden Felder senkrecht aufeinander stehen müssen. Die Ausbreitungsrichtung der elektromagnetischen Welle (also unseres Funksignals ...) steht wiederum senkrecht sowohl auf dem elektrischen als auch dem magnetischen Feld.
  
[picture:886:e_emfeld_ausbreitung:Ausbreitung der elektromagnetischen Welle]
  
Die geschilderten Zusammenhänge werden mathematisch durch die *Maxwellschen Gleichungen* beschrieben, nach James Clerk Maxwell, der sie zwischen 1861 und 1864 anhand von Beobachtungen anderer Physiker erarbeitet. Er kam dabei zu der Erkenntnis, dass die magnetischen und elektrischen Felder gekoppelt sein müssen:
  
1. $\vec{\nabla} \cdot \vec{E} =\frac{\rho}{\varepsilon_{0}}$
2. $\vec{\nabla} \cdot \vec{B} = 0$
3. $\vec{\nabla} \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$
4. $\vec{\nabla } \times \vec{B} =\mu_0 (\vec{j} +\varepsilon_0 \frac{\partial\vec{E}}{\partial t})$
  
Die Gleichung (3) zeigt, dass ein zeitlich veränderliches Magnetfeld ein elektrisches Feld erzeugt. Dieses zeitlich veränderliche elektrische Feld trägt gemäß Gleichung (4) über den Verschiebungsstrom wiederum zur Erzeugung eines Magnetfeldes bei. Diese Zusammenhänge gehen weit über das hinaus was man im Amateurfunk wissen muss.
  
Experimentell wurde die Existenz des elektromagnetischen Felds allerdings erst mehr als zwanzig Jahre später (1886) durch Heinrich Hertz nachgewiesen.
</indepth>

Wie in den Abbildungen  und [ref:e_emfeld_ausbreitung] gezeigt, steht die magnetische Feldkomponente im Fernfeld (weit weg von der Antenne) stets senkrecht auf der elektrischen Feldkomponente.

[question:EB303]

Die im Fernfeld senkrecht aufeinander stehenden magnetischen und elektrischen Feldkomponenten legen auch die Ausbreitungsrichtung $S$, wie in Abbildung [ref:e_vertikalantenne_em] gezeigt, fest: sie steht wiederum senkrecht auf beiden. Man kann sich das so vorstellen, dass magnetisches und elektrisches Feld eine Ebene aufspannen, auf der die Ausbreitungsrichtung senkrecht steht.

[question:EB304]