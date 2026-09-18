## Le processus d’échantillonnage

* Les signaux analogiques sont convertis en échantillons discrets
* Échantillonnage : conversion d’un signal continu en échantillons à intervalles de temps réguliers
* Comparable à un appareil photo qui prend des images à intervalles réguliers

---

### L’échantillonnage – L’exemple de l’appareil photo

* Un appareil photo prend par exemple $\num{24}$ images par seconde
* Entre les images, des mouvements rapides peuvent se produire sans être capturés
* Comme avec un appareil photo, un événement soudain (par exemple une mouche) peut disparaître entre deux prises de vue
* Cela entraîne une perte d’informations temporelles

---

### Perte d’informations et limite de reconstruction

* Entre les échantillons, des variations rapides du signal peuvent passer inaperçues
* Pour une reconstruction sans erreur, il doit y avoir un échantillon avant et après chaque changement de signal
* Si ce n’est pas le cas, des détails sont perdus – l’aliasing se produit

---

## Le théorème d’échantillonnage de Nyquist-Shannon

* Pour un signal de fréquence maximale $f_{\mathrm{max}}$, la fréquence d’échantillonnage doit être $\gt 2 \cdot f_{\mathrm{max}}$
* Seule cette condition permet de capturer et de reconstruire correctement toutes les variations du signal
* Si cette limite n’est pas respectée, des effets d’aliasing apparaissent

---

[question:AF617]

---

### Exemple pratique : Lecteur CD

* Les lecteurs CD fonctionnent généralement avec une fréquence d’échantillonnage de $\qty{44,1}{\kilo\sps}$ ($
um{44100}$ échantillons par seconde)
* Il en résulte que des fréquences jusqu’à environ $\qty{22}{\kilo\hertz}$ peuvent être correctement représentées
* Cela correspond à la bande passante HiFi des bonnes installations stéréo
* À retenir : La fréquence d’échantillonnage doit toujours être légèrement supérieure au double de la fréquence maximale à traiter

---

[question:AF616]

---

[question:AF618]

---

[question:AF619]