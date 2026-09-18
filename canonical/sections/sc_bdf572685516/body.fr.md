Une ligne d’alimentation peut être représentée comme un circuit composé de nombreuses petites inductances et capacités, comme illustré dans la figure [ref:a_wellenwiderstand]. À partir de ces grandeurs linéiques appelées inductance linéique $L'$ en $\unit{\henry\per\meter}$ et capacité linéique $C'$ en $\unit{\farad\per\meter}$, on déduit l’impédance caractéristique $Z$ de la ligne. En général, on a :

$Z_0 = \sqrt{\frac{L'}{C'}}.$

<margin>
[picture:1108:a_wellenwiderstand:Impédance caractéristique d’une ligne d’alimentation]

| X: Propriété                  | l: Valeur                               |
| Impédance                     | $\qty{50}{\ohm}$                      |
| Bande de fréquences           | $ < \qty{1}{\giga\hertz}$             |
| Capacité linéique             | $\qty{100}{\pico\farad\per\meter}$    |
| Inductance linéique           | $\qty{0,25}{\micro\henry\per\meter}$  |
| Vitesse de propagation        | $\qty{0,66}{\percent}$                |
[table:a_rg58:Caractéristiques techniques extraites d’une fiche technique d’un câble coaxial RG-58]
</margin>

Le tableau [ref:a_rg58] présente les caractéristiques techniques d’un câble coaxial RG-58. L’impédance caractéristique est de $\qty{50}{\ohm}$, la capacité linéique de $\qty{100}{\pico\farad\per\meter}$ et l’inductance linéique de $\qty{0,25}{\micro\henry\per\meter}$. À partir de ces valeurs, on peut calculer l’impédance caractéristique à l’aide de la formule ci-dessus :

$Z_0 = \sqrt{\frac{\qty{0,25}{\micro\henry\per\meter}}{\qty{100}{\pico\farad\per\meter}}} = \sqrt{2500} = \qty{50}{\ohm}$

Si ces valeurs de capacité linéique et d’inductance linéique ne sont pas connues, il existe des formules dans le recueil de formules qui reposent sur les dimensions géométriques de la ligne et la permittivité relative du diélectrique.

L’impédance caractéristique $Z_0$ d’une ligne bifilaire symétrique dépend, par exemple, de la distance entre les conducteurs ($a$) et de leur diamètre ($d$), ainsi que de la permittivité relative $\epsilon_\mathrm{r}$ du diélectrique situé entre eux. L’équation indiquée dans le recueil de formules est valable pour $a/d > 2,5$ :

$Z_0 = \dfrac{\qty{120}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{2\cdot a}{d}\right)}$

Ici, $\ln$ désigne le logarithme naturel.

[question:AG305]

L’impédance caractéristique $Z_0$ d’une ligne coaxiale dépend du rapport entre le diamètre intérieur du conducteur extérieur ($D$) et le diamètre du conducteur intérieur ($d$), ainsi que du diélectrique situé entre eux. D’après le recueil de formules, on a :

$Z_0 = \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{D}{d}\right)}$

Ici, $\ln$ désigne le logarithme naturel et $\epsilon_\mathrm{r}$ la permittivité relative du diélectrique.

[question:AG306]
[question:AG307]

Lorsqu’une ligne est terminée par une impédance égale à son impédance caractéristique, c’est-à-dire lorsqu’un composant ou une antenne présentant exactement la même résistance que l’impédance caractéristique de la ligne est connecté à une extrémité, on parle d’adaptation. Dans ce cas, les ondes ne sont pas réfléchies à cette extrémité du câble.

[question:AG304]