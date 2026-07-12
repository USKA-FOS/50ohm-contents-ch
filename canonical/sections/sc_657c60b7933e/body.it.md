Finora abbiamo considerato campi elettrici e magnetici per il caso in cui i campi non variano nel tempo. In tecnica radio questi campi sono in realtà poco interessanti, poiché ci occupiamo di tensioni e correnti che variano nel tempo. Allo stesso modo, i campi elettrici e magnetici generati variano nel tempo.

<margin>
[picture:885:e_vertikalantenne_em:Campo elettrico e magnetico su un'antenna]
</margin>

Ciò comporta effetti aggiuntivi. Già nel 1831 Michael Faraday scoprì che un campo magnetico che varia nel tempo genera una tensione elettrica in un conduttore adiacente. Questo effetto, chiamato *induzione*, viene utilizzato ad esempio nel trasformatore: una corrente che varia nel tempo (ad esempio sinusoidale) nell'avvolgimento primario genera un campo magnetico che varia nel tempo, il quale a sua volta induce una tensione nell'avvolgimento secondario.

Per capire che, viceversa, la variazione di un campo elettrico porta a un campo magnetico, immaginiamo un condensatore a piastre le cui piastre formano un circuito con una fonte di tensione esterna. Se modifichiamo il campo elettrico all'interno del condensatore, le cariche devono essere spostate nel circuito esterno. Lo spostamento di portatori di carica implica però una corrente elettrica. Questa corrente elettrica, a sua volta, genera un campo magnetico attorno al conduttore.

Mentre le rappresentazioni con conduttori elettrici sono per noi intuitive, è molto importante che questi conduttori non siano necessari. Campi magnetici ed elettrici esistono anche al di fuori dei conduttori, persino nel vuoto. Anche qui, un campo magnetico che varia nel tempo genera un campo elettrico che varia nel tempo. Questo campo che varia nel tempo porta a sua volta a un campo magnetico che varia nel tempo. *Quindi, campi magnetici che variano nel tempo e campi elettrici che variano nel tempo sono sempre accoppiati.* Parliamo quindi anche di *campo elettromagnetico*. In sintesi: un'onda elettromagnetica che può propagarsi liberamente nello spazio si basa sull'interazione tra campi magnetici ed elettrici che variano nel tempo.

[question:EB302]

Come già descritto sopra, tensioni e correnti costanti nel tempo non possono generare un campo elettromagnetico. Per questo è necessaria una corrente che varia nel tempo in un conduttore.

[question:EB301]

<indepth>
Il campo magnetico e il campo elettrico sono in realtà descritti da *vettori*, cioè da grandezze che hanno una direzione nello spazio. Matematicamente si può dimostrare che nel *campo lontano*, cioè sufficientemente lontano dall'antenna, i vettori dei due campi devono essere perpendicolari tra loro. La direzione di propagazione dell'onda elettromagnetica (cioè del nostro segnale radio...) è a sua volta perpendicolare sia al campo elettrico che a quello magnetico.
  
[picture:886:e_emfeld_ausbreitung:Propagazione dell'onda elettromagnetica]
  
Le relazioni descritte sono matematicamente descritte dalle *equazioni di Maxwell*, da James Clerk Maxwell, che le elaborò tra il 1861 e il 1864 basandosi sulle osservazioni di altri fisici. Giunse alla conclusione che i campi magnetici ed elettrici devono essere accoppiati:
  
1. $\vec{\nabla} \cdot \vec{E} =\frac{\rho}{\varepsilon_{0}}$
2. $\vec{\nabla} \cdot \vec{B} = 0$
3. $\vec{\nabla} \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$
4. $\vec{\nabla } \times \vec{B} =\mu_0 (\vec{j} +\varepsilon_0 \frac{\partial\vec{E}}{\partial t})$
  
L'equazione (3) mostra che un campo magnetico che varia nel tempo genera un campo elettrico. Questo campo elettrico che varia nel tempo, secondo l'equazione (4), contribuisce a sua volta alla generazione di un campo magnetico attraverso la corrente di spostamento. Queste relazioni vanno ben oltre ciò che si deve sapere nel radioamatore.
  
L'esistenza del campo elettromagnetico fu tuttavia dimostrata sperimentalmente solo più di vent'anni dopo (1886) da Heinrich Hertz.
</indepth>

Come mostrato nelle figure e [ref:e_emfeld_ausbreitung], nel campo lontano (lontano dall'antenna) la componente del campo magnetico è sempre perpendicolare alla componente del campo elettrico.

[question:EB303]

Le componenti del campo magnetico ed elettrico perpendicolari tra loro nel campo lontano determinano anche la direzione di propagazione $S$, come mostrato nella figura [ref:e_vertikalantenne_em]: questa è a sua volta perpendicolare a entrambe. Si può immaginare che il campo magnetico ed elettrico definiscano un piano sul quale la direzione di propagazione è perpendicolare.

[question:EB304]