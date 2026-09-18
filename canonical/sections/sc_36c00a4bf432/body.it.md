A differenza della modulazione, che avviene sul lato trasmettitore, la demodulazione dei segnali nel ricevitore consente di convertire un segnale modulato, ad esempio, nuovamente in BF rendendolo udibile o generando una sequenza di bit in una trasmissione digitale.

A seconda del tipo di modulazione utilizzato sul lato trasmettitore, sul lato ricevitore deve essere eseguita una demodulazione corrispondente. Esistono diversi concetti di circuito che consentono la demodulazione. Come funziona la modulazione nel digitale verrà affrontato in un capitolo successivo. In questo capitolo ci concentreremo inizialmente sulla demodulazione dei segnali analogici.

La forma più semplice di demodulazione di un segnale ad alta frequenza è rappresentata dalla modulazione di ampiezza (AM).
I segnali AM possono essere demodulati mediante un cosiddetto demodulatore ad inviluppo, come mostrato nella figura [ref:demodulator_huellkurvendemodulator_am]. A tal fine, il segnale ad alta frequenza viene prima selezionato alla frequenza di ricezione desiderata, ad esempio mediante un circuito oscillante sintonizzato, e poi rettificato tramite un diodo. Un condensatore collegato dopo il diodo viene caricato al valore di picco istantaneo del segnale e scaricato contemporaneamente tramite una resistenza collegata in parallelo, con una costante di tempo appropriata. Questa costante di tempo è notevolmente superiore al periodo del segnale HF, ma notevolmente inferiore al periodo del segnale BF.

<margin>
[picture:141:demodulator_huellkurvendemodulator_am:Demodulatore ad inviluppo per la demodulazione dei segnali AM]
</margin>

[question:AD501]

Al terminale X nella figura [ref:demodulator_huellkurvendemodulator_am_2] viene visualizzata la tensione di picco rettificata del segnale HF, che tra i picchi del segnale HF diminuisce leggermente in base alla costante di tempo della resistenza collegata in parallelo al condensatore. L’inviluppo del segnale corrisponde quindi alla BF modulata, che, a causa della costante di tempo del condensatore, è sovrapposta a un segnale a dente di sega (frequenza portante) e corrisponde al segnale mostrato nella figura [ref:demodulator_huellkurvendemodulator_am_abbx]. Nelle successive fasi di elaborazione della BF (non mostrate), le residue componenti di questa frequenza portante vengono filtrate, in modo che rimanga il segnale BF puro come segnale di uscita (cfr. figura [ref:demodulator_huellkurvendemodulator_am_clean]).

<margin>
[picture:607:demodulator_huellkurvendemodulator_am_2:Demodulatore ad inviluppo per la demodulazione dei segnali AM con rappresentazione del segnale di ingresso IF che giunge all’ingresso del demodulatore]
[picture:146:demodulator_huellkurvendemodulator_am_abbx:Segnale demodulato al punto X del demodulatore ad inviluppo]
[picture:147:demodulator_huellkurvendemodulator_am_clean:Segnale filtrato all’uscita del demodulatore ad inviluppo]
</margin>

[question:AD502]

---
<margin>
[picture:841:demodulator_flankendiskriminator:Circuito oscillante utilizzato come discriminatore di pendenza]

[picture:149:demodulator_flankendiskriminator_schaltung:Discriminatore di pendenza FM]
</margin>

Un circuito molto simile al demodulatore ad inviluppo descritto in precedenza può essere utilizzato per la demodulazione dei segnali FM.
Partendo dalla frequenza intermedia nel ricevitore FM, come mostrato nella figura [ref:demodulator_flankendiskriminator], il segnale entra in un circuito oscillante che, con la sua frequenza di risonanza $f_\text{res}$, è sintonizzato leggermente al di sopra o al di sotto della frequenza IF $f_\text{IF}$. In questo modo, il segnale FM da demodulare si trova sul fianco del circuito oscillante e converte le variazioni di frequenza della FM in variazioni di ampiezza. Mediante il demodulatore AM successivo, il segnale FM ora convertito in un segnale AM viene quindi demodulato e reso udibile. Questo circuito, mostrato nella figura [ref:demodulator_flankendiskriminator_schaltung], viene chiamato discriminatore di pendenza.

