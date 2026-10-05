<margin>
[include:hamnet_map]
</margin>

Dans le chapitre [sec:linkstrecken], nous avons appris les bases des liaisons point à point et les règlements pertinents de l'OFCOM. Ici, nous allons aborder concrètement la technique du HAMNET.

Le HAMNET occupe un rôle particulier dans le radioamateurisme – un réseau réservé exclusivement aux radioamateurs. HAMNET (Highspeed Amateurradio Multimedia Network) est un réseau basé sur IP, développé et exploité par des radioamateurs. Dans son fonctionnement, il ressemble à Internet, mais utilise principalement des liaisons radio pour la transmission de données.

À l'origine, HAMNET a été conçu comme un remplacement progressif du réseau Packet-Radio existant depuis les années 1980 et l'a maintenant presque entièrement remplacé. Les connexions de données rapides entre les points d'accès individuels et les nœuds sont principalement réalisées via les bandes micro-ondes de 6 cm, 9 cm et 13 cm. Pour accéder au HAMNET, il faut avoir une vue dégagée vers un nœud HAMNET avec accès utilisateur ainsi qu'un émetteur-récepteur WLAN adapté avec une antenne directionnelle.

---

<margin>
Le [*SWISS-ARTG*](https://www.swiss-artg.ch/index.php?id=9) offre à ses membres un accès VPN via la [HAMCloud](https://www.swiss-artg.ch/index.php?id=37). Cela permet d'accéder au HAMNET, même si un accès direct par radio n'est pas possible.

[Devenez membre de l'USKA maintenant !](https://uska.ch/de/uska-beitreten/)
</margin>

On peut utiliser le Hamnet exactement comme Internet, dans le cas le plus simple avec un navigateur web. C'est possible parce que le protocole Internet (IP) et tout ce qui s'y appuie peut également être utilisé à d'autres fins qu'Internet.

[question:EE414]

Le Hamnet, tout comme Internet, est un ensemble de nombreux réseaux individuels. Si deux participants ne peuvent pas se joindre directement, les paquets de données sont alors acheminés via d'autres nœuds.

[question:EE412]

Dans de telles structures étendues, on crée de l'ordre en numérotant tous les ordinateurs. Les numéros des participants sont appelés adresses IP. Il existe les versions IPv4 et IPv6. Pour notre hobby, il suffit généralement de se familiariser avec la version 4, plus simple.

Les adresses IPv4 sont des nombres binaires d'une longueur de 32 bits. Elles sont écrites sous forme de quatre nombres décimaux, chacun représentant 8 bits, séparés par des points. Le nombre maximal possible est 255, correspondant au nombre binaire 11111111.

Pour tous les ordinateurs situés dans le même réseau, le début des adresses IP est identique. Cette partie réseau a une longueur variable. Les grands réseaux ont besoin de nombreux bits parmi les 32 pour numéroter leurs ordinateurs dans la partie dite hôte à la fin. Ils utilisent pour cela une partie réseau plus courte. Pour les petits réseaux, c'est exactement l'inverse. Ce principe est connu du réseau téléphonique. Les plus grandes villes ont des indicatifs à trois chiffres, par exemple 089, et les petits réseaux locaux ont des indicatifs à cinq ou six chiffres comme 038725.

---

La longueur de la partie réseau s'indique le plus simplement par une barre oblique après l'adresse IP. 141.17.5.18/24 signifie, par exemple, que la partie réseau est longue de 24 bits. Pour tous les ordinateurs du même réseau, l'adresse commence par 141.17.5. Il ne reste que 8 des 32 bits pour numéroter toutes les stations. Il s'agit donc d'un réseau relativement petit.

<indepth>
Parfois, les réseaux sont attribués à une classe dite, bien que ce système ait été abandonné depuis longtemps. La classe A signifiait /8, la classe B /16 et la classe C /24.
</indepth>
%TODO Ajouter le routage interdomaine sans classe (CIDR) comme approfondissement.

---

La plupart des appareils réseau exigent une autre notation, à savoir le masque de sous-réseau (voir figure [ref:netzmaske]). Ce sont 32 bits dans la même notation que les adresses IP. Les bits qui représentent la partie réseau sont marqués par un 1 et les bits de la partie hôte par un 0. Le masque de réseau commence donc avec autant de uns que la partie réseau est longue. Le reste est complété par des zéros. Les réseaux domestiques et les petits réseaux d'entreprise utilisent presque toujours le masque de réseau 255.255.255.0, ce qui signifie la même chose que /24.

Les appareils réseau ne peuvent communiquer directement entre eux qu'au sein de leur propre réseau local. Ils le reconnaissent au fait que leur propre adresse IP et leur masque de sous-réseau donnent la même partie réseau que celle du partenaire. Dans tous les autres cas, ils envoient les données à un routeur. Il s'agit d'une station intermédiaire qui relie deux réseaux ou plus. Si un appareil est directement connecté à plusieurs réseaux, il a sa propre adresse IP dans chacun d'eux.

<margin>
[picture:699:netzmaske:Adresse IPv4 et masque de réseau en notation décimale et binaire]
</margin>

<margin>
[picture:706:netzwerk:Extrait d'une infrastructure réseau]
</margin>

Tous les participants d'un réseau doivent pouvoir utiliser le routeur quasiment simultanément. C'est pourquoi dans les réseaux IP, aucune ligne fixe n'est établie. Au lieu de cela, les ordinateurs divisent tous les flux de données en paquets, c'est-à-dire en courtes sections. Le routage de ces paquets individuels est appelé commutation de paquets.

[question:EE413]