* Per aggirare i filtri, alcuni apparecchi radio FM offrono una porta separata per i modi digitali
* Questa porta è spesso etichettata come *DATA* o *9600*
* 9600 corrisponde al baud ($\unit{\baud}$), la velocità di trasmissione che può essere gestita
* A questa porta viene collegato direttamente il TNC (Terminal Node Controller) dal computer
* Oggi spesso implementata direttamente come connessione USB

---

[photo:303:e_9600_port:Apparecchio radio con porta DATA]

---
<left>
* Sia la trasmissione che la ricezione avvengono senza filtro BF e stadio finale BF
* Viene pilotato direttamente il modulatore FM o il demodulatore FM
* I segnali non vengono distorti
</left>
<right>
[picture:354:e_9600_port_fm_sender:Trasmettitore FM con linea di alimentazione del segnale dati a $\qty{9600}{\baud}$ al punto 2]
[picture:355:e_9600_port_fm_empfaenger:Ricevitore FM con prelievo del segnale dati a $\qty{9600}{\baud}$ al punto 4]
</right>
---

<left>
* In passato utilizzato per il Packet Radio
* Oggi per modi moderni e open-source come M17
</left>
<right>
[photo:185:m17_tnc:Modulo M17, un TNC per la tecnica di trasmissione M17]
</right>

---
[question:EF309]
---
[question:EF219]