## Mesure du courant et de la tension

<left>
* La tension est mesurée en parallèle avec le composant
* Le courant est mesuré en série avec le composant
</left>
<right>
[picture:1003:a_strom_spannung_messung:Mesure de la puissance d'un amplificateur (PA)]
</right>

---
[question:AI101]
---
[question:AI102]
---
## Précision de la mesure

La valeur mesurée affichée diffère généralement de la valeur réelle
* Résistance interne de l'appareil de mesure
* Pouvoir de résolution $\rightarrow$ *résolution la plus petite*
* L'affichage ne change qu'après une modification de la plus petite résolution
* Le fabricant détermine l'écart
* L'écart est indiqué dans la fiche technique

---

<left>
[picture:1004:a_reale_spannungsmessung:Circuit équivalent appareil de mesure de tension réel]
</left>

<right>
[picture:1007:a_reale_strommessung:Circuit équivalent appareil de mesure de courant réel]
</right>

---
[question:AI103]
--- style="font-size: smaller;"
### Solution

* Calcul en pourcentage – les valeurs absolues ne sont pas pertinentes
* donné: $U_{\mathrm{Abw}}$ avec $\qty{95}{\percent}$ de la valeur réelle
* donné: $I_{\mathrm{Abw}}$ avec $\qty{95}{\percent}$ de la valeur réelle
* recherché: écart de la puissance $P = U \cdot I$

<fragment>
$\begin{split} P_{\textrm{Abw}} &= 100\% - (U_{\mathrm{Abw}} \cdot I_{\mathrm{Abw}})\\ &= 100\% - (95\% \cdot 95\%)\\ &= 100\% - 90,25\%\\ &= 9,75\% \end{split}$
</fragment>

---
## Courant à travers un multimètre

* Même lors d'une mesure de tension, un courant traverse un appareil de mesure
* Il se produit une division de courant
* Grâce à la haute résistance interne, le courant qui s'écoule est relativement faible

---
[question:AI104]
---
### Solution
* donné: $U = \qty{0,5}{\volt}$
* donné: $R = \qty{10}{\mega\ohm}$
* recherché: $I$

<fragment>
$$I = \frac{U}{R} = \frac{\qty{0,5}{\volt}}{\qty{10}{\mega\ohm}} = \qty{50}{\nano\ampere}$$
</fragment>

