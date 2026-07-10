Transistoren haben eine *Kennlinie*, die den *Zusammenhang zwischen Eingangssignal (Basis-Emitter- oder Gate-Source-Spannung) und Ausgangssignal (Kollektor-/Drainstrom)* darstellt. Hierbei gibt es im Bereich der Kennlinie verschiedene Abschnitte, in denen der Transistor *lineare oder auch nichtlineare Charakteristik* hat.
Gerade Bereiche der Kennlinie, in denen eine Änderung der Steuergröße eine proportionale Änderung der Ausgangsgröße bewirkt, werden als linear bezeichnet.
Andere Bereiche der Kennlinie, in denen eine Änderung der Steuergröße **keine** proportionale Änderung der Ausgangsgröße bewirkt, werden als nichtlinear bezeichnet.

<margin>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Kennlinie eines Transistors mit Arbeitspunkten]  
</margin>

Für einen optimalen Betrieb des Verstärkers bzgl. Wirkungsgrad und Oberwellenfreiheit des verstärkten Signals ist eine optimale Wahl des Arbeitspunktes des Verstärkers auf dessen Kennlinie vorzunehmen.
Dieser Arbeitspunkt wird durch eine geeignete Hilfsgleichspannung (Vorspannung) an der Basis oder Gate festgelegt.

Die Verstärkung des Eingangssignals erfolgt dann um den gewünschten Arbeitspunkt herum, der das Zentrum des Arbeitsbereiches definiert.
Durch die Wahl des Arbeitspunktes ergibt sich ein entsprechender Ruhestrom des Transistors. Dieser fließt auch ohne vorhandenes Eingangssignal. Der Ruhestrom beeinflusst die Effizienz eines Verstärkers maßgeblich, da er dessen thermische Verlustleistung erhöht und damit dessen Wirkungsgrad reduziert.

Alle Signale, deren Modulations-Information sich in deren Amplitude befindet, müssen linear verstärkt werden, um die übertragene Information verzerrungsfrei zu übermitteln (SSB, AM etc.). Signale, deren Modulations-Information sich nicht in der Amplitude sondern nur in der Frequenz befindet, können auch im nichtlinearen Bereich eines Verstärkers verstärkt werden (FM etc.) und anschließend gefiltert werden.

Je nach Betriebsart unterscheidet man mögliche Arbeitspunkte und deren Bezeichnung auf der Kennlinie (siehe Abbildung [ref:a_kennlinien_transistor_arbeitspunkt] ):

AP1: C-Betrieb des Verstärkers
- ohne Vorspannung
- Ruhestrom null
- Wirkungsgrad ca. $\qtyrange{80}{87}{\percent}$
- hoher Oberwellenanteil

AP2: B-Betrieb des Verstärkers
- Geringe Vorspannung bis zum Einsetzen des Kollektorstroms
- Ruhestrom fast null (gering)
- Wirkungsgrad ca. bis zu $\qty{80}{\percent}$
- geringer Oberwellenanteil

AP3: A/B-Betrieb des Verstärkers
- Höhere Vorspannung als im B-Betrieb, jedoch geringer als im A-Betrieb
- Ruhestrom größer als im B-Betrieb, aber deutlich geringer als im A-Betrieb
- Wirkungsgrad zwischen $\qty{50}{\percent}$ bis $\qty{80}{\percent}$
- geringer Oberwellenanteil

AP4: A-Betrieb des Verstärkers
- Höhe der Vorspannung ist so gewählt, dass der Ruhestrom ca. $\qty{50}{\percent}$ des maximal zulässigen Wertes erreicht
- Wirkungsgrad ca. $\qty{40}{\percent}$
- sehr geringer Oberwellenanteil

[question:AD416]
[question:AD419]
[question:AD420]
[question:AD421]

Die Ausgangsleistung eines Verstärkers kann durch Kenntnis des Arbeitspunktes und damit dessen ungefähren Wirkungsgrads grob berechnet werden. Hierbei berechnet man zunächst die Gleichspannungsleistung aus dem Produkt von Spannung und Strom, die dem Verstärker zugeführt wird. Anschließend multipliziert man diese Leistung mit dem numerischen Faktor des Wirkungsgrads, wobei $\qty{100}{\percent}$ einem Wirkungsgrad von $1$ entsprechen. Beispielsweise entspricht ein Wirkungsgrad von $\qty{40}{\percent}$ dann einem Faktor von $0,4$.

[question:AD424]
[question:AD425]
[question:AD418]
[question:AD417]

Damit ein Verstärker für den SSB-Betrieb (lineare Verstärkung) verwendet werden kann, muss sich dessen Arbeitspunkt im A-/AB- oder B-Betrieb befinden. Grundsätzlich ist A-Betrieb aufgrund der hohen Linearität möglich, jedoch bei höheren Leistungen nicht effizient. Hier schaltet man 2 Transistoren in einer sog. Gegentaktschaltung zusammen, so dass jeder der beiden Transistoren nur jeweils eine Halbwelle (positiv oder negativ) verstärkt. Hierdurch ist auch AB- oder B-Betrieb mit erhöhtem Wirkungsgrad des Verstärkers möglich.
Im C-Betrieb wird das Signal jedoch immer verzerrt. Daher kann ein SSB-Sender nicht im C-Betrieb arbeiten.
Insbesondere beim AB- oder B-Betrieb eines Verstärkers ist Übersteuerung zu vermeiden, da diese schnell zu Verzerrungen des Signals führen kann. Diese äußern sich bei SSB in Form von Splatter auf benachbarten Frequenzen.

[question:AD422]
[question:AJ218]
[question:AD423]

Verstärker im C-Betrieb erzeugen aufgrund ihres stark nichtlinearen Betriebspunktes hohe Oberwellenanteile, die im weiteren Signalweg z.B. durch Filterung (Tiefpass) unterdrückt werden müssen.
Da bei Leistungsverstärkern im C-Betrieb auch Oberwellenanteile mit hohen Amplituden und Leistungen im Verstärker sowie im anschließenden Filter vorhanden sind, müssen sowohl Verstärker als auch Filter in einem gut abschirmenden Metallgehäuse betrieben werden, so dass sie keine Störungen durch Oberwellenanteile verursachen.

[question:AF402]
[question:AF403]


