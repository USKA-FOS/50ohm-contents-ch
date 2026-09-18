Jusqu’à présent, nous avons étudié l’ASK et la PSK. Il peut sembler naturel, pour ces deux procédés, de choisir un nombre de symboles aussi grand que possible afin de transmettre autant d’informations que possible par symbole. Cependant, le récepteur doit alors pouvoir distinguer de nombreuses amplitudes différentes, ce qui rend le procédé plus sensible aux perturbations.

Pour atténuer ce problème, on peut recourir à un astuce : au lieu de modifier un seul paramètre (par exemple l’amplitude), on fait varier deux paramètres par symbole, à savoir l’amplitude et la phase. Un symbole correspond alors à une combinaison d’une amplitude et d’une phase déterminées. Ainsi, malgré un nombre réduit d’amplitudes et de phases distinctes, on obtient un plus grand nombre de symboles. À débit de symboles égal, on peut donc transmettre davantage de bits par seconde. Ce procédé est appelé *modulation d’amplitude en quadrature* (QAM).

L’illustration [ref:a_8qam] montre un signal 8-QAM dans le domaine temporel. Chaque symbole possède une amplitude, une phase et une séquence de 3 bits définie par le mappage. Chaque symbole permet ainsi de transmettre trois bits. L’illustration [ref:a_16qam] présente un mappage 16-QAM dans le diagramme de constellation. Chaque symbole correspond à une combinaison d’une amplitude et d’une phase déterminées. Chaque symbole permet ainsi de transmettre quatre bits.

<margin>
[picture:702:a_8qam:Évolution temporelle d’un signal 8-QAM, chaque symbole avec amplitude ($\num{0,5}$ ou $\num{1}$), phase et séquence de 3 bits]
[picture:1061:a_16qam:Diagramme I-Q pour un mappage 16-QAM]
</margin>

[question:AE403]

---

Après avoir découvert la représentation I/Q, le diagramme de constellation et la modulation d’amplitude en quadrature, la question se pose de savoir comment un tel signal peut être généré techniquement. On peut utiliser pour cela un *modulateur I/Q*.

Un modulateur I/Q fonctionne avec deux porteuses de même fréquence, déphasées de $\qty{90}{\degree}$ l’une par rapport à l’autre. La première porteuse est pondérée par le signal I et la porteuse déphasée de $\qty{90}{\degree}$ par le signal Q. L’illustration [ref:a_iq_modulator] montre le schéma bloc d’un modulateur I/Q.

Les deux porteuses modulées sont ensuite additionnées. Selon les valeurs de I et Q, on obtient un signal d’amplitude et de phase déterminées. En modifiant les valeurs de I et Q, on peut ainsi faire varier l’amplitude et la phase du signal résultant.

<margin>
[picture:196:a_iq_modulator:Schéma bloc d’un modulateur I/Q]
</margin>

<webonly>
<indepth>
Tout cela peut être décrit mathématiquement. Pour la somme d’une porteuse cosinus et d’une autre porteuse cosinus déphasée de $\qty{90}{\degree}$, on a la relation suivante :

$ I(t)\cdot \cos\left(\omega t\right) + Q(t)\cdot \cos\left(\omega t + \qty{90}{\degree}\right)=A \cdot \cos\left(\omega t+\phi\right) $

On obtient donc un nouveau signal cosinus d’amplitude

$A=\sqrt{I(t)^2 + Q(t)^2}$ 

et de déphasage

$ \phi = \operatorname{atan2}\left(Q(t),I(t)\right)$

[include:applet_iq]
</indepth>
</webonly>

[question:AF632]
[question:AE404]

Dans un système numérique, les valeurs de I et Q peuvent être générées très simplement par logiciel. Par exemple, un microcontrôleur, un processeur de signal ou un SDR associe à chaque symbole à transmettre deux valeurs numériques pour I et Q. Un point du diagramme de constellation correspond ainsi directement à un couple de valeurs $(I,Q)$.

Pour une 16-QAM, on pourrait par exemple utiliser quatre valeurs différentes pour I et Q. Leur combinaison génère les $\num{16}$ points de signal différents. Le logiciel n’a qu’à fournir, pour chaque symbole, les valeurs I et Q correspondant au point de signal souhaité.

Les valeurs numériques initiales pour I et Q peuvent ensuite être converties en tensions analogiques à l’aide de deux convertisseurs numérique-analogique (DAC) et envoyées au modulateur I/Q. Ainsi, on peut générer par logiciel pratiquement n’importe quel point du diagramme de constellation. Les *Software Defined Radios* (SDR) modernes utilisent exactement ce principe : une grande partie de la modulation n’est plus définie par des circuits analogiques câblés, mais par le calcul des signaux I et Q dans le logiciel.

---

Un modulateur I/Q n’est pas limité aux procédés de modulation numériques comme la QPSK ou la QAM. Au lieu de valeurs I et Q fixes, le logiciel peut également calculer des évolutions de signaux I et Q continûment variables. Cela permet de générer également des procédés de modulation analogiques.

Pour une modulation d’amplitude, par exemple, on fait varier la longueur du vecteur de signal résultant. Pour une modulation de phase, on fait varier son angle. Même pour une modulation de fréquence, la phase du vecteur de signal est continûment modifiée, la vitesse de cette variation de phase déterminant la fréquence instantanée. Avec deux signaux I et Q générés de manière appropriée, on peut également produire un signal à bande latérale unique (SSB).

Avec le même modulateur I/Q, on peut donc générer entre autres de l’AM, de la FM, de la PM, du SSB, de la PSK et de la QAM. Il suffit simplement de calculer différemment les signaux I et Q. Le modulateur I/Q est ainsi, pour ainsi dire, le "couteau suisse des modulateurs". C’est aussi une raison majeure de la grande flexibilité des techniques SDR modernes : le procédé de modulation utilisé est déterminé en grande partie par le logiciel, tandis que le matériel haute fréquence reste largement inchangé.