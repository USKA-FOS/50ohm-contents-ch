## Application

<left>
* Une diode ne permet le passage du courant que dans un sens
* Dans l'autre sens, elle agit comme une résistance élevée
* Les diodes sont utilisées, entre autres, pour redresser la tension alternative
</left>
<right>
[picture:689:e_led:Diverse LED in verschiedenen Bauformen und Farben]
</right>
<note>
* Nous avons déjà connu une forme de construction particulière sous le nom de LED
</note>

---
[question:EC501]
---
[question:EC502]
---

## Tension de seuil

<left>
* Pour qu'une diode conduise dans le sens passant, une tension déterminée - la tension de seuil ou tension de passage - doit être dépassée
* Selon la base de l'élément chimique, la tension de seuil est plus ou moins élevée
</left>
<right>
* Germanium : $\qtyrange{0,2}{0,4}{\volt}$
* Silicium : $\qtyrange{0,6}{0,8}{\volt}$
* LED (Rouge) : $\qtyrange{1,6}{2,2}{\volt}$
* LED (Jaune, Vert) : $\qtyrange{1,9}{2,5}{\volt}$
* LED (Bleu, Blanc) : $\qtyrange{2,7}{3,5}{\volt}$
</right>

---
[question:EC503]
---

## Diode Schottky

* Permet une fréquence de commutation élevée
* Une tension de seuil très faible de $\qty{0,4}{\volt}$ à moins de $\qty{0,1}{\volt}$ est nécessaire

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

## Diode conductrice

<left>
* Une diode conduit toujours lorsque la tension à l'anode est plus positive que celle à la cathode de la tension de seuil
* Valable également pour les tensions négatives
* Dans l'examen, seules les diodes au silicium avec une tension de seuil de $\qty{0,7}{\volt}$ sont présentes
</left>
<right>
[picture:113:e_leitende_siliziumdiode:Spannungen an einer leitenden Siliziumdiode]
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

## Application des LED

<left>
* Une LED sert d'indicateur lumineux
</left>
<right>
[picture:324:e_led_schaltung:LED mit Vorwiderstand]
</right>

---
[question:EC514]
---
### Résistance en série

<left>
* Comme la LED elle-même a peu de résistance, elle agirait comme un court-circuit en cas de connexion directe à une source de tension
* Avec une résistance en série, le courant de passage est limité
</left>
<right>
[picture:324:e_led_schaltung:LED mit Vorwiderstand]
</right>

---
* Calcul : $R = \dfrac{U_q - U_{\mathrm{LED}}}{I_D}$
* $U_q$ : source de tension
* $U_{\mathrm{LED}}$ : tension de seuil de la LED
* $I_D$ : courant de passage

---
[question:EC515]
---
[question:EC516]
---

## Diode Zener

<left>
* Normalement, la tension inverse maximale d'une diode est d'environ $\qty{1000}{\volt}$
* Dans le cas des diodes Zener, une rupture de tension se produit selon le type de construction entre $\qty{3}{\volt}$ et $\qty{100}{\volt}$
* Servent à la stabilisation de la tension
</left>
<right>
[picture:560:_e_z_diode:Schaltzeichen Z-Diode]
</right>
<note>
* Autrefois nommée d'après Clarence Melvin Zener
* Aujourd'hui, d'autres effets sont déterminants, mais la diode Zener est restée comme nom
</note>

---
### Polarisation

<left>
* Les diodes Zener sont utilisées avec une résistance en série dans le sens bloquant
</left>
<right>
[picture:549:e_z_diode_polung:Z-Diode korrekt in Sperrichtung eingesetzt]
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
[picture:753:e_z_diode_spannungsstabilisierung:Z-Diode zur Spannungsstabilisierung]
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
* Les courants à la résistance en série s'additionnent
* Les règles de Kirchhoff n'étaient pas encore un sujet
</note>