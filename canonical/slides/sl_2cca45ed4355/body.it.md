## Antenne di eccitazione in un riflettore parabolico
<left>
[picture:850:a_parabolspiegel_schnitt:Sezione di un riflettore parabolico con antenna]
</left>
<right>
* Le antenne di eccitazione vengono posizionate nel punto focale davanti al riflettore parabolico
* Le antenne elicoidali, che generano una polarizzazione circolare, sono particolarmente adatte per la gamma delle microonde
</right>

---
## Antenna a tromba e guide d'onda
<left>
Immagine di un'antenna a tromba in seguito
</left>
<right>
* Le antenne a tromba possono essere alimentate tramite una guida d'onda
* Nelle guide d'onda, cioè tubi metallici, l'energia a microonde viene guidata tramite riflessione sulle pareti esterne
</right>

---
## Guide d'onda in dettaglio

* Le guide d'onda guidano le microonde riflettendole sulle loro pareti metalliche esterne
* In questo modo l'onda viene indirizzata verso un'antenna a tromba, da cui viene irradiata o immessa nella guida d'onda

---
[question:AG225]
---
## Guadagno di un riflettore parabolico

$g_i = 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot d}{\lambda}\right)^2 \cdot \eta\right)}\unit{\dBi}$

* Calcolo con la formula nella [raccolta di formule](#)
* Dipendente dal diametro
* Solitamente guadagno molto elevato

---
[question:AG226]
---
#### Procedimento di soluzione
<left>
* dati: $d = \qty{30}{\centi\meter}$
* dati: $\eta_{eff} = 1$
</left>
<right>
* dati: $f = \qty{5,7}{\giga\hertz}$
* richiesto: $g_i$
</right>

<fragment>
$\lambda = \frac{c}{f} = \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{5,7}{\giga\hertz}} = \qty{0,053}{\meter}$
</fragment>
<fragment>
$\begin{split}g_i &= 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot d}{\lambda}\right)^2 \cdot \eta\right)}\unit{\dBi}\\ &= 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot \qty{0,3}{\meter}}{\qty{0,053}{\meter}}\right)^2 \cdot 1\right)} \unit{\dBi}\\n&= \qty{25,1}{\dBi}\end{split}$
</fragment>
---
[question:AG227]
---
#### Procedimento di soluzione
<left>
* dati: $d = \qty{80}{\centi\meter}$
* dati: $\eta_{eff} = 1$
</left>
<right>
* dati: $f = \qty{5,7}{\giga\hertz}$
* richiesto: $g_i$
</right>

<fragment>
$\lambda = \frac{c}{f} = \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{5,7}{\giga\hertz}} = \qty{0,053}{\meter}$
</fragment>
<fragment>
$\begin{split}g_i &= 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot d}{\lambda}\right)^2 \cdot \eta\right)}\unit{\dBi}\\ &= 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot \qty{0,8}{\meter}}{\qty{0,053}{\meter}}\right)^2 \cdot 1\right)} \unit{\dBi}\\n&= \qty{33,6}{\dBi}\end{split}$
</fragment>
---
[question:AG228]
---
#### Procedimento di soluzione
<left>
* dati: $d = \qty{80}{\centi\meter}$
* dati: $\eta_{eff} = 1$
</left>
<right>
* dati: $f = \qty{10,4}{\giga\hertz}$
* richiesto: $g_i$
</right>

<fragment>
$\lambda = \frac{c}{f} = \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{10,4}{\giga\hertz}} = \qty{0,029}{\meter}$
</fragment>
<fragment>
$\begin{split}g_i &= 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot d}{\lambda}\right)^2 \cdot \eta\right)}\unit{\dBi}\\ &= 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot \qty{0,8}{\meter}}{\qty{0,029}{\meter}}\right)^2 \cdot 1\right)} \unit{\dBi}\\
&= \qty{38,8}{\dBi}\end{split}$
</fragment>
---
[question:AG229]
---
#### Procedimento di soluzione
<left>
* dati: $d = \qty{120}{\centi\meter}$
* dati: $\eta_{eff} = 1$
</left>
<right>
* dati: $f = \qty{10,4}{\giga\hertz}$
* richiesto: $g_i$
</right>

<fragment>
$\lambda = \frac{c}{f} = \frac{\qty{3\cdot 10^8}{\meter\per\second}}{\qty{10,4}{\giga\hertz}} = \qty{0,029}{\meter}$
</fragment>
<fragment>
$\begin{split}g_i &= 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot d}{\lambda}\right)^2 \cdot \eta\right)}\unit{\dBi}\\ &= 10 \cdot \log_{10}{\left(\left(\frac{\pi \cdot \qty{1,2}{\meter}}{\qty{0,029}{\meter}}\right)^2 \cdot 1\right)} \unit{\dBi}\\
&= \qty{42,3}{\dBi}\end{split}$