Una Phase-Locked Loop (PLL) serve a sincronizzare un oscillatore variabile, potenzialmente instabile (VCO – Voltage Controlled Oscillator) utilizzando un oscillatore di riferimento stabile. Il confronto di fase tra i due segnali viene utilizzato per generare una frequenza di uscita stabile.

Struttura di base ed elementi di una PLL

Una PLL è costituita essenzialmente dai seguenti componenti:
1. **Comparatore di fase:** Confronta le fasi dei segnali provenienti dal VCO e dall'oscillatore di riferimento.
2. **Filtro passa-basso:** Converte gli impulsi generati dal comparatore di fase in una tensione continua.
3. **Oscillatore controllato in tensione (VCO):** Genera il segnale di uscita, la cui frequenza è controllata dalla tensione continua erogata dal filtro passa-basso.

Inoltre, la PLL può essere integrata con un **divisore di frequenza** per sincronizzare la frequenza del VCO su multipli della frequenza di riferimento.

Principio di funzionamento

1. **Confronto di fase e correzione**:  

Il comparatore di fase misura la differenza di fase tra i segnali del VCO e dell'oscillatore di riferimento. In caso di deviazione di fase, emette impulsi che corrispondono all'errore. Questi impulsi vengono livellati dal filtro passa-basso e convertiti in una tensione continua proporzionale.

2. **Regolazione del VCO**:  

La tensione continua generata funge da segnale di controllo per il VCO, che ne regola la frequenza in modo da ridurre gradualmente la differenza di fase a zero. Quando questo stato viene raggiunto, si dice che la PLL è "agganciata" (locked).

3. **Stato agganciato**:  

Nello stato stabile della PLL, le frequenze e le posizioni di fase dei due segnali sono identiche. La frequenza di uscita è stabile e corrisponde essenzialmente alla frequenza di riferimento o ai suoi multipli (a seconda del rapporto di divisione scelto del divisore di frequenza).

<margin>
[picture:45:a_oszillator_pll_pll:Rappresentazione di una Phase-Locked Loop (PLL)]  
</margin>

[question:AD701]
[question:AD702]

Precisione e stabilità

La precisione e la stabilità della frequenza di uscita della PLL dipendono principalmente dalla qualità dell'oscillatore di riferimento, che è solitamente un oscillatore a quarzo.

[question:AD705]

Divisione di frequenza e sintonizzabilità

Per impostare una PLL su frequenze diverse, è possibile utilizzare un divisore di frequenza all'interno del circuito di controllo. Ciò consente di generare la frequenza di uscita come multiplo intero della frequenza di riferimento. L'intervallo di frequenza selezionabile più piccolo corrisponde alla frequenza dell'oscillatore di riferimento, poiché la divisione può avvenire solo in passaggi interi.

[question:AD703]

Calcolo del rapporto di divisione

Per ottenere una determinata frequenza di uscita data una frequenza di riferimento, il fattore di divisione viene scelto in modo che la stessa frequenza arrivi agli ingressi del comparatore di fase. Ciò consente di calcolare il rapporto di divisione necessario per la frequenza di uscita desiderata.

[question:AD704]
