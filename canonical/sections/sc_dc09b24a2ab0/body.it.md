Nella sezione [sec:spannungsquelle] abbiamo già conosciuto le sorgenti di tensione. Inizialmente ci occuperemo della sorgente di corrente, prima di esaminare più in dettaglio la resistenza interna delle sorgenti di tensione e di corrente.

Similmente alla sorgente di tensione, una sorgente di corrente garantisce che fornisca possibilmente una corrente costante. La figura [ref:a_isource_schematic] mostra il suo schema equivalente.

<margin>
[picture:1058:a_isource_schematic:Schema equivalente sorgente di corrente $R_i$ ad alta impedenza]
</margin>

<indepth>
Considerazione di una sorgente di corrente costante usando l'esempio di un alimentatore da laboratorio:

[photo:298:a_Strombegrenzung:Alimentatore da laboratorio con limitazione di corrente impostata a $\qty{500}{\milli\ampere}$]

Negli alimentatori da laboratorio è incorporata una limitazione di corrente, cioè se la corrente di carico supera una corrente massima, la tensione ai morsetti viene ridotta in modo che la corrente di carico rimanga costante. Ciò corrisponde alla funzione di una sorgente di corrente costante -- In caso di cortocircuito ai morsetti d'uscita, scorre la corrente massima impostata.
</indepth>

Una sorgente di corrente costante ideale fornisce una corrente continua costante indipendentemente dal carico collegato. In teoria ciò è possibile con una resistenza interna infinita. In pratica le sorgenti di corrente hanno una resistenza interna molto alta.

<margin>
[picture:1018:a_vsource_schematic:Schema equivalente sorgente di tensione]
</margin>

---

La figura [ref:a_vsource_schematic] mostra uno schema equivalente di una sorgente di tensione. La resistenza interna $R_i$ è in serie con la sorgente di tensione ideale e nel caso ideale dovrebbe essere $\qty{0}{\ohm}$. In pratica le sorgenti di tensione hanno una piccola resistenza interna.

[question:AB201]

Quando una sorgente di tensione reale viene caricata con $R_L$, la tensione ai morsetti $U_k$ diminuisce. La ragione è la resistenza interna presente $R_i$ di questa sorgente di tensione. Attraverso di essa si forma praticamente un partitore di tensione. Poiché la tensione della sorgente $U_q$ a vuoto, cioè senza carico, è $U_q=U_L$, questa viene anche chiamata tensione a vuoto.

Con un multimetro la resistenza interna non è misurabile, ma può essere determinata calcolando tramite la legge di Ohm (cfr. raccolta di formule):

$R_i = \frac{\Delta U}{\Delta I}$

Per il calcolo sono necessari due casi di carico:
1. A vuoto senza carico: $I = \qty{0}{\ampere}$ e $U_L = U_q$
2. Carico con $R_L$: Misuriamo $I_L$ e $U_L$

Attraverso la variazione di tensione ($\Delta U = U_q~-~U_L$) ai morsetti e la variazione della corrente di carico ($\Delta I = I_L~-~\qty{0}{\ampere}$), la resistenza interna può essere calcolata secondo la formula sopra.

$R_i = \frac{\Delta U}{\Delta I} = \frac{U_q - U_L}{I_L-\qty{0}{\ampere}} = \frac{U_q - U_L}{I_L}$

Con questa conoscenza possiamo rispondere alle seguenti domande d'esame:

[question:AB205]
[question:AB206]
[question:AB207]
[question:AB208]

Riassumiamo:

* Le sorgenti di tensione dovrebbero avere una resistenza interna molto bassa $R_i \ll R_L$, nel caso ideale: $\qty{0}{\ohm}$, allora la tensione d'uscita rimane invariata sotto carico. Se la tensione ai morsetti rimane costante sotto carico, allora si parla di adattamento di tensione.
* Le sorgenti di corrente dovrebbero avere una resistenza interna molto alta $R_i \gg R_L$. Caso ideale: $\qty{\infty}{\ohm}$, allora la corrente di carico rimane costante al variare della resistenza di carico, perciò si parla anche di adattamento di corrente.

[question:AB203]
[question:AB204]

---

Se una sorgente di tensione deve emettere la potenza massima a un carico, si parla di adattamento di potenza. Ciò è importante ad esempio anche per un trasmettitore, che dovrebbe trasferire la massima potenza a un'antenna.

Il massimo trasferimento di potenza viene raggiunto quando

$R_i = R_L$

vale, cioè quando la resistenza interna e la resistenza di carico sono uguali.

In questo caso la tensione della sorgente si distribuisce uniformemente sulla resistenza interna e sul carico. Ciò produce sul carico il prodotto massimo di tensione e corrente e quindi la potenza più grande possibile.

La figura [ref:a_Leistungsanpassung] mostra la potenza normalizzata sul carico in dipendenza dal rapporto $R_L/R_i$. Il massimo viene raggiunto esattamente a $R_L/R_i = 1$, cioè quando la resistenza interna e la resistenza di carico sono uguali. Tuttavia il rendimento nell'adattamento di potenza è solo $\qty{50}{\percent}$, poiché la stessa potenza viene convertita sia sul carico che sulla resistenza interna.

<margin>
[picture:1077:a_Leistungsanpassung:Adattamento di potenza ottimale a $R_i = R_L$, qui il quoziente $\frac{R_L}{R_i}=1$ e quindi la potenza massima viene emessa al carico. Il grafico è logaritmico.]
[picture:937:a_Leistungsanpassung:Potenza d'uscita ottimale a $\qty{50}{\ohm}$ resistenza di carico con una resistenza interna di $\qty{50}{\ohm}$. Il grafico non è logaritmico.]
</margin>

<indepth>
Le sorgenti di tensione alternata, ad esempio i generatori sinusoidali, possiedono anche una resistenza interna, indicata sulla presa d'uscita.
[photo:292:Sinusgenerator 50 Ohm:Generatore sinusoidale con resistenza interna di 50 ohm]
</indepth>

% EVENTUALMENTE questo deve andare altrove?
<indepth>
Il valore frequentemente utilizzato nella tecnica delle alte frequenze di $\qty{50}{\ohm}$ è un compromesso tecnico tra il massimo trasferimento di potenza e perdite il più possibile basse nei cavi.

I cavi coassiali con un'impedenza caratteristica di circa $\qty{30}{\ohm}$ possono trasmettere potenze particolarmente elevate, poiché la corrente nel cavo viene distribuita in modo minore. I cavi con circa $\qty{77}{\ohm}$ possiedono invece le perdite per attenuazione più basse e sono particolarmente adatti per una trasmissione del segnale a bassa perdita.

Il valore oggi molto diffuso di $\qty{50}{\ohm}$ si trova tra i due ottimi e rappresenta un buon compromesso tra alto trasferimento di potenza, perdite moderate e costruzione pratica del cavo. Perciò i $\qty{50}{\ohm}$ si sono affermati come standard nella tecnica radio.

Se un trasmettitore, un cavo e un'antenna vengono ciascuno adattati a $\qty{50}{\ohm}$, allora la potenza viene trasferita in modo ottimale e le riflessioni sulla linea vengono minimizzate.

[picture:1078:a_50ohm:50 ohm come compromesso tra massimo trasferimento di potenza e perdite minime nella tecnica delle alte frequenze]

Ora sai anche perché la nostra piattaforma si chiama 50ohm.de: Vogliamo aiutarti a padroneggiare le domande d'esame e quindi raggiungere la potenza ottimale nell'esame 🤓
</indepth>

[question:AG401]
[question:AB202]
