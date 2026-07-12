--- data-transition="none"
## De la diode au transistor
<left>
La fonction peut être imaginée comme suit:
* Au moyen d'un canal de commande, le débit d'un barrage est régulé
* Si aucun courant ne circule dans le canal de commande, le barrage est fermé
</left>
<right>
[picture:835:e_transistor_wehr_geschlossen:Canal de commande ferme le barrage complètement]
</right>

--- data-transition="none"

## De la diode au transistor
<left>
La fonction peut être imaginée comme suit:
* Si un peu d'eau circule dans le canal de commande, le barrage s'ouvre à moitié
</left>
<right>
[picture:837:e_transistor_wehr_halb_offen:Canal de commande ouvre le barrage à moitié]
</right>

--- data-transition="none"

## De la diode au transistor
<left>
La fonction peut être imaginée comme suit:
* Si plus d'eau circule dans le canal de commande, le barrage est complètement ouvert
</left>
<right>
[picture:836:e_transistor_wehr_geoeffnet:Canal de commande ouvre le barrage complètement]
</right>

---

[question:EC602]

---

[question:EC608]

---

### Transistor bipolaire et schéma

<left>
Règle mnémotechnique pour PNP $\rightarrow$ Flèche vers la plaque
</left>
<right>
[picture:374:e_schaltbild_npn_transistor:Schéma du transistor NPN]
[picture:375:e_schaltbild_pnp_transistor:Schéma du transistor PNP]
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

### Interrupteur ou amplificateur?
* Le pilotage peut être réglé de manière à ce que le transistor soit bloqué ou complètement conducteur, on parle alors d'un transistor de commutation.
* Le pilotage peut être réglé de manière à ce que le transistor soit commandé de manière progressive, on parle alors d'un amplificateur.

---

[question:EC601]

---
[question:EC603]

---

## Tension de commande et sa polarité
Selon le type de transistor bipolaire, on a différentes polarités.

* Pour un transistor NPN, on a besoin d'une tension de commande positive pour la conduction.
* Pour un transistor PNP, on a besoin d'une tension de commande négative pour la conduction.

La tension de commande est d'environ $\qty{0,6}{\volt}$ comme pour une diode au silicium.

---

[question:EC610]

---

Comme le courant de collecteur et le courant de base traversent le transistor, le courant le plus important traverse la borne d'émetteur.

---

[question:EC611]

--- style="font-size: smaller;"

### Quand le transistor NPN conduit-il?
La tension base-émetteur est-elle suffisante et positive?
Il faut faire attention aux signes et repenser en cas de signes négatifs, exemples:

* Base $\qty{+2}{\volt}$ et Émetteur $\qty{+1,4}{\volt} \rightarrow$ La tension base-émetteur est positive et vaut $\qty{+0,6}{\volt}$
* Base $\qty{-5,6}{\volt}$ et Émetteur $\qty{-6,2}{\volt} \rightarrow$ La tension base-émetteur est positive et vaut $\qty{+0,6}{\volt}$

---

Soit on le comprend intuitivement, soit on le calcule (en tenant compte des signes).

$U_{ BE } = U_{ B } - U_{ E }$

---

[question:EC612]

---

[question:EC613]

--- style="font-size: smaller;"

### Quand le transistor PNP conduit-il?
La tension base-émetteur est-elle suffisante et négative?
Il faut faire attention aux signes et repenser en cas de signes négatifs, exemples:

* Base $\qty{+5,6}{\volt}$ et Émetteur $\qty{+6,2}{\volt} \rightarrow$ La tension base-émetteur est négative et vaut $\qty{-0,6}{\volt}$
* Base $\qty{-2}{\volt}$ et Émetteur $\qty{-1,4}{\volt} \rightarrow$ La tension base-émetteur est négative et vaut $\qty{-0,6}{\volt}$

---

Soit on le comprend intuitivement, soit on le calcule (en tenant compte des signes).

$U_{ BE } = U_{ B } - U_{ E }$

---

[question:EC614]

---

[question:EC615]

---

## Types de transistors
Les transistors traités jusqu'à présent sont appelés *transistors bipolaires*. Ce sont les types de transistors qui ont déclenché une révolution technique dans les années 50 et ont remplacé les tubes électroniques. Contrairement aux transistors bipolaires commandés par le courant, les *transistors à effet de champ (FET)* sont commandés par la tension, donc aucun courant de commande ne les traverse. Nous nous occuperons plus intensivement de ceux-ci dans le cours de classe A.

---

[question:EC604]