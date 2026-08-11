label avg26033(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215719)]' (**arg(1, 1215719))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215720)]' (**arg(2, 1215720))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215721)]' (**arg(3, 1215721))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215722)]' (**arg(4, 1215722))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215753)]' (**arg(5, 1215753))
get_char('c0') '[convertstrid(1215723)]' (**arg(6, 1215723))
get_char('c0') '[convertstrid(1215724)]' (**arg(7, 1215724))
get_char('c0') '[convertstrid(1215725)]' (**arg(8, 1215725))
return "avg26033"