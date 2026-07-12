La sintesi digitale diretta (Direct Digital Synthesis o DDS in breve) serve per la generazione di segnali periodici a banda limitata con alta risoluzione di frequenza.
Oltre alla sintesi di segnali tramite anelli di controllo PLL, questo metodo di generazione del segnale è oggi ampiamente diffuso nella tecnologia delle comunicazioni e di misurazione e rappresenta lo stato dell'arte. I segnali qui sono molto finemente sintonizzabili in frequenza, a differenza di una classica PLL.

Principio di funzionamento di base di una DDS:

Utilizzando un generatore di clock a frequenza fissa, un contatore di indirizzi viene continuamente incrementato. Al superamento del contatore di indirizzi, questo ricomincia da capo. Ciò genera una sequenza crescente di valori binari alla sua uscita. Utilizzando questi valori, una tabella sinusoidale viene percorsa continuamente. Ciò genera all'uscita della tabella sinusoidale valori di ampiezza digitali per un'oscillazione sinusoidale, che vengono poi trasmessi a un registro. I valori di ampiezza digitali vengono quindi inviati, tramite il clock del registro, a un convertitore D/A a valle, che li converte in un segnale analogico (oscillazione sinusoidale) e lo emette.

<indepth>
Una DDS può anche percorrere diverse tabelle di valori, in modo da poter generare anche forme d'onda cicliche arbitrarie. Controllando il contatore di indirizzi (tramite una Tuning-Word), che influenza continuamente il passo del contatore, la frequenza con cui la tabella di valori viene percorsa può essere controllata entro ampi limiti.
Per il registro degli indirizzi si utilizzano spesso registri con $\qty{32}{\bit}$ o più, di cui solo un numero minore di bit di ordine superiore (ad esempio, i $\qty{14}{\bit}$ superiori) viene utilizzato per percorrere la tabella dei valori. Ciò consente di emettere anche frazioni della frequenza di clock, aumentando così la risoluzione di frequenza della DDS.
Il vantaggio di una DDS rispetto a una PLL è che, controllando i parametri sopra menzionati, si può ottenere una risoluzione di frequenza quasi arbitraria. Inoltre, è possibile passare rapidamente da una frequenza all'altra (controllando tramite la Tuning-Word) senza tempi di assestamento.

La qualità del segnale di uscita di una DDS dipende essenzialmente dalla qualità del generatore di clock utilizzato (stabilità, jitter). Inoltre, anche la risoluzione di ampiezza (quantizzazione) del convertitore D/A e la sua linearità sono decisive per la qualità del segnale di uscita.
</indepth>

[question:AD620]