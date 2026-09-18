Nella modulazione di ampiezza (AM) e nella SSB, l'informazione da trasmettere viene veicolata da una variazione dell'ampiezza della portante ad alta frequenza. Nel capitolo [sec:fm] abbiamo già appreso che nella modulazione di frequenza (FM) l'ampiezza della portante rimane invece costante: l'informazione viene trasmessa tramite una variazione della frequenza istantanea della portante.

La figura [ref:e_frequenzmodulation_t] mostra l'andamento temporale di un segnale FM con ampiezza costante. Un segnale FM è quindi riconoscibile dal fatto che l'ampiezza della portante (idealmente) rimane costante, mentre la sua frequenza istantanea varia continuamente in funzione del segnale di modulazione.

<margin>
[picture:906:e_frequenzmodulation_t:Andamento temporale di un segnale FM]
</margin>

[question:EE301]

---

La figura [ref:e_frequenzmodulation_frequenzhub] mostra un esempio di segnale sinusoidale BF che provoca una corrispondente deviazione di frequenza (deviazione di frequenza portante) di una portante ad alta frequenza nello spettro. Ciò significa che in un segnale FM l'informazione di volume viene trasmessa tramite la *deviazione della frequenza portante*. Un segnale BF più intenso provocherebbe una maggiore deviazione della frequenza portante e quindi una larghezza di banda maggiore del segnale FM.

<margin>
[picture:827:e_frequenzmodulation_frequenzhub:Deviazione della portante nella modulazione di frequenza]
</margin>

<indepth>
La larghezza di banda occupata da un'emissione FM è determinata dalla deviazione e dalla frequenza massima di modulazione. In prima approssimazione, per deviazioni ridotte e basse frequenze di modulazione, si può applicare la *formula di Carson*. Essa indica in quale larghezza di banda si trova il $\qty{99}{\percent}$ della potenza di trasmissione.

$B\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$

Questo argomento viene trattato in modo più approfondito in [sec:fm_3].
</indepth>

[question:EE306]
[question:EE304]

Per rispettare i requisiti di legge relativi alla larghezza di banda occupata da un segnale FM, nel trasmettitore FM il segnale del microfono viene prima limitato in ampiezza (tramite un amplificatore limitatore) e poi modulato sulla portante tramite FM. In questo caso, la deviazione di frequenza del modulatore, in caso di massima escursione del volume, è fissata o regolabile tramite un regolatore di deviazione.

[question:EE305]

I segnali FM, poiché l'informazione modulata non è contenuta nell'ampiezza ma solo nella frequenza, sono relativamente poco sensibili ai disturbi di ampiezza (ad esempio causati da fulmini, impianti di accensione, motori) rispetto a AM o SSB. Ciò comporta vantaggi in termini di suscettibilità ai disturbi, in particolare durante l'uso in veicoli e in ambienti disturbati.

[question:EE302]
[question:EE303]