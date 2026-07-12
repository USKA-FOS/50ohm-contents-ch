Analizziamo ora più da vicino il processo di campionamento e ricordiamo l'esempio precedente della fotocamera che scatta immagini di una scena a intervalli specifici. Supponiamo, ad esempio, che la nostra fotocamera scatti 24 immagini al secondo di una determinata scena. Se immaginiamo di filmare un corridore mentre corre, noteremo che tra un'immagine e l'altra c'è sempre un movimento a scatti delle gambe e del corpo del nostro corridore rispetto all'immagine precedente. Se facciamo scorrere le immagini una dopo l'altra molto velocemente, si crea un movimento visivamente continuo. Tuttavia, le informazioni che catturiamo a 24 fotogrammi al secondo sono limitate nel tempo (ricorda: tempo discreto). Cosa succederebbe se, tra due immagini consecutive, una mosca volasse improvvisamente velocemente davanti all'obiettivo della nostra fotocamera? Sarebbe ancora possibile percepirlo? Dipende dal fatto che la mosca scelga il momento giusto tra due immagini per il suo passaggio. Se entrasse nell'inquadratura solo dopo che un'immagine è stata scattata e l'avesse già lasciata prima che venisse scattata l'immagine successiva, non potremmo ricostruire questo evento nelle immagini che abbiamo registrato. Ci sfuggirebbero informazioni.

<webonly>
<margin>
[include:applet_nyquist]
</margin>
</webonly>

Lo stesso vale per il campionamento dei segnali analogici. Se questi vengono acquisiti (campionati) con una determinata frequenza di campionamento $f_\text{s}$, potremmo non essere più in grado di catturare cambiamenti rapidi del segnale nel tempo tra 2 campioni. Il campionamento comporta quindi sempre una perdita di informazioni temporali. Ora ci si può chiedere quale risoluzione temporale sia necessaria per campionare un segnale analogico di una determinata frequenza (cambiamento dell'ampiezza del segnale al secondo) senza perdita di informazioni (tutti i cambiamenti devono essere catturati). A tal fine, si può fare la seguente considerazione. Per poter catturare almeno ogni cambiamento del segnale in modo inequivocabile, è necessario (come nel nostro esempio precedente con la fotocamera) essere in grado di garantire che venga prelevato almeno un campione prima e dopo ogni cambiamento del segnale. Nel caso della nostra mosca che vola attraverso l'immagine, il presupposto sarebbe che la mosca possa volare attraverso l'immagine solo così velocemente da essere visibile in almeno 2 immagini. Altrimenti, non si potrebbe dire da dove è volata attraverso l'immagine e in quale direzione. Se questo presupposto non è soddisfatto, perdiamo queste informazioni. In questo caso si parla anche di impossibilità di una ricostruzione priva di errori.

Si può dimostrare matematicamente che per acquisire un segnale con la frequenza più alta presente $f_{\mathrm{max}}$, la frequenza di campionamento $f_\text{s}$ deve essere più del doppio, quindi poco più di $f_\text{s} > 2 \cdot f_{\mathrm{max}}$, affinché possiamo ricostruire il nostro segnale in modo inequivocabile. Questa intuizione è anche nota nell'elaborazione digitale dei segnali come teorema di campionamento e, secondo i suoi scopritori Nyquist e Shannon, come teorema di campionamento di Nyquist-Shannon o condizione di Nyquist. Il teorema di campionamento determina quindi la frequenza di campionamento minima teoricamente necessaria $f_\text{s}$ per una ricostruzione priva di errori di un segnale.

[question:AF618]

[question:AF616]

---

Se il teorema non viene soddisfatto, si verificano i cosiddetti effetti alias, o effetti di aliasing. 

[question:AF617]

<webonly>
L'applet a lato consente di sperimentare con la frequenza di campionamento. Se la frequenza di campionamento scende al di sotto di $\qty{2}{\kilo\hertz}$, la condizione di Nyquist non è più soddisfatta e il segnale non può più essere ricostruito in modo univoco.
È interessante notare che anche con una frequenza di campionamento di esattamente $\qty{2}{\kilo\hertz}$, la ricostruzione non funziona in modo affidabile. Pertanto, si sceglie solitamente una frequenza di campionamento leggermente superiore alla condizione di Nyquist per garantire una ricostruzione sicura del segnale.
</webonly>

<indepth>
Prendiamo un esempio pratico come nel caso di un lettore CD che opera con una frequenza di campionamento di, ad esempio, $\qty{44,1}{\kilo\sps}$. Se si applica il teorema di campionamento come descritto sopra, ciò significa che con una frequenza di campionamento di $\qty{44,1}{\kilo\sps}$ è possibile rappresentare solo frequenze inferiori a $\qty{22,05}{\kilo\hertz}$. Pertanto, le frequenze fino a circa $\qty{22}{\kilo\hertz}$ possono ancora essere rappresentate correttamente. Ciò corrisponde alla gamma di frequenza HiFi degli impianti stereo di buona qualità. 
</indepth>

Con il seguente esercizio puoi testare le tue conoscenze sul teorema di campionamento.

[question:AF619]
