label avg26010:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1215560)]' (**arg(1, 1215560))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215561)]' (**arg(2, 1215561))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215562)]' (**arg(3, 1215562))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215563)]' (**arg(4, 1215563))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215742)]' (**arg(5, 1215742))
get_char('c0') '[convertstrid(1215564)]' (**arg(6, 1215564))
get_char('c0') '[convertstrid(1215565)]' (**arg(7, 1215565))
return