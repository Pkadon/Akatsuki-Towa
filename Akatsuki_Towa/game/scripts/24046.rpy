label avg24046(trans=fade_in):

$ play_music("ed7301.ogg")
scene avg_bg_218
$ update_narrator('c7531')
window show
with trans
get_char('c7531') '[convertstrid(1200186)]' (**arg(1, 1200186))
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1200187)]' (**arg(2, 1200187))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1200188)]' (**arg(3, 1200188))
hide p1
$ update_narrator('c7531')
with fade
get_char('c7531') '[convertstrid(1200189)]' (**arg(4, 1200189))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200190)]' (**arg(5, 1200190))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
get_char('c7531') '[convertstrid(1200191)]' (**arg(6, 1200191))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200192)]' (**arg(7, 1200192))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
get_char('c7531') '[convertstrid(1200193)]' (**arg(8, 1200193))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200194)]' (**arg(9, 1200194))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200195)]' (**arg(10, 1200195))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c7531') '[convertstrid(1200196)]' (**arg(11, 1200196))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200197)]' (**arg(12, 1200197))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200198)]' (**arg(13, 1200198))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
get_char('c7531') '[convertstrid(1200199)]' (**arg(14, 1200199))
return "avg24046"