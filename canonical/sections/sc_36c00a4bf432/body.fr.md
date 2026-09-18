Contrairement à la modulation, qui a lieu côté émetteur, la démodulation des signaux dans le récepteur permet de convertir un signal modulé, par exemple, à nouveau en BF, le rendant ainsi audible ou en générant une séquence binaire dans le cas d’une transmission numérique.

Selon le type de modulation utilisé côté émetteur, une démodulation correspondante doit être effectuée côté récepteur. Différents concepts de circuits permettent cette démodulation. Nous verrons comment fonctionne la modulation numérique dans un chapitre ultérieur. Dans ce chapitre, nous nous concentrerons d’abord sur la démodulation des signaux analogiques.

La forme la plus simple de démodulation d’un signal haute fréquence est la modulation d’amplitude (AM).

Les signaux AM peuvent être démodulés au moyen d’un démodulateur à enveloppe, comme illustré dans la figure [ref:demodulator_huellkurvendemodulator_am]. Pour cela, le signal haute fréquence est d’abord sélectionné à la fréquence de réception souhaitée, par exemple au moyen d’un circuit oscillant accordé, puis redressé par une diode. Un condensateur placé en aval de la diode se charge à la valeur de crête instantanée du signal et se décharge simultanément, via une résistance montée en parallèle avec une constante de temps appropriée. Cette constante de temps est nettement supérieure à la durée d’une période du signal HF, mais bien inférieure à celle du signal BF.

<margin>
[picture:141:demodulator_huellkurvendemodulator_am:Démodulateur à enveloppe pour la démodulation des signaux AM]
</margin>

[question:AD501]


À la borne X dans la figure [ref:demodulator_huellkurvendemodulator_am_2], on observe la tension de crête redressée du signal HF, qui diminue légèrement entre les crêtes du signal HF en fonction de la constante de temps de la résistance montée en parallèle avec le condensateur. L’enveloppe du signal correspond ainsi à la BF modulée, laquelle, en raison de la constante de temps du condensateur, est superposée à un signal en dents de scie (fréquence porteuse) et correspond au signal de la figure [ref:demodulator_huellkurvendemodulator_am_abbx]. Dans les étages de traitement BF suivants (non représentés), les résidus de cette fréquence porteuse sont ensuite filtrés, de sorte que seule la BF pure subsiste en tant que signal de sortie (cf. figure [ref:demodulator_huellkurvendemodulator_am_clean]).

<margin>
[picture:607:demodulator_huellkurvendemodulator_am_2:Démodulateur à enveloppe pour la démodulation des signaux AM avec représentation du signal FI d’entrée appliqué à l’entrée du démodulateur]
[picture:146:demodulator_huellkurvendemodulator_am_abbx:Signal démodulé au point X du démodulateur à enveloppe]
[picture:147:demodulator_huellkurvendemodulator_am_clean:Signal filtré à la sortie du démodulateur à enveloppe]
</margin>

[question:AD502]

---
<margin>
[picture:841:demodulator_flankendiskriminator:Circuit oscillant utilisé comme discriminateur de flanc]

[picture:149:demodulator_flankendiskriminator_schaltung:Discriminateur de flanc FM]
</margin>

Un circuit très similaire à celui du démodulateur à enveloppe peut être utilisé pour démoduler les signaux FM. Comme illustré dans la figure [ref:demodulator_flankendiskriminator], le signal, issu de la fréquence intermédiaire dans le récepteur FM, est appliqué à un circuit oscillant accordé à une fréquence de résonance $f_\text{res}$ légèrement supérieure ou inférieure à la fréquence FI $f_\text{FI}$. Ainsi, le signal FM à démoduler se situe sur le flanc du circuit oscillant et convertit les variations de fréquence de la FM en variations d’amplitude. Au moyen du démodulateur AM placé en aval, le signal FM converti en signal AM est alors démodulé et rendu audible. Ce circuit, représenté dans la figure [ref:demodulator_flankendiskriminator_schaltung], est appelé discriminateur de flanc.

