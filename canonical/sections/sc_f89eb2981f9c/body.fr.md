Les radioamateurs sont légalement tenus de respecter certaines limites de puissance pour leurs installations radio. La puissance de sortie de l'émetteur est particulièrement importante, ainsi que l'évitement des émissions non désirées – nous aborderons ces dernières dans les sections [sec:unerwuenschte_aussendungen_1], [sec:unerwuenschte_aussendungen_2] et [sec:unerwuenschte_aussendungen_3]. Dans cette section, nous nous intéressons d'abord à la puissance de sortie de l'émetteur.

Dans de nombreuses bandes de radioamateurisme, attribuées principalement au radioamateurisme, la puissance de sortie maximale de l'émetteur – en anglais Peak Envelope Power (abrégé PEP) – est la limite de référence. Les prescriptions de puissance exactes se trouvent dans l'[ordonnance de l'OFCOM sur l'utilisation du spectre des fréquences de radiocommunication (OOUS)](https://www.bakom.admin.ch/dam/de/sd-web/oW59XCrgOEpK/20251028_Hilfstabellen%20en.pdf) sur le site web de l'OFCOM.

---

Comme le montre la figure [ref:e_senderausgangsleisung], la puissance de sortie d'un émetteur est toujours mesurée directement à la sortie de l'émetteur – sans qu'aucun appareil supplémentaire, filtre ou câble ne soit intercalé. Pour déterminer la puissance d'un émetteur BLU, il doit être exploité avec une modulation appropriée à amplitude constante. Une méthode simple consiste à injecter un signal à un seul ton, par exemple en appuyant sur la clé Morse en mode CW ; une excitation à deux tons est cependant encore meilleure. Une mesure avec la parole est inadaptée, car la puissance de sortie y fluctue fortement.

<margin>
[picture:916:e_senderausgangsleisung:Mesure de la puissance de sortie de l'émetteur]
</margin>

<indepth>
Un *signal à deux tons* est idéal pour la mesure de puissance et de linéarité d'un émetteur BLU, car il contient deux sinusoïdes pures d'amplitude constante. Cela génère dans l'émetteur exactement les produits d'intermodulation typiques des signaux vocaux réels, mais sous une forme clairement définie et reproductible.
</indepth>


[question:EF401]
[question:EF402]

---

La PEP décrit la puissance de crête de l'émetteur dans des conditions de fonctionnement normales : c'est la puissance que l'émetteur peut fournir en moyenne à une résistance de terminaison réelle pendant une période de l'oscillation haute fréquence au pic le plus élevé de l'enveloppe de modulation (cf. figure [ref:e_senderausgangsleisung_2]). Comment mesurer précisément la PEP – par exemple à l'aide d'un oscilloscope – nous l'aborderons plus en détail dans la section [sec:sender_messages].

<margin>
[picture:875:e_senderausgangsleisung_2:Pic le plus élevé de l'enveloppe de modulation]
</margin>

[question:EB501]

Outre la puissance de crête d'un émetteur (PEP), il existe aussi la *puissance moyenne*. Elle est indépendante de l'enveloppe, car la puissance mesurée dans son évolution temporelle est moyennée sur une durée longue par rapport à la période de la fréquence de modulation la plus basse. Avec cette réflexion, on peut identifier très simplement la réponse correcte à la question suivante.

[question:EB502]
