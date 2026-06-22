label avg26024:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1215656)]' (**arg(1, 1215656))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215657)]' (**arg(2, 1215657))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215658)]' (**arg(3, 1215658))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215659)]' (**arg(4, 1215659))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215660)]' (**arg(5, 1215660))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215661)]' (**arg(6, 1215661))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215749)]' (**arg(7, 1215749))
get_char('c0') '[convertstrid(1215662)]' (**arg(8, 1215662))
get_char('c0') '[convertstrid(1215663)]' (**arg(9, 1215663))
get_char('c0') '[convertstrid(1215664)]' (**arg(10, 1215664))
return