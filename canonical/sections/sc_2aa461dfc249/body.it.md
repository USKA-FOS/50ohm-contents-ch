<margin>
[picture:542:n_digital_voice_repeaternetwork:Rete per Voice digitale: stazione ripetitore DB0FZ con connessione a Internet, Hotspot DN9YI e stazione ripetitore DB0HOB con collegamento radio direzionale a DB0FZ]
</margin>

Anche la voce può essere trasmessa in digitale, ad esempio con le tecniche di trasmissione DMR, D-Star, C4FM e M17. A seconda della tecnica utilizzata, ciò può avvenire tramite un computer o un apparecchio radio idoneo. In questo modo è possibile comunicare tramite stazioni ripetitore VHF o UHF collegate in rete con radioamatori in tutto il mondo. Se due o più stazioni ripetitore sono collegate in rete, le trasmissioni ricevute da una delle stazioni possono essere inoltrate tramite una rete, ad esempio HAMNET o Internet, e ritrasmesse da altre stazioni collegate. Per accedere a una tale rete di ripetitori, è possibile utilizzare anche un cosiddetto Hotspot a casa propria. Fintanto che non si dispone dell’autorizzazione corrispondente per una stazione telecomandata, l’utilizzo di un Hotspot può avvenire solo come stazione presidiata, cioè occorre spegnere il trasmettitore se non è supervisionato in loco. In onde corte, le connessioni vocali digitali vengono stabilite principalmente direttamente, ad esempio con FreeDV.

<webmargin>
| l: Abbreviazione | X: Tecnica di trasmissione |
| D-STAR | Digital Smart Technologies for Amateur Radio |
| C4FM | Continuous 4-level frequency modulation |
| DMR | Digital Mobile Radio |
| M17 | Tecnica di trasmissione open-source |
[table:n_dv_uebertragungsverfahren:Tecniche di trasmissione più utilizzate per la radiotelefonia digitale]
</webmargin>

[question:NE404]

---

Nella trasmissione digitale della voce, i segnali vocali vengono convertiti in un flusso di dati prima della trasmissione. Più flussi di dati di questo tipo possono essere trasmessi anche in rapida alternanza periodica. Questo metodo è denominato TDMA (Time Division Multiple Access) o multiplazione a divisione di tempo. In questo modo, due o più connessioni vocali utilizzano quasi contemporaneamente la stessa frequenza. Per un apparecchio radio, ciò significa che, premendo il tasto PTT, deve passare rapidamente e costantemente tra modalità di trasmissione e ricezione per non perdere il ritmo.

<margin>
[picture:474:n_digital_voice_tdma:TDMA con tre connessioni su una frequenza]
</margin>

<tip>
La maggior parte degli amplificatori di potenza esterni non è in grado di commutare tra modalità di trasmissione e ricezione abbastanza velocemente quanto richiesto dal TDMA. Pertanto, per DMR e altre tecniche che utilizzano slot temporali, devono essere impiegati esclusivamente amplificatori di potenza idonei. Altrimenti, la frequenza risulterebbe occupata non solo durante il proprio slot temporale, causando interferenze con le trasmissioni di altre stazioni sulla stessa frequenza.
</tip>

[question:NE403]

---

A differenza delle trasmissioni analogiche, in cui solitamente sono sufficienti la frequenza e il tipo di modulazione per stabilire una connessione con un altro partecipante, per la voce digitale spesso occorre considerare ulteriori impostazioni, ad esempio il gruppo di conversazione, la posizione o il riflettore per collegare stazioni ripetitore, oppure lo slot temporale TDMA da utilizzare.

<indepth>
A seconda della tecnica utilizzata, possono esserci numerose altre impostazioni, ad esempio per DMR il codice colore, che consente a più gruppi di utenti di condividere una frequenza senza interferire reciprocamente. Tali parametri devono essere impostati correttamente sull’apparecchio prima di iniziare una connessione affinché questa venga stabilita.
</indepth>

[question:NE402]




















































Sugli apparecchi portatili VHF/UHF e tramite stazioni ripetitore, oltre alla radiotelefonia FM, vengono spesso utilizzate anche le tecniche digitali DMR, D-Star o C4FM.


[question:NE307]


% TODO: Auf die Tabelle wird nicht eingegangen und sie ist nicht komplett ... 
%<webmargin>
%| l: Verfahren | l: Eigene Kennung | l: Gruppenruf | l: Direktruf | X: Sonstige |
%| M17 | Rufzeichen | - | Rufzeichen | Channel Access Number (CAN), Übertragungsrate (1600 oder 3200 Bit/s) |
%| FreeDV | - | - | - | Mode (1600, 700C, 700D, 700E, 2020) |
%| DMR | DMR-ID | Talkgroup | DMR-ID | Color-Code (1 bis 4, im Amateurfunk meist 1), Zeitschlitz (TS 1 oder TS 2) |
%| C4FM | Rufzeichen | Reflektor | - | |
%| D-Star | Rufzeichen | ? | ? | |
%[table:n_digital_voice_verfahren:Verfahren für Digital Voice und mögliche Einstellungen]
%</webmargin>

<latexonly>
\newpage
</latexonly>