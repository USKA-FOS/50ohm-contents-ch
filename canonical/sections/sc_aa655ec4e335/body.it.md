Nel capitolo sui transistor abbiamo già appreso che con una piccola corrente di base $I_\text{B}$ è possibile controllare una corrente di collettore $I_\text{C}$ notevolmente maggiore. Questo principio può essere utilizzato per costruire un amplificatore per segnali elettrici. A seconda del tipo di circuito, i transistor possono amplificare segnali di ogni tipo, siano essi segnali digitali, a bassa frequenza (NF) o ad alta frequenza (HF). Un'amplificazione significa che la potenza d'uscita di un segnale è maggiore della sua potenza d'ingresso, il che rappresenta la caratteristica fondamentale di un amplificatore.

---

La figura [ref:e_nf_verstaerker] mostra un amplificatore a bassa frequenza (amplificatore NF) che deve amplificare i segnali audio dall'apparecchio radio per un altoparlante. Ciò si riconosce facilmente dal simbolo dell'altoparlante nel circuito. Gli amplificatori di potenza HF vengono utilizzati, ad esempio, per aumentare il segnale di trasmissione.

<margin>
[picture:763:e_nf_verstaerker:Schema di un amplificatore NF]  
</margin>

[question:ED402]
[question:ED403]

Dato che la potenza d'uscita aumenta rispetto alla potenza d'ingresso, è necessario fornire sempre energia a un amplificatore. Pertanto, è necessaria una fonte di tensione adeguatamente dimensionata.

[question:ED401]

---

Affinché un amplificatore possa essere definito *lineare*, deve possedere la proprietà che raddoppiando il segnale d'ingresso, anche il segnale d'uscita dell'amplificatore si raddoppi.
Le deviazioni di linearità sono generalmente indesiderate e tollerabili solo per modi operativi come FM (in cui l'informazione del segnale non viene trasmessa tramite l'ampiezza, ma solo tramite la frequenza). Se un amplificatore non funziona linearmente, nel suo segnale d'uscita sono presenti frequenze che non erano presenti nel segnale d'ingresso (i cosiddetti splatter). Nell'ambito NF, questo comportamento si manifesta come distorsione. Nell'ambito HF, si creano armoniche superiori del segnale amplificato. Entrambi sono indesiderati. La figura [ref:e_verstaerker_linearitaet] mostra in modo esemplificativo come un segnale sinusoidale viene deformato da un comportamento non lineare. 

<margin>
[picture:828:e_verstaerker_linearitaet:Il segnale d'ingresso viene amplificato. In caso di limitazione dovuta a mancanza di linearità, il segnale d'uscita viene deformato.]
</margin>

[question:EF403]

Per la linearità di un trasmettitore è necessaria anche un'alimentazione stabilizzata e disaccoppiata da altri stadi, per evitare indesiderati feedback.

[question:EF405]

Gli amplificatori NF non si trovano solo nell'altoparlante dell'apparecchio radio, ma anche già nel microfono. Qui servono, ad esempio, per amplificare il segnale del microfono. Di solito, le componenti di frequenza più basse (sotto $\qty{300}{\hertz}$) e più alte (sopra $\qty{3}{\kilo\hertz}$) del segnale del microfono vengono già soppresse all'interno dell'amplificatore del microfono tramite una caratteristica passa-banda, per limitare la larghezza di banda del segnale NF e sopprimere le componenti di frequenza più basse come il ronzio di rete (cfr. figura [ref:e_frequenzgang_mikrofonverstaerker]). Per una buona intelligibilità vocale, nella comunicazione vocale è necessaria una larghezza di banda NF di circa $\qtyrange{2,5}{3}{\kilo\hertz}$.

<margin>
[picture:246:e_frequenzgang_mikrofonverstaerker:Tipica risposta in frequenza per un amplificatore microfonico per radioamatore]
</margin>

[question:EF308]
[question:EF307]