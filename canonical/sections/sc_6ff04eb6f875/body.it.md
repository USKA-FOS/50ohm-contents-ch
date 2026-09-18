La *Sintesi Digitale Diretta*, in inglese *Direct Digital Synthesis* o più brevemente DDS [index:Sintesi Digitale Diretta] [index:DDS], serve per la generazione di segnali periodici con una frequenza regolabile con grande precisione. Oggi viene impiegata, accanto alla sintesi di frequenza con circuiti PLL, spesso nei moderni apparati radioamatoriali. Un vantaggio fondamentale della DDS consiste nel fatto che la frequenza di uscita può essere impostata digitalmente con una risoluzione molto elevata. Inoltre, è possibile passare molto rapidamente tra frequenze diverse, poiché non è necessario attendere che un anello di regolazione si stabilizzi su una nuova frequenza, come avviene in una classica PLL.

<margin>
[picture:1082:a_dds_aufbau:Schema a blocchi di una DDS (Direct Digital Synthesizer)]
</margin>

La struttura di base di una DDS è illustrata in [ref:a_dds_aufbau]. Un generatore di clock produce un segnale di clock con una frequenza fissa $f_\mathrm{Takt}$. Ad ogni impulso di clock, un accumulatore di fase [index:DDS:Accumulatore di fase], detto anche contatore di indirizzi, incrementa il valore di fase corrente di un incremento di fase $K$:

$\varphi_{n+1} = \varphi_n + K$

L’incremento di fase $K$ è anche denominato *Tuning Word*. Esso determina di quanti passi di fase l’accumulatore di fase viene avanzato ad ogni impulso di clock. Il valore corrente dell’accumulatore di fase funge da indirizzo per una tabella di valori, detta anche *tabella di ricerca* (*Lookup-Tabelle*). Per la generazione di un’oscillazione sinusoidale, questa tabella contiene i valori digitali di ampiezza di un periodo sinusoidale completo. Per ogni valore di fase viene letto il corrispondente valore di ampiezza dalla tabella del seno. La dimensione dell’incremento di fase $K$ determina la velocità con cui la tabella del seno viene attraversata e, di conseguenza, la frequenza del segnale di uscita. L’incremento di fase può essere, ad esempio, controllato da un microcontrollore. Un registro preleva il valore digitale di ampiezza in sincronia con il segnale di clock e lo trasmette a un convertitore D/A. Quest’ultimo converte la sequenza dei valori digitali di ampiezza in un segnale analogico, inizialmente a gradini. Un filtro passa-basso posto a valle elimina le componenti indesiderate ad alta frequenza e smussa il segnale di uscita.

---

Il seguente esempio lo illustra chiaramente: con un incremento di fase $K=1$, il valore di fase viene incrementato di esattamente un passo ad ogni impulso di clock ($\varphi_{n+1} = \varphi_n + 1$). La tabella del seno viene quindi attraversata passo dopo passo. Quando viene generato un periodo completo, il contatore di indirizzi viene resettato e l’accumulatore di fase ricomincia da capo. Il segnale di uscita risultante è mostrato in [ref:a_dds_phaseninkrement_k1].

<margin>
[picture:1083:a_dds_phaseninkrement_k1:Segnale di confronto]
</margin>

---

Se l’incremento di fase viene raddoppiato a $K=2$, il valore di fase viene incrementato di due passi ad ogni impulso di clock ($\varphi_{n+1} = \varphi_n + 2$). Di conseguenza, vengono richiamati solo ogni secondo valore di fase e la tabella del seno viene attraversata due volte più velocemente. Il periodo del segnale di uscita si dimezza e la sua frequenza raddoppia. Questo è illustrato in [ref:a_dds_phaseninkrement_k2].

<margin>
[picture:1084:a_dds_phaseninkrement_k2:Incremento di fase raddoppiato e frequenza di uscita raddoppiata]
</margin>

[question:AD620]

<indepth>
Se l’accumulatore di fase ha una larghezza di $N$ bit, può rappresentare $2^N$ valori di fase diversi. Quando viene superato il valore massimo, il contatore si azzera e ricomincia da capo:

$\varphi_{n+1} = \left(\varphi_n + K\right) \bmod 2^N$

Questo azzeramento corrisponde al passaggio da $\qty{360}{\degree}$ a $\qty{0}{\degree}$. L’incremento di fase $K$ può essere scelto quasi arbitrariamente e non deve essere una potenza di due. In questo modo è possibile generare anche frequenze di uscita che non sono divisori interi della frequenza di clock.

Una DDS non è inoltre limitata alle oscillazioni sinusoidali. Se la tabella di valori contiene, ad esempio, i valori di ampiezza di un’oscillazione triangolare o a dente di sega, la DDS può generare anche queste forme d’onda.

La qualità del segnale di uscita dipende principalmente dalla stabilità e dal jitter [index:Jitter] del generatore di clock, nonché dalla risoluzione e dalla linearità del convertitore D/A. A causa del numero limitato di valori di fase e ampiezza, si verificano errori di quantizzazione e componenti spettrali aggiuntive. Un filtro passa-basso posto a valle sopprime gran parte di queste componenti indesiderate del segnale.