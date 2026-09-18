Dans la classe N, nous avons déjà appris que l’exploitation à distance n’est autorisée que pour les radioamateurs de classe A. C’est pourquoi nous allons maintenant examiner quelques aspects techniques de l’exploitation à distance, pertinents pour l’utilisation d’une station à distance.

Une station pour l’exploitation à distance est composée de plusieurs blocs fonctionnels logiquement séparables. Dans le cas des appareils modernes, certaines parties de ces blocs fonctionnels peuvent être intégrées dans un seul appareil (par exemple, un émetteur-récepteur avec connexion réseau et interface à distance).

Une configuration pour l’exploitation à distance peut être représentée logiquement par les blocs fonctionnels suivants.

---

<margin>
[picture:501:a_remotebetrieb:Schéma bloc de l'exploitation à distance]
</margin>

* *Ordinateur et interface de commande de l’opérateur (bloc 1)* : celui-ci sert à contrôler la station à distance. Les signaux audio locaux ainsi que les signaux de commande sont convertis en paquets de données réseau et transmis à la station à distance. Les signaux de commande et audio reçus de la station à distance (transmis via le réseau) sont à nouveau rendus audibles et visibles par l’ordinateur ou l’interface de commande.
* *Réseau* : réseau ou réseaux de connexion entre l’emplacement de l’opérateur et la station à distance. Internet peut également servir de réseau entre les deux emplacements.
* *Ordinateur ou interface à distance sur le site distant (bloc 2)* : celui-ci convertit les paquets de données reçus de l’opérateur en signaux de commande et en signaux audio pour le contrôle ultérieur de l’émetteur-récepteur sur le site distant, et transmet en retour les signaux audio reçus de l’émetteur-récepteur via le réseau vers l’opérateur. Les réglages de l’émetteur-récepteur ainsi que les signaux de commande en retour sont également transmis via le réseau vers l’opérateur.
* *Émetteur-récepteur/amplificateur/tuner/rotor d’antenne (bloc 3)* : ces appareils sont contrôlés ou reçoivent des signaux de retour par l’interface à distance ou un ordinateur sur le site distant, via des signaux transmis par l’opérateur via le réseau vers l’interface à distance.

[question:AF701]
[question:AF702]
[question:AF704]
[question:AF703]
[question:AF705]

---

En cas d’exploitation à distance, des délais de transmission dans le réseau et des temps de traitement lors du codage et du décodage des signaux audio entraînent des retards temporels. Ceux-ci doivent être pris en compte lors des communications radio via des stations à distance.

<tip>
[photo:342:a_remote_station:Station à distance du DARC e. V.]

Le DARC e. V. exploite pour ses membres plusieurs stations club à distance réparties dans toute l’Allemagne. Sur [mein.darc.de](https://mein.darc.de/), les membres peuvent se connecter à ces stations à distance et effectuer des communications radio via Internet, à condition de disposer d’une autorisation de classe A. Pour les classes N et E, seul l’écoute (SWL) est possible.

[Devenir membre du DARC dès maintenant !](https://50ohm.de/mw)
</tip>

[question:AF709]
[question:AF710]

Pour garantir qu’une station à distance ne tombe pas dans un état ou un fonctionnement incontrôlé en cas de rupture ou de perturbation de la connexion de données entre l’utilisateur/l’interface de commande et l’interface à distance, une surveillance permanente et un retour d’information entre l’opérateur et la station à distance sont nécessaires, au moyen d’un système de surveillance (watchdog). Celui-ci envoie, par exemple à intervalles de quelques secondes, des paquets de données de la station à distance vers l’ordinateur de l’opérateur, qui doivent être confirmés par une réponse dans un délai déterminé. Si cette réponse n’est pas reçue, la station à distance sait que la connexion avec l’opérateur est interrompue et peut automatiquement placer l’émetteur-récepteur dans un état sûr défini (par exemple, en mode réception) et interrompre une émission en cours.

[question:AF708]

Comme l’émetteur-récepteur lui-même peut également se retrouver dans un état indéfini (par exemple, en raison d’une erreur logicielle ou matérielle dans l’appareil), il est recommandé de pouvoir couper à distance la tension d’alimentation de l’émetteur-récepteur. Cela peut être réalisé, par exemple, au moyen d’une prise intelligente IP, contrôlable par l’opérateur via le réseau.

[question:AF707]

Lors de l’exploitation d’une station à distance, il faut également tenir compte du fait que des composants de la station à distance peuvent être perturbés par l’émetteur-récepteur situé sur le site de la station à distance.

[question:AF706]