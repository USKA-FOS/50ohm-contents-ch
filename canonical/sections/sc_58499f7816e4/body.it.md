Un *filtro notch (filtro a tacca)* è un filtro a banda molto stretta che deve sopprimere una frequenza specifica nello spettro BF del segnale ricevuto. Ciò serve, ad esempio, a eliminare selettivamente una portante disturbante in una trasmissione, lasciando il resto della trasmissione quasi inalterato. I filtri notch possono essere realizzati sia nel campo BF che nel campo IF. I filtri nel campo IF hanno il vantaggio di poter sopprimere in modo più efficace i segnali di disturbo particolarmente forti e di ridurne l'influenza sull'AGC.

[question:EF215]

<margin>
[picture:242:frequenzverlauf_notchfilter:Caratteristica di filtro di un filtro notch]
</margin>

---

La caratteristica di filtro di un filtro notch è progettata in modo tale che solo una piccola parte della frequenza del segnale BF venga fortemente soppressa. Ciò crea una tacca nello spettro. Da qui il nome filtro notch.

[question:EF216]

<tip>
Molti dispositivi moderni realizzano filtri notch utilizzando la tecnologia dei filtri digitali. In questo caso, la larghezza di banda, la caratteristica del filtro e la frequenza possono spesso essere parametrizzate con precisione. Un ulteriore vantaggio in questo contesto sono i cosiddetti filtri auto-notch, che riconoscono automaticamente le componenti di portante fisse nel segnale BF e le escludono automaticamente.
</tip>