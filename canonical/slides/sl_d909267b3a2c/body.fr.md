## Détection d'erreurs : bit de parité

* Un bit de parité supplémentaire est ajouté aux données
* Deux variantes :
* *Parité paire* : le nombre de bits à 1 est ajusté pour obtenir un nombre pair
* *Parité impaire* : le nombre de bits à 1 est ajusté pour obtenir un nombre impair
* L'émetteur et le récepteur doivent convenir du procédé utilisé

---

## Parité paire : exemple 1

<left>
[picture:677:byte:Un octet]
</left>
<right>
* Octet à transmettre
* On compte 5 bits à 1 → nombre impair
* Le bit de parité doit être mis à $\num{1}$ pour obtenir un nombre pair
</right>

---

<left>
[picture:678:even_parity:L'octet avec bit de parité paire]
</left>
<right>
* Le bit de parité a été mis à $\num{1}$
* L'octet résultant a un nombre pair de bits à 1
* En cas d'erreur de transmission, le bit de parité ne correspond plus
</right>

---

## Parité paire : exemple 2

<left>
[picture:679:even_parity:Octet avec bit de parité paire]
</left>
<right>
* Octet d'origine : 4 bits à 1 (pair)
* Le bit de parité est mis à $\num{0}$
</right>

---
## Détection d'erreurs en cas d'erreurs de bits

* En cas d'erreur sur un seul bit, la parité est inversée → erreur détectée
* En cas de deux erreurs, la parité reste inchangée → erreur non détectée
* En cas de trois erreurs, la parité change à nouveau → erreur détectée

---

[question:AE411]

---

[question:AE412]

---

## Détection d'erreurs avancée

* Des bits de parité supplémentaires permettent de détecter des erreurs sur plusieurs bits
* Pour des messages variables, on utilise souvent des méthodes de somme de contrôle comme le *contrôle de redondance cyclique (CRC)*
* Le CRC détecte les erreurs avec une certaine probabilité résiduelle

<note>
Utilisé pour l'IBAN ou les numéros de pièce d'identité
</note>

---

[question:AE410]