[question:AD504]

---

I segnali modulati FM possono essere demodulati anche mediante una PLL (anello ad aggancio di fase) (cfr. figura [ref:demodulator_pll]). In una PLL, un oscillatore controllato in tensione (VCO) viene accoppiato tramite un anello ad aggancio di fase a un segnale di ingresso in modo da seguirne la frequenza. Se la frequenza del segnale di ingresso cambia (modulazione FM), la tensione di regolazione del VCO segue la modulazione FM. Questa tensione di regolazione corrisponde esattamente alla modulazione del segnale FM e quindi alla BF modulata, e può essere prelevata dalla PLL per un’ulteriore elaborazione.

<margin>
[picture:77:demodulator_pll:PLL per la demodulazione dei segnali FM]
</margin>

[question:AD505]

---

Per demodulare i segnali modulati SSB si utilizza un cosiddetto rivelatore a prodotto. Questo è essenzialmente un mixer ad anello, che abbiamo già conosciuto nel capitolo sul ricevitore, che utilizza come segnali di ingresso la IF del ricevitore e un BFO (oscillatore a battimento). Attraverso la miscelazione (prodotto) di questi due segnali di ingresso, uno dei prodotti di miscelazione risultanti è il segnale BF desiderato (segnale SSB), che può essere prelevato all’uscita per un’ulteriore elaborazione. Per una chiarezza ottimale della BF demodulata, il BFO deve essere sintonizzato sulla frequenza della portante soppressa del segnale SSB.


<indepth>
[picture:153:demodulator_produktdetektor:Rivelatore a prodotto per la demodulazione dei segnali SSB]
[picture:1125:a_produktdetektor_spannung:Esempio di tensioni al rivelatore a prodotto]

Per la demodulazione di un segnale SSB viene spesso utilizzato un cosiddetto *rivelatore a prodotto*. Questo può essere realizzato, ad esempio, come mixer ad anello. Come segnali di ingresso riceve il segnale SSB alla frequenza intermedia (IF) e il segnale di un *oscillatore a battimento (BFO)*.

Il funzionamento può essere spiegato in modo semplificato con un mixer a commutazione. Il segnale BFO commuta il mixer ad anello alternativamente tra due stati. In modo semplificato, il segnale BFO può quindi essere considerato come un segnale che alterna tra i valori $+1$ e $-1$, come mostrato nel grafico superiore della figura [ref:a_produktdetektor_spannung].

Il segnale IF viene quindi alternativamente trasmesso invariato o invertito in polarità. Nella rappresentazione semplificata, il segnale IF può quindi essere considerato come il prodotto tra il segnale BF e il segnale di commutazione del BFO:

$u_\mathrm{IF}(t)=u_\mathrm{BF}(t)\cdot s_\mathrm{BFO}(t)$

Nel rivelatore a prodotto, questo segnale viene nuovamente moltiplicato per il segnale BFO:

$u_\mathrm{IF}(t)\cdot s_\mathrm{BFO}(t)=u_\mathrm{BF}(t)\cdot s_\mathrm{BFO}(t)\cdot s_\mathrm{BFO}(t)$

Poiché il segnale semplificato di commutazione del BFO assume solo i valori $+1$ e $-1$, vale:

$s_\mathrm{BFO}^2(t)=1$

Pertanto, rimane come componente a bassa frequenza il segnale BF originale:

$u_\mathrm{BF}(t)=u_\mathrm{IF}(t)\cdot s_\mathrm{BFO}(t)$

Oltre al segnale BF desiderato, durante il processo di miscelazione vengono generati altri prodotti di miscelazione ad alta frequenza. Questi vengono soppressi all’uscita del rivelatore a prodotto da un filtro passa-basso.

Affinché il segnale BF originale venga recuperato con l’altezza tonale corretta, la frequenza del BFO deve essere regolata in modo appropriato alla frequenza della portante soppressa del segnale SSB.
</indepth>

[question:AD506]