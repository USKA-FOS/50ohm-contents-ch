<left>
[picture:1058:a_vsource_schematic:Ersatzschaltbild Stromquelle $R_i$ hochohmig]
</left>
<right>
* Fournit un courant constant
* Indépendant de la charge connectée
* Théorie : Résistance interne infinie
* Pratique : Résistance interne très élevée
</right>

---

### Application d'une source de courant

* Alimentations de laboratoire
* Technologie de charge des accumulateurs

<note>
Les alimentations de laboratoire seront traitées plus en détail dans la section suivante
</note>

### Source de tension
<left>
[picture:1018:a_vsource_schematic:Ersatzschaltbild Spannungsquelle]
</left>
<right>
* Une source de tension réelle est chargée avec $R_L$ $\rightarrow$ la tension de sortie $U_k$ diminue
* La cause est la résistance interne
* Sans charge / en circuit ouvert : $U_q = U_L$
</right>
<note>
</note>

---
### Résistance interne

<left>
* Non mesurable avec un multimètre
* Déterminée par calcul : <br/>$R_i = \frac{\Delta U}{\Delta I}$
</left>
<right>
* Circuit ouvert : $I = \qty{0}{\ampere}$
* Charge avec $R_L$ : <br/>$I_L = \frac{U_L}{R_L}$
</right>

---
### Résistance interne de la source de tension

$(\Delta U = \qty{0}{\volt})$;  $R_i = \frac{\Delta U}{\Delta I} = \frac{0}{x} = \qty{0}{\ohm}$

<fragment>
Les sources de tension idéales doivent avoir une résistance interne très faible $R_i \ll R_L$

Cas idéal : $\qty{0}{\ohm}$, alors la tension de sortie reste inchangée sous charge.
</fragment>

---

### Limitation de courant

* Intégré dans les alimentations de laboratoire
* Le courant de charge dépasse une intensité de courant maximale
* $\rightarrow$ la tension de sortie est réduite
* $\rightarrow$ le courant de charge reste constant
* Fonction de la source de courant constant

---
### Résistance interne de la source de courant

$R_i = \frac{\Delta U}{\Delta I}$; $(\Delta I \to \qty{0}{\ampere})$;  $R_i = \frac{\Delta U}{\Delta I} \to \qty{\infty}{\ohm}$

<fragment>
Les sources de courant idéales doivent avoir une résistance interne très élevée $R_i \gg R_L$.

Cas idéal : $\qty{\infty}{\ohm}$, alors le courant de charge reste constant lorsque la résistance de charge change, c'est pourquoi on parle aussi d'adaptation de courant.
</fragment>

---
[question:AB201]
---
### Adaptation de puissance

* Transmission optimale de puissance de l'émetteur à l'antenne
* $R_i = R_L$

--- style="font-size: 0.7em;"

|c: Résumé de la résistance interne | c: Résistance interne |
| Adaptation de tension pour une source de tension constante| $R_i$ est très faible; théoriquement $\qty{0}{\ohm}$; $R_i \ll R_L$ identique à $R_L \gg R_i$|
|Adaptation de courant pour une source de courant constant|$R_i$ est très élevé; $R_i \gg R_L$ identique à $R_L \ll R_i$ |
| Adaptation de puissance pour les amplificateurs| $R_L = R_i$|
[table:a_Innenwiderstand Zusammenfassung:Résumé de la résistance interne]

---
[question:AG401]
---
[question:AB202]
---
[question:AB203]
---
[question:AB204]
---
[question:AB207]
---
#### Solution
* donné : $U_0 = \qty{13,5}{\volt}$
* donné : $U_{Kl} = \qty{13}{\volt}$
* donné : $I = \qty{2}{\ampere}$
* recherché : $R_i$

<fragment>
$R_i = \frac{U_i}{I} = \frac{U_0-U_{Kl}}{I} = \frac{\qty{13,5}{\volt} - \qty{13}{\volt}}{\qty{2}{\ampere}} = \qty{0,25}{\ohm}$
</fragment>
---
[question:AB208]
---
#### Solution
* donné : $U_0 = \qty{13,8}{\volt}$
* donné : $U_{Kl} = \qty{13,6}{\volt}$
* donné : $I = \qty{20}{\ampere}$
* recherché : $R_i$

<fragment>
$R_i = \frac{U_i}{I} = \frac{U_0-U_{Kl}}{I} = \frac{\qty{13,8}{\volt} - \qty{13,6}{\volt}}{\qty{20}{\ampere}} = \qty{10}{\milli\ohm}$
</fragment>
---
[question:AB206]
---
#### Solution
* donné : $U_0 = \qty{13,5}{\volt}$
* donné : $U_{Kl} = \qty{12,4}{\volt}$
* donné : $I = \qty{0,9}{\ampere}$
* recherché : $R_i$

<fragment>
$R_i = \frac{U_i}{I} = \frac{U_0-U_{Kl}}{I} = \frac{\qty{13,5}{\volt} - \qty{12,4}{\volt}}{\qty{0,9}{\ampere}} = \qty{1,22}{\ohm}$
</fragment>
---
[question:AB205]
---
#### Solution
* donné : $U_0 = \qty{5,0}{\volt}$
* donné : $U_{Kl} = \qty{4,8}{\volt}$
* donné : $R_L = \qty{1,2}{\ohm}$
* recherché : $R_i$

<fragment>
$I = \frac{U_{Kl}}{R_L} = \frac{\qty{4,8}{\volt}}{\qty{1,2}{\ohm}} = \qty{4}{\ampere}$
</fragment>
<fragment>
$R_i = \frac{U_i}{I} = \frac{U_0 - U_{Kl}}{I} = \frac{\qty{5,0}{\volt} - \qty{4,8}{\volt}}{\qty{4}{\ampere}} = \qty{0,05}{\ohm}$
</fragment>

