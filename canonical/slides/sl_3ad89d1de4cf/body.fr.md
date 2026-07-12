* L'un des circuits les plus importants en radioamateur
* Génération d'oscillations haute fréquence dans les émetteurs et les récepteurs
* Cœur de chaque appareil radio

---
### Gain de boucle

* Élément amplificateur dont le signal de sortie est rétro-couplé à l'entrée
* En phase
* Amplitude au moins égale $\rightarrow$ *Gain de boucle supérieur à 1*
* Nécessaire pour l'auto-excitation et maintient l'oscillation

---
[question:AD613]
---
<left>
[picture:760:a_oszillator_schaltungen_oszillateur:Circuit d'un oscillateur à trois points à rétroaction capacitive]
</left>
<right>
* Le signal de sortie est rétro-couplé de l'émetteur à la base via un diviseur de tension capacitif
* La fréquence est déterminée par le circuit oscillant dans la base et le diviseur de tension capacitif monté en parallèle
* Oscillateur en configuration collecteur
</right>
<note>
Les circuits à transistors viendront un peu plus tard dans le chapitre
</note>

---
[question:AD614]
---
[question:AD616]
---
<left>
[picture:497:a_oszillator_schaltungen_quarzoszillateur:Circuit d'un oscillateur à quartz en configuration collecteur avec fonctionnement du quartz à la fréquence fondamentale]
</left>
<right>
* Le circuit oscillant est remplacé par un quartz
* Le quartz peut osciller à la fréquence fondamentale ou sur des harmoniques $\rightarrow$ L'amplificateur doit être conçu pour être sélectif en fréquence, par exemple avec un circuit oscillant
</right>
<note>
Aucun autre circuit oscillant n'est présent ici, donc le quartz est utilisé à la fréquence fondamentale
</note>

---
[question:AD617]
---
### Couplage du signal

* Toujours au point de plus faible impédance d'un oscillateur
* Ainsi, l'oscillateur est peu chargé
* Dans le cas d'un circuit collecteur, à l'émetteur du transistor

---
### Étage tampon

* Ajouter un étage tampon
* Découple l'oscillateur des autres parties du circuit
* La fréquence n'est pas influencée par la charge de la sortie
* L'étage tampon est souvent un circuit collecteur (en tant que suiveur d'émetteur) et a une impédance d'entrée élevée

---
[question:AD610]
---
[question:AD615]
---
### Mesure

* Une mesure doit être effectuée après l'étage tampon
* Sinon, l'oscillateur est chargé par les capacités parasites
* La fréquence est ainsi influencée

---
[question:AD619]
---
[question:AD618]
