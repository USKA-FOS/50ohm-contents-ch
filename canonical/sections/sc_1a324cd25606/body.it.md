% Semiconduttori II
% DF2DR 2024-08-19

Il materiale di base del nostro mondo moderno sono i materiali semiconduttori. Ragion per cui vale la pena approfondire un po' questo argomento. I semiconduttori hanno una struttura cristallina reticolare, il che significa che i loro atomi sono disposti periodicamente. 

<margin>
[picture:854:a_silizium_halbleiter:Cristallo semiconduttore di silicio]
</margin>

Tutti i materiali semiconduttori hanno due proprietà in comune:

---

Esiste una *banda proibita di energia*, che è una conseguenza della struttura periodica. Ciò significa che gli elettroni nel cristallo non possono assumere determinate energie. La massima energia che gli elettroni legati agli atomi possono avere, la chiamiamo *energia della banda di valenza*. Poiché gli elettroni sono tutti legati agli atomi del reticolo, non possono contribuire al flusso di corrente. Esistono altri stati energetici che gli elettroni possono raggiungere - si trovano nella *banda di conduzione*, che si trova al di sopra del bordo della banda di valenza per l'importo della banda proibita. Gli elettroni nella banda di conduzione possono contribuire al flusso di corrente se applichiamo una *Tensione* alla sonda semiconduttrice. Per fare ciò, necessitano di un'energia maggiore della banda proibita di energia. Possono assorbire questa energia sotto forma di energia termica, motivo per cui i semiconduttori ad alta purezza sono ottimi isolanti a basse temperature.

[question:AB104]

<margin>
L'energia della banda proibita è determinata dalla composizione chimica del semiconduttore. Rispetto al Si, il Ge ha un'energia della banda proibita significativamente inferiore, GaAs e InP leggermente superiore e GaN molto superiore.
</margin>

Il silicio (Si) e il germanio (Ge) sono *semiconduttori elementari* (come, tra l'altro, anche il diamante, che è carbonio cristallino). Ma esistono anche composti chimici che sono semiconduttori (*semiconduttori composti*), come l'arseniuro di gallio (GaAs), il fosfuro di indio (InP) o anche il nitruro di gallio (GaN). 

---

I materiali con una banda proibita di energia sono definiti semiconduttori solo se sono anche *dopabili*. La loro *conduttività* può essere modificata entro ampi limiti mediante l'aggiunta mirata di impurità al materiale semiconduttore ad alta purezza. L'arsenico (As), ad esempio, ha un elettrone in più nel guscio elettronico esterno rispetto ai semiconduttori elementari. Questo elettrone può diventare molto facilmente e con poca energia un elettrone libero nella banda di conduzione. Chiamiamo questo tipo di drogaggio *drogaggio n*.

<margin>
[picture:855:a_n_dotierung:Drogaggio n]
</margin>

---

Ma cosa succede se contaminamo il semiconduttore con un *Materiale* che ha un elettrone in meno nel guscio elettronico esterno? Chiamiamo una tale lacuna elettronica una *lacuna*. Poiché l'atomo era precedentemente neutro, la lacuna elettronica ha una carica positiva. Le lacune possono anche muoversi nel cristallo e contribuire al flusso di *Corrente*. Chiamiamo questo tipo di drogaggio *drogaggio p*.

<margin>
[picture:856:a_p_dotierung:Drogaggio p]
</margin>

In sintesi, possiamo affermare:
* Il drogaggio n crea un eccesso di elettroni nel semiconduttore.
* Il drogaggio p crea un eccesso di lacune nel semiconduttore.

[question:AB105]
[question:AB106]
[question:AB107]

---

Se si combinano zone p-dopate e n-dopate in un cristallo, ma spazialmente separate, avviene uno scambio di portatori di carica nel piano di contatto: gli elettroni si muovono dalla zona n drogata verso la zona p drogata, le lacune si muovono dalla zona p drogata verso la zona n drogata. Chiamiamo questo movimento di portatori di carica, causato dalle differenze di densità di elettroni e lacune, corrente di diffusione.
D'altra parte, questa separazione di carica crea un *Campo elettrico* con un effetto opposto, che porta a una corrente di campo. In equilibrio (senza *Tensione* applicata esternamente), gli effetti della diffusione e del *Campo elettrico* si bilanciano perfettamente. Tra le zone p e n si forma una regione senza portatori di carica liberi, chiamata *zona di svuotamento* o *strato di blocco*. Una tale struttura rappresenta una *Diode* pn.

[question:AB108]

<margin>
[picture:857:a_pn_uebergang:Giunzione PN]
</margin>

---

Ora applichiamo una *Tensione* esterna, in cui la zona p (*anodo*) è più positiva della zona n (*catodo*). L'elettrodo positivo attira elettroni attraverso la zona di svuotamento e l'elettrodo negativo attira lacune. La zona di svuotamento viene rimossa, si verifica un flusso di *Corrente*. Questo rappresenta il funzionamento in *direzione di conduzione*.

<margin>
[picture:956:a_pn_uebergang_mit_spannung:Giunzione PN con tensione esterna]
</margin>

[question:AC402]

---

Se invertiamo la *Tensione*, la zona di svuotamento si espande, il flusso di *Corrente* si interrompe. Questo è il *funzionamento in blocco* della *Diode*.

<margin>
[picture:957:a_pn_uebergang_mit_spannung:Giunzione PN con tensione esterna]
</margin>


[question:AB109]