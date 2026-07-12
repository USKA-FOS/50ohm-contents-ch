La *MUF* (*maximum usable frequency*), ovvero la frequenza massima che la ionosfera può ancora rifrangere per la distanza tra trasmettitore e ricevitore, l'abbiamo già conosciuta nella classe E. Lì è diventato chiaro che la MUF dipende dalla densità degli elettroni liberi nella regione rifrangente. Nella classe A, esamineremo questo argomento in modo ancora più dettagliato, in particolare per quanto riguarda l'angolo di emissione.

[question:AH206]
[question:AH207]

Come sappiamo anche, la portata delle onde spaziali dipende dall'angolo di emissione. Più piatta è l'incidenza dell'onda sulla ionosfera, più facile è la rifrazione. Questa relazione vale anche per la MUF: la frequenza appena rifratta, la *MUF*, è tanto più alta quanto più piatto è l'angolo di incidenza del nostro segnale sulla ionosfera. La figura [ref:e_muf_winkel2] mostra una simulazione della distanza di salto per un giorno d'estate del 2024 per un segnale radioamatoriale intorno ai $\qty{7}{\mega\hertz}$. A $\qty{45}{\degree}$ la MUF in quel giorno era di $\qty{7,5}{\mega\hertz}$. Se si cambia l'angolo di emissione, cambia anche la MUF: se si emette con un angolo più ripido (ad es. $\qty{60}{\degree}$), la MUF diminuisce e l'onda radio non viene più rifratta. Se invece si emette con un angolo più piatto (ad es. $\qty{30}{\degree}$), la MUF aumenta. Di seguito esamineremo più da vicino questa relazione.

<margin>
[picture:998:e_muf_winkel2:Distanza di salto a 7 MHz nell'estate 2024]
</margin>

---

Dalle stazioni di misurazione ionosferica viene misurata la cosiddetta frequenza critica $f_\text{c}$ (o spesso anche $f_\text{k}$, $f_\text{krit}$ o $f_\text{oF2}$). Questa è la frequenza più alta alla quale l'onda spaziale che entra perpendicolarmente nella ionosfera viene ancora riflessa (cfr. figura [ref:e_muf_winkel]). Se trasmettiamo perpendicolarmente verso l'alto, cioè il nostro segnale incide sulla ionosfera con un angolo di $\qty{90}{\degree}$, la MUF è minima, poiché il nostro segnale deve "invertirsi" completamente nella ionosfera, cioè compiere una svolta di 180°. Ciò significa che a $\qty{90}{\degree}$ vale $f_\text{c} = MUF$.

<indepth>
Come simbolo di formula si usa $f_o$ (piccola lettera "O" in pedice per *ordinary wave*) seguita dalla regione ionosferica per cui vale questa frequenza, quindi ad es. $f_\text{oF2}$ per la regione F2. Tuttavia, si usano spesso anche $f_\text{c}$, $f_\text{k}$ o $f_\text{krit}$ come simboli di formula.
</indepth>

<margin>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
</margin>

<indepth>
La frequenza critica è quindi la frequenza più alta che ritorna dalla ionosfera quando si trasmette perpendicolarmente verso l'alto. Una regola empirica dice che la frequenza più alta che viene ancora riflessa con un'incidenza *piatta* è circa il triplo della frequenza critica.
</indepth>

[question:AH204]
[question:AH205]

---

La figura [ref:e_muf_fof2] mostra l'andamento temporale di MUF e $f_\text{c}$ il 08.09.2025, misurato con la ionosonda a Juliusruh. MUF $\qty{3000}{\kilo\meter}$ significa in questo caso che l'emissione è molto piatta per raggiungere una distanza di salto di $\qty{3000}{\kilo\meter}$.

<margin>
[picture:999:e_muf_fof2:MUF e $f_\text{c}$ il 08.09.2025]
</margin>

Per altri angoli di emissione, la MUF può essere determinata approssimativamente da $f_\text{c}$ utilizzando la seguente formula dalla raccolta di formule (valida per $\alpha > \qty{40}{\degree}$):

$MUF \approx \frac{f_\text{c}}{sin(\alpha)}$

dove $\alpha$ indica l'angolo di emissione (cfr. figura [ref:e_muf_winkel]). Guardando più attentamente la formula, si riconosce che la MUF è sempre superiore alla frequenza critica, e tanto più quanto più piatta è l'emissione dell'antenna trasmittente o la ricezione dell'antenna ricevente.

[question:AH208]

---

Per la pianificazione delle frequenze commerciali, dove è importante che un collegamento radio avvenga con alta probabilità, esiste inoltre il concetto di *FOT* (*frequency of optimal transmission*, frequenza di trasmissione ottimale), o anche $f_\text{opt}$. Questa è la frequenza che consente un collegamento radio su un determinato percorso del segnale statisticamente nel 90% di tutti i giorni; di solito è inferiore del 15% alla media mensile della MUF. Nella raccolta di formule troviamo questa relazione come 

$f_\text{OPT} = MUF \cdot 0,85$

Con queste informazioni possiamo ora risolvere il seguente problema; un calcolatore è utile.

[question:AH209]

<indepth>
Per i collegamenti DX nel radioamatore, la $f_\text{opt}$ non ha importanza, poiché di solito si sceglie la banda di frequenza più alta che consente ancora un collegamento (cioè la più vicina alla MUF), poiché lì ci si aspetta il minor rumore di fondo e quindi il miglior segnale (maggiore rapporto segnale/rumore SNR).
</indepth>

Nella classe E abbiamo già conosciuto la LUF (Lowest Usable Frequency). È determinata dalla regione D e indica la frequenza minima utilizzabile, al di sotto della quale l'attenuazione è troppo elevata. La regione D *attenua* il nostro segnale radio e per ogni salto questo segnale deve attraversare questa regione D *due* volte. Allo stesso tempo, questa attenuazione è tanto maggiore quanto più bassa è la frequenza (la relazione è quadratica: se si dimezza la frequenza, l'attenuazione si quadruplica). Pertanto, se si riduce continuamente la frequenza, si raggiungerà anch'essa prima o poi il punto in cui il segnale rifratto non è più utilizzabile; questa è la LUF.

[question:AH210]
[question:AH211]
