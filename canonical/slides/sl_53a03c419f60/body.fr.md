## Exploitation à distance de stations radio

* Composée de plusieurs blocs fonctionnels
* Les appareils modernes intègrent parfois plusieurs blocs
* Séparation entre l’opérateur et le site à distance

---

### Schéma bloc d’une station à distance

<left>
[picture:501:a_remotebetrieb:Schéma bloc exploitation à distance]
</left>
<right>
* Représentation logique des blocs fonctionnels
* Commande, connexion réseau, interface à distance
* Émetteur-récepteur et appareils connectés
</right>

---

#### Ordinateur et unité de commande de l’opérateur (Bloc 1)

<left>
[picture:501:a_remotebetrieb:Schéma bloc exploitation à distance]
</left>
<right>
* Convertit les signaux audio et de commande en paquets réseau
* Les signaux reçus sont rendus audibles et visibles
</right>

---

#### Réseau

<left>
[picture:501:a_remotebetrieb:Schéma bloc exploitation à distance]
</left>
<right>
* Connecte l’opérateur au site à distance
* Utilisation d’Internet possible
</right>

---

#### Interface à distance sur le site à distance (Bloc 2)

<left>
[picture:501:a_remotebetrieb:Schéma bloc exploitation à distance]
</left>
<right>
* Convertit les paquets réseau en signaux de commande et audio
* Transmet les signaux audio reçus vers l’opérateur
</right>

---

#### Émetteur-récepteur/amplificateur/tuner/rotor d’antenne (Bloc 3)

<left>
[picture:501:a_remotebetrieb:Schéma bloc exploitation à distance]
</left>
<right>
* Commandés via l’interface à distance
* La confirmation des commandes de contrôle est transmise via le réseau
</right>

---

[question:AF701]

---
[question:AF702]

---
[question:AF704]

---
[question:AF703]

---
[question:AF705]

---

### Délais dans l’exploitation à distance

* Les temps de traitement et de réseau entraînent des latences
* Le codage et le décodage des signaux audio provoquent des retards
* Doit être pris en compte lors des communications radio

---

[question:AF709]

---
[question:AF710]

---

### Watchdog pour la surveillance de la station à distance

* Empêche un état incontrôlé en cas de rupture de connexion
* Échange régulier de paquets de données entre la station et l’opérateur
* En l’absence de réponse, l’émetteur-récepteur passe en état sûr

---

[question:AF708]

---

### Arrêt à distance de l’alimentation électrique

* L’émetteur-récepteur peut se retrouver dans un état indéfini
* La tension d’alimentation doit pouvoir être coupée à distance
* Solution : prise intelligente IP pour le contrôle via le réseau

---

[question:AF707]

---

### Perturbations causées par l’émetteur-récepteur

* La station à distance peut être perturbée par ses propres signaux
* Des mesures de déparasitage appropriées sont nécessaires

---

[question:AF706]
