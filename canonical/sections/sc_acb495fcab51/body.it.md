La *MUF* (*maximum usable frequency*, frequenza massima utilizzabile), cioè la frequenza più alta che la ionosfera può ancora rifrangere per la distanza tra trasmettitore e ricevitore, l'abbiamo già incontrata nella classe E. In quella sede è emerso che la MUF dipende dalla densità degli elettroni liberi nella regione di rifrazione. Nella classe A approfondiremo questo argomento, in particolare con riguardo all'angolo di irradiazione.

[question:AH206]
[question:AH207]

Come già sappiamo, la portata delle onde spaziali dipende dall'angolo di irradiazione. Più piatto è l'angolo con cui l'onda incide sulla ionosfera, più agevole è la rifrazione. Questo rapporto vale anche per la MUF: la frequenza appena rifratta, cioè la *MUF*, è tanto più alta quanto più piatto è l'angolo di incidenza del nostro segnale nella ionosfera. La figura [ref:e_muf_winkel2] mostra una simulazione della distanza di salto per una giornata estiva nel 2024 per un segnale radioamatoriale intorno ai $\qty{7}{\mega\hertz}$. A $\qty{45}{\degree}$ la MUF in quel giorno era di $\qty{7,5}{\mega\hertz}$. Modificando l'angolo di irradiazione, cambia anche la MUF: se si irradia con un angolo più ripido (ad esempio $\qty{60}{\degree}$), la MUF diminuisce e l'onda radio non viene più rifratta. Se invece si irradia con un angolo più piatto (ad esempio $\qty{30}{\degree}$), la MUF aumenta. Nei paragrafi seguenti esamineremo questo rapporto in dettaglio.

<margin>
[picture:998:e_muf_winkel2:Distanza di salto a 7 MHz nell'estate 2024]
</margin>

---

Le stazioni di misurazione della ionosfera rilevano la cosiddetta frequenza critica $f_\text{c}$ (o spesso anche $f_\text{k}$, $f_\text{krit}$ o $f_\text{oF2}$). Si tratta della frequenza più alta alla quale l'onda spaziale che entra perpendicolarmente nella ionosfera viene appena riflessa (cfr. figura [ref:e_muf_winkel]). Se irradiamo verticalmente verso l'alto, cioè il nostro segnale incide sulla ionosfera con un angolo di $\qty{90}{\degree}$, la MUF è minima, poiché il segnale deve compiere un "giro" completo di 180° all'interno della ionosfera. Ciò significa che a $\qty{90}{\degree}$ vale $f_\text{c} = MUF$. 

<indepth>
Come simbolo si usa $f_o$ (lettera minuscola "o" in pedice per *ordinary wave*) seguita dalla regione ionosferica a cui si riferisce questa frequenza, ad esempio $f_\text{oF2}$ per la regione F2. Tuttavia, spesso si usano anche i simboli $f_\text{c}$, $f_\text{k}$ o $f_\text{krit}$.
</indepth>

<margin>
[picture:870:e_muf_winkel:Gli angoli per il calcolo della MUF]
</margin>

<indepth>
La frequenza critica è quindi la frequenza più alta che torna indietro dalla ionosfera quando si irradia verticalmente verso l'alto. Una regola empirica afferma che la frequenza più alta che viene ancora riflessa in caso di incidenza *piatta* è circa il triplo della frequenza critica.
</indepth>

[question:AH204]
[question:AH205]

---

La figura [ref:e_muf_fof2] mostra l'andamento temporale della MUF e di $f_\text{c}$ l'08.09.2025, misurato con l'ionosonda di Juliusruh. La MUF $\qty{3000}{\kilo\meter}$ in questo caso significa che si irradia con un angolo molto piatto per raggiungere una distanza di salto di $\qty{3000}{\kilo\meter}$.

<margin>
[picture:999:e_muf_fof2:MUF e $f_\text{c}$ l'08.09.2025]
</margin>

Per altri angoli di irradiazione, la MUF può essere determinata approssimativamente dalla $f_\text{c}$ utilizzando la seguente formula tratta dalla raccolta di formule (vale per $\alpha > \qty{40}{\degree}$):

$MUF \approx \frac{f_\text{c}}{sin(\alpha)}$

dove $\alpha$ indica l'angolo di irradiazione (cfr. figura [ref:e_muf_winkel]). Osservando attentamente la formula, si nota che la MUF è sempre più alta della frequenza critica – e tanto più quanto più piatto è l'angolo di irradiazione dell'antenna trasmittente o ricevente.

[question:AH208]

---

Per la pianificazione delle frequenze commerciali, dove è importante che un collegamento radio abbia un'elevata probabilità di successo, esiste inoltre il concetto di *FOT* (*frequency of optimal transmission*, frequenza di trasmissione ottimale), o anche $f_\text{opt}$. Si tratta della frequenza che, su un determinato percorso del segnale, consente un collegamento radio statisticamente nel 90% dei giorni; di solito è il 15% in meno della media mensile della MUF. Nella raccolta di formule troviamo questa relazione come

$f_\text{OPT} = MUF \cdot 0,85$

Con queste informazioni possiamo ora risolvere il seguente esercizio; un calcolatore tascabile può essere utile.

[question:AH209]

<indepth>
Per i collegamenti DX nel radioamatoriale, la $f_\text{opt}$ non riveste alcun ruolo, poiché in genere si sceglie la banda di frequenza più alta che consente ancora un collegamento (quindi la più vicina alla MUF), poiché in questo caso si può aspettare il minor rumore di fondo e quindi il miglior segnale (maggiore rapporto segnale/rumore SNR).
</indepth>

Nella classe E abbiamo già incontrato la LUF (*Lowest Usable Frequency*). Essa è determinata dallo strato D e indica la frequenza minima utilizzabile, al di sotto della quale l'attenuazione è troppo elevata. Lo strato D *attenua* infatti il nostro segnale radio e, per ogni salto, questo segnale deve attraversare *due* volte questo strato. Allo stesso tempo, questa attenuazione è tanto maggiore quanto più bassa è la frequenza (la relazione è quadratica: dimezzando la frequenza, l'attenuazione si quadruplica). Pertanto, se si continua a ridurre la frequenza, si arriverà prima o poi al punto in cui il segnale rifratto non è più utilizzabile; questa è la LUF.

[question:AH210]
[question:AH211]
