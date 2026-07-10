Bei der Phasenmodulation wird die Phase einer Trägerwelle in Abhängigkeit vom Modulationssignal verändert. Das bedeutet, dass die Phasenverschiebung der Trägerwelle direkt proportional zur Amplitude des Modulationssignals variiert. Diese Veränderung der Phase bleibt im Verlauf des Signals erhalten und variiert im Vergleich zur ursprünglichen Trägerwelle in einem bestimmten Muster. Das Resultat ist ein sinusförmiges Signal, dessen „Versatz“ (Phase) sich laufend anpasst, ohne dass sich dabei die Amplitude des Signals ändert.

Die Phasenmodulation kann man sich bildlich als das Verschieben der Sinuskurve entlang der Zeitachse vorstellen, wobei jede Veränderung der Phase durch das Modulationssignal gesteuert wird. Je stärker die Amplitude des Modulationssignals, desto mehr verschiebt sich die Phase des Trägersignals.

Phasenmodulation und Frequenzmodulation gehören beide zur Gruppe der Winkelmodulationstechniken, da sie beide den Winkel der Trägerwelle beeinflussen. Der Unterschied liegt darin, dass bei der Frequenzmodulation die Frequenz und bei der Phasenmodulation die Phase direkt beeinflusst wird.

Dies zeigt sich besonders deutlich bei einem Rechtecksignal als Nutzsignal: Bei der Phasenmodulation bewirkt jede Flanke des Rechtecks einen sofortigen Phasensprung des Trägersignals, während bei der Frequenzmodulation die Signalflanke lediglich einen Frequenzwechsel auslöst – die daraus resultierende Phasenänderung entsteht erst indirekt, indem sie sich kontinuierlich über die Zeit aufakkumuliert.

<margin>
[picture:907:a_phasenmodulation:Phasenmodulation mit Umkehrung der Phase]
</margin>

<webonly>
<margin>
[include:applet_pm]
</margin>
</webonly>

<indepth>
Für mathematisch Interessierte: Bei der Phasenmodulation hat das Nutzsignal $m(t)$ einen direkten Einfluss auf die Phase, z. B.: 

$\varphi(t) = m(t)$

Das Trägersignal wird als Sinusschwingung der Form

$s(t) = A_c \cos(2\pi f_c t + \varphi(t))$

erzeugt, wobei $A_c$ die Amplitude, $f_c$ die Trägerfrequenz und $\varphi(t)$ die modulierte Phase ist.

Die beiden Modulationsarten FM und PM stehen in einem engen Zusammenhang: Die Phasenmodulation eines Signals hat indirekt eine Veränderung der Frequenz zur Folge, und umgekehrt erzeugt die Frequenzmodulation eine Änderung der Phase. Mathematisch kann man den Zusammenhang zwischen Frequenz und Phase durch die folgende Beziehung ausdrücken:

$f_i(t) = \frac{1}{2\pi} \cdot \frac{d\varphi(t)}{dt}$

Das bedeutet die Frequenz ist die zeitliche Ableitung der Phase.

Es ist also möglich, die Frequenzmodulation durch Phasenmodulation zu realisieren, indem das Nutzsignal $m(t)$ integriert wird:

$\varphi(t) = 2\pi \int m(t) \, dt$

Das Ergebnis wird anschließend als $\varphi(t)$ in die Trägerfunktion eingesetzt.
</indepth>

[question:AE313]