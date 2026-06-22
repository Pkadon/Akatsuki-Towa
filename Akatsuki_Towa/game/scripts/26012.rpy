label avg26012:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1215572)]' (**arg(1, 1215572))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215573)]' (**arg(2, 1215573))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215574)]' (**arg(3, 1215574))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215575)]' (**arg(4, 1215575))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215743)]' (**arg(5, 1215743))
get_char('c0') '[convertstrid(1215576)]' (**arg(6, 1215576))
get_char('c0') '[convertstrid(1215577)]' (**arg(7, 1215577))
get_char('c0') '[convertstrid(1215578)]' (**arg(8, 1215578))
get_char('c0') '[convertstrid(1215579)]' (**arg(9, 1215579))
return