Come già illustrato nel capitolo "Raddrizzatori I" della classe E, un singolo diodo lascia passare solo la mezza onda positiva. Affinché da questa si ottenga una tensione continua utilizzabile, è necessario aggiungere almeno un condensatore che smorzi la tensione d’uscita pulsante (vedi circuito [ref:a_einweggleichrichtung_c]).

<margin>
[picture:795:a_einweggleichrichtung_c:Raddrizzatore a una semionda con condensatore]
</margin>

---

Durante la mezza onda positiva, il diodo $D$ conduce e permette il passaggio della corrente. In questo intervallo, il condensatore $C_L$ si carica fino al valore di picco della tensione alternata. Al momento della mezza onda negativa, il diodo $D$ blocca la corrente e il condensatore $C_L$ si scarica attraverso la resistenza di carico $R_L$.

Di conseguenza, ai capi della resistenza di carico $R_L$ si stabilisce una tensione continua $U_L$ leggermente pulsante (cfr. fig. [ref:a_Restwelligkeit]). Maggiore è la capacità del condensatore, più uniforme sarà la tensione continua ai capi della resistenza di carico.

<margin>
[picture:75:a_Restwelligkeit:Ondulazione della tensione continua d’uscita $U_L$]
</margin>

Tuttavia, nella progettazione del diodo e del condensatore, dobbiamo considerare che le tensioni del trasformatore sono indicate come tensioni efficaci $U_{\mathrm{eff}}$. Pertanto, dobbiamo prima determinare la tensione di picco $\hat{U}$.

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}}$

Se su un trasformatore è indicata, ad esempio, la tensione $U_a = \qty{15}{\volt}$, calcoliamo:

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}} = \sqrt{2} \cdot \qty{15}{\volt} = \qty{21,21}{\volt}$

Pertanto, in assenza di carico, si stabilirà una tensione di picco a vuoto di circa $\qty{21}{\volt}$.

[question:AD302]

Nella domanda successiva dobbiamo applicare il rapporto di trasformazione del trasformatore per determinare la nostra tensione d’uscita. Quindi inseriamo come tensione efficace d’ingresso $U_{\mathrm{eff}}$ un ventesimo della tensione d’ingresso del trasformatore di $\qty{230}{\volt}$. Dalla tensione di picco possiamo poi aggiungere metà della tensione per tenere conto della tolleranza di sicurezza.

[question:AD303]

Per risolvere il seguente esercizio dobbiamo riconoscere che il valore di picco della mezza onda negativa e la tensione del condensatore si sommano e caricano il diodo in polarizzazione inversa. Questa è la tensione massima che può verificarsi ai capi del diodo in polarizzazione inversa.

Calcoliamo: $U_{\mathrm{sperr}} = 2 \cdot \hat{u}$
Da considerare sono poi il rapporto di trasformazione $5 : 1$ del trasformatore di rete e la tolleranza di sicurezza del $\qty{20}{\percent}$.

[question:AD304]

%TODO Inserire simulazione: https://tinyurl.com/22m65xlw