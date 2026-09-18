I condensatori vengono utilizzati in molte applicazioni in collegamento in serie, in parallelo o anche con una tecnica di circuito misto. Il collegamento in parallelo è più semplice da comprendere, per questo motivo lo analizziamo per primo.

Con il collegamento in parallelo, le piastre opposte sono più numerose e, di conseguenza, la superficie delle piastre aumenta proporzionalmente. Allo stesso modo, aumenta anche la capacità nel circuito complessivo.

<margin>
[picture:822:e_3C-parallel: Collegamento in parallelo di 3 condensatori]
</margin>

---

In un collegamento in parallelo di condensatori di uguale dimensione, la capacità raddoppia, mentre la tenuta in tensione rimane invariata. Naturalmente è possibile calcolare la capacità totale. La formula si trova nella raccolta di formule:

$C_{\mathrm{ges}} = C_{1} + C_{2} + C_{3} + \dots$

<tip>
La capacità totale in un collegamento in parallelo è sempre maggiore della capacità minima di un singolo condensatore.
</tip>

Nel seguente esercizio si aggiunge una difficoltà aggiuntiva, poiché i prefissi dei valori di capacità sono diversi. Prima di tutto è necessario convertire tutti i valori in un prefisso comune. I numeri non devono essere né troppo grandi né troppo piccoli, per questo motivo si consiglia di scegliere il prefisso nano ($\unit{\nano}$). 

$\begin{split} \qty{0,1}{\micro\farad} &= \qty{100}{\nano\farad} \\ \qty{50000}{\pico\farad} &= \qty{50}{\nano\farad}\end{split}$

Ora non resta che sommare tutti i valori in $\unit{\nano\farad}$.

[question:ED117]

<margin>
[photo:262:a_Netzteil BEKO PA $7 \times \qty{10000}{\micro\farad}$ parallel: Collegamento in parallelo di $7 \times \qty{10000}{\micro\farad}$ in un alimentatore di stadio finale]
</margin>

Come test di comprensione si può utilizzare il prossimo esercizio.

[question:ED118]


---

In un collegamento in serie di condensatori, come mostrato nell'illustrazione [ref:e_3C-parallel], aumenta la tenuta in tensione, ma diminuisce la capacità. Naturalmente è possibile calcolare anche la capacità totale. Questa è molto simile al collegamento in parallelo di resistenze:

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

<margin>
[picture:823:e_3C-parallel: Collegamento in serie di 3 condensatori] 
</margin>

<tip>
La capacità totale in un collegamento in serie è sempre minore della capacità minima di un singolo condensatore.
</tip>

<tip>
Per la soluzione degli esercizi si consiglia la seguente procedura:
  
1. Disegnare lo schema del circuito
2. Annotare i valori di capacità dei componenti.
3. Convertire in prefissi uguali.
4. Semplificare il circuito unificando gruppi di circuiti simili
5. Calcolare passo dopo passo la capacità totale
</tip>

Se tutti i condensatori hanno lo stesso valore di capacità, la capacità totale può essere calcolata facilmente dividendo una singola capacità per 3. Nel seguente esercizio si calcola $\qty{0,33}{\micro\farad} / 3 = \qty{0,11}{\micro\farad}$.

[question:ED119]

Nel collegamento in serie di condensatori del seguente esercizio si trovano $\unit{\micro\farad}$ e $\unit{\nano\farad}$ come prefissi. È molto utile convertire prima $\qty{200000}{\nano\farad}$ in $\qty{200}{\micro\farad}$. In un collegamento in serie si può ora applicare la formula presente nella raccolta di formule.


$C_{\mathrm{ges}} =\frac{1}{\frac{1}{\qty{100}{\micro\farad}} + \frac{1}{\qty{200}{\micro\farad}} + \frac{1}{\qty{200}{\micro\farad}}}$

[question:ED120]

---
  
Nella domanda successiva vengono combinati 3 condensatori in collegamento in serie e in parallelo.

[question:ED121]

Quale parte del circuito può essere semplificata per prima? Esatto: il collegamento in serie.
Questo gruppo parziale ha come capacità totale la metà di $\qty{10}{\nano\farad}$, quindi $\qty{5}{\nano\farad}$. Ora è più semplice continuare il calcolo, poiché in un collegamento in parallelo i valori di capacità si sommano. Congratulazioni per il risultato di $\qty{10}{\nano\farad}$.

Gli esercizi successivi sono simili e facilmente risolvibili.

[question:ED122]
[question:ED123]
[question:ED124]

%<margin>
%
%Suggerimenti per le soluzioni:
%
%*ED 118:* Collegamento in serie di $\qty{22}{\nano\farad}$, $\qty{0,033}{\micro\farad} = \qty{33}{\nano\farad}$ e $\qty{15000}{\pico\farad} = \qty{15}{\nano\farad}$.
%$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{\qty{22}{\nano\farad}} + \frac{1}{\qty{33}{\nano\farad}} + \frac{1}{\qty{15}{\nano\farad}}$
%In realtà non è necessario calcolare, perché esiste un solo risultato minore di $\qty{15}{\nano\farad}$.
%*ED 120:* $\qty{50}{\micro\farad}$ 
%*ED 122:* $C_2 = \qty{1}{\micro\farad}$ e $C_3 = \qty{1}{\micro\farad}$ in collegamento in parallelo danno insieme $\qty{2}{\micro\farad}$. Aggiungendo $C_1 = \qty{2}{\micro\farad}$ in serie si ottiene la metà, quindi $\qty{1}{\micro\farad}$.
% 
%*ED 123:* $C_2 = \qty{4}{\nano\farad}$ e $C_3 = \qty{4}{\nano\farad}$ in collegamento in parallelo danno insieme $\qty{8}{\nano\farad}$. Aggiungendo $C_1 = \qty{8}{\nano\farad}$ in serie si ottiene la metà, quindi $\qty{4}{\nano\farad}$.
%  
%*ED 124:* $C_2 = \qty{100}{\nano\farad}$ e $C_3 = \qty{100000}{\pico\farad} = \qty{100}{\nano\farad}$ in collegamento in parallelo danno insieme $\qty{200}{\nano\farad}$. Aggiungendo %$C_1 = \qty{200}{\nano\farad}$ in serie si ottiene la metà, quindi $\qty{100}{\nano\farad}$.
%</margin>
