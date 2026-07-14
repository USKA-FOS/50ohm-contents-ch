<margin>
[picture:666:n_halbleiter_diode_merkhilfe:Merkhilfe Diode]
</margin>

Um aus einer Wechselspannung eine Gleichspannung zu erzeugen, wird ein Gleichrichter benötigt. Die einfachste Form der Gleichrichtung erfolgt mithilfe einer Diode. Wie wir bereits in der Klasse N gelernt haben, lässt eine Diode den Strom nur in einer Richtung fließen.

---

Diese Eigenschaft der Diode nutzen wir zur Erzeugung einer Gleichspannung aus einer Wechselspannung (vgl. Abbildung [ref:e_einweggleichrichter_ue]). Schaltet man einen Lastwiderstand über eine in Reihe geschaltete Diode an eine Wechselspannungsquelle (Schaltung in Abbildung [ref:e_einweggleichrichter]), so leitet die Diode den Strom nur dann, wenn die Anode gegenüber der Kathode positiver ist. In diesem Fall wird die positive Halbwelle der Wechselspannung durchgelassen.

Während der negativen Halbwelle sperrt die Diode, sodass die Ausgangsspannung in dieser Zeit auf null bleibt (vgl. Abbildung [ref:e_einweggleichrichter_ul]). Da bei dieser Schaltung nur eine Halbwelle der sinusförmigen Wechselspannung genutzt wird, bezeichnet man sie als *Einweggleichrichtung*.

---
<margin>
[picture:797:e_einweggleichrichter:Einweggleichrichter]
[picture:798:e_einweggleichrichter_ue:Eingangsspannung Einweggleichrichter]
[picture:796:e_einweggleichrichter_ul:Lastspannung Einweggleichrichter]
</margin>

[question:ED304]

Schaltet man nun zusätzlich einen ausreichend großen Kondensator parallel zum Lastwiderstand, lädt sich dieser während der leitenden Halbwelle schnell über die Diode auf. In der darauffolgenden Halbwelle, in der die Diode sperrt, entlädt sich der Kondensator langsam über den Widerstand. Auf diese Weise wird die pulsierende Spannung geglättet und nähert sich einer Gleichspannung an.

Neben der Einweggleichrichtung existieren weitere Gleichrichterschaltungen, beispielsweise der Brückengleichrichter. Auf diese Varianten werden wir jedoch erst in der Klasse A genauer eingehen.