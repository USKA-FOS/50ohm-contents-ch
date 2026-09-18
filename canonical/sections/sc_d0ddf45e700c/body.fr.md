Une méthode connue depuis des décennies connaît depuis quelque temps un regain d'intérêt dans le [radioamateurisme](Amateurfunk) : la *modulation polaire* [index:Polarmodulation].


Il n'existe aucune question d'examen sur ce sujet. Cependant, la modulation polaire est une méthode passionnante qui sera de plus en plus utilisée dans les équipements radioamateurs à l'avenir. C'est pourquoi elle est brièvement présentée ici, comme un regard au-delà du programme d'examen. Ceux qui souhaitent apprendre uniquement le contenu de l'examen peuvent sauter ce sujet sans problème.


La modulation polaire repose sur l'observation de ce qui se passe lorsque l'on zoome temporellement sur un signal quelconque de bande passante relativement étroite : l'onde individuelle ressemble alors à une onde sinusoïdale.


Cette onde sinusoïdale est définie par quelques paramètres, à savoir la [fréquence](Frequenz), la [phase](Phase) et l'[amplitude](Amplitude). La [fréquence](Frequenz) et la [phase](Phase) sont liées : si l'on commence avec une [fréquence](Frequenz) de base, mais que l'on décale la [phase](Phase) à chaque onde dans la même direction, on obtient une [fréquence](Frequenz) différente, décalée.


Ces considérations mènent à la *modulation polaire*. Cette méthode permet de générer des signaux de bande passante relativement étroite, par exemple des signaux BLU. Pour cela, il suffit de pouvoir contrôler simultanément l'[amplitude](Amplitude) et la [phase](Phase) du signal à partir d'une [fréquence](Frequenz) de base.


L'illustration [ref:polar_modulator] montre le [schéma bloc](Blockschaltbild) avec lequel cette idée est généralement mise en œuvre aujourd'hui. Les deux composantes du signal $I(t)$ et $Q(t)$ (décrites dans le chapitre précédent) sont converties en [amplitude](Amplitude) instantanée $A(t)$ et en [phase](Phase) instantanée $\varphi(t)$ :


$A(t)=\sqrt{I^2(t)+Q^2(t)}$


$\varphi(t)=\operatorname{atan2}\left(Q(t),I(t)\right)$


L'information de [phase](Phase) $\varphi(t)$ module ensuite une [porteuse](Träger) HF d'[amplitude](Amplitude) constante. Le signal résultant, toujours d'[amplitude](Amplitude) constante, contient déjà l'information de [phase](Phase) complète. Il peut être amplifié par un [étage final](Endstufe) particulièrement efficace, par exemple un amplificateur de classe E. En pratique, de tels étages finaux atteignent souvent un [rendement](Wirkungsgrad) supérieur à $\qtyrange{80}{90}{\percent}$.


Mais comment l'[amplitude](Amplitude) est-elle modulée ? Pour cela, la [tension d'alimentation](Versorgungsspannung) de l'étage final est manipulée en conséquence. L'information d'[amplitude](Amplitude) $A(t)$ est appliquée via un amplificateur d'enveloppe. Cela modifie l'[amplitude](Amplitude) de sortie selon l'[amplitude](Amplitude) requise à l'instant donné, ce qui donne l'enveloppe souhaitée. À la sortie, on obtient à nouveau le signal complet modulé en [amplitude](Amplitude) et en [phase](Phase) :


$s(t)=A(t)\cos\left(\omega_\mathrm{T}t+\varphi(t)\right)$


Pour que le signal reste aussi peu distordu que possible, les voies d'[amplitude](Amplitude) et de [phase](Phase) doivent être parfaitement synchronisées dans le temps.


Pour l'amplificateur d'enveloppe, un simple amplificateur BF lent suffit. La plage de [fréquences](Frequenzbereich) qu'il doit couvrir dépend de la bande passante du signal à générer. Pour maintenir un [rendement](Wirkungsgrad) élevé, on utilise généralement ici une technologie d'alimentation à découpage (amplificateur BF de classe D).


Grâce au [rendement](Wirkungsgrad) élevé, peu de puissance électrique est convertie en chaleur. Cela permet d'économiser de l'énergie, de réduire les besoins en refroidissement et de concevoir des équipements radio plus petits et plus légers, sans grands dissipateurs thermiques métalliques ni transistors d'étage final coûteux. La modulation polaire est particulièrement adaptée aux équipements QRP fonctionnant sur batterie, mais elle est également utilisée dans des émetteurs-récepteurs commerciaux plus performants.


<indepth>
Dans le [radioamateurisme](Amateurfunk), cette méthode a été utilisée dans les années 1970 sous le nom de "HELAPS" à bord du satellite AO-7. À l'époque, tout était réalisé avec des moyens analogiques. Aujourd'hui, les amplificateurs d'enveloppe et les étages finaux restent classiquement analogiques, tandis que le reste du traitement est assuré par des algorithmes SDR. Les CPU puissants, capables de gérer ces tâches sans problème, sont aujourd'hui moins chers qu'une pizza.
</indepth>


<margin>
[picture:1117:polar_modulator:Modulateur polaire]
</margin>
