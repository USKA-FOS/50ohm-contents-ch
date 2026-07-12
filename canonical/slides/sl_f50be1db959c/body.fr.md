## Mapping dans le traitement numérique des signaux

* Convertit les données numériques en points de signal spécifiques (symboles)
* Essentiel pour les techniques de modulation comme QAM et QPSK
* Permet la transmission des données via le système de communication

---

## Étape 1 : Conversion des données binaires en symboles

* Dans le cas de QPSK, deux bits sont regroupés pour former un symbole
* Il en résulte 4 combinaisons possibles : $\num{00}$, $\num{01}$, $\num{10}$, $\num{11}$
* Chaque combinaison est attribuée à un point de signal spécifique

---

## Étape 2 : Attribution de phase

* Chaque symbole se voit attribuer une phase propre
* Phases typiques en pas de $\qty{90}{\degree}$ :
* $\num{00}$ correspond à $\qty{0}{\degree}$
* $\num{01}$ correspond à $\qty{90}{\degree}$
* $\num{10}$ correspond à $\qty{180}{\degree}$
* $\num{11}$ correspond à $\qty{270}{\degree}$

--- style="font-size: smaller;"
## Étape 3 : Mapping sur le diagramme de constellation

<left>
[picture:697:a_8qam:I-Q-Diagramm für ein 8QAM-Mapping]
La représentation est pour un mapping 8QAM. QPSK dans l'exemple correspond au cercle extérieur.
</left>
<right>
* Le diagramme de constellation représente les points de signal dans un diagramme carré
* L'axe X (*I*n-Phase) et l'axe Y (*Q*uadratur) montrent les amplitudes des composantes du signal
* Pour QPSK, les quatre points de signal se trouvent aux extrémités d'un carré
</right>

---

## Représentation des symboles QPSK

* $\num{00}$ à $\qty{0}{\degree}$ : point sur l'axe X positif
* $\num{01}$ à $\qty{90}{\degree}$ : point sur l'axe Y positif
* $\num{10}$ à $\qty{180}{\degree}$ : point sur l'axe X négatif
* $\num{11}$ à $\qty{270}{\degree}$ : point sur l'axe Y négatif

* La séparation claire des phases facilite la distinction des symboles - même en présence de bruit
