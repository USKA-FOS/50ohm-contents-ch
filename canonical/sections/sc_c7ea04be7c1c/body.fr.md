Un vieux dicton de radioamateur dit que le meilleur amplificateur haute fréquence est l'antenne. Dans les premières années de la technique radio, elle était le seul "amplificateur", car il n'existait pas encore d'électronique amplificatrice. En 1907, le tube électronique fit son apparition : un composant très performant, mais encombrant et peu efficace. Dès les années 1920, les scientifiques rêvaient de composants offrant une fonction similaire, mais dont le fonctionnement interne se déroulerait entièrement dans un solide (semi-conducteur) et non dans le vide. Le premier composant à concrétiser cela en pratique fut, en 1947/1948, le *transistor bipolaire*, qui fait également l'objet de questions d'examen.

[question:EC602]

<indepth>
Le *transistor bipolaire* est également appelé BJT (*Bipolar Junction Transistor*) en anglais, soit transistor bipolaire à jonction en français.
</indepth>

La fonction idéale de tous les types de transistors, y compris le tube électronique, est celle d'une *source de courant commandée en tension* : une petite variation de tension à l'entrée doit provoquer une grande variation de courant à la sortie.

Le transistor bipolaire possède trois broches, appelées émetteur, base et collecteur. L'émetteur émet des porteurs de charge vers la base — pour un transistor bipolaire NPN, il s'agit d'*électrons*, et pour un transistor PNP, de *trous* (ou *défauts d'électrons*). La physique derrière ces concepts sera abordée dans la formation pour la classe A. Ces porteurs de charge traversent la base et sont collectés par le collecteur.

---

L'illustration [ref:e_npn_pnp_symbol] montre les symboles de circuit des transistors NPN et PNP. L'électrode d'émetteur est reconnaissable à une flèche : elle pointe vers la base pour le transistor PNP et s'éloigne de la base pour le transistor NPN.

<margin>
[picture:864:e_npn_pnp_symbol:Symboles de transistors NPN et PNP]
</margin>

[question:EC605]
[question:EC606]
[question:EC607]
[question:EC608]
[question:EC609]

---

Les transistors bipolaires sont composés de deux diodes — la diode émetteur-base et la diode base-collecteur. 
En fonctionnement actif, la diode émetteur-base est toujours polarisée en direct. Pour un transistor NPN, le potentiel de la base doit alors être plus positif que celui de l'émetteur, et pour un transistor PNP, plus négatif. La diode base-collecteur est polarisée en inverse. Pour cela, le potentiel du collecteur doit être plus positif que celui de la base dans un transistor NPN, et plus négatif dans un transistor PNP.

<tip>
La fonction du transistor ne s'établit que si la zone de base entre l'émetteur et le collecteur ne dépasse pas quelques micromètres d'épaisseur. Il n'est donc pas possible de fabriquer un transistor en soudant simplement deux diodes séparées l'une à l'autre.
</tip>

La tension minimale au niveau de la jonction émetteur-base dépend du semi-conducteur utilisé. Pour un transistor NPN en silicium, la base doit être environ $\qty{0,6}{\volt}$ plus positive que l'émetteur, et pour un transistor PNP en silicium, environ $\qty{0,6}{\volt}$ plus négative. Cette tension est appelée tension base-émetteur $U_\mathrm{BE}$.

[question:EC610]
[question:EC612]
[question:EC613]
[question:EC614]
[question:EC615]

---

<margin>
[picture:863:e_npn_i_u:Courants et tensions dans un transistor NPN]
</margin>

---

Les courants et tensions dans un transistor NPN sont illustrés dans l'image [ref:e_npn_i_u]. Nous connaissons déjà la tension base-émetteur $U_\mathrm{BE}$. Il existe également la tension collecteur-base $U_\mathrm{CB}$ et la tension collecteur-émetteur $U_\mathrm{CE}$. Le courant de collecteur $I_\mathrm{C}$ dépend exponentiellement de la tension base-émetteur :

$I_\mathrm{C} = I_\mathrm{S}\ e^{\frac{U_\mathrm{BE}}{U_\mathrm{T}}}$

À température ambiante, $U_\mathrm{T}$ vaut environ $\qty{26}{\milli\volt}$.

<indepth>
$I_\mathrm{S}$ désigne le courant de saturation inverse d'un transistor bipolaire. Il s'agit d'un paramètre caractéristique du composant et est étroitement lié à la diode émetteur-base. Il s'agit d'un très faible courant de fuite qui traverse le transistor même lorsque la jonction base-émetteur n'est pas conductrice.
</indepth>

Le courant de base $I_\mathrm{B}$ présente, dans de larges plages de fonctionnement, la même dépendance en tension que le courant de collecteur, de sorte que le rapport entre le courant de collecteur et le courant de base reste constant :

$\frac{I_\mathrm{C}}{I_\mathrm{B}} = B$

*$B$* est le gain en courant (plus précisément, le gain en courant en montage à émetteur commun). Il est souvent plus pratique de considérer le transistor comme un composant commandé en courant, même si ce n'est pas le cas physiquement. Le gain en courant des transistors pratiques varie entre $50$ et $350$.

<tip>
Pour la commande en courant du transistor bipolaire, il existe une analogie ancienne impliquant un grand et un petit canal d'eau, une écluse dans le grand canal et un volet de commande. Les plus âgés d'entre nous s'en souviennent peut-être grâce au "Petit Radioamateur" des éditions Kosmos ...

[picture:835:e_transistor_wehr_geschlossen:Le canal de commande ferme complètement l'écluse]

Au début, aucun courant ne circule dans le petit canal. L'écluse dans le grand canal est fermée, donc aucun courant n'y circule non plus.

[picture:837:e_transistor_wehr_halb_offen:Le canal de commande ouvre l'écluse à moitié]

Puis de l'eau commence à circuler dans le petit canal, le canal de commande. L'eau soulève le volet, qui actionne à son tour l'écluse — de l'eau commence également à circuler dans le canal principal.

[picture:836:e_transistor_wehr_geoeffnet:Le canal de commande ouvre complètement l'écluse]

Maintenant, plus d'eau circule dans le canal de commande, le volet se soulève davantage, et l'écluse dans le canal principal s'ouvre complètement.
</tip>

[question:EC603]

Le courant d'émetteur $I_E$ est la somme du courant de collecteur et du courant de base :

$I_\mathrm{E} = I_\mathrm{C} + I_\mathrm{B}$

[question:EC611]

Le point de fonctionnement en tension des transistors est généralement indiqué par la tension collecteur-émetteur :

$U_\mathrm{CE} = U_\mathrm{CB} + U_\mathrm{BE}$

Outre les transistors bipolaires principalement traités ici, il existe surtout les *transistors à effet de champ*, qui fonctionnent différemment sur le plan physique, mais offrent extérieurement la même fonction de base (source de courant commandée en tension). Sous forme de MOSFET, ils dominent notre électronique, car ils sont présents à des millions, voire des milliards d'exemplaires dans les circuits intégrés de l'électronique numérique.

<indepth>
MOSFET signifie *metal-oxide-semiconductor field effect transistor*, soit transistor à effet de champ métal-oxyde-semi-conducteur en français.
</indepth>

[question:EC604]

Les transistors peuvent être utilisés non seulement comme amplificateurs, mais aussi comme interrupteurs (courant allumé/éteint) ou, pour de faibles tensions en sortie, comme résistance commandable. Cette dernière fonction est principalement mise en œuvre avec des transistors à effet de champ.

[question:EC601]