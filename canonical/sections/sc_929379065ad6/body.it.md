Nella sezione [sec:reihe_parallel_widerstandsnetz_1] abbiamo già analizzato le reti di resistenze. La maggior parte degli esercizi poteva ancora essere risolta abbastanza facilmente a mente. Qui approfondiremo ulteriormente questo argomento. I seguenti esercizi richiedono diversi passaggi di calcolo per arrivare alla soluzione. A tal fine, si scompone l'esercizio in singole aree parziali, che vengono prima calcolate e poi combinate. In questo modo non sono necessarie formule complicate e si arriva in modo affidabile al risultato corretto.

[question:AD106]
[question:AD107]
[question:AD108]

Nel seguente circuito di resistenze è integrato un resistore variabile (potenziometro).
Il valore della resistenza può essere variato da $\qty{0}{\kilo\ohm}$ fino a un massimo di $\qty{1}{\kilo\ohm}$.
Per determinare l'intervallo della resistenza di ingresso dobbiamo quindi considerare due casi limite: da un lato, quando il cursore del potenziometro è a $\qty{0}{\ohm}$, dall'altro, quando è a $\qty{1}{\kilo\ohm}$. Quindi praticamente due esercizi in uno.

---

[question:AD109]

<tip>
Il collegamento in parallelo di $\qty{100}{\ohm}$ con $\qty{200}{\ohm}$ (cursore del potenziometro a $\qty{0}{\ohm}$) o di $\qty{100}{\ohm}$ con $\qty{1,2}{\kilo\ohm}$ (cursore del potenziometro a $\qty{1}{\kilo\ohm}$) dà sempre un valore inferiore a $\qty{100}{\ohm}$. Se poi si aggiungono $\qty{200}{\ohm}$, la resistenza totale non sarà maggiore di $\qty{300}{\ohm}$.
C'è solo una soluzione che soddisfa questa condizione.
</tip>

Ora esaminiamo un circuito di resistenze con 4 resistori, che viene spesso utilizzato. Due partitori di tensione ciascuno in collegamento in parallelo danno luogo a un cosiddetto circuito a ponte. I circuiti a ponte vengono applicati, ad esempio, negli strumenti di misura della resistenza secondo il principio di un cosiddetto ponte di Wheatstone.

---

[question:AD110]

<tip>
Questo esercizio può essere facilmente calcolato a mente. Abbiamo due collegamenti in parallelo con resistenze uguali, che sono state collegate in serie. Con resistenze di uguale valore, i valori di resistenza si dimezzano nel collegamento in parallelo: $R_1 || R_2 = \qty{1100}{\ohm}$ e $R_3 || R_4 = \qty{110}{\ohm}$. Il risultato è quindi solo la somma dei due valori: $R_\mathrm{ges} = \qty{1100}{\ohm} + \qty{110}{\ohm} = \qty{1210}{\ohm}$.
</tip>
