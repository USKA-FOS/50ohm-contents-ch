## Mesure de fréquence chez les récepteurs

* La fréquence de réception ne peut généralement pas être mesurée directement, car il n'y a pas de point de mesure disponible
* Pour vérifier, un oscillateur ou un générateur de fréquence précis est connecté à la prise d'antenne
* Comparaison de la fréquence du générateur avec l'affichage du récepteur
* Les oscillateurs synchronisés par GPS/OCXO offrent une plus grande précision

<note>
Un générateur de fréquence connecté directement peut endommager facilement une entrée de récepteur. En cas de doute, la mesure doit être effectuée avec la tension la plus faible du générateur et un atténuateur.
</note>

---

[question:AI511]

---

[question:AI504]

---

## Mesure de fréquence chez les émetteurs

* La mesure de fréquence chez les émetteurs est plus simple
* Un compteur de fréquence est connecté à la prise d'antenne via un atténuateur
* La mesure n'est utile que pour une porteuse non modulée

<note>
Les émetteurs SSB ne génèrent aucun signal sans modulation. Pour mesurer leur fréquence d'émission, on peut injecter un signal audio de fréquence connue dans la prise du microphone. Pour USB, la fréquence audio est soustraite de la valeur mesurée par le compteur de fréquence à la sortie de l'émetteur, pour LSB elle est ajoutée.
</note>

---

[question:AI502]

---

[question:AI501]

---

* La mesure de fréquence au moyen d'un oscilloscope n'est qu'une solution de fortune, car ces appareils ont rarement une base de temps aussi précise que les compteurs de fréquence.

---

[question:AI503]

---

* Les compteurs de fréquence simples fonctionnent presque toujours avec une soi-disant *temps de porte*
* L'appareil active l'entrée pendant un certain temps, compte les périodes et calcule la fréquence à partir de celles-ci
* Un temps de porte de $\qty{1}{\second}$ donne directement la fréquence en $\unit{\hertz}$
* Temps de porte court : actualisation rapide
* Temps de porte long : précision de mesure plus élevée

---

[question:AI505]


