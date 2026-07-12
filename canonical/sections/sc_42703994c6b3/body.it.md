<margin>
[picture:804:mischer_linear_vs_nichtlinear:Resistenza lineare e diodo non lineare]
</margin>

Le caratteristiche di controllo di gruppi o componenti possono avere un carattere lineare, non lineare o misto a tratti. Ad esempio, una resistenza ha una caratteristica lineare, mentre la caratteristica di un diodo è non lineare [ref:mischer_linear_vs_nichtlinear].

Nell'area lineare delle caratteristiche di controllo non si verificano distorsioni dei segnali di ingresso, poiché a ogni variazione di un segnale di ingresso corrisponde una variazione proporzionalmente uguale del segnale di uscita. Matematicamente ciò corrisponde a un comportamento lineare (addizione). Un esempio di caratteristica di controllo uniformemente lineare è una resistenza. Nelle caratteristiche di controllo lineari o nell'area lineare delle caratteristiche di controllo **non** avviene alcun processo di miscelazione.

Nell'area non lineare delle caratteristiche di controllo si verificano distorsioni dei segnali di ingresso, poiché una variazione di un segnale di ingresso non provoca una variazione proporzionalmente uguale di un segnale di uscita. Matematicamente ciò corrisponde a un comportamento non lineare in cui avviene una moltiplicazione delle grandezze di ingresso e quindi si creano prodotti di miscelazione aggiuntivi (a seconda della forma della caratteristica). Pertanto, nell'area non lineare delle caratteristiche di controllo avviene sempre un processo di miscelazione. I prodotti di miscelazione creano sempre frequenze aggiuntive nel segnale di uscita che sono prevalentemente presenti nel segnale di uscita come somme e differenze delle frequenze di ingresso.

In pratica, tuttavia, si formano anche molti prodotti di miscelazione indesiderati di ordine superiore, che devono essere soppressi in modo mirato mediante misure tecniche come la filtratura.

%TODO EVENTUALMENTE RIFERIMENTO A ULTERIORE LETTERATURA O BACKGROUND MATEMATICO

[question:AF212]

---
<margin>
[picture:805:mischer_ringmischer:Miscelatore bilanciato, miscelatore ad anello o anche modulatore ad anello]
</margin>

L'obiettivo di un miscelatore è che idealmente solo i prodotti di miscelazione desiderati appaiano alla sua uscita e i prodotti di miscelazione indesiderati, così come i segnali di ingresso, siano soppressi al massimo.

Questo obiettivo si raggiunge al meglio con l'aiuto di un cosiddetto miscelatore bilanciato. Questo è costruito con 4 diodi o transistor in una schaltung ad anello [ref:mischer_ringmischer]. Grazie alla sua struttura simmetrica, i segnali di ingresso vengono soppressi al massimo all'uscita. Altre forme di miscelatori, come ad esempio i miscelatori a doppio diodo, i miscelatori a doppio transistor e i miscelatori a diodi additivi, a causa della loro struttura asimmetrica, lasciano sempre passare anche uno dei segnali di ingresso all'uscita.

<indepth>
Funzionamento di un miscelatore ad anello:

L'oscillatore locale ($U_2$ nello schema) rende conduttivi alternativamente due diodi opposti durante una semionda, mentre gli altri due diodi sono bloccati. Nella semionda successiva dell'oscillatore locale, le condizioni si invertono esattamente. A tal fine, l'ampiezza dell'oscillatore locale ($U_2$) deve essere sufficientemente elevata affinché i diodi possano essere pilotati adeguatamente durante le semionde positive e negative.

Ciò fa sì che l'anello di diodi funzioni come un invertitore di polarità per il segnale presente all'ingresso ($U_1$).
Per ottenere un buon risultato di miscelazione per quanto riguarda i prodotti di miscelazione indesiderati e la soppressione del segnale di ingresso, la sua ampiezza deve essere significativamente inferiore all'ampiezza dell'oscillatore locale.
Valori ottimali vengono raggiunti con i cosiddetti miscelatori ad anello ad alto livello, il cui livello di ingresso LO può essere fino a $\qty{10}{\milli\watt}$.
</indepth>

<tip>
È importante notare che il miscelatore ad anello può essere distinto da un circuito raddrizzatore a diodi, che ha un aspetto molto simile, dal fatto che i diodi nel miscelatore ad anello sono collegati in serie come un anello (catodo collegato all'anodo del diodo successivo). Nel raddrizzatore, invece, sono sempre collegati 2 catodi e 2 anodi.
</tip>
  
Il miscelatore bilanciato, chiamato anche miscelatore ad anello o modulatore ad anello, è il più adatto per sopprimere i segnali di uscita indesiderati.

% FEEDBACK: Come funziona il tutto? Non è chiaro! Inoltre: Indicazione sulla confusione con il raddrizzatore a ponte!
% RISPOSTA AL FEEDBACK: Abbiamo ampliato l'articolo con un consiglio e approfondimenti sui punti sollevati.

[question:AF213]
[question:AF214]