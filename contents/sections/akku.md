Neben den bekannten Bleiakku (Pb), Nickel-Metallhydrid (NiMH) verwenden auch wir in der Funktechnik z.B. bei Portabelbetrieb immer mehr Lithium-Eisen-Phosphat-Mischungen (LiFePO4). Doch schauen wir uns erstmal ein Akku und dessen Aufschriften in Abbildung [ref:a_akku_lifepo4] an.

% TODO Bild LiFePO4 einfügen
[photo:175:a_akku_lifepo4:LiFePO4]

* Kapazität: $\qty{4200}{\milli\ampere\hour}$
* Spannung: 4S1P / $\qty{13,2}{\volt}$
* Entladung: 30C Constant / 40C Burst
* Balance Stecker: JST-XH
* Entlastung Stecker: $\qty{5.5}{\milli\meter}$ Kugel-Stecker

Die für uns wichtigsten Kenndaten sind die Nennspannung $\qty{13,2}{\volt}$ und die Verschaltung 4S1P. Das bedeutet, dass sich die Nennspannung von $\qty{13,2}{\volt}$ aus 4 in Serie bzw. Reihe und 1 mal parallel, also alle 4 in Serie geschalten sind. Üblicherweise besitzen LiFePO4 eine Zellnennspannung von $\qty{3,2}{\volt}$ bis $\qty{3,3}{\volt}$. Und somit ergibt sich $\qty{3,3}{\volt} \cdot 4 = \qty{13,2 }{\volt} \cdot 1 = \qty{13,2}{\volt}$.

---

<margin>
| l: Zellspannung | l: Bemerkung |
| $\qty{3,3}{\volt}$ | Nennspannung |
| $\qty{2,5}{\volt}$ | min. Spannung |
| $\qty{3,6}{\volt}$ | max. Spannung |
[table:a_akku_lifepo4spannung:LiFePO4 Zellspannung]
</margin>

<attention>
Beachte bei dem Einsatz von einem LiFePO4 als 4S1P verschalten, dass Spannungen zwischen $\qty{10}{\volt}$ bis $\qty{14,4}{\volt}$ anliegen können. Nicht jedes Funkgerät kann mit diesen Spannungen arbeiten.
</attention>

Bei einem 4S2P sind insgesamt 8 Zellen verbaut. 4 in Serie und das 2 mal parallel. Dies würde dann eine Spannung von $\qty{13,2}{\volt}$ aber eine Kapazität von $\qty{8400}{\milli\ampere\hour}$ ergeben.

Bei dem Beispiel-Akku sind $\qty{4200}{\milli\ampere\hour}$ angegeben. Dies entspricht $\qty{4,2}{\ampere\hour}$. Das würde theoretisch bedeuten, wir können unseren Akku $\qty{1}{\hour}$ lang mit $\qty{4,2}{\ampere}$ oder $\qty{2}{\hour}$ lang mit $\qty{2,1}{\ampere}$ usw. belasten.
$t=\frac{Q}{I}$
$t=\frac{\qty{4,2}{\ampere\hour}}{\qty{1}{\ampere}} = \qty{1}{\hour}$
Wenn die Kapazität $Q$ in $\unit{\ampere\second}$ zu berechnen ist, dann erfolgt die Umrechnung  dadurch, dass die Angabe Stunden ($\unit{\hour}$) durch $\qty{3600}{\second}$ ersetzt wird. Daraus ergibt sich $\qty{4,2}{\ampere} \cdot \qty{3600}{\second} = \qty{15120}{\ampere\second}$.
Nun wollen wir aber auch wissen, wie viel elektrische Energie in dem Akku gespeichert ist. Energie ($\unit{\watt\hour}$) ist die Ladung $Q$ ($\unit{\ampere\hour}$) des Akkus multipliziert mit der Gesamtspannung $U$ in Volt.

