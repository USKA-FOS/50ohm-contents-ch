Le applicazioni degli attenuatori le abbiamo già incontrate nella sezione [sec:vorverstaerker_daempfungsglied]. Ora consideriamo diverse forme di realizzazione degli attenuatori.

Gli attenuatori sono spesso necessari nella tecnica RF per attenuare in modo definito i livelli di segnale. Ad esempio, attraverso un attenuatore di potenza, la potenza d’uscita di un trasmettitore può essere ridotta al punto che il suo segnale di uscita non danneggi o sovraccarichi gli strumenti di misura collegati. Si usano attenuatori anche per ridurre i livelli d'ingresso per amplificatori e ricevitori a un livello definito.

Un attenuatore deve sempre essere progettato per un'impedenza di sistema definita rispetto all'ingresso e all'uscita. Negli attenuatori simmetricamente costruiti, le impedenze d'ingresso e d'uscita sono identiche. Spesso queste sono le consuete $\qty{50}{\ohm}$ nella tecnica RF. Affinché un attenuatore presenti le impedenze richieste al suo ingresso e uscita, è necessario un adattamento di impedenza corretto su entrambi i lati. Ciò si ottiene con una rete di resistenze adeguata.

Esistono diverse varianti circuitali, che differiscono nella disposizione delle resistenze. Le due varianti più comuni sono l'attenuatore a T (cfr. figura [ref:a_daempfungsglied_t]) e l'attenuatore a $\pi$ (cfr. figura [ref:a_daempfungsglied_pi]). In entrambe le varianti, l'attenuazione si ottiene con una rete di resistenze che converte la potenza immessa in calore.

<margin>
[picture:342:a_daempfungsglied_pi:Attenuatore in configurazione PI con sorgente e resistenza di carico]
</margin>

<margin>
[picture:341:a_daempfungsglied_t:Attenuatore in configurazione T con sorgente e resistenza di carico]
</margin>

[question:AD801]
[question:AD802]

---

L'attenuazione di un attenuatore è solitamente indicata in dB (decibel) e si riferisce alla potenza. Ad esempio, $\qty{20}{\dB}$ significa un'attenuazione della potenza d’ingresso di un fattore $\num{100}$. La potenza d’uscita dopo questo attenuatore è quindi solo $\frac{1}{100}$ della potenza d’ingresso, che nel caso di $\qty{100}{\watt}$ di potenza d’ingresso corrisponde a una potenza d’uscita di $\qty{1}{\watt}$.

Negli attenuatori ohmici, l'attenuazione avviene convertendo la potenza immessa in calore. Se, ad esempio, un segnale di $\qty{100}{\watt}$ viene attenuato di $\qty{20}{\dB}$ come descritto prima, allora $\qty{99}{\watt}$ vengono convertiti in calore nell'attenuatore. La potenza rimanente di $\qty{1}{\watt}$ è quindi ancora disponibile all'uscita dell'attenuatore.

[question:AD806]
[question:AD803]
[question:AD804]
[question:AD805]

Un attenuatore simmetrico può essere costruito, ad esempio, come rete a T o a $\pi$ di resistenze. La denominazione deriva dall'aspetto della disposizione delle resistenze nel circuito.

<indepth>
I valori delle resistenze per un attenuatore a $\pi$ per un'impedenza di $\qty{50}{\ohm}$ possono essere calcolati con le seguenti formule:

$R_1 = R_3 = \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}+1}{10^{\frac{a}{20}}-1}\right)$

Dove $a$ è l'attenuazione desiderata in $\unit{\dB}$.

$R_2 = \frac{\qty{50}{\ohm}}{2} \cdot \left( 10^{\frac{a}{20}} - \frac{1}{10^{\frac{a}{20}}}\right)$

I valori delle resistenze per un attenuatore a T per un'impedenza di $\qty{50}{\ohm}$ possono essere calcolati con le seguenti formule:

$R_1 = R_2 = \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}-1}{10^{\frac{a}{20}}+1} \right)$

$R_3 = 2\cdot \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}}{10^{\frac{a}{10}}-1} \right)$

<webonly>
[include:applet_daempfungsglied]
</webonly>

</indepth>

