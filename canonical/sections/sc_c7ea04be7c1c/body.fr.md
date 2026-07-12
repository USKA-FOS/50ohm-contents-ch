Un vieux dicton de radio dit que le meilleur amplificateur haute fréquence est l'antenne. Dans les premières années de la technologie radio, c'était le seul "amplificateur", il n'y avait pas d'électronique amplificatrice. En 1907, la lampe à vide est apparue - un composant très réussi, mais assez grand et peu efficace. Dès les années vingt, la science rêvait de composants fonctionnant de manière similaire, mais où tout se déroule à l'intérieur d'un solide (semi-conducteur), et non dans le vide. Le premier composant où cela a également réussi en pratique était en 1947/1948 le *transistor bipolaire*, qui est également principalement le sujet des questions d'examen de l'examen de classe E.

[question:EC602]

<indepth>
Le *transistor bipolaire* est également appelé BJT : Bipolar Junction Transistor, en allemand transistor bipolaire à jonction, en anglais bipolar junction transistor.
</indepth>

La fonction idéale de tous les types de transistors, ainsi que de la lampe à vide, est celle d'une *source de courant commandée par tension* : avec une variation de tension aussi faible que possible à l'entrée, une variation de courant aussi grande que possible doit être obtenue à la sortie.

Le transistor bipolaire a trois bornes, appelées émetteur, base et collecteur. L'émetteur envoie des porteurs de charge dans la base - dans le cas du transistor bipolaire npn, il s'agit d'*électrons*, dans le cas du transistor bipolaire pnp, de défauts d'électrons, également appelés *trous*. La physique derrière ces termes sera discutée pour la première fois lors de la formation pour la classe A. Ces porteurs de charge traversent la base et sont à nouveau collectés par le collecteur. 

---

L'illustration [ref:e_npn_pnp_symbol] montre les symboles de circuit des transistors NPN et PNP. Nous reconnaissons l'électrode d'émetteur à une flèche qui, dans le cas du transistor pnp, pointe vers la base et, dans le cas du transistor npn, s'éloigne de la base. 

<margin>
[picture:864:e_npn_pnp_symbol:Symboles NPN et PNP Transistor]
</margin>

[question:EC605]
[question:EC606]
[question:EC607]
[question:EC608]
[question:EC609]

---

Les transistors bipolaires sont composés de deux diodes - la diode émetteur-base et la diode base-collecteur.
En fonctionnement actif, la diode émetteur-base est toujours branchée dans le sens passant. Dans le cas du transistor NPN, le potentiel à la base doit être plus positif que celui de l'émetteur, et dans le cas du transistor PNP, plus négatif. La diode base-collecteur est polarisée dans le sens bloquant. À cet effet, le potentiel du collecteur doit être choisi plus positif que la base dans le cas du transistor NPN, et plus négatif dans le cas du transistor PNP.

<tip>
La fonction du transistor ne s'établit cependant que si la zone de base entre l'émetteur et le collecteur a une largeur maximale de quelques micromètres. Nous ne pouvons donc pas créer un transistor en soudant deux diodes séparées l'une à l'autre.
</tip>

La tension minimale à la jonction émetteur-base dépend du semi-conducteur utilisé. Dans le cas d'un transistor NPN en silicium, la base doit être environ $\qty{0,6}{\volt}$ plus positive que l'émetteur, et dans le cas d'un transistor PNP en silicium, environ $\qty{0,6}{\volt}$ plus négative.

[question:EC610]
[question:EC612]
[question:EC613]
[question:EC614]
[question:EC615]

---

<margin>
[picture:863:e_npn_i_u:Courants et tensions sur un transistor npn]
</margin>

---

Les courants et tensions sur un transistor npn sont représentés dans l'illustration [ref:e_npn_i_u]. Nous connaissons déjà la tension base-émetteur $U_{BE}$, ainsi que la tension collecteur-base $U_{CB}$. Le courant de collecteur $I_C$ dépend exponentiellement de la tension base-émetteur:

$I_C = I_\text{S}\ e^{\frac{U_{BE}}{U_T}}$

$U_T$ est d'environ $\qty{26}{\milli\volt}$ à température ambiante.

<indepth>
$I_\text{S}$ désigne le courant de saturation-blocage dit d'un transistor bipolaire. Il s'agit d'un paramètre caractéristique du composant et il est en étroite relation avec la diode émetteur-base. Il s'agit d'un très petit courant de fuite qui traverse également le transistor lorsque la jonction base-émetteur n'est pas conductrice.
</indepth>

Le courant de base $I_B$ a, dans de larges plages de fonctionnement, la même dépendance à la tension que le courant de collecteur, de sorte que le rapport entre le courant de collecteur et le courant de base est constant:

$\frac{I_C}{I_B} = B$

*B* est l'amplification de courant (plus précisément, l'amplification de courant en configuration émetteur). Il est souvent plus pratique de se représenter le transistor comme un composant commandé par le courant, même si ce n'est pas le cas physiquement. L'amplification de courant dans les transistors pratiques est de $50 \dots 350$.

<tip>
Pour la commande de courant du transistor bipolaire, il existe une analogie très ancienne dans laquelle un grand et un petit canal d'eau, une vanne dans le grand canal et un clapet de commande jouent un rôle. Les plus âgés d'entre nous s'en souviennent peut-être encore du "Petit Radiomann" de l'éditeur Kosmos ...
  
[picture:835:e_transistor_wehr_geschlossen:Le canal de commande ferme complètement la vanne]
  
Au début, aucune eau ne s'écoule dans le petit canal. La vanne dans le grand canal est fermée, donc aucune eau ne s'écoule non plus.
  
[picture:837:e_transistor_wehr_halb_offen:Le canal de commande ouvre la vanne à moitié]

Ensuite, l'eau commence à s'écouler dans le petit canal, le canal de commande. L'eau soulève le clapet, qui à son tour actionne la vanne - l'eau commence également à s'écouler dans le canal principal.
  
[picture:836:e_transistor_wehr_geoeffnet:Le canal de commande ouvre complètement la vanne]

Maintenant, plus d'eau s'écoule dans le canal de commande, le clapet est soulevé plus loin, la vanne dans le canal principal s'ouvre complètement.
</tip>

[question:EC603]

Le courant d'émetteur $I_E$ est la somme du courant de collecteur et du courant de base:

$I_E = I_C + I_B$

[question:EC611]

Le point de fonctionnement en tension des transistors est généralement donné par la tension collecteur-émetteur:

$U_{CE} = U_{CB} + U_{BE}$

Outre les transistors bipolaires principalement traités ici, il existe surtout aussi des *transistors à effet de champ*, qui fonctionnent physiquement différemment, mais ont la même fonction de base (source de courant commandée par tension) vers l'extérieur. Sous forme de MOSFET, ils dominent notre électronique, car ils sont contenus des millions à des milliards de fois dans les circuits intégrés de l'électronique numérique.

<indepth>
MOSFET signifie *metal-oxide-semiconductor field effect transistor*, en allemand transistor à effet de champ métal-oxyde-semi-conducteur
</indepth>

[question:EC604]

Les transistors peuvent être utilisés non seulement comme amplificateurs, mais aussi comme interrupteurs (courant marche/arrêt) ou, pour de petites tensions à la sortie, comme résistance commandée. Cette dernière fonction est principalement mise en œuvre avec des transistors à effet de champ.

[question:EC601]
