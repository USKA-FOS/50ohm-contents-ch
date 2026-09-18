Un anello ad aggancio di fase (PLL) può, ad esempio, sincronizzare un oscillatore controllato in tensione (VCO) variabile e potenzialmente instabile con un oscillatore di riferimento stabile (G). A tal fine, confronta le fasi dei due segnali e regola il VCO in modo che si ottenga una frequenza di uscita stabile. Nel radioamatore, le PLL vengono utilizzate principalmente per la generazione stabile e precisa di frequenze in trasmettitori e ricevitori, ad esempio per la selezione dei canali, la generazione di frequenze di miscelazione e la sincronizzazione di oscillatori.

Una PLL è composta essenzialmente dalle seguenti componenti:

* *Confrontatore di fase*: confronta le fasi dei segnali provenienti dal VCO e dall’oscillatore di riferimento.
* *Filtro passa-basso*: converte gli impulsi generati dal confrontatore di fase in una tensione continua.
* *VCO*: genera il segnale di uscita, la cui frequenza è controllata dalla tensione continua fornita dal filtro passa-basso.

[question:AD701]

Opzionalmente, la PLL può essere integrata da un *divisore di frequenza* per sincronizzare la frequenza del VCO su multipli della frequenza di riferimento.

<margin>
[picture:45:a_oszillator_pll:Rappresentazione schematica di un anello ad aggancio di fase (PLL)]  
</margin>

---

Il confrontatore di fase misura la differenza di fase tra i segnali del VCO ($f_\mathrm{out}$) e dell’oscillatore di riferimento ($f_\mathrm{ref}$). In caso di scostamento di fase, emette impulsi corrispondenti all’errore. Questi impulsi vengono smorzati dal filtro passa-basso e convertiti in una tensione continua proporzionale. La tensione continua generata funge da segnale di comando per il VCO, che regola la sua frequenza in modo che la differenza di fase si riduca gradualmente a zero. Quando questo stato viene raggiunto, si dice che la PLL è "agganciata" (locked), cioè in uno *stato stabile*. Nello stato stabile della PLL, le frequenze e le fasi dei due segnali sono identiche. Vale:


$f_\mathrm{ref}=\frac{f_\mathrm{out}}{n}$


La frequenza di uscita è stabile e corrisponde essenzialmente alla frequenza di riferimento o ai suoi multipli (a seconda del rapporto di divisione scelto del divisore di frequenza).


Il principio di funzionamento è illustrato in un esempio semplice nella figura [ref:a_oszillator_pll]: l’oscillatore di riferimento fornisce al punto A una frequenza di $f_\mathrm{ref}=\qty{10}{\mega\hertz}$. La frequenza di uscita del VCO viene divisa al punto C dal divisore di frequenza con rapporto di divisione $n=100$. Quando la PLL è agganciata, cioè nello *stato stabile*, le frequenze nei punti A e B sono uguali. Da ciò deriva per la frequenza di uscita:


$f_\mathrm{out}=n\cdot f_\mathrm{ref}=100\cdot\qty{10}{\mega\hertz}=\qty{1}{\giga\hertz}$


Il VCO genera quindi una frequenza di $\qty{1}{\giga\hertz}$, che viene divisa dal divisore di frequenza a $\qty{10}{\mega\hertz}$ e confrontata con la frequenza di riferimento.


<indepth>
Una PLL può essere realizzata in modo analogico, digitale o come combinazione delle due tecniche. Negli apparecchi radio vengono spesso utilizzati confrontatori di fase digitali e divisori di frequenza con un filtro di anello analogico e un VCO.
</indepth>

[question:AD702]


La precisione e la stabilità della frequenza di uscita della PLL dipendono principalmente dalla qualità dell’oscillatore di riferimento, che di solito è un oscillatore a quarzo.


[question:AD705]


Per regolare una PLL su frequenze diverse, ciò può essere fatto tramite il divisore di frequenza. In questo modo è possibile generare la frequenza di uscita come un multiplo intero della frequenza di riferimento. Il più piccolo intervallo di frequenza selezionabile corrisponde alla frequenza dell’oscillatore di riferimento, poiché la divisione avviene solo in passi interi. In un apparecchio radio FM con una griglia di canale di $\qty{12,5}{\kilo\hertz}$, può quindi essere utilizzata una frequenza di confronto di $\qty{12,5}{\kilo\hertz}$. Se il rapporto di divisione $n$ viene aumentato o diminuito di uno, la frequenza di uscita cambia di conseguenza di $\qty{12,5}{\kilo\hertz}$. In questo modo, la PLL può essere regolata sui singoli canali radio.


[question:AD703]


Per ottenere una determinata frequenza di uscita con una data frequenza di riferimento, il fattore di divisione viene scelto in modo che la stessa frequenza sia presente agli ingressi del confrontatore di fase. In questo modo è possibile calcolare il rapporto di divisione necessario per la frequenza di uscita desiderata.


[question:AD704]