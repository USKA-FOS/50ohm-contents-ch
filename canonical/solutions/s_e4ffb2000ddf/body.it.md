Iniziamo considerando la resistenza d’ingresso del circuito. Nel radioamatore questa dovrebbe essere esattamente di $\qty{50}{\ohm}$. Quindi, in realtà, possiamo saltare questa parte del calcolo. Per completezza, mostriamo comunque che in questo caso si ottiene un totale di $\qty{50}{\ohm}$.

Il partitore di tensione formato dai due resistori da $\qty{330}{\ohm}$ ciascuno ha in totale:

$R_\mathrm{T}=\qty{330}{\ohm}+\qty{330}{\ohm}=\qty{660}{\ohm}$


Questo è in parallelo a $R_1=\qty{54,1}{\ohm}$:


$R_\mathrm{in}=R_1\parallel R_\mathrm{T}$


$R_\mathrm{in}=\frac{\qty{54,1}{\ohm}\cdot\qty{660}{\ohm}}{\qty{54,1}{\ohm}+\qty{660}{\ohm}}\approx\qty{50}{\ohm}$


Il circuito forma quindi approssimativamente un carico di $\qty{50}{\ohm}$.


All’uscita si misurano $\qty{14,9}{\volt}$ di tensione continua. A causa della tensione diretta del diodo al silicio di $\qty{0,7}{\volt}$, il valore di picco della HF alla giunzione del diodo deve essere maggiore di questa quantità:


$\hat U_\mathrm{D}=\qty{14,9}{\volt}+\qty{0,7}{\volt}=\qty{15,6}{\volt}$


Il diodo è collegato al punto centrale del partitore di tensione formato dai due resistori uguali da $\qty{330}{\ohm}$. Qui, quindi, è presente solo metà della tensione d’ingresso della HF. Il valore di picco all’ingresso è quindi:


$\hat U_\mathrm{in}=2\cdot\qty{15,6}{\volt}=\qty{31,2}{\volt}$


Per il calcolo della potenza ci serve il valore efficace:


$U_\mathrm{eff}=\frac{\hat U_\mathrm{in}}{\sqrt{2}}=\frac{\qty{31,2}{\volt}}{\sqrt{2}}\approx\qty{22,1}{\volt}$


Da ciò si ottiene la potenza della HF:


$P=\frac{U_\mathrm{eff}^2}{R_\mathrm{in}}=\frac{(\qty{22,1}{\volt})^2}{\qty{50}{\ohm}}\approx\qty{9,7}{\watt}$


La potenza d’ingresso della HF è quindi di circa $\qty{9,7}{\watt}$.