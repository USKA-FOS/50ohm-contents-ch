Idealmente, le correnti attraverso il conduttore interno ed esterno di un cavo coassiale sono esattamente uguali e di direzione opposta. La loro somma è quindi zero e si parla di un puro *segnale di modo differenziale*. In questo caso non si verificano onde di mantel.

Se la somma del segnale è invece diversa da zero, è presente un cosiddetto *segnale di modo comune*. La componente di modo comune di una corrente nel cavo coassiale scorre sempre sulla superficie esterna del conduttore esterno ed è quindi una corrente di mantel con una corrispondente onda di mantel attorno al cavo coassiale.

[question:AG425]

Abbiamo già appreso che un cavo coassiale avvolto attorno a un nucleo di ferrite è adatto per la soppressione delle onde di mantel. Questa è una forma della cosiddetta *bobina di modo comune*.

Una bobina di modo comune è una bobina progettata per bloccare le correnti ad alta frequenza. La bobina di modo comune è una costruzione di una bobina di modo comune in cui due avvolgimenti separati sono avvolti sullo stesso nucleo magnetico. La bobina di modo comune è collegata in modo tale che i segnali di modo differenziale, cioè segnali in cui la corrente in un avvolgimento è esattamente opposta a quella dell'altro avvolgimento e altrimenti hanno la stessa grandezza, non inducono alcun campo magnetico nel nucleo. La bobina di modo comune lascia quindi passare i segnali di modo differenziale senza ostacoli. Le componenti di modo comune, cioè ad esempio le correnti che scorrono solo sul conduttore esterno e quindi solo in un avvolgimento, vengono bloccate dall'induttanza.

[question:AG426]

---

Un trasformatore di isolamento RF rappresenta un'alternativa alla bobina di modo comune. Poiché gli avvolgimenti primario e secondario non sono collegati tra loro, una corrente che entra nel trasformatore di isolamento da un lato deve (almeno approssimativamente) uscire dall'altro lato con la stessa grandezza. Una componente di modo comune è quindi esclusa.

<indepth>
Poiché tra le spire della bobina di un trasformatore di isolamento si crea una capacità e la bobina forma anche una capacità rispetto all'altra bobina, anche un trasformatore di isolamento non sopprime completamente la componente di modo comune di un segnale.
</indepth>

[question:AJ115]

Quando un cavo coassiale è privo di segnali RF di modo comune, il conduttore esterno non presenta alcuna tensione ad alta frequenza rispetto alla terra. Ciò è dovuto al fatto che in un segnale di modo differenziale, cioè correnti opposte nel conduttore interno ed esterno, un campo elettrico si forma esclusivamente tra il conduttore interno ed esterno. Visti dall'esterno, gli effetti delle due correnti si annullano a vicenda, poiché la loro somma è zero. La presenza di onde di mantel è quindi direttamente correlata alla presenza di tensioni RF sul conduttore esterno.

Proprio tali tensioni sul conduttore esterno si verificano, ad esempio, quando colleghiamo un'antenna simmetrica al cavo, poiché nel punto di alimentazione ogni braccio del dipolo presenta una tensione rispetto alla terra. Se colleghiamo i bracci rispettivamente a un conduttore del cavo coassiale, anche il conduttore esterno presenterà una tensione rispetto alla terra.

Le antenne ben messe a terra, ad esempio un'antenna Groundplane con molti radiali ben accordati o interrati, presentano una tensione quasi nulla rispetto alla terra nel punto di alimentazione dei radiali. Le antenne Groundplane mal messe a terra, invece, possono essere suscettibili alle onde di mantel.

Un altro modo in cui possono formarsi onde di mantel è tramite accoppiamento senza contatto nel schermo del cavo coassiale. Se, ad esempio, si posiziona un cavo di alimentazione parallelamente a un braccio del dipolo, si crea un accoppiamento tramite il campo elettromagnetico vicino dell'antenna.

[question:AG427]

Per antenne completamente simmetriche, è possibile utilizzare un cosiddetto balun di tensione per simmetrizzare le correnti nel cavo coassiale. Una forma costruttiva popolare è un autotrasformatore, in cui il cavo coassiale viene collegato al centro e all'estremità di una bobina, e l'antenna viene collegata alle due estremità della bobina.

% TODO: Bild Spannungsbalun / Spartransformator

Con questa costruzione, oltre alla simmetrizzazione desiderata, si verifica anche un raddoppio della tensione ($ü = 2$) e una corrispondente dimezzamento della corrente, che corrisponde a una trasformazione di impedenza 1:4, cioè a un cavo coassiale da $\qty{50}{\ohm}$ deve essere collegata un'antenna con una resistenza di alimentazione di preferenza $\qty{200}{\ohm}$.

[question:AG421]
[question:AG422]

Questa costruzione è tuttavia adatta a sopprimere le onde di mantel solo se l'antenna collegata si comporta effettivamente in modo simmetrico e non viene caricata in modo asimmetrico a causa di influenze ambientali.

Per tutti i componenti che servono alla soppressione delle onde di mantel, è comune che un accoppiamento "senza contatto" tramite i campi elettromagnetici vicini delle antenne possa comunque avvenire direttamente sullo schermo del cavo coassiale, cioè dietro il filtro per onde di mantel. Qui può aiutare, ad esempio, un ulteriore filtro per onde di mantel aggiuntivo a una certa distanza dall'antenna.

[question:AG428]
[question:AG429]