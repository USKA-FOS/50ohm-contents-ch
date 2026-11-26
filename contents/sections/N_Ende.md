Diese Seite wird vorläufig für die Bearbeiter missbraucht als Sandkasten, wenn etwas simuliert werden muss (Bsp wenn etwas nicht funktioniert) und dient auch als "Vorlagen-Container" um wiederkehrende Sachen (wie bsp die farbigen Boxen in der rechten Spalte) mit Copy&Paste im Markdown holen zu können.
Der Originalinhalt ist noch immer hier drin, weil bisher unklar ist ob der noch gebraucht wird.

**Wenn Du Kursteilnehmer bist, überspringe bitte diese internen Informationen und scrolle nach unten bis zur Stelle "AB HIER ORIGINALTEXT".**


**Vorlagen**
<margin>
hier sind alle die verschiedenen Boxen als Vorlage
</margin>

<indepth>
Das ist ein Mustertext mit dem Kommando (indepth). Das generiert den grauen Kasten „Vertiefung“.
</indepth>

<tip>
Das ist ein Mustertext mit dem Kommando (tip). Das generiert den roten Kasten „Tipp“.
</tip>

<attention>
Das ist ein Mustertext mit dem Kommando (attention). Das generiert den gelben Kasten „Achtung“.
</attention>

<danger>
Das ist ein Mustertext mit dem Kommando (danger). Das generiert den roten Kasten „Gefahr“.
</danger>

<unit>
Das ist ein Mustertext mit dem Kommando (unit). Das generiert den grünen Kasten „Neue Einheit“.
</unit>

<law>
Das ist ein Mustertext mit dem Kommando (law). Das generiert den blauen Kasten «Gesetzliche Grundlage».
Dieser wird verwendet für Ausführungen von oder Links zu Gesetzen, Verordnungen, RR, CEPT, Merkblatt BAKOM, etc.
[angezeigter Text](Direktlink zur Zielseite)

[Merkblatt Amateurfunk](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk)
</law>


<margin>
Externer Link
So macht man einen Direktlink auf eine externe Seite [angezeigter Text](Direktlink zur Zielseite)
</margin>



**Interne Verlinkung**

Das ist ein Test für eine interne Verlinkung zu einem anderen Abschnitt innerhalb von der 50Ohm-Webseite. - Das ist so wie es sein soll  - 
Das ist zu benutzen, wenn bspw. im Text steht "Das haben wir bereits im Abschnitt [sec:rufzeichen] behandelt".

Dieser Test ist für die fehlerhafte Verlinkung.  - Das ist okay so. Das muss der Editor/Reviewer bereits merken und korrigieren. - 
Wenn man den Namen der Section gross [sec:Rufzeichen] oder mit dem Zusatz NE_ [sec:NE_rufzeichen] oder mit der Endung .md [sec:rufzeichen.md] oder .html [sec:rufzeichen.html] oder sonstirgendwie fehlerhaft schreibt.

Dieser Test ist für die kursübergreifende Verlinkung. - 

Bspw wenn man "im Abschnitt [sec:kondensator_2] wird da noch tiefer darauf eingegangen." schreiben will (Verweis auf eine HB9 Section in der HB3 Edition.)

Bspw wenn man "wie wir im Abschnitt [sec:kondensator_2] schon gelernt haben." schreiben will. (Verweis auf eine HB3 Section in der HB9 Upgrade Edition.)



**Anführungszeichen**
Das ist ein "Test" zur Verwendung von Anführungszeichen. Dies Anführungszeichen wurden mit CTRL+2 erstellt.
Das ist ein Versuch <<Guilements>> (Guilements) zu erstellen. Dies mit der doppelten Nutzung der Grösser/kleiner Zeichen auf der Tastatur.



**Testreihe für Formel**
Es geht hier um Tests warum das gewisse Formeln NICHT zentriert in Serif sonder linksbündig in SansSerif ausgegeben werden.

