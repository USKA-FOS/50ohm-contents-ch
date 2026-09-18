Dans la section suivante, les différentes étapes d’une chaîne d’émission et de réception sont décrites. L’illustration [ref:a_sdr_sender] montre par exemple un émetteur SDR pour la communication vocale. Dans un premier temps, le signal du microphone est numérisé par un convertisseur analogique-numérique (A/N). Le signal numérique est ensuite compressé par un codeur de source afin de réduire la bande passante nécessaire. L’étape suivante consiste à ajouter de la redondance au signal compressé à l’aide d’un codeur de canal, permettant ainsi de détecter et corriger les erreurs de transmission. Les données codées sont enfin converties en symboles par un mappeur, puis modulées par un modulateur I/Q. La chaîne d’émission se termine par un amplificateur de puissance et une antenne qui rayonne le signal.

<margin>
[picture:1062:a_sdr_sender:Émetteur SDR pour communication vocale]
</margin>

Les blocs mis en évidence en bleu dans l’illustration [ref:a_sdr_sender] représentent les étapes de traitement du signal qui peuvent être implémentées, par exemple, de manière purement logicielle ou à l’aide d’un FPGA. L’ordre de ces étapes de traitement est toujours le même pour un émetteur et doit être bien mémorisé pour les questions d’examen :

1. Codeur de source : compression des données
2. Codeur de canal : ajout de redondance pour la détection et correction d’erreurs
3. Mappeur : conversion des données binaires en symboles, par exemple amplitude et phase pour la QAM

[question:AF626]
[question:AF627]

---

Pour un récepteur, le processus fonctionne à l’envers : l’antenne reçoit le signal, qui est amplifié par un amplificateur de puissance. Ensuite, la démodulation est effectuée par un démodulateur I/Q pour extraire les symboles. Le démappeur associe ces symboles aux données binaires d’origine. Le décodeur de canal détecte et corrige ensuite les erreurs éventuellement survenues pendant la transmission. Enfin, le décodeur de source décompresse les données pour restituer le signal d’origine, qui est ensuite converti en signal analogique par un convertisseur numérique-analogique (N/A) et, par exemple, transmis à un haut-parleur via un amplificateur.

Nous résumons le traitement numérique du signal (DSP) dans le récepteur en trois étapes :

1. Démappeur : conversion des symboles en données binaires
2. Décodeur de canal : détection et correction des erreurs
3. Décodeur de source : décompression des données

<margin>
[picture:1063:a_sdr_empfänger:Récepteur SDR pour communication vocale]
</margin>

[question:AF628]
[question:AF629]
