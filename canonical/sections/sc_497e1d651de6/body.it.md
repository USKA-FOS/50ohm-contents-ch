Una cosiddetta *linea di Lecher* è costituita da due conduttori paralleli su cui, per sovrapposizione di onda diretta e onda riflessa, si formano onde stazionarie ad alta frequenza. Essa può terminare sia in circuito aperto (cfr. figura [ref:a_lecherleitung_offen]) che in corto circuito (cfr. figura [ref:a_lecherleitung_kurzgeschlossen]). In entrambi i casi si generano distribuzioni caratteristiche di corrente e tensione, che possono essere utilizzate, ad esempio, per determinare la lunghezza d’onda λ.

<margin>
[picture:1112:a_lecherleitung_offen:Linea di Lecher con estremità aperta]
</margin>

In una linea di Lecher con estremità *aperta* non può scorrere corrente al termine della linea. In quel punto si trova quindi un minimo di corrente e contemporaneamente un massimo di tensione. Dal teorema di Ohm

$R=\frac{U}{I}$

si deduce che il rapporto tra tensione e corrente in questo punto diventa idealmente infinito, cioè $R=\infty$. La corrente e la tensione sono spostate spazialmente lungo la linea di $\frac{\lambda}{4}$. A una distanza di $\frac{\lambda}{4}$ dall’estremità aperta della linea si trova quindi un massimo di corrente e contemporaneamente un minimo di tensione. Poiché in quel punto la tensione idealmente tende a zero, secondo il teorema di Ohm si ottiene $R=0$. Dopo ulteriori $\frac{\lambda}{4}$, i massimi di corrente e tensione si alternano. Dopo una distanza di $\frac{\lambda}{2}$, la distribuzione di corrente e tensione è identica a quella rappresentata nella figura [ref:a_lecherleitung_offen].

---

In una linea di Lecher con estremità *in corto circuito* i due conduttori non possono avere una tensione diversa al termine della linea. In quel punto vale quindi $U=0$. Si trova quindi un minimo di tensione e contemporaneamente un massimo di corrente. Con $R=\frac{U}{I}$ ne consegue idealmente $R=0$. A una distanza di $\frac{\lambda}{4}$ dal corto circuito si trova invece un massimo di tensione e contemporaneamente un minimo di corrente. Poiché in quel punto la corrente idealmente tende a zero, il rapporto $\frac{U}{I}$ diventa molto grande e idealmente vale $R=\infty$. Anche nella linea di Lecher in corto circuito, i massimi di corrente e tensione si alternano dopo ogni $\frac{\lambda}{4}$. Dopo una distanza di $\frac{\lambda}{2}$, la distribuzione di corrente e tensione è identica a quella rappresentata nella figura [ref:a_lecherleitung_kurzgeschlossen].

<margin>
[picture:1111:a_lecherleitung_kurzgeschlossen:Linea di Lecher con estremità in corto circuito]
</margin>

La frequenza che si forma come risonanza su una linea di Lecher dipende essenzialmente dalla sua lunghezza. Se la lunghezza della linea cambia, anche la frequenza di risonanza cambia.

[question:AG320]

Con una lunghezza della linea pari a $\frac{\lambda}{2}$, la distribuzione di corrente e tensione si ripete completamente. Un carico con impedenza all’estremità della linea appare quindi all’ingresso della linea con lo stesso valore.

Un caso particolare molto importante si verifica quando la linea di Lecher, alla frequenza considerata, ha una lunghezza elettrica esattamente pari a $\frac{\lambda}{4}$. Come abbiamo visto dalle distribuzioni di corrente e tensione, su una distanza di $\frac{\lambda}{4}$ un massimo di corrente e un massimo di tensione si scambiano tra loro. In questo modo, un’impedenza elevata viene trasformata in un’impedenza bassa e viceversa.

In una linea di $\frac{\lambda}{4}$ con estremità *aperta*, l’impedenza all’estremità della linea è idealmente infinita. Dopo una distanza di $\frac{\lambda}{4}$, all’ingresso della linea si trova invece un minimo di tensione e un massimo di corrente. L’impedenza di ingresso è quindi quasi nulla ($Z_\mathrm{in} \approx \qty{0}{\ohm}$). Un’estremità aperta della linea viene quindi trasformata approssimativamente in un corto circuito da una linea di lunghezza $\frac{\lambda}{4}$.

---

[question:AG411]

Viceversa, una linea con estremità *in corto circuito* ha all’estremità dell’impedenza $\qty{0}{\ohm}$. Dopo una distanza di $\frac{\lambda}{4}$, all’ingresso della linea si trova un massimo di tensione e un minimo di corrente. L’impedenza di ingresso diventa quindi molto grande ($Z_\mathrm{in} \rightarrow \infty$). Un corto circuito all’estremità della linea viene quindi trasformato approssimativamente in un circuito aperto da una linea di lunghezza $\frac{\lambda}{4}$.

<indepth>
Il comportamento di una linea $\frac{\lambda}{4}$ può essere paragonato anche a quello dei circuiti risonanti. Una linea $\frac{\lambda}{4}$ aperta ha all’ingresso un’impedenza molto bassa e si comporta in modo simile a un *circuito risonante serie in risonanza*. Una linea $\frac{\lambda}{4}$ in corto circuito ha invece all’ingresso un’impedenza molto alta e si comporta in modo simile a un *circuito risonante parallelo in risonanza*.
</indepth>

Nel prossimo paragrafo esamineremo come sia possibile effettuare trasformazioni di impedenza mirate con l’aiuto di linee $\frac{\lambda}{4}$.