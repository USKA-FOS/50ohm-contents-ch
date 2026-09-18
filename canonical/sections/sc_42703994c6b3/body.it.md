<margin>
[picture:804:mischer_linear_vs_nichtlinear:Resistenza lineare e diodo non lineare]
</margin>


I componenti e i moduli possono comportarsi in modo *lineare* o *non lineare*. In un componente lineare, la grandezza di uscita segue quella di ingresso secondo una relazione fissa. Una resistenza ideale, ad esempio, ha una caratteristica lineare. La caratteristica di un diodo, invece, è non lineare (cfr. [ref:mischer_linear_vs_nichtlinear]).

Per un processo di miscelazione, un comportamento puramente lineare non è sufficiente. Se più segnali vengono trasmessi attraverso un circuito lineare, possono essere amplificati, attenuati o sommati tra loro, ma non si influenzano reciprocamente. Non si generano quindi nuove componenti di frequenza.

Affinché avvenga una miscelazione, i segnali di ingresso devono essere combinati tra loro. Questo può avvenire, ad esempio, grazie alla caratteristica non lineare di un diodo o di un transistor. Un'altra possibilità molto utilizzata consiste nell'accendere e spegnere rapidamente il segnale di ingresso, o invertirne la polarità, mediante il segnale dell'oscillatore. Anche questa operazione di commutazione non è un processo lineare e provoca la combinazione dei due segnali.

È proprio questa proprietà che viene sfruttata intenzionalmente in un mixer. Per questo motivo, gli stadi di miscelazione funzionano con componenti non lineari o con circuiti in cui transistor o diodi vengono commutati dal segnale dell'oscillatore.
In pratica, tuttavia, si formano anche molti prodotti di miscelazione indesiderati di ordine superiore, che devono essere soppressi intenzionalmente mediante misure tecniche come la filtrazione.

[question:AF212]

L'obiettivo di un mixer è che, alla sua uscita, appaiano idealmente solo i prodotti di miscelazione desiderati, mentre i prodotti indesiderati e i segnali di ingresso vengano soppressi al massimo.

Questo obiettivo si raggiunge al meglio con un cosiddetto *miscelatore bilanciato*. Esso è realizzato con 4 diodi o transistor collegati a formare un anello [ref:mischer_ringmischer]. Grazie alla sua struttura simmetrica, i segnali di ingresso vengono soppressi al massimo all'uscita. Altre tipologie di mixer, come ad esempio il mixer a diodi doppi, il mixer a transistor duali o il mixer a diodi additivi, a causa della loro struttura asimmetrica, trasmettono sempre uno dei segnali di ingresso all'uscita.

<indepth>
Funzionamento di un mixer ad anello:

L'oscillatore locale ($U_2$ nel diagramma) commuta sempre due diodi opposti in conduzione durante una semionda, mentre gli altri due diodi sono bloccati. Nella semionda successiva dell'oscillatore locale, le condizioni si invertono esattamente. Per questo motivo, l'ampiezza dell'oscillatore locale ($U_2$) deve essere sufficientemente elevata affinché i diodi possano essere portati in conduzione durante le semionde positive e negative.

In questo modo, il ring di diodi funziona come un invertitore di polarità per il segnale applicato all'ingresso ($U_1$).
Per ottenere un buon risultato di miscelazione in termini di prodotti indesiderati e soppressione del segnale di ingresso, la sua ampiezza deve essere notevolmente inferiore a quella dell'oscillatore locale.
Valori ottimali si ottengono con i cosiddetti *mixer ad anello ad alto livello*, la cui potenza di ingresso dell'oscillatore locale può arrivare fino a $\qty{10}{\milli\watt}$.

<webonly>
[include:applet_ringmodulator]
</webonly>
<latexonly>
[picture:805:mischer_ringmischer:Miscelatore bilanciato, mixer ad anello o anche modulatore ad anello]
</latexonly>
</indepth>

<tip>
È importante distinguere il mixer ad anello dal circuito di un raddrizzatore a diodi, che appare molto simile, poiché nei mixer ad anello i diodi sono collegati in serie a formare un anello (il catodo di ciascun diodo è collegato all'anodo del diodo successivo). Nel raddrizzatore, invece, sono sempre collegati 2 catodi e 2 anodi.
</tip>

Il miscelatore bilanciato, chiamato anche mixer ad anello o modulatore ad anello, è il più adatto per sopprimere i segnali di uscita indesiderati.

[question:AF213]
[question:AF214]
