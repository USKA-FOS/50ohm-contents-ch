Le apparecchiature radio devono essere talvolta ricalibrate, ad esempio dopo riparazioni o quando i componenti si sono alterati a causa dell'invecchiamento. Nei ricevitori, la calibrazione include il controllo delle frequenze dell'oscillatore. A questo scopo, di solito si utilizza un frequenzimetro.

[domanda:EI501]

La figura [rif:e_frequenzzaehler1] mostra il display di un frequenzimetro. La cifra tre staccata, posizionata più a destra, indica, come in alcune calcolatrici, $\num{10^3}$. Quindi il contatore misura la frequenza di $\qty{455}\cdot \qty{10^3}{\hertz}$ o $\qty{455}{\kilo\hertz}$. I dispositivi di misura più recenti mostrano direttamente il prefisso dell'unità invece della potenza di dieci.

<margin>
[foto:187:e_frequenzzaehler1:Display di un frequenzimetro che indica $\qty{455}\cdot \qty{10^3}{\hertz}$]
</margin>

% Ho rimosso questo per questioni di spazio
%<margin>
%[foto:189:e_frequenzzaehler2:Multimetro che mostra nel campo di misura della frequenza $\qty{455}{\kilo\hertz}$. Al di sopra sono visibili un simbolo per la bassa tensione della batteria, l'umidità dell'aria e la temperatura. Questi valori non hanno nulla a che fare con la misurazione della frequenza.
%</margin>

<indepth>
La frequenza di $\qty{455}{\kilo\hertz}$ è spesso utilizzata come frequenza intermedia nei ricevitori a conversione e può essere misurata quando il ricevitore è sintonizzato su un segnale forte.
</indepth>

---

Nelle istruzioni di calibrazione spesso si richiede di impostare una frequenza con una tolleranza specifica, ad esempio $\pm\qty{10}{\hertz}$. In questi casi, è utile conoscere il valore posizionale delle singole cifre. La potenza di dieci indicata dal dispositivo di misura, quindi in $\qty{455}{\kilo\hertz}$ il valore $\num{10^3}$ o $\num{1000}$, vale sempre per la cifra immediatamente prima della virgola. La cifra a sinistra di questa rappresenta $\qty{10}{\kilo\hertz}$ o $\qty{10^4}{\hertz}$, mentre quella ancora più a sinistra, nell'esempio il quattro, rappresenta $\qty{100}{\kilo\hertz}$ o $\qty{10^5}{\hertz}$. Verso destra, la logica è invertita.

Nella figura [rif:e_frequenzzaehler_stellen] vediamo un esempio con una frequenza più alta.

<margin>
[immagine:793:e_frequenzzaehler_stellen:Questo display mostra una frequenza in $\unit{\mega\hertz}$. Questo è anche il valore posizionale della cifra prima della virgola.]
</margin>

<attenzione>
Gli ingressi dei frequenzimetri possono avere un'elevata resistenza interna. Questo vale anche per i tester e gli oscilloscopi. Tuttavia, esistono anche connessioni con $\qty{50}{\ohm}$. Queste sono solitamente molto sensibili e il valore massimo di tensione o potenza indicato nel manuale del contatore non deve mai essere superato.
</attenzione>

[domanda:EI502]
[domanda:EI503]

I frequenzimetri sono progettati per un determinato intervallo di valori, ad esempio da $\qty{100}{\kilo\hertz}$ a $\qty{2}{\giga\hertz}$. Al di fuori di questo intervallo, le misurazioni sono inaccurate o addirittura impossibili. Per misurare frequenze più elevate, esistono divisori di frequenza. Questi dividono la frequenza di un segnale applicato al loro ingresso per un valore fisso e restituiscono il risultato come oscillazione elettrica in uscita. Vengono anche chiamati predivisori perché vengono collegati tra l'oggetto da misurare e il contatore.

%TODO Immagine divisore di frequenza

Spesso i predivisori dividono la frequenza per dieci. Se si applica all'ingresso di un divisore 10:1 una frequenza di $\qty{2,4}{\giga\hertz}$, il frequenzimetro successivo mostrerà $\qty{240}{\mega\hertz}$.

[domanda:EI504]