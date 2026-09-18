## Il processo di campionamento

* I segnali analogici vengono convertiti in campioni discreti
* Campionamento: acquisizione di un segnale continuo a intervalli di tempo definiti
* Paragonabile a una fotocamera che scatta immagini a intervalli regolari

---

### Campionamento – L’esempio della fotocamera

* Una fotocamera scatta, ad esempio, $\num{24}$ immagini al secondo
* Tra un’immagine e l’altra possono verificarsi movimenti rapidi che non vengono catturati
* Come nella fotocamera, un evento improvviso (ad esempio una mosca) può perdersi tra due scatti
* Ne consegue una perdita di informazioni temporali

---

### Perdita di informazioni e limite di ricostruzione

* Tra un campione e l’altro possono passare inosservati rapidi cambiamenti del segnale
* Per una ricostruzione senza errori, deve esserci un campione prima e dopo ogni variazione del segnale
* Se ciò non avviene, si perdono dettagli e si verifica l’effetto aliasing

---

## Il teorema di campionamento di Nyquist-Shannon

* Per un segnale con frequenza massima $f_{\mathrm{max}}$, la frequenza di campionamento deve essere $\gt 2 \cdot f_{\mathrm{max}}$
* Solo così tutti i cambiamenti del segnale possono essere correttamente acquisiti e ricostruiti
* Se questo limite non viene rispettato, si verificano effetti di aliasing

---

[domanda:AF617]


---

### Esempio pratico: lettore CD

* I lettori CD lavorano tipicamente con $\qty{44,1}{\kilo\sps}$ ($
\num{44100}$ campioni al secondo)
* Ne consegue che le frequenze fino a circa $\qty{22}{\kilo\hertz}$ possono essere correttamente rappresentate
* Questo corrisponde alla banda di frequenza HiFi di impianti stereo di buona qualità
* Nota: la frequenza di campionamento dovrebbe sempre essere leggermente superiore al doppio della frequenza massima da elaborare

---

[domanda:AF616]


---

[domanda:AF618]


---

[domanda:AF619]