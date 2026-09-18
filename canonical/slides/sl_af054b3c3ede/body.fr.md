### Pourquoi l’I/Q ?

* Les symboles peuvent différer par leur amplitude, leur fréquence ou leur phase.
* Pour représenter l’amplitude et la phase de manière claire, on utilise une représentation appelée *représentation I/Q*.
* Elle montre l’état du signal d’un symbole sous forme de point dans un plan.

--- style="font-size: 0.7em;"

<left>
[include:applet_iq_zeiger]
</left>
<right>
### Symbole représenté par un vecteur

* Longueur du vecteur : amplitude $A$
* Angle du vecteur : phase $\varphi$

* Le vecteur peut être décomposé en deux composantes :


$I=A\cdot\cos(\varphi)$


$Q=A\cdot\cos(\varphi-\qty{90}{\degree})=A\cdot\sin(\varphi)$


* Le diagramme de constellation montre l’état initial du vecteur pour chaque symbole.
</right>


---

[question:AF633]

---

### Diagramme de constellation

[picture:1060:a_konstellationsdiagramm:Diagramme de constellation]


---

### Diagramme de constellation

* Pour représenter les symboles, on ne considère pas la rotation continue de la porteuse.
* On considère plutôt l’état du signal associé à un symbole.
* Chaque état possible d’un symbole est représenté par un point dans le plan I/Q.
* Distance par rapport à l’origine : amplitude
* Angle par rapport à l’axe I : position de phase

---

### Pourquoi en avons-nous besoin ?

* Les diagrammes de constellation permettent de visualiser d’un seul coup d’œil les symboles possibles d’une méthode de transmission numérique.
* On peut voir si les symboles diffèrent par leur amplitude, leur phase ou les deux.
* Dans les sections suivantes, nous utiliserons cette représentation pour le *mapping*, la PSK et la QAM.