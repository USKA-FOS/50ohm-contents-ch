Les atténuateurs sont souvent nécessaires en technique HF pour réduire de manière définie le niveau des signaux. Par exemple, un atténuateur de puissance peut être utilisé pour réduire la puissance de sortie d’un émetteur à un niveau tel que le signal de sortie ne risque pas d’endommager ou de surmoduler les appareils de mesure connectés. On utilise également des atténuateurs pour ajuster le niveau d’entrée des amplificateurs et des récepteurs à une valeur définie.

Un atténuateur doit toujours être conçu pour une impédance de système définie en entrée et en sortie. Dans le cas d’atténuateurs symétriques, les impédances d’entrée et de sortie sont identiques. Il s’agit souvent des $\qty{50}{\ohm}$ habituels en technique HF. Pour qu’un atténuateur présente les impédances requises à son entrée et à sa sortie, il est nécessaire de le terminer correctement en impédance des deux côtés. Cela est réalisé au moyen d’un réseau de résistances adapté.

Il existe différentes variantes de circuits qui diffèrent par l’agencement des résistances. Les deux variantes les plus courantes sont l’atténuateur en T (cf. Figure [ref:a_daempfungsglied_t]) et l’atténuateur en $\pi$ (cf. Figure [ref:a_daempfungsglied_pi]). Dans les deux cas, l’atténuation est obtenue par un réseau de résistances qui convertit la puissance fournie en chaleur.

<margin>
[picture:342:a_daempfungsglied_pi:Atténuateur en configuration π avec source et résistance de charge]
</margin>

<margin>
[picture:341:a_daempfungsglied_t:Atténuateur en configuration T avec source et résistance de charge]
</margin>

[question:AD801]
[question:AD802]

---

L’atténuation d’un atténuateur est généralement indiquée en dB (décibels) et se réfère à la puissance. Par exemple, $\qty{20}{\dB}$ signifie une atténuation de la puissance d’entrée d’un facteur $\num{100}$. La puissance de sortie après cet atténuateur ne représente donc plus que $\frac{1}{100}$ de la puissance d’entrée, ce qui, dans le cas d’une puissance d’entrée de $\qty{100}{\watt}$, correspond à une puissance de sortie de $\qty{1}{\watt}$.

Dans le cas d’atténuateurs ohmiques, l’atténuation est obtenue par conversion de la puissance fournie en chaleur. Si, par exemple, un signal de $\qty{100}{\watt}$ est atténué de $\qty{20}{\dB}$ comme décrit précédemment, $\qty{99}{\watt}$ sont dissipés sous forme de chaleur dans l’atténuateur. La puissance restante de $\qty{1}{\watt}$ est alors disponible à la sortie de l’atténuateur.

[question:AD806]
[question:AD803]
[question:AD804]
[question:AD805]

Un atténuateur symétrique peut être réalisé, par exemple, sous la forme d’un réseau en T ou en $\pi$ composé de résistances. La dénomination provient de l’aspect visuel de l’agencement des résistances dans le circuit.

<indepth>
Les valeurs des résistances pour un atténuateur en $\pi$ pour une impédance de $\qty{50}{\ohm}$ peuvent être calculées à l’aide des formules suivantes :

$R_1 = R_3 = \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}+1}{10^{\frac{a}{20}}-1}\right)$

Ici, $a$ représente l’atténuation souhaitée en $\unit{\dB}$.

$R_2 = \frac{\qty{50}{\ohm}}{2} \cdot \left( 10^{\frac{a}{20}} - \frac{1}{10^{\frac{a}{20}}}\right)$

Les valeurs des résistances pour un atténuateur en T pour une impédance de $\qty{50}{\ohm}$ peuvent être calculées à l’aide des formules suivantes :

$R_1 = R_2 = \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}-1}{10^{\frac{a}{20}}+1} \right)$

$R_3 = 2\cdot \qty{50}{\ohm} \cdot \left( \frac{10^{\frac{a}{20}}}{10^{\frac{a}{10}}-1} \right)$

<webonly>
[include:applet_daempfungsglied]
</webonly>

</indepth>

