Le tensioni alternate sinusoidali cambiano continuamente il loro valore. Per poterle descrivere meglio, nei paragrafi seguenti esamineremo tre importanti grandezze caratteristiche:

1. $\hat{U}$: il valore di picco di una tensione alternata
2. $U_\text{SS}$: il valore picco-picco
3. $U_\text{eff}$: il valore efficace

<margin>
[picture:834:e_wechselspannung_kenngroessen:Le tre grandezze caratteristiche di una tensione alternata]
</margin>

---

Il *valore di picco* di una tensione alternata $\hat{U}$ corrisponde all'ampiezza, che abbiamo già imparato a conoscere nella classe N (cfr. figura [ref:e_wechselspannung_kenngroessen]). Esso è importante, tra l'altro, per la tenuta in tensione dei condensatori. La figura [ref:e_spannungsfestigkeit_elkos] mostra due condensatori elettrolitici con terminali sui quali è stampigliata la tensione massima consentita. Il valore di picco della tensione applicata non deve superare questo limite, altrimenti il condensatore rischia di essere danneggiato. Spesso si scelgono componenti con una tenuta in tensione superiore al necessario, sia per motivi di sicurezza che per prolungarne la durata.

<margin>
[photo:198:e_spannungsfestigkeit_elkos:Condensatori elettrolitici con tenuta in tensione di 16 volt e 25 volt]
</margin>

Un'altra grandezza caratteristica è il *valore picco-picco*. Si tratta della differenza tra il picco massimo e quello minimo. Per le tensioni alternate sinusoidali vale:

$U_\text{SS} = 2\cdot \hat{U}$.

[question:EB406]
[question:EB407]

Se non è la tensione, ma la potenza dei dispositivi o il carico termico di componenti e conduttori a essere al centro dell'attenzione, il valore di picco non è utile. In questo caso è stato definito il *valore efficace*. Il valore efficace di una tensione alternata corrisponde al valore di una tensione continua che riscalderebbe una resistenza ohmica con la stessa intensità.

---

Nelle tensioni sinusoidali, il valore di picco o di cresta è circa 1,4 volte maggiore del valore efficace (vedi figura [ref:e_wechselspannung_kenngroessen]). Il calcolo preciso porta a una formula semplice:

$U_{eff} = \frac{\hat{U}}{\sqrt{2}}$ oppure $\hat{U} = U_{eff} \cdot \sqrt{2}$

Se una tensione alternata è indicata solo con la lettera $U$ senza ulteriori specificazioni, di norma si intende il valore efficace. L'esempio più noto è la nostra tensione di rete di $\qty{230}{\volt}$ – anche in questo caso si tratta del valore efficace. La tensione di picco è notevolmente più alta, ovvero:

$\hat{U} = \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{325}{\volt}$.

<indepth>
La derivazione precisa di questa formula avviene tramite il calcolo integrale e va oltre le conoscenze richieste per l'esame radioamatoriale. Chi conosce il calcolo integrale e si interessa può leggere la derivazione qui: [Wikipedia](https://de.wikipedia.org/wiki/Effektivwert)
</indepth>

[question:EB401]

Il valore di $U_\text{SS}$ per la tensione di rete risulta quindi essere il doppio del valore di picco:

$ U_\text{SS} = 2 \cdot \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{651}{\volt}$

[question:EB402]

Lo stesso principio si applica anche alle seguenti domande:

[question:EB403]
[question:EB404]

---

% TODO inserire riferimento al capitolo sulla potenza:

Nella domanda successiva viene richiesto indirettamente il valore efficace della tensione. Se si sa che $\frac{1}{\sqrt{2}} \approx 0,7$, si possono leggere direttamente i due risultati.

<indepth>
È importante notare che sia la tensione continua $\qty{0,7}{\volt}$ che quella negativa $\qty{-0,7}{\volt}$ portano allo stesso risultato. Questo perché, con una tensione negativa, anche il segno della corrente cambia, ma ciò porta comunque alla stessa potenza – poiché vale $P = U \cdot I$.
</indepth>

[question:EB405]

A proposito: tutto ciò che è stato scritto qui sulle tensioni alternate vale analogamente anche per le correnti alternate.