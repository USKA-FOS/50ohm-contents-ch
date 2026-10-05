Dans la section [sec:remote_stationen], nous avons déjà appris les conditions formelles pour la mise en service et l'utilisation d'une installation de radioamateur télécommandée. Dans cette section, nous allons examiner quelques aspects techniques de l'exploitation à distance, qui sont pertinents pour l'exploitation et l'utilisation d'une station à distance.

Une station pour exploitation à distance se compose de plusieurs blocs fonctionnels logiquement séparables les uns des autres. Dans les appareils modernes, certaines parties de ces blocs fonctionnels peuvent être intégrées dans un seul appareil (par exemple, un émetteur-récepteur avec connexion réseau et interface distante).

Une configuration pour exploitation à distance peut être représentée logiquement avec les blocs fonctionnels suivants.

---

<margin>
[picture:501:a_remotebetrieb:schéma bloc exploitation à distance]
</margin>

* *Ordinateur et partie de commande de l'opérateur (bloc 1)* : Celui-ci sert à commander la station à distance. Localement, les signaux audio ainsi que les signaux de commande sont convertis en paquets de données réseau et transmis à la station à distance. Les signaux de commande et audio reçus de la station à distance (qui sont transmis via le réseau) sont rendus audibles et visibles à nouveau par l'ordinateur/la partie de commande.
* *Réseau* : Réseau de connexion ou réseaux de connexion entre l'emplacement de l'opérateur et la station à distance. Ici, Internet peut également servir de réseau entre les emplacements.
* *Ordinateur ou interface distante à l'emplacement distant (bloc 2)* : Celui-ci convertit les paquets de données réseau reçus de l'opérateur en signaux de commande et signaux audio pour la commande ultérieure de l'émetteur-récepteur à l'emplacement distant et transmet en retour les signaux audio reçus de l'émetteur-récepteur via le réseau vers l'opérateur. Les réglages de l'émetteur-récepteur ainsi que les signaux de commande de retour sont également transmis via le réseau vers l'opérateur.
* *Émetteur-récepteur/amplificateur/tuner/rotor d’antenne (bloc 3)* : Ces appareils sont commandés/asservis par l'interface distante ou un ordinateur à l'emplacement distant via des signaux que l'opérateur transmet via le réseau à l'interface distante.

[question:AF701]
[question:AF702]
[question:AF704]
[question:AF703]
[question:AF705]

---

Avec l'exploitation à distance, des retards temporels se produisent en raison des temps de propagation dans le réseau et des temps de traitement lors du codage et du décodage des signaux audio. Ceci doit être pris en compte lors de l'exploitation radio via des stations à distance.

<indepth>
Particularités de l'exploitation à distance

- Pour les liaisons vocales, les retards sont plutôt peu problématiques.

- Pour les liaisons télégraphiques (Morse), les retards - notamment en exploitation de concours - peuvent apparaître comme gênants selon le concept de manipulation.

- Pour les modes de fonctionnement numériques basés sur l'émission de tons, il faut noter que le codec vocal peut, dans certaines circonstances, influencer les signaux de manière perturbatrice.

</indepth>

<tip>
Les stations à distance sont parfois proposées par [les sections USKA](https://uska.ch/de/funkamateure/die-uska/sektionen/) ou par des clubs pour leurs membres. D'autres stations à distance appartiennent à des groupes d'utilisateurs fermés. Idéalement, les stations à distance sont situées à des emplacements d'antenne avantageux.

[Devenez membre de l'USKA maintenant !](https://uska.ch/de/uska-beitreten/)
</tip>

[question:AF709]
[question:AF710]

Pour garantir qu'une station à distance ne tombe pas dans un état/une exploitation incontrôlé(e) en cas d'interruption ou de perturbation de la connexion de données entre l'utilisateur/la partie de commande et l'interface distante, une surveillance permanente et un retour d'information entre l'opérateur et la station à distance via un soi-disant watchdog sont nécessaires. Ici, par exemple, à des intervalles de quelques secondes, des paquets de données sont envoyés de la station à distance à l'ordinateur de l'opérateur, qui doivent être acquittés par une réponse de retour dans un certain temps. Si cette réponse de retour n'a pas lieu, la station à distance sait que la connexion avec l'opérateur est interrompue et peut mettre automatiquement l'émetteur-récepteur dans un état sûr défini (par exemple, mode réception) et interrompre une émission en cours.

[question:AF708]

Puisque l'émetteur-récepteur lui-même peut également entrer dans un état indéfini (par exemple, en raison d'erreurs logicielles ou matérielles dans l'appareil), la tension d'alimentation de l'émetteur-récepteur devrait pouvoir être coupée à distance. Cela peut se faire, par exemple, via une prise IP, qui peut être commandée par l'opérateur via le réseau.

<tip>
Certains émetteurs-récepteurs ont une fonction "Transmit Timeout Timer" (TOT), avec laquelle la durée d'émission maximale ininterrompue peut être limitée à une durée réglable. Cela constitue une protection supplémentaire contre l'émission continue.
</tip>

[question:AF707]

Lors de l'exploitation d'une station à distance, il faut également prendre en compte et s'attendre à ce que des composants de la station à distance puissent être perturbés par l'émetteur-récepteur à l'emplacement de la station à distance.

[question:AF706]
