--- style="font-size: smaller;"

## Filtres dans la conversion A/N et N/A

[picture:1131:a_adc_dac_filter:Conversion A/N et N/A avec filtre anti-repliement et filtre de reconstruction]

* Avant le convertisseur A/N : *filtre anti-repliement*
* Après le convertisseur N/A : *filtre de reconstruction*
* Les deux filtres suppriment les composantes fréquentielles indésirables

<note>
L'illustration montre toute la chaîne de traitement du signal, d'un signal d'entrée analogique à travers le traitement numérique du signal (DSP) jusqu'à un signal de sortie analogique.

Avant le convertisseur A/N se trouve le filtre anti-repliement. Après le convertisseur N/A se trouve le filtre de reconstruction.

Pourquoi ces deux filtres sont nécessaires, nous allons l'examiner plus en détail.
</note>

---

## Repliement spectral au convertisseur A/N

* Pour l'échantillonnage, la règle suivante s'applique : $f_\mathrm{S}>2\cdot f_\mathrm{max}$
* Le signal d'entrée peut contenir des fréquences plus élevées indésirables
* Si la fréquence d'échantillonnage est trop faible, des fréquences apparentes se produisent
* Ces fréquences sont appelées *replis spectraux*

<note>
Par une antenne, nous recevons généralement non seulement le signal souhaité, mais aussi de nombreuses autres composantes fréquentielles.

Si la fréquence d'échantillonnage est trop faible pour l'une de ces composantes, elle peut apparaître après la numérisation comme une fréquence différente de celle présente dans le signal d'origine.

Nous avons déjà rencontré cet effet lors du théorème d'échantillonnage.
</note>

--- style="font-size: smaller;"

## Filtre anti-repliement

[picture:1131:a_adc_dac_filter_aa:Conversion A/N et N/A avec filtre anti-repliement et filtre de reconstruction]

* Le filtre se trouve *avant* le convertisseur A/N
* Il limite la bande de fréquences du signal d'entrée
* Des filtres passe-bas ou passe-bande peuvent être utilisés
* Les composantes fréquentielles critiques doivent être suffisamment supprimées

<fragment>
En particulier, les fréquences supérieures à $\frac{f_\mathrm{S}}{2}$ ne doivent pas atteindre le convertisseur A/N sans être atténuées.
</fragment>

<note>
Le filtre anti-repliement empêche que des fréquences, pour lesquelles la fréquence d'échantillonnage n'est pas suffisamment élevée, n'atteignent le convertisseur A/N.

Selon l'application, un filtre passe-bas ou passe-bande peut être utilisé. Pour les signaux vocaux, par exemple, un filtre passe-bande peut être approprié.

Il est essentiel que les composantes fréquentielles pouvant entraîner un repliement spectral soient suffisamment supprimées avant la numérisation.
</note>

---

[question:AF622]

---

[question:AF623]

---

## Générateur d'horloge d'échantillonnage

<left>
[picture:1132:a_anit_alias:Filtre anti-repliement, convertisseur A/N et générateur d'horloge]
</left>
<right>
* Le convertisseur A/N nécessite une horloge pour l'échantillonnage
* L'horloge détermine les instants des différents échantillons
* Sa fréquence définit la fréquence d'échantillonnage
* La fréquence d'horloge peut être fixe ou réglable
</right>

<note>
Le générateur d'horloge d'échantillonnage indique au convertisseur A/N quand il doit prendre un nouvel échantillon.

Sa fréquence détermine directement la fréquence d'échantillonnage. La fréquence d'horloge peut être prédéfinie ou contrôlée, par exemple, par un microcontrôleur.
</note>

---

[question:AF620]

---

## Retour au signal analogique

* Le convertisseur N/A génère à partir des échantillons numériques des valeurs de tension analogiques
* Les valeurs sont émises à intervalles de temps fixes
* En sortie, on obtient d'abord une courbe de signal non parfaitement lisse
* Les transitions abruptes contiennent des composantes fréquentielles élevées

<note>
Du côté de la sortie, le processus inverse se produit.

Le convertisseur N/A émet les différentes valeurs numériques sous forme de valeurs de tension analogiques. En raison de la sortie discrète dans le temps, on obtient d'abord une courbe non parfaitement lisse.

En particulier, les arêtes vives et les transitions contiennent des composantes fréquentielles supplémentaires de haute fréquence.
</note>

--- style="font-size: smaller;"

## Filtre de reconstruction

<left>
[picture:300:a_adc_4bit:Signal avant le filtre de reconstruction]
</left>
<right>
[picture:299:a_adc_12bit:Signal après le filtre de reconstruction]
</right>

* Le filtre de reconstruction se trouve *après* le convertisseur N/A
* Il laisse passer la bande de fréquences utile souhaitée
* Les composantes fréquentielles indésirables de haute fréquence sont supprimées
* Des filtres passe-bas ou passe-bande peuvent être utilisés

<fragment>
Cela permet d'obtenir à nouveau un signal de sortie analogique aussi propre que possible.
</fragment>

<note>
Le filtre de reconstruction élimine les composantes fréquentielles indésirables de haute fréquence en sortie du convertisseur N/A.

À gauche, un signal avant le filtrage est représenté. Les arêtes clairement visibles contiennent des composantes fréquentielles élevées.

Après le filtrage, on obtient une courbe de signal plus lisse, qui se rapproche du signal analogique souhaité.

Selon l'application, un filtre passe-bas ou passe-bande peut être utilisé.
</note>

---

[question:AF624]

---

[question:AF625]