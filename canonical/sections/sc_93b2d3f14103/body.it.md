%TODO: Questo capitolo non è ancora stato completato e deve essere rivisto!!!

Il fattore di amplificazione prima degli amplificatori è solitamente espresso in decibel ($\qty{\frac{1}{10}}{\bel}$). È sempre necessario considerare se si sta considerando l'amplificazione di tensione o l'amplificazione di potenza di un amplificatore.
*Infatti, potenza e tensione sono quadraticamente correlate* e devono essere calcolate in modo diverso!
Un raddoppio della tensione da parte di un amplificatore corrisponde a un quadruplicamento della potenza (con la stessa impedenza all'ingresso e all'uscita dell'amplificatore).

Considerando l'amplificazione di tensione di un amplificatore, possiamo esprimerla in decibel ($\unit{\dB}$). Per fare ciò, dobbiamo mettere in rapporto i due livelli di tensione al quadrato (livello di uscita e livello di ingresso) ed estrarre il logaritmo in base dieci. Otterremo quindi il risultato in Bel. Per convertirlo in decibel, deve essere moltiplicato per il fattore $10$.
Per poter utilizzare direttamente i livelli di tensione nel calcolo e non doverli prima elevare al quadrato, si può estrarre il quadrato come fattore $2$ dal logaritmo in base dieci. Pertanto, in questo caso, il risultato deve essere moltiplicato per il fattore $2$. In totale, quindi, per il fattore $10 \cdot 2 = 20$.

<tip>
Breve excursus sul calcolo dei logaritmi

Un quadrato all'interno del logaritmo può essere "estratto" dal logaritmo. In questo caso, il quadrato diventa il fattore $2$. Lo stesso vale per potenze superiori. In questo caso, la potenza diventa sempre il moltiplicatore davanti al logaritmo quando viene "estratta" dal logaritmo.

Esempio: $\log(x^2) = 2 \cdot \log(x)$
</tip>

%TODO: Suggerimento con calcolo di Bel e decibel per rapporti di tensione e potenza con spiegazione del perché il fattore $2$ va davanti al logaritmo (il quadrato del logaritmo diventa fattore $2$ quando estratto).

Considerando l'amplificazione di potenza di un amplificatore, possiamo anche esprimerla in decibel ($\unit{\dB}$). Per fare ciò, dobbiamo mettere in rapporto i due livelli di potenza (livello di uscita e livello di ingresso) ed estrarre il logaritmo in base dieci. Successivamente, il risultato deve essere moltiplicato per il fattore $10$ per ottenere l'amplificazione di potenza in $\unit{\dB}$.

Le formule corrispondenti per il calcolo dell'amplificazione di potenza e dell'amplificazione di tensione degli amplificatori si trovano anche nella raccolta di formule.

[question:AD427]
[question:AD428]

Se si desidera ora calcolare inversamente il rapporto tra potenza d’uscita e potenza d’ingresso dall'amplificazione di potenza in $\unit{\dB}$, è necessario prima riconvertire il valore in $\unit{\dB}$ in Bel, dividendolo prima per il fattore $10$. Questo valore deve quindi essere calcolato come esponente di $10$.
Da ciò si ottiene il fattore di amplificazione, che deve essere moltiplicato per la potenza d’ingresso per ottenere la potenza d’uscita di un amplificatore.
In questo caso, è opportuno memorizzare determinati rapporti in $\unit{\dB}$ (vedi raccolta di formule!). Ciò può semplificare notevolmente il calcolo.

Esempio:
Per convertire un'amplificazione di $\qty{13}{\dB}$ nel fattore di amplificazione, si può ricordare che $\qty{3}{\dB}$ corrispondono sempre a un raddoppio della potenza e $\qty{10}{\dB}$ a un decuplicamento della potenza. In questo caso, si moltiplicano i fattori di amplificazione $2$ e $10$ tra loro e si ottiene per $\qty{13}{\dB}$ il fattore di amplificazione $20$.

<tip>
Nel calcolo con valori in $\unit{\dB}$, si può ricordare che l'addizione di singoli valori in $\unit{\dB}$ (noti) corrisponde sempre a una moltiplicazione dei corrispondenti fattori di amplificazione.

Esempio:
  
$\qty{3}{\dB}$ = fattore $2$ per la potenza e fattore $\sqrt{2}$ per la tensione

$\qty{6}{\dB}$ = fattore $4$ per la potenza e fattore $\sqrt{4}$ per la tensione

$\qty{10}{\dB}$ = fattore $10$ per la potenza e fattore $\sqrt{10}$ per la tensione

$\qty{20}{\dB}$ = fattore $100$ per la potenza e fattore $\sqrt{100}$ per la tensione

$\qty{26}{\dB}$ per la potenza = $\qty{20}{\dB}$ + $\qty{6}{\dB}$ = fattore $100 \times$ fattore $4 =$ fattore $400$

Quindi, un'amplificazione di potenza di $\qty{26}{\dB}$ corrisponde a un fattore di amplificazione di potenza di $400$.
  
L'amplificazione di tensione corrispondente si calcola come:

Fattore $10 \times$ fattore $2 =$ fattore $20$

In alternativa: $\sqrt{400}$, se si utilizza come base il fattore di amplificazione di potenza.
</tip>

[question:AD426]