Un **relè** consente di ottenere una portata maggiore rispetto a quella possibile con un collegamento radio diretto tra due stazioni radioamatoriali. I relè vengono generalmente installati in posizioni esposte, ad esempio sulle cime delle montagne, su edifici alti, torri di chiese o altre strutture simili. Esistono anche relè installati su satelliti che orbitano intorno alla **terra**. La struttura e il funzionamento di un relè sono illustrati nell’immagine [ref:n_relaisfunkstellen_aufbau]. 
% Finde Bild nicht gut. Das das oben auf dem Berg ein Relais sein soll, kann man grad noch so erkennen. Das dieses aber etwas empfängt und "weiterleitet" ist nicht ersichtlich. Issue #38 eröffnet

[picture:648:n_relaisfunkstellen_aufbau:Rappresentazione schematica di una stazione radioamatoriale relè con utenti]

Se, ad esempio, tra due stazioni radio è presente una montagna, è impossibile trasmettere attraverso di essa. Un relè installato sulla cima della montagna consente comunque di stabilire un collegamento, poiché entrambe le stazioni possono raggiungere direttamente il relè.

---
<law>
Link diretto alla pagina di segnalazione su [eGov](https://www.egov.swiss/de/amateurfunk/spezielle-frequenznutzung-detail)

[Bollettino radioamatoriale](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) 1.7
</law>


In Svizzera, solo le associazioni radioamatoriali possono gestire stazioni non presidiate, come ad esempio i relè.

Le associazioni radioamatoriali che intendono installare una stazione non presidiata, inclusi i relè, sono soggette all’obbligo di segnalazione all’UFCOM (registrazione). Tale segnalazione deve essere presentata all’UFCOM prima della messa in funzione. 
Per garantire un utilizzo delle frequenze privo di interferenze da parte dell’impianto non presidiato, si consiglia di effettuare preventivamente una coordinazione delle frequenze. A tal fine, è possibile rivolgersi all’USKA [Contatto:](qrg@uska.ch), che offre supporto su base volontaria. Successivamente, è possibile effettuare la segnalazione all’UFCOM tramite il portale eGov.
% Sollte das auf die "einführende Infoseite"?
[question:VN007]



Il **nominativo** di una stazione radioamatoriale relè inizia, in base al [piano dei nominativi](https://50ohm.de/rzp), generalmente con DB0, DM0 o DO0.
La definizione ufficiale di ripetitore recita, in modo più asciutto: *"Stazione radioamatoriale relè": una stazione radioamatoriale telecomandata (anche su satelliti) che riceve emissioni radioamatoriali, parti di esse o altri segnali immessi o memorizzati e li ritrasmette a distanza per aumentare la raggiungibilità delle stazioni radioamatoriali.*
Tuttavia, la seguente domanda relativa a questa definizione può essere risolta anche con il metodo dell’esclusione, conoscendo i seguenti punti:
* Le stazioni radioamatoriali relè non vengono gestite con nominativi personali.
* Le stazioni radioamatoriali relè non sono generalmente presidiate.
* Le stazioni radioamatoriali relè non devono necessariamente essere installate in posizioni geograficamente esposte.
[question:VD118]
% gibt es dazu eine HB Rechtgrundlage? 

---
% Stimt das mit der "Ablage". Gibt es für die Schweiz eine solche Liste. Stimmen Tabelle NE-4.9.2? 
I relè vengono anche chiamati ripetitori o stazioni radioamatoriali relè. Li si può riconoscere dal fatto che trasmettono regolarmente il proprio nominativo.

Un relè riceve su una **frequenza di ricezione** il segnale di una stazione radioamatoriale e lo ritrasmette contemporaneamente sulla propria frequenza di trasmissione. Affinché il trasmettitore del relè non interferisca con il proprio ricevitore, le frequenze di trasmissione e ricezione sono generalmente diverse. La distanza tra la frequenza di trasmissione e quella di ricezione viene chiamata **larghezza di banda** o semplicemente *ablage*. Le larghezze di banda comunemente utilizzate in Germania sono riportate nella tabella [ref:n_relaisfunkstellen_ablage].

<margin>
| r: Banda | X: Larghezza di banda |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Larghezza di banda]
</margin>

Ad esempio, la frequenza di un relè da $\qty{70}{\centi\meter}$ viene indicata come segue:
* Frequenza di ricezione: $\qty{431,275}{\mega\hertz}$
* Larghezza di banda: $\qty{+7,600}{\mega\hertz}$
* Frequenza di trasmissione: $\qty{438,875}{\mega\hertz}$

[question:BE401]
[question:BE402]
[question:BE403]

<indepth>
Alcuni relè operano anche in modalità *crossband*. Ciò significa che una stazione trasmette e riceve su una banda (ad esempio $\qty{70}{\centi\meter}$), mentre un’altra stazione, sullo stesso relè ma su una banda diversa (ad esempio $\qty{2}{\meter}$), riceve e trasmette. Il controllo del relè gestisce la conversazione tra le due bande. È possibile anche una conversione del modo di trasmissione, ad esempio da SSB a **modulazione di frequenza**.
</indepth>

Un relè che trasmette dati invece di voce viene chiamato digipeater. Un digipeater è in grado di ricevere **pacchetti di dati** e ritrasmetterli. Una particolarità è che la trasmissione può avvenire solo in parte o con un certo ritardo. Inoltre, i pacchetti di dati possono essere ripetuti o singoli campi di dati modificati.

[question:NF118]

---

Prima di iniziare un collegamento radio tramite un relè, è necessario conoscerne le caratteristiche tecniche e i parametri. Per alcuni relè, oltre alla frequenza, sono necessarie ulteriori impostazioni sul proprio **trasmettitore-ricevitore** per garantire un funzionamento privo di interferenze. Oltre alla **modulazione di frequenza** analogica, vengono utilizzati anche metodi digitali, come DMR e D-Star, come modalità di trasmissione vocale.

<tip>
Informazioni sui relè, sui parametri tecnici e sulle caratteristiche specifiche possono essere ottenute dall’associazione radioamatoriale locale, dalla persona responsabile del relè o da internet.
</tip>
% Wo erhält man die in der Schweiz? USKA? https://uska.ch/bandplan/ (Achtung Umbau USKA Webseite September 26)
[question:NE309]
[question:NE308]

Un’impostazione importante è la **larghezza di banda** del canale in modalità FM. Ricordiamo: la larghezza di banda indica quanto "spazio" nel spettro di frequenza viene occupato dalla trasmissione. In questo caso, esiste il Wide-FM, che occupa una larghezza di banda di $\qty{25}{\kilo\hertz}$ e viene visualizzato sul display, ad esempio, come *FM-W*. Esiste poi lo Schmalband-FM (Narrow-FM), che occupa solo $\qty{12,5}{\kilo\hertz}$ e viene indicato, ad esempio, come *FM-N* sul **apparecchio radio**. Molti ripetitori non gradiscono segnali troppo ampi, poiché ciò può causare distorsioni del segnale e interferenze con frequenze di relè adiacenti.
% Zusätzliche Erklärung für 25kHz nötig. FRV wollte die Frage unbedingt.
[question:BE407]
[question:BE417]

Il collegamento radio tramite stazioni radioamatoriali telecomandate è generalmente consentito a tutti i radioamatori in possesso di un nominativo assegnato. Tuttavia, per garantire un funzionamento privo di interferenze, il gestore può escludere altri radioamatori dall’utilizzo della stazione.
%Die BNetzA ist hiervon zu unterrichten.
[question:VD504]
% Gibt es eine HB Rechtsgrundlage? Text stehen lassen soweit sinnvoll?

Quando si opera tramite stazioni relè, i passaggi di trasmissione dovrebbero essere il più brevi possibile, in modo da consentire anche a stazioni mobili e portatili di utilizzare il relè più facilmente, soprattutto se si trovano solo temporaneamente nell’area di ricezione. Tra un passaggio e l’altro, è opportuno mantenere una pausa per consentire ad altre stazioni di accedere al relè.

[question:BE406]
[question:BE404]

Se due stazioni diverse trasmettono contemporaneamente, la trasmissione del relè viene disturbata fino a renderla incomprensibile. Per evitare questo fenomeno, chiamato *doppeln*, è fondamentale una corretta transizione tra gli utenti del ripetitore. Ciò significa anche iniziare la trasmissione solo dopo che la stazione precedente ha terminato la propria.

---
<indepth>
Spiegare la corretta transizione
</indepth>
%Todo Margin-Box sinnvoll füllen

[question:NE310]
[question:BE405]


C’è una particolarità nella valutazione di un collegamento radio tramite una stazione radioamatoriale relè. Poiché l’**intensità del segnale** con cui si riceve il partner radio è quella della stazione relè e non quella del partner stesso, non viene indicata. Nel rapporto si valuta solo la leggibilità (R).

---
<indepth>
Spiegare il rapporto su un relè con un esempio.
</indepth>
%Todo Margin-Box sinnvoll füllen

[question:BE408]


Nelle disposizioni dell’allegato 1 dell’AFuV sono riportate anche le specifiche per le potenze di trasmissione delle stazioni relè. Al di sopra di 30 MHz, una stazione che opera automaticamente può essere utilizzata con una potenza massima di 50 W ERP.
[question:VD503]
% Gibt es eine HB Rechtsgrundlage? 