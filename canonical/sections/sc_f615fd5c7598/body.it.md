Come abbiamo visto nei paragrafi precedenti, i transistor hanno una curva caratteristica che rappresenta la relazione tra il segnale di ingresso (tensione base-emettitore o gate-source) e il segnale di uscita (corrente di collettore/drain). In questa curva caratteristica esistono diverse sezioni in cui il transistor presenta una risposta lineare o non lineare. Le aree della curva caratteristica in cui una variazione della grandezza di controllo provoca una variazione proporzionale della grandezza di uscita sono definite lineari. In rappresentazione lineare, queste aree sono riconoscibili da un andamento rettilineo, senza curvature. Altre aree della curva caratteristica, in cui una variazione della grandezza di controllo **non** provoca una variazione proporzionale della grandezza di uscita, sono definite non lineari.

<margin>
[picture:1085:a_kennlinien_transistor_arbeitspunkt:Curva caratteristica semplificata di un transistor con diversi punti di funzionamento]  
</margin>

La tensione di polarizzazione alla base o al gate imposta inizialmente il punto di funzionamento a riposo del transistor. Insieme all’ampiezza del segnale di ingresso, questo determina su quale porzione della curva caratteristica viene pilotato il transistor e per quale frazione di un periodo del segnale scorre corrente. Da ciò derivano le classi di amplificazione A, A/B, B e C con proprietà diverse in termini di rendimento, linearità, angolo di conduzione e contenuto di armoniche. La figura [ref:a_kennlinien_transistor_arbeitspunkt] mostra i tipici punti di funzionamento a riposo delle diverse classi di amplificazione per le modalità operative A, B, A/B e C. Attraverso la struttura dell’intero circuito di amplificazione, è possibile sfruttare consapevolmente i rispettivi vantaggi o compensare parzialmente gli svantaggi. Nei paragrafi seguenti esamineremo le diverse classi di amplificazione.

[question:AD416]

---

% Modalità operativa A dell’amplificatore:

Nella *modalità operativa A* il punto di funzionamento viene scelto in modo che il transistor rimanga in conduzione per l’intero periodo del segnale (angolo di conduzione $\qty{360}{\degree}$). Per ottenere un pilotaggio ampio e simmetrico, il punto di funzionamento a riposo si trova spesso approssimativamente al centro della retta di lavoro, cioè tra interdizione e saturazione, in modo che il transistor operi completamente nella regione lineare. L’amplificazione del segnale di ingresso (cfr. [ref:a_eingangsspannung]) avviene quindi intorno al punto di funzionamento desiderato, che definisce il centro dell’area di lavoro. La scelta del punto di funzionamento determina una corrispondente corrente di riposo ($I_\mathrm{A}$) del transistor (cfr. [ref:a_ausgangsstrom_a]). Questa corrente scorre anche in assenza di segnale di ingresso. La corrente di riposo influisce in modo significativo sull’efficienza di un amplificatore, poiché ne aumenta la potenza dissipata termicamente e riduce quindi il suo rendimento. Nella modalità operativa A si ottiene generalmente un rendimento di circa $\eta = \qty{40}{\percent}$, che per un amplificatore lineare è un buon valore. Il contenuto di armoniche nella modalità operativa A è molto basso, poiché il transistor opera completamente nella regione lineare.

Tutti i segnali la cui informazione di modulazione è contenuta nell’ampiezza devono essere generalmente amplificati in modo lineare per trasmettere l’informazione senza distorsioni (SSB, AM, ecc.). Tuttavia, esistono anche trucchi circuitali che permettono di evitare la necessità di una modalità operativa A lineare. I segnali la cui informazione di modulazione non è contenuta nell’ampiezza ma solo nella frequenza possono essere amplificati anche nella regione non lineare di un amplificatore (FM, ecc.) e poi filtrati.

Riepilogo modalità operativa A:

- Rendimento circa $\qty{40}{\percent}$
- Contenuto di armoniche molto basso
- Adatto per AM e SSB
- Una corrente di uscita scorre per l’intero periodo (angolo di conduzione $\Theta =\qty{360}{\degree}$) del segnale di ingresso

<margin>
[picture:1086:a_eingangsspannung:Esempio di una tensione di ingresso RF $U_\mathrm{BE}$ di un transistor]
[picture:1087:a_ausgangsstrom_a:Esempio di una corrente di uscita RF $I_\mathrm{C}$ di un transistor in modalità operativa A]
</margin>

[question:AD419]

% Modalità operativa B dell’amplificatore:

