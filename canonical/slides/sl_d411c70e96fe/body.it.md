## Il processo di campionamento

* I segnali analogici vengono convertiti in campioni discreti
* Campionamento: campionamento di un segnale continuo a intervalli di tempo definiti
* Paragonabile a una fotocamera che scatta immagini a intervalli regolari

---

### Campionamento – L'esempio della fotocamera

* Una fotocamera scatta, ad esempio, $\num{24}$ immagini al secondo
* Tra le immagini possono verificarsi movimenti rapidi che non vengono catturati
* Come con la fotocamera, un evento improvviso (ad esempio, una mosca) può andare perso tra due scatti
* Ciò comporta una perdita di informazioni temporali

---

### Perdita di informazioni e limite di ricostruzione

* Tra i campioni, cambiamenti rapidi del segnale possono rimanere inosservati
* Per una ricostruzione senza errori, è necessario un campione prima e dopo ogni cambio di segnale
* Se ciò non avviene, si perdono dettagli – si verifica l'aliasing

---

## Il teorema di Nyquist-Shannon

* Per un segnale con frequenza massima $f_{\mathrm{max}}$, la frequenza di campionamento deve essere $\gt 2 \cdot f_{\mathrm{max}}$
* Solo così tutti i cambiamenti del segnale possono essere acquisiti e ricostruiti correttamente
* Se questo limite viene violato, si verificano effetti alias

---

[question:AF617]

---

### Esempio pratico: lettore CD

* I lettori CD operano tipicamente con $\qty{44,1}{\kilo\sps}$ ($\num{44100}$ campioni al secondo)
* Ne consegue: le frequenze fino a circa $\qty{22}{\kilo\hertz}$ possono essere rappresentate correttamente
* Ciò corrisponde alla gamma di frequenza Hi-Fi dei buoni impianti stereo
* Ricorda: la frequenza di campionamento dovrebbe essere sempre leggermente superiore al doppio della frequenza massima da elaborare

---

[question:AF616]

---

[question:AF618]

---

[question:AF619]
