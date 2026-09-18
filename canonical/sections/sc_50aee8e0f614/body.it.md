Con l'aiuto di un mixer è possibile convertire una determinata frequenza (o una banda di frequenza con larghezza di banda definita) in una frequenza più alta o più bassa. A questo scopo, i segnali vengono moltiplicati tra loro.

<indepth>
La moltiplicazione di segnali nel dominio del tempo porta a una somma (o sottrazione) nel dominio della frequenza. Questa relazione può essere spiegata in modo intuitivo con la seguente identità trigonometrica (semplificata, i fattori $2\pi\cdot t$ sono stati omessi per chiarezza):

$\sin(f_1)\cdot\sin(f_2) = \frac{1}{2}\left(\cos(f_1-f_2)-\cos(f_1+f_2)\right)$

Se due segnali sinusoidali vengono moltiplicati tra loro – uno con frequenza $f_1$ e uno con frequenza $f_2$ – nel dominio della frequenza si generano due nuovi segnali cosinusoidali (che non sono altro che un seno sfasato). Questi si trovano alle frequenze $f_1 - f_2$ e $f_1 + f_2$. Si può immaginare che una componente di frequenza venga spostata verso il basso e un'altra verso l'alto. È proprio questo principio che sfrutta il mixer.

In questo processo si generano sempre due componenti di frequenza. In pratica, tuttavia, di solito solo una di queste è desiderata, motivo per cui dopo il mixer vengono utilizzati filtri adatti per selezionare il prodotto di miscelazione desiderato. In realtà, nella formazione della differenza possono anche verificarsi frequenze negative, motivo per cui in generale si considera il valore assoluto $| f_1 \pm f_2 |$.
</indepth>

---

Un mixer utilizza componenti non lineari, ad esempio diodi, per moltiplicare tra loro i segnali. In questo modo si generano i cosiddetti prodotti di miscelazione, le cui frequenze corrispondono matematicamente alla somma e alla differenza delle frequenze dei segnali di ingresso.

Grazie a questa proprietà, i mixer vengono impiegati specificamente per convertire i segnali in altre bande di frequenza desiderate – ad esempio per la conversione verso l'alto o verso il basso in trasmettitori e ricevitori. Negli schemi a blocchi, un mixer viene rappresentato, come mostrato nella figura [ref:e_mischer], da un cerchio con un simbolo di moltiplicazione che indica l'effetto moltiplicativo di questo componente.

<margin>
[picture:903:e_mischer:Mixer]
</margin>

---

Le frequenze generate all'uscita di un mixer consistono principalmente nelle due componenti di miscelazione dei segnali forniti $f_\text{e}$, il segnale di ingresso, e $f_\text{o}$, il segnale proveniente da un oscillatore. In questo caso si ottengono due prodotti di miscelazione desiderati come somma e valore assoluto della differenza dei segnali forniti:

$f_\text{z}=|f_\text{e}\pm f_\text{o}|$

A causa del $\pm$ è necessario distinguere i casi: si ottengono quindi $f_\text{z1} = f_\text{e}+f_\text{o}$ e $f_\text{z2}=|f_\text{e}-f_\text{o}|$.

Le barre di valore assoluto $|x|$ indicano che viene considerato solo il valore numerico senza segno. Se $x$ è negativo, viene reso positivo. Se $x$ è già positivo, rimane invariato.

Normalmente, solo uno dei prodotti di miscelazione desiderati viene utilizzato per l'ulteriore elaborazione del segnale. L'altro prodotto di miscelazione (e possibilmente ulteriori prodotti di miscelazione indesiderati – vedi approfondimento) deve essere rimosso dal segnale misto mediante filtraggio.

<indepth>
Un mixer reale genera, oltre ai prodotti di miscelazione desiderati, anche prodotti di miscelazione di ordine superiore come ad esempio $2 * f_\text{in1} + f_\text{in2}$ e così via. Anche questi prodotti di miscelazione indesiderati devono essere rimossi in seguito mediante filtri adatti. Inoltre, nei mixer reali le due frequenze di ingresso non sono completamente soppresse nel segnale di uscita e devono essere prese in considerazione nell'ulteriore elaborazione del segnale. Utilizzando un mixer ad anello bilanciato (balance mixer), i due segnali di ingresso possono essere molto ben soppressi nel segnale di uscita, motivo per cui questo tipo di mixer viene spesso utilizzato.
</indepth>

[question:EF201]

In questa domanda dobbiamo semplicemente sommare e sottrarre la frequenza dell'oscillatore e tenere conto del valore assoluto.

$f_\text{z1} = f_\text{e}+f_\text{o} = \qty{21}{\mega\hertz} + \qty{31,7}{\mega\hertz} = \qty{52,7}{\mega\hertz}$

$f_\text{z2}=|f_\text{e}-f_\text{o}| =|\qty{21}{\mega\hertz} - \qty{31,7}{\mega\hertz}| = |\qty{-10,7}{\mega\hertz}| = \qty{10,7}{\mega\hertz}$

Le domande seguenti funzionano secondo lo stesso principio.

[question:EF202]
[question:EF203]
[question:EF204]
[question:EF205]

Poiché nei mixer vengono generate svariate frequenze durante il processo di miscelazione, *le fasi di miscelazione devono essere sempre ben schermate*, in modo che da queste non avvenga alcuna irradiazione verso altre fasi o dispositivi e, in particolare, non vengano disturbati altri servizi di radiocomunicazione!

[question:EF206]