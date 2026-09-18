L'illustration [ref:kanal] montre un émetteur et un récepteur reliés par un canal. Des perturbations sur le canal peuvent survenir, par exemple en raison des conditions météorologiques, d'autres influences atmosphériques ou des émissions d'autres stations. Ces perturbations peuvent entraîner des erreurs de transmission.

<margin>
[picture:674:kanal:Kanal]
</margin>

Contrairement au codage de source, le codage de canal ajoute délibérément de la redondance à l'information à transmettre, par exemple des répétitions ou des sommes de contrôle. Contrairement à la redondance supprimée lors du codage de source, cette redondance ajoutée de manière systématique peut être utilisée pour détecter ou corriger automatiquement les erreurs de transmission.

---

L'illustration [ref:kanalcodierer] montre un symbole pour un codeur de canal. Le bloc représente l'ajout de redondance aux données.

<margin>
[picture:676:kanalcodierer:Kanalcodierer]
</margin>

[question:AE409]

Nous distinguons deux types de codage de canal :

* Détection d'erreurs : on peut détecter qu'une erreur s'est produite lors de la transmission, puis par exemple demander une retransmission.
* Correction d'erreurs sans voie de retour : les erreurs survenant lors de la transmission sont corrigées à l'aide de la redondance au niveau du récepteur.

Nous allons maintenant examiner ces deux types plus en détail.