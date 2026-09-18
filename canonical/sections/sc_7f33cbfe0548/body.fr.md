Examinons maintenant le processus d'échantillonnage de manière plus détaillée et rappelons-nous l'exemple précédent de l'appareil photo qui prend des images d'une scène à intervalles réguliers. Imaginons par exemple que notre appareil photo enregistre 24 images par seconde d'une scène donnée. Si l'on imagine que nous filmons un coureur en train de courir, nous constaterons qu'entre chaque image, il y a un mouvement saccadé des jambes et du corps du coureur par rapport à l'image précédente. Si nous faisons défiler les images rapidement les unes après les autres, nous obtenons une impression de mouvement continu. Cependant, les informations que nous capturons à 24 images par seconde sont limitées dans le temps (à noter : discrètes dans le temps). Que se passerait-il si une mouche traversait rapidement le champ de vision de notre appareil photo entre deux images consécutives ? Serions-nous encore en mesure de la percevoir ? Cela dépend du moment choisi par la mouche pour traverser le champ de vision. Si elle n'entre dans le champ de vision qu'après la prise d'une image et le quitte avant la prise de l'image suivante, cet événement ne sera pas visible sur les images enregistrées. Une partie de l'information nous échappera.

<webonly>
<margin>
[include:applet_nyquist]
</margin>
</webonly>

Il en va de même pour l'échantillonnage des signaux analogiques. Si ceux-ci sont capturés (échantillonnés) à une certaine fréquence d'échantillonnage $f_\text{s}$, nous risquons de ne plus pouvoir détecter les variations rapides du signal entre deux échantillons. L'échantillonnage implique donc toujours une perte d'information temporelle. On peut alors se demander quelle résolution temporelle est nécessaire pour échantillonner un signal analogique d'une certaine fréquence (changement d'amplitude du signal par seconde) sans perte d'information (tous les changements doivent être capturés). Pour cela, on peut faire la réflexion suivante : pour pouvoir détecter sans erreur chaque changement du signal, il faut, comme dans l'exemple précédent de l'appareil photo, s'assurer qu'un échantillon est pris avant et après chaque changement du signal. Dans le cas de notre mouche traversant l'image, cela signifie que la mouche ne doit pas voler si vite qu'elle n'apparaît que sur une seule image. Sinon, on ne pourrait pas déterminer d'où elle vient ni dans quelle direction elle se dirige. Si cette condition n'est pas remplie, cette information nous échappe. On parle alors d'une impossibilité de reconstruction sans erreur.

On peut démontrer mathématiquement que pour capturer un signal contenant la fréquence maximale $f_{\mathrm{max}}$, la fréquence d'échantillonnage $f_\text{s}$ doit être supérieure au double de cette fréquence, soit $f_\text{s} > 2 \cdot f_{\mathrm{max}}$, afin de pouvoir reconstruire le signal sans erreur. Cette découverte, connue sous le nom de théorème d'échantillonnage, est également appelée théorème de Nyquist-Shannon ou condition de Nyquist, d'après ses découvreurs Nyquist et Shannon. Le théorème d'échantillonnage détermine donc la fréquence d'échantillonnage minimale théorique nécessaire pour une reconstruction sans erreur d'un signal.

[question:AF618]

[question:AF616]

---

Si le théorème n'est pas respecté, des effets d'aliasing, ou repliement de spectre, se produisent.

[question:AF617]

<webonly>
L'applet ci-contre permet d'expérimenter avec la fréquence d'échantillonnage. Si celle-ci tombe en dessous de $\qty{2}{\kilo\hertz}$, la condition de Nyquist n'est plus respectée et le signal ne peut plus être reconstruit de manière univoque.

Il est également intéressant de noter que même avec une fréquence d'échantillonnage de exactement $\qty{2}{\kilo\hertz}$, la reconstruction ne fonctionne pas de manière fiable. C'est pourquoi on choisit généralement une fréquence d'échantillonnage légèrement supérieure à la condition de Nyquist afin de garantir une reconstruction du signal sûre.
</webonly>

<indepth>
Prenons un exemple concret, comme celui d'un lecteur de CD qui fonctionne avec une fréquence d'échantillonnage de $\qty{44,1}{\kilo\sps}$. Si l'on applique le théorème d'échantillonnage comme décrit ci-dessus, cela signifie qu'avec une fréquence d'échantillonnage de $\qty{44,1}{\kilo\sps}$, seules les fréquences inférieures à $\qty{22,05}{\kilo\hertz}$ peuvent être représentées. Ainsi, les fréquences jusqu'à environ $\qty{22}{\kilo\hertz}$ peuvent encore être correctement reproduites. Cela correspond à la plage de fréquences HiFi des bonnes chaînes stéréo.
</indepth>

Avec l'exercice suivant, vous pouvez tester vos connaissances sur le théorème d'échantillonnage.

[question:AF619]
