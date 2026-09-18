<left>
[photo:212:a_oszilloskop:Oscilloscope numérique]
</left>
<right>
* Affiche l’évolution temporelle des tensions
* Mesure la forme du signal
</right>
---
[question:AI301]
---
[question:AI304]
---
### Largeur d’impulsion

<left>
[picture:1005:a_impulsbreite:Détermination de la largeur d’impulsion d’un signal rectangulaire non idéal]
</left>
<right>
Définition : la largeur d’impulsion est mesurée à 50 % de la valeur de crête
</right>
---
[question:AI303]
---
### Trigger

<left>
[photo:219:a_oszilloskop_x-ablenkung:Sans tension d’entrée, sur un oscilloscope analogique, seul un point se déplace de gauche à droite à l’écran, ici à une vitesse d’un carreau par seconde.]
</left>
<right>
* Le trigger analyse le signal appliqué
* Par exemple, le passage de la tension 0 de négatif à positif
* Cela permet d’afficher une image stable d’une onde
</right>
---
[question:AI302]
---
### Pointes de mesure

<left>
[photo:223:a_oszilloskop_tastkoepfe:Pointes de mesure avec différentes pointes de touche. Les pinces crocodiles ont été retirées pour cette photo.]
</left>
<right>
* Pour mesurer la tension
* Pointe en forme de crochet ou d’aiguille
* Masse de référence généralement via une pince crocodile séparée
* Les pointes 10:1 divisent la tension par dix
</right>
---
### Mesure avec un oscilloscope

[photo:224:a_oszilloskop_messung:Mesure avec une pointe de mesure. Entre les diodes D1 et D2, on voit la pointe de touche et plus à gauche la pince crocodile pour la connexion de masse.]
---
[question:AI305]
---
### Méthode de résolution
* donné : $R=\qty{50}{\ohm}$
* donné : (d’après la représentation) $\hat{U} = \qty{100}{\volt}$
* recherché : $P_{\textrm{PEP}}$

<fragment>
$\begin{split} P_{\textrm{PEP}} &= \frac{U_{\textrm{eff}}^2}{R} = \frac{\left(\frac{\qty{100}{\volt}}{\sqrt{2}}\right)^2}{\qty{50}{\ohm}}\\n&=\frac{\frac{(\qty{100}{\volt})^2}{2}}{\qty{50}{\ohm}} = \frac{\qty{5000}{\volt}^2}{\qty{50}{\ohm}} = \qty{100}{\watt} \end{split}$
</fragment>
---
[question:AI306]
---
### Méthode de résolution
* donné : $R=\qty{50}{\ohm}$
* donné : (d’après la représentation avec une pointe 10:1) $\hat{U} = \qty{6}{\volt}\cdot 10$
* recherché : $P_{\textrm{PEP}}$

<fragment>
$\begin{split} P_{\textrm{PEP}} &= \frac{U_{\textrm{eff}}^2}{R} = \frac{\left(\frac{\qty{6}{\volt}\cdot 10}{\sqrt{2}}\right)^2}{\qty{50}{\ohm}}\\n&=\frac{\frac{(\qty{60}{\volt})^2}{2}}{\qty{50}{\ohm}} = \qty{36}{\watt} \end{split}$
</fragment>

---
## Impulsion

<left>
* Un signal passe d’une valeur à une valeur supérieure, puis revient à une valeur inférieure à un instant ultérieur
* La durée de l’impulsion est mesurée du milieu du front montant au milieu du front descendant
</left>
<right>
[picture:57:e_impuls:Impulsion sur un oscilloscope] 
</right>
---
[question:EI303]