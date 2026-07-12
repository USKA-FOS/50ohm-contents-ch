Un alimentatore converte la tensione alternata di $\qty{230}{\volt}$ dalla presa di corrente in una tensione continua più bassa. Nell'ambito del radioamatore, utilizziamo spesso alimentatori che forniscono una tensione continua di $\qty{13,8}{\volt}$ alla loro uscita, per alimentare ad esempio un trasmettitore-ricevitore.

<margin>
[picture:740:n_netzgeraet:Alimentatore]
</margin>

<indepth>
Per il *controllo dello stato operativo* di un alimentatore, esistono interruttori illuminati, diodi luminosi di controllo o strumenti di visualizzazione illuminati. Gli strumenti di visualizzazione possono indicare separatamente la tensione di servizio in volt e l'intensità di corrente che scorre in ampere. Esistono anche display digitali commutabili per questo scopo.
</indepth>

[question:ND101]
[question:ND102]

---

Un alimentatore viene spesso collegato alla presa di corrente tramite una *spina con contatto di protezione* (in breve spina Schuko). Con la spina con contatto di protezione, la direzione di inserimento non ha importanza, poiché la polarità della tensione alternata cambia continuamente. La spina e la presa hanno ciascuna 3 poli, come si può vedere nella figura [ref:n_schutzkontakt]. I perni della spina si inseriscono nelle aperture della presa e consentono il collegamento ai cosiddetti conduttori L e N, tra i quali si trova la pericolosa tensione alternata di $\qty{230}{\volt}$.

<margin>
[photo:86:n_schutzkontakt:Contatto di protezione su una presa e spina Schuko]
</margin>

Il contatto a slitta esterno della spina Schuko è chiamato *contatto di protezione* (contrassegnato in rosso nella figura [ref:n_schutzkontakt]). Quando la spina viene inserita, il contatto di protezione si collega al cosiddetto *conduttore PE*. "PE" è l'abbreviazione del termine inglese "protective earth", che significa messa a terra di protezione. Quando la spina viene inserita, l'involucro metallico dell'alimentatore viene quindi messo a terra. In questo modo si esclude una tensione pericolosa sull'involucro.

[question:ND109]

---

L'uscita dell'alimentatore e il cavo di collegamento al trasmettitore-ricevitore sono a due poli, in modo da poter formare un circuito chiuso. Questa è la condizione necessaria affinché la corrente possa fluire dall'alimentatore al trasmettitore-ricevitore, attraversarlo e tornare all'alimentatore.

<webmargin>
[picture:680:n_Netzgeraet_TRX:Collegamento di alimentatore e TRX]
</webmargin>

I morsetti di uscita per la tensione continua sono colorati: il rosso indica il positivo e il nero il negativo. Durante il collegamento del cavo al trasmettitore-ricevitore, è assolutamente necessario rispettare questa polarità. Altrimenti, si potrebbe verificare un cortocircuito o, nei casi estremi, persino la distruzione del trasmettitore-ricevitore. Solo dopo che tutti i cavi sono stati collegati e la polarità è stata controllata, l'alimentatore deve essere acceso.

[question:ND104]
[question:ND103]
[question:ND105]
[question:ND106]
[question:ND107]

---

Nell'alimentatore e nel cavo di collegamento al trasmettitore-ricevitore sono presenti delle cosiddette micrifusibili. Questi possono rilevare un guasto (cortocircuito o sovraccarico) e interrompere il flusso di corrente. Spesso si tratta di fusibili a filo, in cui un sottile filo si fonde quando scorre troppa corrente. Il circuito non è più chiuso e non può più scorrere corrente. Si parla quindi di un *fusibile bruciato* o, nel gergo tecnico, di uno *spegnimento termico*.

<margin>
[photo:88:n_feinsicherungen:Micrifusibili]
</margin>

<indepth>
*Approfondimento:* Le micrifusibili sono grandi $\qty{5}{\milli\meter} \times \qty{20}{\milli\meter}$ e disponibili in diverse versioni. Si differenziano per le intensità di corrente e le caratteristiche di intervento. I fusibili a lenta interruzione vengono sempre utilizzati quando la corrente di spunto è significativamente più alta della corrente nominale, ad esempio negli alimentatori. Il tempo di intervento del fusibile dipende dall'intensità di corrente e dalla durata del flusso di corrente. La tabella [ref:n_feinsicherung] elenca i valori comuni per il tempo di intervento. I produttori forniscono informazioni più precise tramite curve caratteristiche nei loro datasheet.
</indepth>

Dopo che un fusibile a filo è intervenuto e si è identificata e risolta la causa, è necessario sostituirlo. I fusibili difettosi devono però essere sostituiti solo con altri identici! È necessario prestare attenzione sia all'intensità di corrente sia alla cosiddetta caratteristica di intervento, che indica la rapidità con cui un fusibile interviene (rapido, semilento, lento).

<webmargin>
| l: Caratteristica di intervento | l: Simbolo | X: Tempo di spegnimento |
| rapido | F | max. $\qty{30}{\milli\second}$ |
| semilento | MT | max. $\qty{90}{\milli\second}$ |
| lento | T | max. $\qty{300}{\milli\second}$ |
[table:n_feinsicherung:Parametri delle micrifusibili, tempo di spegnimento con dieci volte la corrente nominale]
</webmargin>

<danger>
*ATTENZIONE:* Il bypass di un fusibile difettoso, a volte praticato, ad esempio con carta stagnola, è vietato e molto pericoloso. Esiste il rischio di incendi!
</danger>

Gli alimentatori di alta qualità spesso dispongono anche di una limitazione elettronica delle correnti. In caso di cortocircuito, questa garantisce che l'intensità di corrente venga limitata. Questo si chiama *limitazione della corrente di cortocircuito*. Dopo che il guasto è stato eliminato, non è necessario sostituire alcun fusibile.

[question:ND108]
[question:NK305]
