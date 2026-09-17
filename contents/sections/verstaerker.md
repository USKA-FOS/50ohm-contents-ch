Im Kapitel zu den Transistoren haben wir bereits kennengelernt, dass sich mit einem kleinen Basisstrom $I_\text{B}$ ein deutlich größerer Kollektorstrom $I_\text{C}$ steuern lässt. Dieses Prinzip kann genutzt werden, um einen Verstärker für elektrische Signale aufzubauen. Abhängig von der jeweiligen Schaltungsart lassen sich mit Transistoren Signale aller Art verstärken – seien es digitale Signale, Niederfrequenz- (NF) oder Hochfrequenz- (HF) Signale. Eine Verstärkung bedeutet dabei, dass die Ausgangsleistung eines Signals größer ist als seine Eingangsleistung, was das grundlegende Kennzeichen eines Verstärkers darstellt.

---

Die Abbildung [ref:e_nf_verstaerker] zeigt einen Niederfrequenz-Verstärker (NF-Verstärker) welcher Audio-Signale aus dem Funkgerät für einen Lautsprecher verstärken soll. Dies ist Leicht am Lautsprechersymbol in der Schaltung zu erkennen. HF-Leistungsverstärker werden z.B. zur Anhebung des Sendesignals eingesetzt.

<margin>
[picture:763:e_nf_verstaerker:Schaltbild eines NF-Verstärkers]  
</margin>

[question:ED402]
[question:ED403]

Da sich die Ausgangsleistung gegenüber der Eingangsleistung erhöht, muss einem Verstärker immer Energie zugeführt werden. Daher ist eine entsprechend belastbare Spannungsquelle erforderlich.

[question:ED401]

---

Damit ein Verstärker als *linear* bezeichnet werden kann, muss er die Eigenschaft besitzen, dass bei einer Verdoppelung des Eingangssignals sich das Ausgangssignal am Verstärker ebenfalls verdoppelt.
Linearitätsabweichungen sind i.d.R unerwünscht und nur bei Betriebsarten wie FM (bei denen die Information des Signals nicht über die Amplitude, sondern nur über die Frequenz übertragen wird) tolerierbar. Arbeitet ein Verstärker nicht linear, so sind in dessen Ausgangssignal Frequenzen vorhanden, die im Eingangssignal nicht vorhanden sind (sog. Splatter). Im NF-Bereich äußert sich dieses Verhalten als Verzerrung. Im HF-Bereich entstehen Oberwellen des verstärkten Signals. Beides ist unerwünscht. Die Abbildung [ref:e_verstaerker_linearitaet] zeigt beispielhaft wie ein Sinus-Signal durch nichtlineares Verhalten verformt wird. 

<margin>
[picture:828:e_verstaerker_linearitaet:Das Eingangssignal wird verstärkt. Bei Begrenzung durch fehlende Linearität wird das Ausgangssignal verformt.]
</margin>

[question:EF403]

Für die Linearität eines Senders ist ebenfalls eine stabilisierte und von anderen Stufen entkoppelte Stromversorgung notwendig, um unerwünschte Rückkopplungen zu vermeiden.

[question:EF405]

Nicht nur beim Lautsprecher am Funkgerät findet man NF-Verstärker, sondern auch bereits am Mikrofon. Diese dienen hierbei z. B. für die Verstärkung des Mikrofon-Signals. Üblicherweise werden hierbei tiefere (unter $\qty{300}{\hertz}$) und höhere Frequenzanteile (über $\qty{3}{\kilo\hertz}$) des Mikrofonsignals bereits innerhalb des Mikrofonverstärkers durch eine Bandpasscharakteristik unterdrückt, um die Bandbreite des NF-Signals zu begrenzen und tiefere Frequenzanteile wie z.B. Netzbrummen zu unterdrücken (vgl. Abbildung [ref:e_frequenzgang_mikrofonverstaerker]). Für eine gute Sprachverständlichkeit ist bei Sprachkommunkation eine NF-Bandbreite von ca. $\qtyrange{2,5}{3}{\kilo\hertz}$ erforderlich.

<margin>
[picture:246:e_frequenzgang_mikrofonverstaerker:Typischer Frequenzgang für einen Amateurfunk-Mikrofonverstärker]
</margin>

[question:EF308]
[question:EF307]