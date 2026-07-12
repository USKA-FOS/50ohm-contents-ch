Un altro modo per sopprimere le onde di modo comune è utilizzare una linea di ritardo di $\lambda / 2$.

[question:AG420]

Come funziona una tale linea di ritardo, sarà spiegato di seguito.

Un'antenna simmetrica richiede una tensione RF rispetto a terra su entrambi i punti di connessione. Le tensioni devono essere uguali in magnitudine, ma con segno opposto, cioè sfasate di $\qty{180}{\degree}$.

Una tale sfasatura può essere ottenuta tramite una linea di ritardo di $\lambda / 2$. Ad esempio, si possono collegare *entrambi* i punti di connessione di un dipolo ripiegato al conduttore interno, dove un punto di connessione viene collegato dopo una linea di ritardo che produce uno sfasamento di $\qty{180}{\degree}$.

Lo schermo del cavo coassiale avrà quindi un potenziale di terra e non si formeranno onde di modo comune.

Tuttavia, bisogna prestare attenzione alle impedenze. Sebbene la linea di ritardo non trasformi direttamente l'impedenza, il collegamento di un'antenna in questo modo provoca comunque una trasformazione dell'impedenza. L'antenna deve avere un'impedenza quattro volte superiore a quella del cavo coassiale affinché vi sia adattamento. La causa è che ogni punto di connessione dell'antenna rispetto a terra ha solo la metà della resistenza, ma entrambi i punti di connessione sono collegati in parallelo, cioè entrambi al conduttore interno.

---

<tip>
Per le due domande successive sulla linea di ritardo, è sufficiente *ricordare* che l'antenna rappresentata è un dipolo ripiegato e che una linea di ritardo di $\lambda/2$ produce uno sfasamento di $\qty{180}{\degree}$.
</tip>

[question:AG423]

<indepth>
Il *collegamento dello schermo del cavo coassiale* al centro del dipolo ripiegato è opzionale e spesso ha ragioni meccaniche (ad esempio, in questo modo il dipolo ripiegato può essere collegato conduttivamente a un supporto metallico messo a terra).
</indepth>

---

[question:AG424]

<attention>
Sebbene la combinazione risulti in una trasformazione di impedenza 1:4, non viene effettuata alcuna trasformazione di impedenza nella linea di ritardo stessa.
</attention>