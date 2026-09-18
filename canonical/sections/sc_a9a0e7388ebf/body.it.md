A differenza della trasmissione vocale, molti metodi di trasmissione digitale (digimode) richiedono una larghezza di banda molto ridotta. Mentre i segnali vocali in SSB occupano tipicamente una larghezza di banda di circa $\qty{2,4}{\kilo\hertz}$, i digimode utilizzano bande di frequenza molto più strette. Ad esempio, BPSK31 necessita solo di circa $\qty{31,25}{\hertz}$, mentre FT8 si attesta intorno ai $\qty{50}{\hertz}$. I segnali generati dai digimode vengono modulati in SSB anche sulle onde corte. La larghezza di banda HF del segnale trasmesso corrisponde quindi esattamente alla larghezza di banda BF del digimode.

[question:EE402]
[question:EE403]

All’interno della consueta larghezza di banda di ricezione SSB di circa $\qty{2,4}{\kilo\hertz}$, possono essere ricevuti contemporaneamente diversi di questi segnali a banda stretta.

<margin>
[picture:718:e_digimode_ssb_empfang_mehrerer_digimodes:Diagramma a cascata della ricezione di più segnali digimode all’interno della larghezza di banda SSB di 2,4 kHz. Ogni colonna rappresenta la trasmissione di un segnale diverso]
</margin>

[question:EE404]

Dal punto di vista matematico, in una larghezza di banda SSB di $\qty{2,4}{\kilo\hertz}$ possono essere trasmessi fino a 48 segnali FT8 ($\frac{\qty{2400}{\hertz}}{\qty{50}{\hertz}}$) o addirittura fino a 76 segnali BPSK31 ($\frac{\qty{2400}{\hertz}}{\qty{31,25}{\hertz}}$). Sul computer è possibile selezionare selettivamente un singolo segnale digimode o, a seconda del software, decodificare contemporaneamente anche una moltitudine di questi segnali. Proprio questa elevata efficienza spettrale rende i digimode a banda stretta particolarmente interessanti per l’attività radioamatoriale.

---

La Slow-Scan Television (SSTV) indica la trasmissione di immagini fisse tramite dati digitalizzati. Le immagini vengono trasmesse riga per riga, il che consente una velocità di trasmissione relativamente bassa. Esistono diversi metodi SSTV che differiscono, tra l’altro, per risoluzione, profondità di colore e durata della trasmissione. Un vantaggio fondamentale della SSTV è la ridotta larghezza di banda necessaria: tipicamente inferiore a $\qty{3}{\kilo\hertz}$, corrispondente circa alla larghezza di banda di un segnale vocale SSB. Grazie a ciò, la SSTV può essere utilizzata anche nelle bande delle onde corte ed è particolarmente adatta per trasmissioni di immagini a livello mondiale nel radioamatore. La figura [ref:e_digimode_ssb_sstv] mostra un’immagine SSTV tipica.

Al contrario, l’Amateur Television (ATV) trasmette immagini in movimento, cioè una vera e propria televisione. A causa della quantità di informazioni nettamente superiore, l’ATV richiede una larghezza di banda molto maggiore, tipicamente diversi megahertz, spesso $\qty{6}{\mega\hertz}$ o più. Per questo motivo, l’ATV non è realizzabile nelle bande delle onde corte e viene impiegato solo a partire da bande di frequenza più elevate, solitamente dal $\qty{70}{\centi\meter}$ in su o, ad esempio, nella banda dei $\unit{\giga\hertz}$ tramite QO-100. Qui sono disponibili bande di frequenza sufficientemente ampie per fornire la larghezza di banda necessaria per le trasmissioni di immagini in movimento.

[question:EE415]

<margin>
[photo:84:e_digimode_ssb_sstv:Conferma di una connessione SSTV a F1BIB da parte di ON1GA con RST 575 e, in aggiunta, l’immagine originariamente ricevuta]
</margin>