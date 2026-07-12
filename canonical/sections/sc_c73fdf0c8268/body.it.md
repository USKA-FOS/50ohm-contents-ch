Le tensioni alternate sinusoidali cambiano continuamente il loro valore. Per poterle descrivere meglio, esamineremo di seguito tre parametri importanti:

1. $\hat{U}$: Il valore di picco di una tensione alternata
2. $U_\text{SS}$: il valore picco-picco 
3. $U_\text{eff}$: il valore efficace

<margin>
[picture:834:e_wechselspannung_kenngroessen:I tre parametri di una tensione alternata]
</margin>

---

Il *valore di picco* di una tensione alternata $\hat{U}$ corrisponde all'ampiezza che abbiamo già imparato nella classe N (cfr. figura [ref:e_wechselspannung_kenngroessen]). È importante, tra l'altro, per la resistenza alla tensione dei condensatori. La figura [ref:e_spannungsfestigkeit_elkos] mostra due condensatori elettrolitici con terminali, sui quali è stampata la resistenza alla tensione consentita. Il valore di picco della tensione applicata non deve superare questo limite, altrimenti si rischia la distruzione del condensatore. Spesso si scelgono componenti con una resistenza alla tensione superiore a quella richiesta, sia per motivi di sicurezza che per prolungare la durata di vita.

<margin>
[photo:198:e_spannungsfestigkeit_elkos:Condensatori elettrolitici con resistenze alla tensione di 16 Volt e 25 Volt]
</margin>

Un altro parametro è il *valore picco-picco*. Questa è la differenza tra il massimo e il minimo scostamento. Per le tensioni alternate sinusoidali vale:

$U_\text{SS} = 2\cdot \hat{U}$.
 
[question:EB406]
[question:EB407]

Se non è importante la tensione, ma la potenza degli apparecchi o il carico termico dei componenti e dei cavi, il valore di picco non è utile. Per questo caso è stato definito il *valore efficace*. Il valore efficace di una tensione alternata corrisponde al valore di una tensione continua che riscalderebbe una resistenza ohmica allo stesso modo.

---

Per le tensioni sinusoidali, il valore di picco o valore di cresta è circa 1,4 volte più grande del valore efficace (vedi figura [ref:e_wechselspannung_kenngroessen]). Il calcolo esatto porta a una formula semplice:

$U_{eff} = \frac{\hat{U}}{\sqrt{2}}$ o $\hat{U} = U_{eff} \cdot \sqrt{2}$

Se una tensione alternata viene indicata solo con la lettera $U$ senza alcuna indicazione aggiuntiva, si intende solitamente il valore efficace. L'esempio più noto è la nostra tensione di rete di $\qty{230}{\volt}$ – anche in questo caso si tratta del valore efficace. La tensione di picco è significativamente più alta, ovvero $\qty{325}{\volt}$.

$\hat{U} = \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{325}{\volt}$.

<indepth>
La derivazione esatta di questa formula avviene tramite il calcolo integrale e va oltre le conoscenze richieste per l'esame di radioamatore. Chi ha familiarità con il calcolo integrale e ne è interessato, può leggere la derivazione qui: [Wikipedia](https://50ohm.de/ew)
</indepth>

[question:EB401]

Il valore per $U_\text{SS}$ per la tensione di rete è quindi il doppio del valore di picco:

$ U_\text{SS} = 2 \cdot \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{651}{\volt}$

[question:EB402]

Secondo lo stesso principio funzionano anche le seguenti domande:

[question:EB403]
[question:EB404]

---

% TODO inserire riferimento al capitolo sulla potenza:

Nella prossima domanda viene chiesto indirettamente il valore efficace della tensione. Se si sa che $\frac{1}{\sqrt{2}} \approx 0,7$, si possono leggere direttamente i due risultati. 

<indepth>
È importante che sia la tensione continua $\qty{0,7}{\volt}$ che la tensione continua $\qty{-0,7}{\volt}$ portino allo stesso risultato. Ciò è dovuto al fatto che con una tensione negativa cambia anche il segno della corrente, il che tuttavia porta comunque alla stessa potenza – poiché vale $P = U \cdot I$.
</indepth>

[question:EB405]

Tra l'altro: tutto ciò che è scritto qui sulle tensioni alternate vale analogamente per le correnti alternate.