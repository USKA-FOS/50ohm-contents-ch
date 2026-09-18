Dans le chapitre précédent, nous avons étudié le [montage à collecteur commun](#) d’un [transistor](#) bipolaire. Dans ce chapitre, nous examinons le [*montage à émetteur commun*](#).


<margin>
[picture:1118:a_emitter_collector:Montages à émetteur et à collecteur commun avec les bornes Base (B), Collecteur (C) et Émetteur (E)]


Résumons brièvement les propriétés des montages à émetteur et à collecteur commun dans le tableau suivant :


| l: Propriété | X: Montage à émetteur commun | X: Montage à collecteur commun |
| Décalage de phase | $\qty{180}{\degree}$ | $\qty{0}{\degree}$ |
| [gain en tension](#) | $\num{100}\dots\num{300}$ | $\num{0,9}\dots\num{0,98}$ |
| [impédance d'entrée](#) | élevée | élevée |
| [impédance de sortie](#) | élevée | faible |
</margin>

Comme nous l’avons appris dans le chapitre précédent, la désignation des montages de base d’un [transistor](#) bipolaire se fait en fonction de la borne qui n’est ni l’entrée ni la sortie du circuit et qui sert donc de point de référence commun pour les circuits d’entrée et de sortie. Dans le montage à émetteur commun, il s’agit de l’[émetteur](#).


---

[question:AD409]


<tip>
Les circuits amplificateurs à [transistors](#) bipolaires sont nommés d’après la borne à laquelle ni l’entrée ni la sortie ne sont directement connectées (cf. figure [ref:a_emitter_collector]).
</tip>

---

La figure [ref:a_emitterschaltung] montre un montage à émetteur commun simple avec [alimentation électrique](#), résistance de collecteur et condensateurs de couplage.


Pour fonctionner en amplificateur linéaire de [tension](#), le [transistor](#) dans le montage à émetteur commun nécessite un [point de fonctionnement](#) défini (en anglais *bias*, polarisation), qui est généralement établi par un [diviseur de tension](#) sur la [base](#).


<margin>
[picture:136:a_emitterschaltung:Montage à émetteur commun]
</margin>

[question:AD411]


La résistance de collecteur convertit le courant circulant dans la jonction collecteur-émetteur en une chute de [tension](#) prélevée au collecteur. Le courant de collecteur du [transistor](#) circule (avec la composante de courant de [base](#), généralement négligeable) via l’[émetteur](#) à travers la résistance d’émetteur vers la [masse](#). Le courant traversant la résistance d’émetteur provoque, par la chute de [tension](#) qui en résulte, une augmentation du potentiel de l’émetteur (tension d’émetteur) et agit ainsi comme contre-réaction sur la [tension](#) de [base](#). Cela permet de stabiliser davantage le [point de fonctionnement](#) du [transistor](#), car les variations thermiques du courant de collecteur sont ainsi compensées.


L’entrée et la sortie des signaux sur la [base](#) et le collecteur s’effectuent via des condensateurs de couplage. Ceux-ci ont pour fonction d’empêcher les composantes de [tension continue](#) de la cellule amplificatrice, qui modifieraient le [point de fonctionnement](#), d’atteindre la cellule.


[question:AD412]


Le condensateur de découplage sur l’[alimentation électrique](#) (+) sert à évacuer les signaux HF et BF indésirables afin d’éviter les effets de rétroaction sur la cellule et sur la [tension d'alimentation](#).


Le déphasage entre le signal d’entrée et le [signal de sortie](#) est de $\qty{180}{\degree}$ dans le montage à émetteur commun, car lors d’une demi-onde positive de la [tension d'entrée](#) sur la [base](#), le courant de collecteur augmente et la chute de [tension](#) aux bornes de la résistance de collecteur s’accroît. La [tension](#) au condensateur de sortie diminue alors, ce qui produit une demi-onde négative en sortie de la cellule amplificatrice.


[question:AD407]
[question:AD408]


Le [gain en tension](#) du montage à émetteur commun, avec un dimensionnement approprié, se situe dans la plage de $100\dots 300$ et est donc très élevé par rapport au montage à collecteur commun.


[question:AD410]


Le condensateur sur l’[émetteur](#) shunte la résistance d’émetteur pour les [tensions alternatives](#), réduisant ainsi la contre-réaction et augmentant le [gain en tension alternative](#), tandis que le [point de fonctionnement](#) en courant continu reste inchangé.


[question:AD413]


Si le condensateur d’émetteur est retiré, le facteur d’amplification de la cellule diminue considérablement (par exemple, de $\num{100}$ à $\num{10}$). Il est alors défini principalement par le rapport entre la résistance de collecteur et la résistance d’émetteur.


[question:AD414]
[question:AD415]


Si un montage à émetteur commun est utilisé, comme dans la question suivante, sans polarisation préalable par un [diviseur de tension](#), la [commande](#) du [transistor](#) se fait uniquement par le signal d’entrée appliqué. Ce n’est que lorsque ce signal dépasse environ $\qty{0,6}{\volt}$ que la jonction base-émetteur du [transistor](#) devient conductrice. Le courant de collecteur ne circule alors que lors des pics de [tension](#), provoquant une chute de [tension](#) en sortie. Le [signal de sortie](#) correspond à la [tension de service](#), qui chute aux moments où le [transistor](#) devient conducteur.


[question:AD406]
