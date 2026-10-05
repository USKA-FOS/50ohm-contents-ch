Examinons maintenant le processus d'échantillonnage de plus près et rappelons-nous l'exemple mentionné dans la section [sec:digitale_signalverarbeitung_einleitung] de la caméra qui capture des images d'une scène à intervalles réguliers. Supposons par exemple que notre caméra capture 24 images par seconde d'une scène donnée. Si nous imaginons par exemple filmer un coureur en train de courir, nous constaterons qu'entre chaque image, il y a toujours un mouvement saccadé des jambes et du corps de notre coureur par rapport à l'image précédente. Si nous faisons défiler les images rapidement les unes après les autres, une séquence de mouvement optiquement continue se crée. Cependant, l'information que nous capturons à 24 images par seconde est limitée dans le temps (note : discrète dans le temps). Et si, entre deux images successives, une mouche passait soudainement rapidement devant l'objectif de notre caméra ? Pourrions-nous encore la percevoir ? Cela dépend si la mouche choisit le bon moment entre deux images pour son passage. Si elle n'entrait dans le champ de vision de la caméra qu'après la capture d'une image et l'avait déjà quitté avant la capture de l'image suivante, nous ne pourrions pas retracer cet événement dans les images que nous avons capturées. Cette information nous resterait cachée.

<webonly>
<margin>
[include:applet_nyquist]
</margin>
</webonly>

Il en va de même pour l'échantillonnage des signaux analogiques. S'ils sont capturés (échantillonnés) avec une certaine fréquence d'échantillonnage $f_\text{s}$, nous pourrions ne plus être en mesure de capturer les variations temporelles rapides du signal entre deux échantillons. L'échantillonnage implique donc toujours une perte d'information temporelle. On peut alors se demander quelle résolution temporelle est nécessaire pour échantillonner un signal analogique d'une certaine fréquence (changement de l'amplitude du signal par seconde) sans perte d'information (tous les changements doivent être capturés). Pour cela, on peut faire le raisonnement suivant. Pour pouvoir capturer au moins chaque changement du signal de manière fiable, il faut (comme dans notre exemple précédent avec la caméra) être capable de s'assurer qu'au moins un échantillon est pris avant et après chaque changement du signal. Dans le cas de notre mouche qui traverse l'image, la condition serait que la mouche ne puisse traverser l'image que suffisamment lentement pour être visible sur au moins 2 images. Sinon, on ne pourrait pas dire d'où elle a traversé l'image et dans quelle direction. Si cette condition n'est pas remplie, cette information nous échappe. Dans ce cas, on dit également qu'une reconstruction sans erreur n'est pas possible.

On peut démontrer mathématiquement que pour capturer un signal avec la fréquence maximale présente $f_{\mathrm{max}}$, la fréquence d'échantillonnage $f_\text{s}$ doit être plus du double, c'est-à-dire un peu plus que $f_\text{s} > 2 \cdot f_{\mathrm{max}}$, afin que nous puissions reconstruire notre signal de manière fiable. Cette constatation est appelée dans le traitement numérique du signal le théorème d'échantillonnage et, d'après ses découvreurs Nyquist et Shannon, est également connue sous le nom de théorème d'échantillonnage de Nyquist-Shannon ou condition de Nyquist. Le théorème d'échantillonnage détermine donc la fréquence d'échantillonnage minimale $f_\text{s}$ théoriquement nécessaire pour une reconstruction sans erreur d'un signal.

[question:AF618]

[question:AF616]

---

Si le théorème n'est pas respecté, des effets dits d'aliasing, ou effets de repliement, se produisent.

[question:AF617]

<webonly>
L'applet adjacente permet d'expérimenter avec la fréquence d'échantillonnage. Si la fréquence d'échantillonnage tombe en dessous de $\qty{2}{\kilo\hertz}$, la condition de Nyquist n'est plus remplie et le signal ne peut plus être reconstruit de manière unique.
Il est également intéressant de noter que même avec une fréquence d'échantillonnage exactement de $\qty{2}{\kilo\hertz}$, la reconstruction ne fonctionne pas de manière fiable. C'est pourquoi on choisit généralement une fréquence d'échantillonnage légèrement supérieure à la fréquence de Nyquist pour garantir une reconstruction sûre du signal.
</webonly>

<indepth>
Prenons un exemple pratique comme dans le cas d'un lecteur CD, qui fonctionne avec une fréquence d'échantillonnage de, par exemple, $\qty{44,1}{\kilo\sps}$. Si l'on se base sur le théorème d'échantillonnage comme décrit ci-dessus, cela signifie qu'avec une fréquence d'échantillonnage de $\qty{44,1}{\kilo\sps}$, seules les fréquences inférieures à $\qty{22,05}{\kilo\hertz}$ peuvent être représentées. Ainsi, les fréquences jusqu'à environ $\qty{22}{\kilo\hertz}$ peuvent encore être correctement représentées. Cela correspond à la bande de fréquences HiFi des bonnes chaînes stéréo.
</indepth>

Avec l'exercice suivant, tu peux tester tes connaissances sur le théorème d'échantillonnage.

[question:AF619]
