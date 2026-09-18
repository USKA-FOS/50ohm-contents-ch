## Mesure de courant et de tension

<left>
* La tension se mesure en parallèle avec le composant
* Le courant se mesure en série avec le composant
</left>
<right>
[picture:1003:a_strom_spannung_messung:Mesure de la puissance d'un amplificateur (PA)]
</right>

---
[question:AI101]
---
[question:AI102]
---
## Précision de mesure

La valeur mesurée affichée diffère généralement de la valeur réelle en raison de plusieurs facteurs :
* Résistance interne de l'appareil de mesure
* Résolution $\rightarrow$ *résolution minimale*
* L'affichage ne change qu'après une modification supérieure à la résolution minimale
* Le fabricant détermine l'écart
* L'écart est indiqué dans la fiche technique

---

<left>
[picture:1004:a_reale_spannungsmessung:Schéma équivalent d'un voltmètre réel]
</left>

<right>
[picture:1007:a_reale_strommessung:Schéma équivalent d'un ampèremètre réel]
</right>

---
[question:AI103]
--- style="font-size: smaller;"
### Méthode de résolution

* Calcul en pourcentage – les valeurs absolues ne sont pas pertinentes
* donné : $U_{\mathrm{écart}}$ à $\qty{95}{\percent}$ de la valeur réelle
* donné : $I_{\mathrm{écart}}$ à $\qty{95}{\percent}$ de la valeur réelle
* recherché : écart de la puissance $P = U \cdot I$

<fragment>
$\begin{split} P_{\textrm{écart}} &= 100\% - (U_{\mathrm{écart}} \cdot I_{\mathrm{écart}})\\ &= 100\% - (95\% \cdot 95\%)\\ &= 100\% - 90,25\%\\ &= 9,75\% \end{split}$
</fragment>

---
## Courant traversant un multimètre

* Même lors d'une mesure de tension, un courant circule à travers l'appareil de mesure
* Il se produit une répartition du courant
* Grâce à la résistance interne élevée, le courant qui s'écoule est relativement faible

---
[question:AI104]
---
### Méthode de résolution
* donné : $U = \qty{0,5}{\volt}$
* donné : $R = \qty{10}{\mega\ohm}$
* recherché : $I$

<fragment>
$$I = \frac{U}{R} = \frac{\qty{0,5}{\volt}}{\qty{10}{\mega\ohm}} = \qty{50}{\nano\ampère}$$
</fragment>
