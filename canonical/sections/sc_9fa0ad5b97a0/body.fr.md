Toutes les antennes n’ont pas, à leur point d’alimentation, exactement l’impédance requise pour être connectées à une ligne d’alimentation ou à un émetteur spécifique. Si l’impédance s’écarte par exemple des $\qty{50}{\ohm}$ habituels, elle doit être adaptée de manière appropriée pour que la puissance HF soit transmise avec le moins de pertes possible. Pour cela, l’impédance existante est *transformée* en une autre impédance souhaitée. Ce processus est appelé *transformation d’impédance* ou *adaptation d’impédance*.

Il existe différentes méthodes pour réaliser l’adaptation ou la transformation d’impédance. Les plus couramment utilisées sont par exemple :

* Les transformateurs,
* Les lignes de $\frac{\lambda}{4}$ ou
* Les réseaux d’adaptation composés de bobines et de condensateurs.

Nous avons déjà abordé les transformateurs avec l’antenne alimentée en extrémité et son Unun 1:49. Dans ce qui suit, nous examinerons donc plus en détail deux autres méthodes : la transformation d’impédance à l’aide de lignes de $\frac{\lambda}{4}$ (présentées dans la section précédente) et l’adaptation avec des réseaux LC. Commençons par un rappel sur les lignes de transformation, où il importe peu qu’il s’agisse d’une ligne d’alimentation symétrique ou d’une ligne coaxiale asymétrique : la transformation fonctionne dans les deux cas.

Pour une ligne dont la longueur électrique est de $\lambda/4$, les résistances actives inférieures à l’impédance caractéristique de la ligne sont transformées en résistances supérieures à cette impédance caractéristique. Inversement, les résistances actives supérieures à l’impédance caractéristique de la ligne sont transformées en résistances inférieures à cette impédance. On utilise cette propriété, par exemple, pour adapter des antennes à haute impédance à un système à basse impédance ($\qty{50}{\ohm}$).

[question:AG410]
[question:AG409]

Pour une longueur de ligne de $\lambda/2$, l’effet s’annule et aucune transformation d’impédance ne se produit.

[question:AG412]
[question:AG416]

Pour les questions suivantes, rappelons qu’un dipôle demi-onde est alimenté en courant (basse impédance) et qu’un dipôle onde entière est alimenté en tension (haute impédance).

[question:AG413]
[question:AG414]
[question:AG415]

Si l’on souhaite transformer une impédance vers une valeur de résistance spécifique, l’impédance caractéristique nécessaire se calcule comme la moyenne géométrique entre la résistance de charge $Z_\mathrm{A}$ et la résistance d’alimentation souhaitée $Z_\mathrm{E}$ à l’autre extrémité du câble :

$Z = \sqrt{Z_\mathrm{E} \cdot Z_\mathrm{A}}$

[question:AG417]
[question:AG418]

---

Les bobines et les condensateurs sont également souvent utilisés pour l’adaptation d’impédance. On trouve fréquemment le filtre en π, qui, en plus de son rôle de passe-bas, effectue une transformation d’impédance. Un tel filtre en π peut donc aussi servir d’accordeur d’antenne.

<indepth>
*Le nom « filtre en π »* provient de la disposition des composants dans le schéma électrique, qui rappelle la lettre grecque $\pi$, et n’a aucun rapport avec le nombre Pi $\pi$.
</indepth>

[question:AG406]
