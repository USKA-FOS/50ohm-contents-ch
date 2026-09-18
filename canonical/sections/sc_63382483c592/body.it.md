Per ridurre la larghezza di banda massima di un segnale SSB trasmesso e utilizzare in modo efficiente lo spettro di frequenza disponibile, la larghezza di banda massima del segnale BF di un segnale SSB non dovrebbe superare $\qty{2,7}{\kilo\hertz}$. Ciò consente una distanza minima tra i segnali SSB di $\qty{3}{\kilo\hertz}$, per un funzionamento senza interferenze.

[question:AE208]
[question:AE209]

Se un segnale SSB viene sovramodulato nel modulatore del trasmettitore, si generano distorsioni che portano a emissioni parassite. Queste emissioni parassite sono comunemente chiamate "splatter" e possono disturbare le trasmissioni adiacenti, poiché in questo caso la larghezza di banda del segnale del trasmettitore supera i $\qty{2,7}{\kilo\hertz}$ richiesti.
[question:AE205]

La voce di ogni persona ha uno spettro di frequenza individuale. Per ottenere la migliore comprensibilità possibile nelle trasmissioni SSB, le frequenze vocali nella gamma alta devono essere enfatizzate e quelle nella gamma bassa attenuate. A questo scopo, un equalizzatore nel preamplificatore del microfono del trasmettitore consente di regolare individualmente la risposta in frequenza del segnale di modulazione. In questo modo, la risposta in frequenza del microfono viene ottimizzata per l’operatore.
[question:AE213]

---

Per valutare la qualità e la linearità della forma dell’inviluppo di un trasmettitore SSB, è possibile utilizzare un segnale a due toni per la modulazione. In questo caso, il trasmettitore SSB viene modulato con un segnale BF composto da due frequenze BF sovrapposte. Queste frequenze BF non devono essere in rapporto intero tra loro. La sovrapposizione genera nel segnale RF trasmesso massimi e minimi (passaggi per zero) del segnale HF. Per la modulazione possono essere utilizzati, ad esempio, un tono di $\qty{700}{\hertz}$ e uno di $\qty{1200}{\hertz}$. Misurando il segnale HF con un oscillogramma (su una resistenza di carico), si ottiene una battimento dell’HF di $\qty{500}{\hertz}$, che idealmente dovrebbe essere sinusoidale. Il segnale a due toni consente anche di misurare la potenza d’inviluppo (PEP) di un trasmettitore SSB visualizzando la forma d’onda sull’oscilloscopio.

[question:AI304]

<margin>
[picture:1092:a_ssb_zweiton:Segnale a due toni per la valutazione della forma dell’inviluppo di un trasmettitore SSB]
</margin>

La figura [ref:a_ssb_zweiton] mostra in 1. un segnale a un tono, cioè un semplice tono BF sinusoidale. Nei punti 2. e 3. è illustrato come questo segnale a un tono viene convertito in HF in AM o SSB. Il segnale SSB al punto 3. consiste di una singola componente HF con ampiezza costante e appare quindi come una portante HF non modulata su una frequenza spostata rispetto alla portante soppressa. Tuttavia, con un segnale a un tono è possibile valutare solo in modo limitato la qualità e la linearità di un trasmettitore SSB; in particolare, non compaiono prodotti di intermodulazione significativi tra più segnali utili.

Al punto 4. è visibile un segnale utile a due toni, costituito dalla sovrapposizione di due toni sinusoidali di $\qty{700}{\hertz}$ e $\qty{1200}{\hertz}$. Nei punti 5. e 6. viene mostrato come questo segnale a due toni viene convertito in HF in AM o SSB. Nel segnale SSB a due toni al punto 6. si generano due componenti HF distanziate di $\qty{500}{\hertz}$. La loro sovrapposizione crea un battimento periodico dell’inviluppo HF con la frequenza di differenza di $\qty{500}{\hertz}$. Questo inviluppo consente di misurare la potenza di picco dell’inviluppo (PEP) e di valutare al contempo la linearità del trasmettitore, poiché le non linearità portano a prodotti di intermodulazione aggiuntivi nello spettro.

[question:AE207]

Per i seguenti esercizi, la potenza di uscita del trasmettitore deve essere determinata come potenza di picco dell’inviluppo (PEP). La PEP descrive la potenza effettiva che il trasmettitore eroga durante il picco dell’inviluppo di modulazione. Essa non si riferisce quindi alla potenza media su tutta la modulazione, ma al valore di potenza al massimo dell’inviluppo, come mostrato nella figura [ref:a_pep_hüllkurve]. La tensione di picco per il calcolo della potenza efficace può essere letta nell’oscillogramma. In questo caso, occorre prestare attenzione al rapporto della sonda di misura.

<margin>
[picture:875:a_pep_hüllkurve:Inviluppo di modulazione per il calcolo della potenza]
</margin>

% Sonda 1:1 PEP
[question:AI305]

% Sonda 10:1 PEP
[question:AI306]