<margin>
[picture:542:n_digital_voice_repeaternetwork:Rete di ripetitori per voce digitale: Stazione ripetitrice DB0FZ con connessione Internet, hotspot DN9YI e stazione ripetitrice DB0HOB con collegamento a microonde a DB0FZ]
</margin>

Anche la voce può essere trasmessa digitalmente, ad esempio con le procedure di trasmissione DMR, D-Star, C4FM e M17. A seconda della procedura, questo può essere fatto con un computer o con un apparecchio radio adatto. Ciò consente di comunicare via radio con radioamatori in tutto il mondo tramite stazioni ripetitrici VHF o UHF in rete. Se due o più stazioni ripetitrici sono in rete, le trasmissioni ricevute da una delle stazioni possono essere inoltrate tramite una rete, ad esempio HAMNET o Internet, e ritrasmesse su altre stazioni collegate. Per accedere a tale rete di ripetitori, è anche possibile gestire un cosiddetto hotspot da casa. Finché non esiste un'autorizzazione appropriata per una stazione telecomandata, la gestione di un hotspot è consentita solo come stazione presidiata, vale a dire che il trasmettitore deve essere spento se non è sorvegliato in loco. Sulla banda delle onde corte, i collegamenti vocali digitali vengono stabiliti principalmente direttamente, ad esempio con FreeDV.

<webmargin>
| l: Abbreviazione | X: Procedura di trasmissione |
| D-STAR | Digital Smart Technologies for Amateur Radio |
| C4FM | Continuous 4-level frequency modulation |
| DMR | Digital Mobile Radio |
| M17 | Procedura di trasmissione open-source |
[table:n_dv_uebertragungsverfahren:Procedure di trasmissione utilizzate frequentemente per la radiotelefonia digitale]
</webmargin>

[question:NE404]

---

Nella trasmissione vocale digitale, i segnali vocali vengono convertiti in un flusso di dati prima della trasmissione. Più flussi di dati di questo tipo possono anche essere trasmessi in rapida successione alternata e periodica. Questo si chiama TDMA (Time Division Multiple Access) o procedura di multiplazione temporale. In questo modo, due o più collegamenti vocali utilizzano quasi contemporaneamente la stessa frequenza. Per un apparecchio radio, ciò significa che quando il tasto PTT è premuto, deve continuamente passare rapidamente dalla modalità di trasmissione a quella di ricezione per non perdere il ritmo. 

<margin>
[picture:474:n_digital_voice_tdma:TDMA con tre collegamenti su una frequenza]
</margin>

<tip>
La maggior parte degli amplificatori di potenza esterni non può passare dalla modalità di trasmissione a quella di ricezione così rapidamente come sarebbe necessario per il TDMA. Pertanto, per DMR e altre procedure che utilizzano time slot, è consentito utilizzare solo amplificatori di potenza adatti a tale scopo. Altrimenti, la frequenza verrà occupata non solo durante il proprio time slot. Ciò può disturbare le trasmissioni di altre stazioni sulla stessa frequenza.
</tip>

[question:NE403]

---

A differenza delle trasmissioni analogiche, dove solitamente solo la frequenza e il tipo di modulazione devono essere noti per stabilire un collegamento con un altro partecipante, per la voce digitale spesso è necessario considerare più regolazioni, ad esempio il gruppo di conversazione, la stanza o il riflettore per collegare le stazioni ripetitrici o il time slot TDMA da utilizzare.

<indepth>
A seconda della procedura, possono esserci anche una serie di altre regolazioni, ad esempio nel DMR il Color-Code, con cui più gruppi di utenti possono condividere una frequenza senza ascoltarsi a vicenda. Tali parametri devono essere impostati correttamente sull'apparecchio prima dell'inizio di un collegamento affinché questo possa avvenire.
</indepth>

[question:NE402]

Sui portatili VHF/UHF e tramite stazioni ripetitrici, oltre alla radiotelefonia FM, vengono utilizzate anche le procedure digitali DMR, D-Star o C4FM.

[question:NE307]

% TODO: La tabella non viene trattata e non è completa ... 
%<webmargin>
%| l: Procedura | l: ID personale | l: Chiamata di gruppo | l: Chiamata diretta | X: Altro |
%| M17 | Nominativo | - | Nominativo | Channel Access Number (CAN), Velocità di trasmissione (1600 o 3200 bit/s) |
%| FreeDV | - | - | - | Mode (1600, 700C, 700D, 700E, 2020) |
%| DMR | ID DMR | Talkgroup | ID DMR | Color-Code (da 1 a 4, nel radioamatore solitamente 1), Time Slot (TS 1 o TS 2) |
%| C4FM | Nominativo | Riflettore | - | |
%| D-Star | Nominativo | ? | ? | |
%[table:n_digital_voice_verfahren:Procedure per Digital Voice e possibili regolazioni]
%</webmargin>

<latexonly>
\newpage
</latexonly>