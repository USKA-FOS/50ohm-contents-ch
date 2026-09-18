Idealmente, le correnti che attraversano il conduttore interno e quello esterno di un cavo coassiale sono esattamente uguali in ampiezza e opposte in direzione. La loro somma è quindi nulla e si parla in questo caso di un segnale *a onda inversa pura*. Solo in questo caso non si generano correnti sulla calza.

Se invece la somma del segnale non è nulla, allora è presente un segnale *a onda diretta*. La componente a onda diretta di una corrente in un cavo coassiale fluisce sempre sulla superficie esterna del conduttore esterno e costituisce quindi una corrente sulla calza con un’onda associata che si propaga intorno al cavo coassiale.

[question:AG425]

Abbiamo già imparato che un cavo coassiale avvolto intorno a un nucleo di ferrite è adatto a sopprimere le correnti sulla calza. Questa è una forma di *induttanza di modo comune*.

Una bobina d’arresto è una bobina che serve a bloccare le correnti ad alta frequenza. L’induttanza di modo comune è una variante costruttiva della bobina d’arresto in cui due avvolgimenti separati sono avvolti sullo stesso nucleo magnetico. In questo caso, l’induttanza di modo comune è collegata in modo che i segnali a onda inversa, cioè i segnali in cui la corrente in un avvolgimento è esattamente opposta a quella nell’altro avvolgimento e ha la stessa ampiezza, non inducano un campo magnetico nel nucleo. L’induttanza di modo comune lascia quindi passare senza ostacoli i segnali a onda inversa. Le componenti a onda diretta, invece, ad esempio le correnti che fluiscono solo sul conduttore esterno e quindi solo in un avvolgimento, vengono bloccate dall’induttanza.

[question:AG426]

<margin>
[picture:633:e_mantelwellen:Mantelwellen]
</margin>

---

Un’alternativa all’induttanza di modo comune è un trasformatore di separazione HF. Poiché gli avvolgimenti primario e secondario non sono collegati tra loro, una corrente che entra in un polo del trasformatore di separazione deve (almeno approssimativamente) uscire dall’altro polo con la stessa ampiezza. Una componente a onda diretta è quindi esclusa.

<indepth>
Poiché tra le spire della bobina di un trasformatore di separazione si forma una capacità e la bobina sviluppa anche una capacità rispetto all’altro avvolgimento, un trasformatore di separazione non sopprime completamente la componente a onda diretta di un segnale.
</indepth>

[question:AJ115]

Se un cavo coassiale è privo di segnali HF a onda diretta, il conduttore esterno non presenta alcuna tensione ad alta frequenza rispetto a terra. Questo perché, in un segnale a onda inversa (correnti opposte nel conduttore interno ed esterno), un campo elettrico si forma esclusivamente tra il conduttore interno e quello esterno. Da un punto di vista esterno, gli effetti delle due correnti si annullano perché la loro somma è nulla. La presenza di correnti sulla calza è quindi direttamente correlata alla presenza di tensioni HF sul conduttore esterno.

Tali tensioni sul conduttore esterno si verificano, ad esempio, quando colleghiamo un’antenna simmetrica al cavo, poiché in corrispondenza del punto di alimentazione ogni ramo del dipolo presenta una tensione rispetto a terra. Se colleghiamo i rami rispettivamente ai due conduttori del cavo coassiale, anche il conduttore esterno presenterà una tensione rispetto a terra.

Le antenne ben messe a terra, invece, ad esempio un’antenna *groundplane* con molti radiali ben accordati o interrati, presentano al punto di alimentazione dei radiali una tensione quasi nulla rispetto a terra. Le antenne *groundplane* mal messe a terra, invece, possono essere suscettibili alle correnti sulla calza.

Un’altra possibile causa di correnti sulla calza è l’accoppiamento senza contatto nel schermo del coassiale. Se, ad esempio, un cavo di alimentazione viene fatto correre parallelamente a un ramo di un dipolo, si verifica un accoppiamento tramite il campo elettromagnetico vicino dell’antenna.

[question:AG427]

Per le antenne completamente simmetriche, può essere utilizzato un *bilanciatore di tensione* per simmetrizzare le correnti nel cavo coassiale. Una forma costruttiva molto diffusa è un autotrasformatore in cui il cavo coassiale viene collegato al centro e alla fine di una bobina, mentre l’antenna viene collegata ai due estremi della bobina.

% TODO: Immagine bilanciatore di tensione / autotrasformatore

In questa configurazione, oltre alla simmetrizzazione desiderata, si verifica anche un raddoppio della tensione ($r = 2$) e una conseguente dimezzamento della corrente, che corrisponde a una trasformazione di impedenza 1:4, cioè a un cavo coassiale da $\qty{50}{\ohm}$ va collegata un’antenna con un’impedenza di alimentazione di $\qty{200}{\ohm}$.

[question:AG421]
[question:AG422]

Questa configurazione è tuttavia adatta a sopprimere le correnti sulla calza solo se l’antenna collegata si comporta effettivamente in modo simmetrico e non viene caricata in modo asimmetrico a causa di influenze ambientali.

Tutti i componenti che servono a sopprimere le correnti sulla calza hanno in comune il fatto che può comunque verificarsi un accoppiamento "senza contatto" tramite i campi elettromagnetici vicini dell’antenna direttamente sullo schermo del coassiale, cioè dopo l’induttanza di modo comune. In questo caso, può essere utile un’ulteriore induttanza di modo comune posizionata a una certa distanza dall’antenna.

[question:AG428]
[question:AG429]