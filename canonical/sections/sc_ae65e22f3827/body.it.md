Il campo elettromagnetico di un'antenna può essere suddiviso, come illustrato nella figura [ref:a_nahfernfeld], in *campo vicino* nelle immediate vicinanze dell'antenna e *campo lontano* nelle zone più distanti. Il campo vicino viene ulteriormente suddiviso in *campo vicino reattivo* e *campo vicino radiativo*.


<tip>
Nelle [spiegazioni delle procedure di valutazione secondo la BEMFV](https://50ohm.de/bemfv) l'Agenzia federale delle reti (BNetzA) ha chiarito i concetti e le procedure per la determinazione delle distanze di sicurezza.
[photo:80:n_Bewertungsverfahren:In questo documento sono descritte le procedure di valutazione.]
</tip>

[picture:1113:a_nahfernfeld:Definizioni delle distanze per campo vicino e campo lontano secondo l'Agenzia federale delle reti (BNetzA).]


---


Secondo la definizione utilizzata nella figura dell'Agenzia federale delle reti (BNetzA), il campo vicino reattivo si estende fino a una distanza


$d \le \dfrac{\lambda}{2 \cdot \pi}$

dall'antenna, dove $\lambda$ indica la lunghezza d’onda. A distanze maggiori inizia il campo vicino radiativo. La distanza di questa soglia dipende quindi dalla lunghezza d’onda. Ad esempio, con una lunghezza d’onda di $\qty{20}{\meter}$ si ottiene:


$d = \frac{\qty{20}{\meter}}{2 \cdot \pi} \approx \qty{3,18}{\meter}$


In questo esempio, il campo vicino reattivo si estende quindi fino a circa $\qty{3,18}{\meter}$ dall'antenna.


Nel campo vicino reattivo di un'antenna, l’intensità di campo elettrico e l’intensità di campo magnetico non presentano una relazione di fase costante tra loro. Cosa significhi esattamente questo viene spiegato in modo più approfondito nel riquadro a lato.


[question:AK101]


Se si osservano l’andamento del campo elettrico e magnetico per un’antenna a dipolo in questi campi nella figura [ref:a_dipol_feld_e_h], si nota che le due grandezze di campo non hanno gli stessi valori. Il campo elettrico è notevolmente più intenso di quello magnetico. Con un’antenna a loop magnetica nella figura [ref:a_loop_feld_e_h] avviene esattamente il contrario: il campo magnetico è notevolmente più intenso di quello elettrico.


<margin>
[picture:1114:a_dipol_feld_e_h:Andamento dell’intensità di campo elettrico e magnetico di un’antenna a dipolo nei campi vicino e lontano (scala logaritmica).]
[picture:1115:a_loop_feld_e_h:Andamento dell’intensità di campo elettrico e magnetico di un’antenna a loop nei campi vicino e lontano (scala logaritmica).]
</margin>


<indepth>
Per chi è interessato alla matematica e già familiarizzato con i numeri complessi, qui viene spiegato in modo semplificato perché l’intensità di campo elettrico e magnetico nel campo vicino reattivo non presentano una relazione di fase indipendente dalla posizione.
Nel caso di un dipolo elettricamente corto, i campi possono essere semplificati come segue:


$ \underline{E}(r)~=~\left( \underbrace{\frac{A}{r^3}}_{\text{quasi statico}} + \underbrace{j\,\frac{B}{r^2}}_{\text{induttivo}} + \underbrace{\frac{C}{r}}_{\text{radiazione}} \right) e^{-jkr}$


$ \underline{H}(r)~=~\left( \underbrace{j\,\frac{D}{r^2}}_{\text{induttivo}} + \underbrace{\frac{F}{r}}_{\text{radiazione}} \right) e^{-jkr}. $


Le grandezze sottolineate sono complesse e descrivono, oltre all’intensità, anche la fase dei rispettivi contributi di campo. Fattori come $j$ o $-j$ nelle equazioni complete del campo corrispondono a sfasamenti di $\qty{90}{\degree}$ o $\qty{-90}{\degree}$.


Poiché i singoli contributi diminuiscono con la distanza $r$ a velocità diverse, il loro rapporto reciproco cambia. Di conseguenza, anche la differenza di fase tra intensità di campo elettrico e magnetico nel campo vicino dipende dalla distanza, dalla direzione e dalla forma dell’antenna.

Per una comprensione completa, è necessario considerare le singole componenti vettoriali delle equazioni del campo. Questi concetti vanno ben oltre i contenuti di apprendimento della classe A e non sono rilevanti per l’esame.
</indepth>


In particolare nel campo vicino reattivo, a causa delle componenti di campo elettrico o magnetico forti e che diminuiscono rapidamente con la distanza, possono verificarsi elevate intensità di campo locali. Questa zona viene definita *reattiva* perché una grande parte dell’energia del campo non viene irradiata, ma oscilla avanti e indietro tra antenna e campo. Proprio come in un condensatore (campo elettrico) o in una bobina (campo magnetico), l’energia immagazzinata nel campo vicino reattivo non viene consumata, ma restituita all’antenna con sfasamento: questa oscillazione tra campo e antenna corrisponde alla componente reattiva dell’impedenza dell’antenna, mentre solo la componente attiva (resistenza di radiazione) descrive la potenza effettivamente irradiata.


Nel *campo vicino radiativo*, nella zona

$\frac{\lambda}{2\pi} < d < 4\cdot\lambda$


le componenti di campo irradiate acquistano progressivamente maggiore rilevanza. In questo caso, il rapporto tra intensità di campo elettrico e magnetico si avvicina sempre più a quello del campo lontano. Tuttavia, l’antenna irradia già da questa zona, ma solo le componenti di campo reattive perdono di importanza con l’aumentare della distanza. Per molte considerazioni semplificate, il campo vicino radiativo può già essere trattato in modo simile al campo lontano. Su questo torneremo in seguito in modo più approfondito.


Il *campo lontano* inizia, secondo la definizione qui utilizzata, a una distanza

$d \ge 4\cdot\lambda$

dall’antenna. In questa zona, l’intensità di campo elettrico e magnetico diminuiscono proporzionalmente a $\frac{1}{d}$. Inoltre, le due componenti di campo presentano un rapporto fisso tra loro e una relazione di fase costante.


---


Il rapporto tra i valori assoluti di intensità di campo elettrico e magnetico viene definito come *impedenza d’onda*:


$Z_\mathrm{F}(d)=\left|\frac{E(d)}{H(d)}\right|$


La figura [ref:a_feldwellenwiderstand] mostra come l’impedenza d’onda cambi con l’aumentare della distanza dall’antenna. Nel campo vicino reattivo, essa dipende fortemente dalla forma dell’antenna, dalla direzione considerata e dalla distanza. In questa zona può essere notevolmente maggiore o minore rispetto all’impedenza d’onda dello spazio libero.


Nel campo vicino radiativo, il rapporto tra intensità di campo elettrico e magnetico si avvicina progressivamente al valore dello spazio libero. Nel campo lontano, infine, è costante e ammonta approssimativamente a:


$Z_0 = \sqrt{\dfrac{\mu_0}{\varepsilon_0}} \approx \qty{120\pi}{\ohm} \approx \qty{377}{\ohm}$


L’impedenza d’onda dello spazio libero mette in relazione tra loro le grandezze di campo elettrico e magnetico. Essa rappresenta una misura di quanto l’intensità di campo elettrico sia forte rispetto a quella magnetica.


[question:AK102]


Questo valore è importante ricordarlo, poiché ci servirà per derivare la formula approssimata.


Riassumiamo:

* Il campo lontano di una sorgente di radiazione è la zona in cui i vettori dell’intensità di campo elettrico (E), dell’intensità di campo magnetico (H) e la direzione di propagazione sono perpendicolari tra loro e non presentano differenze di fase. Inoltre, l’impedenza d’onda deve corrispondere a quella dello spazio libero.
* Il confine tra campo lontano e campo vicino dipende principalmente dalla lunghezza d’onda. Tuttavia, anche il tipo di antenna utilizzata e il suo ambiente giocano un ruolo importante. Nelle antenne a filo prevalentemente utilizzate nel radioamatoriale (ad esempio dipoli), il campo lontano si forma a una distanza di circa $4\cdot\lambda$.


<margin>
[picture:1116:a_feldwellenwiderstand:Andamento dell’impedenza d’onda nei campi vicino e lontano (scala logaritmica).]
</margin>