Nella classe E abbiamo già imparato a conoscere le sorgenti di tensione. Prima di tutto vogliamo occuparci della sorgente di corrente, per poi analizzare più in dettaglio la resistenza interna delle sorgenti di tensione e di corrente.

Allo stesso modo di una sorgente di tensione, una sorgente di corrente garantisce che eroghi una corrente il più possibile costante. La figura [ref:a_isource_schematic] mostra il suo schema equivalente.

<margin>
[picture:1058:a_isource_schematic:Schema equivalente sorgente di corrente $R_i$ ad alta impedenza]
</margin>

<indepth>
Analisi di una sorgente di corrente costante, ad esempio di un alimentatore da laboratorio:

[photo:298:a_Strombegrenzung:Alimentatore da laboratorio con limitazione di corrente impostata a $\qty{500}{\milli\ampere}$]

Negli alimentatori da laboratorio è integrata una limitazione di corrente, cioè se la corrente di carico supera un valore massimo, la tensione ai morsetti viene ridotta in modo che la corrente di carico rimanga costante. Questo corrisponde alla funzione di una sorgente di corrente costante: in caso di cortocircuito ai morsetti di uscita, scorre la corrente massima impostata.
</indepth>

Una sorgente di corrente ideale eroga una corrente costante indipendentemente dal carico collegato. In teoria questo è possibile con una resistenza interna infinita. In pratica, le sorgenti di corrente hanno una resistenza interna molto elevata.

<margin>
[picture:1018:a_vsource_schematic:Schema equivalente sorgente di tensione]
</margin>

---

La figura [ref:a_vsource_schematic] mostra uno schema equivalente di una sorgente di tensione. La resistenza interna $R_i$ è in serie alla sorgente di tensione ideale e, in condizioni ideali, dovrebbe essere $\qty{0}{\ohm}$. In pratica, le sorgenti di tensione hanno una resistenza interna piccola.

[question:AB201]

Se una sorgente di tensione reale viene caricata con $R_L$, la tensione ai morsetti $U_k$ diminuisce. La causa è la resistenza interna $R_i$ presente in questa sorgente di tensione. Essa crea, per così dire, un partitore di tensione. Poiché la tensione della sorgente $U_q$ a vuoto, cioè senza carico, è $U_q=U_L$, questa viene anche chiamata tensione a vuoto.

Con un multimetro non è possibile misurare la resistenza interna, ma può essere calcolata tramite la legge di Ohm (cfr. raccolta di formule):

$R_i = \frac{\Delta U}{\Delta I}$

Per il calcolo sono necessari due casi di carico:
1. A vuoto senza carico: $I = \qty{0}{\ampere}$ e $U_L = U_q$
2. Con carico $R_L$: misuriamo $I_L$ e $U_L$

Attraverso la variazione di tensione ($\Delta U = U_q~-~U_L$) ai morsetti e la variazione di corrente di carico ($\Delta I = I_L~-~\qty{0}{\ampere}$), è possibile calcolare la resistenza interna con la formula sopra riportata.

$R_i = \frac{\Delta U}{\Delta I} = \frac{U_q - U_L}{I_L-\qty{0}{\ampere}} = \frac{U_q - U_L}{I_L}$

Con queste conoscenze possiamo rispondere alle seguenti domande d’esame:

[question:AB205]
[question:AB206]
[question:AB207]
[question:AB208]

Riassumiamo:

* Le sorgenti di tensione devono avere una resistenza interna molto bassa $R_i \ll R_L$, in condizioni ideali: $\qty{0}{\ohm}$, in modo che la tensione d’uscita rimanga invariata in caso di carico. Se la tensione ai morsetti rimane costante in caso di carico, si parla di adattamento in tensione.
* Le sorgenti di corrente devono avere una resistenza interna molto elevata $R_i \gg R_L$. In condizioni ideali: $\qty{\infty}{\ohm}$, in modo che la corrente di carico rimanga costante al variare della resistenza di carico; per questo motivo si parla anche di adattamento in corrente.

[question:AB203]
[question:AB204]

---

Se una sorgente di tensione deve erogare la potenza massima a un carico, si parla di adattamento di potenza. Questo è importante, ad esempio, per un trasmettitore che deve trasferire la potenza massima possibile a un’antenna.

La trasmissione di potenza massima si ottiene quando

$R_i = R_L$

cioè quando la resistenza interna e la resistenza di carico sono uguali.

In questo caso la tensione della sorgente si distribuisce uniformemente tra la resistenza interna e il carico. Di conseguenza, sul carico si ottiene il prodotto massimo tra tensione e corrente e, quindi, la potenza più elevata possibile.

La figura [ref:a_Leistungsanpassung] mostra la potenza normalizzata sul carico in funzione del rapporto $R_L/R_i$. Il massimo viene raggiunto esattamente quando $R_L/R_i = 1$, cioè quando la resistenza interna e quella di carico sono uguali. Tuttavia, in caso di adattamento di potenza il rendimento è solo $\qty{50}{\percent}$, poiché la stessa potenza viene dissipata sia sul carico che sulla resistenza interna.

<margin>
[picture:1077:a_Leistungsanpassung:Adattamento ottimale di potenza quando $R_i = R_L$, qui il rapporto $\frac{R_L}{R_i}=1$ e quindi la potenza massima viene erogata al carico. Il grafico è in scala logaritmica.]
[picture:937:a_Leistungsanpassung:Potenza d’uscita ottimale con resistenza di carico $\qty{50}{\ohm}$ e resistenza interna $\qty{50}{\ohm}$. Il grafico non è in scala logaritmica.]
</margin>

<indepth>
Anche le sorgenti di tensione in corrente alternata, ad esempio i generatori di segnale, possiedono una resistenza interna che è indicata sulla presa di uscita.
[photo:292:Sinusgenerator 50 Ohm:Generatore di segnale sinusoidale con resistenza interna $\qty{50}{\ohm}$]
</indepth>

% Forse va spostato altrove?
<indepth>
Il valore di $\qty{50}{\ohm}$, molto diffuso nella tecnica ad alta frequenza, rappresenta un compromesso tecnico tra massima trasmissione di potenza e minime perdite nei cavi.

I cavi coassiali con un’impedenza caratteristica di circa $\qty{30}{\ohm}$ possono trasmettere potenze particolarmente elevate, poiché la corrente nel cavo è distribuita in modo meno intenso. I cavi con circa $\qty{77}{\ohm}$ presentano invece le minori perdite di attenuazione e sono particolarmente adatti per una trasmissione del segnale a basse perdite.

Il valore di $\qty{50}{\ohm}$, oggi molto diffuso, si colloca tra questi due ottimi e rappresenta un buon compromesso tra alta trasmissione di potenza, perdite moderate e costruzione pratica del cavo. Per questo motivo $\qty{50}{\ohm}$ si è affermato come standard nella tecnica radio.

Se un trasmettitore, un cavo e un’antenna sono adattati a $\qty{50}{\ohm}$, la potenza viene trasmessa in modo ottimale e le riflessioni sulla linea vengono minimizzate.

[picture:1078:a_50ohm:50 ohm come compromesso tra massima trasmissione di potenza e minime perdite nella tecnica ad alta frequenza]

Ora sai anche perché il nostro sito si chiama 50ohm.de: vogliamo aiutarti a superare le domande d’esame e ottenere così la potenza ottimale nell’esame 🤓
</indepth>

[question:AG401]
[question:AB202]