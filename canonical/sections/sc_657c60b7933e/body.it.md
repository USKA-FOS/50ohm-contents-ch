Finora abbiamo considerato i campi elettrici e magnetici nel caso in cui questi campi non variano nel tempo. Tuttavia, nella tecnica radio questi campi sono in realtà poco interessanti, poiché ci occupiamo di tensioni e correnti che variano nel tempo. Allo stesso modo, i campi elettrici e magnetici generati sono variabili nel tempo.

<margin>
[picture:885:e_vertikalantenne_em:Campo elettrico e magnetico su un'antenna]
</margin>

In questo caso si verificano effetti aggiuntivi. Già nel 1831, Michael Faraday scoprì che un campo magnetico variabile nel tempo induce in un conduttore vicino una tensione elettrica. Questo effetto, chiamato *induzione*, viene sfruttato ad esempio nel trasformatore: una corrente variabile nel tempo (ad esempio sinusoidale) nel primario genera un campo magnetico variabile nel tempo, che a sua volta induce una tensione nel secondario.

Per comprendere che, al contrario, la variazione di un campo elettrico genera un campo magnetico, immaginiamo un condensatore a piastre il cui circuito è formato da una sorgente di tensione esterna. Se modifichiamo il campo elettrico all'interno del condensatore, nel circuito esterno devono essere spostate delle cariche. Lo spostamento di portatori di carica implica però una corrente elettrica. Questa corrente elettrica genera a sua volta un campo magnetico intorno al conduttore.

Sebbene le rappresentazioni con conduttori elettrici siano intuitive per noi, è fondamentale capire che questi conduttori non sono necessari. I campi magnetici ed elettrici esistono anche al di fuori dei conduttori, persino nel vuoto. Anche in questo caso vale che un campo magnetico variabile nel tempo genera un campo elettrico variabile nel tempo. Questo campo elettrico variabile nel tempo, a sua volta, porta alla formazione di un campo magnetico variabile nel tempo. *I campi magnetici e quelli elettrici variabili nel tempo sono quindi sempre accoppiati.* Per questo motivo parliamo anche di *campo elettromagnetico*. In sintesi: un'onda elettromagnetica che si propaga liberamente nello spazio si basa sull'interazione tra campi magnetici ed elettrici variabili nel tempo.

[question:EB302]

Come già descritto in precedenza, tensioni e correnti costanti nel tempo non possono generare un campo elettromagnetico. Per questo è necessario un flusso di corrente variabile nel tempo in un conduttore.

[question:EB301]

<indepth>
Il campo magnetico e quello elettrico sono descritti matematicamente da *vettori*, cioè da grandezze che hanno una direzione nello spazio. È possibile dimostrare matematicamente che nel *campo lontano*, cioè a una distanza sufficiente dall'antenna, i vettori dei due campi devono essere perpendicolari tra loro. La direzione di propagazione dell'onda elettromagnetica (cioè del nostro segnale radio ...) è a sua volta perpendicolare sia al campo elettrico che a quello magnetico.

[picture:886:e_emfeld_ausbreitung:Propagazione dell'onda elettromagnetica]

Le relazioni descritte vengono formalizzate matematicamente dalle *equazioni di Maxwell*, formulate da James Clerk Maxwell tra il 1861 e il 1864 sulla base di osservazioni di altri fisici. Egli giunse alla conclusione che i campi magnetici ed elettrici devono essere accoppiati:

1. $\vec{\nabla} \cdot \vec{E} =\frac{\rho}{\varepsilon_{0}}$
2. $\vec{\nabla} \cdot \vec{B} = 0$
3. $\vec{\nabla} \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$
4. $\vec{\nabla } \times \vec{B} =\mu_0 (\vec{j} +\varepsilon_0 \frac{\partial\vec{E}}{\partial t})$

L'equazione (3) mostra che un campo magnetico variabile nel tempo genera un campo elettrico. Questo campo elettrico variabile nel tempo contribuisce, secondo l'equazione (4), tramite la corrente di spostamento, alla generazione di un campo magnetico. Queste relazioni vanno ben oltre ciò che è necessario sapere per il radioamatoriale.

L'esistenza del campo elettromagnetico fu dimostrata sperimentalmente solo vent'anni dopo (1886) da Heinrich Hertz.
</indepth>

<indepth>
Poiché nell'approfondimento precedente sono state presentate le equazioni di Maxwell, qui verranno spiegati i simboli specifici:

L'*operatore nabla* ∇ è uno strumento matematico che descrive come un campo (ad esempio un campo elettrico o magnetico) varia da una posizione all'altra. A seconda di come viene utilizzato, indica dove le linee di campo hanno origine o terminano, oppure se ruotano intorno a un punto.

Il punto ⋅ indica la *divergenza*. Essa descrive se in un punto le linee di campo hanno origine o scompaiono.

La croce × indica la *rotazione*. Essa descrive quanto un campo "ruota".

Va notato che la comprensione e l'applicazione delle equazioni di Maxwell vanno ben oltre le conoscenze richieste per l'esame. Tuttavia, si tratta di un concetto così fondamentale dell'elettrotecnica che almeno il nome dovrebbe essere noto.
</indepth>

Come mostrato nelle figure [ref:e_vertikalantenne_em] e [ref:e_emfeld_ausbreitung], nel campo lontano (lontano dall'antenna) la componente magnetica del campo è sempre perpendicolare a quella elettrica.

[question:EB303]

Le componenti del campo magnetico ed elettrico, perpendicolari tra loro nel campo lontano, determinano anche la direzione di propagazione $S$, come mostrato nella figura [ref:e_emfeld_ausbreitung]: essa è a sua volta perpendicolare a entrambe. Si può immaginare che il campo magnetico e quello elettrico definiscano un piano su cui la direzione di propagazione è perpendicolare.

[question:EB304]