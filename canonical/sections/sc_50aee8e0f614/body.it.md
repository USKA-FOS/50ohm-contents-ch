Con l'aiuto di un mixer è possibile convertire una frequenza specifica (o un intervallo di frequenze con una larghezza di banda definita) in una frequenza più alta o più bassa. Per fare ciò, i segnali vengono moltiplicati tra loro.

<indepth>
Una moltiplicazione di segnali nel dominio del tempo porta a un'addizione (o sottrazione) nel dominio della frequenza. Questa relazione può essere spiegata in modo intuitivo con la seguente identità trigonometrica (leggermente semplificata, i fattori $2\pi\cdot t$ sono stati omessi per chiarezza):  
  
$\sin(f_1)\cdot\sin(f_2) = \frac{1}{2}\left(\cos(f_1-f_2)-\cos(f_1+f_2)\right)$
  
Se due segnali sinusoidali vengono moltiplicati tra loro – uno con la frequenza $f_1$ e uno con la frequenza $f_2$ – nel dominio della frequenza si creano due nuovi segnali cosinusoidali (che non sono altro che un seno sfasato). Questi si trovano alle frequenze $f_1 - f_2$ e $f_1 + f_2$. Si può pensare che una componente di frequenza venga spostata verso il basso e un'altra verso l'alto. È esattamente questo principio che sfrutta il mixer.

In linea di principio, si creano sempre due componenti di frequenza. In pratica, tuttavia, di solito solo una di esse è desiderata, motivo per cui vengono utilizzati filtri appropriati dopo il mixer per selezionare il prodotto di miscelazione desiderato. A rigor di termini, nella sottrazione possono verificarsi anche frequenze negative, motivo per cui in generale si considera il valore assoluto $| f_1 \pm f_2 |$.
</indepth>

---

Un mixer utilizza componenti non lineari, ad esempio diodi, per moltiplicare i segnali tra loro. In questo processo si creano i cosiddetti prodotti di miscelazione, le cui frequenze corrispondono matematicamente alla somma e alla differenza delle frequenze dei segnali di ingresso.

Grazie a questa proprietà, i mixer vengono utilizzati appositamente per convertire i segnali in altri intervalli di frequenza desiderati, ad esempio per la conversione su o giù in trasmettitori e ricevitori. Negli schemi a blocchi, un mixer, come mostrato nella figura [ref:e_mischer], è simboleggiato da un cerchio con un segno di moltiplicazione, che indica l'effetto moltiplicativo di questo gruppo funzionale.

<margin>
[picture:903:e_mischer:Mischer]
</margin>

---

Le frequenze generate su un'uscita di un mixer consistono principalmente nei due prodotti di miscelazione dei segnali applicati $f_\text{e}$, il segnale di ingresso, e $f_\text{o}$, il segnale proveniente da un oscillatore. In questo caso, si ottengono due prodotti di miscelazione desiderati come somma e valore assoluto della differenza dei segnali applicati:

$f_\text{z}=|f_\text{e}\pm f_\text{o}|$

A causa del $\pm$ è necessario distinguere i casi: si ottiene quindi $f_\text{z1} = f_\text{e}+f_\text{o}$ e $f_\text{z2}=|f_\text{e}-f_\text{o}|$.

Le barre del valore assoluto $|x|$ significano che si considera solo il valore numerico senza segno. Se $x$ è negativo, viene reso positivo. Se $x$ è già positivo, rimane invariato.

Normalmente, solo uno dei prodotti di miscelazione desiderati viene utilizzato per l'ulteriore elaborazione del segnale. L'altro prodotto di miscelazione (così come eventuali altri prodotti di miscelazione indesiderati - vedi approfondimento) deve essere successivamente rimosso dalla miscela di segnali tramite filtraggio.

<indepth>
Un mixer reale genera, oltre ai prodotti di miscelazione desiderati, anche prodotti di miscelazione di ordine superiore come ad esempio $2 * f_\text{in1} + f_\text{in2}$ ecc. Questi prodotti di miscelazione indesiderati devono essere successivamente rimossi tramite filtri adeguati. Anche le due frequenze di ingresso non sono completamente soppresse nel segnale di uscita dei mixer reali e devono essere considerate nell'ulteriore elaborazione del segnale. Utilizzando un mixer ad anello bilanciato (mixer bilanciato), i due segnali di ingresso possono essere fortemente soppressi nel segnale di uscita, motivo per cui questo tipo di mixer viene spesso utilizzato.
</indepth>

[question:EF201]

In questa domanda dobbiamo semplicemente sommare e sottrarre la frequenza dell'oscillatore, tenendo conto del valore assoluto.

$f_\text{z1} = f_\text{e}+f_\text{o} = \qty{21}{\mega\hertz} + \qty{31,7}{\mega\hertz} = \qty{52,7}{\mega\hertz}$

$f_\text{z2}=|f_\text{e}-f_\text{o}| =|\qty{21}{\mega\hertz} - \qty{31,7}{\mega\hertz}| = |\qty{-10,7}{\mega\hertz}| = \qty{10,7}{\mega\hertz}$

Le seguenti domande funzionano secondo lo stesso principio.

[question:EF202]
[question:EF203]
[question:EF204]
[question:EF205]

Poiché nei mixer vengono generate le più svariate frequenze attraverso il processo di miscelazione, gli *stadi mixer devono sempre essere molto ben schermati*, in modo che da essi non possa avvenire alcuna irradiazione verso altri stadi o apparecchi e, in particolare, non vengano disturbati altri servizi radio!

[question:EF206]