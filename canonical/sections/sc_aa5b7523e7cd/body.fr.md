<margin>
[picture:666:n_halbleiter_diode_merkhilfe:aide-mémoire diode]
</margin>

Pour convertir une tension alternative en tension continue, un redresseur est nécessaire. La forme la plus simple de redressement s'effectue à l'aide d'une diode. Comme nous l'avons déjà appris dans le chapitre [sec:diode_1], une diode ne laisse passer le courant que dans un seul sens.

---

Cette propriété de la diode est utilisée pour générer une tension continue à partir d'une tension alternative (voir figure [ref:e_einweggleichrichter_ue]). Si l'on branche une résistance de charge en série avec une diode sur une source de tension alternative (circuit représenté dans la figure [ref:e_einweggleichrichter]), la diode ne conduit que lorsque l'anode est positive par rapport à la cathode. Dans ce cas, la demi-onde positive de la tension alternative est transmise.

Pendant la demi-onde négative, la diode est bloquée, de sorte que la tension de sortie reste à zéro pendant cette période (voir figure [ref:e_einweggleichrichter_ul]). Comme ce circuit n'utilise qu'une demi-onde de la tension alternative sinusoïdale, on parle de *redressement mono-alternance*.

---
<margin>
[picture:797:e_einweggleichrichter:redresseur mono-alternance]
[picture:798:e_einweggleichrichter_ue:tension d'entrée redresseur mono-alternance]
[picture:796:e_einweggleichrichter_ul:tension de charge redresseur mono-alternance]
</margin>

[question:ED304]

Si l'on ajoute en parallèle à la résistance de charge un condensateur de capacité suffisante, celui-ci se charge rapidement à travers la diode pendant la demi-onde conductrice. Pendant la demi-onde suivante, où la diode est bloquée, le condensateur se décharge lentement à travers la résistance. Ainsi, la tension pulsatoire est lissée et se rapproche d'une tension continue.

Outre le redressement mono-alternance, il existe d'autres circuits redresseurs, par exemple le redresseur en pont. Cependant, nous aborderons ces variantes plus en détail dans le cours pour HB9, dans les chapitres [sec:gleichrichter_2] et [sec:brueckengleichrichter].