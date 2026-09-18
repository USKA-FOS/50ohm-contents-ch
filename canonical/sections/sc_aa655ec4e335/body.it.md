Nel capitolo dedicato ai transistor abbiamo già imparato che, con una piccola corrente di base $I_\text{B}$, è possibile controllare una corrente di collettore $I_\text{C}$ molto più elevata. Questo principio può essere sfruttato per costruire un **amplificatore** per **segnali elettrici**. A seconda del tipo di circuito, i transistor possono amplificare segnali di ogni genere: digitali, a **bassa frequenza** (BF) o ad **alta frequenza** (HF). L’amplificazione consiste nel fatto che la **potenza d’uscita** di un segnale è maggiore della sua **potenza d’ingresso**, caratteristica fondamentale di un amplificatore.

---

La figura [ref:e_nf_verstaerker] mostra un **amplificatore BF** che deve amplificare i **segnali audio** provenienti dall’**apparecchio radio** per un altoparlante. Questo è riconoscibile dal simbolo dell’altoparlante nel circuito. Gli **amplificatori di potenza HF** vengono utilizzati, ad esempio, per aumentare il **segnale di trasmissione**.

<margin>
[picture:763:e_nf_verstaerker:Schema di un amplificatore BF]  
</margin>

[question:ED402]
[question:ED403]

Poiché la **potenza d’uscita** è maggiore rispetto a quella d’ingresso, un **amplificatore** deve sempre ricevere energia. Pertanto, è necessaria una **sorgente di tensione** sufficientemente robusta.

[question:ED401]

---

Affinché un **amplificatore** possa essere definito *lineare*, deve possedere la proprietà che, se il **segnale d’ingresso** raddoppia, anche il **segnale d’uscita** all’amplificatore raddoppia. Le deviazioni dalla linearità sono generalmente indesiderate e tollerabili solo in alcune **modalità operative**, come la FM (in cui le informazioni del **segnale** non vengono trasmesse tramite l’**ampiezza**, ma solo tramite la **frequenza**). Se un **amplificatore** non è lineare, nel suo **segnale d’uscita** sono presenti frequenze non presenti nel **segnale d’ingresso** (il cosiddetto *splatter*). Nel campo BF questo comportamento si manifesta come distorsione. Nel campo HF si generano **armoniche** del **segnale** amplificato. Entrambi gli effetti sono indesiderati. La figura [ref:e_verstaerker_linearitaet] mostra un esempio di come un segnale sinusoidale venga deformato da un comportamento non lineare.

<margin>
[picture:828:e_verstaerker_linearitaet:Il **segnale d’ingresso** viene amplificato. In caso di **limitazione** dovuta alla mancanza di linearità, il **segnale d’uscita** viene deformato.]
</margin>

[question:EF403]

Per garantire la linearità di un trasmettitore, è necessaria anche un’**alimentazione elettrica** stabilizzata e decouplata dagli altri stadi, al fine di evitare **retroazioni** indesiderate.

[question:EF405]

Gli **amplificatori BF** non si trovano solo negli altoparlanti collegati agli **apparecchi radio**, ma anche nei microfoni. In questo caso, servono ad esempio per amplificare il **segnale del microfono**. Solitamente, in questi **amplificatori**, vengono già attenuate le componenti a frequenza più bassa (sotto $\qty{300}{\hertz}$) e più alta (sopra $\qty{3}{\kilo\hertz}$) del **segnale del microfono**, grazie a una caratteristica di **filtro passa-banda**, per limitare la **larghezza di banda** del **segnale BF** ed eliminare componenti a bassa frequenza come, ad esempio, il ronzio della rete (cfr. figura [ref:e_frequenzgang_mikrofonverstaerker]). Per una buona intelligibilità vocale nelle comunicazioni, è necessaria una **larghezza di banda BF** di circa $\qtyrange{2,5}{3}{\kilo\hertz}$.


<margin>
[picture:246:e_frequenzgang_mikrofonverstaerker:Risposta in frequenza tipica di un amplificatore per microfono nel **radioamatoriale**]
</margin>

[question:EF308]
[question:EF307]