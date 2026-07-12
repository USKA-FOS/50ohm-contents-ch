Les atténuateurs sont souvent nécessaires dans la technique HF pour atténuer de manière définie les niveaux de signal. Par exemple, un atténuateur de puissance peut réduire la puissance de sortie d'un émetteur de manière à ne pas endommager ou surcharger les appareils de mesure connectés. On utilise également des atténuateurs pour réduire les niveaux d'entrée pour les amplificateurs et les récepteurs à une valeur définie.

Un atténuateur doit toujours être conçu pour une impédance de système définie en ce qui concerne l'entrée et la sortie. Dans le cas d'atténuateurs symétriques, les impédances d'entrée et de sortie sont identiques. Il s'agit souvent des $\qty{50}{\ohm}$ habituels dans la technique HF. Pour qu'un atténuateur présente les impédances requises à son entrée et à sa sortie, une terminaison correcte de l'impédance des deux côtés est nécessaire. Cela est réalisé par un réseau de résistances approprié. L'atténuation est indiquée en dB (décibels) et se réfère à la puissance ; ainsi, par exemple, $\qty{20}{\dB}$ signifie une atténuation de la puissance d'entrée d'un facteur de $\num{100}$. La puissance de sortie après cet atténuateur n'est donc plus que $\frac{1}{100}$ de la puissance d'entrée, ce qui, dans le cas d'une puissance d'entrée de $\qty{100}{\watt}$, correspond à une puissance de sortie de $\qty{1}{\watt}$.

Dans le cas des atténuateurs ohmiques, l'atténuation se fait par conversion de la puissance injectée en chaleur. Par exemple, si un signal de $\qty{100}{\watt}$ est atténué de $\qty{20}{\dB}$ comme décrit précédemment, $\qty{99}{\watt}$ sont convertis en chaleur dans l'atténuateur. La puissance restante de $\qty{1}{\watt}$ est alors encore disponible à la sortie de l'atténuateur.

[question:AD806]
[question:AD803]
[question:AD804]
[question:AD805]

Un atténuateur symétrique peut être constitué, par exemple, d'un réseau T ou Pi de résistances. La dénomination résulte ici de l'apparence de l'arrangement des résistances dans le circuit.

<margin>
[picture:342:daempfungsglied_pi:Atténuateur en configuration PI avec source et résistance de charge]
</margin>

<margin>
[picture:341:daempfungsglied_t:Atténuateur en configuration T avec source et résistance de charge]
</margin>

%TODO: ÉVENTUELLEMENT INSÉRER PI COMME CARACTÈRE SPÉCIAL

[question:AD801]
[question:AD802]



