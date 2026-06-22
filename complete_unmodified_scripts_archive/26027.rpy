label avg26027:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1215675)]' (**arg(1, 1215675))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215676)]' (**arg(2, 1215676))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215677)]' (**arg(3, 1215677))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215678)]' (**arg(4, 1215678))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215679)]' (**arg(5, 1215679))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215680)]' (**arg(6, 1215680))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215751)]' (**arg(7, 1215751))
get_char('c0') '[convertstrid(1215681)]' (**arg(8, 1215681))
get_char('c0') '[convertstrid(1215682)]' (**arg(9, 1215682))
get_char('c0') '[convertstrid(1215683)]' (**arg(10, 1215683))
return