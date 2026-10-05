Un relè consente una portata maggiore di quanto spesso sia possibile con una connessione diretta tra due stazioni radioamatoriali. I relè sono solitamente installati in posizioni esposte, ad esempio su cime di montagne, grattacieli, campanili e altre torri. Esistono anche relè su satelliti che orbitano attorno alla Terra.

La struttura e la funzione di un relè terrestre sono rappresentate schematicamente nell'immagine [ref:n_relaisfunkstellen_aufbau]. La trasmissione e la ricezione avvengono su frequenze diverse. L'esempio numerico proviene dal relè sull'Üetliberg.

<margin>
[picture:648:n_relaisfunkstellen_aufbau:Rappresentazione schematica di una stazione relè con utenti]
</margin>

Se, ad esempio, c'è una montagna tra due stazioni radio, è impossibile trasmettere attraverso la montagna. Un relè sulla cima della montagna consente comunque di stabilire una connessione, poiché entrambe le stazioni possono raggiungere direttamente il relè.

L'immagine [ref:nea_linkstrecken_antenne_Pilatus] mostra il montaggio di un'antenna di uplink sul campus di Windisch per il relè Pilatus del [gruppo UHF](https://hb9uf.ch) della USKA.

</tip>

---

<margin>
[photo:1000:nea_linkstrecken_antenne_Pilatus:Lavori di manutenzione sul campus di Windisch, HB9DWW e HB9ZGF durante il montaggio dell'antenna di uplink "Echolink" per il relè Pilatus]
</margin>

---

<law>
Collegamento diretto alla pagina di segnalazione in [eGov](https://www.egov.swiss/de/amateurfunk/spezielle-frequenznutzung-detail)

[Nota informativa sul radioamatoriale](https://www.bakom.admin.ch/de/amateurfunk#Merkblatt-Amateurfunk) 1.7
</law>


In Svizzera, solo le associazioni radioamatoriali possono gestire stazioni non presidiate, inclusi i relè.

Le associazioni radioamatoriali che desiderano installare una stazione non presidiata sono soggette all'obbligo di notifica all'UFCOM (registrazione). Questa deve essere ottenuta dall'UFCOM prima della messa in servizio.
Per garantire un utilizzo della frequenza senza interferenze dell'impianto non presidiato, si consiglia di effettuare preventivamente una coordinazione delle frequenze. A tal fine, è possibile contattare la USKA [Contatto:](qrg@uska.ch), che fornisce supporto su base volontaria.
%TODO: Correggere il link USKA

Successivamente, è possibile effettuare la notifica all'UFCOM tramite il portale eGov.
% Dovrebbe essere sulla "pagina introduttiva informativa"?
[question:VN007]



Il nominativo di un relè inizia solitamente con DB0, DM0 o DO0, secondo il [piano dei nominativi](https://50ohm.de/rzp).

%TODO: Elvetizzare il piano dei nominativi

La definizione ufficiale dei ripetitori è un po' più arida: *"Stazione relè": una stazione radioamatoriale telecomandata (anche su satelliti) che trasmette telecomandata emissioni radioamatoriali ricevute, parti di esse o altri segnali immessi o memorizzati, servendo ad aumentare la raggiungibilità delle stazioni radioamatoriali.*
La seguente domanda su questa definizione può essere risolta bene anche per esclusione, sapendo che:
* I relè non sono gestiti con nominativi personali.
* I relè di solito non sono costantemente presidiati.
* I relè non devono necessariamente essere gestiti in posizioni geograficamente esposte.
[question:VD118]
% Esiste una base giuridica HB per questo?

---
% È corretto per "scarto". Esiste un tale elenco per la Svizzera? La tabella NE-4.9.2 è corretta?
I relè sono anche chiamati ripetitori o stazioni relè. Possono essere riconosciuti dal fatto che trasmettono regolarmente il loro nominativo.

Un relè riceve sulla sua frequenza di ingresso il segnale di una stazione radioamatoriale e lo ritrasmette simultaneamente sulla sua frequenza di uscita. Affinché il trasmettitore del relè non interferisca con il proprio ricevitore, le frequenze di trasmissione e ricezione sono generalmente diverse. La differenza tra la frequenza di trasmissione e quella di ricezione è chiamata scarto di frequenza o semplicemente scarto. Gli scarti comunemente utilizzati in Germania si trovano nella tabella [ref:n_relaisfunkstellen_ablage].

<margin>
| r: Banda | X: Scarto |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Scarto di frequenza]
</margin>

Ad esempio, la frequenza di un relè da $\qty{70}{\centi\meter}$ è indicata come segue:
* Frequenza di ingresso: $\qty{431,275}{\mega\hertz}$
* Scarto: $\qty{+7,600}{\mega\hertz}$
* Frequenza di uscita: $\qty{438,875}{\mega\hertz}$

[question:BE401]
[question:BE402]
[question:BE403]

<indepth>
Alcuni relè operano anche nel cosiddetto *funzionamento crossband*. Ciò significa: una stazione trasmette e riceve su una banda (ad es. $\qty{70}{\centi\meter}$), un'altra stazione sullo stesso relè, ma su una banda diversa (ad es. $\qty{2}{\meter}$). Il controllo del relè media le conversazioni sulle due bande. Può anche avvenire una conversione del modo di trasmissione, ad esempio da SSB a FM.
</indepth>

Un relè che trasmette dati anziché voce è chiamato digipeater. Un digipeater è in grado di ricevere e ritrasmettere pacchetti di dati. La particolarità qui è che la trasmissione può avvenire solo in parte o in modo ritardato. Inoltre, i pacchetti di dati possono essere ripetuti o singoli campi di dati possono essere modificati.

[question:NF118]

---

Prima di poter iniziare l'attività radio tramite un relè, è necessario conoscerne le caratteristiche tecniche e i parametri. Per alcuni relè, oltre alla frequenza, sono necessarie ulteriori impostazioni sul proprio trasmettitore-ricevitore per garantire un funzionamento senza interferenze. Oltre alla FM analogica (modulazione di frequenza), vengono utilizzati anche metodi digitali, come DMR e D-Star, come metodi di trasmissione vocale.

<tip>
Le informazioni sui relè, inclusi i parametri tecnici e le particolarità, possono essere ottenute dalla sezione locale DARC più vicina, dalla persona responsabile del relè o da Internet.
</tip>
% Dove si ottengono in Svizzera? USKA? https://uska.ch/bandplan/ (Attenzione: ristrutturazione sito web USKA settembre 26)
[question:NE309]
[question:NE308]

Un'impostazione importante è la larghezza di banda del canale in funzionamento FM. Ricordiamo: la larghezza di banda indica quanto "spazio" si occupa nello spettro di frequenze con l'emissione. Qui c'è da un lato il Wide-FM, dove la larghezza di banda è di $\qty{25}{\kilo\hertz}$ e viene visualizzata sul display ad esempio come *FM-W*. Dall'altro lato c'è il Narrow-FM (FM a banda stretta), che occupa una larghezza di banda di soli $\qty{12,5}{\kilo\hertz}$ ed è ad esempio rappresentato sull'apparecchio radio come *FM-N*. Molti ripetitori non gradiscono affatto che i segnali siano troppo larghi. Infatti, ciò può causare segnali distorti e interferire con le frequenze dei relè adiacenti.
% Spiegazione aggiuntiva necessaria per 25kHz. FRV voleva assolutamente la domanda.
[question:BE407]
[question:BE417]

L'attività radio tramite stazioni radioamatoriali telecomandate deve essere consentita in linea di principio a tutti i radioamatori con nominativo assegnato. Tuttavia, per garantire un funzionamento senza interferenze, il gestore può escludere altri radioamatori dall'utilizzo della stazione radioamatoriale.
%La BNetzA deve essere informata di ciò.
[question:VD504]
% Esiste una base giuridica HB? Mantenere il testo finché è sensato?

Durante l'attività radio tramite stazioni relè, i passaggi dovrebbero essere il più brevi possibile, in modo che le stazioni mobili e portatili possano utilizzare più facilmente il relè, specialmente se si trovano nell'area di ricezione solo per breve tempo. Tra un passaggio e l'altro, si dovrebbe fare una pausa per dare ad altre stazioni la possibilità di segnalarsi.

[question:BE406]
[question:BE404]

Con un ingresso vocale simultaneo di due stazioni diverse, l'emissione del relè viene disturbata fino all'illegibilità. Per evitare questo cosiddetto *raddoppio*, dovrebbe sempre avvenire un corretto passaggio tra gli utenti del ripetitore. Ciò significa anche iniziare a trasmettere solo quando la stazione precedente ha terminato la sua emissione.

---
<indepth>
Spiegare il corretto passaggio.
</indepth>
%Todo Riempire in modo sensato la Margin-Box

[question:NE310]
[question:BE405]


C'è una particolarità nella valutazione di un collegamento radio tramite una stazione relè. Poiché l'intensità del segnale con cui si riceve il corrispondente radio è l'intensità del segnale della stazione relè e non quella del corrispondente radio, si rinuncia a indicarla. Nel rapporto, viene valutata solo la leggibilità (R).

---
<indepth>
Spiegare il rapporto sui relè con un esempio.
</indepth>
%Todo Riempire in modo sensato la Margin-Box

[question:BE408]


Nell'allegato 1 dell'AFuV, già discusso, si trovano anche specifiche per le potenze di trasmissione delle stazioni relè. Al di sopra di 30 MHz, una stazione che funziona automaticamente può operare con un massimo di 50 W ERP.
[question:VD503]
% Esiste una base giuridica HB?

% Il titolo di Stazione relè è stato cambiato in Relè.
% Altre occorrenze di Stazione relè sono state cambiate in Relè.
% TODO inserito per l'elvetizzazione del piano dei nominativi.
