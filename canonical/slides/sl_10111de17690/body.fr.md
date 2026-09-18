## Situation initiale : ASK et PSK

* Avec l’ASK et la PSK, on peut utiliser davantage de symboles pour transmettre plus de bits par symbole
* Avec un très grand nombre de symboles, les états possibles du signal sont de plus en plus proches les uns des autres
* Le récepteur doit alors pouvoir distinguer des différences plus petites
* La méthode devient plus sensible aux perturbations

<note>
Il peut sembler tentant d’augmenter simplement le nombre d’amplitudes ou de positions de phase. Cela permet effectivement de transmettre plus de bits par symbole, mais en contrepartie, il devient plus difficile pour le récepteur de distinguer clairement les symboles individuels.
</note>

---

## Modulation d’amplitude en quadrature (QAM)

* Astuce : on ne modifie pas *un seul* paramètre
* La QAM combine différents
  * amplitudes et
  * positions de phase
* Un symbole correspond à une combinaison spécifique d’amplitude et de phase

<fragment>
Avec le même débit de symboles, il est ainsi possible de transmettre davantage de bits par seconde.
</fragment>

<note>
Au lieu de devoir distinguer de nombreuses amplitudes différentes, comme dans le cas de l’ASK, la QAM exploite simultanément deux degrés de liberté : l’amplitude et la phase.

Ainsi, même avec un nombre relativement restreint de valeurs distinctes, il est possible de générer un plus grand nombre de symboles différents.
</note>

--- style="font-size: 0.7em;"
## Exemple : 8-QAM

[picture:702:a_8qam:Évolution du signal d’un signal 8QAM, chaque symbole étant caractérisé par une amplitude (0,5 ou 1), une position de phase et une séquence de 3 bits]

* 8 symboles différents
* Chaque symbole possède une amplitude et une position de phase déterminées
* 8 symboles → 3 bits par symbole

<note>
L’illustration montre un signal 8-QAM dans le domaine temporel.

À chaque symbole est associée, par le biais d’un mappage, une séquence de 3 bits. Comme il existe huit symboles différents, trois bits peuvent être transmis à chaque symbole.
</note>

---
## Exemple : 16-QAM

<left>
[picture:1061:a_16qam:Diagramme I-Q pour un mappage 16-QAM]
</left>
<right>
* 16 points de signal différents
* Chaque point correspond à une paire de valeurs (I, Q)
* Cela donne lieu à différentes amplitudes et positions de phase
* 16 symboles → 4 bits par symbole
</right>

<note>
Le diagramme de constellation permet de visualiser clairement comment la QAM génère de nombreux symboles différents.

Avec la 16-QAM, il existe 16 points de signal possibles. À chaque point est associée une combinaison de 4 bits.

La position d’un point est décrite par les deux valeurs I et Q. Cela détermine à son tour l’amplitude et la position de phase du signal résultant.
</note>

---
[question:AE403]

---
## Comment un signal QAM est-il généré ?

Après avoir découvert le diagramme de constellation, la question se pose :

<fragment>
**Comment un émetteur génère-t-il un point de signal souhaité ?**
</fragment>

<fragment>
Pour cela, on peut utiliser un *modulateur I/Q*.
</fragment>

---
## Modulateur I/Q

<left>
[picture:196:a_iq_modulator:Schéma bloc d’un modulateur I/Q]
</left>
<right>
* Deux porteuses de même fréquence
* Décalage de phase de 90°
* Une porteuse est pondérée par le *signal I*
* L’autre porteuse est pondérée par le *signal Q*
* Les deux signaux sont ensuite additionnés
</right>

<note>
Un modulateur I/Q utilise deux porteuses sinusoïdales de même fréquence. Les deux porteuses sont déphasées de 90° l’une par rapport à l’autre.

La première est pondérée par la valeur I et la seconde par la valeur Q. Les deux composantes de signal sont ensuite additionnées.

Selon la combinaison de I et Q, il en résulte un signal d’une amplitude et d’une position de phase déterminées.
</note>

---
## I et Q déterminent l’amplitude et la phase

* Chaque point du diagramme de constellation correspond à une paire de valeurs (I, Q)
* En modifiant I et Q, on modifie
  * l’amplitude et
  * la position de phase
  du signal résultant

<fragment>
Le modulateur I/Q peut ainsi générer n’importe quel point souhaité du mappage.
</fragment>

<note>
Voici le lien direct entre le diagramme de constellation et le circuit réel :

