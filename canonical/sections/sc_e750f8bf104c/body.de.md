Wir haben gelernt: Ist eine Antenne perfekt an die Zuleitung (z. B. ein Koaxialkabel) angepasst, zeigt das SWR-Meter den Wert 1 an. Dies ist der bestmögliche Fall, da die gesamte Sendeleistung von der Antenne aufgenommen wird und keine Leistung zum Sender zurückreflektiert wird. Ist hingegen gar keine Antenne angeschlossen oder ist die Übertragungsleitung unterbrochen bzw. kurzgeschlossen, steigt der SWR-Wert gegen unendlich ($\infty$). In diesen Fällen wird die Sendeleistung nahezu vollständig reflektiert. Eine solche vollständige Rückreflexion kann im schlimmsten Fall zur Beschädigung der Endstufe des Senders führen. Hier vertiefen wir das Thema nun etwas und lernen auch Werte zwischen $\num{1}$ und $\infty$ kennen.

Das Stehwellenverhältnis (SWR), als Formelsymbol $s$, lässt sich aus der vorlaufenden Leistung $P_\text{V}$ und der rücklaufenden Leistung $P_\text{R}$ berechnen. Der entsprechende Zusammenhang lautet:

$s = \frac{\sqrt{P_\text{V}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{V}}-\sqrt{P_\text{R}}}$

Gibt zum Beispiel der Sender eine Leisung von $P_\text{V}=\qty{100}{\watt}$ ab, und es werden $P_\text{R}=\qty{25}{\watt}$ von der Antenne in Richtung Sender zurück reflektiert, so ergibt sich:

$s = \frac{\sqrt{100}+\sqrt{25}}{\sqrt{100}-\sqrt{25}} = \frac{10+5}{10-5} = \frac{15}{5} = 3$

Das bedeutet, dass ein SWR von $\num{3}$ einer Reflektion von $\frac{\qty{25}{\watt}}{\qty{100}{\watt}}=\qty{25}{\percent}$ entspricht. Weitere Entsprechungen sind in der Tabelle [ref:e_swr_werte] dargestellt.

<margin>
| l: SWR | l: Reflektierte Leistung |
| $\num{1}$ | $\qty{0}{\percent}$ |
| $\num{1,5}$ | $\qty{4}{\percent}$ |
| $\num{2}$ | $\qty{11,1}{\percent}$ |
| $\num{2,5}$ | $\qty{18,4}{\percent}$ |
| *$\num{3}$* | *$\qty{25}{\percent}$* |
| $\num{4}$ | $\qty{36}{\percent}$ |
| $\num{6}$ | $\qty{51}{\percent}$ |
| $\num{10}$ | $\qty{66,9}{\percent}$ |
| $\num{20}$ | $\qty{81,9}{\percent}$ |
| $\infty$ | $\qty{100}{\percent}$ |
[table:e_swr_werte:SWR-Werte in Bezug auf die reflektierte Leistung]
</margin>

---

<tip>
Zur Beantwortung der folgenden Fragen reicht es aus zu wissen, dass ein Stehwellenverhältnis von $\num{3}$ einer Reflexion von $\qty{25}{\percent}$ der Energie entspricht, d.h. die rücklaufende Welle überträgt ein Viertel der Energie der vorlaufenden Welle. Entsprechend werden nur $\qty{75}{\percent}$ der Energie am Ende der Leitung z. B. an eine Antenne oder einen Verlustwiderstand abgegeben (also nicht reflektiert). 
</tip>

[question:EG401]
[question:EG402]
[question:EG403]

<indepth>
Herleitung der hier verwendeten SWR-Leistungsformel anhand der BAKOM-Formelsammlung.
Man kann obige Formel auch einfach verwenden. Ein Verständnis der Herleitung ist nicht erforderich! 😉

1. Ausgangsbasis (BAKOM-Formelsammlung)

Die BAKOM-Formelsammlung definiert das Stehwellenverhältnis ($s$) und den Reflexionsfaktor ($|r|$) über folgende zwei Gleichungen:

$$s = \frac{1 + |r|}{1 - |r|}$$

$$|r| = \frac{\sqrt{P_\text{r}}}{\sqrt{P_\text{d}}}$$

---

2. Herleitung

Um den Bruch für $s$ zu vereinfachen und das $|r|$ zu ersetzen, multipliziert man gedanklich jeden Term im Zähler und im Nenner direkt mit $\sqrt{P_\text{d}}$. Dadurch kürzt sich der Nenner von $|r|$ sofort weg:

1. Aus der $1$ wird:
   $$1 \cdot \sqrt{P_\text{d}} = \sqrt{P_\text{d}}$$
2. Aus dem $|r|$ wird:
   $$\frac{\sqrt{P_\text{r}}}{\sqrt{P_\text{d}}} \cdot \sqrt{P_\text{d}} = \sqrt{P_\text{r}}$$

Setzt man diese Terme direkt in die SWR-Gleichung ein, ergibt sich unmittelbar:

$$s = \frac{\sqrt{P_\text{d}} + \sqrt{P_\text{r}}}{\sqrt{P_\text{d}} - \sqrt{P_\text{r}}}$$

---

3. Anpassung an die hier verwendete Notation

Durch das Ersetzen der Variablennamen ($s \rightarrow \text{SWR}$ und $P_\text{d} \rightarrow P_\text{v}$ für die Vorwärtsleistung) erhält man exakt die Zielformel:

$$\text{SWR} = \frac{\sqrt{P_\text{v}} + \sqrt{P_\text{r}}}{\sqrt{P_\text{v}} - \sqrt{P_\text{r}}}$$
</indepth>
