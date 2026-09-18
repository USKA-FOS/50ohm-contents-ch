## Traitement numérique du signal : filtres

* Les informations numériques peuvent être traitées de manière presque arbitraire  
* Les échantillons d'entrée sont convertis en échantillons de sortie à l'aide de fonctions mathématiques  
* Les opérations de filtrage peuvent être implémentées numériquement (par exemple, filtres passe-bas, passe-bande ou passe-haut)

---

### Filtre FIR (Finite Impulse Response)

* « Finite » = seul un nombre limité d'échantillons d'entrée est utilisé pour chaque échantillon de sortie  
* Pas de rétroaction ; le calcul repose exclusivement sur les échantillons actuels et passés

---

### Filtre IIR (Infinite Impulse Response)

* « Infinite » = le calcul d'un échantillon de sortie se réfère à tous les échantillons d'entrée précédents  
* L'utilisation de la rétroaction conduit à un comportement impulsionnel théoriquement infini

---

[question:AF631]