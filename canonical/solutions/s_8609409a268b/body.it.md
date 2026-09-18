Analizziamo passo dopo passo cosa fa il circuito con la potenza introdotta.

Innanzitutto, si nota un collegamento in parallelo di $\qty{110}{\ohm}$, $\qty{110}{\ohm}$ e due resistenze da $\qty{330}{\ohm}$. Sappiamo che in un sistema da $\qty{50}{\ohm}$ la resistenza d’ingresso deve essere anch’essa di $\qty{50}{\ohm}$. Se lo si desidera, è possibile verificarlo calcolando la rete resistiva.

Dalla raccolta di formule:

$\frac{1}{R} = \frac{1}{110} + \frac{1}{110} + \frac{1}{2 \cdot 330}$


Quindi $R = \frac{660}{13} \approx \qty{50}{\ohm}$


Se si introduce $\qty{1}{\watt}$ in questo collegamento in parallelo, si ottiene:


$U = \sqrt{P \cdot R} = \sqrt{1 \cdot 50} \approx \sqrt{49} \approx \qty{7}{\volt}$


Per il diodo conta solo la semionda positiva, quindi la tensione di picco:


$\hat{U} = U \cdot \sqrt{2} \approx \qty{10}{\volt}$


La tensione d’ingresso viene dimezzata dal partitore di tensione da $2 \cdot \qty{330}{\ohm}$ e poi ridotta di $U_F$:


$U_A = \frac{\hat{U}}{2} - U_F = \qty{5}{\volt} - \qty{0,23}{\volt} \approx \qty{4,8}{\volt}$