*Tests ARK*

Original ab Problemseite https://50ohm.uska.ch/50ohm_review_de/NEA_spitze_effektiv_wert.html  (6.13)

$U_{eff} = \frac{\hat{U}}{\sqrt{2}}$ oder $\hat{U} = U_{eff} \cdot \sqrt{2}$

$ \hat{U} = \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{325}{\volt}$

$ U_\text{SS} = 2 \cdot \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{651}{\volt}$


Test mit dritter Formel in einem Satz eingebettet:

Die Spitze-Spitze-Spannung beträgt $U_\text{SS} = 2 \cdot \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{651}{\volt}$ bei einer sinusförmigen Netzspannung.


Noch ein Test:
Jede Formel auf eigener Zeile

$U_\text{SS} = 2 \cdot 230 \cdot \sqrt{2} \approx 651$

$A = 2 \cdot 230 \cdot \sqrt{2} \approx 651$

$U_{eff} = \frac{\hat{U}}{\sqrt{2}}$

---

Test mit geänderter Formel
$$ statt $ mit Formel auf eigener Zeile (was eigentlich echtes Latex wäre gemäss FRV). Zudem mit qquad als Abstand und \text für das "oder"

$$
U_\text{eff} = \frac{\hat{U}}{\sqrt{2}}
\qquad \text{oder} \qquad
\hat{U} = U_\text{eff} \cdot \sqrt{2}
$$

---

$$
\hat{U} = \qty{230}{\volt} \cdot \sqrt{2}
\approx \qty{325}{\volt}
$$

---

und weiter geht's 

$$
U_\text{SS} = 2 \cdot \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{651}{\volt}
$$

$$ funktioniert offenbar nicht, deshalb neuer Versuch YPA mit $ und alles auf einer Zeile.

Zeile 108-112 in einer freistehenden Zeile mit $$

$$ U_\text{eff} = \frac{\hat{U}}{\sqrt{2}}\qquad \text{oder} \qquad\hat{U} = U_\text{eff} \cdot \sqrt{2}$$

Zeile 108-112 in einer Zeile mit $ aber ohne Leerzeile
$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}}\qquad \text{oder} \qquad\hat{U} = U_\text{eff} \cdot \sqrt{2}$

Simulation für Formeln im Fliestext:

Bei sinusförmigen Spannungen ist der Spitzen- oder Scheitelwert etwa 1,4-mal so groß wie der Effektivwert (siehe Abbildung [ref:e_wechselspannung_kenngroessen]). Die genaue Rechnung führt zu einer einfachen Formel: $U_{eff} = \frac{\hat{U}}{\sqrt{2}}$ oder $\hat{U} = U_{eff} \cdot \sqrt{2}$

Wird eine Wechselspannung nur mit dem Buchstaben $U$ ohne Zusatz angegeben, ist in der Regel der Effektivwert gemeint. Das bekannteste Beispiel ist unsere Netzspannung von $\qty{230}{\volt}$ – auch hierbei handelt es sich um den Effektivwert. Die Spitzenspannung liegt deutlich höher, nämlich bei: $ \hat{U} = \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{325}{\volt}$.


---
<unit>
Formeln sollen nicht in Sanserif ausgegeben werden. Spannend ist aber dass diese hier trotz Fehlformatierung mit $$ statt $ zentriert wird. (wobei zentriert ist sie nicht wirklich, es ist eher so 1/3 Einzug als wirklich 1/2)
  
$$\qty{1}{\hertz} = \frac{1}{\unit{\second}}$$
  
</unit>

<unit>
hier dann statt $$ mit $. Dann wirds serif, aber der Einzug bleibt bei 1/3 
  
$\qty{1}{\hertz} = \frac{1}{\unit{\second}}$
  
</unit>

<margin>
das ist der Test ob Formeln in rechter Spalte die nicht in einer Box sind richtig zentriert (1/2) werden
oben mit 1 Dollar unten mit 2 Dollar

