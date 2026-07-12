La figure [ref:kanal] montre un émetteur et un récepteur reliés par un canal. Par exemple, en raison du temps, d'autres influences atmosphériques ou d'émissions d'autres stations, des perturbations peuvent survenir sur le canal. Celles-ci peuvent entraîner des erreurs lors de la transmission.

<margin>
[picture:674:kanal:Kanal]
</margin>

Contrairement au codage de source, le codage de canal ajoute délibérément de la redondance aux informations à transmettre, par exemple des répétitions ou des sommes de contrôle. Contrairement à la redondance supprimée lors du codage de source, cette redondance ajoutée systématiquement peut être utilisée pour la détection ou la correction automatique des erreurs de transmission.

---

La figure [ref:kanalcodierer] montre un symbole pour un codeur de canal. Le bloc représente l'ajout de redondance aux données.

<margin>
[picture:676:kanalcodierer:Kanalcodierer]
</margin>

[question:AE409]

Nous distinguons deux types de codage de canal:

* Détection d'erreur: On peut détecter qu'une erreur s'est produite lors de la transmission, puis demander par exemple une nouvelle transmission.
* Correction d'erreur sans retour: Les erreurs qui surviennent lors de la transmission sont corrigées à l'aide de la redondance par le récepteur.

Nous allons examiner de plus près ces deux types ci-dessous.