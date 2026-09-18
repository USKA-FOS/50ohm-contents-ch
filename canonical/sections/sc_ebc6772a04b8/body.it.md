Gli attenuatori vengono spesso utilizzati nella tecnica ad alta frequenza (HF) per ridurre in modo definito il livello di un segnale. Ad esempio, con un attenuatore di potenza è possibile ridurre la potenza d’uscita di un trasmettitore a un livello tale che il segnale di uscita non danneggi o sovramoduli gli strumenti di misura collegati. Gli attenuatori vengono impiegati anche per ridurre il livello d’ingresso degli amplificatori e dei ricevitori a un valore definito.

Un attenuatore deve sempre essere progettato per un’impedenza di sistema definita tra ingresso e uscita. Negli attenuatori realizzati in modo simmetrico, le impedenze d’ingresso e d’uscita sono identiche. Spesso si tratta dei valori usuali nella tecnica HF, ovvero $\qty{50}{\ohm}$. Affinché un attenuatore presenti le impedenze richieste all’ingresso e all’uscita, è necessario un corretto adattamento su entrambi i lati. Questo viene ottenuto mediante una rete di resistenze idonea.

Esistono diverse varianti circuitali che si differenziano per la disposizione delle resistenze. Le due varianti più comuni sono l’attenuatore a T (cfr. figura [ref:a_daempfungsglied_t]) e quello a $\pi$ (cfr. figura [ref:a_daempfungsglied_pi]). In entrambe le varianti, l’attenuazione viene ottenuta tramite una rete di resistenze che converte la potenza immessa in calore.


<margin>
[picture:342:a_daempfungsglied_pi:Attenuatore in configurazione π con sorgente e resistenza di carico]
</margin>

<margin>
[picture:341:a_daempfungsglied_t:Attenuatore in configurazione T con sorgente e resistenza di carico]
</margin>

[question:AD801]
[question:AD802]

---

L’attenuazione di un attenuatore viene solitamente espressa in dB (decibel) e si riferisce alla potenza. Ad esempio, $\qty{20}{\dB}$ significa una riduzione della potenza d’ingresso di un fattore $\num{100}$. La potenza d’uscita dopo questo attenuatore sarà quindi solo $\frac{1}{100}$ della potenza d’ingresso, il che, in caso di $\qty{100}{\watt}$ di potenza d’ingresso, corrisponde a una potenza d’uscita di $\qty{1}{\watt}$.


Negli attenuatori ohmici, l’attenuazione avviene convertendo la potenza immessa in calore. Se, ad esempio, un segnale di $\qty{100}{\watt}$ viene attenuato di $\qty{20}{\dB}$ come descritto in precedenza, $\qty{99}{\watt}$ vengono dissipati come calore nell’attenuatore. La potenza residua di $\qty{1}{\watt}$ è quindi ancora disponibile all’uscita dell’attenuatore.


[question:AD806]
[question:AD803]
[question:AD804]
[question:AD805]

Un attenuatore simmetrico può essere realizzato, ad esempio, come rete a T o a $\pi$ utilizzando resistenze. La denominazione deriva dalla disposizione delle resistenze nel circuito.


<indepth>
I valori delle resistenze per un attenuatore a $\pi$ con impedenza di $\qty{50}{\ohm}$ possono essere calcolati con le seguenti formule:


$R_1 = R_3 = \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}+1}{10^{\frac{a}{20}}-1}\right)$


Dove $a$ è l’attenuazione desiderata in $\unit{\dB}$.


$R_2 = \frac{\qty{50}{\ohm}}{2} \cdot \left( 10^{\frac{a}{20}} - \frac{1}{10^{\frac{a}{20}}}\right)$


I valori delle resistenze per un attenuatore a T con impedenza di $\qty{50}{\ohm}$ possono essere calcolati con le seguenti formule:


$R_1 = R_2 = \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}-1}{10^{\frac{a}{20}}+1} \right)$


$R_3 = 2\cdot \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}}{10^{\frac{a}{10}}-1} \right)$


<webonly>
[include:applet_daempfungsglied]
</webonly>

</indepth>

