Lors du calcul de la puissance rayonnée efficace (ERP), seule l'énergie qui est effectivement fournie à l'antenne doit être prise en compte, c'est-à-dire que les pertes éventuelles dans les câbles peuvent être déduites avant de multiplier par le facteur de gain.

La puissance rayonnée efficace (ERP) d'une antenne se réfère au dipôle demi-onde. Dans le cas de la puissance rayonnée, seule l'énergie qui arrive effectivement à l'antenne est pertinente. En raison de l'atténuation du câble, etc., la puissance de l'émetteur ne peut pas être entièrement fournie à l'antenne dans le monde réel. Cette puissance perdue ne doit pas être prise en compte dans le calcul de la puissance rayonnée. Le gain d'antenne dans la direction préférentielle fait bien sûr partie du calcul. L'ERP est le produit de la puissance fournie et du gain d'antenne.

[question:AG501]

Dans la question suivante, il est absolument nécessaire de prêter attention aux signes de calcul. Les pertes sont soustraites de la puissance d'émission et ensuite multipliées par le facteur de gain ($G_{Antenne}$).
Puisque l'ERP doit être calculée, la référence doit être faite à un dipôle demi-onde.

[question:AG502]

---

Une indication sur la solution correcte est déjà donnée par le plan de fréquences pour le service radioamateur. Là, la puissance maximale pour la bande de $\qty{630}{\meter}$ est spécifiée à $\qty{1}{\watt}$ ERP.

Un dipôle demi-onde aurait une longueur de $\qty{315}{\meter}$. Cela n'est pas réalisable pour la plupart des radioamateurs. Par conséquent, des antennes fortement raccourcies sont utilisées. Les antennes raccourcies ont malheureusement un rendement inférieur à celui d'un dipôle demi-onde de longueur complète. Un "gain d'antenne" de $\qty{-20}{\dBd}$ n'est donc pas surprenant. Comme le câble coaxial est court, son atténuation peut être négligée dans cette bande de fréquences.

Pour résoudre la question AG503, on peut se référer au tableau des rapports de puissance dans le recueil de formules. Là, pour $\qty{-20}{\dB}$, le facteur $\num{0,01}$ est indiqué.

$\qty{50}{\watt}\cdot 0,01 = \qty{0,5}{\watt}$

La solution correcte est $\qty{0,5}{\watt}$.

%Un émetteur pour la bande de $\qty{630}{\meter}$ avec $\qty{50}{\watt}$ de puissance de sortie est connecté à une antenne avec $\qty{20}{\dBd}$ de perte au moyen d'un court câble coaxial. Quelle ERP est rayonnée par l'antenne?

[question:AG503]

<tip>
 Ce tableau est inclus dans le recueil de formules et est disponible pendant l'examen.
  
| r:   | r: rapport de puissance | r: rapport de tension |
| $\qty{-20}{\dB}$ | $\num{0,01}$ | $\num{0,1}$ |
| $\qty{-10}{\dB}$ | $\num{0,1}$ | $\num{0,32}$ |
| $\qty{-6}{\dB}$ | $\num{0,25}$ | $\num{0,5}$ |
| $\qty{-3}{\dB}$ | $\num{0,5}$ | $\num{0,71}$ |
| $\qty{-1}{\dB}$ | $\num{0,79}$ | $\num{0,89}$ |
| $\qty{0}{\dB}$ | $\num{1}$ | $\num{1}$ |
| $\qty{1}{\dB}$ | $\num{1,26}$ | $\num{1,12}$ |
| $\qty{3}{\dB}$ | $\num{2}$ | $\num{1,41}$ |
| $\qty{6}{\dB}$ | $\num{4}$ | $\num{2}$ |
| $\qty{10}{\dB}$ | $\num{10}$  | $\num{3,16}$ |
| $\qty{20}{\dB}$ | $\num{100}$ | $\num{10}$ |
[table:Pegel_Verhältnis:Rapports de puissance et de tension pour des valeurs d'atténuation et d'amplification importantes]

</tip>
