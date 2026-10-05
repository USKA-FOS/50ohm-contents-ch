Un alimentatore converte la tensione alternata di $\qty{230}{\volt}$ dalla presa di corrente in una tensione continua più bassa. Nel servizio radioamatoriale utilizziamo spesso alimentatori che forniscono all'uscita una tensione continua di $\qty{13,8}{\volt}$, per alimentare ad esempio un trasmettitore-ricevitore.

<margin>
[picture:740:n_netzgeraet:Alimentatore]
</margin>

<indepth>
Per il *controllo dello stato di funzionamento* di un alimentatore, ci sono interruttori illuminati, diodi LED di controllo o strumenti di visualizzazione illuminati. Gli strumenti di visualizzazione possono mostrare separatamente la tensione di servizio in volt e l'intensità di corrente attualmente in circolazione in ampere. Esistono anche display digitali commutabili per questo scopo.
</indepth>

[question:ND101]
[question:ND102]

<danger>
Le spine bipolari possono essere utilizzate solo per apparecchi con doppio isolamento di protezione.
</danger>

---
Un alimentatore viene spesso collegato alla presa di rete con una **spina con contatto di protezione**. In Svizzera vengono utilizzati per questo sistemi di spine secondo
*SN 441011*. In una presa tripolare, i tre collegamenti sono previsti per il *conduttore esterno (L)*, il *conduttore neutro (N)* e il *conduttore di protezione (PE)*, come visibile nella figura [NE-10.3.2](https://50ohm.uska.ch/50ohm_review_de/NE_netzgeraet_1.html#ref_n_schutzkontakt). Tra il conduttore esterno L e il conduttore neutro N è presente la tensione di rete di 230 V di tensione alternata.

Il contatto di protezione della spina stabilisce, durante l'inserimento, la connessione al conduttore di protezione PE della presa. "PE" è l'abbreviazione del termine inglese "protective earth", cioè conduttore di protezione o messa a terra di protezione.

Se l'alimentatore è realizzato con un involucro conduttivo e un collegamento per il conduttore di protezione, l'involucro viene collegato tramite il conduttore PE al sistema di conduttori di protezione dell'impianto elettrico. In questo modo, in caso di un guasto di isolamento, una corrente di guasto può fluire attraverso il conduttore di protezione e far scattare il dispositivo di protezione, ad esempio un interruttore magnetotermico o un interruttore differenziale (salvavita). L'involucro rimane così normalmente non permanentemente a una tensione pericolosa. Un collegamento bipolare, cioè senza il conduttore di protezione, è consentito solo se l'apparecchio è a doppio isolamento di protezione.

---

<margin>
[photo:86:n_schutzkontakt:Spina svizzera con e senza conduttore di protezione]
</margin>

[question:ND109]

---

L'uscita dell'alimentatore e il cavo di collegamento al trasmettitore-ricevitore sono progettati in modo bipolare, in modo da ottenere un circuito chiuso. Questa è la condizione necessaria affinché la corrente possa fluire dall'alimentatore al trasmettitore-ricevitore, attraverso di esso e tornare indietro all'alimentatore.

<webmargin>
[picture:680:n_Netzgeraet_TRX:Collegamento di alimentatore e TRX]
</webmargin>

I morsetti di uscita per la tensione continua sono realizzati a colori: il rosso indica il positivo e il nero il negativo. Nel collegamento del cavo al trasmettitore-ricevitore, questa polarità deve essere assolutamente rispettata. Altrimenti può verificarsi un cortocircuito o, nei casi estremi, anche la distruzione del trasmettitore-ricevitore. Solo dopo che tutti i cavi sono stati collegati e la polarità è stata controllata, l'alimentatore dovrebbe essere acceso.

[question:ND104]
[question:ND103]
[question:ND105]
[question:ND106]
[question:ND107]

---

Nell'alimentatore e nel cavo di collegamento al trasmettitore-ricevitore ci sono i cosiddetti fusibili miniatura. Questi possono rilevare un caso di guasto (cortocircuito o sovraccarico) e interrompere il flusso di corrente. Spesso si tratta di fusibili a cartuccia, in cui un filo sottile si fonde quando scorre troppa corrente. Allora il circuito non è più chiuso e non può più scorrere corrente. Si parla allora di un *fusibile bruciato* o, in linguaggio tecnico, anche di un *intervento termico*.

<margin>
[photo:88:n_feinsicherungen:Fusibili miniatura]
</margin>

<indepth>
*Approfondimento:* I fusibili miniatura sono grandi $\qty{5}{\milli\meter} \times \qty{20}{\milli\meter}$ e sono disponibili in diverse versioni. Si differenziano per intensità di corrente e caratteristiche di intervento. I fusibili ritardati vengono sempre utilizzati quando la corrente di avviamento è significativamente più alta della corrente nominale, ad esempio negli alimentatori. Il tempo di intervento del fusibile dipende dall'intensità di corrente e dalla durata del flusso di corrente. Nella tabella [ref:n_feinsicherung] sono riportati i valori usuali per il tempo di intervento. Indicazioni più precise sono fornite dai produttori tramite curve caratteristiche nei loro datasheet.
</indepth>

Dopo che un fusibile a cartuccia è intervenuto e la causa è stata identificata e risolta, deve essere sostituito. I fusibili difettosi però possono essere sostituiti solo con altri identici! In questo caso bisogna prestare attenzione sia all'intensità di corrente che alla cosiddetta caratteristica di intervento, che indica quanto velocemente un fusibile interviene (rapido, mediamente ritardato, ritardato).

<webmargin>
| l: Caratteristica di intervento | l: Segno distintivo | X: Tempo di interruzione |
| rapido | F | max. $\qty{30}{\milli\second}$ |
| mediamente ritardato | MT | max. $\qty{90}{\milli\second}$ |
| ritardato | T | max. $\qty{300}{\milli\second}$ |
[table:n_feinsicherung:Caratteristiche dei fusibili miniatura, tempo di interruzione a dieci volte la corrente nominale]
</webmargin>

<danger>
*ATTENZIONE:* Il ponteggiamento talvolta praticato di un fusibile difettoso, ad esempio con carta stagnola, è inammissibile e molto pericoloso. Esiste il rischio di incendi!
</danger>

Alimentatori di alta qualità spesso hanno anche una limitazione elettronica delle correnti. In caso di cortocircuito, questa fa sì che l'intensità di corrente sia limitata. Questo si chiama *limitazione della corrente di cortocircuito*. Dopo che il guasto è stato eliminato, non è necessario sostituire alcun fusibile.

[question:ND108]
[question:NK305]
