Abbiamo imparato che nella modulazione di ampiezza, oltre alla portante, si generano due bande laterali, una inferiore (LSB) e una superiore (USB), nelle quali è contenuta tutta l'informazione del segnale di modulazione, mentre la portante stessa non trasmette alcuna informazione. Poiché entrambe le bande laterali contengono la stessa informazione, è sufficiente trasmetterne solo una e sopprimere la portante (cfr. figura [ref:e_ssb_am_modulation]). Questa procedura è chiamata modulazione a banda laterale singola, o Single Sideband (SSB). Il vantaggio della SSB è che non si spreca potenza di trasmissione per la portante e la seconda banda laterale, consentendo di utilizzare tutta la potenza in modo efficiente per la trasmissione dell'informazione e riducendo al contempo la larghezza di banda necessaria rispetto alla AM.


Nella modulazione a banda laterale singola (SSB), il segnale trasmesso contiene – a seconda della banda laterale scelta sul trasmettitore-ricevitore – o la frequenza portante più la frequenza di modulazione NF (per USB) o la frequenza portante meno la frequenza di modulazione NF (per LSB). La figura [ref:e_ssb_einzelsignal] mostra due esempi a riguardo: se si modula un trasmettitore con la frequenza portante di $\qty{7,100}{\mega\hertz}$ con un segnale NF di $\qty{1}{\kilo\hertz}$ in USB, il trasmettitore irradierà una frequenza di $\qty{7,100}{\mega\hertz} + \qty{1}{\kilo\hertz} = \qty{7,101}{\mega\hertz}$. Se invece si modula il trasmettitore in LSB, il trasmettitore irradierà una frequenza di $\qty{7,100}{\mega\hertz} -\qty{1}{\kilo\hertz} = \qty{7,099}{\mega\hertz}$.

<margin>
[picture:1056:e_ssb_einzelsignal:Bande laterali in AM e SSB]
</margin>

Le seguenti domande possono essere risolte secondo questo schema.

[question:EE203]
[question:EE204]

---

I segnali AM trasmettono entrambe le bande laterali e la portante e hanno quindi una larghezza di banda di poco superiore al doppio del segnale NF modulante (cfr. figura [ref:e_ssb_einzelsignal]). La larghezza di banda di un segnale SSB corrisponde approssimativamente alla larghezza di banda del segnale NF modulante (dopo filtraggio e limitazione della larghezza di banda del segnale NF). Con SSB, anche le componenti del segnale al di sotto di $\qty{300}{\hertz}$ e la portante ($\qty{0}{\hertz}$) non vengono trasmesse e vengono soppresse. Pertanto, SSB ha una larghezza di banda leggermente inferiore alla metà di quella AM.

<margin>
[picture:743:e_ssb_einzelsignal:Bande laterali in AM e SSB]
</margin>

[question:EE202]
[question:EE201]

---

Come abbiamo già imparato nella classe N sull'argomento telegrafia Morse con *Continuous Wave* (CW), un'alta frequenza portante costante viene accesa e spenta secondo un ritmo specifico. I segnali CW richiedono, rispetto ai segnali modulati vocalmente come AM e SSB, la minore larghezza di banda. Ciò è dovuto al fatto che con CW viene semplicemente tastata un'unica frequenza e non, come con i segnali vocali, devono essere trasmesse contemporaneamente più componenti di frequenza di un segnale NF.

<indepth>
La larghezza di banda dei segnali CW dipende dalla velocità dei caratteri (velocità di tastatura) e ammonta a circa $\qty{300}{\hertz}$ a velocità medie di trasmissione di 20 parole al minuto (100 caratteri al minuto).
</indepth>

[question:EE207]

Per evitare disturbi alle stazioni adiacenti nella banda di frequenza, la larghezza di banda occupata da un segnale SSB dovrebbe essere limitata a un massimo di circa $\qty{2,7}{\kilo\hertz}$. Questa larghezza di banda è completamente sufficiente per una buona intelligibilità vocale. Per questo motivo, il segnale NF del microfono nel trasmettitore viene limitato in banda: le componenti di frequenza al di sotto di circa $\qty{300}{\hertz}$ e al di sopra di circa $\qty{3}{\kilo\hertz}$ vengono soppresse, poiché contribuiscono poco all'intelligibilità vocale.

[question:EJ211]
[question:EJ210]

In pratica, i filtri SSB per la generazione di un segnale SSB hanno spesso una larghezza di banda di soli circa $\qty{2,4}{\kilo\hertz}$. Anche questa minore larghezza di banda è sufficiente in molti casi per una buona intelligibilità vocale e consente al contempo un utilizzo ancora più efficiente dello spettro di frequenza disponibile.

[question:EF310]

Disturbi alle stazioni adiacenti possono anche verificarsi a causa del cosiddetto *splatter*, che può essere causato da un'amplificazione del microfono impostata troppo alta e quindi da una sovraeccitazione degli stadi NF. Nel segnale trasmesso, ciò si manifesta con un aumento della larghezza di banda della trasmissione SSB, che può disturbare altre stazioni.

[question:EJ215]

Un'amplificazione del microfono troppo bassa (ampiezza NF) porta a una minore modulazione del trasmettitore SSB, con conseguente riduzione della potenza d’uscita. Pertanto, è importante che l'amplificazione del microfono sia adattata in modo ottimale per una buona comunicazione in SSB (né troppo alta né troppo bassa). Nel capitolo sul compressore dinamico torneremo più in dettaglio su questo aspetto. 

[question:EE206]
[question:EE205]
