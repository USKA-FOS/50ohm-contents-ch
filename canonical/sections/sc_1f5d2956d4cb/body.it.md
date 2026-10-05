Nella sezione [sec:oszilloskop_1] abbiamo imparato che un oscilloscopio rappresenta l'andamento temporale delle tensioni. Possiamo quindi utilizzare un oscilloscopio per verificare le forme d'onda dei segnali.

[question:AI301]

<margin>
[picture:1005:a_impulsbreite:Determinazione della larghezza dell'impulso di un segnale rettangolare non ideale]
</margin>

---

Oltre alle tensioni alternate sinusoidali, a causa della tecnologia digitale, si presentano anche tensioni rettangolari. Tuttavia, non può esistere un andamento di tensione perfettamente rettangolare. I bordi sono sempre un po' inclinati o deformati. Il tempo tra la salita e la discesa di un rettangolo, chiamato larghezza del impulso o durata dell'impulso, viene quindi sempre misurato a metà altezza, cioè al 50% della tensione. In questo modo si garantisce che per lo stesso segnale tutti ottengano lo stesso risultato di misura.

<indepth>
La causa di queste deformazioni sono le capacità e le induttanze inevitabili nei cavi e nei componenti, che agiscono come filtri e attenuano le componenti ad alta frequenza di un segnale rettangolare.
</indepth>

[question:AI303]
[question:EI303]

% TODO La domanda EI303 non è presente. Si prega di vedere Issue #52.

Gli oscilloscopi possono rappresentare segnali con frequenze e andamenti molto diversi. Affinché questi segnali appaiano stabili sullo schermo, gli oscilloscopi possiedono un cosiddetto sistema di trigger (dall'inglese trigger = "innescare"). In questo caso, l'apparecchio monitora continuamente il segnale di ingresso e avvia l'acquisizione esattamente quando una condizione precedentemente definita è soddisfatta – ad esempio, quando il segnale supera una determinata tensione, la cosiddetta tensione di trigger. Da quel momento inizia il campionamento e la memorizzazione dei valori misurati, che successivamente vengono rappresentati come curva sullo schermo.


Grazie a questa procedura, ogni rappresentazione inizia sempre nello stesso stato del segnale, in modo che segnali periodici come oscillazioni sinusoidali o impulsi rettangolari appaiano apparentemente congelati e chiaramente riconoscibili. Gli oscilloscopi digitali possono inoltre visualizzare anche immagini singole, cioè "congelare" lo schermo. Questo facilita l'analisi di segnali non periodici. Il tasto previsto per questo è solitamente etichettato con SINGLE. Inoltre, è possibile sovrapporre più misurazioni, ad esempio per rendere visibili le fluttuazioni temporali di un segnale (dall'inglese jitter).

[question:AI302]

%<indepth>
%La figura [ref:a_oszilloskop_einzelbild] mostra un'immagine singola dalla registrazione musicale della figura [ref:a_oszilloskop_ueberlagerung]. È stata fotografata da un oscilloscopio più vecchio, che lavora principalmente in modo analogico e possiede inoltre una piccola memoria digitale.
%[photo:222:a_oszilloskop_einzelbild:Immagine singola da una registrazione musicale]
%</indepth>

Non ogni cavo è adatto per segnali ad alta frequenza – questo vale anche per la connessione tra l'oggetto di misura e l'oscilloscopio. Per questo si utilizzano generalmente le cosiddette sonde di prova. Esse stabiliscono la connessione e garantiscono che il segnale venga trasmesso il più possibile senza distorsioni, senza caricare eccessivamente il circuito. A tal fine, riducono la tensione del segnale (ad esempio in un rapporto 10:1), adattano la resistenza e la capacità e spesso contengono una compensazione per le alte frequenze.

Una sonda di prova è costituita da un alloggiamento simile a una penna, paragonabile a una penna a sfera. Alla sua punta possono essere applicati diversi ganci o aghi per contattare il punto di misura. La connessione di massa avviene tramite una pinza a coccodrillo (vedi figura [ref:a_oszilloskop_messung]). La figura [ref:a_oszilloskop_tastkoepfe] mostra tre esempi di tali sonde di prova. I modelli di alta qualità sono di conseguenza costosi, poiché devono offrire ampie bande passanti, distorsione minima del segnale e una meccanica precisa.

<margin>
[photo:224:a_oszilloskop_messung:Misurazione con una sonda di prova. Tra i diodi D1 e D2 si vede la punta di prova e più a sinistra la pinza a coccodrillo per la connessione di massa.]
</margin>

<margin>
[photo:223:a_oszilloskop_tastkoepfe:Sonde di prova con diverse punte di prova. Le pinze a coccodrillo sono state rimosse per questa foto.]
</margin>

Le sonde di prova più semplici collegano direttamente la punta di prova all'ingresso di misura. Si parla di sonde 1:1, perché la tensione presente alla punta arriva inalterata all'oscilloscopio. Le sonde di prova per alte frequenze sono costruite in modo più elaborato. Esse riducono la tensione d'ingresso a un valore più piccolo, spesso un decimo. Se si misura una tensione di 10 volt con una sonda 10:1, sullo schermo viene visualizzato 1 volt.

<indepth>
Su alcuni oscilloscopi è possibile impostare quale rapporto di divisione ha la sonda. Quindi sullo schermo viene visualizzata la tensione effettiva. Le sonde passive 10:1 contengono, tra l'altro, una resistenza da $\qty{9}{\mega\ohm}$ che si trova nel percorso del segnale. Gli oscilloscopi hanno generalmente una resistenza interna di $\qty{1}{\mega\ohm}$. In questo modo si ottiene un partitore di tensione 10:1. Inoltre, nella sonda o nel connettore è presente un piccolo condensatore variabile. Serve per adattare la capacità della sonda e del cavo all'ingresso di misura e viene regolato in modo che un segnale rettangolare appaia il più possibile senza distorsioni sullo schermo. Oltre alle sonde passive qui descritte, esistono diverse altre varianti. Ci sono, ad esempio, sonde con cavo coassiale adattato a $\qty{50}{\ohm}$. Sono particolarmente adatte per frequenze molto elevate, ma hanno solo una resistenza interna relativamente piccola. Le versioni attive risolvono questo problema amplificando il segnale direttamente nella sonda.
</indepth>
