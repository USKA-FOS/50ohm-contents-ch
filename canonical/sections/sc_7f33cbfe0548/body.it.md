Ora esaminiamo più da vicino il processo di campionamento e ricordiamo l'esempio menzionato nella sezione [sec:digitale_signalverarbeitung_einleitung] della fotocamera che scatta immagini di una scena a intervalli specifici. Supponiamo, ad esempio, che la nostra fotocamera scatti 24 immagini al secondo di una determinata scena. Se immaginiamo, ad esempio, di filmare un corridore mentre corre, noteremo che tra un'immagine e l'altra c'è sempre un movimento a scatti delle gambe e del corpo del nostro corridore rispetto all'immagine precedente. Se facciamo scorrere le immagini rapidamente una dopo l'altra nel tempo, si crea una sequenza di movimento otticamente continua. Tuttavia, l'informazione che acquisiamo con 24 immagini al secondo è limitata nel tempo (nota: tempo discreto). Cosa succederebbe se tra 2 immagini consecutive una mosca passasse rapidamente davanti all'obiettivo della nostra fotocamera? Potremmo ancora percepirla? Dipende dal fatto che la mosca scelga il momento giusto tra due immagini per il suo passaggio. Se entrasse nel campo visivo della fotocamera solo dopo aver scattato un'immagine e lo lasciasse prima di scattare l'immagine successiva, non potremmo ricostruire questo evento nelle immagini che abbiamo scattato. Ci rimarrebbe nascosta dell'informazione.

<webonly>
<margin>
[include:applet_nyquist]
</margin>
</webonly>

Lo stesso vale per il campionamento dei segnali analogici. Se questi vengono acquisiti (campionati) con una determinata frequenza di campionamento $f_\text{s}$, potremmo non essere più in grado di acquisire cambiamenti temporali rapidi del segnale tra 2 campioni. Il campionamento significa quindi sempre anche una perdita di informazione temporale. Ora ci si può chiedere quale risoluzione temporale sia necessaria per campionare un segnale analogico di una determinata frequenza (cambiamento dell'ampiezza del segnale al secondo) senza perdita di informazione (tutti i cambiamenti devono essere acquisiti). Per questo si può fare la seguente considerazione. Per poter acquisire almeno ogni cambiamento del segnale in modo accurato, si deve essere in grado di garantire (come nel nostro esempio precedente con la fotocamera) che venga prelevato almeno un campione prima e dopo ogni cambiamento del segnale. Nel caso della nostra mosca che vola attraverso l'immagine, la condizione sarebbe che la mosca possa volare attraverso l'immagine solo così lentamente da essere visibile in almeno 2 immagini. Altrimenti non si potrebbe dire da dove sia volata attraverso l'immagine e in quale direzione. Se questa condizione non è soddisfatta, ci sfugge questa informazione. In questo caso si dice anche che una ricostruzione senza errori non è possibile.

Si può dimostrare matematicamente che per acquisire un segnale con la frequenza massima presente $f_{\mathrm{max}}$, la frequenza di campionamento $f_\text{s}$ deve essere più del doppio, cioè un po' più di $f_\text{s} > 2 \cdot f_{\mathrm{max}}$, affinché possiamo ricostruire il nostro segnale in modo accurato. Questa scoperta nella elaborazione numerica dei segnali è chiamata teorema di campionamento ed è nota anche come teorema di campionamento di Nyquist-Shannon o condizione di Nyquist, dai suoi scopritori Nyquist e Shannon. Il teorema di campionamento determina quindi la frequenza di campionamento minima $f_\text{s}$ teoricamente necessaria per una ricostruzione senza errori di un segnale.

[question:AF618]

[question:AF616]

---

Se il teorema non è soddisfatto, si verificano i cosiddetti effetti di alias, o effetti di aliasing.

[question:AF617]

<webonly>
L'applet accanto consente di sperimentare con la frequenza di campionamento. Se la frequenza di campionamento scende sotto $\qty{2}{\kilo\hertz}$, la condizione di Nyquist non è più soddisfatta e il segnale non può più essere ricostruito in modo univoco.
È interessante notare che anche con una frequenza di campionamento esattamente di $\qty{2}{\kilo\hertz}$ la ricostruzione non funziona in modo affidabile. Pertanto, di solito si sceglie una frequenza di campionamento leggermente superiore alla frequenza di Nyquist per garantire una ricostruzione sicura del segnale.
</webonly>

<indepth>
Prendiamo un esempio pratico come nel caso di un lettore CD, che funziona con una frequenza di campionamento di, ad esempio, $\qty{44,1}{\kilo\sps}$. Se si assume il teorema di campionamento come descritto sopra, ciò significa che con una frequenza di campionamento di $\qty{44,1}{\kilo\sps}$ possono essere rappresentate solo frequenze inferiori a $\qty{22,05}{\kilo\hertz}$. Pertanto, le frequenze fino a circa $\qty{22}{\kilo\hertz}$ possono ancora essere rappresentate correttamente. Ciò corrisponde alla banda di frequenza HiFi di buoni impianti stereo.
</indepth>

Con il seguente esercizio puoi testare la tua conoscenza del teorema di campionamento.

[question:AF619]
