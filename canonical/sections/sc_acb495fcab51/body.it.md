La *MUF* (*maximum usable frequency*), ovvero la frequenza più alta che la ionosfera può ancora rifrangere per la distanza tra trasmettitore e ricevitore, l'abbiamo già conosciuta nel corso HB3 nella sezione [sec:muf_luf_1]. Lì è stato chiarito che la MUF dipende dalla densità degli elettroni liberi nella regione rifrangente. Ora, nel corso HB9, esamineremo questo argomento più in dettaglio, in particolare per quanto riguarda l'angolo di irradiazione.

[question:AH206]
[question:AH207]

Come già sappiamo, la portata delle onde spaziali dipende dall'angolo di irradiazione. Più piatta è l'onda che incide sulla ionosfera, più facile è la rifrazione. Questa relazione vale anche per la MUF: la frequenza appena rifratta, la *MUF*, è tanto più alta quanto più piatto è il nostro segnale che entra nella ionosfera. La figura [ref:e_muf_winkel2] mostra una simulazione della distanza di salto per una giornata estiva del 2024 per un segnale radioamatoriale intorno ai $\qty{7}{\mega\hertz}$. A $\qty{45}{\degree}$ la MUF in quel giorno era di $\qty{7,5}{\mega\hertz}$. Se si cambia l'angolo di irradiazione, cambia anche la MUF: se si irradia più verticalmente (ad esempio $\qty{60}{\degree}$), la MUF diminuisce e l'onda radio non viene più rifratta. Se invece si irradia più piattamente (ad esempio $\qty{30}{\degree}$), la MUF aumenta. Di seguito esamineremo questa relazione più in dettaglio.

<margin>
[picture:998:e_muf_winkel2:Distanza di salto a 7 MHz nell'estate 2024]
</margin>

%<wordorigin>
%L'abbreviazione *FOT* può essere facilmente ricordata così: *F*réquence *O*ptimale de *T*rafic o "Frequency %Optimum Traffic".
%La FOT è standardmente all'85% della MUF (Maximum Usable Frequency).
%</wordorigin>
% Rimossa di nuovo perché ridondante.

---

Le stazioni di misurazione ionosferiche misurano la cosiddetta frequenza critica $f_\text{c}$ (o spesso anche $f_\text{k}$, $f_\text{krit}$ o $f_\text{oF2}$). Questa è la frequenza più alta alla quale l'onda spaziale che entra perpendicolarmente nella ionosfera viene ancora riflessa (cfr. figura [ref:e_muf_winkel]). Quando irradiamo verticalmente verso l'alto, cioè il nostro segnale entra nella ionosfera con un angolo di $\qty{90}{\degree}$, la MUF è la più piccola, perché il nostro segnale deve allora "invertire" completamente nella ionosfera, cioè compiere una svolta di 180°. Ciò significa che a $\qty{90}{\degree}$ vale $f_\text{c} = MUF$.

<indepth>
Come simbolo si usa $f_o$ (lettera "o" minuscola in pedice per *ordinary wave*) seguita dalla regione ionosferica per cui vale questa frequenza, ad esempio $f_\text{oF2}$ per la regione F2. Tuttavia, spesso vengono usati anche $f_\text{c}$, $f_\text{k}$ o $f_\text{krit}$ come simboli.
</indepth>

<margin>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
</margin>

<indepth>
La frequenza critica è quindi la frequenza più alta che ritorna dalla ionosfera quando si irradia verticalmente verso l'alto. Una regola empirica dice che la frequenza più alta che viene ancora riflessa con un'incidenza *piatta* è circa il triplo della frequenza critica.
</indepth>

[question:AH204]
[question:AH205]

---

La figura [ref:e_muf_fof2] mostra l'andamento temporale di MUF e $f_\text{c}$ l'08.09.2025, misurato con l'ionosonda di Juliusruh. MUF $\qty{3000}{\kilo\meter}$ significa in questo caso che si irradia molto piattamente per raggiungere una distanza di salto di $\qty{3000}{\kilo\meter}$.

<margin>
[picture:999:e_muf_fof2:MUF e $f_\text{c}$ l'08.09.2025]
</margin>

Per altri angoli di irradiazione, la MUF può essere determinata approssimativamente dalla $f_\text{c}$ utilizzando la seguente formula dalla raccolta di formule (vale per $\alpha > \qty{40}{\degree}$):

$MUF \approx \frac{f_\text{c}}{sin(\alpha)}$

dove $\alpha$ indica l'angolo di irradiazione (cfr. figura [ref:e_muf_winkel]). Osservando più da vicino la formula, si riconosce che la MUF è sempre più alta della frequenza critica – e tanto più quanto più piatta irradia l'antenna trasmittente o riceve l'antenna ricevente.

[question:AH208]

---

Per la pianificazione delle frequenze commerciali, dove è importante che un collegamento radio abbia un'alta probabilità di successo, esiste inoltre il concetto di *FOT* (*frequency of optimal transmission*, frequenza ottimale di trasmissione), o anche $f_\text{opt}$. Questa è la frequenza che su un determinato percorso di segnale consente statisticamente un collegamento radio il 90% di tutti i giorni; di solito si trova il 15% al di sotto della media mensile della MUF. Nella raccolta di formule troviamo questa relazione come

$f_\text{OPT} = MUF \cdot 0,85$

Con queste informazioni possiamo ora risolvere il seguente esercizio; una calcolatrice è utile in questo caso.

[question:AH209]

<indepth>
Per i collegamenti DX in radioamatoriale, la $f_\text{opt}$ non ha alcun ruolo, perché lì si sceglie in genere la banda di frequenza più alta che consente ancora un collegamento (cioè quella più vicina alla MUF), poiché lì ci si aspetta il rumore di fondo più basso e quindi il segnale migliore (rapporto segnale/rumore SNR più alto).
</indepth>

Nella classe E abbiamo già conosciuto la LUF (Lowest Usable Frequency). È determinata dallo strato D e indica la frequenza utilizzabile più bassa al di sotto della quale l'attenuazione è troppo forte. Lo strato D *attenua* infatti il nostro segnale radio e per ogni salto questo segnale deve anche passare *due* volte attraverso questo strato D. Allo stesso tempo, questa attenuazione è tanto maggiore quanto più bassa è la frequenza (la relazione è quadratica: se si dimezza la frequenza, l'attenuazione quadruplica). Pertanto, se si continua a diminuire la frequenza, si arriverà anche a un punto in cui il segnale rifratto non è più utilizzabile; questa è la LUF.

[question:AH210]
[question:AH211]
