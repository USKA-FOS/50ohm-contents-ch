Grâce à sa simplicité de mise en œuvre, le redresseur en pont est un montage redresseur très couramment utilisé. Il nécessite un transformateur et 4 diodes.

<latexonly>
Dans l'illustration [ref:a_brueckenlgeichrichter], un tel redresseur en pont est représenté.

<margin>
[picture:965:a_brueckenlgeichrichter:Redresseur en pont]
</margin>
</latexonly>

<webonly>
Dans l'applet ci-contre, un tel redresseur en pont est représenté. En observant la polarité de la tension du transformateur $U_a$ ou $U_s$, on peut suivre l'évolution du courant de charge dans sa courbe et constater qu'il circule toujours dans le même sens à travers la résistance de charge $R$.

<margin>
[include:applet_gleichrichter_2]
</margin>
</webonly>

<tip>
[picture:67:a_brueckenlgeichrichter_2:Disposition des diodes dans le redresseur en pont]
Dans le redresseur en pont, les diodes sont orientées avec leurs cathodes vers le pôle positif et leurs anodes vers le pôle négatif. On peut donc retenir : les "barres" des diodes se rejoignent à la sortie positive. Cette disposition ne doit pas être confondue avec celle d'un mélangeur à diodes en anneau, que nous découvrirons plus tard.
</tip>

[question:AD305]

---

Si l'on ajoute un condensateur de lissage $C_L$ et un filtre LC (voir illustration [ref:a_netzteil_Ucs]) après le redresseur en pont, on obtient une amplitude plus faible dans la tension continue de sortie pulsée. On dispose ainsi d'une alimentation conventionnelle.

<margin>
[picture:66:a_netzteil_Ucs:Montage redresseur avec filtrage]
</margin>

Dans le redresseur en pont également, le condensateur se charge à la tension de crête $\hat{U}$ de la tension secondaire $U_{\mathrm{sek}}$ du transformateur.

$\hat{U}=U_{\mathrm{eff}}\cdot\sqrt{2}$

Il faut également tenir compte du rapport de transformation $ü$ du transformateur. Avec ces connaissances, nous pouvons résoudre l'exercice suivant.

[question:AD306]

<indepth>
[photo:296: Formes de construction du redresseur en pont : Formes de construction de redresseurs en pont]
Il faut veiller à la bonne identification des bornes.

1. Redresseur en pont haute intensité 26 MB 20 A ($\(\qty{200}{\volt}$, $\(\qty{25}{\ampere}$) en boîtier métallique pour montage direct sur un radiateur
2. B80 C 5000/3300 signifie : tension de service maximale $\(\qty{80}{\volt}$, charge capacitive max. $\(\qty{2500}{\micro\farad}$ avec résistance de protection $R = \qty{1}{\ohm}$, courant de charge permanent maximal : $\(\qty{5000}{\milli\ampere}$ avec radiateur, $\(\qty{3300}{\milli\ampere}$ sans radiateur
3. Redresseur en pont BY 225 - boîtier particulier
4. Forme ronde d'un redresseur en pont B 80 C 1000
5. B40 C 1500 - il faut veiller à l'ordre modifié des connexions
6. FPU 4M ($\(\qty{1000}{\volt}$, $\(\qty{4}{\ampere}$)
7. Ordre des connexions estampillé dans le plastique
</indepth>
