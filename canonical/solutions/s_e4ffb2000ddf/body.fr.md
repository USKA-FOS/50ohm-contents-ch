Commençons par examiner l'impédance d'entrée du circuit. Dans le cadre du radioamateurisme, celle-ci doit être exactement de $\qty{50}{\ohm}$. On peut donc sauter cette partie du calcul. Pour être complet, nous montrons tout de même qu'il en résulte ici un total de $\qty{50}{\ohm}$.

Le diviseur de tension constitué des deux résistances de $\qty{330}{\ohm}$ chacune donne au total :


$R_\mathrm{T}=\qty{330}{\ohm}+\qty{330}{\ohm}=\qty{660}{\ohm}$


Celui-ci est en parallèle avec $R_1=\qty{54,1}{\ohm}$ :


$R_\mathrm{in}=R_1\parallel R_\mathrm{T}$


$R_\mathrm{in}=\frac{\qty{54,1}{\ohm}\cdot\qty{660}{\ohm}}{\qty{54,1}{\ohm}+\qty{660}{\ohm}}\approx\qty{50}{\ohm}$


Le circuit forme ainsi approximativement une terminaison de $\qty{50}{\ohm}$.


À la sortie, une tension continue de $\qty{14,9}{\volt}$ est mesurée. En raison de la tension directe de la diode au silicium de $\qty{0,7}{\volt}$, la valeur de crête HF à l'entrée de la diode doit être supérieure de cette valeur :


$\hat U_\mathrm{D}=\qty{14,9}{\volt}+\qty{0,7}{\volt}=\qty{15,6}{\volt}$


La diode est connectée au point milieu du diviseur de tension constitué des deux résistances égales de $\qty{330}{\ohm}$. C'est pourquoi seule la moitié de la tension d'entrée HF y est présente. La valeur de crête à l'entrée est donc :


$\hat U_\mathrm{in}=2\cdot\qty{15,6}{\volt}=\qty{31,2}{\volt}$


Pour le calcul de la puissance, nous avons besoin de la valeur efficace :


$U_\mathrm{eff}=\frac{\hat U_\mathrm{in}}{\sqrt{2}}=\frac{\qty{31,2}{\volt}}{\sqrt{2}}\approx\qty{22,1}{\volt}$


Cela donne la puissance HF :


$P=\frac{U_\mathrm{eff}^2}{R_\mathrm{in}}=\frac{(\qty{22,1}{\volt})^2}{\qty{50}{\ohm}}\approx\qty{9,7}{\watt}$


La puissance d'entrée HF est donc d'environ $\qty{9,7}{\watt}$.