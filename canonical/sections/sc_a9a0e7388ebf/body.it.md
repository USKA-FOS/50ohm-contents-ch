A differenza della trasmissione vocale, molti metodi di trasmissione digitale (Digimodes) richiedono solo una larghezza di banda molto ridotta. Mentre i segnali vocali in SSB occupano tipicamente una larghezza di banda di circa $\qty{2,4}{\kilo\hertz}$, i Digimodes utilizzano frequenze significativamente più strette. Ad esempio, BPSK31 richiede solo circa $\qty{31,25}{\hertz}$ di larghezza di banda, mentre FT8 si accontenta di circa $\qty{50}{\hertz}$. I segnali generati dai Digimodes sulle onde corte vengono solitamente modulati anch'essi in SSB. La larghezza di banda HF del segnale trasmesso corrisponde quindi esattamente alla larghezza di banda NF del Digimode.

[question:EE402]
[question:EE403]

All'interno della consueta larghezza di banda di ricezione SSB di circa $\qty{2,4}{\kilo\hertz}$, è possibile ricevere contemporaneamente più segnali Digimode a banda stretta di questo tipo.

<margin>
[picture:718:e_digimode_ssb_empfang_mehrerer_digimodes:Diagramma waterfall della ricezione di più segnali Digimode all'interno della larghezza di banda SSB di 2,4 kHz. Ogni colonna rappresenta la trasmissione di un segnale diverso]
</margin>

[question:EE404]

Puramente teoricamente, in una larghezza di banda SSB di $\qty{2,4}{\kilo\hertz}$ si potrebbero inserire fino a 48 segnali FT8 ($\frac{\qty{2400}{\hertz}}{\qty{50}{\hertz}}$) o addirittura fino a 76 segnali BPSK31 ($\frac{\qty{2400}{\hertz}}{\qty{31,25}{\hertz}}$). Al computer è quindi possibile selezionare selettivamente un singolo segnale Digimode o, a seconda del software, decodificare contemporaneamente una moltitudine di questi segnali. Proprio questa elevata efficienza spettrale rende i Digimodes a banda stretta particolarmente attraenti per il traffico radioamatoriale.

---

Slow-Scan Television (SSTV) si riferisce alla trasmissione di immagini fisse tramite dati di immagine digitalizzati. Le immagini vengono trasmesse riga per riga, consentendo una velocità di trasmissione relativamente bassa. Esistono diverse procedure SSTV, che differiscono tra loro per risoluzione, profondità di colore e durata della trasmissione. Un vantaggio significativo dell'SSTV è la bassa larghezza di banda richiesta: è tipicamente inferiore a $\qty{3}{\kilo\hertz}$, corrispondendo quindi approssimativamente alla larghezza di banda di un segnale vocale SSB. Ciò consente l'uso dell'SSTV anche nelle bande delle onde corte ed è particolarmente adatto per le trasmissioni di immagini a livello mondiale nel radioamatore. La figura [ref:e_digimode_ssb_sstv] mostra un'immagine SSTV tipica.

Al contrario, l'Amateur Television (ATV) trasmette immagini in movimento, cioè vera televisione. A causa della quantità di informazioni notevolmente maggiore, l'ATV richiede una larghezza di banda significativamente più ampia, tipicamente diversi megahertz, spesso $\qty{6}{\mega\hertz}$ o più. Per questo motivo, l'ATV non è realizzabile nelle bande delle onde corte e viene utilizzato solo in frequenze più elevate, di solito a partire dalla banda dei $\qty{70}{\centi\meter}$ in su o, ad esempio, nella gamma dei $\unit{\giga\hertz}$ tramite QO-100. Lì sono disponibili larghezze di banda sufficientemente ampie per fornire la larghezza di banda necessaria per le trasmissioni di immagini in movimento.

[question:EE415]

<margin>
[photo:84:e_digimode_ssb_sstv:Conferma di un collegamento SSTV da F1BIB a ON1GA con RST 575 e l'immagine originariamente ricevuta]
</margin>
