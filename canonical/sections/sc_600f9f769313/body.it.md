Nelle sezioni [sec:strommessung], [sec:spannungsmessung] e [sec:strom_spannung_messung_2] abbiamo già imparato come misurare correttamente la corrente e la tensione e quali proprietà hanno le resistenze interne degli strumenti di misura. Se gli strumenti di misura non vengono collegati correttamente nel circuito, si ottengono letture errate o prive di senso o, nel peggiore dei casi, si può danneggiare lo strumento di misura. Qui, nel corso per HB9, ci sono altre due domande che verificano la corretta misurazione della corrente e della tensione – sebbene in un contesto leggermente più complesso.

La prima domanda riguarda la misurazione della potenza di un amplificatore (Power Amplifier, PA). Conosciamo già la relazione $P = U \cdot I$: la potenza può essere determinata misurando la tensione e la corrente e poi moltiplicando i due valori. Nella figura [ref:a_strom_spannung_messung] a sinistra è collegata l'alimentazione elettrica sotto forma di alimentatore, al centro si trova la PA e a destra è collegato un altro carico, il trasmettitore (TRX). Se ora vogliamo determinare la potenza della PA, possiamo misurare solo la corrente che scorre nella PA.

<margin>
[picture:1003:a_strom_spannung_messung:Misurazione della potenza di un amplificatore (PA)]
</margin>

[question:AI101]

Per la prossima domanda, ricordiamo le regole del corso HB3, cioè che i voltmetri sono sempre collegati in parallelo e gli amperometri sempre in serie. Questo rende la domanda molto facile da risolvere.

[question:AI102]

---

Di seguito, esaminiamo due caratteristiche nella misurazione che vengono spesso confuse:

- Risoluzione
- Precisione di misura (anche chiamata tolleranza o errore)

La *risoluzione* indica la più piccola variazione della grandezza misurata che un apparecchio può ancora visualizzare. Esempio: un multimetro con una risoluzione di $\qty{0,1}{\volt}$ non può distinguere tra $\qty{10,5}{\volt}$ e $\qty{10,45}{\volt}$ se la differenza è inferiore alla risoluzione. Un apparecchio con una risoluzione di $\qty{0,01}{\volt}$ può invece distinguere in modo molto più fine. La risoluzione è generalmente indicata dal produttore dello strumento di misura.

<tip>
Consideriamo prima la *risoluzione* usando un orologio come esempio. Se l'orologio ha un display di ore e minuti, il tempo può essere indicato con una precisione al minuto. Ma se sono le 13:03:10 o le 13:03:59 non si può leggere. *Un minuto* è quindi la *risoluzione minima* dell'orologio (di conseguenza, un orologio con una lancetta dei secondi ha una risoluzione minima di un secondo).
</tip>

La *precisione di misura* (anche errore di misura o tolleranza) di un apparecchio descrive quanto il valore visualizzato può al massimo discostarsi dal valore reale – sia in eccesso che in difetto, ad esempio $\pm\qty{5}{\percent}$. Una semplice regola empirica è: maggiore è l'intervallo di misura che un apparecchio deve coprire, minore è generalmente la precisione della misurazione.

La precisione di misura dipende, tra l'altro, dalla resistenza interna dello strumento di misura, poiché questa influenza il risultato della misura.
Nella classe E abbiamo imparato: un amperometro ha una resistenza interna molto bassa (idealmente $\qty{0}{\ohm}$), un voltmetro invece ha una resistenza interna molto alta (idealmente $\qty{\infty}{\ohm}$). Nella classe A vogliamo ora esaminare anche quanto accuratamente i nostri strumenti di misura possano rilevare la tensione effettivamente presente o l'intensità di corrente. Il valore misurato visualizzato differisce infatti generalmente dal valore reale – e ciò è dovuto alle resistenze interne non perfette degli strumenti di misura, che influenzano la misurazione.

---

Osserviamo lo schema equivalente di un voltmetro reale nella figura [ref:a_reale_spannungsmessung] per la seguente domanda d'esame. Oltre all'amperometro ideale, un voltmetro reale contiene una resistenza collegata in parallelo, ad esempio di $\qty{10}{\mega\ohm}$. Se questa resistenza fosse infinita, praticamente non esisterebbe – e avremmo uno strumento di misura ideale. Ciò significa tuttavia che in una misurazione reale della tensione scorre sempre una piccola corrente attraverso questa resistenza, che influenza il nostro risultato di misura. Immaginiamo, ad esempio, di voler misurare la tensione su un partitore di tensione: a causa della resistenza interna dello strumento di misura, il partitore di tensione viene leggermente caricato, quindi non misuriamo esattamente la tensione che mostrerebbe uno strumento di misura ideale.

<margin>
[picture:1004:a_reale_spannungsmessung:Schema equivalente di un voltmetro reale]
</margin>

---

Similmente al voltmetro, si comporta anche l'amperometro. Un amperometro reale consiste nell'amperometro effettivo e in una piccola resistenza collegata in serie, su cui cade sempre una piccola tensione. Se questa resistenza fosse zero, praticamente non esisterebbe – e avremmo di nuovo lo strumento di misura ideale.

<margin>
[picture:1007:a_reale_strommessung:Schema equivalente di un amperometro reale]
</margin>

---

[question:AI104]

<tip>
In questa domanda, il suggerimento "Risoluzione minima $\qty{100}{\micro\volt}$" non è importante. Può essere risolta utilizzando solo la legge di Ohm.
</tip>

---

Come si comportano invece le grandezze caratteristiche che vengono calcolate dai valori misurati – come la potenza nel nostro esempio iniziale ($P = U \cdot I$) dopo una misurazione di corrente e tensione? Le singole grandezze misurate come corrente e tensione si discostano ciascuna dal valore reale a causa degli errori di misura, e queste deviazioni si propagano di conseguenza nel calcolo.

Esaminiamo un esempio concreto: supponiamo di voler determinare la potenza e per questo misuriamo una tensione continua e una corrente continua. Entrambi gli strumenti di misura mostrano valori che sono rispettivamente del cinque percento troppo bassi. Non si deve commettere l'errore di sommare semplicemente le deviazioni delle singole misurazioni. La formula della potenza mostra chiaramente che in questo caso gli errori si moltiplicano. Esaminiamolo in dettaglio:

$U_\text{Misurata}=0,95 \cdot U_\text{Vera}$ e $I_\text{Misurata}=0,95 \cdot I_\text{Vera}$

Calcoliamo la potenza con la nostra formula nota:

$P_\text{Misurata}=U_\text{Misurata} \cdot I_{Misurata}$

Ora sostituiamo i valori veri:

$P_\text{Misurata} = 0,95 \cdot U_\text{Vera} \cdot 0,95 \cdot I_\text{Vera} = 0,9025 \cdot U_\text{Vera} \cdot I_\text{Vera}$

Ciò significa che la potenza misurata è circa $\qty{9,75}{\percent}$ inferiore alla potenza effettiva, poiché $1-0,9025 \equiv \qty{9,75}{\percent}$. Con questa conoscenza, la seguente domanda d'esame è risolvibile; i valori specifici di corrente e tensione non sono rilevanti per la soluzione.

[question:AI103]
