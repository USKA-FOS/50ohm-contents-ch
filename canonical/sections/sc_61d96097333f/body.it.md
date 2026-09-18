Le antenne multibanda, che sono sintonizzate in modo mirato su più bande, le abbiamo già conosciute, ad esempio l'antenna alimentata in estremità con trasformatore 1:49. Torniamo al nostro esempio della sezione "Alimentazione in corrente e tensione II": un dipolo a semionda alimentato al centro può essere sintonizzato, oltre che sulla sua frequenza fondamentale, anche su multipli dispari di questa frequenza. Ad esempio, un dipolo progettato per la banda degli 80 metri con una frequenza fondamentale di 3,5 MHz presenta ulteriori risonanze approssimativamente a 10,5 MHz e 17,5 MHz.

A multipli pari della frequenza fondamentale, ad esempio a 7 MHz o 14 MHz, nel punto di alimentazione centrale si ha invece un minimo di corrente e quindi un'alta impedenza. Queste frequenze non sono quindi utilizzabili senza ulteriori accorgimenti in un semplice dipolo alimentato al centro. Un modo per creare risonanze aggiuntive su queste frequenze è rappresentato dal cosiddetto *dipolo a circuito trappola*, anche noto come *dipolo con trappole*.

In un dipolo a circuito trappola, in ciascuna semionda del dipolo è presente almeno un circuito oscillante parallelo composto da una bobina e un condensatore. Un tale circuito oscillante viene chiamato *trappola* (dall'inglese *trap*). Un circuito oscillante parallelo è altamente resistivo alla sua frequenza di risonanza (cfr. figura [ref:a_sperrkreis]). Agisce quindi come *circuito trappola* e impedisce in gran parte che la corrente fluisca nella parte più esterna del dipolo. In questo modo, lo stesso dipolo può avere lunghezze elettriche diverse su più bande di frequenza.

<margin>
[immagine:1036:a_sperrkreis:Risposta in frequenza qualitativa di un circuito oscillante parallelo (circuito trappola)]
</margin>

[domanda:AG109]
[domanda:AG110]

---

L'effetto di una trappola sul dipolo dipende da come la frequenza operativa si rapporta alla sua frequenza di risonanza $f_\mathrm{res}$.

* Quando $f=f_\mathrm{res}$, il circuito oscillante parallelo è altamente resistivo e agisce come circuito trappola. La parte esterna del dipolo viene così separata in gran parte da quella interna.
* Quando $f<f_\mathrm{res}$, prevale l'effetto induttivo della trappola. Essa agisce in modo simile a una bobina di allungamento e allunga elettricamente il radiatore.
* Quando $f>f_\mathrm{res}$, prevale l'effetto capacitivo della trappola. Il radiatore viene così leggermente accorciato elettricamente.

<margin>
In questa applet è possibile esaminare l'effetto di una trappola su un dipolo per diverse frequenze:

[include:applet_traps]
</margin>

Particolarmente chiaro è inizialmente il caso di risonanza. Se il dipolo viene utilizzato alla frequenza di risonanza della trappola (ad esempio 7,05 MHz nell'immagine), il circuito oscillante parallelo è altamente resistivo. Quindi scorre poca corrente nella parte esterna del dipolo. Il dipolo si comporta approssimativamente come se terminasse nella posizione della trappola.

[domanda:AG112]

Questa relazione può essere sfruttata per la progettazione di un dipolo a due bande. Per la banda a frequenza più alta, la distanza tra le due trappole determina in gran parte la lunghezza efficace del dipolo. A questa frequenza, i tratti di filo esterni vengono in gran parte isolati dall'effetto trappola, come se non ci fossero, e il dipolo si comporta come un dipolo più corto.

[domanda:AG116]

---

Se invece il dipolo viene utilizzato a una frequenza *inferiore* alla frequenza di risonanza della trappola (ad esempio 3,5 MHz nell'immagine), il circuito oscillante non è più altamente resistivo. Il suo effetto induttivo prevale. La trappola agisce quindi in modo simile a una bobina di allungamento e allunga elettricamente il dipolo. In questo modo, l'intero dipolo, comprese le parti esterne di filo, può essere utilizzato per una banda a frequenza più bassa.

[domanda:AG111]

---

A una frequenza *superiore* alla frequenza di risonanza, prevale invece l'effetto capacitivo della trappola. La trappola agisce quindi come un accorciatore elettrico e può essere sintonizzata, ad esempio, sulla frequenza di 14 MHz. Anche questo effetto deve essere considerato nella progettazione di un dipolo a circuito trappola.

[domanda:AG113]

---

Con più coppie di trappole è possibile realizzare dipoli per ancora più bande di frequenza. Le trappole per le frequenze più alte sono posizionate più all'interno, poiché in questo caso è necessaria la lunghezza efficace più corta del dipolo.

La trappola più interna viene quindi sintonizzata sulla frequenza più alta prevista. La coppia di trappole successiva, più esterna, viene sintonizzata sulla frequenza immediatamente inferiore e così via. Più bassa è la frequenza operativa, più grandi sono le parti del dipolo che diventano operative.

[domanda:AG115]
[domanda:AG114]

Le trappole non vengono utilizzate solo nelle antenne dipolo. Anche nelle antenne direttive come le antenne Yagi, i circuiti trappola possono essere impiegati negli elementi individuali per rendere l'antenna utilizzabile su più bande di frequenza.