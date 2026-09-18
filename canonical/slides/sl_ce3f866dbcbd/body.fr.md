[picture:438:a_oszillator_dds:schéma bloc de la synthèse numérique directe]

* Génération de signaux périodiques à bande limitée avec une haute résolution en fréquence
* Technique de pointe pour la génération de signaux
* La fréquence est réglable avec une grande précision
* La modulation de fréquence (FM) et de phase (PM) peut être générée directement

--- style="font-size: smaller;"
[picture:438:a_oszillator_dds:schéma bloc de la synthèse numérique directe]

* Un générateur d'horloge à fréquence fixe incrémente un compteur d'adresses
* En cas de dépassement, le compteur d'adresses redémarre depuis le début
* Une table de consultation de sinus fournit une valeur de sinus numérique prédéfinie
* Cette valeur est convertie en un signal analogique via un registre et un convertisseur numérique-analogique (DAC)

<note>
Le principe de fonctionnement n'est pas pertinent pour l'examen, seul le schéma bloc doit être reconnu
</note>

---
[question:AD620]