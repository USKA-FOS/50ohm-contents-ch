**IN BEARBEITUNG**

[index:Oberwellen] [index:Harmonische] [index:Nebenaussendungen]

In den Abschnitten [sec:unerwuenschte_aussendungen_1] und [sec:unerwuenschte_aussendungen_2] haben wir bereits unerwünschte Aussendungen in Form von *Oberwellen* und *Nebenaussendungen* kennengelernt. Oberwellen bzw. Harmonische eines Signals entstehen immer, wenn sich Abweichungen von der idealen Sinus-Kurve bilden und sind immer ganzzahlige Vielfache der Grundfrequenz, wie in Abbildung [ref:a_harmonische] dargestellt.

Ein Beispiel zeigt die folgende Prüfungsfrage: Wird ein Verstärker übersteuert, werden die Spitzen der Amplitude des Sinussignals begrenzt – dadurch entstehen Oberwellen.

[question:AJ207]

<margin>
[picture:868:a_harmonische: Oberwellen (OW), Harmonische (Harm.) und Nebenaussendungen (NA)]
</margin>

---

Bei der Betrachtung von Vielfachen der Grundfrequenz eines Signals unterscheiden wir zwischen den Begriffen *Harmonische und Oberwellen* des Signals. Diese beiden Begriffe unterscheiden sich nur in deren Definition und Zählweise. Die 1. Harmonische eines Signals ist dessen Grundfrequenz selbst. Die 2. Harmonische entspricht der 1. Oberwelle eines Signals, die 3. Harmonische der 2. Oberwelle eines Signals und so weiter. Die nebenstehende Tabelle [ref:a_harmonische] zeigt den Zusammenhang. 

<margin>
| l: Vielfaches der Grundfrequenz | l: Harmonische | l: Oberwelle |
| $f_0$ | 1 | ~ |
| $2 \cdot f_0$ | 2 | 1 |
| $3 \cdot f_0$ | 3 | 2 |
| $4 \cdot f_0$ | 4 | 3 |
[table:a_harmonische:Harmonische und Oberwellen]
</margin>

---
  
[question:AJ203]
[question:AJ204]

<tip>
Das UKW-Radio ist das klassische analoge Radio auf auf Ultrakurzwelle (UKW). Die Ausstrahlung von Radioprogrammen erfolgt im Frequenzbereich von 87,5 bis 108 MHz.

In der Schweiz war ursprünglich vorgesehen, die UKW-Verbreitung Ende 2024 einzustellen. Inzwischen wurde die Fortführung der UKW-Verbreitung beschlossen. Das BAKOM vergibt neue UKW-Funkkonzessionen, die grundsätzlich ab 2027 gelten und bis Ende 2034 befristet sind.
</tip>

Sollen bestimmte Oberwellen oder Harmonische eines Signals einzeln unterdrückt werden, so kann dies neben dem klassischen Oberwellenfilters (Tiefpass) auch durch sog. *Sperrkreise* erfolgen. Ein Sperrkreis unterdrückt genau eine Frequenz maximal und lässt ansonsten alle anderen nahezu ungehindert passieren.

[question:AJ210]

---

Das BAKOM verweist bezüglich der einzuhaltenden technischen Daten auf die **Radio Interface Regulations** 
**RIR**. RIR1101 enthält die Anforderungen an Amateurfunkanlagen. Die Schweiz lehnt sich hierbei eng an das ITU Radioreglement (Anhang 3) und die harmonisierten europäischen Normen (ETSI EN 301 783) an.
Die Dämpfung der Nebenaussendungen (Spurious Emissions) relativ zur Leistung der Hauptfrequenz muss folgende Mindestwerte einhalten.

| **Frequenzen**   | **Grenzwert für Nebenaussendungen**                     |
| **Bis 30 MHz**   | Höherer Wert aus −(43 + 10 · log₁₀(PEP)) dBc und −50 dBc |
| **Über 30 MHz**  | Höherer Wert aus −(43 + 10 · log₁₀(PEP)) dBc und −70 dBc |

<indepth>
Der Erfolg der modernen Telekommunikation beruht auch auf gut verfügbaren, internationalen Normen. Wichtige Normen-Organisationen sind:

- **I**nternational **T**elecommunication **U**nion (**ITU**)

- **C**onférence **E**uropéenne des Administrations des **P**ostes et des **T**élécommunications (**CEPT**)

- **E**uropean **T**elecommunications **S**tandards **I**nstitute (**ETSI**)

</indepth>

<margin>
**Zahlenbeispiel für Kurzwelle**

Nehmen wir einen Kurzwellen-Sender mit einer Spitzenleistung bei der Modulation (PEP) von **100 W**.
Nach der zuvor genannten ETSI-Formel ergibt sich:

$$43 + 10 \cdot \log_{10}(100) = 43 + 20 = 63\mathrm{dB}$$

Der Grenzwert ist der weniger strenge der beiden Werte −63 dBc und −50 dBc, also **−50 dBc**.
Das bedeutet: Die Nebenaussendung darf höchstens 50 dB unter der Bezugsleistung liegen.

Umgerechnet in eine absolute Leistung:

$$P_{\text{Neben}} = 100\mathrm{W} \cdot 10^{-50/10}= 0{,}001\mathrm{W}= \boxed{1\mathrm{mW}}$$

**Praxisergebnis:**
Bei einem Sender mit 100 W PEP liegt der Grenzwert für die Nebenaussendungen bei **$\qty{1}{\milli\watt}$**.

**Rechenaufgabe**

