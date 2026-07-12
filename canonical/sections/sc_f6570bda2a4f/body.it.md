Per calcolare la distanza di sicurezza esiste una formula approssimata. La troviamo nella raccolta di formule: 

$ E = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{d} $

Questa può essere rapidamente riorganizzata per la distanza di sicurezza $d$: 

$ d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{E} $

La raccolta di formule contiene un'ulteriore nota, secondo cui la formula sopra è valida solo per calcoli nel campo lontano (o campo vicino radiante) a partire da $ d > \frac{\lambda}{2\pi} $.

Ciò è dovuto al fatto che solo nel campo lontano il campo elettrico e quello magnetico hanno una relazione di fase fissa e costante tra loro. Nel campo vicino reattivo, al contrario, possono verificarsi localmente forti aumenti sia del campo elettrico che di quello magnetico. Questi effetti non possono essere rilevati in modo affidabile con le formule approssimate per il campo lontano. Per i calcoli nel campo vicino reattivo, cioè per distanze $d \le \frac{\lambda}{2\pi}$, sono generalmente necessarie simulazioni numeriche. Con delle limitazioni (non per antenne magnetiche, non per antenne molto corte) i risultati sono utilizzabili anche nel campo vicino radiante.

<indepth>
Il campo lontano di una sorgente di radiazione è l'area in cui i vettori dell'intensità di campo elettrico ($E$) e dell'intensità di campo magnetico ($H$) sono perpendicolari tra loro e non presentano differenze di fase. 

Il confine tra campo lontano e campo vicino dipende principalmente dalla lunghezza d'onda. Il campo lontano si forma, secondo le [spiegazioni sulla BEMFV](https://50ohm.de/ebemfv), a una distanza di circa $4\cdot\lambda$. 

Il campo vicino è suddiviso in campo vicino *reattivo* e campo vicino *radiante*. In pratica, nel campo vicino radiante è comunque possibile utilizzare la formula per il campo lontano. Ciò è dovuto al fatto che la formula approssimata fornisce qui stime molto conservative, il che significa che le intensità di campo effettive sono inferiori a quelle calcolate. Si è dalla parte sicura. 
  
Con la formula $ d > \frac{\lambda}{2\pi} $ ci assicuriamo quindi di essere al di fuori del *campo vicino reattivo*.
</indepth>

%TODO Applet basteln: https://www.leifiphysik.de/elektrizitaetslehre/elektromagnetische-wellen/versuche/dipolstrahlung-animation

La seguente domanda si riferisce a questo argomento:

[question:EK105]

Per $\qty{3,5}{\mega\hertz}$ il campo lontano (campo vicino radiante) inizia a $\qty{13,64}{\meter}$.

 $\begin{split} d &> \frac{\lambda}{2 \cdot \pi}\\ d &> \frac{\qty{85,7}{\meter}}{2 \cdot \pi}\\ d &> \qty{13,64}{\meter}\end{split}$
 
La distanza determinata di $\qty{3,65}{\meter}$ si trova chiaramente nel campo vicino reattivo ed è quindi non valida. Invece della formula approssimata per il campo lontano, deve essere scelto un altro metodo. Sono possibili misurazioni delle componenti del campo E e H, simulazioni o calcoli nel campo vicino.

Affinché la seguente domanda possa essere risposta, è necessario calcolare dove inizia il campo lontano (campo vicino radiante) per la banda dei $\qty{160}{\meter}$ e degli $\qty{80}{\meter}$.

[question:EK106]

Per $\qty{160}{\meter}$ vale: $d > \frac{\qty{160}{\meter}}{2\pi} = \qty{25,5}{\meter}$
 
Per $\qty{80}{\meter}$ vale: $d > \frac{\qty{80}{\meter}}{2\pi} = \qty{12,7}{\meter}$

Il calcolo non è valido se la distanza per $\qty{160}{\meter}$ è inferiore a $\qty{25,5}{\meter}$ e per $\qty{80}{m}$ è inferiore a $\qty{12,7}{\meter}$.

%%%%

Nella seguente domanda deve ora essere calcolata per la prima volta una distanza di sicurezza corretta. 

[question:EK108]

Innanzitutto dobbiamo calcolare la potenza irradiata in $P_\textrm{EIRP}$. Inoltre, notiamo che il guadagno d'antenna è indicato in $\unit{\dBd}$. A tal fine utilizziamo nuovamente la formula della raccolta di formule:

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{100}{W} \cdot 10^{\frac{\qty{7,5}{\dBd}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{653}{\watt}$

La somma dei guadagni e delle attenuazioni dell'intero sistema d'antenna è il guadagno d'antenna di $\qty{7,5}{\dBd}$, meno l'attenuazione del cavo di $\qty{1,5}{\dB}$ e più il guadagno di $\qty{2,15}{\dBi}$ per il radiatore isotropo (il guadagno d'antenna si riferisce al dipolo).

In alternativa, come già fatto nei capitoli precedenti, possiamo determinare i rispettivi fattori per i guadagni e l'attenuazione.
$\qty{7,5}{\dB} - \qty{1,5}{dB} = \qty{6}{\dB}$, che corrisponde a un fattore di $\num{4}$. Il fattore per $\qty{2,15}{\dBi}$ è $\num{1,64}$.

$P_\textrm{EIRP} = \qty{100}{\watt} \cdot 4 \cdot 1,64 = \qty{656}{\watt}$

---

I risultati dei due percorsi di calcolo dovrebbero essere uguali. Tuttavia, differiscono leggermente. Questo è il risultato degli arrotondamenti dei due fattori. La potenza calcolata con arrotondamento è comunque sufficientemente precisa per risolvere correttamente la domanda. Inseriamo quindi questo valore nella formula della distanza:

$ d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{E} = \frac{\sqrt{\qty{30}{\ohm}\cdot \qty{656}{\watt}}}{\qty{28}{\volt\per\meter}} \approx \qty{5}{\meter}  $

La distanza di sicurezza di $\qty{5}{\meter}$ è stata determinata con la formula per il campo lontano. Pertanto, è valida solo se si trova nel campo lontano (o campo vicino radiante). Questo può essere verificato rapidamente come sopra.

$\begin{split} d &> \frac{\lambda}{2\pi}\\ d &> \frac{\qty{10}{\meter}}{2\pi}\\ d &> \qty{1,6}{\meter} \end{split}$

La distanza di sicurezza calcolata di $\qty{5}{\meter}$ è maggiore di $\qty{1,6}{\meter}$ e si trova chiaramente nel campo lontano (o campo vicino radiante). Il calcolo è quindi valido. La risposta corretta è $\qty{5}{\meter}$.

<indepth>
Nella tabella, per $\qty{6}{\dB}$ c'è un fattore di $\num{4}$. Questo è un valore arrotondato e in realtà è $\num{3,981071706}$. Ecco perché si verifica l'errore di arrotondamento.
</indepth>
