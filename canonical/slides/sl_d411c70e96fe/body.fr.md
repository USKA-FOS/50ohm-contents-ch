## Le processus d'échantillonnage

* Les signaux analogiques sont convertis en échantillons discrets  
* Échantillonnage : échantillonnage d'un signal continu à intervalles de temps fixes  
* Comparable à une caméra qui prend des photos à intervalles réguliers

---

### Échantillonnage – L'exemple de la caméra

* Une caméra prend par exemple $\num{24}$ images par seconde
* Entre les images, des mouvements rapides peuvent se produire qui ne sont pas capturés  
* Comme pour la caméra, un événement soudain (par exemple une mouche) peut être perdu entre deux prises de vue  
* Cela entraîne une perte d'information temporelle

---

### Perte d'information et limite de reconstruction

* Entre les échantillons, des changements de signal rapides peuvent rester indécelés  
* Pour une reconstruction sans erreur, un échantillon doit se trouver avant et après chaque changement de signal  
* Si ce n'est pas le cas, des détails sont perdus – l'effet d'aliasing se produit

---

## Le théorème d'échantillonnage de Nyquist-Shannon

* Pour un signal avec une fréquence maximale $f_{\mathrm{max}}$, la fréquence d'échantillonnage doit être $\gt 2 \cdot f_{\mathrm{max}}$
* Seule cette condition permet de capturer et de reconstruire correctement tous les changements de signal  
* Si cette limite n'est pas respectée, des effets d'aliasing se produisent

---

[question:AF617]

---

### Exemple pratique : Lecteur CD

* Les lecteurs CD fonctionnent typiquement avec $\qty{44,1}{\kilo\sps}$ ($\num{44100}$ échantillons par seconde)
* Il en résulte : les fréquences jusqu'à environ $\qty{22}{\kilo\hertz}$ peuvent être représentées correctement
* Cela correspond à la plage de fréquences HiFi des bonnes installations stéréo  
* Remarque : La fréquence d'échantillonnage doit toujours être légèrement supérieure au double de la fréquence maximale à traiter

---

[question:AF616]

---

[question:AF618]

---

[question:AF619]
