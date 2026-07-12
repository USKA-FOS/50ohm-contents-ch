## Détection d'erreur : Bit de parité

* Un bit de contrôle supplémentaire (bit de parité) est ajouté aux données
* Deux variantes :
* *Parité paire* : Le nombre de uns est fixé à un nombre pair
* *Parité impaire* : Le nombre de uns est fixé à un nombre impair
* L'émetteur et le récepteur doivent se mettre d'accord sur la méthode utilisée

---

## Parité paire : Exemple 1

<left>
[picture:677:byte:Un octet]
</left>
<right>
* Octet à transmettre
* 5 uns sont comptés → nombre impair
* Le bit de contrôle doit être défini sur $\num{1}$ pour obtenir un nombre pair
</right>

---

<left>
[picture:678:even_parity:L'octet avec le bit de parité paire]
</left>
<right>
* Le bit de contrôle a été défini sur $\num{1}$
* L'octet résultant a un nombre pair de uns
* En cas d'erreur de transmission, le bit de contrôle ne correspond plus
</right>

---

## Parité paire : Exemple 2

<left>
[picture:679:even_parity:Octet avec parité paire]
</left>
<right>
* Octet d'origine : 4 uns (pair)
* Le bit de contrôle est défini sur $\num{0}$
</right>

---
## Détection d'erreur en cas d'erreurs de bit

* En cas d'erreur sur un bit, la parité est inversée → l'erreur est détectée
* En cas de deux erreurs, la parité reste la même → l'erreur n'est pas détectée
* En cas de trois erreurs, la parité change à nouveau → l'erreur est détectée

---

[question:AE411]

---

[question:AE412]

---

## Détection d'erreur étendue

* Des bits de contrôle supplémentaires peuvent détecter les erreurs sur plusieurs bits
* Pour les messages variables, des procédures de somme de contrôle comme la *vérification de redondance cyclique (CRC)* sont souvent utilisées
* La CRC détecte les erreurs jusqu'à une certaine probabilité résiduelle

<note>
Utilisé pour l'IBAN ou les numéros de carte d'identité
</note>

---

[question:AE410]
