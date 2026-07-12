## Émissions indésirables par des produits de mélange

<left>
[picture:243:a_unerwuenschte_aussendungen_bandpassfilter:Réponse en fréquence d'un filtre passe-bande]
</left>
<right>
* Se produisent lors de la préparation des fréquences des émetteurs  
* Les produits de mélange se produisent dans les mélangeurs  
* Les filtres passe-bande suppriment les signaux indésirables  
</right>

---

[question:AJ208]

---

[question:AJ211]

---

[question:AJ209]

--- style="font-size: smaller;"

### Harmoniques et harmoniques supérieures

<left>
[picture:868:a_harmonische: Harmoniques (Harm.), harmoniques supérieures (OW) et émissions parasites (NA)]
</left>
<right>
* Multiples de la fréquence fondamentale d'un signal  
* Différence dans la définition et la numérotation  
* 1ère harmonique = fréquence fondamentale  
* 2ème harmonique = 1ère harmonique supérieure  
* 3ème harmonique = 2ème harmonique supérieure  
</right>
  
---

[question:AJ204]

---
#### Solution
* donné: $f = \qty{29,5}{\mega\hertz}$
* donné: $n = 3$
* donné: domaine radio: $\qtyrange{88,5}{108,0}{\mega\hertz}$

<fragment>
$f \cdot n = \qty{29,5}{\mega\hertz} \cdot 3 = \qty{88,5}{\mega\hertz}$
</fragment>

---

[question:AJ203]

---
#### Solution
* donné: $f = \qty{7,20}{\mega\hertz}$
* donné: $n = 4$
* recherché: 3ème harmonique supérieure

<fragment>
$f \cdot n = \qty{7,20}{\mega\hertz} \cdot 4 = \qty{28,80}{\mega\hertz}$
</fragment>

---

### Formation des harmoniques supérieures

<left>
[picture:106:a_unerwuenschte_aussendungen_uebersteuerung:Signal surchargé]
</left>
<right>
* Cause: surcharge des étages amplificateurs  
* Limitation des pics d'amplitude entraîne des distorsions  
* Les harmoniques supérieures apparaissent lorsque la forme sinusoïdale n'est pas idéale  
</right>

<note>
Les harmoniques supérieures et les harmoniques apparaissent toujours lorsque des écarts par rapport à la courbe sinusoïdale idéale se forment.
</note>

---

[question:AJ207]

---

## Circuits bouchons pour la suppression

* Suppression d'harmoniques supérieures ou d'harmoniques individuelles  
* Circuit bouchon: atténue une fréquence au maximum  
* Les autres fréquences sont laissées passer presque sans entrave  

---

[question:AJ210]

---

## Émissions parasites

* Apparaît à proximité immédiate du signal d'émission  
* Difficile à supprimer par des filtres  
* Formation par une amplification de microphone surchargée  
* Élargit involontairement le signal d'émission (émission parasite, produits secondaires, "Splatter")  

---

[question:AJ219]

---

## Perturbations dues à une tension d'alimentation instable

* Les mauvaises alimentations génèrent une tension de bourdonnement  
* Peut entraîner des émissions AM  
* Les interférences BF influencent l'émetteur  
* Particulièrement problématique avec les anciens émetteurs  

---

[question:AJ222]

---

[question:AJ223]

---

## Valeurs limites légales pour les harmoniques supérieures et les émissions parasites

* Les radioamateurs doivent respecter les valeurs limites  
* Deux domaines de fréquences avec des exigences différentes  

<note>
Plus d'informations dans la [disposition 33](http://50ohm.de/vfg33) de 2007.
</note>

---

### Domaine HF ($\qtyrange{1,7}{35}{\mega\hertz}$)

* Atténuation d'au moins $\qty{40}{\dB}$
* Puissance de signal supérieure à $\qty{0,25}{\micro\watt}$ pertinente

---

[question:AJ224]

---

### Domaine VHF/UHF/SHF ($\qtyrange{50}{1000}{\mega\hertz}$)

* Atténuation d'au moins $\qty{60}{\dB}$
* Puissance de signal supérieure à $\qty{0,25}{\micro\watt}$ pertinente

---

[question:AJ225]
