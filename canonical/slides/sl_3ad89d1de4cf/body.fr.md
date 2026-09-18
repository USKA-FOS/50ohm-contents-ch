* L'une des circuits les plus importants en radioamateurisme
* Génération d'oscillations haute fréquence dans les émetteurs et récepteurs
* Cœur de tout appareil radio

---
### Gain de boucle

* Élément amplificateur dont le signal de sortie est réinjecté à l'entrée
* En phase
* Amplitude au moins égale $\rightarrow$ *gain de boucle supérieur à $1$*
* Nécessaire pour l'auto-excitation et maintient l'oscillation

---
[question:AD613]
---
<left>
[picture:760:a_oszillator_schaltungen_oszillator:Schéma d'un oscillateur à trois points à couplage capacitif]
</left>
<right>
* Le signal de sortie est réinjecté de l'émetteur vers la base via un diviseur de tension capacitif
* La fréquence est déterminée par le circuit oscillant à la base et le diviseur de tension capacitif en parallèle
* Oscillateur en montage à collecteur commun
</right>
<note>
Les circuits à transistors seront abordés plus tard dans le chapitre
</note>

---
[question:AD614]
---
[question:AD616]
---
<left>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Schéma d'un oscillateur à quartz en montage à collecteur commun fonctionnant à la fréquence fondamentale]
</left>
<right>
* Le circuit oscillant est remplacé par un quartz
* Le quartz peut osciller à sa fréquence fondamentale ou sur ses harmoniques $\rightarrow$ l'amplificateur doit être conçu de manière sélective en fréquence, par exemple avec un circuit oscillant
</right>
<note>
Ici, aucun autre circuit oscillant n'est présent, donc le quartz fonctionne à sa fréquence fondamentale
</note>

---
[question:AD617]
---
### Extraction du signal

* Toujours au point de plus faible impédance d'un oscillateur
* Ainsi, l'oscillateur est peu chargé
* En montage à collecteur commun, au niveau de l'émetteur du transistor

---
### Étage tampon

* Ajouter un étage tampon
* Découple l'oscillateur des autres parties du circuit
* La fréquence n'est pas influencée par la charge de la sortie
* L'étage tampon est souvent un montage à collecteur commun (émetteur suiveur) et possède une impédance d'entrée élevée

---
[question:AD610]
---
[question:AD615]
---
### Mesure

* Une mesure doit être effectuée après l'étage tampon
* Sinon, l'oscillateur est chargé par les capacités parasites
* La fréquence est alors influencée

---
[question:AD619]
---
[question:AD618]