Nelle sezioni [sec:unerwuenschte_aussendungen_1] e [sec:unerwuenschte_aussendungen_2] abbiamo già conosciuto le emissioni indesiderate sotto forma di *armoniche* e *emissioni secondarie*. Le armoniche superiori o armoniche di un segnale si formano sempre quando si verificano deviazioni dalla curva sinusoidale ideale e sono sempre multipli interi della frequenza fondamentale, come mostrato nella figura [ref:a_harmonische].

Un esempio è mostrato dalla seguente domanda d'esame: Se un amplificatore è sovraeccitato, i picchi dell'ampiezza del segnale sinusoidale vengono limitati – ciò genera armoniche.

[question:AJ207]

<margin>
[picture:868:a_harmonische: Armoniche superiori (OW), armoniche (Harm.) ed emissioni secondarie (NA)]
</margin>

---

Quando si considerano i multipli della frequenza fondamentale di un segnale, distinguiamo tra i termini *armoniche e armoniche superiori* del segnale. Questi due termini differiscono solo nella loro definizione e nel modo di contarli. La 1a armonica di un segnale è la sua frequenza fondamentale stessa. La 2a armonica corrisponde alla 1a armonica superiore di un segnale, la 3a armonica alla 2a armonica superiore di un segnale e così via. La tabella adiacente [ref:a_harmonische] mostra la relazione.

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
La radio FM è la radio "classica" in onda ultracorta (UKW). La trasmissione di programmi radiofonici avviene nella banda di frequenza di $\qtyrange{87,6}{107,9}{\mega\hertz}$.
In Svizzera, contrariamente ai piani precedenti, i trasmettitori FM dovrebbero continuare a funzionare in misura limitata.
</tip>
%TODO: Helvetizzazione 

Se si desidera sopprimere singolarmente determinate armoniche superiori o armoniche di un segnale, ciò può avvenire, oltre al classico filtro per armoniche superiori (filtro passa-basso), anche tramite i cosiddetti *circuiti trappola*. Un circuito trappola sopprime esattamente una frequenza al massimo e lascia passare quasi indisturbate tutte le altre.

[question:AJ210]

---

Secondo l'Ordinanza sulle radiocomunicazioni amatoriali (AFuV), le emissioni indesiderate devono essere limitate al minimo possibile. La [Disposizione 33](https://50ohm.de/vfg33) del 2007 stabilisce però valori limite precisi, che devono essere rispettati sia dal radioamatore che dai produttori di apparecchi commerciali.
%TODO: Helvetizzazione 

<margin>
[photo:319:a_vfg33:Estratto dalla Disposizione 33 del 2007]
</margin>

Per la gamma VHF/UHF/SHF di $\qtyrange{50}{1000}{\mega\hertz}$ vale che le emissioni secondarie e le armoniche superiori devono essere attenuate almeno di $\qty{60}{\dB}$ rispetto al livello di picco massimo del segnale di trasmissione del trasmettitore (PEP), fintanto che la potenza dei segnali si trova al di sopra di un livello di $\qty{0,25}{\micro\watt}$ (cfr. figura [ref:a_uagw]).

[question:AJ225]

<margin>
[picture:918:a_uagw:Atenuazione delle armoniche superiori gamma VHF/UHF/SHF]
</margin>

Per la gamma delle onde corte di $\qtyrange{1,7}{35}{\mega\hertz}$ vale che le emissioni secondarie e le armoniche superiori devono essere attenuate almeno di $\qty{40}{\dB}$ rispetto al livello di picco massimo del segnale di trasmissione del trasmettitore (PEP), fintanto che la potenza dei segnali si trova al di sopra di un livello di $\qty{0,25}{\micro\watt}$.

[question:AJ224]

%TODO INSERIRE IMMAGINE DI DL1COM
Con un analizzatore di spettro è possibile eseguire una misurazione delle armoniche superiori o armoniche (inglese: harmonics) in modalità emissioni spurie, come mostrato nella figura [ref:a_uagw]. L'analizzatore di spettro rileva automaticamente il livello della portante e la soppressione delle armoniche e li mostra anche sullo schermo. Se si costruisce un apparecchio da soli, è cruciale assicurarsi tramite misurazioni che i valori limite prescritti siano rispettati. Un produttore commerciale di apparecchi radio conferma il rispetto di questi valori limite con la dichiarazione CE, tuttavia può accadere che singoli apparecchi non soddisfino i requisiti – in tali casi l'Agenzia federale delle reti può vietarne il funzionamento e la vendita.

Le emissioni indesiderate non si formano solo a causa delle armoniche superiori, ma possono anche verificarsi nella preparazione della frequenza dei trasmettitori – ad esempio attraverso prodotti di miscelazione indesiderati, fluttuazioni nella tensione di alimentazione o attraverso una sovramodulazione del segnale BF. Questo lo vogliamo esaminare più in dettaglio di seguito.

Per sopprimere prodotti di miscelazione indesiderati – ma anche le armoniche superiori – dopo i miscelatori viene spesso utilizzato un filtro passa-banda. Specialmente nei trasmettitori a banda singola e negli apparecchi per la gamma VHF, UHF e SHF, invece dei classici filtri passa-basso per armoniche superiori, vengono utilizzati filtri passa-banda. In questi apparecchi radio spesso devono essere soppressi anche componenti del segnale che si formano già durante la preparazione del segnale di trasmissione e possono persino trovarsi al di sotto della frequenza di trasmissione effettiva.

[question:AJ211]
[question:AJ209]
[question:AJ208]

Le emissioni indesiderate possono anche essere presenti in prossimità immediata del segnale di trasmissione. Queste sono difficili o impossibili da sopprimere con l'uso di filtri e dovrebbero quindi essere efficacemente soppresse già all'inizio della preparazione del segnale attraverso misure appropriate. Tali *emissioni secondarie*, o anche chiamate *prodotti secondari* (colloquialmente anche indicati come "splatter"), che allargano involontariamente il segnale di trasmissione, spesso si formano a causa di un'impostazione troppo alta dell'amplificatore del microfono di un trasmettitore. Ciò distorce il segnale BF, il che ha come conseguenza emissioni secondarie indesiderate. La figura [ref:a_harmonische] mostra le emissioni secondarie.

[question:AJ219]

Anche attraverso una tensione di alimentazione non sufficientemente stabilizzata degli stadi finali del trasmettitore possono formarsi emissioni indesiderate. In questo caso, ad esempio, un alimentatore scarsamente filtrato o stabilizzato (affetto da tensione di ronzio) sul lato della tensione di alimentazione può portare a emissioni AM dello stadio finale. Anche le interferenze di segnali BF sul lato dell'alimentazione di rete di un trasmettitore possono portare a corrispondenti emissioni AM. Questo è spesso percepibile nelle emissioni CW come portante/tono "ronzante", specialmente nei trasmettitori più vecchi.

[question:AJ222]
[question:AJ223]
