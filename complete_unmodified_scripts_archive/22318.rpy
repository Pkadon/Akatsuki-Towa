label avg22318(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1133325)]' (**arg(1, 1133325))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1133326)]' (**arg(2, 1133326))
hide p1
$ update_portrait('sc050_01 4', 'p57', [mid(-19), light], 6)
get_char('c573') '[convertstrid(1133327)]' (**arg(3, 1133327))
hide p57
get_char('c0') '[convertstrid(1133328)]' (**arg(4, 1133328))
return "avg22318"