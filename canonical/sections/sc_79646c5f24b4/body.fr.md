Plus le signal porteur en AM est modulé, plus son amplitude varie au cours du temps. Sans modulation, seule la porteuse HF est émise avec une amplitude constante (cf. figure [ref:modulationsgrad_0]). À mesure que la modulation augmente, l'amplitude de la porteuse HF suit de plus en plus le signal BF modulant, ce qui donne lieu à l'enveloppe caractéristique (cf. figure [ref:modulationsgrad_10]).

Le *taux de modulation* $m$ est déterminé par le rapport entre l'amplitude du signal BF modulant et l'amplitude de la porteuse non modulée. Pour un taux de modulation de $m=1$ ou $\qty{100}{\percent}$, la porteuse est entièrement exploitée. L'enveloppe oscille alors entre zéro et le double de l'amplitude de la porteuse non modulée (cf. figure [ref:modulationsgrad_100]).

[question:AE201]

<margin>
[picture:27:modulationsgrad_0:Taux de modulation de $\qty{0}{\percent}$ d'un signal AM]
[picture:26:modulationsgrad_10:Taux de modulation de $\qty{10}{\percent}$ d'un signal AM]
[picture:24:modulationsgrad_100:Taux de modulation de $\qty{100}{\percent}$ d'un signal AM]
</margin>

---

Dès que le taux de modulation dépasse $m=1$ ou $\qty{100}{\percent}$ (cf. figure [ref:modulationsgrad_1000]), on parle de *surmodulation*. L'enveloppe atteint alors non seulement la valeur zéro, mais changerait mathématiquement de polarité. Cela empêche le signal d'être restitué sans distorsion par un démodulateur d'enveloppe classique.

Dans les émetteurs réels, la surmodulation peut également entraîner une limitation et donc des composantes spectrales indésirables supplémentaires, appelées *splatter de bande latérale*. Pour éviter cela, le taux de modulation en AM classique ne doit pas dépasser $\qty{100}{\percent}$.

<margin>
[picture:28:modulationsgrad_1000:Taux de modulation de $> \qty{100}{\percent}$ (surmodulation) d'un signal AM]
</margin>

[question:AE204]
[question:AE203]

---

Le taux de modulation se calcule à l'aide de la formule suivante (incluse dans la figure [ref:modulationsgrad] du *recueil de formules*):

$m = \frac{\hat{U}_\mathrm{mod}}{\hat{U}_\mathrm{T}}$

<margin>
[picture:328:modulationsgrad:Taux de modulation d'un signal AM]
</margin>

Essayez maintenant, dans la question suivante, de lire les valeurs et de calculer le taux de modulation $m$:

[question:AE202]