label avg24033(trans=fade_in):

$ play_music("ed7305.ogg")
scene avg_bg_051
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200130)]' (**arg(1, 1200130))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c7641') '[convertstrid(1200131)]' (**arg(2, 1200131))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200132)]' (**arg(3, 1200132))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
get_char('c7641') '[convertstrid(1200133)]' (**arg(4, 1200133))
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1200134)]' (**arg(5, 1200134))
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200135)]' (**arg(6, 1200135))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
get_char('c7641') '[convertstrid(1200136)]' (**arg(7, 1200136))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200137)]' (**arg(8, 1200137))
return "avg24033"