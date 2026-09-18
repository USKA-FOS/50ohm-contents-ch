## Champ proche et ses subdivisions

* Le champ proche se divise en champ proche réactif et champ proche rayonnant
* Dans la plupart des cas, le champ proche rayonnant peut être traité comme le champ lointain

---
### Champ proche réactif

* Dans le champ proche réactif, il n’existe pas de relation de phase constante entre l’intensité de champ électrique et l’intensité de champ magnétique

---
[question:AK101]

---
## Champ lointain et relation de phase constante

* Une relation de phase constante entre l’intensité de champ électrique et l’intensité de champ magnétique n’apparaît qu’en champ lointain
* Le champ lointain proprement dit ne commence qu’à une distance de $4\cdot\lambda$
* Si la formule d’approximation du champ lointain est utilisée dans le champ proche rayonnant, cela donne une intensité de champ plus élevée et conservative
* Cela ne s’applique pas aux antennes magnétiques et aux antennes très courtes

---
### Transition du champ proche réactif au champ proche rayonnant

* La transition dépend de la longueur d’onde
* Condition remplie : $d > \frac{\lambda}{2\pi}$
* Exemple : Pour $\lambda = \qty{20}{\meter}$, la transition se situe à environ $d \approx \qty{3,18}{\meter}$

---
### Distances de protection des personnes en champ lointain

* En champ lointain, une formule d’approximation peut être appliquée pour calculer les distances de protection des personnes
* Formule : $d = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_{\textrm{EIRP}}}}{E}$
* Valable pour la plupart des formes d’antennes si la condition $d > \frac{\lambda}{2\pi}$ est remplie
* Cette formule n’est pas applicable pour les petites antennes ou les distances de sécurité en champ proche

---
[question:AK103]

## Définition du champ lointain

* En champ lointain, les vecteurs de l’intensité de champ électrique (E), de l’intensité de champ magnétique (H) et de la direction de propagation sont perpendiculaires les uns aux autres
* Il n’y a pas de différences de phase entre E et H
* L’impédance d’onde du champ correspond à celle de l’espace libre

---
### Limite entre champ proche et champ lointain

* La limite dépend principalement de la longueur d’onde
* Pour les antennes filaires (par ex. dipôles), le champ lointain se forme généralement à partir d’une distance d’environ $4\cdot\lambda$
* Condition de transition en champ proche : $d > \frac{\lambda}{2\pi}$ ; pour $\lambda = \qty{20}{\meter}$, cela donne environ $d \approx \qty{3,18}{\meter}$

---
### Application de la formule d’approximation du champ lointain

* La formule d’approximation $d = \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_{\textrm{EIRP}}}}{E}$ est valable pour la plupart des formes d’antennes
* Elle est appliquée lorsque la distance de sécurité calculée se situe dans le champ proche rayonnant ou en champ lointain
* La formule permet d’éviter des mesures ou simulations complexes pour déterminer les distances de protection des personnes

---
### Procédures d’évaluation selon la BEMFV

<left>
[photo:80:n_Bewertungsverfahren:Dans ce document sont décrites les procédures d’évaluation.]
</left>
<right>
Dans les [explications des procédures d’évaluation selon la BEMFV](https://50ohm.de/bemfv), l’Agence fédérale des réseaux (BNetzA) a décrit les termes et procédures pour la détermination des distances de sécurité.
</right>