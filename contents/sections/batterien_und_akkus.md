Wie wir schon gelernt haben, liefern Batterien  deshalb eine elektrische Spannung, weil darin Ladungen getrennt werden. Dies wird durch elektrochemische Vorgänge erreicht. Diese finden statt, sobald der Stromkreis geschlossen ist. Akkumulatoren, kurz Akkus genannt, funktionieren ganz ähnlich. Sie haben aber die Besonderheit, dass sie wiederaufladbar sind. Dabei wird Spannung an die Batterie angelegt und die elektrochemische Reaktion läuft umgekehrt ab. Anschließend kann das Entladen erneut beginnen. Batterien können hingegen nicht wieder aufgeladen werden, sondern sind nur einmal verwendbar.

In Handfunkgeräten werden meistens Akkus, manchmal aber auch Batterien eingesetzt. Um Funkstationen unabhängig vom Stromnetz, z. B. auf einem Fieldday, zu betreiben, werden häufig Akkus verwendet.

Der Aufdruck auf Batterien (Abbildung [ref:n_Bat_AA]) kennzeichnet z. B. den Plus- bzw. Minuspol und weist auf polungsrichtigen Einsatz hin. Bei Batterien ist der Warnhinweis "Nicht wiederaufladbar" stets zu beachten.

Abbildung [ref:n_schaltzeichen_batt] zeigt das Schaltzeichen einer Batterie beziehungsweise eines Akkus. Der lange Strich im Schaltzeichen kennzeichnet den Plus-Pol, der kurze den Minus-Pol. Als Eselsbrücke gilt: ein Plus-Zeichen erfordert 2 Striche, ein Minus-Zeichen aber nur einen.

[question:NB201]
[question:NB203]

<margin>
[photo:89:n_Bat_AA:Eine Batterie mit Kennzeichnung der Pole und Warnhinweisen]
</margin>

<margin>
[picture:517:n_schaltzeichen_batt:Schaltzeichen einer Batterie]
</margin>

<webindepth>
Es gibt unterschiedlichste Batterien und Akkus mit verschiedenen Spannungen, Kapazitäten und Bauformen:
* Häufige Spannungsangaben bei Batterien oder Akkus sind z. B. $\qty{1,5}{\volt}$ oder $\qty{9}{\volt}$. Es gibt sie aber auch mit anderen Spannungen. Ferngesteuerte Modellautos verwenden beispielsweise meist $\qty{7,2}{\volt}$. In akkubetriebenen Werkzeugen finden sich oftmals Akkus mit $\qty{18}{\volt}$, $\qty{20}{\volt}$ oder $\qty{40}{\volt}$.
* Die Kapazität einer Batterie oder eines Akkus wird in Amperestunden ($\unit{\ampere\hour}$) angegeben. Hat ein Akku eine Kapazität von $\qty{5}{\ampere\hour}$ kann er für 5 Stunden einen Strom von einem Ampere fließen lassen - oder beispielsweise auch für 10 Stunden einen Strom von 0,5 Ampere oder einen Strom von $\qty{5}{\ampere}$ für nur eine Stunde. Bei Batterien fehlt oft die Angabe der Kapazität. Haushaltsübliche Batterien haben oft eine Kapazität von weniger als $\qty{5}{\ampere\hour}$. Große Akkus können auch $\qty{100}{\ampere\hour}$ oder mehr Kapazität aufweisen. Bei Akkus wird im Gegensatz zu Batterien praktisch immer die Kapazität angegeben.
* Bei den Bauformen sind die zylinderförmigen AA- und AAA-Zellen sehr bekannt, die in den meisten Haushaltsgeräten eingesetzt werden. Es gibt aber gerade bei den Akkus alle möglichen Bauformen. Oftmals sogar Bauformen, die nur für ein einziges Gerät passen.
</webindepth>

<margin>
[photo:209:batterien_und_akkus_sammlung:Verschiedene Batterien und Akkus]
</margin>

