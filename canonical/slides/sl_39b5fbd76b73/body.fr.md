* L'intensité du signal d'un signal haute fréquence diminue avec l'augmentation de la longueur du câble
* Cela est appelé *atténuation du câble*
* Les connecteurs peuvent également atténuer le signal
* Ce phénomène est indésirable

---
<left>
* L'atténuation est généralement indiquée en décibels ($\unit{\dB}$)
* Lorsqu'on parle d'atténuation, le chiffre reste positif
</left>
<right>
* Utiliser le facteur de conversion en $\unit{\dB}$
* Ou consulter le recueil de formules
</right>
<note>
* Cela peut prêter à confusion, mais sans cela, les réponses aux examens seraient incorrectes
* Dans une évaluation globale des gains et des pertes, l'atténuation est cependant comptée négativement
</note>

---
[question:EG309]
---
[question:EG310]
---
[question:EG308]
---
## Pertes de câble

* Toutes les pertes qui se produisent dans les câbles
* L'antenne et l'amplificateur amplifient le signal, mais ne modifient pas les pertes de câble

---
[question:EG307]
---
## Diagramme d'atténuation du câble

<left>
* Annexe du recueil de formules
* Atténuations de différents câbles en fonction de la fréquence
* Référence à $\qty{100}{\meter}$ – pour des câbles plus courts, il faut convertir
</left>
<right>
[picture:202:e_kabeldaempfung_diagramm:Diagramme d'atténuation du câble dans le recueil de formules]
</right>
<note>
* éventuellement zoomer ici
</note>
---

[question:EG312]
---
### Méthode de résolution

* recherché : atténuation pour $\qty{100}{\meter}$ de câble RG58 à $\qty{145}{\mega\hertz}$
* Solution : lecture sur le diagramme
* Point d'intersection de la ligne RG58 avec $\qty{145}{\mega\hertz} \rightarrow \qty{20}{\dB}$

---
[question:EG311]
---
### Méthode de résolution

* recherché : atténuation pour $\qty{20}{\meter}$ avec une atténuation de $\qty{20}{\dB}$ sur $\qty{100}{\meter}$
* Solution : règle de trois

$\dfrac{\qty{20}{\dB}}{\qty{100}{\meter}} = \dfrac{x}{\qty{20}{\meter}}$
$x = \dfrac{\qty{20}{\dB} \cdot \qty{20}{\meter}}{\qty{100}{\meter}} = \qty{4}{\dB}$

---
[question:EG313]
---
### Méthode de résolution

* recherché : atténuation pour $\qty{15}{\meter}$ de câble RG58 à $\qty{145}{\mega\hertz}$
* Solution : lecture sur le diagramme et règle de trois
* Point d'intersection de la ligne RG58 avec $\qty{145}{\mega\hertz} \rightarrow \qty{20}{\dB}$

$\dfrac{\qty{20}{\dB}}{\qty{100}{\meter}} = \dfrac{x}{\qty{15}{\meter}}$
$x = \dfrac{\qty{20}{\dB} \cdot \qty{15}{\meter}}{\qty{100}{\meter}} = \qty{3}{\dB}$

---
[question:EG314]
---
[question:EG315]
---
[question:EG316]