--- data-transition="none"
## De la diode au transistor
<left>
On peut imaginer la fonction comme suit :
* Un canal de commande régule le débit d’un barrage
* Si aucun courant ne circule dans le canal de commande, le barrage est fermé
</left>
<right>
[picture:835:e_transistor_wehr_geschlossen:Le canal de commande ferme complètement le barrage]
</right>

--- data-transition="none"

## De la diode au transistor
<left>
On peut imaginer la fonction comme suit :
* Si un peu d’eau circule dans le canal de commande, le barrage s’ouvre à moitié
</left>
<right>
[picture:837:e_transistor_wehr_halb_offen:Le canal de commande ouvre le barrage à moitié]
</right>

--- data-transition="none"

## De la diode au transistor
<left>
On peut imaginer la fonction comme suit :
* Si davantage d’eau circule dans le canal de commande, le barrage s’ouvre complètement
</left>
<right>
[picture:836:e_transistor_wehr_geoeffnet:Le canal de commande ouvre complètement le barrage]
</right>

---

[question:EC602]

---

[question:EC608]

---

### Transistor bipolaire et schéma de câblage

<left>
Astuce pour le PNP → Flèche vers la plaque
</left>
<right>
[picture:374:e_schaltbild_npn_transistor:Schéma de câblage du transistor NPN]
[picture:375:e_schaltbild_pnp_transistor:Schéma de câblage du transistor PNP]
</right>

---

[question:EC607]

---

[question:EC606]

---

[question:EC605]

---

[question:EC609]

---

### Interrupteur ou amplificateur ?
* La commande peut être réglée de manière à ce que le transistor soit bloqué ou complètement conducteur : on parle alors de transistor de commutation.
* La commande peut être réglée de manière à ce que le transistor soit contrôlé de façon progressive : on parle alors d’amplificateur.

---

[question:EC601]

---
[question:EC603]

---

## Tension de commande et sa polarité
Selon le type de transistor bipolaire, les polarités diffèrent.

* Pour un transistor NPN, une tension de commande positive est nécessaire pour le rendre conducteur.
* Pour un transistor PNP, une tension de commande négative est nécessaire pour le rendre conducteur.

La tension de commande, comme pour une diode au silicium, est d’environ $\qty{0,6}{\volt}$.

---

[question:EC610]

---

Comme le courant de collecteur et le courant de base circulent à travers le transistor, le courant le plus élevé passe par la broche d’émetteur.

---

[question:EC611]

--- style="font-size: smaller;"

### Quand le transistor NPN devient-il conducteur ?
La tension base-émetteur est-elle suffisante et se trouve-t-elle à un potentiel positif ?
Il faut ici faire attention aux signes et adapter sa réflexion en cas de valeurs négatives, exemples :

* Base $\qty{+2}{\volt}$ et émetteur $\qty{+1,4}{\volt} \rightarrow$ La tension base-émetteur est positive et s’élève à $\qty{+0,6}{\volt}$
* Base $\qty{-5,6}{\volt}$ et émetteur $\qty{-6,2}{\volt} \rightarrow$ La tension base-émetteur est positive et s’élève à $\qty{+0,6}{\volt}$

---

On peut le déterminer intuitivement ou par calcul (en tenant compte des signes).

$U_{ BE } = U_{ B } - U_{ E }$

---

[question:EC612]

---

[question:EC613]

--- style="font-size: smaller;"

### Quand le transistor PNP devient-il conducteur ?
La tension base-émetteur est-elle suffisante et se trouve-t-elle à un potentiel négatif ?
Il faut ici faire attention aux signes et adapter sa réflexion en cas de valeurs négatives, exemples :

* Base $\qty{+5,6}{\volt}$ et émetteur $\qty{+6,2}{\volt} \rightarrow$ La tension base-émetteur est négative et s’élève à $\qty{-0,6}{\volt}$
* Base $\qty{-2}{\volt}$ et émetteur $\qty{-1,4}{\volt} \rightarrow$ La tension base-émetteur est négative et s’élève à $\qty{-0,6}{\volt}$

---

On peut le déterminer intuitivement ou par calcul (en tenant compte des signes).

$U_{ BE } = U_{ B } - U_{ E }$

---

[question:EC614]

---

[question:EC615]

---

## Types de transistors
Les transistors traités jusqu’ici sont appelés *transistors bipolaires*. Il s’agit du type de transistors qui, dans les années 1950, a révolutionné la technique et remplacé les tubes électroniques. Contrairement aux transistors bipolaires commandés par le courant, les *transistors à effet de champ (FET)* sont commandés par la tension : aucun courant de commande ne circule donc dans le transistor. Nous aborderons ces derniers plus en détail dans le cours de classe A.

---

[question:EC604]