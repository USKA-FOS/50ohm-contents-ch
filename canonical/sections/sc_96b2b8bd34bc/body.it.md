Nel paragrafo precedente abbiamo visto che l’informazione in un simbolo può essere rappresentata, ad esempio, da ampiezze o frequenze diverse. Un’altra possibilità consiste nel modificare la fase di un segnale. Per rappresentare in modo chiaro gli stati del segnale con ampiezza e fase diverse, si utilizza spesso la cosiddetta *rappresentazione I/Q*.

Consideriamo inizialmente uno stato del segnale al tempo $t=0$. Per il simbolo vengono fissati un’ampiezza $A$ e una fase $\varphi$. In una rappresentazione vettoriale, l’ampiezza determina la lunghezza del vettore e la fase il suo angolo rispetto all’asse orizzontale.

Il vettore può essere scomposto in una componente orizzontale e una verticale. La componente orizzontale viene indicata come $I$ per *In-Phase Component*, mentre quella verticale come $Q$ per *Quadrature Component*. Per lo stato del segnale rappresentato vale:

$I=A\cdot\cos(\varphi)$

$Q=A\cdot\cos(\varphi-\qty{90}{\degree})=A\cdot\sin(\varphi)$

Se lasciamo scorrere il tempo, il vettore associato all’oscillazione ruota. Le sue proiezioni su entrambi gli assi seguono un andamento sinusoidale e sono sfasate tra loro di $\qty{90}{\degree}$. L’applet mostra questa relazione tra l’oscillazione e la sua rappresentazione I/Q.

[include:applet_iq_zeiger]

[question:AF633]

In modo intuitivo si può immaginare che all’inizio di ogni intervallo di simbolo, il valore del simbolo da trasmettere fissi un punto nel piano I/Q e quindi l’ampiezza e la fase iniziale dell’oscillazione per quel simbolo. Al simbolo successivo si passa allo stato del segnale del punto successivo.

Per la rappresentazione dei simboli, quindi, non ci interessa la rotazione continua del vettore, ma lo stato iniziale fissato per ogni simbolo. Se i possibili stati iniziali vengono rappresentati come punti nel piano I/Q (cfr. [ref:a_iq_ebene]), si parla di *diagramma di costellazione* (cfr. figura [ref:a_konstellationsdiagramm]). Ogni punto corrisponde a un possibile simbolo. La distanza di un punto dall’origine descrive l’ampiezza del segnale. Il suo angolo rispetto all’asse I descrive la fase.

<margin>
[picture:1060:a_iq_ebene:Piano I/Q con un punto di segnale]
[picture:1059:a_konstellationsdiagramm:Diagramma di costellazione con 4 punti di costellazione]
</margin>

<indepth>
Per chi è interessato alla matematica: un’oscillazione sinusoidale può essere descritta anche come un *vettore complesso* che ruota con la pulsazione $\omega_\mathrm{c}$:

$s(t) = \Re\left\{A \cdot e^{j(\omega_\mathrm{c}t+\varphi)}\right\} = A\cos(\omega_\mathrm{c}t+\varphi)$

Qui $A$ descrive l’ampiezza e $\varphi$ la fase iniziale del segnale. L’espressione complessa può essere scomposta in due parti:

$A \cdot e^{j(\omega_\mathrm{c}t+\varphi)} = \underbrace{A \cdot e^{j\varphi}}_{\text{Ampiezza e fase}} \cdot \underbrace{e^{j\omega_\mathrm{c}t}}_{\text{Portante}}$

In un diagramma di costellazione ci interessa la prima parte $A \cdot e^{j\varphi}$. Essa descrive ampiezza e fase dello stato del segnale. La rotazione continua della portante vera e propria non viene rappresentata.
</indepth>

Questa rappresentazione la utilizzeremo nei paragrafi successivi: con essa è possibile rappresentare in modo chiaro i possibili simboli dei metodi di modulazione digitale e, in seguito, descrivere anche l’assegnazione delle combinazioni di bit a questi simboli.