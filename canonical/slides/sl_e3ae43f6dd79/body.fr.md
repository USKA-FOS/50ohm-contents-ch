## Bande passante
<left>
* Contrairement à l'AM, on utilise moins de la moitié de la bande passante
* Maximum $\qty{2,7}{\kilo\hertz}$
* Correspond au signal BF
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
* Le choix préalable de l'USB ou du LSB détermine la fréquence porteuse
* Le mélangeur génère deux fréquences
* Le filtre de bande ne laisse passer qu'une seule fréquence
</left>
<right>
[picture:500:e_ssb_modulation:Schéma bloc de la modulation SSB avec la méthode de filtrage]
</right>

---
<left>
* L'astuce ici est que le filtre de bande n'a qu'une seule fréquence de résonance
* En décalant la fréquence porteuse dans l'oscillateur, on laisse passer la bande latérale souhaitée
</left>
<right>
[picture:500:e_ssb_modulation:Schéma bloc de la modulation SSB avec la méthode de filtrage]
</right>
---
<left>
Exemple LSB :
* Microphone : $\qty{300}{\hertz}$ - $\qty{3}{\kilo\hertz}$
* Oscillateur LSB : $\qty{9001,5}{\kilo\hertz}$
* Signal DSB :<br/> a) $\qtyrange{8998,5}{9001,2}{\kilo\hertz}$<br/> b) $\qtyrange{9001,8}{9004,5}{\kilo\hertz}$
* Filtre : $\qty{9000}{\kilo\hertz}\pm\qty{1,5}{\kilo\hertz}$
* Signal SSB :<br/> $\qtyrange{8998,5}{9001,2}{\kilo\hertz}$
</left>
<right>
[picture:831:e_ssb_modulation_lsb:Fréquences avec la méthode de filtrage en LSB]
[picture:940:e_ssb_modulation_lsb_spektrum:Spectre avec la méthode de filtrage en LSB]
</right>
<note>
* L'interrupteur dans l'image doit être réglé sur LSB
* Seul le signal a) est transmis
* Le signal SSB peut être mélangé à nouveau pour une émission dans la bande radioamateur
</note>
---
<left>
Exemple USB :
* Microphone : $\qty{300}{\hertz}$ - $\qty{3}{\kilo\hertz}$
* Oscillateur USB : $\qty{8998,5}{\kilo\hertz}$
* Signal DSB :<br/> a) $\qtyrange{8995,5}{8998,2}{\kilo\hertz}$<br/> b) $\qtyrange{8998,8}{9001,5}{\kilo\hertz}$
* Filtre : $\qty{9000}{\kilo\hertz}\pm\qty{1,5}{\kilo\hertz}$
* Signal SSB :<br/> $\qtyrange{8998,8}{9001,5}{\kilo\hertz}$
</left>
<right>
[picture:832:e_ssb_modulation_usb:Fréquences avec la méthode de filtrage en USB]
[picture:941:e_ssb_modulation_usb_spektrum:Spectre avec la méthode de filtrage en USB]
</right>
<note>
* Seul le signal b) est transmis
* Le signal SSB peut être mélangé à nouveau pour une émission dans la bande radioamateur
</note>

---
[question:EE203]
---
[question:EE204]

---
### Signal BF

<left>
* Pour la voix, une bande entre $\qty{300}{\hertz}$ et $\qty{3000}{\hertz}$ suffit
* Cela correspond à $\qty{2,7}{\kilo\hertz}$
* On utilise également des filtres plus petits, par exemple $\qty{2,4}{\kilo\hertz}$
* Sur de nombreux émetteurs-récepteurs, les filtres sont réglables
</left>
<right>
* Si un signal BF de plus grande bande passante est utilisé, la bande passante HF augmente
* Cela doit être évité pour ne pas perturber les signaux adjacents
* Respecter la bande passante maximale dans le plan de bande
</right>

---
[question:EJ211]
<note>
* Si l'on retire les $\qty{300}{\hertz}$ inférieurs du signal BF, on obtient à nouveau $\qty{2,7}{\kilo\hertz}$
</note>
---
[question:EF310]
---
[question:EE207]

---
## Amplification du microphone
* La puissance BF contrôle la puissance HF à la sortie de l'émetteur
* Un microphone trop faible réduit la puissance de sortie
* Une amplification trop forte du microphone peut causer des perturbations sur les stations voisines en fréquence

---
[question:EE206]
---
[question:EE205]
---
[question:EJ215]