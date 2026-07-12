Un oscilloscopio è uno strumento di misura della tensione che può visualizzare l'andamento temporale delle tensioni. Come altri strumenti di misura della tensione, gli oscilloscopi hanno un'elevata resistenza interna. Di solito è possibile misurare contemporaneamente due o più tensioni. L'apparecchio nella figura [ref:e_oszilloskop_digital] è impostato, ad esempio, in modo che due segnali dividano lo schermo.

<margin>
[photo:212:e_oszilloskop_digital: Oscilloscopio con numerose funzioni aggiuntive]
</margin>

Consideriamo ora più da vicino la visualizzazione dell'oscilloscopio nella figura [ref:e_oszilloskop_bildschirmfoto_sinus]. Con un oscilloscopio è possibile determinare, ad esempio, i parametri di una tensione alternata sinusoidale ($T$, $\hat{U}$, $U_\text{SS}$ e $U_\text{eff}$). Oltre all'andamento del segnale, vengono visualizzate indicazioni di tempo e di tensione – nell'esempio $\qty{50,0}{\nano\second}$ e $\qty{500}{\milli\volt}$. Ciò significa che un quadratino in direzione orizzontale corrisponde a 50 nanosecondi e in direzione verticale a 500 millivolt. Questi quadratini sono spesso chiamati divisioni o scale, da cui la dicitura $\qty{500}{\milli\volt\per\oszidiv}$.

<margin>
[photo:214:e_oszilloskop_bildschirmfoto_sinus: una tensione sinusoidale, visualizzata su un oscilloscopio digitale]
</margin>

---

Possiamo immaginarlo come un sistema di coordinate e leggere la durata del periodo ($T$) e l'ampiezza ($\hat{U}$). Nell'esempio, un periodo è lungo 5 quadratini o divisioni di scala. Moltiplicato per $\qty{50,0}{\nano\second}$ per divisione di scala, si ottiene la durata del periodo $\qty{250,0}{\nano\second}$. L'ampiezza, ovvero la massima deviazione dalla posizione zero, è di $\qty{1500}{\milli\volt}$ o $\qty{1,5}{\volt}$, poiché è alta 3 divisioni di scala e ogni divisione corrisponde a $\qty{500}{\milli\volt}$. 

[question:EI301]

<tip>
Per misurazioni semplici, molti oscilloscopi digitali hanno un tasto AUTO. Premendolo, alcune impostazioni vengono effettuate automaticamente e di solito appare un'immagine ferma dei segnali applicati. La visualizzazione può essere spostata orizzontalmente. Una manopola con questa funzione è spesso etichettata come X-Position. Per leggere la durata del periodo, si sposta un punto di riferimento come un passaggio per lo zero su una linea verticale della griglia e si contano quanti divisioni di scala corrisponde un periodo.
</tip>
 
---

Una volta nota la durata del periodo di un'oscillazione, è possibile determinarne anche la frequenza. Nella classe N abbiamo già appreso la relazione qualitativa: la frequenza indica il numero di oscillazioni al secondo. Se la durata del periodo è di un secondo, si ottiene una frequenza di $\qty{1}{\hertz}$. Se dimezziamo la durata del periodo a mezzo secondo, due oscillazioni entrano in un secondo – la frequenza è quindi di $\qty{2}{\hertz}$.

Nella classe E consideriamo ora questa relazione come formula:
  
$f=\dfrac{1}{T}$ o $T=\dfrac{1}{f}$

La frequenza in hertz è il reciproco della durata del periodo in secondi.

Il segnale nella figura [ref:e_oszilloskop_bildschirmfoto_sinus] ha quindi la frequenza

$f = \dfrac{1}{\qty{250}{\nano\second}} = \qty{4}{\mega\hertz}$.
 
[question:EB408]
[question:EB409]
[question:EB411]
[question:EB410]
[question:EI302]

---

A volte i segnali vengono deformati involontariamente. Ciò accade, ad esempio, quando in un amplificatore viene immessa una tensione d’ingresso troppo elevata. Si dice allora che l'amplificatore è sovrasterzato e il suo segnale di uscita è distorto. Distorsioni forti come nella figura [ref:e_oszilloskop_verzerrt] possono essere riconosciute con un oscilloscopio. Per la valutazione dei segnali audio nel radioamatore, questo è generalmente sufficiente.

<margin>
[photo:215:e_oszilloskop_verzerrt: segnale di ingresso sinusoidale (sopra) e segnale di uscita distorto di un amplificatore sovrasterzato]
</margin>

<indepth>
Se un segnale ad alta frequenza sia privo di distorsioni che influenzano altre bande di frequenza, non è possibile valutarlo bene con un oscilloscopio. Per questo, un analizzatore di spettro è lo strumento di misura giusto.
</indepth>

% EI304 NF-Verzerrungen 
[question:EI304]