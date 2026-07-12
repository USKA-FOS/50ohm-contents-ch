<left>
[picture:648:n_relaisfunkstellen_aufbau:Rappresentazione schematica di una stazione radio ripetitrice con utenti]
</left>
<right>
* Consente una maggiore portata rispetto alla connessione diretta
* Solitamente in posizioni esposte, ad es. cime delle montagne, grattacieli, (chiese-)campanili
* O nei satelliti
</right>

<note>
* Non è possibile comunicare attraverso la montagna
* Con il ripetitore, entrambi i radioamatori possono stabilire un collegamento
* Maggiori informazioni sui satelliti più tardi
</note>
---
## Definizione di stazione radio ripetitrice
una stazione radioamatoriale controllata a distanza (anche nei satelliti), che ritrasmette segnali radioamatoriali ricevuti, parti di essi o altri segnali immessi o memorizzati, attivata a distanza e che serve ad aumentare la raggiungibilità delle stazioni radioamatoriali
---
<left>
* Chiamata anche brevemente: Relais o Repeater
* Trasmettono regolarmente il loro nominativo
* Il nominativo inizia solitamente con DB0, DM0 o DO0
</left>
<fragment>
<right>
* Le stazioni radio ripetitrici non sono gestite con nominativi personali.
* Le stazioni radio ripetitrici di solito non sono presidiate permanentemente.
* Le stazioni radio ripetitrici non devono necessariamente essere gestite in posizioni geograficamente esposte.
</right>
</fragment>

---
[question:NF118]
---
## Funzionamento
<left>
* Riceve il segnale di una stazione radioamatoriale sulla frequenza di ingresso
* Lo ritrasmette contemporaneamente sulla frequenza di uscita
* Affinché il trasmettitore non disturbi, le frequenze sono solitamente diverse
</left>
<right>
<fragment>
La differenza è chiamata *scarto di frequenza* o brevemente *scarto*

| r: Banda | r: Scarto |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Scarto di frequenza]
</fragment>
</right>

---
Esempio di un ripetitore per $\qty{70}{\centi\meter}$:
* Frequenza di ingresso: $\qty{431,275}{\mega\hertz}$
* Scarto: $\qty{+7,600}{\mega\hertz}$
* Frequenza di uscita: $\qty{438,875}{\mega\hertz}$

---
[question:BE401]
---
[question:BE402]
---
[question:BE403]

--- indepth
## Funzionamento Crossband
* Trasmette e riceve contemporaneamente su due bande diverse, ad es. $\qty{2}{\meter}$ e $\qty{70}{\centi\meter}$
* Possibile anche la conversione del modo di trasmissione, ad es. SSB su FM

---
## Digipeater
* Instrada dati invece di voce
* Riceve e trasmette pacchetti di dati
* La trasmissione può avvenire solo in parte o con ritardo
* I pacchetti di dati possono essere ripetuti
* Singoli campi di dati possono essere modificati

<note>
* Per il Packet Radio, che era popolare negli anni '90 prima di Internet
* Più avanti verrà trattato più in dettaglio
</note>
---
## Impostazioni speciali
* Potrebbero essere necessarie ulteriori impostazioni per il collegamento al ripetitore
* Queste informazioni sono disponibili negli elenchi dei ripetitori, sui siti web o presso il responsabile del ripetitore
* Oltre ai ripetitori FM, ce ne sono per la voce digitale come DMR o D-Star

<note>
Un esempio di ulteriori impostazioni è un subtono con CTCSS
</note>

---
[question:NE309]
---
[question:NE308]
---
## Larghezza di banda del canale
* Lo spazio necessario nello spettro di frequenza
* FM larga: $\qty{25}{\kilo\hertz}$
* FM stretta: $\qty{12,5}{\kilo\hertz}$
* I ripetitori preferiscono la FM stretta, altrimenti i segnali vengono distorti e le frequenze adiacenti vengono disturbate

---
[question:BE407]
---
## Funzionamento senza disturbi
* In linea di principio, tutti i radioamatori con il loro nominativo assegnato possono utilizzare le stazioni radioamatoriali controllate a distanza
* Il gestore può escludere i radioamatori per garantire un funzionamento senza disturbi
* La BNetzA deve essere informata di ciò

---
[question:VD504]
---
## Funzionamento sui ripetitori
* Brevi trasmissioni
* Le stazioni mobili e portatili sono spesso solo per breve tempo nel raggio di ricezione
* Pausa tra le trasmissioni per consentire ad altre stazioni di inserirsi

---
[question:BE406]
---
[question:BE404]
---
## Duplicazione
* In caso di immissione vocale simultanea, la trasmissione viene disturbata fino a diventare illeggibile
* Evitare la "duplicazione" con un passaggio di consegne corretto
* Iniziare la trasmissione solo dopo che la stazione precedente ha terminato

---
[question:NE310]
---
[question:BE405]
---
## Potenza di trasmissione
* Secondo l'Allegato 1 dell'AFuV
* Per stazioni automatiche sopra i $\qty{30}{\mega\hertz}$ con $\qty{50}{\watt}$ ERP

---
[question:VD503]
---
## Rapporto
* La potenza del segnale ricevuto (S) è quella del ripetitore
* Si rinuncia a questo
* Solo la leggibilità (R) viene valutata nel rapporto

---
[question:BE408]