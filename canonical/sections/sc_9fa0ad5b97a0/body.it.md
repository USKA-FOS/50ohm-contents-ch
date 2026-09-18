Non tutte le antenne hanno esattamente l’impedenza necessaria al punto di alimentazione per essere collegate a una specifica linea di alimentazione o a un trasmettitore. Se l’impedenza, ad esempio, si discosta dai consueti $\qty{50}{\ohm}$, deve essere adattata di conseguenza affinché la potenza RF possa essere trasmessa con la minor perdita possibile. A questo scopo, l’impedenza esistente viene *trasformata* in un’altra impedenza desiderata. Questo processo è noto come *trasformazione dell’impedenza* o *adattamento dell’impedenza*.

Per l’adattamento o la trasformazione dell’impedenza esistono diverse possibilità. Tra le più utilizzate troviamo ad esempio:

* Trasformatori,
* linee $\frac{\lambda}{4}$ o
* reti di adattamento composte da induttori e condensatori.

Abbiamo già incontrato i trasformatori con l’antenna alimentata all’estremità e un Unun 1:49. Nei paragrafi seguenti, quindi, esamineremo più da vicino altre due possibilità: la trasformazione dell’impedenza con linee $\frac{\lambda}{4}$ (trattate nel paragrafo precedente) e l’adattamento con reti LC. Prima di tutto, riprendiamo in considerazione le linee di trasformazione. A questo proposito, non importa se utilizziamo una linea di alimentazione simmetrica o una linea coassiale asimmetrica: la trasformazione funziona in entrambi i casi.

In una linea la cui lunghezza elettrica è $\lambda/4$, le resistenze ohmiche inferiori all’impedenza caratteristica della linea vengono trasformate in resistenze superiori all’impedenza caratteristica della linea. Viceversa, le resistenze ohmiche superiori all’impedenza caratteristica della linea vengono trasformate in resistenze inferiori all’impedenza caratteristica. Questo principio viene sfruttato, ad esempio, per adattare antenne ad alta impedenza a un sistema a bassa impedenza ($\qty{50}{\ohm}$).

[question:AG410]
[question:AG409]

Con una lunghezza della linea pari a $\lambda/2$, l’effetto si annulla e non si verifica alcuna trasformazione dell’impedenza.

[question:AG412]
[question:AG416]

Per le domande seguenti, ricordiamo che un dipolo a semionda è alimentato in corrente (bassa impedenza) e un dipolo a onda intera è alimentato in tensione (alta impedenza).

[question:AG413]
[question:AG414]
[question:AG415]

Se si desidera trasformare un valore di resistenza in un altro, l’impedenza caratteristica necessaria si ricava dalla media geometrica tra la resistenza di carico $Z_\mathrm{A}$ e la resistenza di alimentazione desiderata $Z_\mathrm{E}$ all’altra estremità del cavo:

$Z = \sqrt{Z_\mathrm{E} \cdot Z_\mathrm{A}}$

[question:AG417]
[question:AG418]

---

Spesso, per l’adattamento dell’impedenza, vengono utilizzati anche induttori e condensatori. Un esempio molto diffuso è il cosiddetto *filtro Pi*, che, oltre alla sua funzione di filtro passa-basso, consente anche una trasformazione dell’impedenza. Pertanto, un tale filtro Pi può essere impiegato anche come accordatore d’antenna.

<indepth>
*Il nome "filtro Pi"* deriva dalla disposizione dei componenti nel diagramma circuitale, che ricorda la lettera greca $\pi$, e non ha nulla a che fare con la costante Pi.
</indepth>

[question:AG406]
