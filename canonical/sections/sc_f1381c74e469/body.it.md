% Fonte: % https://www.bfs.de/DE/themen/emf/hff/wirkung/hff-nachgewiesen/hff-nachgewiesen.html

Nelle comunicazioni radioamatoriali con microonde si utilizzano spesso antenne paraboliche o elicoidali. Entrambe le tipologie di antenna consentono di ottenere un guadagno d'antenna molto elevato. Da pochi watt, addirittura da pochi milliwatt, si possono ottenere potenze irradiate notevoli. Con antenne paraboliche è relativamente semplice raggiungere un guadagno di $\qty{20}{\dB}$. Da una potenza di trasmissione di $\qty{1}{\watt}$ si ottiene così una potenza irradiata di $\qty{100}{\watt}$. Se lo specchio ha un guadagno di $\qty{30}{\dB}$, la potenza irradiata sale addirittura a $\qty{1000}{\watt}$. Di conseguenza, i campi elettromagnetici nella zona di radiazione principale sono molto intensi.

I campi elettromagnetici ad alta frequenza agiscono sul corpo umano principalmente in modo termico, cioè riscaldando i tessuti. Le aree del corpo con una minore capacità di dissipare calore, come gli occhi, il cervello o i testicoli, sono particolarmente sensibili. Per questo motivo, misure di protezione adeguate sono necessarie per tutte le persone.

La permanenza nel percorso diretto del fascio di un'antenna trasmittente è pericolosa. In particolare con le microonde, deve essere assolutamente evitata!

<indepth>
Nella raccolta di formule è possibile trovare la formula per calcolare il guadagno d'antenna delle antenne paraboliche:

$g_\text{i} = 10 \cdot \log_{10} \left[\left(\frac{\pi\cdot d}{\lambda}\right) ^2 \cdot\eta~\right] \unit{\dB}$

La lunghezza d’onda entra nel calcolo al denominatore, cioè: minore è la lunghezza d’onda, maggiore è il guadagno.

Nel Hamnet vengono utilizzate le bande di frequenza $\qtyrange{5650}{5850}{\mega\hertz}$ ($\lambda = \qty{5,2}{\centi\meter}$ al centro della banda). Con uno specchio di diametro pari a $\qty{0,80}{\meter}$ si ottiene già un guadagno di circa $\qty{33}{\dB}$ (con $\eta=1$). Per ottenere un guadagno simile nella banda dei $\qty{70}{\centi\meter}$, sarebbe necessario un diametro di $\qty{10}{\meter}$. Antenne paraboliche così grandi non possono essere installate ovunque. Per questo motivo si pone particolare attenzione all'uso delle microonde, dove il pericolo può essere sottovalutato a causa delle antenne relativamente piccole.
</indepth>

---

[question:EK201]
% se comparabile a "bfs" dalla Svizzera, sostituire.
<attention>
L’[Ufficio federale tedesco per la protezione dalle radiazioni](https://50ohm.de/bfs) informa sulla sua pagina web sugli effetti biologici dei campi elettromagnetici ad alta frequenza sul corpo umano.

* I campi elettromagnetici ad alta frequenza vengono assorbiti dal corpo.
* L’intensità dell’assorbimento di energia dipende dall’intensità e dalla frequenza dei campi elettromagnetici.
* Effetti chiaramente dimostrati sono le interazioni meccaniche e gli effetti termici dei campi ad alta frequenza.
* L’effetto termico è determinante per possibili effetti sulla salute umana.
</attention>
