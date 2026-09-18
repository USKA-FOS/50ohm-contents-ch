* Le Hamnet, le réseau réservé aux radioamateurs, repose sur le protocole Internet (IP).
* C'est pourquoi on peut utiliser le Hamnet avec les mêmes logiciels que ceux employés pour Internet.
* Dans le cas le plus simple, il s'agit d'un navigateur web.

---

* Le protocole Internet (IP) attribue aux ordinateurs concernés des adresses IP afin qu'ils puissent se joindre mutuellement.
* Les adresses IP s'écrivent sous la forme de quatre nombres décimaux séparés par des points. Exemple : 141.17.5.18
* Chaque nombre décimal a une longueur de 8 bits, c'est pourquoi le nombre maximal possible est 255 (binaire : 11111111).

<note>
Il existe les versions IPv4 et IPv6. Ici, nous nous concentrons sur la version 4.
</note>

---

* Les adresses IP sont divisées en une partie réseau et une partie hôte.
* Pour tous les ordinateurs situés dans le même réseau, le début des adresses IP est identique ; cette partie initiale est appelée partie réseau.
* La taille de la partie réseau varie selon le nombre d'ordinateurs (hôtes) à gérer dans le réseau.

---

Exemples :

     *10*.100.234.22 (petite partie réseau, grande partie hôte)
     
     *192.168.1*.252 (grande partie réseau, petite partie hôte)
     
Ce principe est similaire à celui du réseau téléphonique. Les grandes villes ont des préfixes plus courts que les petites villes.

---

[picture:699:netzmaske:Adresse IPv4 et masque de sous-réseau en notation décimale et binaire]

* Un masque de sous-réseau indique la division d'une adresse IP en partie réseau et partie hôte en représentant tous les bits de la partie réseau par des 1.

---

* Il existe deux façons de l'écrire, exemple pour une partie réseau de 24 :
* 255.255.255.0, ce qui correspond en binaire à 11111111.11111111.11111111.00000000.
* La notation avec une barre oblique, par exemple 192.168.111.90/24

<note>
Le nombre après la barre oblique indique le nombre de 1 dans le masque de sous-réseau.
</note>

---

[picture:706:netzwerk:Extrait d'une infrastructure réseau]

* Les appareils réseau ne peuvent communiquer directement entre eux que s'ils appartiennent au même réseau local.

--- data-transition="none"

[picture:706:netzwerk:Extrait d'une infrastructure réseau]

* On les reconnaît au fait que la partie réseau de leur propre adresse IP et de leur masque de sous-réseau est identique à celle du partenaire.

--- data-transition="none"

[picture:706:netzwerk:Extrait d'une infrastructure réseau]

* Dans tous les autres cas, ils envoient les paquets de données à un routeur. Il s'agit d'une station intermédiaire qui relie deux réseaux ou plus pour acheminer les paquets de données.

---
[question:EE412]

---
[question:EE414]

---
[question:EE413]
