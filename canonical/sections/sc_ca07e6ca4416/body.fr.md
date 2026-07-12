Une boucle à verrouillage de phase (PLL) sert à synchroniser un oscillateur variable, potentiellement instable (VCO – Voltage Controlled Oscillator) à l'aide d'un oscillateur de référence stable. Le comparateur de phase entre les deux signaux est utilisé pour générer une fréquence de sortie stable.

Structure de base et éléments d'une PLL

Une PLL se compose essentiellement des composants suivants:
1. **Comparateur de phase:** Compare les phases des signaux du VCO et de l'oscillateur de référence.
2. **Filtre passe-bas:** Convertit les impulsions générées par le comparateur de phase en une tension continue.
3. **Oscillateur commandé en tension (VCO):** Génère le signal de sortie, dont la fréquence est contrôlée par la tension continue fournie par le filtre passe-bas.

En outre, la PLL peut être complétée par un **diviseur de fréquence** pour synchroniser la fréquence du VCO sur des multiples de la fréquence de référence.

Principe de fonctionnement

1. **Comparaison de phase et correction**:  

Le comparateur de phase mesure la différence de phase entre les signaux du VCO et de l'oscillateur de référence. En cas de déphasage, il émet des impulsions correspondant à l'erreur. Ces impulsions sont lissées par le filtre passe-bas et converties en une tension continue proportionnelle.

2. **Régulation du VCO**:  

La tension continue générée sert de signal de commande pour le VCO, qui ajuste sa fréquence de sorte que la différence de phase se réduise progressivement à zéro. Lorsque cet état est atteint, on dit que la PLL est « verrouillée » (locked).

3. **État verrouillé**:  

Dans l'état stable de la PLL, les fréquences et les phases des deux signaux sont identiques. La fréquence de sortie est stable et correspond essentiellement à la fréquence de référence ou à ses multiples (selon le rapport de division choisi du diviseur de fréquence).

<margin>
[picture:45:a_oszillator_pll_pll:Représentation d'une boucle à verrouillage de phase (PLL)]  
</margin>

[question:AD701]
[question:AD702]

Précision et stabilité

La précision et la stabilité de la fréquence de sortie de la PLL dépendent principalement de la qualité de l'oscillateur de référence, qui est généralement un oscillateur à quartz.

[question:AD705]

Division de fréquence et accordabilité

Pour régler une PLL sur différentes fréquences, un diviseur de fréquence peut être utilisé dans le circuit de régulation. Cela permet de générer la fréquence de sortie comme un multiple entier de la fréquence de référence. Le plus petit intervalle de fréquence sélectionnable correspond à la fréquence de l'oscillateur de référence, car la division ne peut se faire que par étapes entières.

[question:AD703]

Calcul du rapport de division

Pour obtenir une fréquence de sortie donnée avec une fréquence de référence donnée, le facteur de division est choisi de manière à ce que la même fréquence soit présente aux entrées du comparateur de phase. Cela permet de calculer le rapport de division nécessaire pour la fréquence de sortie souhaitée.

[question:AD704]
