## Modulation par déplacement de phase (PSK)

* Procédé de modulation numérique pour la transmission de données
* Les symboles sont représentés par différentes positions de phase d'une porteuse
* L'amplitude et la fréquence de la porteuse restent identiques en PSK idéale
* Lors du changement de symbole, la phase peut varier

---

## Représentation temporelle de la PSK

<left>
[picture:705:a_psk:Modulation par déplacement de phase (Phase-Shift Keying)]
</left>
<right>
* L'amplitude reste constante
* L'information est contenue dans la *position de phase*
* Lors du passage entre deux symboles, la phase peut changer brusquement
* Si le même symbole est transmis à nouveau, la position de phase reste inchangée
</right>

---

## Modulation par déplacement de phase binaire (BPSK)

<left>
[picture:1101:a_psk_mapping:BPSK dans le diagramme de constellation]
</left>
<right>
* Deux positions de phase différentes
* Deux symboles possibles
* Permet de transmettre $\num{1}$ bit par symbole
* Exemple : $\qty{0}{\degree}$ → $0$ et $\qty{180}{\degree}$ → $1$
* Les deux points du signal sont opposés dans le diagramme de constellation
</right>

<note>
La forme la plus simple de modulation par déplacement de phase est la BPSK. Les deux symboles possibles possèdent la même amplitude, mais leurs phases diffèrent de 180 degrés.

Remarque : mathématiquement, la BPSK peut aussi être générée en multipliant la porteuse par +1 ou -1 selon la valeur du bit. La multiplication par -1 correspond à un déphasage de 180 degrés :


$-\sin(\omega t)=\sin(\omega t+\qty{180}{\degree})$


Le choix de 0 degré et 180 degrés n'est pas obligatoire. Par exemple, 90 degrés et 270 degrés seraient également possibles.
</note>

---

[question:AE401]


---

## Plus de positions de phase – plus de symboles

* Avec davantage de positions de phase, on peut représenter plus de symboles différents
* Cela permet de regrouper plusieurs bits en un seul symbole

<fragment>
* *BPSK* : $\num{2}$ symboles → $\num{1}$ bit par symbole
* *QPSK* : $\num{4}$ symboles → $\num{2}$ bits par symbole
* *8-PSK* : $\num{8}$ symboles → $\num{3}$ bits par symbole
</fragment>

---

[question:AE402]


---

## Modulation par déplacement de phase en quadrature (QPSK)

* La QPSK utilise quatre positions de phase différentes
* Quatre symboles différents sont ainsi disponibles
* Deux bits sont regroupés en un symbole : $00$, $01$, $10$, $11$
* Chaque symbole QPSK transmet donc $\num{2}$ bits


---

## QPSK dans le diagramme de constellation

<left>
[picture:1059:a_qpsk:Diagramme I/Q pour un mappage QPSK]
</left>
<right>
Dans cet exemple :

* $11$ → $\qty{45}{\degree}$
* $01$ → $\qty{135}{\degree}$
* $00$ → $\qty{225}{\degree}$
* $10$ → $\qty{315}{\degree}$


<fragment>
* Tous les points du signal possèdent la même amplitude
* Les positions de phase sont décalées de $\qty{90}{\degree}$ les unes par rapport aux autres
* Les quatre points se trouvent sur un cercle
</fragment>
</right>

<note>
L'attribution des combinaisons de bits aux différentes positions de phase n'est pas fixe. Cependant, l'émetteur et le récepteur doivent utiliser la même cartographie.

La cartographie utilisée ici correspond également à celle du texte pédagogique et de l'applet suivant.
</note>

---

## Code de Gray en QPSK

<left>
[picture:1059:a_qpsk_gray:Diagramme I/Q pour un mappage QPSK]
</left>
<right>
* Les symboles adjacents ne diffèrent que par *un seul bit*
* Une telle attribution est appelée *code de Gray*


<fragment>
Exemple :

$11 \leftrightarrow 01 \leftrightarrow 00 \leftrightarrow 10$
</fragment>


<fragment>
Si un symbole adjacent est détecté par erreur à cause du bruit, cela entraîne généralement une seule erreur de bit.
</fragment>
</right>

<note>
La cartographie est choisie de telle sorte que les points adjacents dans le diagramme de constellation ne diffèrent que par un seul bit.

Par exemple, lors du passage de 11 à 01, seul le premier bit change. Il en va de même pour les autres points adjacents, y compris 10 et 11.
</note>

---

<left>
[include:applet_qpsk]
</left>

<right>
### QPSK en présence de bruit
* Le bruit modifie l'amplitude et la phase du signal reçu
* Les valeurs reçues s'écartent des symboles QPSK idéaux
* Le récepteur décide du symbole le plus proche
* Si une limite de décision est franchie, une erreur de symbole se produit
</right>

<note>
L'applet montre non seulement les symboles QPSK idéaux, mais aussi la situation au niveau du récepteur.

Les croix marquent les quatre points de signal idéaux. Les petits points colorés représentent les valeurs reçues bruitées. En raison du bruit et d'autres perturbations, l'amplitude et la phase du signal reçu changent.

Les zones colorées en arrière-plan sont les zones de décision du récepteur. Le récepteur attribue une valeur reçue au symbole idéal le plus proche.

Tant qu'un point bruité reste dans la zone de décision du symbole initialement émis, il est correctement reconnu. Si le point franchit une limite de décision en raison d'un bruit important, un autre symbole est reconnu à la place.

Avec « Transmettre à nouveau », le même flux de bits est transmis une nouvelle fois avec un nouveau bruit. Cela permet de bien voir que, malgré des symboles émis identiques, des valeurs reçues différentes apparaissent à chaque fois.

Avec l'augmentation du bruit, la probabilité d'erreurs de symbole et donc de bits augmente. Grâce à un codage de canal adapté, de nombreuses erreurs peuvent être détectées et corrigées.
</note>

---

## ASK et PSK dans le diagramme de constellation

* En *ASK*, les symboles diffèrent principalement par leur amplitude
  * distance différente par rapport à l'origine
  * même position de phase
* En *PSK*, les symboles diffèrent par leur position de phase
  * même distance par rapport à l'origine
  * angle différent
* En PSK, les points du signal se trouvent donc sur un cercle, car l'amplitude est constante.