[question:AD504]

---

Les signaux modulés en FM peuvent également être démodulés au moyen d’une PLL (*Phase Locked Loop*, boucle à verrouillage de phase) (cf. figure [ref:demodulator_pll]). Dans une PLL, un oscillateur commandé en tension (VCO) est couplé à un signal d’entrée par l’intermédiaire d’une boucle à verrouillage de phase. Si la fréquence du signal d’entrée change (modulation FM), la tension de régulation du VCO suit la modulation FM. Cette tension de régulation correspond alors exactement à la modulation du signal FM, et donc à la BF modulée, et peut être prélevée sur la PLL pour un traitement ultérieur.

<margin>
[picture:77:demodulator_pll:PLL pour la démodulation des signaux FM]
</margin>

[question:AD505]

---

Pour démoduler les signaux modulés en BLU (*Bande Latérale Unique*), on utilise un détecteur de produit. Celui-ci est essentiellement un mélangeur en anneau, que nous avons déjà rencontré dans le chapitre sur les récepteurs, qui utilise comme signaux d’entrée la FI du récepteur ainsi qu’un BFO (*Beat Frequency Oscillator*, oscillateur à battement). Par le mélange (produit) de ces deux signaux d’entrée, l’un des produits de mélange obtenus est le signal BF souhaité (signal BLU), qui peut être prélevé à la sortie pour un traitement ultérieur. Pour une intelligibilité optimale de la BF démodulée, le BFO doit être accordé sur la fréquence de la porteuse supprimée du signal BLU.


<indepth>
[picture:153:demodulator_produktdetektor:Détecteur de produit pour la démodulation des signaux BLU]
[picture:1125:a_produktdetektor_spannung:Exemple de tensions au niveau du détecteur de produit]


Pour démoduler un signal BLU, on utilise souvent un *détecteur de produit*. Celui-ci peut être conçu, par exemple, comme un mélangeur en anneau. Il reçoit en entrée le signal BLU sur la fréquence intermédiaire (FI) et le signal d’un *oscillateur à battement (BFO)*.


Le fonctionnement peut être expliqué de manière simplifiée à l’aide d’un mélangeur à commutation. Le signal BFO commute le mélangeur en anneau alternativement entre deux états. De manière simplifiée, on peut considérer le signal BFO comme un signal qui bascule entre les valeurs $+1$ et $-1$, comme illustré dans la partie supérieure de la figure [ref:a_produktdetektor_spannung].

Le signal FI est ainsi alternativement transmis sans modification ou inversé en polarité. Dans cette représentation simplifiée, le signal FI peut donc être considéré comme le produit du signal BF et du signal de commutation du BFO :

$u_\text{FI}(t)=u_\text{BF}(t)\cdot s_\text{BFO}(t)$


Dans le détecteur de produit, ce signal est à nouveau multiplié par le signal BFO :

$u_\text{FI}(t)\cdot s_\text{BFO}(t)=u_\text{BF}(t)\cdot s_\text{BFO}(t)\cdot s_\text{BFO}(t)$


Comme le signal de commutation simplifié du BFO ne prend que les valeurs $+1$ et $-1$, on a :

$s_\text{BFO}^2(t)=1$


Il reste donc comme composante basse fréquence le signal BF d’origine :

$u_\text{BF}(t)=u_\text{FI}(t)\cdot s_\text{BFO}(t)$


Outre le signal BF souhaité, d’autres produits de mélange haute fréquence apparaissent lors du processus de mélange. Ceux-ci sont supprimés à la sortie du détecteur de produit par un filtre passe-bas.

Pour retrouver le signal BF d’origine avec la bonne hauteur tonale, la fréquence du BFO doit être réglée en fonction de la fréquence de la porteuse supprimée du signal BLU.
</indepth>

[question:AD506]
