Nella classe E abbiamo già conosciuto le emissioni indesiderate sotto forma di *armoniche superiori* e *emissioni spurie*. Le armoniche superiori o armoniche di un segnale si formano sempre quando si verificano deviazioni dalla curva sinusoidale ideale e sono sempre multipli interi della frequenza fondamentale, come mostrato nella figura [ref:a_harmonische].

Un esempio è la seguente domanda d'esame: se un amplificatore è sovraeccitato, le punte dell'ampiezza del segnale sinusoidale vengono limitate, il che genera armoniche superiori.

[question:AJ207]

<margin>
[picture:868:a_harmonische: Armoniche superiori (OW), Armoniche (Harm.) ed Emissioni spurie (NA)]
</margin>

---

Quando si considerano i multipli della frequenza fondamentale di un segnale, si distingue tra i termini *armoniche e armoniche superiori* del segnale. Questi due termini differiscono solo per la loro definizione e numerazione. La 1ª armonica di un segnale è la sua frequenza fondamentale stessa. La 2ª armonica corrisponde alla 1ª armonica superiore di un segnale, la 3ª armonica alla 2ª armonica superiore di un segnale e così via. La tabella a lato [ref:a_harmonische] mostra la relazione.

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
La radio FM è la radio "classica" in modulazione di frequenza (FM). La trasmissione dei programmi radio avviene nella banda di frequenza da $\qtyrange{87,6}{107,9}{\mega\hertz}$.
</tip>

Se si desidera sopprimere singole armoniche superiori o armoniche di un segnale, ciò può essere fatto, oltre al classico filtro per armoniche superiori (passa-basso), anche tramite i cosiddetti *circuiti trappola*. Un circuito trappola sopprime al massimo una singola frequenza e lascia passare quasi tutte le altre senza impedimenti.

[question:AJ210]

---

Secondo il regolamento radioamatoriale (AFuV), le emissioni indesiderate devono essere ridotte al minimo indispensabile. La [disposizione 33](https://50ohm.de/vfg33) del 2007 stabilisce tuttavia limiti precisi che devono essere rispettati dai radioamatori e dai produttori di apparecchiature commerciali.

<margin>
[photo:319:a_vfg33:Estratto dalla disposizione 33 del 2007]
</margin>

Per la gamma VHF/UHF/SHF da $\qtyrange{50}{1000}{\mega\hertz}$, le emissioni spurie e le armoniche superiori devono essere attenuate di almeno $\qty{60}{\dB}$ rispetto al livello di picco del segnale di trasmissione massimo dell'emittente (PEP), purché la potenza dei segnali sia superiore a un livello di $\qty{0,25}{\micro\watt}$ (cfr. figura [ref:a_uagw]).

[question:AJ225]

<margin>
[picture:918:a_uagw:Attenuazione delle armoniche superiori nella gamma VHF/UHF/SHF]
</margin>

Per la gamma delle onde corte da $\qtyrange{1,7}{35}{\mega\hertz}$, le emissioni spurie e le armoniche superiori devono essere attenuate di almeno $\qty{40}{\dB}$ rispetto al livello di picco del segnale di trasmissione massimo dell'emittente (PEP), purché la potenza dei segnali sia superiore a un livello di $\qty{0,25}{\micro\watt}$.

[question:AJ224]

%TODO BILD VON DL1COM EINBAUEN
Con un analizzatore di spettro, è possibile effettuare una misurazione delle armoniche superiori o armoniche (in inglese: harmonics) nella modalità emissioni spurie, come mostrato nella figura [ref:a_uagw]. L'analizzatore di spettro rileva automaticamente il livello della portante e la soppressione delle armoniche, visualizzandole anche sullo schermo. Se si costruisce un apparecchio da soli, è fondamentale assicurarsi tramite misurazioni che vengano rispettati i limiti prescritti. Un produttore di apparecchi radio commerciali conferma con la dichiarazione CE il rispetto di questi limiti, tuttavia può accadere che singoli apparecchi non soddisfino le specifiche; in questi casi, l'autorità di regolamentazione federale può vietarne l'uso e la vendita.

Le emissioni indesiderate non derivano solo da armoniche superiori, ma possono anche verificarsi nella generazione di frequenza degli emittenti, ad esempio a causa di prodotti di miscelazione indesiderati, fluttuazioni della tensione di alimentazione o sovraeccitazione del segnale audio. Questo lo esamineremo più in dettaglio di seguito.

Per la soppressione di prodotti di miscelazione indesiderati, ma anche delle armoniche superiori, viene spesso utilizzato un filtro passa-banda dopo i mixer. Soprattutto negli emittenti monobanda e negli apparecchi per le gamme VHF, UHF e SHF, vengono utilizzati filtri passa-banda invece dei classici filtri passa-basso per armoniche superiori. In questi apparecchi radio, spesso è necessario sopprimere anche componenti del segnale che si generano già durante la preparazione del segnale di trasmissione e che possono addirittura trovarsi al di sotto della frequenza di trasmissione effettiva.

[question:AJ211]
[question:AJ209]
[question:AJ208]

Le emissioni indesiderate possono anche trovarsi nelle immediate vicinanze del segnale di trasmissione. Queste sono difficili o impossibili da sopprimere con l'uso di filtri e dovrebbero quindi essere efficacemente soppresse fin dall'inizio della preparazione del segnale tramite misure appropriate. Spesso tali *emissioni spurie*, o anche chiamate *prodotti secondari* (nel linguaggio colloquiale anche "splatter"), che allargano involontariamente il segnale di trasmissione, si verificano a causa di un'impostazione troppo alta del guadagno del microfono di un emittente. Ciò distorce il segnale audio, con conseguenti emissioni spurie. La figura [ref:a_harmonische] mostra le emissioni spurie.

[question:AJ219]

Anche una tensione di alimentazione non sufficientemente stabilizzata degli stadi finali di un emittente può causare emissioni indesiderate. Ad esempio, un alimentatore mal filtrato o stabilizzato (con ripple) sul lato della tensione di alimentazione può portare a emissioni AM dello stadio finale. Anche interferenze di segnali audio sul lato dell'alimentazione di rete di un emittente possono causare corrispondenti emissioni AM. Questo è spesso percepibile nelle trasmissioni CW come una portante/tono "ronzante", soprattutto nei vecchi emittenti.

[question:AJ222]
[question:AJ223]