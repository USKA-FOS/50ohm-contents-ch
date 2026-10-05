Nelle sezioni [sec:transistor_1] e [sec:transistor_2] sui transistor abbiamo già appreso che con una piccola corrente di base $I_\text{B}$ è possibile controllare una corrente di collettore $I_\text{C}$ significativamente maggiore. Questo principio può essere utilizzato per costruire un amplificatore per segnali elettrici. A seconda del tipo di circuito, con i transistor è possibile amplificare segnali di ogni tipo – siano essi segnali digitali, segnali a bassa frequenza (BF) o ad alta frequenza (HF). Un guadagno significa che la potenza d’uscita di un segnale è maggiore della sua potenza d’ingresso, il che rappresenta la caratteristica fondamentale di un amplificatore.

---

La figura [ref:e_nf_verstaerker] mostra un amplificatore BF (amplificatore BF) che deve amplificare i segnali audio dall'apparecchio radio per un altoparlante. Ciò è facilmente riconoscibile dal simbolo dell'altoparlante nel circuito. Gli amplificatori di potenza HF sono utilizzati, ad esempio, per aumentare il segnale di trasmissione.

<margin>
[picture:763:e_nf_verstaerker:Schema circuitale di un amplificatore BF]  
</margin>

[question:ED402]
[question:ED403]

Poiché la potenza d’uscita aumenta rispetto alla potenza d’ingresso, a un amplificatore deve essere sempre fornita energia. Pertanto, è necessaria una sorgente di tensione adeguatamente robusta.

[question:ED401]

---

Affinché un amplificatore possa essere definito *lineare*, deve possedere la proprietà che raddoppiando il segnale di ingresso, anche il segnale di uscita dell'amplificatore raddoppi.
Le deviazioni dalla linearità sono generalmente indesiderate e tollerabili solo in modalità operative come la FM (in cui l'informazione del segnale non viene trasmessa tramite l'ampiezza, ma solo tramite la frequenza). Se un amplificatore non opera in modo lineare, nel suo segnale di uscita sono presenti frequenze che non sono presenti nel segnale di ingresso (cosiddetto splatter). Nel campo BF questo comportamento si manifesta come distorsione. Nel campo HF si generano armoniche del segnale amplificato. Entrambi sono indesiderati. La figura [ref:e_verstaerker_linearitaet] mostra, ad esempio, come un segnale sinusoidale venga deformato da un comportamento non lineare. 

<margin>
[picture:828:e_verstaerker_linearitaet:Il segnale di ingresso viene amplificato. In caso di limitazione dovuta alla mancanza di linearità, il segnale di uscita viene deformato.]
</margin>

[question:EF403]

Per la linearità di un trasmettitore è inoltre necessaria un'alimentazione elettrica stabilizzata e disaccoppiata da altri stadi, per evitare retroazioni indesiderate.

[question:EF405]

Gli amplificatori BF non si trovano solo nell'altoparlante dell'apparecchio radio, ma già nel microfono. Qui servono, ad esempio, per amplificare il segnale del microfono. Di solito, le componenti di frequenza più basse (sotto $\qty{300}{\hertz}$) e più alte (sopra $\qty{3}{\kilo\hertz}$) del segnale del microfono vengono già soppresse all'interno dell'amplificatore del microfono mediante una caratteristica passa-banda, per limitare la larghezza di banda del segnale BF e sopprimere componenti di frequenza più basse come, ad esempio, il ronzio di rete (cfr. figura [ref:e_frequenzgang_mikrofonverstaerker]). Per una buona intelligibilità del parlato, nella comunicazione vocale è necessaria una larghezza di banda BF di circa $\qtyrange{2,5}{3}{\kilo\hertz}$.

<margin>
[picture:246:e_frequenzgang_mikrofonverstaerker:Risposta in frequenza tipica per un amplificatore di microfono radioamatoriale]
</margin>

[question:EF308]
[question:EF307]
