Gli apparecchi radio a volte devono essere ricalibrati, ad esempio dopo riparazioni o se i componenti si sono modificati a causa dell'invecchiamento. Per i ricevitori, la calibrazione include il controllo delle frequenze dell’oscillatore. A tale scopo si utilizza solitamente un frequenzimetro.

[question:EI501]

La figura [ref:e_frequenzzaehler1] mostra il display di un frequenzimetro. La cifra tre separata a destra, come su alcune calcolatrici, sta per $\num{10^3}$. Quindi il misuratore misura la frequenza $\qty{455}\cdot \qty{10^3}{\hertz}$ o $\qty{455}{\kilo\hertz}$. Strumenti di misura più recenti visualizzano direttamente il prefisso dell'unità invece della potenza di dieci.

<margin>
[photo:187:e_frequenzzaehler1:Display di un frequenzimetro che mostra $\qty{455}\cdot \qty{10^3}{\hertz}$]
</margin>

% Ich hab das mal aus Platzgründen entfernt
%<margin> 
%[photo:189:e_frequenzzaehler2:Multimetro che mostra $\qty{455}{\kilo\hertz}$ nel campo di misura della frequenza. Sopra appaiono un simbolo di bassa tensione della batteria, l'umidità e la temperatura. Questi valori non hanno nulla a che fare con la misura della frequenza.]
%</margin>

<indepth>
La frequenza di $\qty{455}{\kilo\hertz}$ si trova frequentemente come frequenza intermedia nei ricevitori supereterodina e può essere misurata quando il ricevitore è sintonizzato su un segnale forte.
</indepth>

---

Nelle istruzioni di calibrazione viene spesso richiesto di impostare una frequenza con una certa deviazione, ad esempio $\pm\qty{10}{\hertz}$. In questi casi, è utile tenere presente il valore posizionale delle singole cifre. La potenza di dieci visualizzata dallo strumento di misura, cioè nel caso di $\qty{455}{\kilo\hertz}$ il valore $\num{10^3}$ o $\num{1000}$, si riferisce sempre alla posizione immediatamente prima della virgola. La posizione a sinistra di essa indica quindi $\qty{10}{\kilo\hertz}$ o $\qty{10^4}{\hertz}$, e la posizione ancora più a sinistra, nell'esempio il quattro, $\qty{100}{\kilo\hertz}$ o $\qty{10^5}{\hertz}$. A destra si procede nell'altra direzione.

 Nella figura [ref:e_frequenzzaehler_stellen] vediamo un esempio con una frequenza più alta.
  
<margin>
[picture:793:e_frequenzzaehler_stellen:Questa visualizzazione rappresenta una frequenza in $\unit{\mega\hertz}$. Questo è anche il valore posizionale della cifra prima della virgola.]
</margin>

<attention>
Gli ingressi dei frequenzimetri possono avere un’alta resistenza interna. Questo lo conosciamo dai misuratori di tensione e dagli oscilloscopi. Tuttavia, esistono anche connessioni da $\qty{50}{\ohm}$. Di solito sono particolarmente sensibili e il valore massimo di tensione o potenza indicato nel manuale d'uso del misuratore non deve assolutamente essere superato.
</attention>

[question:EI502]
[question:EI503]

I frequenzimetri sono costruiti per un determinato intervallo di valori, ad esempio da $\qty{100}{\kilo\hertz}$ a $\qty{2}{\giga\hertz}$. Al di fuori di questo intervallo, misurano in modo impreciso o per nulla. Per misurare frequenze più elevate esistono i divisori di frequenza. Essi dividono la frequenza di un segnale applicato al loro ingresso per un valore fisso ed emettono il risultato come oscillazione elettrica in uscita. Vengono anche chiamati pre-divideri, perché vengono collegati tra l'oggetto di misura e il frequenzimetro.

%TODO Bild Frequenzteiler

Spesso i pre-divideri dividono la frequenza per dieci. Se si applica $\qty{2,4}{\giga\hertz}$ all'ingresso di un tale divisore 10:1, il frequenzimetro collegato dopo visualizzerà $\qty{240}{\mega\hertz}$.

[question:EI504]