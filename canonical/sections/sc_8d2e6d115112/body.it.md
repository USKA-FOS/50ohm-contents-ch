Gli oscillatori sono uno degli elementi circuitali più importanti nel radioamatoriale. Sono, per così dire, il cuore di ogni apparecchio radio. Gli oscillatori servono alla generazione di oscillazioni ad alta frequenza nei trasmettitori e nei ricevitori. Esistono diverse possibilità per realizzare tecnicamente gli oscillatori.

---

<margin>
[include:applet_schwingkreis]
</margin>

La forma più semplice di un oscillatore è il cosiddetto *oscillatore LC*, che contiene come elementi determinanti della frequenza un circuito oscillante (costituito da una bobina e un condensatore), che abbiamo imparato a conoscere nel capitolo precedente.

<indepth>
Un oscillatore è composto da un *elemento determinante della frequenza*, ad esempio un circuito oscillante LC o un quarzo, un *amplificatore* e una *retroazione positiva*. La retroazione riporta una parte del segnale di uscita in fase con l'ingresso e compensa le perdite del circuito oscillante. In questo modo vengono generate oscillazioni non smorzate con la frequenza determinata dall'elemento di frequenza.
</indepth>

[question:ED501]

Gli oscillatori LC hanno lo svantaggio che i loro componenti determinanti della frequenza (L e C) possono variare notevolmente in funzione della temperatura, il che può portare a grandi deviazioni di frequenza.

Secondo la raccolta di formule, la formula per la frequenza di oscillazione (formula del circuito oscillante di Thomson) è:

$ f_0 = \frac{1}{2\pi \sqrt{L\cdot C}} $

La frequenza di un oscillatore LC cambia se il valore del condensatore o della bobina varia, ad esempio a causa dell'effetto della temperatura. Come questo influisce sulla frequenza può essere visto nella formula:
Se la *capacità del condensatore* o l'*induttanza della bobina* *aumentano*, la *frequenza del circuito oscillante diminuisce*. Viceversa, la *frequenza del circuito oscillante aumenta* se la capacità o l'induttanza *diminuiscono*.

[question:ED503]
[question:ED505]
[question:ED502]
[question:ED504]

La velocità di variazione della temperatura determina anche la velocità di variazione della frequenza di un oscillatore. Tuttavia, la frequenza non cambia in modo improvviso, poiché gli effetti termici sono sempre soggetti a una certa inerzia. Pertanto, la frequenza di un oscillatore soggetto a temperature fluttuanti di solito cambia lentamente in una direzione o nell'altra.

[question:EF304]

Un tipo di oscillatore molto più stabile in frequenza è l'*oscillatore al quarzo*. In questo caso, come componente determinante della frequenza viene utilizzato un quarzo, la cui frequenza di risonanza dipende in misura molto minore dalla temperatura (rispetto agli oscillatori LC).

[question:ED506]
[question:ED507]

Per evitare irradiazioni indesiderate, gli oscillatori e gli stadi di buffer dovrebbero essere sempre ben schermati. Questo può essere ottenuto, ad esempio, installando l'oscillatore in un contenitore metallico collegato a terra.

[question:EF207]