Nachtrag: offenbar liegt es nicht an der Box. 
  
$\qty{1}{\hertz} = \frac{1}{\unit{\second}}$

$$\qty{1}{\hertz} = \frac{1}{\unit{\second}}$$

</margin>

Das ist der Test ob $$ links korrekt ausgeben wird

$$\qty{1}{\hertz} = \frac{1}{\unit{\second}}$$

Das ist der Test ob $ links korrekt ausgeben wird

$\qty{1}{\hertz} = \frac{1}{\unit{\second}}$

---

**Erkenntnisse:**

1.

Formeln müssen **alleine** heisst **einzeln** in einer Zeile stehen.
Es dürfen keine andern Zeichen in derselben Zeile stehen. Kein "und", "oder", Satzzeichen, etc.
Zudem muss es vor und nach der Formel eine Leerzeile haben.

Ergo
Wenn zwei Formeln gelten die bspw. mit  "und" verbunden werden sollen, müssen diese auf zwei eigenen Zeilen stehen und dazwischen jeweils Leerzeilen.
Wenn die auf einer Zeile stehen sollen mit dem Wort dazwischen muss das mit $formel1 \quad \text{oder} \quad formel2£ gelöst werden  (damit die Schreibweise sichtbar wird, wurde das Dollar durch £ ersetzt. £ durch Dollar ersetzen, dann wird die Formel als Formel ausgegeben.)

2. ein oder 2 Dollar
2 Dollar wäre echtes Latex für abgesetze (Serif und zentriert) Formeln. Eines für inline -Formeln
Zwei funktioniert aber hier überhaupt nicht. 
$formel$ führt zum gewünschten Ergebnis (Serif und zentriert)

**Vorläufiges Ende Erkenntnisse**



**Original aus 6.28/132**
das ist eine Formel die in 3 Zeilen ausgegeben wird aber sehr zusammengequetsch wird. Es ist eine "Formel umstellen"- Formel

$\begin{split} g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right)\\ g &= 10 \cdot 2 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \\ g &= 20 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \end{split}$

Lösungansatz für mehr Leerraum zwischen den Formeln: Auflösung in 3 Formeln aber auf einer Zeile (durch $ vor und nach den Teilformeln) - dürfte nicht funktionieren

$g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right)\\$ $g &= 10 \cdot 2 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \\$   g &= 20 \cdot \log_{10}\left(\frac{U_1}{U_2}\right)$

Auflösung in 3 Formeln wie gewohnt untereinander - ohne Leerzeile (dürfte nicht funktionieren)

$g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right)\\$ 
$g &= 10 \cdot 2 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \\$   
$g &= 20 \cdot \log_{10}\left(\frac{U_1}{U_2}\right)$


Auflösung in 3 Formeln wie gewohnt untereinander - mit Leerzeile (müsste funktioniern, funktioniert aber nicht)

$g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right)\\$ 

$g &= 10 \cdot 2 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \\$   

$g &= 20 \cdot \log_{10}\left(\frac{U_1}{U_2}\right)$


---
AB

HIER

ORIGINALTEXT
% ARK: TODO: Photo des Schweizer 50Ohm-Teams erstellen und einbauen

---

<margin>
[photo:329:n_team:50ohm.de-Team]
[photo:1009:n_team:Symbolbild als Platzhalter für das 50ohm.ch-Team]
</margin>
   
**AB HIER ORIGINALTEXT - BITTE STEHEN LASSEN**

