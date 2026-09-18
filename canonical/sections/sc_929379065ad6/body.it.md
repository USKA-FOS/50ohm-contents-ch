Nella classe E abbiamo già analizzato reti resistive. La maggior parte dei problemi poteva essere risolta abbastanza facilmente a mente. Nella classe A questo argomento viene approfondito ulteriormente. I problemi seguenti richiedono diversi passaggi di calcolo per giungere alla soluzione. Per farlo, si suddivide il problema in aree parziali che vengono calcolate inizialmente e poi combinate tra loro. In questo modo non servono formule complesse e si giunge in modo affidabile al risultato corretto.

[question:AD106]
[question:AD107]
[question:AD108]

Nel seguente circuito resistivo è inserita una resistenza variabile (potenziometro).
Il valore della resistenza può essere modificato da $\qty{0}{\kilo\ohm}$ fino a un massimo di $\qty{1}{\kilo\ohm}$. 
Per determinare l’intervallo della resistenza d’ingresso dobbiamo considerare due casi limite: da un lato, quando il cursore del potenziometro è su $\qty{0}{\ohm}$, dall’altro, quando è su $\qty{1}{\kilo\ohm}$. Quindi, in pratica, due problemi in uno.

---

[question:AD109]

<tip>
Il collegamento in parallelo di $\qty{100}{\ohm}$ con $\qty{200}{\ohm}$ (potenziometro su $\qty{0}{\ohm}$) o di $\qty{100}{\ohm}$ con $\qty{1,2}{\kilo\ohm}$ (potenziometro su $\qty{1}{\kilo\ohm}$) restituisce sempre un valore inferiore a $\qty{100}{\ohm}$. Se si aggiunge ancora $\qty{200}{\ohm}$, la resistenza totale non supererà $\qty{300}{\ohm}$.
Esiste un’unica soluzione che soddisfa questa condizione.
</tip>

Ora analizziamo un circuito resistivo con 4 resistenze, spesso utilizzato. Due partitori di tensione collegati in parallelo formano una cosiddetta configurazione a ponte. Le configurazioni a ponte vengono impiegate, ad esempio, negli strumenti di misura della resistenza secondo il principio del ponte di Wheatstone.

---

[question:AD110]

<tip>
Questo problema può essere risolto facilmente anche a mente. Abbiamo due collegamenti in parallelo con resistenze uguali, collegate in serie. Con resistenze di valore uguale, i valori delle resistenze si dimezzano nel collegamento in parallelo: $R_1 || R_2 = \qty{1100}{\ohm}$ e $R_3 || R_4 = \qty{110}{\ohm}$. Il risultato è semplicemente la somma dei due valori: $R_\mathrm{ges} = \qty{1100}{\ohm} + \qty{110}{\ohm} = \qty{1210}{\ohm}$.
</tip>
