Quando si collegano le antenne, l'obiettivo è che solo l'antenna emetta o riceva segnali, e non la linea di alimentazione stessa, che potrebbe essere posata all'interno dell'edificio. A questo scopo sono adatti cavi schermati, ad esempio cavi coassiali, poiché in condizioni ideali non emettono né ricevono onde elettromagnetiche, ma trasmettono il segnale in modo schermato dall'esterno (ad esempio dall'impianto elettrico dell'edificio) attraverso il cavo.

<indepth>
Affinché la schermatura di un cavo coassiale svolga la funzione desiderata, deve essere soddisfatta una *condizione*: la corrente nel conduttore interno deve essere esattamente opposta a quella nel conduttore esterno e entrambe le correnti devono avere lo stesso valore assoluto. In questo caso, si genera un campo solo tra i due conduttori e l'ambiente circostante il cavo non viene influenzato. Il conduttore esterno non presenta quindi alcuna tensione ad alta frequenza rispetto a terra.

Viceversa, questo significa anche: se il conduttore esterno presenta una tensione ad alta frequenza rispetto a terra, allora le correnti nel conduttore interno non sono simmetriche e il cavo coassiale irradia.

Le correnti nel cavo coassiale devono quindi essere simmetriche (stesso valore assoluto ma segno opposto o direzione opposta) e le tensioni rispetto a terra devono essere *asimmetriche* (solo il conduttore interno presenta tensione rispetto a terra).
</indepth>

---

Se si collega tuttavia un'antenna simmetrica, ad esempio un dipolo a semionda, a un cavo coassiale, può comunque verificarsi che il cavo coassiale, nonostante la schermatura, irradia! Questo accade perché sulla superficie esterna del conduttore metallico esterno possono scorrere correnti ad alta frequenza, accompagnate da un campo elettromagnetico intorno all'isolante esterno (cfr. figura [ref:e_mantelwellen]). Questo effetto viene definito *correnti sulla calza*, che possono disturbare altri apparecchi nell'edificio sia in trasmissione che in ricezione, poiché il cavo coassiale diventa in parte parte dell'antenna e può quindi captare più facilmente influenze disturbanti all'interno dell'edificio. Le correnti aggiuntive sulla calza "mancano" poi su uno dei due bracci del dipolo, causando inoltre una deformazione del diagramma di radiazione.

[question:EG405]
[question:EG406]

La figura [ref:e_mantelwellen] mostra chiaramente come parte della corrente, che in realtà dovrebbe fluire nel braccio del dipolo, ritorni sulla calza del cavo coassiale.

<margin>
[picture:633:e_mantelwellen:Correnti sulla calza]
</margin>

Le correnti sulla calza scorrono effettivamente in gran parte sulla superficie del conduttore esterno. Questo è dovuto all'effetto *pelle*, che fa sì che le correnti ad alta frequenza scorrano prevalentemente sulla superficie dei conduttori metallici. Pertanto, un cavo coassiale può essere considerato come un sistema a tre conduttori:
  
1. Superficie esterna del conduttore interno
2. Superficie interna del conduttore esterno
3. Superficie esterna del conduttore esterno
  
La corrente sulla superficie esterna del conduttore interno e quella sulla superficie interna del conduttore esterno hanno sempre lo stesso valore assoluto e sono opposte ($I_1$). La corrente sulla superficie esterna del conduttore esterno ($I_3$) rappresenta la corrente sulla calza.

[question:EG404]

---

Le correnti sulla calza possono essere evitate, ad esempio, utilizzando un cosiddetto *elemento di simmetrizzazione*, un balun, per collegare il cavo coassiale all'antenna.

<indepth>
Il termine *balun* è composto dalle parole inglesi "balanced" e "unbalanced", poiché si vuole collegare un lato simmetrico (ad esempio un'antenna simmetrica) a un lato asimmetrico (il cavo coassiale, in cui idealmente solo il conduttore interno presenta tensione rispetto a terra).
</indepth>

[question:EG407]

---

Un'altra variante costruttiva per un balun consiste nell'avvolgere un cavo coassiale intorno a un nucleo di ferrite. Questo rappresenta una cosiddetta *induttanza di modo comune*, che viene anche chiamata *induttanza di modo comune*. Per i segnali in controfase, essa presenta una bassa impedenza, poiché, quando la corrente nel conduttore interno è opposta a quella nel conduttore esterno, non si verifica un'interazione significativa con il materiale del nucleo di ferrite. Per le correnti sulla calza, invece, questa struttura funziona come una bobina (con perdite).

<margin>
[photo:325:e_mantelwellendrossel:Induttanza di modo comune]
</margin>

[question:EG408]