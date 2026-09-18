Nella classe E abbiamo già imparato a conoscere la linea di alimentazione bifilare, chiamata anche *linea bifilare* (cfr. figura [ref:a_huenerleiter]). Essa è composta da due conduttori paralleli. Le linee bifilari, a patto di essere alimentate e caricate in modo simmetrico, si comportano anche in modo simmetrico per quanto riguarda la distribuzione di corrente e tensione. Ciò significa che, in una determinata posizione, la corrente e la tensione sui due conduttori hanno lo stesso valore assoluto, ma segni opposti, come illustrato nella figura [ref:a_zweidrahtleitung].

<margin>
[photo:324:a_huenerleiter:Linea bifilare, anche chiamata linea bifilare]
</margin>

Le correnti sui due conduttori fluiscono quindi in direzioni opposte in ogni istante. Si parla di *correnti in controfase*. I campi elettromagnetici generati dai due conduttori si annullano quindi reciprocamente a grande distanza. Una linea bifilare alimentata in modo simmetrico irradia quindi molto poco.

<margin>
[picture:1107:a_zweidrahtleitung:Distribuzione di corrente e tensione su una linea bifilare]
</margin>

Se invece la linea di alimentazione non è completamente simmetrica, possono verificarsi anche *correnti in fase*. In questo caso, parte della corrente fluisce sui due conduttori nella stessa direzione. I campi generati da queste correnti non si annullano reciprocamente. La linea di alimentazione può quindi comportarsi come un’antenna e irradiare energia ad alta frequenza. Tali componenti in fase possono ad esempio verificarsi se un dipolo non è costruito in modo esattamente simmetrico, se viene collegata un’antenna o un carico asimmetrico, o se la transizione tra un’antenna simmetrica e una linea di alimentazione asimmetrica non è decouplata da un balun o da un’induttanza di modo comune.

[question:AG312]

In particolare nel campo vicino ad altre linee o dispositivi elettrici può verificarsi un accoppiamento elettromagnetico più forte. Per questo motivo, le linee di alimentazione all’interno di edifici vengono solitamente realizzate in versione schermata, ad esempio come cavo coassiale. In un cavo coassiale, i campi elettromagnetici della modalità differenziale si trovano prevalentemente tra il conduttore interno e lo schermo. In questo modo si riducono sia l’irradiazione della linea di alimentazione che l’accoppiamento di disturbi esterni.

[question:AG301]

Come cavo schermato, il cavo coassiale è una soluzione ideale, che abbiamo già imparato a conoscere nella classe E. I cavi coassiali sono disponibili in varie versioni. Nella domanda seguente verranno trattate le *caratteristiche ad alta frequenza* dei cavi coassiali, cioè le loro proprietà elettriche alle alte frequenze. Queste sono essenzialmente:

* l’impedenza caratteristica,
* l’attenuazione del cavo e il
* fattore di velocità,

che verranno esaminati più da vicino. Il raggio di curvatura, invece, è una proprietà meccanica che indica quanto strettamente il cavo può essere posato in una curva. La perdita di ritorno indica quante riflessioni sono presenti, dipendendo dal carico collegato alla linea e quindi non è una proprietà del cavo.

[question:AG303]

Il fattore di velocità dipende dal materiale dielettrico presente tra il conduttore interno e quello esterno. In questo spazio si propaga la maggior parte dell’onda elettromagnetica trasmessa dal cavo. La scelta del materiale dielettrico determina la velocità con cui l’onda si propaga nel cavo. La velocità di propagazione nel cavo coassiale è inferiore alla velocità della luce nello spazio libero. Materiali dielettrici comuni sono il polietilene (PE) e il teflon (PTFE). Attraverso la schiumatura si ottiene una miscela con l’aria, che riduce l’attenuazione del cavo.

[question:AG314]
[question:AG302]

La velocità di propagazione ridotta dal materiale dielettrico si riflette nel fattore di velocità, che indica di quanto deve essere accorciata meccanicamente la lunghezza di un cavo per avere una determinata lunghezza elettrica (ad esempio un quarto di lunghezza d’onda). Per il fattore di velocità troviamo nella raccolta di formule la seguente relazione:

$k_\mathrm{v} = \frac{L_\mathrm{G}}{L_\mathrm{E}} = \frac{1}{\sqrt{\epsilon_\mathrm{r}}}$

Qui $k_\mathrm{v}$ è il fattore di velocità, $L_\mathrm{G}$ la lunghezza geometrica ("meccanica"), e $L_\mathrm{E}$ la lunghezza elettrica. La costante dielettrica relativa $\epsilon_\mathrm{r}$ dipende dal materiale dielettrico utilizzato. Per il polietilene (PE) non schiumato, nella raccolta di formule possiamo trovare un valore della costante dielettrica di $\num{2,29}$.

[question:AG317]