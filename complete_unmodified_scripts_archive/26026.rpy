label avg26026:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1215669)]' (**arg(1, 1215669))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215670)]' (**arg(2, 1215670))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215671)]' (**arg(3, 1215671))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215672)]' (**arg(4, 1215672))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215750)]' (**arg(5, 1215750))
get_char('c0') '[convertstrid(1215673)]' (**arg(6, 1215673))
get_char('c0') '[convertstrid(1215674)]' (**arg(7, 1215674))
return