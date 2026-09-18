* Dans le domaine de la technique radio, on parle d’appareils fonctionnant à l’aide d’un traitement numérique du signal, appelés appareils SDR.
* *SDR* signifie *Software Defined Radio* (radio définie par logiciel).
* Dans ces appareils, au moins une partie du traitement du signal est réalisée par logiciel.
* Cela présente un avantage en termes de coût et offre une grande flexibilité.

---
[question:EF603]
---
## Convertisseur analogique-numérique

* Pour que les données puissent être traitées numériquement, elles doivent d’abord être numérisées.
* Pour cela, le signal analogique est converti en valeurs numériques à l’aide d’un convertisseur analogique-numérique (A/D).

---
<left>
* Le signal analogique est échantillonné à intervalles de temps fixes et représenté dans une plage de valeurs numériques (par exemple de $\num{-128}$ à $\num{+127}$).
* Les valeurs mesurées individuelles du signal sont appelées échantillons.
</left>
<right>
[picture:411:e_digitale_signalverarbeitung:Représentation simplifiée d’une onde sinusoïdale composée de $\num{16}$ échantillons et $\num{7}$ valeurs]
</right>
<note>
* Plus d’informations dans la classe A
</note>

---
[question:EF602]
---
## Convertisseur numérique-analogique

* Après le traitement numérique du signal, celui-ci est reconverti en signal analogique à l’aide d’un convertisseur numérique-analogique (D/A).

---
[question:EF601]