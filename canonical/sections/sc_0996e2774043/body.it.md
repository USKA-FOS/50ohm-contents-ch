Quando si collegano antenne, vogliamo assicurarci che solo l'antenna irradi o riceva segnali, ma non la linea di alimentazione stessa, che potrebbe essere posata all'interno della casa. A questo scopo sono adatti cavi schermati, ad es. cavi coassiali, poiché, in condizioni ideali, non irradiano né ricevono onde elettromagnetiche, ma conducono il segnale schermato dal mondo esterno (quindi, ad esempio, dall'impianto elettrico della casa) attraverso il cavo.

<indepth>
Affinché la schermatura di un cavo coassiale svolga la funzione desiderata, è necessario che sia soddisfatta una *condizione*: la corrente nel conduttore interno deve essere esattamente opposta alla corrente nel conduttore esterno e entrambe le correnti devono avere lo stesso valore. In questo caso, si genera un campo solo tra i due conduttori e l'ambiente circostante il cavo non viene influenzato. Il conduttore esterno non presenta quindi alcuna tensione ad alta frequenza rispetto alla terra.

Viceversa, ciò significa anche che se il conduttore esterno presenta una tensione ad alta frequenza rispetto alla terra, le correnti nel conduttore interno non sono simmetriche e il cavo coassiale irradia.

Le correnti nel cavo coassiale dovrebbero quindi essere simmetriche (stesso valore ma segno opposto o direzione opposta) e le tensioni rispetto alla terra dovrebbero essere *asimmetriche* (solo il conduttore interno porta tensione rispetto alla terra).
</indepth>

---

Tuttavia, se si collega un'antenna simmetrica, ad es. un Dipolo a semionda, a un cavo coassiale, può comunque accadere che il cavo coassiale irradi nonostante la schermatura! Ciò è dovuto al fatto che sulla superficie esterna del conduttore esterno metallico possono scorrere correnti ad alta frequenza, accompagnate da un campo elettromagnetico attorno all'isolamento esterno (cfr. figura [ref:e_mantelwellen]). Chiamiamo questo effetto *onde di mantello*, che possono sia disturbare altri apparecchi in casa durante la trasmissione, sia causare disturbi di ricezione, poiché il cavo coassiale diventa in parte parte dell'antenna e quindi gli influssi disturbanti in casa possono essere captati più facilmente dall'apparecchio radio. Le correnti di mantello aggiuntive "mancano" quindi su uno dei due bracci del dipolo, il che inoltre causa una deformazione della direttività.

[question:EG405]
[question:EG406]

La figura [ref:e_mantelwellen] illustra come una parte della corrente che dovrebbe effettivamente fluire nel braccio del dipolo, ritorni sullo schermo coassiale.

<margin>
[picture:633:e_mantelwellen:Mantelwellen]
</margin>

Le correnti di mantello scorrono effettivamente in gran parte sulla superficie del conduttore esterno. Ciò è legato al cosiddetto *effetto pelle*, che fa sì che le correnti ad alta frequenza scorrano in gran parte sulla superficie dei conduttori metallici. In questo senso, un cavo coassiale può anche essere considerato un sistema a tre conduttori:
  
1. Lato esterno del conduttore interno
2. Lato interno del conduttore esterno
3. Lato esterno del conduttore esterno
  
La corrente sul lato esterno del conduttore interno e la corrente sul lato interno del conduttore esterno hanno sempre lo stesso valore e sono dirette in modo opposto ($I_1$). La corrente sul lato esterno del conduttore esterno ($I_3$) rappresenta la corrente di mantello.

[question:EG404]

---

Le onde di mantello possono essere evitate, ad esempio, utilizzando un cosiddetto *elemento di simmetrizzazione*, un balun, per collegare il cavo coassiale e l'antenna.

<indepth>
La parola *Balun* è composta dalle parole inglesi "balanced" e "unbalanced", poiché deve essere collegato un lato simmetrico (ad es. un'antenna simmetrica) con un lato asimmetrico (il cavo coassiale, in cui idealmente solo il conduttore interno presenta una tensione rispetto alla terra).
</indepth>

[question:EG407]

---

Un'altra forma costruttiva per un balun consiste nell'avvolgere un cavo coassiale attorno a un nucleo di ferrite. Questo rappresenta una cosiddetta *bobina di blocco per correnti di mantello* ed è anche chiamato *soppressore di onde di mantello*. Per i segnali push-pull ha una bassa impedenza, poiché, quando nel conduttore interno scorre la corrente opposta a quella nel conduttore esterno, non vi è alcuna interazione degna di nota con il materiale di ferrite. Per le onde di mantello, tuttavia, la struttura agisce come una bobina (con perdite).

<margin>
[photo:325:e_mantelwellendrossel:Mantelwellensperre]
</margin>

[question:EG408]