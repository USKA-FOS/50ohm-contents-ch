Il diodo Zener stabilizza la tensione al terminale sinistro di $R_2$ a

$U_Z=\qty{6,2}{\volt}$

Se il cursore di $R_3$ è alla posizione 1, il cursore è direttamente collegato al terminale superiore di $R_3$. Da questo punto verso massa ci sono due rami in parallelo:

$R_4=\qty{6,8}{\kilo\ohm}$

e

$R_3+R_6=\qty{220}{\ohm}+\qty{150}{\ohm}=\qty{370}{\ohm}$

La resistenza equivalente verso massa risulta quindi:

$R_\mathrm{u}=R_4\parallel(R_3+R_6)$

$R_\mathrm{u}=\frac{\qty{6800}{\ohm}\cdot\qty{370}{\ohm}}{\qty{6800}{\ohm}+\qty{370}{\ohm}}\approx\qty{351}{\ohm}$

Ora va considerato anche $R_2=\qty{270}{\ohm}$. $R_2$ e $R_\mathrm{u}$ formano un partitore di tensione sulla tensione stabilizzata di $\qty{6,2}{\volt}$:

$U_\mathrm{G}=\qty{6,2}{\volt}\cdot\frac{\qty{351}{\ohm}}{\qty{270}{\ohm}+\qty{351}{\ohm}}\approx\qty{3,5}{\volt}$

Poiché i terminali di source dei transistor sono collegati a massa, la tensione di gate corrisponde contemporaneamente alla tensione gate-source:

$U_\mathrm{GS}\approx\qty{3,5}{\volt}$

La tensione gate-source risulta quindi pari a circa $\qty{3,5}{\volt}$.

A proposito:

La resistenza $R_5=\qty{51}{\ohm}$ non influisce praticamente sulla tensione continua al gate, poiché nel gate del transistor LDMOS non scorre quasi corrente continua. Tuttavia, per il segnale RF, $R_5$ è importante: insieme alla capacità di gate smorza possibili oscillazioni ad alta frequenza e migliora così la stabilità dell’amplificatore.

La resistenza $R_4=\qty{6,8}{\kilo\ohm}$ garantisce che il gate, anche in caso di interruzione della polarizzazione, abbia un potenziale definito rispetto a massa. Inoltre, scarica la capacità di gate e impedisce che il transistor diventi conduttivo in modo involontario a causa di un gate flottante. Poiché $R_4$ è in parallelo al ramo inferiore del partitore di tensione, deve essere considerato nel calcolo preciso della tensione di gate.