$\qty{1}{\watt\hour} = \qty{1}{\ampere\hour} \cdot \qty{1}{\volt}$

Für unser Beispiel berechnen wir $\qty{4,2}{\ampere\hour} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\hour}$ als gespeicherte Energie.
Die Entladung dieses Akkus kann mit einem konstanten Entladestrom von  "30 $C$" erfolgen. Das bedeutet,  dass der Akku mit 30 · Kapazität $Q$ entladen werden kann.
Endladestrom = $30 \cdot \qty{4200}{\milli\ampere} = \qty{126}{\ampere}$
Das ist allerdings nur ein theoretisch möglicher Wert, da unser Akku somit innerhalb von $\qty{108}{\second}$ entladen wäre. Auch der Kabelquerschnitt ist dabei zu berücksichtigen.
Bei Reihen- bzw. Serienschaltung von Akkus, wie in Abbildung [ref:a_akku_4S1P] addieren sich die Spannungen und die Kapazität bleibt gleich. 

% TODO Bild Reihenschaltung liegt bei DG1HXJ als .tex
[photo:176:a_akku_4S1P:Reihenschaltung]

Bei der Parallelschaltung wie in Abbildung [ref:a_akku_4S2P] bleibt die Spannung gleich und die Kapazitäten addieren sich. 

% TODO Bild Parallelschaltung liegt bei DG1HXJ als .tex
[photo:177:a_akku_4S2P:Parallelschaltung]

---

Wichtig ist jedoch, dass wir nur Zellen/ Akkus mit gleichen Daten zusammenschalten, da sich die Zellen gegenseitig beeinflussen und sonst beschädigt werden können.
Insbesondere bei den aktuellen Lithium-Akkumulatoren ist es sinnvoll eine Überwachungseinrichtung (Balancer, Batteriemonitor) zu verbauen. Dieser sorgt u.a. für den notwendigen Ausgleich der Zellspannungen und für eine optimale Ladung. In der Abb. [ref:a_akku_lifepo4_anschluss]

% TODO Bild Infobox Anschluss Akku liegt bei DG1HXJ als .tex
<margin>
[photo:178:a_akku_lifepo4_anschluss:LiFePO4 Anschlüsse]
</margin>
[question:AB210]

Die Akku-Nennkapazität $Q$ wird auch als Ladung bezeichnet und, wie bereits bekannt, in $\unit{\ampere\hour}$ oder $\unit{\milli\ampere\hour}$ angegeben.

------

[question:AB209]
Die Gesamtspannung ist die Summe der Zellenspannungen. Die Gesamtladung entspricht der Ladung einer Zelle.


[question:AB211]

Zuerst muss die entnehmbare Ladungsmenge von $\qty{90}{\percent}$ ermittelt werden.
Die Entladezeit $t$ ergibt sich aus: $t=\frac{Q}{I}$


[question:AB501]
Die im Akku gespeicherte Energie in $\unit{\watt\hour}$ oder $\unit{\volt\ampere\hour}$ ergibt sich aus der Multiplikation der Akkuspannung $U$ ($\unit{\volt}$) mit der Ladung $Q$ ($\unit{\ampere\hour}$).
Beispiel:
$\qty{1}{\volt} \cdot \qty{1}{\ampere\hour} = \qty{1}{\watt\hour}$
<margin>
  
  Lösungshilfe:
  
  AB 209: $6 \cdot \qty{2}{\volt} = \qty{12}{\volt} / \qty{10}{\ampere\hour}$
  AB 210: Nennkapazität
  AB 211: $\qty{90}{\percent} = \qty{54}{\ampere\hour}; \qty{54}{\ampere\hour} / \qty{0,8}{\ampere} = \qty{67,5}{\hour}$ oder 67 Stunden und 30 Minuten
  AB 501: $\qty{12}{\volt} \cdot \qty{5}{\ampere\hour} = \qty{60,0}{\watt\hour}$
  
</margin>