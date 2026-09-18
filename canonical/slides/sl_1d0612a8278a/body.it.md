<left>
[picture:648:n_relaisfunkstellen_aufbau:Rappresentazione schematica di una stazione ripetitrice con utenti]
</left>
<right>
* Consente una portata maggiore rispetto a una connessione diretta
* Generalmente situata in posizioni esposte, ad esempio cime montuose, grattacieli, torri (di chiese)
* Oppure su satelliti
</right>

<note>
* La montagna non permette il passaggio del segnale
* Con il relè entrambi i radioamatori possono stabilire una connessione
* Maggiori informazioni sui satelliti in seguito
</note>

---

## Definizione di stazione ripetitrice
una stazione radioamatoriale telecomandata (anche su satelliti), che emette in modo telecomandato le emissioni radioamatoriali ricevute, parti di esse o altri segnali immessi o memorizzati, al fine di aumentare la raggiungibilità delle stazioni radioamatoriali

---
<left>
* Detto anche brevemente: relè o ripetitore
* Trasmette regolarmente il proprio nominativo
* Il nominativo inizia generalmente con DB0, DM0 o DO0
</left>
<fragment>
<right>
* Le stazioni ripetitrici non operano con nominativi personali.
* Le stazioni ripetitrici non sono generalmente presidiate.
* Le stazioni ripetitrici non devono necessariamente essere collocate in posizioni geografiche esposte.
</right>
</fragment>

---
[question:VD118]
---

## Funzionamento
<left>
* Riceve sulla frequenza di ingresso il segnale di una stazione radioamatoriale
* Lo trasmette contemporaneamente sulla frequenza di uscita
* Per evitare interferenze del trasmettitore, le frequenze sono generalmente diverse
</left>
<right>
<fragment>
La distanza tra le frequenze viene chiamata *scostamento di frequenza* o semplicemente *scostamento*

| r: Banda | r: Scostamento |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Scostamento di frequenza]
</fragment>
</right>

---
Esempio di un relè a $\qty{70}{\centi\meter}$:
* Frequenza di ingresso: $\qty{431,275}{\mega\hertz}$
* Scostamento: $\qty{+7,600}{\mega\hertz}$
* Frequenza di uscita: $\qty{438,875}{\mega\hertz}$

---
[question:BE401]
---
[question:BE402]
---
[question:BE403]

---

## Funzionamento crossband
* Trasmette e riceve contemporaneamente su due bande diverse, ad esempio $\qty{2}{\meter}$ e $\qty{70}{\centi\meter}$
* È possibile anche la conversione del modo di emissione, ad esempio SSB in FM

---

## Digipeater
* Inoltra dati invece di voce
* Riceve e trasmette pacchetti di dati
* L’emissione può avvenire solo in parte o con ritardo
* I pacchetti di dati possono essere ripetuti
* È possibile modificare singoli campi dei dati

<note>
* Utilizzato per Packet Radio, popolare negli anni '90 prima di Internet
* Verrà trattato in modo più approfondito in seguito
</note>

---
[question:NF118]
---

## Impostazioni particolari
* Potrebbero essere necessarie ulteriori impostazioni per la connessione al relè
* Queste informazioni sono disponibili nei registri dei ripetitori, sui siti web o presso il responsabile del relè
* Oltre ai ripetitori FM, esistono anche quelli per la voce digitale come DMR o D-Star

<note>
Un esempio di impostazione aggiuntiva è un subtono con CTCSS
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
* I ripetitori preferiscono la FM stretta, poiché altrimenti i segnali vengono distorti e si disturbano le frequenze adiacenti

---
[question:BE407]
---

## Operatività senza interferenze
* In linea di principio, tutti i radioamatori possono utilizzare stazioni radioamatoriali telecomandate con il proprio nominativo assegnato
* Il gestore può escludere radioamatori per garantire un funzionamento senza interferenze
* La BNetzA deve essere informata di ciò

---
[question:VD504]
---

## Attività radio sui ripetitori
* Trasmissioni brevi
* Le stazioni mobili e portatili sono spesso raggiungibili solo per brevi periodi
* Pausa tra le trasmissioni per consentire ad altre stazioni di intervenire

---
[question:BE406]
---
[question:BE404]
---

## Sovrapposizione
* Se due stazioni trasmettono contemporaneamente, l’emissione risulta disturbata fino a diventare illeggibile
* Evitare la "sovrapposizione" con una corretta gestione dei turni
* Iniziare la trasmissione solo quando la stazione precedente ha terminato

---
[question:NE310]
---
[question:BE405]
---

## Potenza di trasmissione
* Secondo l’allegato 1 dell’AFuV
* Per stazioni automatiche al di sopra di $\qty{30}{\mega\hertz}$ con $\qty{50}{\watt}$ ERP

---
[question:VD503]
---

## Rapporto
* L’intensità del segnale ricevuto (S) è quella del relè
* Viene omessa
* Nel rapporto si valuta solo la leggibilità (R)

---
[question:BE408]