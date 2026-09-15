label avg24074(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_074
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1200287)]' (**arg(1, 1200287))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 5', 'p1037', [l(2), light, flip], 6)
get_char('c10371') '[convertstrid(1200288)]' (**arg(2, 1200288))
hide p2
$ update_portrait('st032_01 5', 'p1037', [l(2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200289)]' (**arg(3, 1200289))
return "avg24074"