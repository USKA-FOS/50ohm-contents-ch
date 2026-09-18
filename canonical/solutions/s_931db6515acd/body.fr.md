Dans une synthèse de fréquence à boucle à verrouillage de phase (PLL), la fréquence de sortie du VCO dans la branche de rétroaction est divisée par le diviseur *:n* puis comparée à la fréquence de référence au point A par le détecteur de phase $\varphi$.

Le circuit de régulation veille à ce que les deux fréquences d’entrée au détecteur de phase soient égales :


$f_A = \frac{f_{VCO}}{n}$


ou encore

$f_{VCO} = n \cdot f_A$


Le facteur de division *n* est réglé via les entrées B et C et est toujours un *nombre entier*. Si l’on augmente *n* de 1, la fréquence de sortie augmente exactement de $f_A$ :


$\Delta f_{VCO} = (n+1) \cdot f_A - n \cdot f_A = f_A$


Le plus petit pas de fréquence possible en sortie – c’est-à-dire l’*espacement des canaux* – correspond donc directement à la fréquence de référence au point A.


Comme un espacement des canaux de $\qty{12,5}{\kilo\hertz}$ est requis, la fréquence au point A doit également être de


$f_A = \qty{12,5}{\kilo\hertz}$.