L'alimentazione di un'antenna avviene sempre con una tensione e una corrente che sono tra loro in un determinato rapporto. Questo rapporto viene chiamato **resistenza di alimentazione**.

Affinché possa essere emessa una potenza, devono essere sempre presenti sia tensione che corrente, poiché la potenza è data dalla moltiplicazione di tensione e corrente. Se fosse nulla la tensione o la corrente, non ci sarebbe alcuna emissione o ricezione di potenza.

Tuttavia, parliamo di *antenne alimentate in corrente* e di *antenne alimentate in tensione*. Con ciò si intende che in alcune antenne è presente una corrente elevata con una tensione relativamente bassa al punto di alimentazione, mentre in altre antenne è presente una tensione elevata con una corrente relativamente bassa.


---

Nei **dipoli a semionda**, la resistenza di alimentazione dipende dal punto in cui avviene l'alimentazione. Questo perché nel dipolo le cariche oscillano avanti e indietro, muovendo un numero particolarmente elevato di cariche al centro, che chiamiamo **ventre di corrente**, e generando tensioni particolarmente elevate alle estremità, che chiamiamo **ventri di tensione**. Dove non si muovono cariche parliamo di **nodo di corrente**, e dove la tensione è nulla parliamo di **nodo di tensione**. La figura [ref:e_strom_spannung_speisung_dipol] mostra la distribuzione di corrente e tensione sul dipolo.

[question:EG203]

<margin>
[picture:787:e_strom_spannung_speisung_dipol:Dipolo a semionda con distribuzione di corrente e tensione]
</margin>

---

Se alimentiamo un dipolo a semionda al centro, devono essere mosse molte cariche e parliamo quindi di un'antenna alimentata in corrente (bassa resistenza di alimentazione). Un dipolo a semionda alimentato all'estremità è invece un'antenna alimentata in tensione (alta resistenza di alimentazione). Per l'alimentazione all'estremità, come mostrato nella figura [ref:e_strom_spannung_speisung_dipol_ende], è necessario un adattatore di impedenza. Questo verrà trattato in modo più approfondito solo nella parte HB9.

<margin>
[picture:851:e_strom_spannung_speisung_dipol_ende:Dipolo a semionda alimentato all'estremità]
</margin>

---

Le antenne alimentate in corrente presentano quindi una bassa resistenza, mentre quelle alimentate in tensione presentano un'alta resistenza.

Questo può essere ben illustrato con la legge di Ohm:

$ R = \frac{U}{I} $

Se si alimenta un dipolo al centro, lì si ha una tensione relativamente bassa con una corrente elevata. Il rapporto tra tensione e corrente è quindi piccolo e la resistenza risultante è bassa. Se invece l'alimentazione avviene all'estremità del dipolo, lì si ha una tensione elevata mentre la corrente tende a zero. Il rapporto diventa quindi molto grande e la resistenza risultante assume valori elevati.

Con resistenze basse parliamo anche di comportamento *a bassa impedenza* ($\downarrow\unit{\ohm}$) e con resistenze alte di comportamento *ad alta impedenza* ($\uparrow\unit{\ohm}$).

<indepth>
Un ordine di grandezza usuale per la *resistenza di alimentazione* di un'antenna alimentata in corrente è ad esempio $\qty{36}{\ohm}$ a $\qty{100}{\ohm}$, mentre per le antenne alimentate in tensione è $\qty{1500}{\ohm}$ a $\qty{4000}{\ohm}$.
</indepth>

---

<indepth>
La distribuzione di corrente su un dipolo dipende dalla frequenza alla quale l'antenna viene utilizzata. La figura [ref:e_stromverteilungen] mostra la distribuzione di corrente per multipli interi della frequenza fondamentale $f$ in un dipolo alimentato al centro. Si può osservare che per multipli pari della frequenza fondamentale si forma un nodo di corrente al punto di alimentazione. In questo caso la corrente è molto bassa, mentre la tensione è elevata, e l'antenna appare ad alta impedenza al punto di alimentazione. Per questo motivo un dipolo alimentato al centro è risonante solo per multipli dispari della frequenza fondamentale. È possibile utilizzare più bande spostando il punto di alimentazione, ad esempio in uno dei ventri di corrente come nella figura [ref:e_stromverteilungen]b (ad esempio nell'antenna Windom) o all'estremità dell'antenna (ad esempio EFHW o antenna Fuchs). In questi casi, tuttavia, sono necessari dispositivi di adattamento, che verranno trattati in modo più approfondito solo nella parte HB9.
  
[picture:1050:e_stromverteilungen:Distribuzioni di corrente a diverse frequenze fondamentali]
</indepth>

[question:EG204]
[question:EG205]
[question:EG206]
