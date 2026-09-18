Al posto di un raddrizzatore a ponte, è possibile ottenere una raddrizzazione a doppia semionda utilizzando due diodi e un trasformatore con presa centrale.

<latexonly>
La figura [ref:a_vollweggleichrichter] mostra un tale cosiddetto raddrizzatore a doppia semionda. 

<margin>
[picture:946:a_vollweggleichrichter:Raddrizzamento a doppia semionda con due diodi]
</margin>
</latexonly>

<webonly>
L’applet qui accanto [ref:a_vollweggleichrichter] mostra un tale cosiddetto raddrizzatore a doppia semionda. 

<margin>
[include:applet_gleichrichter_1]
</margin>
</webonly>

---

Per comprendere il funzionamento, è necessario analizzare separatamente la semionda positiva e quella negativa. Quando sulla parte superiore dell’avvolgimento è presente una semionda positiva rispetto alla presa centrale sull’anodo del diodo $D_1$, solo questo diodo conduce e trasferisce la semionda all’uscita, indicata con il segno +. In questo momento, sul diodo $D_2$ è presente una semionda negativa all’anodo rispetto alla presa centrale. Questo diodo rimane bloccato durante questa semionda.

Nella semionda successiva, il diodo $D_1$ è bloccato e il diodo $D_2$ conduce, poiché in questo caso è presente una semionda positiva rispetto alla presa centrale del trasformatore. All’uscita della tensione continua compaiono ora due semionde, ma sempre in direzione positiva rispetto alla presa centrale. La presa centrale forma il polo negativo della tensione continua d’uscita.

<tip>
Stesso trucco mnemonico del raddrizzatore a ponte: i due catodi dei diodi sono collegati insieme al polo positivo della tensione d’uscita.
</tip>

[question:AD307]

Se due anodi sono collegati insieme a un polo d’uscita, in quel punto la tensione continua pulsante sarà negativa rispetto alla presa centrale del trasformatore. Entrambe le semionde si trovano al di sotto della linea dello zero.

[question:AD308]