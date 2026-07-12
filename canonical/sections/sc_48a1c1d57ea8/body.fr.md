%Pour calculer l'intensité du champ électrique d'une antenne dans le champ lointain ($d>\frac \lambda {2 \pi}$), il existe la formule d'approximation suivante :

%$E=\frac{\sqrt{\qty{30}{\ohm} \cdot P_\text{A} \cdot G_\text{i}}} {d}=\frac {\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}} d$

%avec la puissance à l'antenne $P_\text{A}$, le facteur de gain par rapport au rayonnement isotropique %$G_\text{i}$, et la distance $d$

%Pour le facteur de gain des antennes, on a :

%$G_\text{i}=G_\text{d} \cdot 1,64$ 

%ou bien

%$g_\text{i} = g_\text{d}+2,15\text{ dB}$

%Dans l'examen, la valeur limite pour la distance de protection des personnes est indiquée. Pour calculer la distance de protection des personnes, la formule doit donc être réarrangée en

%$d=\frac{\sqrt{\qty{30}{\ohm} \cdot P_\text{A} \cdot G_\text{i}}} {E}$

%Cependant, la puissance à l'antenne n'est généralement pas indiquée, et de même, le gain par rapport à un rayonnement isotropique non plus. Il faut donc tenir compte de ces facteurs. Cela donne alors :

%$d=\dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\text{Transceiver} \cdot G_\text{Kabel} \cdot G_\text{d} \cdot 1,64}} {E}$

%Avec la puissance à l'émetteur-récepteur $P_\text{Transceiver}$, le "gain" du câble $G_\text{Kabel}$ (ici, il faut insérer un signe négatif) et le gain par rapport au dipôle $G_\text{d}$.

%Le "gain" du câble peut être calculé, par exemple, pour un câble avec une atténuation de $2 \text{ dB}$ :
%$G_\text{Kabel} = 10^{\frac {-2 \text{ dB}} {10 \text{ dB}}} = 10^{-0,2}= 0,631$

% DD4UQ
Lors de l'affichage d'une installation fixe de radioamateur, les distances de sécurité peuvent être déterminées selon différentes procédures. L'une d'entre elles est le calcul du champ lointain. 
Pour le calcul, on a besoin de la puissance d'émission ($P_\text{S}$), du facteur de gain de l'antenne par rapport au rayonnement isotropique ($G_i = 1,64$) et de la valeur limite pour l'intensité du champ électrique $(E = \qty{28}{\volt\per\meter})$ dans le champ lointain d'une antenne. La longueur d’onde ($\qty{10}{\meter}$) n'est indiquée que pour déterminer le début du champ lointain.

$\begin{split} d &=\dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\text{A} \cdot G_\text{i}}}{E}\\ d &=\dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{100}{\watt} \cdot 1,64}}{\qty{28}{\volt\per\meter}}\\ d &\approx \qty{2,50}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

 $\begin{split}d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{10}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{1,59}{\meter}\end{split}$
 
 La distance de sécurité de $\qty{2,50}{\meter}$ se situe clairement dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK106]

La question AK108 ressemble à la question précédente. Ici, il faut en outre tenir compte de l'atténuation du câble. 

Il est ici judicieux de calculer d'abord l'EIRP.

