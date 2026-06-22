label avg26011:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 15', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1215566)]' (**arg(1, 1215566))
hide p1
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215567)]' (**arg(2, 1215567))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215568)]' (**arg(3, 1215568))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215755)]' (**arg(4, 1215755))
get_char('c0') '[convertstrid(1215569)]' (**arg(5, 1215569))
get_char('c0') '[convertstrid(1215570)]' (**arg(6, 1215570))
get_char('c0') '[convertstrid(1215571)]' (**arg(7, 1215571))
return