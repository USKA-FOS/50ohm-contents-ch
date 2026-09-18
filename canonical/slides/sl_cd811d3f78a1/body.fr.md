## Application

<left>
* Une diode ne laisse passer le courant que dans un seul sens
* Dans l’autre sens, elle se comporte comme une résistance élevée
* Les diodes sont notamment utilisées pour redresser une tension alternative
</left>
<right>
[picture:689:e_led:Diverses LED sous différentes formes et couleurs]
</right>
<note>
* Une forme particulière nous est déjà connue sous le nom de LED
</note>

---
[question:EC501]
---
[question:EC502]
---

## Tension de seuil

<left>
* Pour qu’une diode conduise en polarisation directe, une certaine tension – la tension de seuil ou tension directe – doit être dépassée
* Selon la base de l’élément chimique, la tension de seuil varie
</left>
<right>
* Germanium : $\qtyrange{0,2}{0,4}{\volt}$
* Silicium : $\qtyrange{0,6}{0,8}{\volt}$
* LED (rouge) : $\qtyrange{1,6}{2,2}{\volt}$
* LED (jaune, vert) : $\qtyrange{1,9}{2,5}{\volt}$
* LED (bleu, blanc) : $\qtyrange{2,7}{3,5}{\volt}$
</right>

---
[question:EC503]
---

## Diode Schottky

* Permet une fréquence de commutation élevée
* Nécessite une très faible tension de seuil, comprise entre $\qty{0,4}{\volt}$ et moins de $\qty{0,1}{\volt}$

---
[question:EC504]
---

## Caractéristiques

---
[question:EC506]
---
[question:EC507]
---
[question:EC508]
---
[question:EC505]
---

## Diode passante

<left>
* Une diode conduit toujours lorsque la tension à l’anode est plus positive que celle à la cathode d’une valeur égale à la tension de seuil
* Cela s’applique également aux tensions négatives
* À l’examen, seules les diodes au silicium avec une tension de seuil de $\qty{0,7}{\volt}$ sont considérées
</left>
<right>
[picture:113:e_leitende_siliziumdiode:Tensions aux bornes d’une diode au silicium passante]
</right>

---
[question:EC513]
---
[question:EC510]
---
[question:EC509]
---
[question:EC511]
---
[question:EC512]
---

## Application de la LED

<left>
* Une LED sert d’indicateur lumineux
</left>
<right>
[picture:324:e_led_schaltung:LED avec résistance en série]
</right>

---
[question:EC514]
---
### Résistance en série

<left>
* Comme la LED elle-même présente une résistance quasi nulle, elle se comporterait comme un court-circuit si elle était directement connectée à une source de tension
* Une résistance en série limite le courant de conduction
</left>
<right>
[picture:324:e_led_schaltung:LED avec résistance en série]
</right>

---
* Calcul : $R = \dfrac{U_q - U_{\mathrm{LED}}}{I_D}$
* $U_q$ : source de tension
* $U_{\mathrm{LED}}$ : tension de seuil de la LED
* $I_D$ : courant de conduction

---
[question:EC515]
---
[question:EC516]
---

## Diode Zener

<left>
* Normalement, la tension inverse maximale d’une diode est d’environ $\qty{1000}{\volt}$
* Pour les diodes Zener, un claquage en tension inverse se produit, selon le modèle, entre $\qty{3}{\volt}$ et $\qty{100}{\volt}$
* Elles servent à la stabilisation de tension
</left>
<right>
[picture:560:_e_z_diode:symbole de circuit diode Zener]
</right>
<note>
* Autrefois nommée d’après Clarence Melvin Zener
* Aujourd’hui, d’autres effets sont déterminants, mais le terme diode Zener est resté
</note>

---
### Polarisation

<left>
* Les diodes Zener sont utilisées avec une résistance en série en polarisation inverse
</left>
<right>
[picture:549:e_z_diode_polung:Diode Zener correctement polarisée en inverse]
</right>

---
[question:EC517]
---
[question:EC518]
---
[question:EC519]
---
[question:EC520]
---

### Résistance en série

<left>
[picture:753:e_z_diode_spannungsstabilisierung:Diode Zener pour stabilisation de tension]
</left>
<right>
* $U_Z$ est la tension à laquelle la diode Zener stabilise
* $U_V = U_1 - U_Z = \qty{13,8}{\volt} - \qty{5}{\volt} = \qty{8,8}{\volt}$
* $R_V = \frac{U_V}{I} = \frac{\qty{8,8}{\volt}}{\qty{30}{\milli\ampere}} \approx \qty{293}{\ohm}$
</right>
---
[question:EC521]
---
[question:EC522]

<note>
* Les courants dans la résistance en série s’additionnent
* Les règles de Kirchhoff n’ont pas encore été abordées
</note>