## Échantillonnage et quantification

Lors de la numérisation d'un signal analogique, deux propriétés doivent être prises en compte :

* **Quand** le signal est-il mesuré ?
  * Échantillonnage
  * à temps continu → à temps discret
* **Avec quelle précision** la valeur mesurée est-elle représentée ?
  * Quantification
  * à valeurs continues → à valeurs discrètes

<note>
L'échantillonnage et la quantification sont deux étapes distinctes.

L'échantillonnage discrétise l'axe temporel : le signal n'est plus considéré qu'à des instants d'échantillonnage précis.

La quantification, en revanche, discrétise l'axe des valeurs : une valeur mesurée est attribuée à l'un des niveaux finis possibles.
</note>

---

## Signal analogique

[picture:408:a_wertkont_zeitkont:Signal à valeurs et temps continus]

* Une valeur de signal est présente à tout moment
* La valeur du signal peut prendre n'importe quelle valeur intermédiaire
* Un signal analogique idéal est donc *à temps et à valeurs continus*

--- style="font-size: smaller;"

## Échantillonnage

<left>
[picture:408:a_wertkont_zeitkont:Signal à valeurs et temps continus]
</left>
<right>
[picture:409:a_wertkont_zeitdisk:Signal à valeurs continues et temps discret]
</right>

<fragment>
* Le signal n'est échantillonné qu'à des instants précis
* Les valeurs individuelles échantillonnées sont appelées *échantillons*
* Un signal à temps continu devient un signal *à temps discret*
* Les valeurs elles-mêmes peuvent encore prendre n'importe quelle valeur pour l'instant
</fragment>

<note>
Dans l'échantillonnage idéalisé, seule l'axe temporel change initialement.

Avant l'échantillonnage, le signal est défini à tout moment. Après l'échantillonnage, seules des valeurs à des instants précis sont disponibles.

Les valeurs des échantillons individuels ne doivent pas encore être quantifiées à ce stade. C'est pourquoi le signal à droite est à temps discret, mais toujours à valeurs continues.
</note>

---

[question:AF601]

---

[question:AF603]

---

## Échantillonnage

* Le processus d'échantillonnage temporel est appelé *échantillonnage*
* Les valeurs échantillonnées individuelles sont appelées *échantillons*
* Entre deux échantillons, le signal analogique peut continuer à évoluer

<fragment>
L'échantillonnage signifie donc :

**à temps continu → à temps discret**
</fragment>

---

[question:AF606]

---

## Fréquence d'échantillonnage

* La *fréquence d'échantillonnage* ou *Abtastrate* indique combien d'échantillons sont enregistrés par unité de temps
* Unité : échantillons par seconde

<fragment>
Exemple CD audio :

$\num{44100}$ échantillons par seconde

correspondent à

$\qty{44,1}{\kilo\sps}$
</fragment>

<note>
Plus la fréquence d'échantillonnage est élevée, plus l'intervalle temporel entre deux échantillons consécutifs est petit.

Quelle fréquence d'échantillonnage est nécessaire au minimum sera abordé ensuite avec le théorème d'échantillonnage.
</note>

---

[question:AF615]

---

## Quantification

* Les valeurs de signal analogiques peuvent prendre n'importe quelle valeur intermédiaire : *à valeurs continues*
* En numérique, seuls un nombre fini de valeurs possibles sont disponibles : *à valeurs discrètes*
* Une valeur mesurée doit être attribuée à l'un des niveaux disponibles

<fragment>
Ce processus est appelé *quantification*.
</fragment>

<note>
Après l'échantillonnage, nous savons à quels instants nous observons le signal.

Il nous faut maintenant décider avec quelle valeur numérique digitale la valeur analogique mesurée doit être représentée.

Si la valeur réelle se situe entre deux niveaux possibles, elle est attribuée à un niveau approprié.
</note>

--- style="font-size: smaller;"

## À valeurs continues et à valeurs discrètes

<left>
[picture:410:a_wertdisk_zeitkont:Signal à valeurs discrètes et temps continu]
</left>
<right>
[picture:411:a_wertdisk_zeitdisk:Signal à valeurs et temps discrets]
</right>

* À gauche : les valeurs sont déjà discrètes, mais le temps est encore continu
* À droite : les valeurs et le temps sont discrets

<fragment>
C'est par la combinaison de **l'échantillonnage et de la quantification** que se forme la représentation digitale d'un signal analogique.
</fragment>

<note>
La représentation de gauche sert surtout à montrer que la discrétisation temporelle et la discrétisation des valeurs sont deux propriétés indépendantes.

Pour la numérisation, la représentation de droite est particulièrement importante : après échantillonnage et quantification, seuls des échantillons individuels sont disponibles, qui ne peuvent prendre qu'un nombre fini de valeurs possibles.
</note>

---

[question:AF602]

---

[question:AF604]

---

[question:AF605]

---

## Exemple pratique : variateur vs. interrupteur à gradins

* Un variateur analogique permet des réglages de luminosité fins et continus
* Un interrupteur à gradins (par exemple $\num{5}$ niveaux) ne permet que des valeurs de luminosité fixes – les valeurs intermédiaires ne sont pas possibles
* Quantification : sélection du niveau le plus proche pour représenter la valeur analogique

---
## Résumé

<left>
[include:quantisierung_und_sampling]
</left>
<right>
* L'échantillonnage détermine **quand** une valeur est considérée
* La quantification détermine **quelle valeur digitale** en résulte
* Ce n'est qu'ensemble que ces deux étapes donnent un signal à temps et à valeurs discrets
</right>

<note>
Avec l'applet, l'échantillonnage et la quantification peuvent être observés ensemble.

La fréquence d'échantillonnage influence l'intervalle temporel entre les échantillons. La quantification détermine en revanche quelles valeurs possibles les échantillons peuvent prendre.

Cela permet de comprendre à nouveau les deux étapes, initialement indépendantes, de manière conjointe.
</note>