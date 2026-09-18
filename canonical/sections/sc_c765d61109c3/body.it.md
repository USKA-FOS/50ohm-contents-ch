In un ricevitore al cui ingresso sono presenti due forti segnali RF, possono verificarsi disturbi dovuti a intermodulazione o modulazione incrociata.
In caso di intermodulazione, questo effetto si manifesta con la generazione di frequenze indesiderate aggiuntive, simili a quelle prodotte in un mixer, a causa del comportamento non lineare dello stadio del ricevitore (funzionamento in prossimità della soglia non lineare). Queste frequenze possono sovrapporsi e disturbare i segnali utili ricevuti.
In caso di modulazione incrociata, questo effetto si manifesta con l’influenza del segnale AM forte e adiacente in frequenza sul segnale utile ricevuto. In questo modo, la modulazione della stazione trasmittente adiacente diventa udibile nel segnale ricevuto e lo disturba.

[question:AF217]
[question:AF219]
[question:AF222]
[question:AF218]

Per attenuare un segnale indesiderato forte già prima dell’ingresso del ricevitore, ad esempio, si può utilizzare un circuito trappola sintonizzato sulla frequenza esatta del segnale disturbante, posto a monte dell’ingresso del ricevitore.

[question:AF223]

La robustezza di un ricevitore nei confronti di segnali forti può essere descritta dal cosiddetto punto di intercetto di terzo ordine (IP3). Si tratta di un parametro che indica il punto in cui i prodotti di intermodulazione di terzo ordine raggiungono la stessa ampiezza del segnale d’ingresso. Più alto è l’IP3 di un ricevitore, maggiore è la capacità di questo di elaborare segnali forti senza subire disturbi.

<indepth>
In questa sezione approfondita consideriamo l’IP3 come parametro per la robustezza di un ricevitore nei confronti di segnali forti. In generale, i prodotti di intermodulazione nascono da non linearità presenti negli amplificatori, nei mixer o in altri stadi del ricevitore. Con due segnali d’ingresso $f_1$ e $f_2$, possono generarsi prodotti di intermodulazione della forma

$f_{\text{mix}} = \left| m \cdot f_1 \pm n \cdot f_2 \right|$

dove $m,n \in \mathbb{N}_0$ e i due coefficienti non possono essere contemporaneamente nulli. L’ordine di un prodotto di intermodulazione è dato dalla somma dei coefficienti:

$\text{Ordine} = m+n$

Particolarmente critici sono i prodotti di intermodulazione di terzo ordine, poiché spesso si trovano vicino ai segnali d’ingresso originali. Di conseguenza, possono cadere nella banda di ricezione desiderata e risultare difficili o impossibili da eliminare con filtri successivi.

Nella figura seguente [ref:a_intermodulation] è illustrata l’intermodulazione di due segnali $f_1$ e $f_2$. I prodotti di intermodulazione di terzo ordine sono evidenziati in modo particolare:

[picture:1095:a_intermodulation:Intermodulazione di due segnali $f_1$ e $f_2$]

È importante notare che questi prodotti di intermodulazione non vengono ricevuti dall’esterno, ma si generano all’interno del ricevitore a causa di un comportamento non lineare. Con un test a due toni è possibile analizzare la linearità di un ricevitore. A tal fine, vengono iniettati due segnali definiti. Se, oltre a questi due segnali fondamentali, compaiono anche prodotti di intermodulazione di terzo ordine nello spettro, ad esempio in un diagramma a cascata, ciò indica un comportamento non lineare.

La figura [ref:a_zweitontest] mostra un test a due toni con uno sweep di potenza, in cui i prodotti di intermodulazione di terzo ordine sono chiaramente visibili.

[picture:1096:a_zweitontest:Test a due toni con sweep di potenza]

Se si rappresenta la potenza d’uscita in funzione della potenza d’ingresso, i segnali fondamentali aumentano linearmente con una pendenza di $1{:}1$. I prodotti di intermodulazione di terzo ordine, invece, aumentano con una pendenza di $3{:}1$. Estendendo linearmente le due curve, si ottiene un punto di intersezione teorico. Questo punto viene chiamato IP3, ovvero punto di intercetto di terzo ordine.

L’IP3 descrive quindi il punto estrapolato in cui, teoricamente, i prodotti di intermodulazione di terzo ordine raggiungerebbero la stessa potenza d’uscita dei segnali fondamentali. In pratica, questo punto non viene generalmente raggiunto, poiché il ricevitore entra in compressione o saturazione prima.

Più alto è l’IP3 di un ricevitore, migliore è la sua robustezza nei confronti di segnali forti. Un IP3 elevato significa che anche segnali adiacenti forti possono essere elaborati senza che si generino prodotti di intermodulazione disturbanti nella banda di ricezione desiderata.
</indepth>

[question:AF221]

Per ridurre la formazione di prodotti di intermodulazione indesiderati all’ingresso del ricevitore a causa di segnali forti, è possibile inserire un attenuatore commutabile a monte dell’ingresso del ricevitore. In questo modo, si riducono sia i prodotti di intermodulazione che la modulazione incrociata nel ricevitore. Il segnale utile viene attenuato solo del fattore dell’attenuatore, mentre i prodotti di intermodulazione indesiderati vengono attenuati di un fattore $\num{3}$ (di terzo ordine) in $\unit{\dB}$. Ad esempio, un attenuatore da $\qty{10}{\dB}$ riduce il segnale utile solo di $\qty{10}{\dB}$, mentre i prodotti di intermodulazione indesiderati vengono attenuati già di $\qty{30}{\dB}$.

[question:AF220]