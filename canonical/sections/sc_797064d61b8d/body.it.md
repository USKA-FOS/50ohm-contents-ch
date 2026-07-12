Nella modulazione di ampiezza (AM) e in SSB, l'informazione da trasmettere viene trasmessa modificando l'ampiezza della portante ad alta frequenza. Abbiamo già appreso che nella modulazione di frequenza (FM), al contrario, l'ampiezza della portante rimane costante: l'informazione viene trasmessa tramite una variazione della frequenza istantanea della portante.

La figura [ref:e_frequenzmodulation_t] mostra l'andamento temporale di un segnale FM con ampiezza costante. Un segnale FM è quindi riconoscibile dal fatto che l'ampiezza della portante (idealmente) rimane costante, mentre la sua frequenza istantanea cambia continuamente in dipendenza dal segnale di modulazione.

<margin>
[picture:906:e_frequenzmodulation_t:Andamento temporale di un segnale FM]
</margin>

[question:EE301]

---

La figura [ref:e_frequenzmodulation_frequenzhub] mostra a titolo esemplificativo un segnale NF sinusoidale che causa una corrispondente deviazione di frequenza (frequenza di modulazione) di una portante ad alta frequenza nello spettro. Ciò significa che in un segnale FM, l'informazione di volume viene trasmessa tramite la *deviazione della frequenza portante (frequenza di modulazione)*. Un segnale NF più forte porterebbe a una maggiore deviazione della frequenza portante e quindi a una maggiore larghezza di banda del segnale FM.

<margin>
[picture:827:e_frequenzmodulation_frequenzhub:Deviazione della portante nella modulazione di frequenza]
</margin>

<indepth>
La larghezza di banda occupata da una trasmissione FM è determinata dalla deviazione e dalla frequenza di modulazione massima. In prima approssimazione, per piccole deviazioni e basse frequenze di modulazione, si può applicare la *formula di Carson*. Essa indica in quale larghezza di banda si trova il $\qty{90}{\percent}$ della potenza di trasmissione.

$B\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$
  
Questo argomento verrà discusso più in dettaglio nella classe A.
</indepth>

[question:EE306]
[question:EE304]

Per rispettare le normative legali relative alla larghezza di banda occupata da un segnale FM, nei trasmettitori FM il segnale del microfono viene prima limitato in ampiezza (tramite un amplificatore limitatore) e successivamente modulato in FM sulla portante. In questo processo, la deviazione di frequenza del modulatore al massimo livello di modulazione è o fissa o regolabile tramite un controllo di deviazione.

[question:EE305]

I segnali FM, poiché l'informazione modulata non è contenuta nell'ampiezza ma solo nella frequenza, sono relativamente insensibili ai disturbi di ampiezza (ad es. causati da fulmini, impianti di accensione, motori) rispetto ad AM o SSB. Ciò offre vantaggi in termini di suscettibilità ai disturbi, in particolare durante il funzionamento nei veicoli e in ambienti disturbati.

[question:EE302]
[question:EE303]
