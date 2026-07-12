Une station pour l'exploitation à distance se compose de plusieurs blocs fonctionnels logiquement séparables. Dans ce cas, même des parties de ces blocs fonctionnels peuvent être intégrées dans un appareil (par exemple, un émetteur-récepteur avec une connexion réseau et une interface à distance).

Un agencement pour l'exploitation à distance peut être représenté logiquement avec les blocs fonctionnels suivants.

---

<margin>
[picture:501:a_remotebetrieb:Schéma bloc Exploitation à distance]
</margin>

* *Ordinateur et partie de commande de l'opérateur (Bloc 1)* : Celui-ci sert à commander la station à distance. Les signaux audio et de commande locaux sont convertis en paquets de réseau et transmis à la station à distance. Les signaux de commande et audio reçus de la station à distance (qui sont transmis par réseau) sont à nouveau rendus audibles et visibles par l'ordinateur/la partie de commande.
* *Réseau* : Réseau de liaison ou réseaux de liaison entre le lieu de l'opérateur et la station à distance. Dans ce cas, Internet peut également servir de réseau entre les lieux.
* *Ordinateur ou interface à distance au lieu à distance (Bloc 2)* : Celui-ci convertit les paquets de réseau reçus de l'opérateur en signaux de commande et audio pour la commande ultérieure de l'émetteur-récepteur au lieu à distance et transmet, en sens inverse, les signaux audio reçus de l'émetteur-récepteur via le réseau à l'opérateur. Les réglages de l'émetteur-récepteur ainsi que les signaux de commande de retour sont également transmis via le réseau à l'opérateur.
* *Émetteur-récepteur/Amplificateur/Syntoniseur/Rotateur d'antenne (Bloc 3)* : Ces appareils sont commandés/rapportés par l'interface à distance ou un ordinateur au lieu à distance par des signaux que l'opérateur transmet à l'interface à distance via le réseau.

[question:AF701]
[question:AF702]
[question:AF704]
[question:AF703]
[question:AF705]

Lors de l'exploitation à distance, des retards temporels se produisent dans le réseau et lors du traitement du codage et du décodage des signaux audio. Cela doit être pris en compte lors de l'exploitation radio via des stations à distance.

[question:AF709]
[question:AF710]

Pour s'assurer qu'une station à distance ne tombe pas dans un état de fonctionnement incontrôlé en cas d'interruption ou de perturbation de la liaison de données entre l'utilisateur/la partie de commande et l'interface à distance, une surveillance et une rétroaction permanentes entre l'opérateur et la station à distance au moyen d'un soi-disant watchdog sont nécessaires. Dans ce cas, des paquets de données sont envoyés par la station à distance à l'ordinateur de l'opérateur à intervalles de quelques secondes, qui doivent être accusés réception dans un certain temps par une réponse. Si cette réponse n'est pas donnée, la station à distance sait que la liaison avec l'opérateur est interrompue et peut mettre l'émetteur-récepteur automatiquement dans un état sûr défini (par exemple, mode réception) et interrompre une émission en cours.

[question:AF708]

Étant donné que l'émetteur-récepteur lui-même peut également entrer dans un état indéfini (par exemple, en raison d'erreurs logicielles ou matérielles dans l'appareil), l'alimentation de l'émetteur-récepteur doit pouvoir être coupée à distance. Cela peut être réalisé, par exemple, par une prise secteur IP, qui peut être commandée par l'opérateur via le réseau.

[question:AF707]

Lors de l'exploitation d'une station à distance, il faut également prendre en compte et s'attendre à ce que des composants de la station à distance puissent être perturbés par l'émetteur-récepteur au lieu de la station à distance.

[question:AF706]