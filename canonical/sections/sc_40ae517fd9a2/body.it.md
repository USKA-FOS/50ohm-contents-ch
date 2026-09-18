Nella classe E abbiamo già imparato a conoscere le emissioni indesiderate sotto forma di *armoniche* e *prodotti secondari*. Le armoniche o armoniche superiori di un segnale si generano sempre quando si verificano deviazioni dalla curva sinusoidale ideale e sono sempre multipli interi della frequenza fondamentale, come mostrato nella figura [ref:a_harmonische].

Un esempio è illustrato dalla seguente domanda d'esame: se un *amplificatore* viene *sovramodulato*, i picchi dell'ampiezza del segnale sinusoidale vengono limitati – ciò genera armoniche.

[question:AJ207]

<margin>
[picture:868:a_harmonische: Armoniche (OW), armoniche superiori (Harm.) e prodotti secondari (NA)]
</margin>

---

Nel considerare i multipli della frequenza fondamentale di un segnale, distinguiamo tra i termini *armoniche superiori* e *armoniche* del segnale. Questi due termini differiscono solo per la loro definizione e modalità di conteggio. La 1ª armonica di un segnale è la sua frequenza fondamentale stessa. La 2ª armonica corrisponde alla 1ª armonica superiore di un segnale, la 3ª armonica alla 2ª armonica superiore del segnale e così via. La tabella a lato [ref:a_harmonische] mostra la relazione.

<margin>
| l: Multiplo della frequenza fondamentale | l: Armonica | l: Armonica superiore |
| $f_0$ | 1 | ~ |
| $2 \cdot f_0$ | 2 | 1 |
| $3 \cdot f_0$ | 3 | 2 |
| $4 \cdot f_0$ | 4 | 3 |
[table:a_harmonische:Armoniche e armoniche superiori]
</margin>

---

[question:AJ203]
[question:AJ204]

<tip>
La radiodiffusione FM è la "classica" trasmissione radio su *onda ultracorta* (UKW). La trasmissione dei programmi radio avviene nella banda di frequenza compresa tra $\qtyrange{87,6}{107,9}{\mega\hertz}$.
</tip>

Se si desidera sopprimere singolarmente determinate armoniche o armoniche superiori di un segnale, oltre al classico filtro armoniche (filtro passa-basso), ciò può essere ottenuto anche mediante i cosiddetti *circuiti trappola*. Un circuito trappola sopprime al massimo una frequenza precisa e lascia passare quasi inalterate tutte le altre.

[question:AJ210]

---

Secondo il regolamento per la radiodiffusione amatoriale (AFuV), le emissioni indesiderate devono essere ridotte al minimo possibile. Tuttavia, la [disposizione 33](https://50ohm.de/vfg33) del 2007 stabilisce valori limite precisi che devono essere rispettati sia dai *radioamatori* che dai produttori di apparecchi commerciali.

<margin>
[photo:319:a_vfg33: Estratto dalla disposizione 33 del 2007]
</margin>

Per la banda VHF/UHF/SHF da $\qtyrange{50}{1000}{\mega\hertz}$, le emissioni secondarie e le armoniche devono essere attenuate di almeno $\qty{60}{\dB}$ rispetto al livello di picco massimo del segnale di trasmissione (PEP) del trasmettitore, purché la potenza dei segnali sia superiore a $\qty{0,25}{\micro\watt}$ (cfr. figura [ref:a_uagw]).

[question:AJ225]

<margin>
[picture:918:a_uagw:Attenuazione armoniche banda VHF/UHF/SHF]
</margin>

Per la banda delle onde corte da $\qtyrange{1,7}{35}{\mega\hertz}$, le emissioni secondarie e le armoniche devono essere attenuate di almeno $\qty{40}{\dB}$ rispetto al livello di picco massimo del segnale di trasmissione (PEP) del trasmettitore, purché la potenza dei segnali sia superiore a $\qty{0,25}{\micro\watt}$.

[question:AJ224]

%TODO INSERIRE IMMAGINE DA DL1COM
Con un analizzatore di spettro, in modalità emissioni spurie, è possibile misurare le armoniche o armoniche superiori (in inglese *harmonics*), come mostrato nella figura [ref:a_uagw]. L'analizzatore di spettro rileva automaticamente il livello della portante e la soppressione delle armoniche, visualizzandoli sullo schermo. Se si costruisce un apparecchio da soli, è fondamentale verificare tramite misurazioni che i valori limite prescritti siano rispettati. Un produttore commerciale di apparecchi radio certifica il rispetto di questi valori limite con la dichiarazione CE, tuttavia può accadere che singoli apparecchi non rispettino le prescrizioni – in questi casi, l'Agenzia federale delle reti può vietarne l'uso e la vendita.

Le emissioni indesiderate non derivano solo dalle armoniche, ma possono anche verificarsi nella preparazione della frequenza dei trasmettitori – ad esempio a causa di prodotti di miscelazione indesiderati, fluttuazioni nella *tensione di alimentazione* o *sovraeccitazione* del segnale BF. Ne parleremo più in dettaglio nel seguito.

Per sopprimere i prodotti di miscelazione indesiderati – ma anche le armoniche – dopo i mixer viene spesso utilizzato un *filtro passa-banda*. In particolare per i trasmettitori a singola banda e per gli apparecchi delle bande VHF, UHF e SHF, invece dei classici filtri passa-basso armoniche, vengono impiegati filtri passa-banda. In questi apparecchi radio, spesso devono essere soppressi anche componenti del segnale che si generano già durante la preparazione del segnale di trasmissione e che possono trovarsi anche al di sotto della frequenza di trasmissione vera e propria.

[question:AJ211]
[question:AJ209]
[question:AJ208]

Le emissioni indesiderate possono anche verificarsi in prossimità del segnale di trasmissione. Queste sono difficili o impossibili da sopprimere con l'uso di filtri e dovrebbero quindi essere efficacemente eliminate già nella fase iniziale della preparazione del segnale, adottando le misure appropriate. Spesso tali *prodotti secondari*, chiamati anche *prodotti secondari* (in gergo tecnico anche *splatter*), che allargano involontariamente il segnale di trasmissione, sono causati da un'impostazione troppo elevata dell'amplificatore del microfono di un trasmettitore. Ciò distorce il segnale BF, generando emissioni secondarie indesiderate. La figura [ref:a_harmonische] mostra le emissioni secondarie.

[question:AJ219]

Anche una *tensione di alimentazione* non sufficientemente stabilizzata degli stadi finali dei trasmettitori può causare emissioni indesiderate. Ad esempio, un *alimentatore* mal filtrato o stabilizzato (con tensione di ronzio) sul lato della tensione di alimentazione può portare a emissioni AM dello stadio finale. Anche interferenze di segnali BF sul lato di alimentazione di rete di un trasmettitore possono causare emissioni AM corrispondenti. Questo è spesso percepibile nelle emissioni CW come portante/tono "ronzante", soprattutto nei trasmettitori più vecchi.

[question:AJ222]
[question:AJ223]