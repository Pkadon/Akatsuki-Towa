label avg24071(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200279)]' (**arg(1, 1200279))
hide p2
$ update_portrait('st032_01 5', 'p1037', [mid(2), light], 6)
get_char('c10373') '[convertstrid(1200280)]' (**arg(2, 1200280))
hide p1037
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200281)]' (**arg(3, 1200281))
return "avg24071"