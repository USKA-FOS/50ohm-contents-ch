## Fonction du convertisseur A/N

* Convertit les signaux d'entrée analogiques en échantillons numériques  
* Essentiel pour la numérisation et le traitement ultérieur des signaux

---

### Aliasing et anti-aliasing

* Théorème d'échantillonnage : Pour une reconstruction sans erreur, la fréquence d'échantillonnage doit être $\gt 2 \cdot f_{\mathrm{max}}$
* Les signaux au-dessus de la fréquence maximale traitée peuvent apparaître comme des alias erronés  
* Les filtres anti-aliasing (passe-bas ou filtre passe-bande) suppriment les fréquences élevées indésirables  
* Protègent le convertisseur A/N des effets d'aliasing erronés

---

[question:AF620]

---

### Générateur de rythme (générateur de fréquence d'échantillonnage)

* Génère le rythme temporel exact pour l'échantillonnage  
* Détermine combien de fois par seconde un échantillon est capturé  
* Peut être réglé de manière fixe ou contrôlé par une commande (par exemple, un microcontrôleur)

---

### Quantification et erreur de quantification

* Lors de la conversion A/N, les valeurs d'amplitude analogiques sont mappées en étapes fixes  
* Cela conduit à une représentation discrète de valeur du signal initialement continu  
* Les erreurs de quantification surviennent car toutes les valeurs intermédiaires ne peuvent pas être capturées exactement

---

[question:AF607]

---

## Résolution du convertisseur A/N

* Nombre d'étapes pouvant être représentées numériquement  
* Exprimé en bits (par exemple, $\qty{8}{\bit} = \num{256}$ étapes, $\qty{16}{\bit} = \num{65536}$ étapes)
* Souvent, la moitié des valeurs sont utilisées pour la plage positive et l'autre moitié pour la plage négative

---

[question:AF608]

---

### Jitter : Instabilités de temporisation

* Le jitter décrit de petites fluctuations aléatoires dans les instants d'échantillonnage  
* Un générateur de fréquence d'échantillonnage instable entraîne des effets de bruit supplémentaires dans le signal numérique  
* Un effort technique élevé est nécessaire pour garantir un rythme précis

---

[question:AF621]
