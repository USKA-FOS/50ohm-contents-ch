Un *filtro a tacca (Notch-Filter)* è un filtro a banda molto stretta che serve a sopprimere una frequenza specifica nello spettro BF del segnale ricevuto. Questo serve, ad esempio, per eliminare selettivamente una portante disturbante in una trasmissione, lasciando quasi inalterato il resto della trasmissione. I filtri a tacca possono essere realizzati sia nella banda BF che nella banda IF. I filtri nella banda IF presentano il vantaggio di poter attenuare in modo più efficace i segnali disturbanti più forti e ridurne l’influenza sull’AGC.

[question:EF215]

<margin>
[picture:242:frequenzverlauf_notchfilter:Caratteristica di risposta in frequenza di un filtro a tacca]
</margin>

---

La caratteristica di risposta in frequenza di un filtro a tacca è progettata in modo che solo una piccola parte della frequenza del segnale BF venga attenuata in modo molto marcato. Questo crea una tacca nello spettro. Da qui il nome "filtro a tacca".

[question:EF216]

<tip>
Molti dispositivi moderni implementano i filtri a tacca utilizzando tecnologie di filtraggio digitale. In questo caso, è spesso possibile parametrizzare con precisione la larghezza di banda, la caratteristica del filtro e la frequenza. Un ulteriore vantaggio in questo contesto sono i cosiddetti *filtri a tacca automatici*, che rilevano automaticamente le componenti fisse della portante nel segnale BF e le eliminano automaticamente.
</tip>