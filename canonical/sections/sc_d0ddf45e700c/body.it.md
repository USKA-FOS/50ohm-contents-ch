Un metodo noto da decenni, ma che da qualche tempo trova un’applicazione sempre più diffusa nel radioamatoriale, è la *modulazione polare* [index:Polarmodulation].

Su questo argomento non ci sono domande d’esame. Tuttavia, la modulazione polare è un metodo affascinante che in futuro sarà impiegato sempre più spesso nei dispositivi radioamatoriali. Per questo motivo viene qui brevemente presentata, come uno sguardo oltre l’ordinario. Chi volesse concentrarsi esclusivamente sulla preparazione all’esame può tranquillamente saltare questo tema.

La modulazione polare si basa sull’osservazione di ciò che accade quando si ingrandisce temporalmente un segnale qualsiasi a banda relativamente stretta: il singolo treno d’onde appare come una sinusoide.

Questa sinusoide è definita da pochi parametri, ovvero frequenza, fase e ampiezza. Frequenza e fase sono tra loro correlate: se si parte da una frequenza fondamentale ma si sposta la fase di ogni treno d’onde sempre nella stessa direzione, si ottiene una frequenza diversa, spostata.

Da queste considerazioni deriva il metodo della *modulazione polare*. Con esso è possibile generare qualsiasi segnale a banda relativamente stretta, ad esempio segnali SSB. Per farlo, è sufficiente controllare contemporaneamente fase e ampiezza del segnale partendo da una frequenza fondamentale.

La figura [ref:polar_modulator] mostra lo *schema a blocchi* con cui questa idea viene generalmente implementata oggi. Qui, i due componenti del segnale $I(t)$ e $Q(t)$ (come descritti nel capitolo precedente) vengono convertiti nell’ampiezza istantanea $A(t)$ e nella fase istantanea $\varphi(t)$:

$A(t)=\sqrt{I^2(t)+Q^2(t)}$

$\varphi(t)=\operatorname{atan2}\left(Q(t),I(t)\right)$

L’informazione di fase $\varphi(t)$ modula poi una portante HF con ampiezza inizialmente costante. Il segnale risultante, ancora a ampiezza costante, contiene già tutte le informazioni di fase. Può essere amplificato da uno stadio finale particolarmente efficiente, ad esempio un amplificatore di classe E. In pratica, tali stadi finali raggiungono spesso rendimenti superiori all’$\qtyrange{80}{90}{\percent}$.

Ma come si introduce la modulazione di ampiezza? Per farlo, si manipola semplicemente la tensione di alimentazione dello stadio finale. Su di essa viene impressa l’informazione di ampiezza $A(t)$ tramite un amplificatore d’inviluppo. In questo modo, l’ampiezza d’uscita varia in base all’ampiezza necessaria in quel momento, ottenendo l’inviluppo desiderato. All’uscita si ottiene nuovamente il segnale completo, modulato sia in ampiezza che in fase:

$s(t)=A(t)\cos\left(\omega_\mathrm{T}t+\varphi(t)\right)$

Affinché il segnale rimanga il più possibile privo di distorsioni, i percorsi di ampiezza e fase devono essere perfettamente sincronizzati tra loro.

Per l’amplificatore d’inviluppo è sufficiente un amplificatore BF relativamente lento. La banda di frequenza che deve coprire dipende dalla larghezza di banda del segnale da generare. Per mantenere alto il rendimento, qui si impiega solitamente la tecnologia degli alimentatori a commutazione ("amplificatori BF di classe D").

Grazie all’elevato rendimento, poca potenza elettrica viene dissipata sotto forma di calore. Questo consente di risparmiare energia, ridurre la necessità di raffreddamento e ottenere apparecchi radio più piccoli e leggeri, privi di grandi dissipatori metallici e con transistor di stadio finale più economici. La modulazione polare è particolarmente adatta per apparecchi QRP a batteria, ma viene impiegata anche in trasceiver commerciali di elevate prestazioni.

<indepth>
Nel radioamatoriale, questo metodo è stato utilizzato negli anni ’70 con il nome "HELAPS" sul satellite AO-7. All’epoca tutto veniva realizzato con mezzi analogici. Oggi, gli amplificatori d’inviluppo e gli stadi finali sono ancora classicamente analogici, mentre il resto del lavoro è affidato ad algoritmi SDR. Le potenti CPU in grado di gestire agevolmente questi compiti oggi costano meno di una pizza.
</indepth>

<margin>
[picture:1117:polar_modulator:Modulatore polare]
</margin>