Se il punto di funzionamento viene scelto per la *modalità operativa B*, il transistor si trova idealmente proprio al punto di interdizione. Senza segnale di ingresso, quindi, non scorre praticamente alcuna corrente di riposo. Con un pilotaggio sinusoidale, come mostrato nella figura [ref:a_eingangsspannung], il transistor inizia a condurre solo a partire da una certa tensione di ingresso. Un singolo transistor è quindi attivo solo durante una semionda, ovvero per un angolo di conduzione di $\qty{180}{\degree}$.
Poiché nello stato di riposo non viene assorbita quasi alcuna potenza, il rendimento teorico di un amplificatore ideale in modalità B può arrivare fino a circa $\qty{80}{\percent}$. Tuttavia, l’andamento della corrente di un singolo transistor non è più sinusoidale e contiene quindi un elevato contenuto di armoniche.

Per ridurre o sopprimere le armoniche, in pratica esistono diverse soluzioni:

- Una possibilità è un circuito push-pull, in inglese *push-pull amplifier*, con due transistor, come mostrato nella figura [ref:a_gegentakt]. In questo caso, ogni transistor amplifica una semionda, in modo che entrambe le semionde vengano ricomposte in un segnale sinusoidale completo e il contenuto di armoniche venga notevolmente ridotto.
- Oltre allo stadio push-pull, per amplificatori RF a banda stretta può essere utilizzato un circuito oscillante sintonizzato. Il transistor fornisce impulsi di corrente solo durante una semionda. Il circuito oscillante accumula energia e continua a oscillare tra gli impulsi di corrente, in modo che all’uscita si ottenga nuovamente un segnale quasi sinusoidale per l’intero periodo. In altre parole: il circuito oscillante funge da filtro che sopprime le armoniche. Questa soluzione è tuttavia adatta solo per amplificatori RF a banda stretta, poiché un circuito oscillante è risonante solo in un intervallo di frequenza ristretto.

<margin>
[picture:1089:a_ausgangsstrom_b:Esempio di una corrente di uscita RF $I_\mathrm{C}$ di un transistor in modalità operativa B]
[picture:1091:a_gegentakt:Stadio push-pull con due transistor che amplificano ciascuno una semionda]
</margin>

Riepilogo modalità operativa B:
- Bassa polarizzazione fino all’inizio della conduzione della corrente di collettore
- Corrente di riposo quasi nulla
- Rendimento fino a circa $\qty{80}{\percent}$
- Basso contenuto di armoniche con stadio push-pull o circuito oscillante
- Angolo di conduzione $\Theta = \qty{180}{\degree}$, cioè viene amplificata solo una semionda

[question:AD420]
[question:AD417]

---

% Modalità operativa A/B dell’amplificatore:

Un’altra possibilità per realizzare un amplificatore è la modalità operativa A/B, in cui il punto di funzionamento si trova tra la modalità A e B. La corrente di riposo ($I_\mathrm{A/B}$) è quindi maggiore rispetto alla modalità B, ma notevolmente inferiore rispetto alla modalità A, come mostrato nella figura [ref:a_ausgangsstrom_ab]. Il rendimento è compreso tra $\qty{50}{\percent}$ e $\qty{80}{\percent}$ e il contenuto di armoniche è basso con una tecnica circuitale appropriata.

Riepilogo modalità operativa A/B dell’amplificatore:
- Polarizzazione più alta rispetto alla modalità B, ma inferiore rispetto alla modalità A
- Corrente di riposo maggiore rispetto alla modalità B, ma notevolmente inferiore rispetto alla modalità A
- Rendimento compreso tra $\qty{50}{\percent}$ e $\qty{80}{\percent}$
- Basso contenuto di armoniche
- Angolo di conduzione: $\qty{180}{\degree} < \Theta < \qty{360}{\degree}$

In particolare nella modalità operativa A/B o B di un amplificatore, è necessario evitare la sovraeccitazione, poiché questa può rapidamente causare distorsioni del segnale. Queste distorsioni si manifestano in SSB sotto forma di splatter su frequenze adiacenti.
[question:AD423]

<margin>
[picture:1088:a_ausgangsstrom_ab:Esempio di una corrente di uscita RF $I_\mathrm{C}$ di un transistor in modalità operativa A/B]
</margin>

---

% Modalità operativa C dell’amplificatore:

