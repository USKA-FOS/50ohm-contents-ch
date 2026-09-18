## Formule d'approximation pour l'intensité de champ
<left>
* Calcul de l'intensité de champ électrique
* À une distance donnée d'un radiateur
* Pour une puissance et un gain donnés
* Valable uniquement en espace libre <br/> ($d > \frac{\lambda}{2\pi}$)
</left>
<right>
$\begin{split} E &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{d}\\ &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{d} \end{split}$
</right>

---
## Formule d'approximation pour la distance
<left>
* Pour une intensité de champ donnée
* Résolution par rapport à $d$
</left>
<right>
$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_A \cdot G_i}}{E}\\ &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{E} \end{split}$
</right>

---
[question:EK108]
---
### Méthode de résolution
<left>
* donné : $E = \qty{28}{\volt\per\meter}$
* donné : $g_d = \qty{7,5}{\dBd}$
* donné : $P_S = \qty{100}{\watt}$
</left>
<right>
* donné : $a_{\textrm{câble}} = \qty{1,5}{\dB}$
* recherché : $P_{\textrm{EIRP}}$
* recherché : $d$
</right>

<left>
<fragment>
$\begin{split} P_{\textrm{EIRP}} &= P_S \cdot 10^{\frac{g_d - a + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &= \qty{100}{\watt} \cdot 10^{\frac{\qty{7,5}{\dBd} - \qty{1,5}{\dB} + \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ &\approx \qty{100}{\watt} \cdot 6,5\\ &= \qty{650}{\watt} \end{split}$
</fragment>
</left>
<right>
<fragment>
$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{E}\\ &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{650}{\watt}}}{\qty{28}{\volt\per\meter}}\\ &\approx \qty{5}{\meter} \end{split}$
</fragment>
</right>

---
### Question bonus

Les $\qty{5}{\meter}$ calculés ne se situent-ils pas dans le champ proche pour la bande des $\qty{10}{\meter}$ mentionnée dans la question ?

<fragment>
$\begin{split} d &> \frac{\lambda}{2\pi}\\ \qty{5}{\meter} &> \frac{\qty{10}{\meter}}{2\pi}\\ \qty{5}{\meter} &\gtrapprox \qty{1,6}{\meter} \end{split}$
</fragment>

---
[question:EK106]
---
### Solution

* La distance de sécurité pour la protection des personnes ne s'applique qu'en espace libre
* $d > \frac{\lambda}{2\pi}$
* Bande des $\qty{160}{\meter}$ : $\qty{25,5}{\meter}$
* Bande des $\qty{80}{\meter}$ : $\qty{12,7}{\meter}$

---
[question:EK105]

<note>
Se situe dans le champ proche, comme nous l'avons calculé précédemment
</note>