Les coordonnées d’un point de signal correspondent exactement aux valeurs I et Q qui commandent le modulateur I/Q.

Le diagramme de constellation ne se limite donc pas à une représentation du signal. Il décrit directement les valeurs I et Q à générer.
</note>

--- style="font-size: smaller;"

## Tester la modulation I/Q

[include:applet_iq_169]

<note>
Avec l’applet, il est possible de tester immédiatement l’effet des deux valeurs I et Q.

Lorsque I et Q sont modifiés, le point de signal se déplace dans le diagramme de constellation. On peut observer simultanément comment l’amplitude et la position de phase du signal résultant changent.

Cela permet également de comprendre comment un modulateur I/Q peut générer les différents points d’un mappage QAM.
</note>

---

[question:AF632]

---

[question:AE404]

---

## I et Q issus d’un logiciel

* Un microcontrôleur, un processeur de signal ou un SDR calcule les valeurs de I et Q
* Pour chaque symbole, la paire de valeurs (I, Q) correspondante est déterminée

<fragment>
Exemple avec la 16-QAM :

* 4 valeurs I possibles
* 4 valeurs Q possibles
* 4 × 4 = 16 points de signal possibles
</fragment>

<note>
Les valeurs I et Q n’ont pas besoin d’être générées par un circuit analogique complexe.

Dans un système numérique, le logiciel peut simplement déterminer, pour chaque symbole à transmettre, les deux valeurs numériques correspondantes.

Avec une 16-QAM, on peut par exemple utiliser quatre valeurs différentes pour I et quatre pour Q. Les combinaisons donnent un total de 16 points de signal.
</note>

---

## De la valeur numérique au signal I/Q

* I et Q existent d’abord sous forme de *valeurs numériques*
* Les convertisseurs numérique-analogique (DAC) génèrent à partir de celles-ci des signaux analogiques I et Q
* Ces signaux commandent le modulateur I/Q

<fragment>
Le mappage souhaité peut ainsi être défini en grande partie dans le *logiciel*.
</fragment>

<note>
Le logiciel génère d’abord des valeurs numériques pour I et Q.

Les convertisseurs numérique-analogique (DAC) transforment ensuite ces valeurs en tensions analogiques, qui sont envoyées au modulateur I/Q.

En simplifiant, le logiciel doit donc simplement calculer quel point du diagramme de constellation doit être généré à un instant donné.
</note>

---

## Radio logicielle (SDR)

* Avec une *radio logicielle (SDR)*, une grande partie du traitement du signal est effectuée par logiciel
* Le logiciel calcule les signaux I et Q nécessaires
* Le matériel haute fréquence peut rester le même pour de nombreuses méthodes de modulation différentes

<fragment>
La méthode de modulation est ainsi déterminée en grande partie par le *logiciel*.
</fragment>

---

## Pas seulement pour la modulation numérique

Un modulateur I/Q peut également traiter des signaux I et Q continûment variables.

<fragment>
Il permet ainsi de générer, par exemple :

* AM
* FM
* PM
* BLU
* PSK
* QAM
</fragment>

<note>
Le principe I/Q n’est en aucun cas limité à la QAM ou à d’autres méthodes de modulation numérique.

Le logiciel peut générer, au lieu de valeurs symboliques fixes, des évolutions continues pour I et Q.

En AM, c’est principalement la valeur absolue du vecteur de signal qui est modifiée. En PM, c’est son angle qui est modifié.

La FM peut également être générée via la phase : la phase est modifiée en continu, la vitesse de variation de la phase correspondant à la fréquence instantanée.

Avec des signaux I et Q appropriés, il est également possible de générer un signal à bande latérale unique.
</note>

---

## Pas seulement pour la modulation numérique

* Le même modulateur I/Q peut générer de nombreuses méthodes de modulation différentes
* Il suffit de calculer différemment les évolutions de *I* et *Q*
* Le matériel HF peut rester largement inchangé

<fragment>
Le modulateur I/Q est ainsi, pour ainsi dire, le
**« couteau suisse des modulateurs »**. 
</fragment>

<note>
C’est précisément cette propriété qui rend la technologie SDR moderne si flexible.

Au lieu de nécessiter un circuit de modulation distinct pour l’AM, la FM, la BLU, la PSK ou la QAM, on peut utiliser le même matériel I/Q de base.

La méthode de modulation souhaitée est obtenue en calculant d’autres signaux I et Q dans le logiciel.
</note>
