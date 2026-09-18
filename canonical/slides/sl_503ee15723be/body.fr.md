## Impédance caractéristique d'une ligne bifilaire

* L'impédance caractéristique $Z$ dépend du rapport entre la distance entre les conducteurs ($a$) et le diamètre des conducteurs $d$, ainsi que du diélectrique
* Formule issue du recueil de formules avec $\epsilon_\mathrm{r}$ comme permittivité relative :

<fragment>
$Z = \dfrac{\qty{120}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{2 \cdot a}{d}\right)}$
</fragment>

---
[question:AG305]
---
#### Méthode de résolution
* donné : $d = \qty{2}{\milli\meter}$
* donné : $a = \qty{20}{\centi\meter}$
* donné : $\epsilon_\mathrm{r} \approx 1$ pour l'air
* recherché : $Z$

<fragment>
$\begin{split}Z &= \dfrac{\qty{120}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{2 \cdot a}{d}\right)}\\ &= \dfrac{\qty{120}{\ohm}}{\sqrt{1}} \cdot \ln{\left(\dfrac{2 \cdot \qty{200}{\milli\meter}}{\qty{2}{\milli\meter}}\right)}\\ &\approx \qty{635}{\ohm}\end{split}$
</fragment>
---
## Impédance caractéristique d'une ligne coaxiale

* L'impédance caractéristique $Z$ dépend du rapport entre le diamètre intérieur du conducteur extérieur ($D$) et le diamètre du conducteur intérieur ($d$), ainsi que du diélectrique
* Formule issue du recueil de formules avec $\epsilon_\mathrm{r}$ comme permittivité relative

<fragment>
$Z = \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\dfrac{D}{d}}$
</fragment>

---
[question:AG306]
----
#### Méthode de résolution
* donné : $D = \qty{5}{\milli\meter}$
* donné : $d = \qty{1}{\milli\meter}$
* donné : $\epsilon_\mathrm{r} \approx 1$ pour l'air
* recherché : $Z$

<fragment>
$\begin{split}Z &= \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{D}{d}\right)}\\ &= \dfrac{\qty{60}{\ohm}}{\sqrt{1}} \cdot \ln{\left(\dfrac{\qty{5}{\milli\meter}}{\qty{1}{\milli\meter}}\right)}\\ &\approx \qty{97}{\ohm}\end{split}$
</fragment>
---
[question:AG307]
---
#### Méthode de résolution
* donné : $d = \qty{0,7}{\milli\meter}$
* donné : $D = \qty{4,4}{\milli\meter}$
* donné : $\epsilon_\mathrm{r} = 2,29$
* recherché : $Z$

<fragment>
$\begin{split}Z &= \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{D}{d}\right)}\\ &= \dfrac{\qty{60}{\ohm}}{\sqrt{2,29}} \cdot \ln{\left(\dfrac{\qty{4,4}{\milli\meter}}{\qty{0,7}{\milli\meter}}\right)}\\ &\approx \qty{75}{\ohm}\end{split}$
</fragment>
---
### Adaptation des lignes coaxiales

* Lorsqu'un composant ou une antenne est connecté(e) avec une impédance caractéristique identique à celle de la ligne, on parle d'adaptation
* En cas d'adaptation, les ondes ne sont pas réfléchies à la terminaison

---
[question:AG304]