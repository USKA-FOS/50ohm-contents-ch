Durch den geringen Aufwand ist der Brückengleichrichter eine häufig verwendete Gleichrichterschaltung. Dazu benötigt man einen Trafo und 4 Dioden.

<latexonly>
In der Abbildung [ref:a_brueckenlgeichrichter] ist ein solcher Brückengleichrichter dargestellt.

<margin>
[picture:965:a_brueckenlgeichrichter:Brückengleichrichter]
</margin>
</latexonly>

<webonly>
In dem nebenstehenden Applet ist ein solcher Brückengleichrichter dargestellt. Man kann bei dargestellter Polarität der Trafospannung $U_a$ bzw. $U_s$ den Laststrom in seinem Stromverlauf verfolgen und erkennen, dass der dieser stets in gleicher Richtung durch den Lastwiderstand $R$ fließt.

<margin>
[include:applet_gleichrichter_2]
</margin>
</webonly>

<tip>
[picture:67:a_brueckenlgeichrichter_2:Anordnung der Dioden im Brückengleichrichter]
Beim Brückengleichrichter zeigen die Dioden mit ihren Kathoden zum Pluspol hin und die Anoden zum Minuspol. Man kann sich also merken: Die "Striche" der Dioden treffen sich am Plusausgang. Diese Anordnung darf nicht mit einem Diodenringmischer verwechselt werden, welchen wir noch später kennenlernen werden. 
</tip>

[question:AD305]

---

Wenn man nach dem Brückengleichrichter einen Ladekondensator $C_L$ und ein LC-Siebglied (vgl. Abbildung [ref:a_netzteil_Ucs] verbaut, erreicht man damit eine kleinere Amplitude in der pulsierenden Ausgangsgleichspannung. Somit haben wir ein konventionelles Netzteil. 

<margin>
[picture:66:a_netzteil_Ucs:Gleichrichterschaltung mit Siebung]
</margin>

Auch beim Brückengleichrichter lädt sich der Kondensator auf die Spitzenspannung $\hat{U}$ der Sekundärspannung $U_{\mathrm{sek}}$ des Trafos auf.

$\hat{U}=U_{\mathrm{eff}}\cdot\sqrt{2}$

Weiterhin müssen wir beachten, ob der Trafo ein Übersetzungsverhältnis $ü$ aufweist. Mit diesem Wissen können wir die folgende Aufgabe lösen.

[question:AD306]

<indepth>
[photo:296: Brückengleichrichter Bauformen: Bauformen von Brückengleichrichtern]
Die Beschriftung der Anschlüsse ist zu beachten.

1. Hochstrom-Brückengleichrichter 26 MB 20 A ($\qty{200}{\volt}$, $\qty{25}{\ampere}$) im Metallgehäuse zur direkten Montage auf einem Kühlkörper
2. B80 C 5000/3300 bedeutet: maximal $\qty{80}{\volt}$ Betriebsspannung, C kapazitive Last max. $\qty{2500}{\micro\farad}$ mit Schutzwiderstand $R = \qty{1}{\ohm}$, maximaler Dauerlaststrom: $\qty{5000}{\milli\ampere}$ mit Kühlkörper, $\qty{3300}{\milli\ampere}$ ohne Kühlkörper
3. BY 225 Brückengleichrichter - besonderes Gehäuse
4. runde Bauform eines Brückengleichrichters B 80 C 1000
5. B40 C 1500 - die veränderte Anschlussfolge ist zu beachten
6. FPU 4M ($\qty{1000}{\volt}$, $\qty{4}{\ampere}$)
7. im Kunststoff eingeprägte Anschlussfolge
</indepth>
