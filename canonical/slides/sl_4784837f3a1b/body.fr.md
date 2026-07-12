* Le Hamnet, le réseau réservé aux radioamateurs, repose sur le protocole Internet (IP).
* C'est pourquoi on peut utiliser le Hamnet avec le même logiciel que celui utilisé pour Internet.
* Dans le cas le plus simple, il s'agit d'un navigateur Web.

---

* Le protocole Internet (IP) attribue des adresses IP aux ordinateurs participants afin qu'ils puissent se joindre mutuellement.
* Les adresses IP sont écrites comme quatre nombres décimaux avec un point entre eux. Exemple : 141.17.5.18
* Chaque nombre décimal a une longueur de 8 bits, donc le nombre le plus grand possible est 255 (binaire : 11111111).

<note>
Il existe les versions IPv4 et IPv6. Nous nous occupons ici de la version 4.
</note>

---

* Les adresses IP sont divisées en une partie réseau et une partie hôte.
* Pour tous les ordinateurs qui se trouvent dans le même réseau, le début des adresses IP est identique, ce début est appelé partie réseau.
* La partie réseau est de taille différente, selon le nombre d'ordinateurs (hôtes) qui doivent être gérés dans le réseau.

---

Exemples :

     *10*.100.234.22 (petite partie réseau, grande partie hôte)
     
     *192.168.1*.252 (grande partie réseau, petite partie hôte)
     
Ce principe est connu du réseau téléphonique. Les grandes villes ont des indicatifs régionaux plus courts que les petites villes.

---

[picture:699:netzmaske:Adresse IPv4 et masque de sous-réseau en écriture décimale et binaire]

* Un masque de sous-réseau indique la division d'une adresse IP en parties réseau et hôte en représentant tous les bits de la partie réseau comme 1.

---

* Il existe deux possibilités de l'écrire, exemple pour une partie réseau de 24 :
* 255.255.255.0, ce qui en binaire est 11111111.11111111.11111111.00000000.
* L'écriture avec la barre oblique, par exemple 192.168.111.90/24

<note>
Le nombre après la barre oblique indique le nombre de uns dans le masque de sous-réseau.
</note>

---

[picture:706:netzwerk:Extrait d'une infrastructure réseau]

* Les appareils réseau ne peuvent communiquer directement entre eux que dans leur propre réseau local.

--- data-transition="none"

[picture:706:netzwerk:Extrait d'une infrastructure réseau]

* On les reconnaît au fait que leur propre adresse IP et leur masque de sous-réseau donnent la même partie réseau que le partenaire.

--- data-transition="none"

[picture:706:netzwerk:Extrait d'une infrastructure réseau]

* Dans tous les autres cas, ils envoient les données à un routeur. Il s'agit d'une station intermédiaire qui relie deux ou plusieurs réseaux entre eux pour transmettre les paquets de données.

---
[question:EE412]

---
[question:EE414]

---
[question:EE413]
