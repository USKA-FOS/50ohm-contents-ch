## QAM et procédé I/Q

* Technique de modulation numérique qui utilise deux porteuses de la même fréquence  
* L'une des porteuses est déphasée de $\qty{90}{\degree}$
* Génère un signal qui change en amplitude et en phase

---

### Génération de QAM

<left>
* Deux porteuses :  
* L'une est modulée avec le signal I (en phase)  
* L'autre, décalée de $\qty{90}{\degree}$, avec le signal Q (en quadrature)
</left>
<right>
* Les deux porteuses modulées sont superposées  
* Le signal résultant change en amplitude et en phase  
</right>

---

[include:applet_iq]

---

[question:AE404]

---

[question:AF632]

---

### Procédé I/Q – côté émetteur

* Le flux de données numériques est divisé en deux parties : I et Q  
* Deux convertisseurs analogiques numériques convertissent les valeurs I et Q numériques en signaux analogiques  
* Ceux-ci modulent les deux porteuses déphasées, qui sont ensuite combinées

---

### Procédé I/Q – côté récepteur

* Le signal reçu est mélangé avec une porteuse à $\qty{0}{\degree}$ pour extraire le signal I
* Simultanément, un mélange est effectué avec une porteuse déphasée de $\qty{90}{\degree}$ pour obtenir le signal Q
* Les deux signaux sont convertis en analogique/numérique et forment ainsi le flux de données I/Q numérique

---

[question:AF633]

---

### Représentation de la bande de fréquences

* Le flux de données I/Q représente la bande de fréquences autour d'une fréquence centrale  
* Exemple :  
* porteuse de $\qty{435}{\mega\hertz}$
* Fréquence d'échantillonnage de $\num{10}$ millions d'échantillons/s $\rightarrow$ bande passante = $\qty{10}{\mega\hertz}$ ($\pm\qty{5}{\mega\hertz}$ autour de la fréquence centrale)
* Plage couverte : environ $\qty{430}{\mega\hertz}$ à $\qty{440}{\mega\hertz}$

---

[question:AF634]

---

### Dépendance de la bande passante du taux d'échantillonnage

* La bande passante couverte en $\unit{\hertz}$ correspond au taux d'échantillonnage en échantillons par seconde

---

[question:AF635]

---

[question:AF636]
