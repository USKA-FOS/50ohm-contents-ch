Avec une antenne artificielle de $\qty{50}{\ohm}$, le ROS à l'entrée de la ligne est d'environ $\num{1}$. Nous savons donc d'abord que la ligne elle-même est en bon état.

Avec l'antenne connectée, un ROS de $\num{3}$ est mesuré. Pour le ROS, avec la tension de l'onde incidente $U_\mathrm{V}$ et celle de l'onde réfléchie $U_\mathrm{R}$, on a :


$s=\frac{U_\mathrm{V}+U_\mathrm{R}}{U_\mathrm{V}-U_\mathrm{R}}.$


Pour $s=\num{3}$, il en résulte que la tension de l'onde réfléchie est la moitié de celle de l'onde incidente :


$\frac{U_\mathrm{R}}{U_\mathrm{V}}=\frac{3-1}{3+1}=\num{0,5}.$


Comme la puissance est proportionnelle au carré de la tension, la puissance réfléchie à l'entrée de la ligne est donc


$\num{0,5}^2=\num{0,25}$

de la puissance incidente. Sur les $\qty{10}{\watt}$ injectés, environ


$\qty{10}{\watt}\cdot\num{0,25}=\qty{2,5}{\watt}$

arrivent donc en tant que puissance réfléchie à l'entrée de la ligne.

La ligne présente une atténuation de $\qty{3}{\decibel}$ sur chaque trajet. Sur les $\qty{10}{\watt}$ injectés, seuls environ $\qty{5}{\watt}$ atteignent l'antenne. Sur le trajet de retour, la puissance réfléchie est à nouveau divisée par deux.


Pour que $\qty{2,5}{\watt}$ de puissance réfléchie arrivent à l'entrée de la ligne, environ $\qty{5}{\watt}$ doivent avoir été réfléchis à l'antenne. Cela correspond pratiquement à toute la puissance y parvenant.

L'antenne ne capte donc presque aucune puissance HF et est défectueuse.