<attention>
Akkus sollten niemals komplett entladen werden. Diese sogenannte Tiefentladung kann den Akku beschädigen. Praktisch lässt sich die Entladung daran erkennen, dass die Spannung des Akkus nach und nach leicht absinkt. Die Stromentnahme muss beendet werden, bevor die vom Hersteller angegebene Mindestspannung unterschritten wird.
</attention>

Viele Geräte benötigen mehrere Batterien. In der Regel dient dies zur Spannungserhöhung, wenn die Spannung einer einzelnen Batterie von z. B. $\qty{1,5}{\volt}$ nicht für den Betrieb ausreicht. Im Batteriefach des Geräts werden diese in Serie verschaltet, sodass der Minuspol der vorhergehenden Batterie jeweils auf den Pluspol der nachfolgenden trifft. Die Spannung an den Enden dieser Kette berechnet sich wie folgt:

$\text{Gesamtspannung} = \text{Anzahl Batterien} \cdot \text{Batteriespannung}$

[question:NB204]

---

Generell gilt, dass bei Batterien und Akkus ein Kurzschluss verhindert werden sollte. Gerade bei leistungsfähigen, modernen Akkus besteht die Gefahr der Überhitzung. Diese können in Brand geraten oder durch den entstehenden Kurzschlusstrom einen Brand verursachen.

<danger>
Während bei Netzgeräten eine Sicherung im Fehlerfall den Stromfluss stoppen kann, fehlt dieser Schutzmechanismus bei Batterien bzw. Akkus meistens. Die Stromstärke, die Batterien und Akkus liefern können, übersteigt oftmals ein Vielfaches des Maximalstroms von Netzgeräten. Dies gilt insbesondere für hochkapazitive Akkus wie z. B. Autobatterien, die kurzzeitig $\qty{1000}{\ampere}$ und mehr Strom liefern können. Bei der Nutzung von externen, hochkapazitiven Akkus sollte unbedingt eine zusätzliche Sicherung vorgesehen werden, wie sie beispielsweise in Abbildung [ref:n_Bat_Sicherung] gezeigt wird!
[photo:90:n_Bat_Sicherung:Anschlussbox mit Kfz-Sicherungen und verpolungsgeschützten Ausgängen zum Schutz von leistungsstarken Akkus]
</danger>

[question:ND110] 

Bei Akkus kommen unterschiedlichste Technologien zum Einsatz, die auf verschiedenen elektrochemischen Reaktionen basieren: Seit vielen Jahrzehnten werden Bleibatterien in Autos verwendet. Kleine, tragbare Geräte verwendeten früher Akkus mit Nickel und Cadmium (NiCd) und später dann die Nickel-Metallhydrid-Technologie (NiMH). Bei Mobiltelefonen, digitalen Kameras oder Notebooks dominieren heute Akkus mit Lithium-Ionen-Technologie. Im Amateurfunk werden zunehmend auch Lithium-Eisen-Phosphat-Mischungen (LiFePO4) verwendet.

Die Unterschiede der elektrochemischen Reaktionen sind beim Aufladen dieser verschiedenen Akkutypen zu berücksichtigen. Es müssen jeweils speziell für die Technologie angepasste Ladegeräte verwendet werden. Unsachgemäße Lade- und Entladevorgänge können zu Überhitzung der Akkus führen. Bei Berührung kann es dann zu gefährlichen Verbrennungen kommen. Auch Explosionen der Akkus und Brände sind durch Überhitzung möglich. Durch freiwerdende Flüssigkeiten kann es zu Verätzungen oder Vergiftungen kommen.

<attention>
Batterien und Akkus sind immer sachgerecht zu entsorgen. Sie gehören nicht in den Hausmüll! Dies wird durch das durchgestrichene Mülltonnensymbol gekennzeichnet (vergleiche Abbildung [ref:n_Bat_AA]).
</attention>

[question:NK306] 

<latexonly>
\newpage
</latexonly>