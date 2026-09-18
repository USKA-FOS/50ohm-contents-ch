## Mesure de fréquence sur les récepteurs

* La fréquence de réception ne peut généralement pas être mesurée directement, car il n'existe pas de point de mesure accessible
* Pour la vérifier, on connecte un oscillateur ou un générateur de fréquence précis à la prise d'antenne
* Comparaison entre la fréquence du générateur et l'affichage du récepteur
* Les oscillateurs/OCXO synchronisés par GPS offrent une précision accrue

<note>
Un générateur de fréquence connecté directement peut endommager légèrement l'entrée du récepteur. En cas de doute, il est conseillé de commencer la mesure avec la tension la plus faible du générateur et d'utiliser un atténuateur.
</note>

---

[question:AI511]

---

[question:AI504]

---

## Mesure de fréquence sur les émetteurs

* La mesure de fréquence sur les émetteurs est plus simple
* Un fréquencemètre est connecté à la prise d'antenne via un atténuateur
* La mesure n'est pertinente que sur une porteuse non modulée

<note>
Les émetteurs en BLU ne génèrent pas de signal sans modulation. Pour mesurer leur fréquence d'émission, on peut injecter un signal audio de fréquence connue dans la prise micro. Pour l'USB, on soustrait la fréquence audio de la valeur mesurée par le fréquencemètre à la sortie de l'émetteur, et pour le LSB, on l'ajoute.
</note>

---

[question:AI502]

---

[question:AI501]

---

* La mesure de fréquence à l'oscilloscope ne constitue qu'une solution de secours, car ces appareils disposent rarement d'une base de temps aussi précise que les fréquencemètres.

---

[question:AI503]

---

* Les fréquencemètres simples fonctionnent presque toujours avec un *temps de porte* déterminé
* L'appareil active l'entrée pendant une durée fixe, compte les périodes et calcule la fréquence à partir de ce comptage
* Un temps de porte de $\qty{1}{\second}$ fournit directement la fréquence en $\unit{\hertz}$
* Temps de porte court : actualisation rapide
* Temps de porte long : précision de mesure accrue

---

[question:AI505]