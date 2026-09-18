## Impedenza caratteristica di una linea bifilare

* L’impedenza caratteristica $Z$ dipende dal rapporto tra la distanza doppia dei conduttori ($a$) e il diametro dei conduttori $d$, nonché dal materiale dielettrico
* Formula tratta dalla raccolta di formule con $\epsilon_\mathrm{r}$ come costante dielettrica relativa:

<fragment>
$Z = \dfrac{\qty{120}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{2 \cdot a}{d}\right)}$
</fragment>

---
[question:AG305]
---
#### Procedimento di soluzione
* dati: $d = \qty{2}{\milli\meter}$
* dati: $a = \qty{20}{\centi\meter}$
* dati: $\epsilon_\mathrm{r} \approx 1$ per l’aria
* richiesto: $Z$

<fragment>
$\begin{split}Z &= \dfrac{\qty{120}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{2 \cdot a}{d}\right)}\\ &= \dfrac{\qty{120}{\ohm}}{\sqrt{1}} \cdot \ln{\left(\dfrac{2 \cdot \qty{200}{\milli\meter}}{\qty{2}{\milli\meter}}\right)}\\ &\approx \qty{635}{\ohm}\end{split}$
</fragment>
---
## Impedenza caratteristica di una linea coassiale

* L’impedenza caratteristica $Z$ dipende dal rapporto tra il diametro interno del conduttore esterno ($D$) e il diametro del conduttore interno ($d$), nonché dal materiale dielettrico
* Formula tratta dalla raccolta di formule con $\epsilon_\mathrm{r}$ come costante dielettrica relativa

<fragment>
$Z = \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\dfrac{D}{d}}$
</fragment>

---
[question:AG306]
----
#### Procedimento di soluzione
* dati: $D = \qty{5}{\milli\meter}$
* dati: $d = \qty{1}{\milli\meter}$
* dati: $\epsilon_\mathrm{r} \approx 1$ per l’aria
* richiesto: $Z$

<fragment>
$\begin{split}Z &= \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{D}{d}\right)}\\ &= \dfrac{\qty{60}{\ohm}}{\sqrt{1}} \cdot \ln{\left(\dfrac{\qty{5}{\milli\meter}}{\qty{1}{\milli\meter}}\right)}\\ &\approx \qty{97}{\ohm}\end{split}$
</fragment>
---
[question:AG307]
---
#### Procedimento di soluzione
* dati: $d = \qty{0,7}{\milli\meter}$
* dati: $D = \qty{4,4}{\milli\meter}$
* dati: $\epsilon_\mathrm{r} = 2,29$
* richiesto: $Z$

<fragment>
$\begin{split}Z &= \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{D}{d}\right)}\\ &= \dfrac{\qty{60}{\ohm}}{\sqrt{2,29}} \cdot \ln{\left(\dfrac{\qty{4,4}{\milli\meter}}{\qty{0,7}{\milli\meter}}\right)}\\ &\approx \qty{75}{\ohm}\end{split}$
</fragment>
---
### Adattamento delle linee coassiali

* Se si collega un componente o un’antenna che presenta esattamente l’impedenza caratteristica della linea, si parla di adattamento
* In caso di adattamento, le onde non vengono riflesse all’estremità della linea

---
[question:AG304]