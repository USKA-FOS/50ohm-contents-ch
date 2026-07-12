<margin>
[include:hamnet_map]
</margin>

Une place particulière dans le radioamateurisme est occupée par le HAMNET – un réseau réservé exclusivement aux radioamateurs. HAMNET (Highspeed Amateurradio Multimedia Network) est un réseau basé sur IP développé et exploité par des radioamateurs. Dans son fonctionnement, il ressemble à Internet, mais utilise principalement des liaisons radio pour la transmission des données.

À l'origine, le HAMNET a été conçu comme un remplacement progressif du réseau Packet-Radio existant depuis les années 1980 et l'a désormais presque entièrement remplacé. Les liaisons de données rapides entre les différents points d'accès et les nœuds sont principalement réalisées via les bandes de micro-ondes de 6 cm, 9 cm et 13 cm. Pour accéder au HAMNET, il faut une vue dégagée vers un nœud HAMNET avec accès utilisateur ainsi qu'un émetteur-récepteur WLAN approprié avec antenne directionnelle.

---

<margin>
Le [*SWISS-ARTG*](https://www.swiss-artg.ch/index.php?id=9) offre à ses membres un accès VPN via les soi-disant [HAMCloud](https://www.swiss-artg.ch/index.php?id=37). Cela permet d'accéder au HAMNET même si une connexion directe par radio n'est pas possible.   

[Devenez membre de l'USKA!](https://uska.ch/wieso-uska-mitglied-werden/)
</margin>

On peut utiliser le Hamnet de la même manière qu'Internet, dans le cas le plus simple avec un navigateur Web. Cela est possible car le protocole Internet (IP) et tout ce qui en découle peuvent être utilisés à d'autres fins que pour Internet.

[question:EE414]

Le Hamnet, comme Internet, est un ensemble de nombreux réseaux individuels. Si deux participants ne peuvent pas se joindre directement, les paquets de données sont alors acheminés via d'autres nœuds.

[question:EE412]

Dans des structures aussi grandes, on crée de l'ordre en numérotant tous les ordinateurs. Les numéros des participants s'appellent adresses IP. Il existe les versions IPv4 et IPv6. Pour notre hobby, il suffit généralement de se familiariser avec la version 4, plus simple.

Les adresses IPv4 sont des nombres binaires de 32 bits de longueur. On écrit quatre nombres décimaux, chacun représentant 8 bits, avec des points entre eux. Le nombre le plus grand est 255 correspondant au nombre binaire 11111111.

Pour tous les ordinateurs qui se trouvent dans le même réseau, le début des adresses IP est identique. Cette partie réseau a une longueur variable. Les grands réseaux ont besoin de nombreux bits des 32 bits pour numérotés leurs ordinateurs dans la partie hôte à l'arrière. Ils utilisent donc une partie réseau plus courte. Dans les petits réseaux, c'est l'inverse. Ce principe est connu du réseau téléphonique. Les plus grandes villes ont des indicatifs à trois chiffres, par exemple 089, et les petits réseaux locaux à cinq ou six chiffres comme 038725.

---

La longueur de la partie réseau est donnée le plus simplement par une barre oblique derrière l'adresse IP. 141.17.5.18/24 signifie par exemple que la partie réseau a une longueur de 24 bits. Pour tous les ordinateurs du même réseau, l'adresse commence par 141.17.5. Il ne reste que 8 des 32 bits pour numérotés toutes les stations. Il s'agit donc d'un réseau relativement petit.

<indepth>
Parfois, les réseaux sont associés à une soi-disant classe, bien que ce système ait été abandonné depuis longtemps. La classe A signifiait /8, la classe B /16 et la classe C /24.
</indepth>
%TODO Ajouter Classless Inter-Domain Routing (CIDR) comme approfondissement.

---

La plupart des appareils réseau exigent une autre écriture, à savoir le masque de sous-réseau (voir figure [ref:netzmaske]). Il s'agit de 32 bits dans la même notation que les adresses IP. Les bits représentant la partie réseau sont marqués par un 1 et les bits de la partie hôte par un 0. Le masque de réseau commence donc par autant de uns que la partie réseau est longue. Le reste est complété par des zéros. Les réseaux domestiques et les petits réseaux d'entreprise utilisent presque toujours le masque de réseau 255.255.255.0, ce qui signifie la même chose que /24.

Les appareils réseau ne peuvent communiquer directement entre eux que dans leur propre réseau local. Ils le reconnaissent au fait que la même partie réseau résulte de leur propre adresse IP et du masque de sous-réseau que chez le partenaire. Dans tous les autres cas, ils envoient les données à un routeur. Il s'agit d'une station intermédiaire qui relie deux ou plusieurs réseaux entre eux. Si un appareil est directement connecté à plusieurs réseaux, il a sa propre adresse IP dans chacun d'eux.

<margin>
[picture:699:netzmaske:Adresse IPv4 et masque de réseau en notation décimale et binaire]
</margin>

<margin>
[picture:706:netzwerk:Extrait d'une infrastructure réseau]
</margin>

Tous les participants d'un réseau doivent pouvoir utiliser le routeur quasi simultanément. C'est pourquoi, dans les réseaux IP, aucune ligne fixe n'est commutée. Au lieu de cela, les ordinateurs divisent tous les flux de données en paquets, c'est-à-dire en courtes sections. L'acheminement de ces paquets individuels s'appelle la commutation de paquets.

[question:EE413]
