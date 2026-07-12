## Bande passante
<left>
* Contrairement à l'AM, moins de la moitié de la bande passante est utilisée
* Maximum $\qty{2,7}{\kilo\hertz}$
* Correspond au signal AF
</left>
<right>
[picture:743:e_bandbreite_am_ssb:Bande passante de l'AM, USB et LSB]
</right>

---
[question:EE201]
---
[question:EE202]
---
[question:EJ210]

---

## Modulation

<left>
* Par mélange et filtrage
* Avec la présélection de USB et LSB, la fréquence porteuse est choisie
* Deux fréquences sont générées par le mélangeur
* Un filtre passe-bande ne laisse passer qu'une seule fréquence
</left>
<right>
[picture:500:e_ssb_modulation:Schéma bloc de la modulation SSB avec la méthode de filtrage]
</right>

---
<left>
* Le truc ici est que le filtre passe-bande n'a qu'une fréquence de résonance
* En décalant la fréquence porteuse dans l'oscillateur, la bande latérale souhaitée est alors transmise
</left>
<right>
[picture:500:e_ssb_modulation:Schéma bloc de la modulation SSB avec la méthode de filtrage]
</right>
---
<left>
Exemple LSB:
* Microphone: $\qty{300}{\hertz}$ - $\qty{3}{\kilo\hertz}$
* Oscillateur LSB: $\qty{9001,5}{\kilo\hertz}$
* Signal DSB:<br/> a) $\qtyrange{8998,5}{9001,2}{\kilo\hertz}$<br/> b) $\qtyrange{9001,8}{9004,5}{\kilo\hertz}$
* Filtre: $\qty{9000}{\kilo\hertz}\pm\qty{1,5}{\kilo\hertz}$
* Signal SSB:<br/> $\qtyrange{8998,5}{9001,2}{\kilo\hertz}$
</left>
<right>
[picture:831:e_ssb_modulation_lsb:Fréquences avec la méthode de filtrage pour LSB]
[picture:940:e_ssb_modulation_lsb_spektrum:Spectre avec la méthode de filtrage pour LSB]
</right>
<note>
* Le commutateur dans l'image doit être sur LSB
* Seul le signal de a) est transmis
* Le signal SSB peut être à nouveau mélangé pour une émission dans la bande AFU
</note>
---
<left>
Exemple USB:
* Microphone: $\qty{300}{\hertz}$ - $\qty{3}{\kilo\hertz}$
* Oscillateur USB: $\qty{8998,5}{\kilo\hertz}$
* Signal DSB:<br/> a) $\qtyrange{8995,5}{8998,2}{\kilo\hertz}$<br/> b) $\qtyrange{8998,8}{9001,5}{\kilo\hertz}$
* Filtre: $\qty{9000}{\kilo\hertz}\pm\qty{1,5}{\kilo\hertz}$
* Signal SSB:<br/> $\qtyrange{8998,8}{9001,5}{\kilo\hertz}$
</left>
<right>
[picture:832:e_ssb_modulation_usb:Fréquences avec la méthode de filtrage pour USB]
[picture:941:e_ssb_modulation_usb_spektrum:Spectre avec la méthode de filtrage pour USB]
</right>
<note>
* Seul le signal de b) est transmis
* Le signal SSB peut être à nouveau mélangé pour une émission dans la bande AFU
</note>

---
[question:EE203]
---
[question:EE204]

---
### Signal AF

<left>
* Pour la parole, entre $\qty{300}{\hertz}$ et $\qty{3000}{\hertz}$ suffit
* Correspond à $\qty{2,7}{\kilo\hertz}$
* Des filtres plus petits, par exemple $\qty{2,4}{\kilo\hertz}$, sont également utilisés
* Sur de nombreux émetteurs-récepteurs, les filtres peuvent être réglés
</left>
<right>
* Si un signal AF avec une bande passante plus grande est utilisé, la bande passante HF augmente
* Cela doit être évité pour ne pas perturber les signaux voisins
* Faire attention à la bande passante maximale dans le plan de bande
</right>

---
[question:EJ211]
<note>
* Si les $\qty{300}{\hertz}$ inférieurs du AF sont soustraits, il reste $\qty{2,7}{\kilo\hertz}$
</note>
---
[question:EF310]
---
[question:EE207]

---
## Amplification du microphone
* Avec la puissance AF, la puissance HF est contrôlée
* Un microphone trop silencieux entraîne une puissance de sortie plus faible à l'émetteur
* Une amplification trop forte du microphone peut causer des perturbations sur les stations à des fréquences très proches

---
[question:EE206]
---
[question:EE205]
---
[question:EJ215]