La cosiddetta *modalità operativa C* è fortemente non lineare, poiché il transistor conduce solo durante una piccola parte dell’oscillazione di ingresso (cfr. figura [ref:a_ausgangsstrom_c]). L’angolo di conduzione è inferiore a $\qty{180}{\degree}$ e, senza segnale di ingresso, idealmente non scorre alcuna corrente di riposo. In questo modo è possibile ottenere rendimenti tipicamente compresi tra $\qtyrange{80}{87}{\percent}$.

Poiché il transistor genera solo brevi impulsi di corrente, il suo segnale di uscita contiene forti componenti di armoniche. Un circuito oscillante sintonizzato o un filtro successivo seleziona la frequenza di uscita desiderata e sopprime le armoniche indesiderate. Poiché queste armoniche possono ancora avere potenze considerevoli all’interno dell’amplificatore di potenza e del filtro, il circuito e i suoi conduttori devono essere realizzati con cura e schermati per evitare che vengano irradiati segnali indesiderati.

La modalità operativa C è particolarmente adatta per segnali con inviluppo costante, ad esempio per FM e CW. Per AM e SSB è invece generalmente inadatta senza misure aggiuntive, poiché l’informazione di ampiezza verrebbe distorta dall’amplificazione non lineare. Pertanto, per i segnali AM e SSB vengono generalmente utilizzate le modalità operative A, B o A/B. Con procedure speciali come la modulazione polare, tuttavia, è possibile generare anche segnali a modulazione di ampiezza con amplificatori non lineari ad alta efficienza. Su questo torneremo in un paragrafo successivo.

Riepilogo: modalità operativa C dell’amplificatore
- Senza polarizzazione
- Corrente di riposo nulla
- Rendimento circa $\qtyrange{80}{87}{\percent}$
- Genera il più alto contenuto di armoniche tra tutte le classi di amplificazione
- Angolo di conduzione $\Theta < \qty{180}{\degree}$, cioè viene amplificata solo una piccola parte dell’onda sinusoidale

<margin>
[picture:1090:a_ausgangsstrom_c:Esempio di una corrente di uscita RF $I_\mathrm{C}$ di un transistor in modalità operativa C]
</margin>

[question:AD418]
[question:AD425]
[question:AD421]
[question:AD422]
[question:AJ218]
[question:AF402]
[question:AF403]

Riassumiamo le classi di amplificazione apprese in una panoramica:

| l: Proprietà | X: Modalità A | X: Modalità B | X: Modalità A/B | X: Modalità C |
| Corrente di riposo | $I_\mathrm{A}$ | 0 | $I_\mathrm{A/B}$ | 0 |
| Rendimento | $\qty{40}{\percent}$ | fino a $\qty{80}{\percent}$ | $\qtyrange{50}{80}{\percent}$ | $\qtyrange{80}{87}{\percent}$ |
| Angolo di conduzione | $\Theta = \qty{360}{\degree}$ | $\Theta = \qty{180}{\degree}$ | $\qty{180}{\degree} < \Theta < \qty{360}{\degree}$ | $\Theta < \qty{180}{\degree}$ |
| Misure contro le armoniche | Filtro | Push-pull o filtro | Push-pull o filtro | Filtro |

La potenza di uscita di un amplificatore può essere calcolata approssimativamente conoscendo il punto di funzionamento e quindi il suo rendimento approssimativo. A tal fine, si calcola inizialmente la potenza in continua dal prodotto di tensione e corrente fornite all’amplificatore. Successivamente, si moltiplica questa potenza per il fattore numerico del rendimento, dove $\qty{100}{\percent}$ corrisponde a un rendimento di $1$. Ad esempio, un rendimento di $\qty{40}{\percent}$ corrisponde a un fattore di $0,4$. Prova ora a risolvere i seguenti esercizi:

[question:AD424]

Oltre alle classiche classi di amplificazione A, B, AB e C, esistono altre classi di amplificazione ad alta efficienza come le classi D, E e F. Nei transistor di classe D ed E vengono utilizzati come interruttori in modo che la potenza dissipata nel transistor stesso sia minima. Gli amplificatori di classe F utilizzano reti sintonizzate aggiuntive per la frequenza fondamentale e armoniche selezionate per modellare favorevolmente gli andamenti di corrente e tensione sul transistor. In questo modo è possibile ottenere rendimenti molto elevati. Tuttavia, tali amplificatori richiedono un’attenta progettazione del circuito e, nel campo RF, sono spesso adatti solo per un intervallo di frequenza limitato. Altre modalità operative come la classe J o la classe S perseguono obiettivi simili, ma non sono rilevanti per l’esame di radioamatore.