Nella classe E abbiamo imparato che un oscilloscopio visualizza l’andamento temporale delle tensioni. Possiamo quindi utilizzare un oscilloscopio per verificare l’andamento dei segnali. 

[question:AI301]

<margin>
[picture:1005:a_impulsbreite:Determinazione della durata dell’impulso di un segnale rettangolare non ideale]
</margin>

---

Oltre alle tensioni alternate sinusoidali, grazie alla tecnologia digitale si utilizzano anche tensioni di forma rettangolare. Tuttavia, non esiste un andamento di tensione perfettamente rettangolare: i bordi sono sempre leggermente inclinati o deformati. Il tempo tra la salita e la discesa di un segnale rettangolare, chiamato durata dell’impulso o durata dell’impulso, viene quindi sempre misurato a metà altezza, cioè al 50% della tensione. In questo modo, tutti ottengono lo stesso risultato di misura per lo stesso segnale.

<indepth>
La causa di queste deformazioni sono le inevitabili capacità e induttanze nei cavi e nei componenti, che agiscono come filtri attenuando le componenti ad alta frequenza di un segnale rettangolare.
</indepth>

[question:AI303]
[question:EI303]



Gli oscilloscopi possono visualizzare segnali con le frequenze e le forme più disparate. Affinché questi segnali appaiano stabili sullo schermo, gli oscilloscopi sono dotati di un dispositivo di trigger (in inglese *trigger* = "attivare"). In questo caso, l’apparecchio monitora continuamente il segnale d’ingresso e avvia la registrazione esattamente quando viene soddisfatta una condizione precedentemente definita, ad esempio quando il segnale supera una determinata tensione, chiamata tensione di trigger. Da quel momento inizia il campionamento e la memorizzazione dei valori di misura, che vengono poi visualizzati come curva sullo schermo.


Grazie a questo procedimento, ogni visualizzazione inizia sempre nello stesso stato del segnale, in modo che i segnali periodici come le oscillazioni sinusoidali o gli impulsi rettangolari appaiano "congelati" e chiaramente riconoscibili. Gli oscilloscopi digitali possono inoltre visualizzare anche singole immagini, "congelando" quindi lo schermo. Questo facilita l’analisi di segnali non periodici. Il tasto adibito a questa funzione è solitamente etichettato con *SINGLE*. Inoltre, è possibile sovrapporre più misurazioni per visualizzare, ad esempio, le fluttuazioni temporali di un segnale (in inglese *jitter*).


[question:AI302]


%<indepth>
%Abbildung [ref:a_oszilloskop_einzelbild] mostra un’immagine singola tratta dalla registrazione musicale di Abbildung [ref:a_oszilloskop_ueberlagerung]. È stata fotografata da un oscilloscopio più vecchio, che funziona principalmente in modo analogico e dispone di una piccola memoria digitale.
%[photo:222:a_oszilloskop_einzelbild:Immagine singola tratta da una registrazione musicale]
%</indepth>

Non tutti i cavi sono adatti per i segnali ad alta frequenza, nemmeno per la connessione tra l’oggetto di misura e l’oscilloscopio. Per questo, di norma si utilizzano le cosiddette sonde. Queste stabiliscono la connessione e garantiscono che il segnale venga trasmesso il più fedelmente possibile, senza caricare eccessivamente il circuito. A tal fine, riducono la tensione del segnale (ad esempio nel rapporto 10:1), adattano resistenza e capacità e spesso includono una compensazione per le alte frequenze.

Una sonda è costituita da un involucro simile a una penna, paragonabile a una sfera. Alla sua estremità possono essere montati ganci o aghi per contattare il punto di misura. La connessione di massa avviene tramite una pinza a coccodrillo (vedi Abbildung [ref:a_oszilloskop_messung]). Abbildung [ref:a_oszilloskop_tastkoepfe] mostra tre esempi di tali sonde. I modelli di alta qualità sono piuttosto costosi, poiché devono offrire un’ampia larghezza di banda, una minima distorsione del segnale e una meccanica precisa.

<margin>
[photo:224:a_oszilloskop_messung:Misurazione con una sonda. Tra i diodi D1 e D2 si vede la punta di prova e, più a sinistra, la pinza a coccodrillo per la connessione di massa.]
</margin>

<margin>
[photo:223:a_oszilloskop_tastkoepfe:Sonde con punte di prova diverse. Le pinze a coccodrillo sono state rimosse per questa foto.]
</margin>

Le sonde più semplici collegano direttamente la punta di prova all’ingresso di misura. Si parla di sonde 1:1, poiché la tensione presente alla punta viene trasmessa all’oscilloscopio senza alterazioni. Le sonde per alte frequenze sono costruite in modo più complesso. Suddividono la tensione d’ingresso in un valore più piccolo, spesso un decimo. Se si misura una tensione di 10 volt con una sonda 10:1, sullo schermo viene visualizzato 1 volt.

<indepth>
In alcuni oscilloscopi è possibile impostare il rapporto di divisione della sonda. In questo caso, sullo schermo viene visualizzata la tensione reale. Le sonde passive 10:1 contengono, tra l’altro, una resistenza da $\qty{9}{\mega\ohm}$ posizionata nel percorso del segnale. Gli oscilloscopi hanno generalmente una resistenza interna di $\qty{1}{\mega\ohm}$. In questo modo si ottiene un partitore di tensione 10:1. Inoltre, nella sonda o nella spina è presente un piccolo condensatore variabile. Questo serve per adattare la capacità della sonda e del cavo all’ingresso di misura e viene regolato in modo che un segnale rettangolare appaia il più fedelmente possibile sullo schermo. Oltre alle sonde passive descritte qui, ne esistono diverse altre varianti. Ad esempio, esistono sonde con cavo coassiale adattato a $\qty{50}{\ohm}$. Queste sono particolarmente adatte per frequenze molto elevate, ma hanno una resistenza interna relativamente bassa. Le versioni attive risolvono questo problema amplificando direttamente il segnale nella sonda.
</indepth>
