Un oscilloscopio è un <i>voltmetro</i> che può visualizzare l’andamento temporale delle tensioni. Come altri <i>voltmetri</i>, gli oscilloscopi hanno un’elevata resistenza interna. Spesso è possibile misurare due o più tensioni contemporaneamente. L’apparecchio mostrato in figura [ref:e_oszilloskop_digital], ad esempio, è impostato in modo che due segnali condividano lo schermo.

<margin>
[photo:212:e_oszilloskop_digital: Oscilloscopio con numerose funzioni aggiuntive]
</margin>

Analizziamo ora più in dettaglio la visualizzazione dell’oscilloscopio nella figura [ref:e_oszilloskop_bildschirmfoto_sinus]. Con un oscilloscopio è possibile determinare, ad esempio, i parametri caratteristici di una tensione alternata sinusoidale (<i>T</i>, <i>Ū</i>, <i>U<sub>SS</sub></i> e <i>U<sub>eff</sub></i>). Oltre all’andamento del segnale, vengono visualizzate anche le indicazioni di tempo e tensione – nell’esempio <i>50,0 ns</i> e <i>500 mV</i>. Ciò significa che una casella in direzione orizzontale corrisponde a 50 nanosecondi e in direzione verticale a 500 millivolt. Queste caselle sono spesso chiamate divisioni o divisioni della scala, da cui anche la notazione <i>500 mV/div</i>.

<margin>
[photo:214:e_oszilloskop_bildschirmfoto_sinus: Una tensione sinusoidale visualizzata su un oscilloscopio digitale]
</margin>

---

Possiamo immaginarlo come un sistema di coordinate e leggere la <i>durata del periodo</i> (<i>T</i>) e l’<i>ampiezza</i> (<i>Ū</i>). Nell’esempio, un periodo è lungo 5 caselle o divisioni della scala. Moltiplicando per <i>50,0 ns</i> per divisione della scala si ottiene la <i>durata del periodo</i> di <i>250,0 ns</i>. L’ampiezza, cioè la massima deviazione dalla posizione zero, è di <i>1500 mV</i> o <i>1,5 V</i>, poiché è alta 3 divisioni della scala e ogni divisione corrisponde a <i>500 mV</i>.

[question:EI301]

<tip>
Per misurazioni semplici, molti oscilloscopi digitali dispongono di un tasto AUTO. Premendolo, alcune impostazioni vengono regolate automaticamente e di solito appare un’immagine stabile dei segnali applicati. La visualizzazione può essere spostata orizzontalmente. Un pulsante di regolazione con questa funzione è spesso etichettato come "posizione X". Per leggere la <i>durata del periodo</i>, si sposta un punto caratteristico come un passaggio per lo zero su una linea verticale della griglia e si contano le divisioni della scala corrispondenti a un periodo.
</tip>

---

Non appena si conosce la <i>durata del periodo</i> di un’oscillazione, è possibile determinare anche la frequenza. Nel corso N abbiamo già imparato la relazione qualitativa: la frequenza indica il numero di oscillazioni al secondo. Se la <i>durata del periodo</i> è di un secondo, si ottiene una frequenza di <i>1 Hz</i>. Se dimezziamo la <i>durata del periodo</i> a mezzo secondo, due oscillazioni si adattano a un secondo – la frequenza è allora di <i>2 Hz</i>.

Nel corso E consideriamo ora questa relazione come formula:

<i>f</i> = <i>1</i>/<i>T</i> oppure <i>T</i> = <i>1</i>/<i>f</i>

La frequenza in hertz è il reciproco della <i>durata del periodo</i> in secondi.

Il segnale nella figura [ref:e_oszilloskop_bildschirmfoto_sinus] ha quindi la frequenza

<i>f</i> = <i>1</i>/<i>250 ns</i> = <i>4 MHz</i>.

[question:EB408]
[question:EB409]
[question:EB411]
[question:EB410]
[question:EI302]

---

A volte i segnali vengono deformati involontariamente. Questo accade, ad esempio, quando in un amplificatore viene immessa una tensione d’ingresso troppo elevata. In tal caso si dice che l’amplificatore è <i>sovramodulato</i> e il suo segnale di uscita risulta distorto. Distorsioni marcate come quella mostrata nella figura [ref:e_oszilloskop_verzerrt] possono essere rilevate con un oscilloscopio. Per la valutazione dei segnali audio nel <i>radioamatoriale</i> questo di solito è sufficiente.

<margin>
[photo:215:e_oszilloskop_verzerrt: Segnale d’ingresso sinusoidale (in alto) e segnale di uscita distorto di un amplificatore sovramodulato]
</margin>

<indepth>
Se un segnale ad alta frequenza è privo di distorsioni che potrebbero compromettere altre bande di frequenza, non è possibile valutarlo adeguatamente con un oscilloscopio. Per questo scopo, lo strumento di misura corretto è un analizzatore di spettro.
</indepth>

% EI304 Distorsioni BF
[question:EI304]