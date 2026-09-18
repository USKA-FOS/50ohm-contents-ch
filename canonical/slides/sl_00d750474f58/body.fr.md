### Principe du transformateur

<left>
[photo:239:e_Trafo mit getrennten Wicklungen:Trafo avec enroulements séparés]
</left>
<right>
* Bobines couplées magnétiquement
* Courant variable dans une bobine
* Génère une tension dans l'autre bobine
* $\rightarrow$ Induction mutuelle
</right>

---
[question:AC301]
--- style="font-size: 0.7em;"
Le rapport des spires entre le côté primaire et secondaire est égal au rapport des tensions entre le primaire et le secondaire, mais inversement proportionnel au rapport des intensités entre le secondaire et le primaire :

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S} = \frac{I_S}{I_P}$

<fragment>
Le rapport de l'impédance primaire à l'impédance secondaire est égal au carré des rapports ci-dessus :

$ü^2 = \frac{Z_P}{Z_S} = \left(\frac{N_P}{N_S}\right)^2 = \left(\frac{U_P}{U_S}\right)^2 = \left(\frac{I_S}{I_P}\right)^2$
</fragment>

<fragment>
Ou, en extrayant la racine carrée :

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S} = \frac{I_S}{I_P} = \sqrt{\frac{Z_P}{Z_S}}$
</fragment>

<note>
La dernière formule est celle indiquée dans le recueil de formules
</note>
---
[question:AC302]
---
#### Méthode de résolution
* donné : $U_P = \qty{230}{\volt}$
* donné : $U_S = \qty{6}{\volt}$
* donné : $I_S = \qty{1,15}{\ampere}$
* recherché : $I_P$

<fragment>
$\begin{split} \frac{U_P}{U_S} &= \frac{I_S}{I_P} \\ \Rightarrow I_P &= \frac{I_S \cdot U_S}{U_P} = \frac{\qty{1,15}{\ampere} \cdot \qty{6}{\volt}}{\qty{230}{\volt}} \\ &= \qty{30}{\milli\ampere} \end{split}$
</fragment>

---
## Adaptation d'impédance

<left>
[picture:260:a_impedanzanpassung:Adaptation de $\qty{2450}{\ohm}$ à $\qty{50}{\ohm}$ avec un transformateur présentant un rapport de spires de 1 à 7]
</left>
<right>
[photo:332:a_unun:Exemple d'un transformateur Unun avec un rapport de spires de 2 à 14, où les côtés primaire et secondaire sont enroulés ensemble de manière bifilaire (toronnée)]
</right>

---
[question:AC306]
---
#### Méthode de résolution
* donné : $Z_P = \qty{50}{\ohm}$
* donné : $Z_S = \qty{2,5}{\kilo\ohm}$
* recherché : $ü$

<fragment>
$\begin{split} ü &= \sqrt{\frac{Z_P}{Z_S}} = \sqrt{\frac{\qty{50}{\ohm}}{\qty{2,5}{\kilo\ohm}}} \\ &= \sqrt{\frac{1}{50}} \approx \frac{1}{7} \end{split}$
</fragment>

---
[question:AC303]
---
#### Méthode de résolution
* donné : $Z_S = \qty{16}{\kilo\ohm}$
* donné : $ü = \frac{1}{4}$
* recherché : $Z_P$

<fragment>
$\begin{split} ü &= \sqrt{\frac{Z_P}{Z_S}} \\ \Rightarrow Z_P &= ü^2 \cdot Z_S = \frac{1^2}{4^2} \cdot \qty{16}{\kilo\ohm} \\ &= \frac{\qty{16}{\kilo\ohm}}{16} = \qty{1}{\kilo\ohm} \end{split}$
</fragment>

---
[question:AC304]
---
#### Méthode de résolution
* donné : $Z_S = \qty{6,4}{\kilo\ohm}$
* donné : $ü = \frac{1}{4}$
* recherché : $Z_P$

<fragment>
$\begin{split} ü &= \sqrt{\frac{Z_P}{Z_S}} \\ \Rightarrow Z_P &= ü^2 \cdot Z_S = \frac{1^2}{4^2} \cdot \qty{6,4}{\kilo\ohm} \\ &= \frac{\qty{6,4}{\kilo\ohm}}{16} = \qty{0,4}{\kilo\ohm} \end{split}$
</fragment>

---
[question:AC305]
---
#### Méthode de résolution
* donné : $Z_P = \qty{450}{\ohm}$
* donné : $Z_S = \qty{50}{\ohm}$
* recherché : $ü$

<fragment>
$\begin{split} ü &= \sqrt{\frac{Z_P}{Z_S}} = \sqrt{\frac{\qty{450}{\ohm}}{\qty{50}{\ohm}}} \\ &= \sqrt{\frac{9}{1}} = \frac{3}{1} \end{split}$
</fragment>


---
### Courant maximal
<left>
* Le câble ne doit pas surchauffer
* Sinon, l'isolation fond
* Ou le conducteur rougit
* $\rightarrow$ densité de courant admissible en fonction de la section du conducteur
</left>
<right>
<fragment>
[photo:236:e_HF Übertrager:Transformateur HF (balun), qui peut fondre en cas de puissance excessive]
</fragment>
</right>
<note>
Les baluns artisanaux fondus dans des boîtiers en plastique sont fréquents lorsque l'on ajoute "juste un peu plus de puissance"
</note>

---
### Exemples de densité de courant admissible

selon VDE

* Conducteurs en cuivre posés librement : $\frac{\qty{12}{\ampere}}{\qty{0,75}{\milli\meter\squared}}$
* Fusibles : jusqu'à $\qty{3000}{\ampere\per\milli\meter\squared}$
* Transformateurs : $\qty{2,5}{\ampere\per\milli\meter\squared}$ (mauvaise dissipation thermique des enroulements)

---
[question:AC307]
---
#### Méthode de résolution
* donné : $d = \qty{0,5}{\milli\meter}$
* donné : densité de courant $\frac{I}{A} = \frac{\qty{2,5}{\ampere}}{\qty{1}{\milli\meter\squared}}$
* recherché : $I_{\mathrm{max}}$

<fragment>
$A_{Dr} = \frac{d^2 \cdot \pi}{4} = \frac{(\qty{0,5}{\milli\meter})^2 \cdot \pi}{4} \approx \qty{0,196}{\milli\meter\squared}$
</fragment>
<fragment>
$I_{\mathrm{max}} = \frac{I}{A} \cdot A_{Dr} = \frac{\qty{2,5}{\ampere}}{\qty{1}{\milli\meter\squared}} \cdot \qty{0,196}{\milli\meter\squared} = \qty{0,49}{\ampere}$
</fragment>
