Analizziamo ora più nel dettaglio il processo di campionamento e ricordiamo l’esempio precedente della fotocamera che scatta immagini di una scena a intervalli regolari. Supponiamo, ad esempio, che la nostra fotocamera acquisisca 24 immagini al secondo di una scena specifica. Se pensiamo di filmare un corridore in movimento, noteremo che tra un’immagine e l’altra si verifica un movimento brusco delle gambe e del corpo del corridore rispetto all’immagine precedente. Se riproduciamo le immagini in rapida successione, otteniamo un movimento continuo dal punto di vista ottico. Tuttavia, le informazioni acquisite a 24 immagini al secondo sono limitate nel tempo (ricordiamo: tempo discreto). Cosa succederebbe se tra due immagini consecutive una mosca attraversasse rapidamente l’obiettivo della fotocamera? Potremmo percepirla? Dipende dal fatto che la mosca scelga il momento giusto tra due scatti per il suo passaggio. Se entrasse nell’inquadratura della fotocamera solo dopo aver scattato un’immagine e ne uscisse prima di quello successivo, non potremmo registrare questo evento nelle immagini acquisite. Ci sfuggirebbe un’informazione importante.

<webonly>
<margin>
[include:applet_nyquist]
</margin>
</webonly>

Lo stesso vale per il campionamento dei segnali analogici. Se questi vengono acquisiti (campionati) con una determinata frequenza di campionamento $f_\text{s}$, potremmo non riuscire a rilevare cambiamenti rapidi del segnale tra due campioni. Il campionamento comporta quindi sempre una perdita di informazioni temporali. A questo punto, possiamo chiederci quale risoluzione temporale sia necessaria per campionare un segnale analogico di una certa frequenza (variazione dell’ampiezza del segnale al secondo) senza perdere informazioni (tutte le variazioni devono essere rilevate). Per questo, possiamo fare la seguente considerazione. Per rilevare correttamente ogni variazione del segnale, come nel nostro esempio della fotocamera, dobbiamo assicurarci che almeno un campione venga acquisito prima e dopo ogni variazione. Nel caso della mosca che attraversa l’inquadratura, la condizione necessaria è che la mosca non attraversi l’inquadratura così velocemente da apparire solo in un’immagine. Altrimenti, non potremmo determinare da dove è entrata e in quale direzione si è mossa. Se questa condizione non è soddisfatta, perdiamo questa informazione. In questo caso si parla anche di impossibilità di una ricostruzione senza errori.

Si può dimostrare matematicamente che, per acquisire un segnale con la frequenza massima $f_{\mathrm{max}}$ presente, la frequenza di campionamento $f_\text{s}$ deve essere più del doppio, cioè $f_\text{s} > 2 \cdot f_{\mathrm{max}}$, affinché il segnale possa essere ricostruito correttamente. Questa conoscenza è nota nella elaborazione digitale dei segnali come teorema di campionamento e, in onore dei suoi scopritori Nyquist e Shannon, è anche chiamata teorema di Nyquist-Shannon o condizione di Nyquist. Il teorema di campionamento determina quindi la frequenza di campionamento minima teoricamente necessaria per una ricostruzione senza errori di un segnale.

[question:AF618]

[question:AF616]

---

Se il teorema non viene rispettato, si verificano i cosiddetti effetti di aliasing.

[question:AF617]

<webonly>
L’applet accanto consente di sperimentare con la frequenza di campionamento. Se la frequenza di campionamento scende sotto $\qty{2}{\kilo\hertz}$, la condizione di Nyquist non è più soddisfatta e il segnale non può più essere ricostruito in modo univoco.
È interessante notare che anche con una frequenza di campionamento esattamente pari a $\qty{2}{\kilo\hertz}$ la ricostruzione non funziona in modo affidabile. Pertanto, di solito si sceglie una frequenza di campionamento leggermente superiore alla condizione di Nyquist per garantire una ricostruzione sicura del segnale.
</webonly>

<indepth>
Prendiamo un esempio pratico, come nel caso di un lettore CD che lavora con una frequenza di campionamento di $\qty{44,1}{\kilo\sps}$. Se applichiamo il teorema di campionamento come descritto sopra, ciò significa che con una frequenza di campionamento di $\qty{44,1}{\kilo\sps}$ possono essere rappresentate correttamente solo frequenze inferiori a $\qty{22,05}{\kilo\hertz}$. Pertanto, frequenze fino a circa $\qty{22}{\kilo\hertz}$ possono essere rappresentate correttamente. Questo corrisponde alla gamma di frequenze HiFi di un buon impianto stereo.
</indepth>

Con il seguente esercizio puoi testare le tue conoscenze sul teorema di campionamento.

[question:AF619]
