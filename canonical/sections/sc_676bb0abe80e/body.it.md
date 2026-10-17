Un oscilloscopio è un voltmetro che può visualizzare l’andamento temporale delle tensioni. Come altri voltmetri, gli oscilloscopi hanno un’elevata resistenza interna. Spesso è possibile misurare due o più tensioni contemporaneamente. L’apparecchio mostrato in figura [ref:e_oszilloskop_digital], ad esempio, è impostato in modo che due segnali condividano lo schermo.

<margin>
[photo:212:e_oszilloskop_digital: Oscilloscopio con numerose funzioni aggiuntive]
</margin>

Analizziamo ora più in dettaglio la visualizzazione dell’oscilloscopio nella figura [ref:e_oszilloskop_bildschirmfoto_sinus]. Con un oscilloscopio è possibile determinare, ad esempio, i parametri caratteristici di una tensione alternata sinusoidale (T, Ū, U<sub>SS</sub> e U<sub>eff</sub>). Oltre all’andamento del segnale, vengono visualizzate anche le indicazioni di tempo e tensione – nell’esempio 50,0 ns e 500 mV. Ciò significa che una casella in direzione orizzontale corrisponde a 50 nanosecondi e in direzione verticale a 500 millivolt. Queste caselle sono spesso chiamate divisioni o divisioni della scala, da cui anche la notazione 500 mV/div.

<margin>
[photo:214:e_oszilloskop_bildschirmfoto_sinus: Una tensione sinusoidale visualizzata su un oscilloscopio digitale]
</margin>

---

Possiamo immaginarlo come un sistema di coordinate e leggere la durata del periodo (T) e l’ampiezza (Ū). Nell’esempio, un periodo è lungo 5 caselle o divisioni della scala. Moltiplicando per 50,0 ns per divisione della scala si ottiene la durata del periodo di 250,0 ns. L’ampiezza, cioè la massima deviazione dalla posizione zero, è di 1500 mV o 1,5 V, poiché è alta 3 divisioni della scala e ogni divisione corrisponde a 500 mV.

[question:EI301]

<tip>
Per misurazioni semplici, molti oscilloscopi digitali dispongono di un tasto AUTO. Premendolo, alcune impostazioni vengono regolate automaticamente e di solito appare un’immagine stabile dei segnali applicati. La visualizzazione può essere spostata orizzontalmente. Un pulsante di regolazione con questa funzione è spesso etichettato come posizione X. Per leggere la durata del periodo, si sposta un punto caratteristico come un passaggio per lo zero su una linea verticale della griglia e si contano le divisioni della scala corrispondenti a un periodo.
</tip>

---

Non appena si conosce la durata del periodo di un’oscillazione, è possibile determinare anche la frequenza. Nel corso N abbiamo già imparato la relazione qualitativa: la frequenza indica il numero di oscillazioni al secondo. Se la durata del periodo è di un secondo, si ottiene una frequenza di 1 Hz. Se dimezziamo la durata del periodo a mezzo secondo, due oscillazioni si adattano a un secondo – la frequenza è allora di 2 Hz.

Nel corso E consideriamo ora questa relazione come formula:

f = 1/T oppure T = 1/f

La frequenza in hertz è il reciproco della durata del periodo in secondi.

Il segnale nella figura [ref:e_oszilloskop_bildschirmfoto_sinus] ha quindi la frequenza

f = 1/250 ns = 4 MHz.

[question:EB408]
[question:EB409]
[question:EB411]
[question:EB410]
[question:EI302]

---

A volte i segnali vengono deformati involontariamente. Questo accade, ad esempio, quando in un amplificatore viene immessa una tensione d’ingresso troppo elevata. In tal caso si dice che l’amplificatore è sovramodulato e il suo segnale di uscita risulta distorto. Distorsioni marcate come quella mostrata nella figura [ref:e_oszilloskop_verzerrt] possono essere rilevate con un oscilloscopio. Per la valutazione dei segnali audio nel radioamatoriale questo di solito è sufficiente.

<margin>
[photo:215:e_oszilloskop_verzerrt: Segnale d’ingresso sinusoidale (in alto) e segnale di uscita distorto di un amplificatore sovramodulato]
</margin>

<indepth>
Se un segnale ad alta frequenza è privo di distorsioni che potrebbero compromettere altre bande di frequenza, non è possibile valutarlo adeguatamente con un oscilloscopio. Per questo scopo, lo strumento di misura corretto è un analizzatore di spettro.
</indepth>

% EI304 Distorsioni BF
[question:EI304]