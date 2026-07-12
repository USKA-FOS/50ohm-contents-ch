A differenza della modulazione, che avviene sul lato del trasmettitore, la demodulazione dei segnali nel ricevitore converte nuovamente un segnale modulato in AF (audiofrequenza) rendendolo udibile.

A seconda del tipo di modulazione utilizzato sul lato del trasmettitore, è necessaria una demodulazione corrispondente sul lato del ricevitore.
A tale scopo esistono diversi concetti di circuito che consentono la demodulazione.

La forma più semplice di demodulazione di un segnale ad alta frequenza è la modulazione di ampiezza (AM).
I segnali AM possono essere demodulati utilizzando un cosiddetto demodulatore di inviluppo come mostrato nella figura [ref:demodulator_huellkurvendemodulator_am]. A tale scopo, il segnale ad alta frequenza viene prima selezionato in base alla frequenza di ricezione desiderata, ad esempio mediante un circuito risonante adattato, e quindi raddrizzato da un diodo. Un condensatore collegato a valle del diodo viene caricato al valore di picco istantaneo del segnale e contemporaneamente scaricato attraverso una resistenza collegata in parallelo con una costante di tempo appropriata. Questa costante di tempo è notevolmente superiore alla durata del periodo del segnale HF ma notevolmente inferiore alla durata del periodo del segnale AF.

<margin>
[picture:141:demodulator_huellkurvendemodulator_am:Demodulatore di inviluppo per la demodulazione di segnali AM]
</margin>

[question:AD501]

Sul collegamento X nella figura [ref:demodulator_huellkurvendemodulator_am_2] viene visualizzata la tensione di picco raddrizzata del segnale HF, che diminuisce leggermente tra i picchi del segnale HF in base alla costante di tempo della resistenza collegata in parallelo al condensatore. L'inviluppo del segnale corrisponde quindi all'AF modulata, che a causa della costante di tempo del condensatore è sovrapposta a un segnale a dente di sega (frequenza portante) e corrisponde al segnale nella figura [ref:demodulator_huellkurvendemodulator_am_abbx]. Negli stadi di elaborazione AF successivi (non mostrati) i residui di questa frequenza portante vengono quindi filtrati, in modo che l'AF pura rimanga come segnale di uscita.

<margin>
[picture:607:demodulator_huellkurvendemodulator_am_2:Demodulatore di inviluppo per la demodulazione di segnali AM con visualizzazione del segnale di ingresso IF che arriva all'ingresso del demodulatore]
[picture:146:demodulator_huellkurvendemodulator_am_abbx:Segnale demodulato al punto X del demodulatore di inviluppo]
</margin>

[question:AD502]

---
<margin>
[picture:841:demodulator_flankendiskriminator:Circuito risonante utilizzato come discriminatore di fianco]

[picture:149:demodulator_flankendiskriminator_schaltung:Discriminatore di fianco FM]
</margin>

Un circuito molto simile al suddetto demodulatore di inviluppo può essere utilizzato per la demodulazione di segnali FM.
Partendo dalla frequenza intermedia nel ricevitore FM, come mostrato nella figura [ref:demodulator_flankendiskriminator], il segnale entra in un circuito risonante la cui frequenza di risonanza $f_\text{res}$ è leggermente al di sopra o al di sotto della frequenza IF $f_\text{IF}$. In questo modo, il segnale FM da demodulare si trova sul fianco del circuito risonante e converte le variazioni di frequenza dell'FM in variazioni di ampiezza. Utilizzando il demodulatore AM collegato a valle, il segnale FM, ora convertito in un segnale AM, viene demodulato e reso udibile. Questo circuito, mostrato nella figura [ref:demodulator_flankendiskriminator_schaltung], è chiamato discriminatore di fianco.

[question:AD504]

I segnali modulati in FM possono anche essere demodulati utilizzando una PLL (Phase Locked Loop). In una PLL, un oscillatore controllato in tensione (VCO) viene accoppiato a un segnale di ingresso in modo da seguire la frequenza tramite un anello di aggancio di fase. Se la frequenza del segnale di ingresso cambia (modulazione FM), la tensione di controllo del VCO segue la modulazione FM. Questa tensione di controllo corrisponde quindi esattamente alla modulazione del segnale FM e quindi all'AF modulata e può essere prelevata dalla PLL per ulteriori elaborazioni.

[question:AD505]

Per demodulare segnali SSB si utilizza un cosiddetto demodulatore di prodotto. Questo è essenzialmente un mixer ad anello che utilizza l'IF del ricevitore e un BFO (Beat Frequency Oscillator) come segnali di ingresso. Dalla miscelazione (prodotto) di questi due segnali di ingresso, uno dei prodotti di miscelazione è il segnale AF desiderato (segnale SSB), che può essere prelevato all'uscita per ulteriori elaborazioni. Per la migliore comprensibilità possibile dell'AF demodulata, il BFO deve essere sintonizzato sulla frequenza della portante soppressa del segnale SSB.

[question:AD506]