Dans la section suivante, les étapes individuelles d'une chaîne d'émission et de réception sont décrites. La figure [ref:a_sdr_sender] montre à titre d'exemple un émetteur SDR pour la communication vocale. Dans un premier temps, le signal du microphone est numérisé par un convertisseur analogique/numérique. Le signal numérique est ensuite compressé par un codeur source afin de réduire la bande passante nécessaire. Dans l'étape suivante, un codeur de canal ajoute intentionnellement de la redondance au signal compressé, permettant ainsi de détecter et de corriger les erreurs de transmission. Les données codées sont ensuite converties en symboles par un mappeur et ensuite modulées par un modulateur I/Q, qui sera abordé plus en détail dans un chapitre ultérieur. La chaîne d'émission se termine par un amplificateur de puissance et l'antenne, qui émet le signal.

<margin>
[picture:1062:a_sdr_sender:Émetteur SDR pour la communication vocale]
</margin>

Les blocs mis en évidence en bleu dans la figure [ref:a_sender] représentent les étapes de traitement du signal qui peuvent être implémentées, par exemple, de manière purement logicielle ou à l'aide d'un FPGA. L'ordre de ces étapes de traitement est toujours le suivant pour un émetteur et doit être bien mémorisé pour les questions d'examen:

1. Codeur source : Compression des données
2. Codeur de canal : Ajout de redondance pour la détection et la correction des erreurs
3. Mappeur : Mappage des données binaires sur des symboles, par exemple amplitude et phase pour QAM

[question:AF626]
[question:AF627]

---

Pour un récepteur, le processus est inversé : l'antenne reçoit le signal, qui est amplifié par un amplificateur de puissance. Ensuite, la démodulation est effectuée par un démodulateur I/Q pour extraire les symboles. Le démappeur associe ces symboles aux données binaires d'origine. Ensuite, le décodeur de canal a pour tâche de détecter et de corriger les erreurs qui peuvent avoir été introduites pendant la transmission. Enfin, le décodeur source décompresse les données pour restaurer le signal d'origine, qui est ensuite converti en signal analogique par un convertisseur numérique/analogique et peut être émis, par exemple, via un amplificateur sur un haut-parleur.

Nous résumons le traitement numérique du signal dans le récepteur en trois étapes suivantes:

1. Démappeur : Mappage des symboles sur des données binaires
2. Décodeur de canal : Détection et correction des erreurs
3. Décodeur source : Décompression des données

<margin>
[picture:1063:a_sdr_empfänger:Récepteur SDR pour la communication vocale]
</margin>

[question:AF628]
[question:AF629]
