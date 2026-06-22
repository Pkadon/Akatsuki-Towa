label avg26004:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1215518)]' (**arg(1, 1215518))
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215519)]' (**arg(2, 1215519))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215520)]' (**arg(3, 1215520))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215521)]' (**arg(4, 1215521))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215522)]' (**arg(5, 1215522))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215738)]' (**arg(6, 1215738))
get_char('c0') '[convertstrid(1215523)]' (**arg(7, 1215523))
get_char('c0') '[convertstrid(1215524)]' (**arg(8, 1215524))
return