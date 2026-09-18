Per calcolare la distanza di sicurezza esiste una formula approssimata. La troviamo nella raccolta di formule:

$ E = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{d} $

Questa può essere rapidamente riorganizzata per ottenere la distanza di sicurezza $d$:

$ d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{E} $

Nella raccolta di formule c'è anche un'indicazione secondo cui la formula sopra vale solo per calcoli nel campo lontano (o nel campo vicino radiante) a partire da $ d > \frac{\lambda}{2\pi} $.

Questo perché solo nel campo lontano il campo elettrico e quello magnetico presentano una relazione di fase fissa e costante tra loro. Nel campo vicino reattivo, invece, possono verificarsi localmente forti picchi sia del campo elettrico che di quello magnetico. Questi effetti non possono essere rilevati in modo affidabile con le formule approssimate per il campo lontano. Per calcoli nel campo vicino reattivo, cioè per distanze $d \le \frac{\lambda}{2\pi}$, sono generalmente necessarie simulazioni numeriche, ad esempio con [EZNEC](https://www.eznec.com/) o [Grasp/TICRA Student-Edition](https://www.ticra.com/software/ticra-tools-student-edition/). L'uso di simulatori numerici non è rilevante per l'esame, ma può essere importante in seguito nella pratica per la valutazione delle antenne. Con alcune limitazioni (non per antenne magnetiche, non per antenne molto corte), i risultati sono utilizzabili anche nel campo vicino radiante.

<indepth>
Il campo lontano di una sorgente di radiazione è la regione in cui i vettori dell'intensità di campo elettrico ($E$), dell'intensità di campo magnetico ($H$) sono perpendicolari tra loro e non presentano sfasamenti.

Il confine tra campo lontano e campo vicino dipende principalmente dalla lunghezza d’onda. Informazioni sul calcolo dell'intensità di campo si trovano nel [foglio di formule per la dichiarazione di emissione per impianti di radioamatore](https://uska.ch/wp-content/uploads/2016/06/Formelblatt_d_08-02-21.pdf).

Informazioni dettagliate sulla creazione di una dichiarazione di emissione concreta sono disponibili presso l'USKA alla pagina [**Calcolo delle emissioni**](https://uska.ch/emissions-berechnung/) e la procedura è descritta nella [guida alla dichiarazione di emissione per impianti di radioamatore](https://uska.ch/wp-content/uploads/2016/06/Wegleitung_d_08-03-02_Rev_A-1.pdf).

% Fonte tedesca rimossa: [Spiegazioni sulla BEMFV](https://50ohm.de/ebemfv)

Il campo vicino si divide in *campo vicino reattivo* e *campo vicino radiante*. In pratica, nel campo vicino radiante è comunque possibile utilizzare la formula per il campo lontano. Questo perché la formula approssimata fornisce qui stime molto conservative, cioè le intensità di campo effettive sono inferiori a quelle calcolate. Ci si trova quindi sul lato sicuro.

Con la formula $ d > \frac{\lambda}{2\pi} $ garantiamo quindi di essere al di fuori del *campo vicino reattivo*.
</indepth>

%TODO Creare applet: https://www.leifiphysik.de/elektrizitaetslehre/elektromagnetische-wellen/versuche/dipolstrahlung-animation

<tip>
La dichiarazione di emissione non deve essere presentata; tuttavia, deve essere disponibile su richiesta, ad esempio in caso di disturbi causati, per essere mostrata.
</tip>

La domanda seguente si riferisce a questo argomento:

[question:EK105]

Per $\qty{3,5}{\mega\hertz}$ il campo lontano (campo vicino radiante) inizia solo a $\qty{13,64}{\meter}$.

$\begin{split} d &> \frac{\lambda}{2 \cdot \pi}\\ d &> \frac{\qty{85,7}{\meter}}{2 \cdot \pi}\\ d &> \qty{13,64}{\meter}\end{split}$

La distanza calcolata di $\qty{3,65}{\meter}$ si trova chiaramente nel campo vicino reattivo ed è quindi non valida. Al posto della formula approssimata per il campo lontano, deve essere scelta un'altra metodologia. Sono possibili misurazioni delle componenti di campo E e H, simulazioni o calcoli del campo vicino.

Per rispondere alla domanda successiva, è necessario calcolare dove inizia il campo lontano (campo vicino radiante) per la banda dei $\qty{160}{\meter}$ e $\qty{80}{\meter}$.

[question:EK106]

Per $\qty{160}{\meter}$ vale: $d > \frac{\qty{160}{\meter}}{2\pi} = \qty{25,5}{\meter}$

Per $\qty{80}{\meter}$ vale: $d > \frac{\qty{80}{\meter}}{2\pi} = \qty{12,7}{\meter}$

Il calcolo non è valido se la distanza per $\qty{160}{\meter}$ è inferiore a $\qty{25,5}{\meter}$ e per $\qty{80}{\meter}$ è inferiore a $\qty{12,7}{\meter}$.

%%%%

Nella domanda seguente, per la prima volta, deve essere calcolata una distanza di sicurezza reale.

[question:EK108]

Innanzitutto dobbiamo calcolare la potenza irradiata $P_\textrm{EIRP}$. Inoltre, notiamo che il guadagno d'antenna è indicato in $\unit{\dBd}$. A questo scopo utilizziamo nuovamente la formula dalla raccolta di formule:

$P_\text{EIRP} = P_\text{trasmettitore} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{100}{\watt} \cdot 10^{\frac{\qty{7,5}{\dBd}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{653}{\watt}$

La somma dei guadagni e delle attenuazioni dell'intero sistema d'antenna corrisponde al guadagno d'antenna di $\qty{7,5}{\dBd}$, meno l'attenuazione del cavo di $\qty{1,5}{\dB}$ e più il guadagno di $\qty{2,15}{\dBi}$ per il radiatore isotropico (il guadagno d'antenna si riferisce al dipolo).

In alternativa, come già nei capitoli precedenti, possiamo determinare i fattori corrispondenti per i guadagni e le attenuazioni.
$\qty{7,5}{\dB} - \qty{1,5}{dB} = \qty{6}{\dB}$, che corrisponde a un fattore di $\num{4}$. Il fattore per $\qty{2,15}{\dBi}$ è $\num{1,64}$.

$P_\textrm{EIRP} = \qty{100}{\watt} \cdot 4 \cdot 1,64 = \qty{656}{\watt}$

---

I risultati dei due metodi di calcolo dovrebbero essere uguali. Tuttavia, differiscono leggermente a causa degli arrotondamenti dei due fattori. Tuttavia, la potenza calcolata con l'arrotondamento è sufficientemente precisa per risolvere correttamente la domanda. Inseriamo quindi questo valore nella formula della distanza:

$ d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{E} = \frac{\sqrt{\qty{30}{\ohm}\cdot \qty{656}{\watt}}}{\qty{28}{\volt\per\meter}} \approx \qty{5}{\meter}  $

La distanza di sicurezza di $\qty{5}{\meter}$ è stata calcolata con la formula per il campo lontano. Pertanto, è valida solo se si trova effettivamente nel campo lontano (o nel campo vicino radiante). Verifichiamo rapidamente anche questo.

$\begin{split} d &> \frac{\lambda}{2\pi}\\ d &> \frac{\qty{10}{\meter}}{2\pi}\\ d &> \qty{1,6}{\meter} \end{split}$

La distanza di sicurezza calcolata di $\qty{5}{\meter}$ è maggiore di $\qty{1,6}{\meter}$ ed è chiaramente nel campo lontano (o nel campo vicino radiante). Il calcolo è quindi valido. La risposta corretta è $\qty{5}{\meter}$.

<indepth>
Nella tabella [sec:dezibel_1] per $\qty{6}{\dB}$ è indicato un fattore di $\num{4}$. Questo è un valore arrotondato e in realtà corrisponde a $\num{3,981071706}$. Ecco perché si verifica l'errore di arrotondamento.
</indepth>
