Die *Automatic-Level-Control (ALC)* regelt die Aussteuerung der Senderendstufe des Funkgerätes und reduziert bei deren Übersteuerung die Amplitude des Signals im Sendezweig. Hierbei ist die ALC nicht zu verwechseln mit der AGC (Automatic-Gain-Control), welche sich im Empfängerzweig befindet (siehe Abbildung [ref:e_alc]).

<margin>
[picture:914:e_alc:Automatic-Level-Control in einem Sender]
</margin>

Die ALC erfasst die Ausgangsleistung der Senderendstufe und vergleicht diese mit einem vorgegebenen maximalen Wert. Bei Überschreiten dieses Grenzwertes gibt die ALC eine entsprechende Regelspannung an die vorgelagerte HF-Verstärkerstufe im Sendezweig und reduziert damit die Amplitude des Sendesignals.

Solange die ALC-Anzeige nicht anspricht, kann davon ausgegangen werden, dass die Regelung nicht eingreift und der Sender nicht durch ein zu starkes NF-Signal übersteuert wird. Sobald die ALC Anzeige reagiert, kann davon ausgegangen werden, dass die Regelung, zumindest teilweise, aktiv wird.

Bei SSB-Aussendungen ist ein geringfügiges Ansprechen der ALC durchaus erwünscht, da hierdurch Lautstärkeschwankungen der Stimme ausgeglichen werden und eine optimale Nutzung der verfügbaren Sendeleistung stattfindet. Viele Transceiver besitzen eine entsprechende ALC-Anzeige, auf der meist ersichtlich ist, bis zu welchem Grad die ALC reagieren kann (grüner Bereich) und ab welchem Bereich eine zu starke Aussteuerung stattfindet, die die ALC nicht mehr verzerrungsfrei kompensieren kann (roter Bereich).

<margin>
[picture:915:e_alc_trx:ALC im Display eines Funkgeräts]
</margin>

<tip>
Praktisch kann man den optimalen Punkt, an dem die ALC grade noch nicht aussteuert durch langsames Erhöhen der NF-Aussteuerung bis zu dem Punkt, an dem die ALC anspricht finden. Im Anschluss dreht man die NF-Aussteuerung wieder etwas zurück, so dass die ALC grade nicht mehr anspricht und die Sendeleistungs-Anzeige noch die gewünschte Ausgangsleistung anzeigt (evtl. etwas weniger).
</tip>

---

Bei Aussendungen mit digitalen Übertragungsverfahren wie z. B. FT8 oder WSPR ist das Ansprechen der ALC oft ein Hinweis darauf, dass das Audiosignal vom PC zu stark ist und übersteuert wird. Das kann zu unerwünschtem *Splatter* auf dem Band führen. Deshalb sollte das Audiosignal bei diesen Übertragungsverfahren stets sorgfältig kontrolliert werden.

<indepth>
Das [Handbuch](https://wsjt.sourceforge.io/wsjtx-main_en.html#TRANSCEIVER)) der Software WSJTX gibt hierzu eine gute Empfehlung: Im ersten Schritt sollte man durch Drücken der TUNE-Taste den Transceiver in den Sendemodus schalten, um einen gleichmäßigen Ton zu erzeugen. Dieser Ton lässt sich mit der Monitor-Funktion des Geräts durch Hören überprüfen oder im Wasserfall des TRX optisch kontrollieren. Dabei sollten keine Verzerrungen, Klicks oder andere Störungen auftreten. Anschließend stellt man den PWR-Regler von seinem Maximum langsam nach unten, bis der HF-Ausgang des Senders leicht abfällt – dies gilt allgemein als gutes Niveau für die Audioaussteuerung. Auch die ALC-Anzeige sowie die Ausgangsleistung des Transceivers können dabei helfen, den optimalen NF-Signalpegel zu finden.
</indepth>

[question:EF305]
