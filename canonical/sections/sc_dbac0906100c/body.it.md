Come abbiamo già imparato, un dipolo a semionda può essere alimentato anche da un'estremità. La resistenza di alimentazione, con una lunghezza del filo di λ/2 o suoi multipli, è elevata (circa 2000–2500 Ω).

Per l'adattamento di un'antenna alimentata da un'estremità esistono diverse possibilità. Di seguito esaminiamo tre varianti tipiche:

* Circuito di Fuchs
* Trasformatore per l'adattamento dell'impedenza
* Antenna Zeppelin

Un metodo di adattamento è il già discusso circuito di Fuchs (cfr. figura [ref:a_fuchskreis]). Si tratta di un circuito risonante parallelo sintonizzato sulla frequenza operativa. Esso trasforma la bassa impedenza della linea di alimentazione sull'elevata impedenza di alimentazione del dipolo a semionda alimentato da un'estremità e, al contempo, bilancia eventuali componenti reattivi presenti.

<margin>
[picture:310:a_fuchskreis:Circuito di Fuchs per l'adattamento di un dipolo a semionda alimentato da un'estremità]
</margin>

[question:AG419]

---

Un'altra possibilità è un trasformatore (cfr. figura [ref:a_unun_1_49]) con un rapporto di trasformazione di ü = 1:7. Poiché sia la tensione che la corrente vengono moltiplicate o divise per un fattore 7, per la resistenza si ottiene una trasformazione di 1:7² = 1:49, corrispondente a (1 · 50 Ω) : (49 · 50 Ω) = 50 Ω : 2450 Ω.

<margin>
[photo:332:a_unun_1_49:Trasformatore 1 a 49 (Un-Un) per l'adattamento di un dipolo a semionda alimentato da un'estremità]
[picture:315:a_endspeisung_1:Dipolo a semionda alimentato da un'estremità con cavo "pigtail"]
[picture:260:a_endspeisung_2:Dipolo a semionda alimentato da un'estremità con cavo coassiale come controantennna]
</margin>

<attention>
Per quanto riguarda la *trasformazione dell'impedenza*, il rapporto di spire di un trasformatore entra in gioco al quadrato, cioè un trasformatore con un rapporto di spire di 1:7 garantisce una trasformazione dell'impedenza di 1:49. Nei Balun e negli Un-Un spesso non è specificato se si tratti del rapporto di spire o del rapporto di impedenza. Esiste quindi la possibilità di confusione. È consuetudine indicare il rapporto di impedenza. Ad esempio, con un trasformatore con un rapporto di spire (ü) di 1:7 si parla di un Un-Un 1:49.
</attention>

Come controantennna si utilizza spesso un corto spezzone di filo (almeno un ventesimo della lunghezza d'onda), cfr. figura [ref:a_endspeisung_1], o una parte del cavo coassiale di alimentazione (almeno 0,05 λ), cfr. figura [ref:a_endspeisung_2]. Un'induttanza di modo comune (abbreviata MWS) impedisce che il resto del cavo di alimentazione diventi parte dell'antenna.

[question:AG123]
[question:AG124]

---

In alternativa a un circuito di Fuchs o a un trasformatore, si può utilizzare una linea bifilare di lunghezza λ/4. In questo caso si parla di *antenna Zeppelin* (cfr. figura [ref:a_zeppelinantenn]). Come una linea trasformi un'impedenza verrà approfondito in una sezione successiva.

Il nome deriva dall'impiego di queste antenne su dirigibili. Grazie alla linea bifilare di lunghezza λ/4, l'alta tensione si manifesta solo alla sua estremità, quindi a una distanza considerevole dal dirigibile riempito di gas (cfr. figura [ref:a_zeppelinantenne_foto]).

<margin>
[picture:314:a_zeppelinantenne:Struttura di un'antenna Zeppelin]
[photo:336:a_zeppelinantenne_foto:Antenna Zeppelin (immagine simbolica)]
</margin>

[question:AG120]

---

Allo stesso modo di un dipolo a semionda alimentato da un'estremità, anche con altre forme di antenna si può utilizzare una linea di alimentazione con impedenza caratteristica diversa per l'adattamento. Per la classe E abbiamo già conosciuto le antenne a loop a onda intera, tra cui la Delta-Loop e l'antenna Quad. Un'antenna Delta-Loop (cfr. figura [ref:a_delta_loop]) con bracci di uguale lunghezza ha un'impedenza di alimentazione di circa 100 Ω. Inserendo una linea λ/4 con impedenza caratteristica di 75 Ω si ottiene una trasformazione ai consueti 50 Ω del radioamatoriale.

<margin>
[picture:311:a_delta_loop:Antenna Delta-Loop]
</margin>

[question:AG117]

<indepth>
Il valore ottimale dell'impedenza caratteristica di una linea di alimentazione λ/4 utilizzata per l'adattamento si calcola come *media geometrica* delle due impedenze, ad esempio 50 Ω e 100 Ω, corrispondente a √(50 Ω · 100 Ω) ≈ 70,7 Ω.
</indepth>

Se si realizza la loop a onda intera come quadrato, la lunghezza di ogni lato deve corrispondere a un quarto della lunghezza d'onda.

[question:AG119]

<attention>
Come nel caso del dipolo, la lunghezza meccanica di un'antenna a loop a onda intera si discosta dalla lunghezza elettrica. Al contrario del fattore di velocità nei dipoli, nelle loop a onda intera si verifica, sorprendentemente, un *fattore di allungamento*, cioè l'antenna deve essere alcuni punti percentuali più lunga di una lunghezza d'onda nello spazio libero.
</attention>

---

Poiché le bande di frequenza presentano diverse condizioni di propagazione a seconda dell'ora del giorno, della stagione e del ciclo solare, i radioamatori desiderano operare su quante più bande di frequenza possibile. Due esempi di antenne multibanda sono l'*antenna G5RV con due bracci di uguale lunghezza* (cfr. figura [ref:a_g5rv]) e una linea bifilare, e l'*antenna Windom asimmetricamente eccitata* (cfr. figura [ref:a_windom]), nelle quali, grazie a dimensioni studiate, si ottengono molte risonanze e quindi la possibilità di utilizzo su molte bande radioamatoriali.

<margin>
[picture:313:a_g5rv:Antenna G5RV]
[picture:309:a_windom:Antenna Windom]
</margin>

[question:AG121]
[question:AG122]

---

% TODO: Verificare la rappresentazione di 5/8 λ

Il fatto che un'antenna sia risonante non significa che abbia anche una buona caratteristica di irradiazione. Spesso si desidera ottenere un'irradiazione il più possibile piatta. Per le antenne verticali eccitate rispetto a terra, una lunghezza di circa 5/8 λ risulta ottimale.

<indepth>
Un semplice filo con la terra come polo opposto, con una lunghezza di 5/8 λ, non è risonante. Le risonanze si verificano solo a 1/4, 3/4, 5/4, ecc. Pertanto, è necessario un adattamento. Questo viene generalmente ottenuto inserendo una bobina che allunga la lunghezza elettrica da 5/8 a 6/8 (cioè 3/4). Tali bobine si vedono spesso nelle antenne per la banda CB o VHF.
% TODO: Immagine antenna VHF o CB per autoveicoli
</indepth>

<attention>
L'ottimale di 5/8 λ vale solo per le antenne eccitate rispetto a terra. Se si considerano, ad esempio, dipoli alimentati al centro che si trovano nello spazio libero o verticalmente, appena sopra il suolo, l'ottimale è a 5/4 λ.
% TODO: La domanda è errata, cfr. seconda revisione di DL9JBE.
</attention>

[question:AG223]