- Berechne den maximal zulässigen Pegel der Nebenaussendungen für einen QRP-Kurzwellensender
  mit $\qty{1}{\watt}$ PEP!
  Das richtige Ergebnis ist: $\qty{50.1}{\micro\watt}$  (-43 dBc)
</margin>

Unerwünschte Aussendungen sind auf das geringstmögliche Maß zu beschränken und dürfen den Grenzwert für Nebenaussendungen keinesfalls überschreiten. Diese Grenzwerte gelten sowohl für Hersteller kommerzieller Amateurfunkgeräte als auch für selbstgebaute Funkgeräte.

Für den Kurzwellenbereich unter $\qty{30}{\mega\hertz}$ gilt, dass Nebenaussendungen und Oberwellen mindestens $\qty{50}{\dB}$ gegenüber dem maximalen Sendesignalspitzenpegel des Senders (PEP) gedämpft werden müssen, solange sich die Leistung der Signale oberhalb eines Pegels von $\qty{50}{\micro\watt}$ befindet (vgl. Abbildung [ref:a_uagw1]).

Die Abbildung [ref:a_uagw3] stellt die zulässigen Grenzwerte dar.

[question:AJ224]

%<margin>
%[picture:1140:a_uagw1:Oberwellendämpfung KW-Bereich]
%</margin>

<margin>
[picture:918:a_uagw:Oberwellendämpfung VHF/UHF/SHF-Bereich]
</margin>

<margin>
[picture:1139:a_uagw3:Oberwellendämpfungen nach ETSI EN 301 783]
</margin>

Für den VHF/UHF/SHF-Bereich über $\qty{30}{\mega\hertz}$ gilt, dass Nebenaussendungen und Oberwellen mindestens $\qty{70}{\dB}$ gegenüber dem maximalen Sendesignalspitzenpegel des Senders (PEP) gedämpft werden müssen, so lange sich die Leistung der Signale oberhalb eines Pegels von $\qty{50}{\micro\watt}$ befindet (vgl. Abbildung [ref:a_uagw]).

[question:AJ225]

%TODO BILD VON DL1COM EINBAUEN
Mit einem Spektrumanalysator lässt sich im Modus spurious emissions eine Messung der Oberwellen bzw. Harmonischen (engl. harmonics) durchführen, wie in Abbildung [ref:a_uagw1] und [ref:a_uagw] dargestellt. Der Spektrumanalysator erfasst dabei automatisch den Pegel des Trägers sowie die Unterdrückung der Harmonischen und zeigt diese zusätzlich auf dem Bildschirm an. Wenn man ein Gerät selbst baut, ist es entscheidend, durch Messungen sicherzustellen, dass die vorgeschriebenen Grenzwerte eingehalten werden. Ein kommerzieller Funkgerätehersteller bestätigt mit der CE-Erklärung zwar die Einhaltung dieser Grenzwerte, dennoch kommt es vor, dass einzelne Geräte die Vorgaben nicht erfüllen – in solchen Fällen kann das BAKOM deren Betrieb, Import und Verkauf verbieten.

Unerwünschte Aussendungen entstehen nicht nur durch Oberwellen, sondern können auch in der Frequenzaufbereitung von Sendern auftreten – etwa durch unerwünschte Mischprodukte, durch Schwankungen in der Versorgungsspannung oder durch eine Übersteuerung des NF-Signals. Das wollen wir uns im Folgenden noch etwas genauer anschauen. 

Zur Unterdrückung von unerwünschten Mischprodukten – aber auch der Oberwellen – wird nach Mischern häufig ein Bandpassfilter eingesetzt. Besonders bei Einbandsendern sowie bei Geräten für den VHF-, UHF- und SHF-Bereich kommen statt klassischer Oberwellen-Tiefpässe nämlich Bandpässe zum Einsatz. Bei diesen Funkgeräten müssen oft auch Signalanteile unterdrückt werden, die bereits innerhalb der Aufbereitung des Sendesignals entstehen und sich sogar unterhalb der eigentlichen Sendefrequenz befinden können.

[question:AJ211]
[question:AJ209]
[question:AJ208]

Unerwünschte Aussendungen können auch in unmittelbarer Nähe zum Sendesignal vorliegen. Diese sind durch den Einsatz von Filtern nur schwer oder gar nicht zu unterdrücken und sollten daher bereits zu Beginn der Signalaufbereitung durch entsprechende Maßnahmen wirksam unterdrückt werden. Häufig entstehen solche *Nebenaussendungen*, oder auch *Nebenprodukte* genannt (umgangssprachlich auch als "Splatter" bezeichnet), welche das Sendesignal ungewollt verbreitern, durch eine zu hohe Einstellung des Mikrofonverstärkers eines Senders. Hierdurch wird das NF-Signal verzerrt, was unerwünschte Nebenaussendungen zur Folge hat. Abbildung [ref:a_harmonische] zeigt die Nebenaussendungen. 

[question:AJ219]

Auch durch eine nicht ausreichend stabilierte Versorgungsspannung von Senderendstufen können unerwünschte Aussendungen entstehen. Hierbei kann beispielsweise ein schlecht gefiltertes oder stabilisiertes Netzteil (mit Brummspannung behaftet) auf der Versorgungsspannungsseite zu AM-Aussendungen der Endstufe führen. Auch Einstreuungen von NF-Signalen auf der Netzversorgungsseite eines Senders können zu entsprechenden AM-Aussendungen führen. Dies ist oft bei CW-Aussendungen als "verbrummter" Träger/Ton wahrzunehmen, insbesondere bei älteren Sendern.

[question:AJ222]
[question:AJ223]
