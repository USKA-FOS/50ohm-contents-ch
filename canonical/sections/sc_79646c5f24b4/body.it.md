Più forte è la modulazione di una portante AM, più la sua ampiezza varia nel tempo. Senza modulazione, viene trasmessa solo la portante HF con ampiezza costante (cfr. figura [ref:modulationsgrad_0]). Con una modulazione crescente, l'ampiezza della portante HF segue sempre più il segnale BF modulante, dando origine all'inviluppo tipico (cfr. figura [ref:modulationsgrad_10]).

Il rapporto tra l'ampiezza del segnale BF modulante e l'ampiezza della portante non modulata determina il *grado di modulazione* $m$. Con un grado di modulazione di $m=1$ o $\qty{100}{\percent}$, la portante viene completamente pilotata. L'inviluppo oscilla allora tra zero e il doppio del valore dell'ampiezza della portante non modulata (cfr. figura [ref:modulationsgrad_100]).

[question:AE201]

<margin>
[picture:27:modulationsgrad_0:Grado di modulazione di $\qty{0}{\percent}$ di un segnale AM]
[picture:26:modulationsgrad_10:Grado di modulazione di $\qty{10}{\percent}$ di un segnale AM]
[picture:24:modulationsgrad_100:Grado di modulazione di $\qty{100}{\percent}$ di un segnale AM]
</margin>

---

Non appena il grado di modulazione supera $m=1$ o $\qty{100}{\percent}$ (cfr. figura [ref:modulationsgrad_1000]), si parla di *sovramodulazione*. L'inviluppo non raggiunge solo il valore zero, ma matematicamente cambierebbe anche la sua polarità. Di conseguenza, il segnale non può più essere riprodotto senza distorsioni con un demodulatore ad inviluppo convenzionale.

Nei trasmettitori reali, la sovramodulazione può inoltre portare a una limitazione e quindi a componenti spettrali indesiderate aggiuntive, chiamate *splatter della banda laterale*. Per evitarlo, il grado di modulazione nell'AM convenzionale non deve superare $\qty{100}{\percent}$.

<margin>
[picture:28:modulationsgrad_1000:Grado di modulazione di $> \qty{100}{\percent}$ (sovramodulazione) di un segnale AM]
</margin>

[question:AE204]
[question:AE203]

---

Il grado di modulazione si calcola con la seguente formula (incl. figura [ref:modulationsgrad] nella raccolta di formule):

$m = \frac{\hat{U}_\mathrm{mod}}{\hat{U}_\mathrm{T}}$

<margin>
[picture:328:modulationsgrad:Grado di modulazione di un segnale AM]
</margin>

Prova ora a leggere i valori nel seguente esercizio e a calcolare il grado di modulazione $m$:

[question:AE202]