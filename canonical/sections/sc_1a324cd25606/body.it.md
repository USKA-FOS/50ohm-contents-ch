% Semiconduttori II
% DF2DR 2024-08-19

Il materiale fondamentale del nostro mondo moderno è costituito dai materiali semiconduttori. Motivo sufficiente per approfondire l'argomento. I semiconduttori hanno una struttura cristallina, cioè i loro atomi sono disposti periodicamente.

<margin>
[picture:854:a_silizium_halbleiter:Cristallo semiconduttore di silicio]
</margin>

Tutti i materiali semiconduttori condividono due proprietà:

---

Esiste una *banda proibita* (o *bandgap*), che è una conseguenza della struttura periodica. Ciò significa che gli elettroni nel cristallo non possono assumere determinate energie. L'energia massima che gli elettroni legati agli atomi possono avere viene chiamata *energia della banda di valenza*. Poiché gli elettroni sono tutti legati agli atomi del reticolo, non possono contribuire al flusso di corrente. Esistono altri stati energetici che gli elettroni possono raggiungere: si trovano nella *banda di conduzione*, che si trova a una distanza pari al valore della banda proibita sopra il bordo della banda di valenza. Gli elettroni nella banda di conduzione possono contribuire al flusso di corrente se applichiamo una tensione al campione semiconduttore. Per farlo, hanno bisogno di un'energia maggiore dell'energia della banda proibita. Possono ottenerla sotto forma di energia termica, motivo per cui i semiconduttori altamente puri sono ottimi isolanti a basse temperature.

[question:AB104]

<margin>
L'energia della banda proibita è determinata dalla composizione chimica del semiconduttore. Rispetto al Si, il Ge ha una banda proibita notevolmente più piccola, il GaAs e l'InP una leggermente più grande e il GaN una molto più grande.
</margin>

Il silicio (Si) e il germanio (Ge) sono *semiconduttori elementari* (come anche il diamante, che è carbonio cristallino). Esistono però anche composti chimici che sono semiconduttori (*semiconduttori composti*), come l'arseniuro di gallio (GaAs), il fosfuro di indio (InP) o anche il nitruro di gallio (GaN).

---

I materiali con banda proibita vengono definiti semiconduttori solo se sono inoltre *drogabili*. La loro conduttività può essere modificata in ampi limiti tramite l'aggiunta mirata di impurità al materiale semiconduttore altamente puro. Ad esempio, l'arsenico (As), rispetto ai semiconduttori elementari, ha un elettrone in più nello strato elettronico esterno. Questo elettrone può diventare molto facilmente un elettrone libero nella banda di conduzione con poca energia. Un drogaggio di questo tipo viene chiamato *drogaggio di tipo N*.

<margin>
[picture:855:a_n_dotierung:Drogaggio di tipo N]
</margin>

---

Cosa succede invece se drogiamo il semiconduttore con un materiale che ha un elettrone in meno nello strato elettronico esterno? Una tale mancanza di elettroni viene chiamata *lacuna*. Poiché l'atomo era neutro prima, la lacuna ha una carica positiva. Le lacune possono muoversi anch'esse nel cristallo e contribuire al flusso di corrente. Un drogaggio di questo tipo viene chiamato *drogaggio di tipo P*.

<margin>
[picture:856:a_p_dotierung:Drogaggio di tipo P]
</margin>

In sintesi, possiamo affermare:
* Il drogaggio di tipo N genera un eccesso di elettroni nel semiconduttore.
* Il drogaggio di tipo P genera un eccesso di lacune nel semiconduttore.

[question:AB105]
[question:AB106]
[question:AB107]

---

Se combiniamo in un cristallo, ma separate spazialmente, zone drogate di tipo P e di tipo N, nella zona di contatto avviene uno scambio di portatori di carica: gli elettroni si muovono dalla zona drogata di tipo N verso quella drogata di tipo P, mentre le lacune si muovono dalla zona drogata di tipo P verso quella drogata di tipo N. Questo movimento di portatori di carica, causato dalle differenze di densità di elettroni e lacune, viene chiamato *corrente di diffusione*.

Questa separazione di carica genera d'altra parte un *campo elettrico* con effetto opposto, che porta a una *corrente di campo*. All'equilibrio (senza tensione applicata dall'esterno), gli effetti della diffusione e del campo elettrico si bilanciano perfettamente. Tra le zone P e N si forma una regione priva di portatori di carica liberi, chiamata *zona di svuotamento* o *strato di sbarramento*. Una struttura di questo tipo rappresenta un *diodo PN*.

[question:AB108]

<margin>
[picture:857:a_pn_uebergang:Giunzione PN]
</margin>

---

Ora applichiamo dall'esterno una tensione che sia più positiva nella zona P (*anodo*) rispetto alla zona N (*catodo*). L'elettrodo positivo attrae gli elettroni attraverso la zona di svuotamento e quello negativo attrae le lacune. La zona di svuotamento si riduce e si verifica un flusso di corrente. Questo rappresenta il funzionamento in *verso diretto*.

<margin>
[picture:956:a_pn_uebergang_mit_spannung:Giunzione PN con tensione esterna]
</margin>

[question:AC402]

---

Se invertiamo la tensione, la zona di svuotamento si espande e il flusso di corrente si arresta. Questo è il *funzionamento in inverso* del diodo.

<margin>
[picture:957:a_pn_uebergang_mit_spannung:Giunzione PN con tensione esterna]
</margin>

[question:AB109]