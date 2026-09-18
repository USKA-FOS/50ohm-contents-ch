Dans la section précédente, nous avons vu que l'information dans un symbole peut être représentée, par exemple, par différentes amplitudes ou fréquences. Une autre possibilité consiste à modifier la phase d'un signal. Pour représenter clairement les états de signal avec différentes amplitudes et phases, on utilise souvent la *représentation I/Q*.


Considérons d'abord un état de signal à l'instant $t=0$. Pour le symbole, on définit une amplitude $A$ et une phase $\varphi$. Dans une représentation vectorielle, l'amplitude détermine la longueur du vecteur et la phase son angle par rapport à l'axe horizontal.


Le vecteur peut être décomposé en une composante horizontale et une composante verticale. La composante horizontale est appelée $I$ pour *In-Phase Component*, la composante verticale $Q$ pour *Quadrature Component*. Pour l'état de signal représenté, on a :


$I=A\cdot\cos(\varphi)$


$Q=A\cdot\cos(\varphi-\qty{90}{\degree})=A\cdot\sin(\varphi)$


Si le temps continue de s'écouler, le vecteur associé à l'oscillation tourne. Ses projections sur les deux axes évoluent de manière sinusoïdale et sont déphasées de $\qty{90}{\degree}$ l'une par rapport à l'autre. L'applet montre cette relation entre l'oscillation et sa représentation I/Q.


[include:applet_iq_zeiger]

[question:AF633]


On peut se représenter intuitivement que, au début de chaque intervalle de symbole, la valeur du symbole à transmettre détermine un point dans le plan I/Q et donc l'amplitude et la phase initiale de l'oscillation pour ce symbole. Pour le symbole suivant, on passe à l'état de signal correspondant au point suivant.


Pour la représentation des symboles, ce qui nous intéresse n'est donc pas la rotation continue du vecteur, mais l'état initial défini pour chaque symbole. Si l'on représente les états initiaux possibles sous forme de points dans le plan I/Q (cf. [ref:a_iq_ebene]), on parle de *diagramme de constellation* (cf. figure [ref:a_konstellationsdiagramm]). Chaque point correspond à un symbole possible. La distance d'un point par rapport à l'origine décrit l'amplitude du signal. Son angle par rapport à l'axe I décrit la phase.


<margin>
[picture:1060:a_iq_ebene:Plan I/Q avec un point de signal]
[picture:1059:a_konstellationsdiagramm:Diagramme de constellation avec 4 points de constellation]
</margin>

<indepth>
Pour les personnes intéressées par les mathématiques : une oscillation sinusoïdale peut également être décrite mathématiquement comme un *vecteur complexe* tournant avec la pulsation $\omega_\mathrm{c}$ :


$s(t) = \Re\left\{A \cdot e^{j(\omega_\mathrm{c}t+\varphi)}\right\} = A\cos(\omega_\mathrm{c}t+\varphi)$


Ici, $A$ décrit l'amplitude et $\varphi$ la phase initiale du signal. L'expression complexe peut être décomposée en deux parties :


$A \cdot e^{j(\omega_\mathrm{c}t+\varphi)} = \underbrace{A \cdot e^{j\varphi}}_{\text{Amplitude et phase}} \cdot \underbrace{e^{j\omega_\mathrm{c}t}}_{\text{Porteuse}}$


Dans un diagramme de constellation, c'est la première partie $A \cdot e^{j\varphi}$ qui nous intéresse. Elle décrit l'amplitude et la phase de l'état de signal. La rotation continue de la porteuse elle-même n'est pas représentée ici.
</indepth>


Cette représentation sera utilisée à plusieurs reprises dans les sections suivantes : elle permet de représenter clairement les symboles possibles des procédés de modulation numériques et, plus tard, de décrire l'attribution des combinaisons de bits à ces symboles.