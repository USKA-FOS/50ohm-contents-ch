Abbiamo imparato che nella modulazione di ampiezza, oltre alla portante, vengono generati due bande laterali, una inferiore (LSB) e una superiore (USB), che contengono tutte le informazioni del segnale di modulazione, mentre la portante stessa non trasmette alcuna informazione. Poiché entrambe le bande laterali contengono le stesse informazioni, è sufficiente trasmetterne solo una e sopprimere la portante (cfr. figura [ref:e_ssb_am_modulation]). Questo metodo viene chiamato modulazione a banda laterale unica o Single Sideband (SSB). Il vantaggio della SSB consiste nel fatto che non viene sprecata potenza di trasmissione per la portante e la seconda banda laterale, consentendo di utilizzare tutta la potenza in modo efficiente per la trasmissione delle informazioni e riducendo al contempo la larghezza di banda necessaria rispetto alla AM.


Nella modulazione a banda laterale unica (SSB), il segnale trasmesso – a seconda della banda laterale selezionata sul trasmettitore-ricevitore – contiene o la frequenza portante più la frequenza di modulazione BF (in USB) o la frequenza portante meno la frequenza di modulazione BF (in LSB). La figura [ref:e_ssb_einzelsignal] mostra due esempi: se si modula un trasmettitore con una frequenza portante di $\qty{7,100}{\mega\hertz}$ con un segnale BF di $\qty{1}{\kilo\hertz}$ in USB, il trasmettitore emette una frequenza di $\qty{7,100}{\mega\hertz} + \qty{1}{\kilo\hertz} = \qty{7,101}{\mega\hertz}$. Se invece si modula il trasmettitore in LSB, il trasmettitore emette una frequenza di $\qty{7,100}{\mega\hertz} - \qty{1}{\kilo\hertz} = \qty{7,099}{\mega\hertz}$.

<margin>
[picture:1056:e_ssb_einzelsignal:Bande laterali in AM e SSB]
</margin>

Le seguenti domande possono essere risolte secondo questo schema.

[question:EE203]
[question:EE204]

---

I segnali AM trasmettono entrambe le bande laterali e la portante e hanno quindi una larghezza di banda di poco più del doppio del segnale BF modulante (cfr. figura [ref:e_ssb_einzelsignal]). La larghezza di banda di un segnale SSB corrisponde circa alla larghezza di banda del segnale BF modulante (dopo il filtraggio e la limitazione della larghezza di banda del segnale BF). Nella SSB non vengono trasmessi e soppressi anche i componenti del segnale al di sotto di $\qty{300}{\hertz}$ e la portante ($\qty{0}{\hertz}$). Pertanto, la SSB ha una larghezza di banda inferiore a meno della metà rispetto alla AM.

<margin>
[picture:743:e_ssb_einzelsignal:Bande laterali in AM e SSB]
</margin>

[question:EE202]
[question:EE201]

---

Come abbiamo già imparato nella classe N durante il tema della telegrafia Morse con *Continuous Wave* (CW), in questo caso un segnale portante ad alta frequenza costante viene acceso e spento secondo un ritmo specifico. I segnali CW, rispetto ai segnali modulati con la voce come AM e SSB, richiedono la larghezza di banda minore. Questo perché nella CW viene manipolata una singola frequenza e non, come nei segnali vocali, devono essere trasmessi contemporaneamente più componenti di frequenza di un segnale BF.

<indepth>
La larghezza di banda dei segnali CW dipende dalla velocità di trasmissione (velocità di manipolazione) e, con velocità di trasmissione medie di 20 parole al minuto (100 caratteri al minuto), è di circa $\qty{300}{\hertz}$.
</indepth>

[question:EE207]

Per evitare interferenze con stazioni adiacenti nella banda di frequenza, la larghezza di banda occupata da un segnale SSB dovrebbe essere limitata a un massimo di circa $\qty{2,7}{\kilo\hertz}$. Questa larghezza di banda è più che sufficiente per una buona intelligibilità della voce. Per questo motivo, il segnale BF del microfono nel trasmettitore viene limitato in banda: i componenti di frequenza inferiori a circa $\qty{300}{\hertz}$ e superiori a circa $\qty{3}{\kilo\hertz}$ vengono soppressi, poiché contribuiscono poco all’intelligibilità della voce.

[question:EJ211]
[question:EJ210]

In pratica, i filtri SSB per la generazione di un segnale SSB hanno spesso una larghezza di banda di circa $\qty{2,4}{\kilo\hertz}$. Anche questa larghezza di banda ridotta è sufficiente in molti casi per una buona intelligibilità della voce e consente al contempo un utilizzo ancora più efficiente dello spettro di frequenza disponibile.

[question:EF310]

Le interferenze con stazioni adiacenti possono verificarsi anche a causa del cosiddetto *splatter*, che può essere causato da un’amplificazione del microfono troppo elevata e quindi da una sovraeccitazione degli stadi BF. Nel segnale trasmesso, questo si traduce in un aumento della larghezza di banda della trasmissione SSB, che può disturbare altre stazioni.

[question:EJ215]

Una troppo bassa amplificazione del microfono (ampiezza BF) porta a una modulazione inferiore del trasmettitore SSB, con conseguente riduzione della potenza d’uscita. Pertanto, è importante regolare in modo ottimale l’amplificazione del microfono per una buona comunicazione in SSB (non troppo alta e non troppo bassa). Nel capitolo Compressore di dinamica ne parleremo in modo più approfondito.

[question:EE206]
[question:EE205]