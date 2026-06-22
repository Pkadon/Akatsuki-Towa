label avg26003:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1215512)]' (**arg(1, 1215512))
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215513)]' (**arg(2, 1215513))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215514)]' (**arg(3, 1215514))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215737)]' (**arg(4, 1215737))
get_char('c0') '[convertstrid(1215515)]' (**arg(5, 1215515))
get_char('c0') '[convertstrid(1215516)]' (**arg(6, 1215516))
get_char('c0') '[convertstrid(1215517)]' (**arg(7, 1215517))
return