Gratulation! Du hast den Kurs nun erfolgreich abgeschlossen. Falls noch nicht geschehen, solltest du dich jetzt gezielt mit einer Lern-App oder einem Prüfungstrainer auf die Amateurfunkprüfung vorbereiten. Dafür eignet sich z. B. der [Hamradiotrainer](http://www.hamradiotrainer.de/)), bei dem man die für die Schweiz geeigneten Fragen laden kann. Auch die Anmeldung zur Prüfung solltest du möglichst zeitnah vornehmen, da die verfügbaren Termine häufig begrenzt sind. Alle wichtigen Informationen zur Anmeldung und zum Ablauf der Prüfung findest du auf der [BAKOM-Webseite](https://www.bakom.admin.ch/de/amateurfunk). Nach bestandener Prüfung beim BAKOM kannst du anschließend dein persönliches Rufzeichen beantragen und offiziell am Amateurfunkbetrieb teilnehmen.

Dieser Kurs wurde dir kostenlos von der USKA zur Verfügung gestellt und von vielen ehrenamtlichen [Mitarbeiterinnen und Mitarbeitern des DARC erarbeitet](https://50ohm.de/infos.html#contributors) und von ehrenamtlichen [Mitarbeiterinnen und Mitarbeitern der USKA und der IGAFuA](https://50ohm.uska.ch/infos.html#contributors) an die Schweizer Verhältnisse angepasst und in drei Landessprachen verfügbar gemacht. Die USKA ist die Schweizer Amateurfunk-Organisation und vertritt die Interessen der Funkamateurinnen und Funkamateure gegenüber Behörden, Politik und anderen Funkdiensten. Eine [Mitgliedschaft in der USKA](https://uska.ch/de/uska-beitreten/) bedeutet, diese Arbeit aktiv mitzutragen: von Ausbildung und Nachwuchsförderung über technische Entwicklung bis hin zur Sicherung unserer Frequenzen und Betriebsarten. Wer Amateurfunk langfristig erhalten und weiterentwickeln möchte, findet in der USKA die gemeinsame organisatorische Basis dafür. Wir würden uns freuen, wenn du dich in Zukunft in unserem Verein engagierst und gemeinsam mit uns die Community voranbringst.

Am einfachsten findest du Kontakt zu anderen Funkamateuren in deiner Nähe, indem du nach einer USKA Sektion suchst. Auf dieser
[Seite](https://uska.ch/de/funkamateure/die-uska/sektionen/) kannst du die nächstgelegene USKA Sektion (Ortsgruppe) finden. Die Mitglieder vor Ort können dir den Einstieg ins Hobby erleichtern und viele praktische Fragen beantworten. Geh doch einfach einmal an einen Stamm oder Höck einer nahegelegenen USKA-Sektion!

Sobald du deine Prüfung geschafft hast, eröffnet sich eine Vielzahl spannender Spielfelder, in denen du dich austoben kannst. Von Contesten über Selbstbau, Notfunk oder Portabel- und Outdoorfunk – um nur einige zu nennen – gibt es zahlreiche Aktivitäten, mit denen du dich als frisch gebackene Funkamateurin oder Funkamateur beschäftigen kannst. Dabei gilt oft die Devise: *Nach der Prüfung ist vor der Prüfung*, denn es gibt noch sehr viel zu entdecken und zu lernen, weit über den reinen Prüfungsstoff hinaus. Die USKA und die USKA-Sektionen unterstützen Dich dabei auch durch verschiedene Weiterbildungs- und Austauschformate, wie zum Beispiel Vorträge, Kurse und Contest Durchführungen. Darüber hinaus bieten Veranstaltungen wie die *HAM RADIO* in Friedrichshafen am Bodensee mit über 13'000 (im Jahr 2026) gleichgesinnten Besucherinnen und Besuchern oder die Surplus Party in Zofingen hervorragende Möglichkeiten zum persönlichen Austausch und zum Kennenlernen der Amateurfunk-Community. Eine weitere schöne Gelegenheit, viele Funkamateur zu treffen, ist das USKA HAMFEST.

Viel Spaß mit deinem neuen Hobby wünschen stellvertretend für das *50ohm.ch-Team*  

Sandy, HB3YPA und Mathias, HB9FRV