$P_\text{EIRP} = P_S \cdot {10^\dfrac{g_d  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}$
Pour une antenne directionnelle, la valeur de $g_d$ doit être indiquée. Un dipôle simple n'a qu'un gain par rapport à un rayonnement isotropique. Ici, $g_d = \qty{0}{\dBd}$.
$\begin{split}P_\text{EIRP} &= \qty{300}{\watt}\cdot {10^\dfrac{\qty{0}{\dBd} −  \qty{0,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{300}{\watt}\cdot {10^\dfrac{\qty{1,65}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{300}{\watt}\cdot {10^{0,165}}\\ P_\text{EIRP} &\approx \qty{438,65}{\watt}\end{split}$

La distance de sécurité peut maintenant être calculée.

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{438,65}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{4,10}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

 $\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{20}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{3,18}{\meter}\end{split}$
 
 La distance de sécurité de $\qty{4,10}{\meter}$ se situe également ici dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK108]

On peut procéder de la même manière que pour la question précédente.
$\begin{split} P_\text{EIRP} &= P_S \cdot {10^\dfrac{g_d  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{700}{\watt}\cdot {10^\dfrac{\qty{0}{\dBd} −  \qty{0,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{700}{\watt}\cdot {10^\dfrac{\qty{1,65}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{700}{\watt}\cdot {10^{0,165}}\\ P_\text{EIRP} &\approx \qty{1023,52}{\watt}\end{split}$

$\begin{split} d & =\dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1023,52}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{6,26}{\meter}\end{split}$

[question:AK109]

Pour la question suivante, la distance de sécurité doit être calculée pour une antenne directionnelle. Le gain $g_d = \qty{11,5}{\dBd}$.

$\begin{split} P_\text{EIRP} &= P_S \cdot {10^\dfrac{g_d  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{75}{\watt}\cdot {10^\dfrac{\qty{11,5}{\dB} −  \qty{1,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{75}{\watt}\cdot {10^\dfrac{\qty{12,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{75}{\watt}\cdot {10^{1,215}}\\ P_\text{EIRP} &\approx \qty{1230,44}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1230,44}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{6,86}{\meter}\end{split}$

 La distance est-elle dans le champ lointain (champ proche rayonnant) ?

 $\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{2}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,32}{\meter}\end{split}$
 
 La distance de sécurité de $\qty{6,86}{\meter}$ se situe également ici dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK110]

La procédure est analogue à celle de la question précédente.

$\begin{split} P_\text{EIRP} &= P_S \cdot {10^\dfrac{g_d  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{100}{\watt}\cdot {10^\dfrac{\qty{10,5}{\dBd} −  \qty{1,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{100}{\watt}\cdot {10^\dfrac{\qty{11,15}{\dBd}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{100}{\watt}\cdot {10^{1,115}}\\ P_\text{EIRP} &\approx \qty{1303,17}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1303,17}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{7,1}{\meter}\end{split}$

La distance de sécurité de $\qty{7,1}{\meter}$ se situe également ici dans le champ lointain (champ proche rayonnant).

[question:AK111]

La bande des $\qty{13}{\centi\meter}$ va de $\qtyrange{2320}{2450}{\mega\hertz}$. Pour la bande de fréquences $\qtyrange{2000}{300000}{\mega\hertz}$, la valeur limite pour l'intensité du champ électrique est de $\qty{61}{\volt\per\meter}$.

$\begin{split} P_\text{EIRP} &= P_S \cdot {10^\dfrac{g_d  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{40}{\watt}\cdot {10^\dfrac{\qty{18}{\dBd} −  \qty{2}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{40}{\watt}\cdot {10^\dfrac{\qty{18,15}{\dB}}{\qty{10}{\dB}}}\\ P_\text{EIRP} &= \qty{40}{\watt}\cdot {10^{1,815}}\\ P_\text{EIRP} &\approx \qty{2612,52}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\text{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{2612,52}{\watt}}} {\qty{61}{\volt\per\meter}}\\ d &\approx \qty{4,6}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

$\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{0,13}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,02}{\meter}\end{split}$

La distance de sécurité de $\qty{4,6}{\meter}$ se situe clairement dans le champ lointain (champ proche rayonnant).

[question:AK112]

<indepth>
Pourquoi les questions de cette section font-elles référence aux procédés de modulation RTTY et FM ?
Lors de l'affichage d'une installation fixe de radioamateur (selon § 9, BEMFV), le facteur de conversion $\textrm{Faktor}_\textrm{FmodPers}$ doit être saisi lors de la configuration.
Avec le facteur, la puissance de crête indiquée (PEP) est convertie en puissance moyenne P. La puissance ainsi corrigée peut être utilisée dans la formule du champ lointain pour calculer la distance de sécurité de protection des personnes. 

RTTY et FM ont le facteur $\num{1}$, tout comme la plupart des procédés de modulation.
</indepth>