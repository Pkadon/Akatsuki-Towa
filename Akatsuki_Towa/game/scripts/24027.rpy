label avg24027(trans=fade_in):

$ play_music("ed7117.ogg")
scene avg_bg_017
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1200109)]' (**arg(1, 1200109))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c9571') '[convertstrid(1200110)]' (**arg(2, 1200110))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200111)]' (**arg(3, 1200111))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200112)]' (**arg(4, 1200112))
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1200113)]' (**arg(5, 1200113))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200114)]' (**arg(6, 1200114))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c9571') '[convertstrid(1200115)]' (**arg(7, 1200115))
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200116)]' (**arg(8, 1200116))
return "avg24027"