Funkgeräte müssen manchmal neu abgeglichen werden, zum Beispiel nach Reparaturen oder wenn sich Bauteile durch Alterung verändert haben. Bei Empfängern gehört zum Abgleich die Kontrolle der Oszillatorfrequenzen. Dafür verwendet man üblicherweise einen Frequenzzähler.

[question:EI501]

Abbildung [ref:e_frequenzzaehler1] zeigt das Display eines Frequenzzählers. Die abgesetzte Drei ganz rechts steht wie bei manchen Taschenrechnern für $\num{10^3}$. Also misst der Zähler die Frequenz $\qty{455}\cdot \qty{10^3}{\hertz}$ oder $\qty{455}{\kilo\hertz}$. Neuere Messgeräte zeigen statt der Zehnerpotenz den Einheitenvorsatz direkt an.

<margin>
[photo:187:e_frequenzzaehler1:Display eines Frequenzzählers, der $\qty{455}\cdot \qty{10^3}{\hertz}$ anzeigt]
</margin>

% Ich hab das mal aus Platzgründen entfernt
%<margin> 
%[photo:189:e_frequenzzaehler2:Multimeter, das im Frequenzmessbereich $\qty{455}{\kilo\hertz}$ anzeigt. Darüber erscheinen ein Symbol für niedrige %Batteriespannung, die Luftfeuchtigkeit und die Temperatur. Diese Werte haben nichts mit der Frequenzmessung zu tun.]
%</margin>

<indepth>
Die Frequenz $\qty{455}{\kilo\hertz}$ kommt häufig als Zwischenfrequenz von Überlagerungsempfängern vor und kann gemessen werden, wenn der Empfänger auf ein starkes Signal abgestimmt ist.
</indepth>

---

In Abgleichanleitungen wird oft verlangt, eine Frequenz bis auf eine bestimmte Abweichung genau einzustellen, zum Beispiel $\pm\qty{10}{\hertz}$. In solchen Fällen ist es hilfreich, sich den Stellenwert der einzelnen Ziffern vor Augen zu führen. Die vom Messgerät angezeigte Zehnerpotenz, also bei $\qty{455}{\kilo\hertz}$ der Wert $\num{10^3}$ oder $\num{1000}$, gilt immer für die Stelle direkt vor dem Komma. Die Stelle links davon steht dann für $\qty{10}{\kilo\hertz}$ oder $\qty{10^4}{\hertz}$ und die Stelle noch eins weiter links, im Beispiel die Vier, für $\qty{100}{\kilo\hertz}$ oder $\qty{10^5}{\hertz}$. Nach rechts geht es in die andere Richtung.

 In Abbildung [ref:e_frequenzzaehler_stellen] sehen wir ein Beispiel mit einer höheren Frequenz.
  
<margin>
[picture:793:e_frequenzzaehler_stellen:Diese Anzeige stellt eine Frequenz in $\unit{\mega\hertz}$ dar. Das ist zugleich der Stellenwert der Ziffer vor dem Komma.]
</margin>

<attention>
Eingänge von Frequenzzählern können einen hohen Innenwiderstand haben. Das kennen wir von Spannungsmessern und Oszilloskopen. Es kommen aber auch Anschlüsse mit $\qty{50}{\ohm}$ vor. Sie sind meistens besonders empfindlich und der in der Bedienungsanleitung des Zählers angegebene Höchstwert für Spannung oder Leistung darf keinesfalls überschritten werden.
</attention>

[question:EI502]
[question:EI503]

Frequenzzähler werden für einen bestimmten Wertebereich gebaut, zum Beispiel $\qty{100}{\kilo\hertz}$ bis $\qty{2}{\giga\hertz}$. Außerhalb dieses Bereichs messen sie ungenau oder gar nicht. Zum Messen höherer Frequenzen gibt es Frequenzteiler. Sie teilen die Frequenz eines Signals, das man an ihren Eingang anlegt, durch einen festen Wert und geben das Ergebnis als elektrische Schwingung am Ausgang aus. Man nennt sie auch Vorteiler, weil sie zwischen Messobjekt und Zähler geschaltet werden.

%TODO Bild Frequenzteiler

Häufig teilen Vorteiler die Frequenz durch zehn. Wenn man an den Eingang so eines 10:1-Teilers $\qty{2,4}{\giga\hertz}$ anlegt, zeigt der Frequenzzähler dahinter $\qty{240}{\mega\hertz}$ an.

[question:EI504]