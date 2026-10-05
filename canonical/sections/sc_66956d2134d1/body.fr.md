La figure [ref:kanal] montre un émetteur et un récepteur connectés par un canal. Par exemple, des perturbations sur le canal peuvent survenir en raison des conditions météorologiques, d'autres influences atmosphériques ou des émissions d'autres stations. Celles-ci peuvent entraîner des erreurs lors de la transmission.

<margin>
[picture:674:kanal:Canal]
</margin>

Contrairement au codage de source, le codage de canal ajoute délibérément de la redondance à l'information à transmettre, par exemple des répétitions ou des sommes de contrôle. Contrairement à la redondance supprimée lors du codage de source, cette redondance ajoutée systématiquement peut être utilisée pour la détection ou la correction automatique des erreurs de transmission.

---

La figure [ref:kanalcodierer] montre un symbole pour un codeur de canal. Le bloc représente l'ajout de redondance aux données.

<margin>
[picture:676:kanalcodierer:Codeur de canal]
</margin>

[question:AE409]

Nous distinguons deux types de codage de canal :

* Détection d'erreurs : On peut détecter qu'une erreur s'est produite lors de la transmission, et demander par exemple une retransmission.
* Correction d'erreurs par anticipation (FEC) : Les erreurs survenant lors de la transmission sont corrigées au niveau du récepteur à l'aide de la redondance.

Dans les deux sections suivantes [sec:fehlererkennung] et [sec:fehlerkorrektur], nous allons examiner ces deux types plus en détail.