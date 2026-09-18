<margin>
[include:hamnet_map]
</margin>

Dans le chapitre [sec:linkstrecken], nous avons appris les bases des liaisons et les prescriptions correspondantes de l'OFCOM. Nous allons maintenant nous concentrer sur la technique du HAMNET.

Le HAMNET occupe une place particulière dans le radioamateurisme : c'est un réseau réservé exclusivement aux radioamateurs. Le HAMNET (Highspeed Amateurradio Multimedia Network) est un réseau IP développé et exploité par des radioamateurs. Son fonctionnement ressemble à celui d'Internet, mais il utilise principalement des liaisons radio pour la transmission de données.

À l'origine, le HAMNET a été conçu comme un remplacement progressif du réseau Packet-Radio, existant depuis les années 1980, et l'a presque entièrement remplacé depuis. Les liaisons de données rapides entre les points d'accès et les nœuds sont principalement réalisées via les bandes micro-ondes de 6 cm, 9 cm et 13 cm. Pour accéder au HAMNET, il faut une ligne de vue vers un nœud HAMNET avec accès utilisateur, ainsi qu'un émetteur-récepteur WLAN adapté avec une antenne directionnelle.

---

<margin>
L'[*SWISS-ARTG*](https://www.swiss-artg.ch/index.php?id=9) propose à ses membres un accès VPN via les [HAMCloud](https://www.swiss-artg.ch/index.php?id=37). Cela permet d'accéder au HAMNET même sans accès radio direct.

[Devenez membre de l'USKA !](https://uska.ch/wieso-uska-mitglied-werden/)
</margin>

On peut utiliser le HAMNET de la même manière qu'Internet, par exemple avec un navigateur web. Cela est possible parce que le protocole Internet (IP) et tout ce qui en découle peuvent être utilisés à d'autres fins que le seul Internet.

[question:EE414]

Le HAMNET, comme Internet, est un ensemble de nombreux réseaux individuels. Si deux participants ne peuvent pas se joindre directement, les paquets de données sont transmis via d'autres nœuds.

[question:EE412]

Dans de tels systèmes, on établit un ordre en attribuant un numéro à chaque ordinateur. Ces numéros sont appelés adresses IP. Il existe les versions IPv4 et IPv6. Pour notre hobby, il suffit généralement de se familiariser avec la version 4, plus simple.

Les adresses IPv4 sont des nombres binaires de 32 bits de longueur. Elles s'écrivent sous la forme de quatre nombres décimaux, chacun représentant 8 bits, séparés par des points. Le nombre maximal est 255, correspondant au nombre binaire 11111111.

Pour tous les ordinateurs situés dans le même réseau, le début des adresses IP est identique. Cette partie réseau a une longueur variable. Les grands réseaux ont besoin de nombreux bits parmi les 32 pour numéroter leurs ordinateurs dans la partie appelée "hostanteil" (partie hôte). Ils utilisent donc une partie réseau plus courte. Dans les petits réseaux, c'est l'inverse. Ce principe est connu du réseau téléphonique. Les grandes villes ont des préfixes à trois chiffres, par exemple 089, tandis que les petits réseaux locaux ont des préfixes à cinq ou six chiffres comme 038725.

---

La longueur de la partie réseau s'indique le plus simplement par une barre oblique après l'adresse IP. Par exemple, 141.17.5.18/24 signifie que la partie réseau fait 24 bits de long. Pour tous les ordinateurs du même réseau, l'adresse commence par 141.17.5. Il ne reste que 8 des 32 bits pour numéroter toutes les stations. Il s'agit donc d'un réseau relativement petit.

<indepth>
Parfois, les réseaux sont classés dans ce qu'on appelle des "classes", bien que ce système ait été abandonné depuis longtemps. La classe A correspondait à /8, la classe B à /16 et la classe C à /24.
</indepth>
%TODO Ajouter des approfondissements sur le Classless Inter-Domain Routing (CIDR).

---

La plupart des appareils réseau nécessitent une autre notation : le masque de sous-réseau (voir figure [ref:netzmaske]). Il s'agit de 32 bits notés de la même manière que les adresses IP. Les bits représentant la partie réseau sont marqués par un 1, et ceux de la partie hôte par un 0. Le masque de sous-réseau commence donc par autant de 1 que la partie réseau est longue, le reste étant complété par des 0. Les réseaux domestiques et les petits réseaux d'entreprise utilisent presque toujours le masque 255.255.255.0, qui équivaut à /24.

Les appareils réseau ne peuvent communiquer directement qu'au sein de leur propre réseau local. Ils le reconnaissent en comparant la partie réseau de leur propre adresse IP et du masque de sous-réseau avec celle de leur partenaire. Dans tous les autres cas, ils envoient les données à un routeur. Il s'agit d'une station intermédiaire qui relie deux ou plusieurs réseaux. Si un appareil est directement connecté à plusieurs réseaux, il possède une adresse IP distincte dans chacun d'eux.

<margin>
[picture:699:netzmaske:Adresse IPv4 et masque de sous-réseau en notation décimale et binaire]
</margin>

<margin>
[picture:706:réseau:Extrait d'une infrastructure réseau]
</margin>

Tous les participants d'un réseau doivent pouvoir utiliser le routeur en même temps. C'est pourquoi les réseaux IP n'établissent pas de connexions fixes. À la place, les ordinateurs divisent tous les flux de données en paquets, c'est-à-dire en segments courts. La transmission de ces paquets individuels s'appelle la commutation par paquets.

[question:EE413]
