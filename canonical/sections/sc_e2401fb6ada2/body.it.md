Un **alimentatore** converte la <i>tensione alternata</i> di $\qty{230}{\volt}$ proveniente dalla presa di corrente in una <i>tensione continua</i> di valore inferiore. Nel <i>radioamatoriale</i> si utilizzano spesso alimentatori che forniscono in <i>uscita</i> una <i>tensione continua</i> di $\qty{13,8}{\volt}$ per alimentare, ad esempio, un <i>trasmettitore-ricevitore</i>.


<margin>
[picture:740:n_netzgeraet:Alimentatore]
</margin>

<indepth>
Per il *controllo dello stato di funzionamento* di un alimentatore esistono <i>interruttori</i> illuminati, spie luminose o strumenti di misura illuminati. Gli strumenti di misura possono visualizzare separatamente la <i>tensione di servizio</i> in volt e l'<i>intensità di corrente</i> che fluisce attualmente in ampere. Esistono anche display digitali commutabili per questo scopo.
</indepth>


[question:ND101]
[question:ND102]

<danger>
Le spine bipolari possono essere utilizzate solo per apparecchi con <i>doppia isolazione</i>.
</danger>

---
Un alimentatore viene spesso collegato alla presa di corrente tramite una **spina con contatto di protezione**. In Svizzera si utilizzano sistemi di spine secondo la norma *SN 441011*. In una presa a tre poli sono previsti tre collegamenti per il *conduttore esterno (L)*, il *neutro (N)* e il *conduttore di protezione (PE)*, come mostrato nella figura [NE-10.3.2](https://50ohm.uska.ch/50ohm_review_de/NE_netzgeraet_1.html#ref_n_schutzkontakt). Tra il conduttore esterno L e il neutro N è presente la <i>tensione alternata</i> di 230 V.


Il contatto di protezione della spina, durante l’inserimento, stabilisce il collegamento con il conduttore di protezione PE della presa. “PE” è l’abbreviazione del termine inglese “<i>protective earth</i>”, cioè conduttore di protezione o messa a terra di protezione.


Se l’alimentatore è dotato di un involucro conduttivo e di un collegamento al conduttore di protezione, l’involucro viene collegato tramite il conduttore PE al sistema di messa a terra dell’impianto elettrico. In questo modo, in caso di guasto all’isolamento, una corrente di guasto può defluire tramite il conduttore di protezione e attivare il dispositivo di protezione, ad esempio un interruttore magnetotermico o un interruttore differenziale (FI). Di norma, l’involucro non rimane permanentemente sotto una <i>tensione</i> pericolosa. Un collegamento bipolare, cioè senza conduttore di protezione, è consentito solo se l’apparecchio è a <i>doppia isolazione</i>.


---

<margin>
[photo:86:n_schutzkontakt:Spina svizzera con e senza conduttore di protezione]
</margin>

[question:ND109]

---

L’<i>uscita</i> dell’alimentatore e il cavo di collegamento al <i>trasmettitore-ricevitore</i> sono realizzati con due poli per consentire la formazione di un circuito chiuso. Questa è la condizione necessaria affinché la corrente possa fluire dall’alimentatore al trasmettitore-ricevitore, attraversarlo e tornare all’alimentatore.


<webmargin>
[picture:680:n_Netzgeraet_TRX:Collegamento tra alimentatore e trasmettitore-ricevitore]
</webmargin>

I morsetti di <i>uscita</i> per la <i>tensione continua</i> sono colorati: il rosso indica il polo positivo e il nero il polo negativo. Durante il collegamento del cavo al trasmettitore-ricevitore, questa polarità deve essere rispettata rigorosamente. In caso contrario, si può verificare un cortocircuito o, nel caso peggiore, la distruzione del trasmettitore-ricevitore. Solo dopo aver collegato tutti i cavi e aver verificato la polarità si deve accendere l’alimentatore.


[question:ND104]
[question:ND103]
[question:ND105]
[question:ND106]
[question:ND107]

---

Nell’alimentatore e nel cavo di collegamento al trasmettitore-ricevitore sono presenti i cosiddetti <i>fusibili miniatura</i>. Questi possono rilevare un guasto (cortocircuito o sovraccarico) e interrompere il flusso di corrente. Spesso si tratta di fusibili a fusione, nei quali un <i>filo</i> sottile si fonde quando scorre una corrente eccessiva. In questo caso, il circuito non è più chiuso e la corrente non può più fluire. Si parla allora di un *fusibile bruciato* o, in termini tecnici, di una *sconnessione termica*.


<margin>
[photo:88:n_feinsicherungen:Fusibili miniatura]
</margin>

<indepth>
*Approfondimento:* I <i>fusibili miniatura</i> misurano $\qty{5}{\milli\meter} \times \qty{20}{\milli\meter}$ e sono disponibili in diverse versioni. Si differenziano per <i>intensità di corrente</i> e caratteristiche di intervento. I fusibili lenti vengono utilizzati quando la corrente di spunto è notevolmente superiore alla corrente nominale, ad esempio negli alimentatori. Il tempo di intervento del fusibile dipende dalla <i>intensità di corrente</i> e dalla durata del flusso di corrente. Nella tabella [ref:n_feinsicherung] sono riportati i valori usuali per il tempo di intervento. Informazioni più precise sono fornite dai produttori tramite le curve caratteristiche nei loro fogli dati.
</indepth>

Dopo che un fusibile a fusione si è attivato e si è individuata e rimossa la causa, è necessario sostituirlo. I fusibili difettosi possono essere sostituiti solo con altri dello stesso tipo! È necessario prestare attenzione sia alla <i>intensità di corrente</i> che alla cosiddetta *caratteristica di intervento*, che indica la velocità con cui un fusibile interviene (istantaneo, medio, lento).


<webmargin>
| l: Caratteristica di intervento | l: Simbolo | X: Tempo di intervento |
| istantaneo | F | max. $\qty{30}{\milli\second}$ |
| medio | MT | max. $\qty{90}{\milli\second}$ |
| lento | T | max. $\qty{300}{\milli\second}$ |
[table:n_feinsicherung:Parametri dei fusibili miniatura, tempo di intervento a dieci volte la corrente nominale]
</webmargin>

<danger>
*ATTENZIONE:* È vietato e molto pericoloso bypassare un fusibile difettoso, ad esempio con un foglio di alluminio. Esiste il rischio di incendio!
</danger>

<attention>
*ATTENZIONE:* Se un apparecchio radio viene collegato direttamente alla batteria dell’auto, sia il cavo positivo che quello negativo devono essere protetti da un fusibile. I fusibili devono essere installati il più vicino possibile alla batteria.

Il fusibile nel cavo negativo protegge il cavo nel raro caso in cui il normale collegamento di massa della batteria al veicolo sia interrotto e una forte corrente del veicolo possa fluire attraverso un altro collegamento di massa dell’apparecchio radio.
</attention>

Gli alimentatori di alta qualità dispongono spesso anche di una <i>limitazione</i> elettronica della corrente. In caso di cortocircuito, questa garantisce che l'<i>intensità di corrente</i> sia limitata. Questo si chiama *limitazione della corrente di cortocircuito*. Dopo aver eliminato il guasto, non è necessario sostituire alcun fusibile.


[question:ND108]
[question:NK305]