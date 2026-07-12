Voyons de plus près le processus d'échantillonnage et rappelons-nous l'exemple précédent de la caméra qui prend des images d'une scène à intervalles réguliers. Supposons par exemple que notre caméra prend 24 images par seconde d'une scène donnée. Si l'on imagine par exemple que nous filmons un coureur en train de courir, on constatera qu'entre les différentes images, il y a toujours un mouvement saccadé des jambes et du corps de notre coureur par rapport à l'image précédente. Si l'on fait défiler les images rapidement, il en résulte une séquence de mouvement optiquement continue. L'information que nous captons à 24 images par seconde est cependant limitée dans le temps (notez : temporellement discret). Que se passerait-il si, entre deux images successives, une mouche passait rapidement devant l'objectif de notre caméra ? Pourrions-nous encore la percevoir ? Cela dépend de savoir si la mouche choisit le bon moment entre deux images pour traverser. Si elle arrivait dans le champ de vision de la caméra après la prise d'une image et l'avait déjà quitté avant la prise de l'image suivante, nous ne pourrions pas retracer cet événement dans les images que nous avons prises. Une information nous échapperait.

<webonly>
<margin>
[include:applet_nyquist]
</margin>
</webonly>

Il en va de même pour l'échantillonnage des signaux analogiques. Si ceux-ci sont capturés (échantillonnés) avec une certaine fréquence d'échantillonnage $f_\text{s}$, nous ne pourrons peut-être plus capturer les changements rapides du signal entre deux échantillons. L'échantillonnage signifie donc toujours une perte d'information temporelle. On peut alors se demander quelle résolution temporelle est nécessaire pour échantillonner un signal analogique d'une certaine fréquence (changement de l'amplitude du signal par seconde) sans perte d'information (tous les changements doivent être capturés). Pour cela, on peut faire la réflexion suivante. Pour pouvoir capturer sans erreur chaque changement du signal, il faut (comme dans notre exemple précédent avec la caméra) être en mesure de garantir qu'au moins avant et après chaque changement du signal, un échantillon est pris. Dans le cas de notre mouche qui traverse l'image, la condition préalable serait que la mouche ne doit pas voler si vite à travers l'image qu'elle est visible sur au moins 2 images. Sinon, on ne pourrait pas dire d'où elle a traversé l'image et dans quelle direction. Si cette condition n'est pas remplie, cette information nous échappe. On parle dans ce cas également du fait qu'une reconstruction sans erreur n'est pas possible.

On peut montrer mathématiquement que pour capturer un signal avec la fréquence la plus élevée $f_{\mathrm{max}}$ la fréquence d'échantillonnage $f_\text{s}$ doit être plus que le double, donc un peu plus que $f_\text{s} > 2 \cdot f_{\mathrm{max}}$, afin que nous puissions reconstruire notre signal sans erreur. Cette connaissance s'appelle également dans le traitement numérique du signal le théorème d'échantillonnage et est connu sous le nom de théorème d'échantillonnage de Nyquist-Shannon ou de condition de Nyquist, d'après ses découvreurs Nyquist et Shannon. Le théorème d'échantillonnage détermine donc la fréquence d'échantillonnage $f_\text{s}$ minimale théoriquement nécessaire pour une reconstruction sans erreur d'un signal.

[question:AF618]

[question:AF616]

---

Si le théorème n'est pas respecté, des effets d'aliasing, ou effets d'aliasing, se produisent. 

[question:AF617]

<webonly>
L'applet à côté permet d'expérimenter avec la fréquence d'échantillonnage. Si la fréquence d'échantillonnage tombe en dessous de $\qty{2}{\kilo\hertz}$, la condition de Nyquist n'est plus remplie, et le signal ne peut plus être reconstruit de manière univoque.
Il est également intéressant de noter que même avec une fréquence d'échantillonnage de exactement $\qty{2}{\kilo\hertz}$, la reconstruction ne fonctionne pas de manière fiable. C'est pourquoi on choisit généralement une fréquence d'échantillonnage légèrement supérieure à la condition de Nyquist pour garantir une reconstruction fiable du signal.
</webonly>

<indepth>
Prenons un exemple pratique comme celui d'un lecteur de CD qui fonctionne avec une fréquence d'échantillonnage de par exemple $\qty{44,1}{\kilo\sps}$. Si l'on applique le théorème d'échantillonnage comme décrit ci-dessus, cela signifie qu'avec une fréquence d'échantillonnage de $\qty{44,1}{\kilo\sps}$, seules les fréquences inférieures à $\qty{22,05}{\kilo\hertz}$ peuvent être représentées. Ainsi, les fréquences jusqu'à environ $\qty{22}{\kilo\hertz}$ peuvent encore être représentées correctement. Cela correspond à la bande de fréquences HiFi des bonnes installations stéréo. 
</indepth>

Avec la tâche suivante, vous pouvez tester vos connaissances sur le théorème d'échantillonnage.

[question:AF619]
