## Transformée de Fourier et décomposition des signaux

* Les signaux peuvent être représentés dans le domaine temporel ou dans le domaine des fréquences  
* Dans le domaine temporel : axe X → temps, axe Y → tension ou puissance  
* Dans le domaine des fréquences : axe X → fréquence, axe Y → amplitude ou puissance

---

### Décomposition des signaux

* Tout signal peut être représenté comme une superposition d'oscillations sinusoïdales  
* Chaque oscillation sinusoïdale possède une amplitude et une phase déterminées  
* Ce principe permet de décomposer des signaux complexes en leurs composantes

---

### Transformée de Fourier (FT)

* Procédé mathématique complexe qui analyse un signal temporel  
* Montre quelles oscillations sinusoïdales (fréquences) sont présentes dans le signal  
* Le résultat est représenté sous forme de spectre de fréquences (axe X : fréquence, axe Y : amplitude/puissance)

---

### Fast Fourier Transform (FFT)

* Calcul efficace de la transformée de Fourier discrète (TFD)  
* Réduit considérablement la charge de calcul  
* Très répandu dans les logiciels et matériels pour le traitement des signaux

--- style="font-size: smaller;"

## Spectres de formes d'onde typiques

* *Sinusoïdal* : une seule fréquence : $f$
* *Carré* : seulement des multiples impairs : $f$, $3f$, $5f$, $7f$, ...
* *Dent de scie* : tous les multiples entiers : $f$, $2f$, $3f$, $4f$, ...
* *Triangulaire* : seulement des multiples impairs : $f$, $3f$, $5f$, $7f$, ... (les harmoniques décroissent plus rapidement que pour le signal carré)

À l'examen, il faut uniquement savoir distinguer le signal sinusoïdal et le signal carré.

<note>
Les signaux carré et triangulaire contiennent tous deux uniquement des harmoniques impaires. La différence réside dans la décroissance des amplitudes : pour le signal triangulaire, les harmoniques supérieures diminuent beaucoup plus rapidement.
</note>

---

[question:AF630]

---

[question:AB404]

---

[question:AB405]

---

[question:AB406]

---

[question:AB407]
